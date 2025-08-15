"""
BROski Dopamine Guardian
========================

This module implements the BROski “Dopamine Guardian”, a small agent designed to
keep morale high and protect against burnout for everyone inside the Hyperfocus
Zone.  It continuously watches user activity and mood, detects signs of
burnout or boredom, and celebrates legendary wins.  When a trigger is
detected it posts celebratory messages, GIFs and emojis to the configured
Discord channel and awards **BROski$** tokens to the deserving user.

Key features
------------

* **Discord bot integration:** Utilises `discord.py` to run a bot that listens
  for slash commands and posts messages in a chosen guild and channel.  It
  automatically welcomes new users, records daily mood check‑ins, logs
  achievements and broadcasts celebrations when appropriate.
* **WebSocket log listener:** Optionally connects to an external log stream
  (configured via `LOGS_WEBSOCKET_URL`) to receive real‑time events from
  other agents or services.  If a log message contains keywords such as
  “burnout”, “boredom” or “legendary win”, the guardian will react
  accordingly.
* **SQLite memory crystal:** Uses a lightweight SQLite database to store
  per‑user status, mood history, achievements and the current BROski$ balance.
* **Background health checks:** Periodically scans user records to detect
  prolonged inactivity or low mood.  When thresholds are breached, a
  gentle nudge or celebration is dispatched automatically.

Setup
-----

1. Install dependencies:

   ```bash
   pip install discord.py websockets aiosqlite
   ```

   The guardian will run in “mock mode” if `discord.py` is unavailable.

2. Create a Discord application and bot through the Discord developer portal,
   enable the `Message Content` intent and add the bot to your guild.  Then set
   the following environment variables:

   * `DISCORD_BOT_TOKEN` – the bot’s secret token.
   * `DISCORD_GUILD_ID` – the ID of the guild (server) where the bot
     operates.
   * `DISCORD_CHANNEL_NAME` – the name of the channel used for
     celebrations and announcements (defaults to **general**).
   * `LOGS_WEBSOCKET_URL` – (optional) a WebSocket endpoint that streams
     log events.  If unset the guardian will skip log listening.
   * `REWARD_AMOUNT` – number of BROski$ tokens to award for each
     celebration (defaults to 10).

3. Run the guardian:

   ```bash
   python -m AI.AGENT_DOPAMINE
   ```

   When the guardian starts it will open a WebSocket connection if
   `LOGS_WEBSOCKET_URL` is defined.  It will then log in to Discord (if
   available) and register slash commands.

Design notes
------------

This implementation follows the idioms found in the Hyperfocus empire code
base.  It embraces descriptive logging, emoji‑rich feedback and optional
integration with the broader Agent Orchestrator (see the separate
`FreshBROskiBot` for inspiration).  All external dependencies are optional
and gracefully degrade in testing environments.
"""

import asyncio
import json
import os
import random
import sqlite3
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional

try:
    import discord
    from discord import app_commands
    from discord.ext import commands, tasks  # tasks will be available in this branch
    DISCORD_AVAILABLE = True
except ImportError:
    # If discord.py isn't installed we run in a non‑interactive mode and
    # print messages to the console instead of sending them to Discord.
    DISCORD_AVAILABLE = False
    # Define dummy app_commands, commands and tasks to avoid NameErrors in type hints
    app_commands = None  # type: ignore
    commands = None  # type: ignore
    # Provide a dummy tasks.loop decorator that simply returns the function
    class _DummyTasks:
        def loop(self, *args: Any, **kwargs: Any):  # type: ignore[misc]
            def decorator(func):
                return func

            return decorator

    tasks = _DummyTasks()  # type: ignore

try:
    import websockets  # type: ignore
except ImportError:
    websockets = None  # type: ignore


class DopamineGuardian:
    """The heart of the BROski Dopamine Guardian.

    This class encapsulates all state, database access, Discord integration
    and log listening.  To start the guardian call :meth:`run`.
    """

    def __init__(self) -> None:
        # Environment configuration
        self.token: Optional[str] = os.getenv("DISCORD_BOT_TOKEN")
        self.guild_id: Optional[int] = (
            int(os.getenv("DISCORD_GUILD_ID")) if os.getenv("DISCORD_GUILD_ID") else None
        )
        self.channel_name: str = os.getenv("DISCORD_CHANNEL_NAME", "general")
        self.reward_amount: int = int(os.getenv("REWARD_AMOUNT", "10"))
        self.websocket_url: Optional[str] = os.getenv("LOGS_WEBSOCKET_URL")

        # Database path inside container; persisted in repo root for easy access
        self.db_path = os.getenv("DOPAMINE_DB_PATH", "/tmp/dopamine_guardian.db")
        self._ensure_database()

        # Discord bot objects
        if DISCORD_AVAILABLE and self.token and self.guild_id:
            intents = discord.Intents.default()
            intents.message_content = True
            intents.members = True
            # mypy may complain if commands is None, but commands is defined when DISCORD_AVAILABLE
            self.bot = commands.Bot(
                command_prefix="!dopamine ",  # type: ignore[arg-type]
                intents=intents,
                description="💥 BROski Dopamine Guardian – protecting your focus and mood!",
            )
            self._setup_events_and_commands()
        else:
            self.bot = None
            if DISCORD_AVAILABLE:
                print(
                    "⚠️ Discord bot not fully configured – set DISCORD_BOT_TOKEN and "
                    "DISCORD_GUILD_ID to enable interactive mode."
                )
            else:
                print("🔧 discord.py not available – running guardian in console mode.")

        # Periodic health check
        if DISCORD_AVAILABLE:
            # Start the background health check only if discord.py is available
            try:
                self.health_check.start()
            except Exception:
                # In test mode tasks may not support start()
                pass

    def _ensure_database(self) -> None:
        """Ensure that the SQLite database exists and has the necessary tables."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Table tracking per‑user status
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                discord_id TEXT PRIMARY KEY,
                username TEXT,
                last_active TIMESTAMP,
                last_mood INTEGER DEFAULT NULL,
                last_mood_time TIMESTAMP DEFAULT NULL,
                tokens INTEGER DEFAULT 0,
                achievements TEXT DEFAULT '[]'
            )
            """
        )

        # Table storing mood history (useful for analytics)
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS mood_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                discord_id TEXT,
                mood INTEGER,
                timestamp TIMESTAMP
            )
            """
        )

        # Table storing logged wins
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS wins (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                discord_id TEXT,
                description TEXT,
                timestamp TIMESTAMP
            )
            """
        )

        conn.commit()
        conn.close()

    # -------------------------------------------------------------------------
    # Database helpers
    # -------------------------------------------------------------------------
    def _get_user(self, discord_id: str) -> Optional[Dict[str, Any]]:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT discord_id, username, last_active, last_mood, last_mood_time, tokens, achievements FROM users WHERE discord_id = ?",
            (discord_id,),
        )
        row = cursor.fetchone()
        conn.close()
        if row:
            return {
                "discord_id": row[0],
                "username": row[1],
                "last_active": datetime.fromisoformat(row[2]) if row[2] else None,
                "last_mood": row[3],
                "last_mood_time": datetime.fromisoformat(row[4]) if row[4] else None,
                "tokens": row[5],
                "achievements": json.loads(row[6] or "[]"),
            }
        return None

    def _update_user(self, discord_id: str, **updates: Any) -> None:
        # Build SQL dynamically based on provided fields
        fields = []
        values = []
        for key, value in updates.items():
            fields.append(f"{key} = ?")
            # Serialise datetime and lists for SQLite
            if isinstance(value, datetime):
                values.append(value.isoformat())
            elif isinstance(value, list):
                values.append(json.dumps(value))
            else:
                values.append(value)
        values.append(discord_id)
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(f"UPDATE users SET {', '.join(fields)} WHERE discord_id = ?", values)
        conn.commit()
        conn.close()

    def _insert_user_if_missing(self, discord_id: str, username: str) -> None:
        if self._get_user(discord_id) is None:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO users (discord_id, username, last_active, tokens, achievements) VALUES (?, ?, ?, ?, ?)",
                (discord_id, username, datetime.utcnow().isoformat(), 0, json.dumps([])),
            )
            conn.commit()
            conn.close()

    # -------------------------------------------------------------------------
    # Discord integration
    # -------------------------------------------------------------------------
    def _setup_events_and_commands(self) -> None:
        if not self.bot:
            return

        @self.bot.event
        async def on_ready() -> None:
            assert self.bot  # for type checkers
            print(f"🎉 Dopamine Guardian connected as {self.bot.user}!")
            # Attempt to sync commands
            try:
                synced = await self.bot.tree.sync(guild=discord.Object(id=self.guild_id))
                print(f"🔄 Synced {len(synced)} commands")
            except Exception as e:
                print(f"⚠️ Failed to sync commands: {e}")

        @self.bot.event
        async def on_member_join(member: discord.Member) -> None:
            """Welcome new members and ensure they exist in the DB."""
            self._insert_user_if_missing(str(member.id), member.display_name)
            channel = self._find_channel(member.guild)
            if channel:
                await channel.send(
                    f"🌟 Welcome {member.mention} to the Hyperfocus Zone! Use `/checkin <mood>` to share how you're feeling."
                )

        # Slash command: /checkin mood (1‑10)
        @self.bot.tree.command(name="checkin", description="Record your current mood on a scale of 1–10")
        @app_commands.describe(mood="How do you feel right now? 1 = burnout, 10 = legendary")
        async def checkin(interaction: discord.Interaction, mood: app_commands.Range[int, 1, 10]) -> None:
            user_id = str(interaction.user.id)
            username = interaction.user.display_name
            self._insert_user_if_missing(user_id, username)
            # Save mood to DB
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO mood_history (discord_id, mood, timestamp) VALUES (?, ?, ?)",
                (user_id, mood, datetime.utcnow().isoformat()),
            )
            conn.commit()
            conn.close()
            # Update user's last mood and activity
            self._update_user(user_id, last_mood=mood, last_mood_time=datetime.utcnow(), last_active=datetime.utcnow())
            await interaction.response.send_message(
                f"📝 Mood recorded: {mood}/10. Thanks for checking in, {interaction.user.mention}!",
                ephemeral=True,
            )
            # Trigger evaluation immediately
            await self._evaluate_user(user_id)

        # Slash command: /win description
        @self.bot.tree.command(name="win", description="Log a legendary win or accomplishment")
        @app_commands.describe(description="Describe your achievement")
        async def win(interaction: discord.Interaction, description: str) -> None:
            user_id = str(interaction.user.id)
            username = interaction.user.display_name
            self._insert_user_if_missing(user_id, username)
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO wins (discord_id, description, timestamp) VALUES (?, ?, ?)",
                (user_id, description, datetime.utcnow().isoformat()),
            )
            conn.commit()
            conn.close()
            # Immediately celebrate the win
            await interaction.response.send_message(
                f"🏆 Legendary win recorded! {interaction.user.mention}: {description}",
                allowed_mentions=discord.AllowedMentions(users=True),
            )
            await self._celebrate(user_id, reason="legendary win")

        # Slash command: /status
        @self.bot.tree.command(name="status", description="View your current mood and BROski$ balance")
        async def status(interaction: discord.Interaction) -> None:
            user_id = str(interaction.user.id)
            user = self._get_user(user_id)
            if user:
                mood = user["last_mood"] or "N/A"
                tokens = user["tokens"]
                await interaction.response.send_message(
                    f"📈 Mood: {mood}/10\n💰 BROski$ Balance: {tokens}",
                    ephemeral=True,
                )
            else:
                await interaction.response.send_message(
                    "❌ You aren't registered yet. Use `/checkin` to get started.",
                    ephemeral=True,
                )

    # -------------------------------------------------------------------------
    # Helper functions
    # -------------------------------------------------------------------------
    def _find_channel(self, guild: Any) -> Optional[Any]:
        """
        Find the configured channel within a guild.

        `guild` is intentionally typed as `Any` because the `discord` module
        may not be available at runtime.  When running without Discord this
        function will never be called.
        """
        for channel in getattr(guild, "text_channels", []):
            if getattr(channel, "name", None) == self.channel_name:
                return channel
        # Fallback to the system channel or the first text channel if available
        sys_channel = getattr(guild, "system_channel", None)
        if sys_channel:
            return sys_channel
        text_channels = getattr(guild, "text_channels", [])
        return text_channels[0] if text_channels else None

    async def _evaluate_user(self, discord_id: str) -> None:
        """Examine a user's recent activity to detect triggers."""
        user = self._get_user(discord_id)
        if not user:
            return
        now = datetime.utcnow()
        # Burnout or boredom detection: no check‑ins for 48 hours or mood ≤ 3
        last_active: Optional[datetime] = user["last_active"]
        last_mood_time: Optional[datetime] = user["last_mood_time"]
        last_mood: Optional[int] = user["last_mood"]
        if (last_mood is not None and last_mood <= 3) or (
            last_mood_time and now - last_mood_time > timedelta(hours=48)
        ):
            await self._nudge(discord_id)

        # Legendary win detection handled separately via /win commands or log listener

    async def _nudge(self, discord_id: str) -> None:
        """Send a gentle nudge to a user experiencing burnout or boredom."""
        user = self._get_user(discord_id)
        if not user:
            return
        message = random.choice(
            [
                "🧘 Take a deep breath and stretch – you’ve got this!",
                "🌱 Remember to rest! Small breaks fuel big breakthroughs.",
                "💡 A quick walk can refresh your mind. Come back when you’re ready.",
            ]
        )
        if self.bot:
            guild = self.bot.get_guild(self.guild_id)  # type: ignore[arg-type]
            if guild:
                channel = self._find_channel(guild)
                if channel:
                    await channel.send(f"{user['username']} {message}")
        else:
            print(f"[NUDGE] {user['username']}: {message}")

    async def _celebrate(self, discord_id: str, reason: str) -> None:
        """Celebrate a user with a message, GIF/emoji and BROski$ reward."""
        user = self._get_user(discord_id)
        if not user:
            return
        # Update user tokens
        new_balance = user["tokens"] + self.reward_amount
        self._update_user(discord_id, tokens=new_balance)
        celebration_messages = [
            "🎉 Legendary vibes incoming!",
            "🚀 Ultra Mode: Activated!",
            "✨ You’re crushing it! Keep the momentum going!",
            "🏅 Epic win detected!",
        ]
        message = random.choice(celebration_messages)
        if self.bot:
            guild = self.bot.get_guild(self.guild_id)  # type: ignore[arg-type]
            if guild:
                channel = self._find_channel(guild)
                if channel:
                    embed = discord.Embed(
                        title=message,
                        description=(
                            f"{user['username']} just achieved a {reason}! "
                            f"You’ve been awarded {self.reward_amount} BROski$!"
                        ),
                        color=0xFFD700,
                    )
                    # Attach a random emoji or GIF link (extend this list with your own URLs)
                    gif_links = [
                        "https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.gif",
                        "https://media.giphy.com/media/l4FGuhL4U2WyjdkaY/giphy.gif",
                        "https://media.giphy.com/media/xT0Gqz6Yq8B8zEShLW/giphy.gif",
                    ]
                    embed.set_image(url=random.choice(gif_links))
                    await channel.send(
                        content=f"🎊 {user['username']} 🎊",
                        embed=embed,
                        allowed_mentions=discord.AllowedMentions(users=True),
                    )
        else:
            print(
                f"[CELEBRATION] {user['username']} triggered {reason}. "
                f"Awarded {self.reward_amount} BROski$. New balance: {new_balance}"
            )

    # -------------------------------------------------------------------------
    # Background tasks
    # -------------------------------------------------------------------------
    @tasks.loop(hours=2)
    async def health_check(self) -> None:
        """Periodic task to scan all users and detect burnout/boredom."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT discord_id FROM users")
        users = [row[0] for row in cursor.fetchall()]
        conn.close()
        for uid in users:
            await self._evaluate_user(uid)

    # Set up a before_loop handler only when discord.py is available.  When
    # running in console mode the dummy tasks.loop decorator does not provide
    # a `before_loop` attribute, so we guard its definition.
    if DISCORD_AVAILABLE:
        @health_check.before_loop  # type: ignore[misc]
        async def before_health_check(self) -> None:
            # Wait until bot is ready if running under Discord
            if self.bot:
                await self.bot.wait_until_ready()

    # -------------------------------------------------------------------------
    # WebSocket log listening
    # -------------------------------------------------------------------------
    async def listen_to_logs(self) -> None:
        """Listen to an external WebSocket for log events and react."""
        if not self.websocket_url or websockets is None:
            return
        while True:
            try:
                async with websockets.connect(self.websocket_url) as ws:  # type: ignore
                    async for message in ws:
                        await self._process_log_message(message)
            except Exception as e:
                print(f"⚠️ Log listener error: {e}. Retrying in 10s …")
                await asyncio.sleep(10)

    async def _process_log_message(self, message: str) -> None:
        """Parse a log message and fire relevant actions."""
        lower = message.lower()
        # Example log payloads might include user id and keyword
        # Format: {"event": "burnout", "discord_id": "123", ...}
        try:
            data = json.loads(message)
            event = data.get("event")
            uid = str(data.get("discord_id"))
        except Exception:
            # Fallback: simple keyword match
            event = None
            uid = None
        if not event:
            if "burnout" in lower or "boredom" in lower:
                # Without explicit user we can't nudge a specific person
                print(f"🪱 Detected burnout/boredom event in logs: {message}")
            if "legendary" in lower and "win" in lower:
                print(f"🌠 Detected legendary win in logs: {message}")
            return
        if event in ("burnout", "boredom") and uid:
            await self._nudge(uid)
        elif event == "win" and uid:
            await self._celebrate(uid, reason="legendary win via log")

    # -------------------------------------------------------------------------
    # Run entry point
    # -------------------------------------------------------------------------
    async def run_async(self) -> None:
        """Entry point for async execution."""
        # Launch WebSocket listener concurrently if configured
        log_task = None
        if self.websocket_url and websockets is not None:
            log_task = asyncio.create_task(self.listen_to_logs())

        if self.bot:
            await self.bot.start(self.token)  # type: ignore[arg-type]
        else:
            # If no Discord bot we keep the log listener alive
            if log_task:
                await log_task

    def run(self) -> None:
        """Synchronous wrapper around async entry point."""
        try:
            asyncio.run(self.run_async())
        except KeyboardInterrupt:
            if self.bot and DISCORD_AVAILABLE:
                asyncio.run(self.bot.close())


def main() -> None:
    guardian = DopamineGuardian()
    guardian.run()


if __name__ == "__main__":
    main()
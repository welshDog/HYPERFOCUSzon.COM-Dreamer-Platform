#!/usr/bin/env python3
"""
🤖💎⚡ LEGENDARY BROski DISCORD BOT LAUNCHER ⚡💎🤖

HyperFocus Zone Discord Lush - AUTO SUPERPOWERS ACTIVATED!
Following BROski Ultra LOOK-THEN-BUILD System Protocol

Features:
- 🚀 Auto-launching Discord bot with secure credentials
- 💎 BROski Economy Integration
- ⚡ HyperFocus Zone Community Commands
- 🧠 ADHD-Friendly Features
- 🌟 Memory Crystal System Integration
- 🔥 Real-time Empire Status Updates
"""

import os
import random
import sys
from datetime import datetime

import discord
from discord.ext import commands, tasks

# Add project root to path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from hyperfocus_security_config import HyperfocusSecurityConfig


class LegendaryBROskiBot:
    def __init__(self):
        """🚀 Initialize the LEGENDARY BROski Discord Bot"""
        self.security_config = HyperfocusSecurityConfig()
        self.logger = self.security_config._setup_logger()

        # 🔐 SECURE: Get credentials from environment
        self.bot_token = self.security_config.get_discord_token()

        if not self.bot_token:
            self.logger.error(
                "❌ Discord token not found! Please set DISCORD_BOT_TOKEN in your .env file"
            )
            sys.exit(1)

        # Discord bot setup with enhanced intents
        intents = discord.Intents.default()
        intents.message_content = True
        intents.guilds = True
        intents.members = True

        self.bot = commands.Bot(
            command_prefix=["!", "broski ", "🤖"], intents=intents, help_command=None
        )

        # 🌟 BROski Economy System
        self.broski_economy = {
            "global_balance": 15750,
            "daily_rewards": {},
            "achievements": [],
        }

        # 🧠 Memory Crystal Integration
        self.memory_crystals_count = 720

        self.setup_events()
        self.setup_commands()

    def setup_events(self):
        """🎯 Setup Discord bot events"""

        @self.bot.event
        async def on_ready():
            await self.on_bot_ready()

        @self.bot.event
        async def on_message(message):
            if message.author.bot:
                return

            # Process hyperfocus keywords
            await self.process_hyperfocus_triggers(message)
            await self.bot.process_commands(message)

    async def on_bot_ready(self):
        """🚀 Bot startup sequence"""
        self.logger.info(f"🎊 LEGENDARY BROski Bot is ALIVE!")
        self.logger.info(f"🌐 Connected to {len(self.bot.guilds)} guild(s)")
        self.logger.info(
            f"👥 Serving {sum(guild.member_count for guild in self.bot.guilds)} members"
        )

        # Set bot status
        activity = discord.Activity(
            type=discord.ActivityType.watching, name="HyperFocus Zone Empire 🏆"
        )
        await self.bot.change_presence(activity=activity)

        # Start background tasks
        if not self.empire_status_update.is_running():
            self.empire_status_update.start()

        # Send startup notification to console
        print(
            f"""
🌟💎⚡ LEGENDARY BROski DISCORD BOT - ACTIVATED! ⚡💎🌟

Bot Info:
├── 🤖 Name: {self.bot.user.name}
├── 🆔 ID: {self.bot.user.id}
├── 🌐 Guilds: {len(self.bot.guilds)}
├── 💎 BROski Economy: ${self.broski_economy['global_balance']:,}
├── 🧠 Memory Crystals: {self.memory_crystals_count}+
└── ⚡ Status: LEGENDARY TIER ACTIVATED

🎯 Commands Available:
├── !status - Empire health check
├── !broski - BROski economy info
├── !hyperfocus - Activate hyperfocus mode
├── !crystals - Memory crystal status
├── !help - Show all commands
└── !empire - Full empire overview

🚀 Ready to serve the HyperFocus Zone community!
        """
        )

    def setup_commands(self):
        """⚡ Setup all Discord bot commands"""

        @self.bot.command(name="status")
        async def empire_status(ctx):
            """🏆 Check HyperFocus Zone Empire status"""
            embed = discord.Embed(
                title="🏆 HyperFocus Zone Empire Status",
                description="Real-time empire health and performance metrics",
                color=0x00FF00,
            )

            embed.add_field(
                name="💎 BROski Economy",
                value=f"${self.broski_economy['global_balance']:,} active",
                inline=True,
            )
            embed.add_field(
                name="🧠 Memory Crystals",
                value=f"{self.memory_crystals_count}+ LEGENDARY",
                inline=True,
            )
            embed.add_field(
                name="⚡ Empire Health", value="100% PERFECTION", inline=True
            )

            embed.set_footer(
                text=f"Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            )
            await ctx.send(embed=embed)

        @self.bot.command(name="broski")
        async def broski_economy(ctx):
            """💰 BROski Economy status and rewards"""
            user_id = str(ctx.author.id)

            # Daily reward system
            today = datetime.now().strftime("%Y-%m-%d")
            if user_id not in self.broski_economy["daily_rewards"]:
                self.broski_economy["daily_rewards"][user_id] = today
                reward = random.randint(50, 200)

                embed = discord.Embed(
                    title="💰 BROski Daily Reward!",
                    description=f"🎉 You earned **{reward} BROski$**!",
                    color=0xFFD700,
                )
            else:
                embed = discord.Embed(
                    title="💎 BROski Economy Status",
                    description=f"Global Balance: **${self.broski_economy['global_balance']:,}**",
                    color=0x0099FF,
                )

            embed.add_field(
                name="🌟 Economy Features",
                value="• Daily rewards\n• Achievement bonuses\n• Community contributions\n• Empire building rewards",
                inline=False,
            )

            await ctx.send(embed=embed)

        @self.bot.command(name="hyperfocus")
        async def hyperfocus_mode(ctx):
            """🧠 Activate HyperFocus mode for ADHD optimization"""
            embed = discord.Embed(
                title="🧠⚡ HyperFocus Mode ACTIVATED!",
                description="ADHD-optimized productivity boost engaged",
                color=0xFF6B6B,
            )

            embed.add_field(
                name="🎯 Focus Techniques",
                value="• 25-min Pomodoro timer\n• Dopamine reward system\n• Progress tracking\n• Distraction blocking",
                inline=False,
            )

            embed.add_field(
                name="💡 Pro Tips",
                value="• Use `!timer 25` for focus sessions\n• Try `!rewards` for motivation\n• Join voice channels for body doubling",
                inline=False,
            )

            await ctx.send(embed=embed)

        @self.bot.command(name="crystals")
        async def memory_crystals(ctx):
            """🔮 Memory Crystal System status"""
            embed = discord.Embed(
                title="🔮💎 Memory Crystal Vault",
                description=f"LEGENDARY status achieved with {self.memory_crystals_count}+ crystals",
                color=0x9932CC,
            )

            embed.add_field(
                name="🌟 Crystal Categories",
                value="• Cosmic Mastery: 144+\n• Empire Optimization: 144+\n• Neurodivergent AI: 144+\n• Ultra Thinking: 144+\n• Performance Boost: 144+",
                inline=False,
            )

            await ctx.send(embed=embed)

        @self.bot.command(name="empire")
        async def full_empire_overview(ctx):
            """🌌 Complete HyperFocus Zone Empire overview"""
            embed = discord.Embed(
                title="🌌⚡ HyperFocus Zone Empire Overview ⚡🌌",
                description="Complete status of the LEGENDARY empire ecosystem",
                color=0x00FFFF,
            )

            embed.add_field(
                name="🏗️ Infrastructure",
                value="✅ Docker Stack\n✅ AI Integration\n✅ Security Hardened\n✅ Auto-Scaling",
                inline=True,
            )

            embed.add_field(
                name="🤖 AI Systems",
                value="✅ BROski COO\n✅ ADHD Coach\n✅ Memory Crystals\n✅ Auto-Optimization",
                inline=True,
            )

            embed.add_field(
                name="🌐 Community",
                value="✅ Discord Integration\n✅ Neurodivergent Focus\n✅ Accessibility First\n✅ Inclusive Design",
                inline=True,
            )

            await ctx.send(embed=embed)

        @self.bot.command(name="help")
        async def help_command(ctx):
            """❓ Show all available commands"""
            embed = discord.Embed(
                title="🤖 BROski Bot Commands",
                description="All available commands for the HyperFocus Zone",
                color=0xFFFFFF,
            )

            commands_list = """
**🏆 Empire Commands:**
`!status` - Empire health check
`!empire` - Full empire overview

**💰 Economy Commands:**
`!broski` - BROski economy status
`!rewards` - Daily rewards (coming soon)

**🧠 HyperFocus Commands:**
`!hyperfocus` - Activate focus mode
`!timer [minutes]` - Pomodoro timer (coming soon)

**🔮 Crystal Commands:**
`!crystals` - Memory crystal status
`!achievements` - View achievements (coming soon)

**❓ Utility Commands:**
`!help` - Show this help menu
`!ping` - Bot response time
            """

            embed.add_field(
                name="Available Commands", value=commands_list, inline=False
            )
            await ctx.send(embed=embed)

        @self.bot.command(name="ping")
        async def ping(ctx):
            """🏓 Check bot responsiveness"""
            latency = round(self.bot.latency * 1000)
            await ctx.send(f"🏓 Pong! **{latency}ms** | ⚡ BROski Bot is ALIVE!")

    async def process_hyperfocus_triggers(self, message):
        """🧠 Process HyperFocus keyword triggers"""
        content = message.content.lower()
        hyperfocus_keywords = [
            "focus",
            "adhd",
            "hyperfocus",
            "motivation",
            "productivity",
            "distracted",
            "overwhelmed",
        ]

        if any(keyword in content for keyword in hyperfocus_keywords):
            # React with supportive emojis
            await message.add_reaction("🧠")
            await message.add_reaction("⚡")
            await message.add_reaction("💎")

    @tasks.loop(minutes=30)
    async def empire_status_update(self):
        """🔄 Periodic empire status updates"""
        self.logger.info("🔄 Running periodic empire status check...")
        # Update memory crystal count, economy status, etc.

    def run(self):
        """🚀 Launch the LEGENDARY BROski Discord Bot"""
        self.logger.info("🚀 Launching LEGENDARY BROski Discord Bot...")

        try:
            self.bot.run(self.bot_token)
        except Exception as e:
            self.logger.error(f"❌ Bot startup failed: {e}")
            sys.exit(1)


if __name__ == "__main__":
    print(
        """
🌟💎⚡ LEGENDARY BROski DISCORD BOT LAUNCHER ⚡💎🌟

🚀 Initializing HyperFocus Zone Discord Lush...
🤖 Loading AUTO SUPERPOWERS...
💎 Connecting to BROski Economy System...
🧠 Activating ADHD-Friendly Features...

    """
    )

    # Create and launch the bot
    legendary_bot = LegendaryBROskiBot()
    legendary_bot.run()

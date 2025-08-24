#!/usr/bin/env python3
"""
🎨💎⚡ DISCORD UI ENHANCEMENT SUPERCHARGER ⚡💎🎨

LEGENDARY visual upgrade system using Discord's newest interactive components!
This enhances our existing Phase 2 engines with stunning modern UI.

DISCORD UI FEATURES:
🔘 Interactive Buttons & Action Rows
🎛️ Select Menus & Dropdowns
📝 Modal Forms & Input Fields
🎮 Discord Activities Integration
📊 Rich Embeds with Progress Bars
🎯 Component-Based Navigation
✨ Animated Status Updates
🌈 Dynamic Color Themes

Following Discord's Design Patterns: https://discord.com/developers/docs/activities/design-patterns
"""

from datetime import datetime
from enum import Enum
from typing import Dict

import discord
from discord import ButtonStyle, SelectOption, TextStyle


class UITheme(Enum):
    """🎨 Dynamic UI themes for different contexts"""

    HYPERFOCUS = {
        "primary": 0xFF6B35,
        "success": 0x00FF7F,
        "warning": 0xFFA500,
        "danger": 0xFF4444,
    }
    SOCIAL = {
        "primary": 0x7289DA,
        "success": 0x43B581,
        "warning": 0xFAA61A,
        "danger": 0xF04747,
    }
    GAMIFICATION = {
        "primary": 0x9370DB,
        "success": 0x32CD32,
        "warning": 0xFFD700,
        "danger": 0xDC143C,
    }
    ML_INSIGHTS = {
        "primary": 0x00CED1,
        "success": 0x90EE90,
        "warning": 0xF0E68C,
        "danger": 0xFA8072,
    }


class ProgressBar:
    """📊 Beautiful ASCII progress bars for Discord"""

    @staticmethod
    def create(
        current: int, maximum: int, length: int = 20, style: str = "hyperfocus"
    ) -> str:
        if maximum == 0:
            percentage = 0
        else:
            percentage = min(100, (current / maximum) * 100)

        filled = int((percentage / 100) * length)
        empty = length - filled

        # Different styles for different contexts
        styles = {
            "hyperfocus": {"fill": "🟦", "empty": "⬜", "ends": ["🔵", "🔘"]},
            "social": {"fill": "🟩", "empty": "⬜", "ends": ["🤝", "👥"]},
            "gamification": {"fill": "🟪", "empty": "⬜", "ends": ["🏆", "⭐"]},
            "challenge": {"fill": "🟨", "empty": "⬜", "ends": ["🎯", "🏁"]},
            "fire": {"fill": "🔥", "empty": "💨", "ends": ["⚡", "✨"]},
        }

        chosen_style = styles.get(style, styles["hyperfocus"])
        bar = chosen_style["fill"] * filled + chosen_style["empty"] * empty

        return f"{chosen_style['ends'][0]} {bar} {chosen_style['ends'][1]} **{percentage:.0f}%**"


class ChallengeJoinView(discord.ui.View):
    """🎯 Interactive challenge joining interface"""

    def __init__(self, social_engine, challenge_id: str, challenge_data: Dict):
        super().__init__(timeout=300)
        self.social_engine = social_engine
        self.challenge_id = challenge_id
        self.challenge_data = challenge_data

        # Add dynamic buttons based on challenge state
        self.update_buttons()

    def update_buttons(self):
        """🔄 Update buttons based on current challenge state"""
        self.clear_items()

        participants = len(self.challenge_data.get("participants", []))
        max_participants = self.social_engine.challenges[self.challenge_data["type"]][
            "max_participants"
        ]

        # Join button
        if (
            participants < max_participants
            and self.challenge_data["status"] == "recruiting"
        ):
            join_button = discord.ui.Button(
                label=f"🚀 Join Challenge ({participants}/{max_participants})",
                style=ButtonStyle.primary,
                emoji="🎯",
                custom_id=f"join_{self.challenge_id}",
            )
            join_button.callback = self.join_challenge
            self.add_item(join_button)

        # Challenge info button
        info_button = discord.ui.Button(
            label="📋 Challenge Info",
            style=ButtonStyle.secondary,
            emoji="ℹ️",
            custom_id=f"info_{self.challenge_id}",
        )
        info_button.callback = self.show_info
        self.add_item(info_button)

        # Start button (for creator only)
        if self.challenge_data["status"] == "recruiting":
            start_button = discord.ui.Button(
                label="⚡ Force Start",
                style=ButtonStyle.success,
                emoji="🏁",
                custom_id=f"start_{self.challenge_id}",
            )
            start_button.callback = self.force_start
            self.add_item(start_button)

    async def join_challenge(self, interaction: discord.Interaction):
        """🎯 Handle challenge join"""
        user_id = str(interaction.user.id)
        success = await self.social_engine.join_challenge(self.challenge_id, user_id)

        if success:
            # Update challenge data
            self.challenge_data = self.social_engine.active_challenges[
                self.challenge_id
            ]
            self.update_buttons()

            # Create success embed
            embed = discord.Embed(
                title="🎉 CHALLENGE JOINED!",
                description=f"**{interaction.user.mention}** joined the challenge!",
                color=UITheme.SOCIAL.value["success"],
            )

            participants = len(self.challenge_data["participants"])
            min_needed = self.social_engine.challenges[self.challenge_data["type"]][
                "min_participants"
            ]

            if (
                participants >= min_needed
                and self.challenge_data["status"] == "recruiting"
            ):
                await self.social_engine.start_challenge(self.challenge_id)
                embed.add_field(
                    name="🚀 CHALLENGE STARTED!",
                    value="The challenge is now active! Good luck everyone!",
                    inline=False,
                )

            # Show progress bar
            max_participants = self.social_engine.challenges[
                self.challenge_data["type"]
            ]["max_participants"]
            progress = ProgressBar.create(
                participants, max_participants, style="challenge"
            )
            embed.add_field(name="👥 Participants", value=progress, inline=False)

            await interaction.response.edit_message(embed=embed, view=self)
        else:
            await interaction.response.send_message(
                "❌ Could not join challenge. It may be full or you're already in it!",
                ephemeral=True,
            )

    async def show_info(self, interaction: discord.Interaction):
        """📋 Show detailed challenge info"""
        challenge_template = self.social_engine.challenges[self.challenge_data["type"]]

        embed = discord.Embed(
            title=f"📋 {challenge_template['name']} - DETAILS",
            description=challenge_template["description"],
            color=UITheme.GAMIFICATION.value["primary"],
        )

        # Requirements with progress bars
        requirements_text = ""
        for req, val in challenge_template["requirements"].items():
            requirements_text += f"• **{req.replace('_', ' ').title()}**: {val}\n"

        embed.add_field(name="🎯 Requirements", value=requirements_text, inline=True)

        # Rewards
        rewards_text = ""
        for reward, points in challenge_template["rewards"].items():
            rewards_text += (
                f"• **{reward.replace('_', ' ').title()}**: {points:,} pts\n"
            )

        embed.add_field(name="🏆 Rewards", value=rewards_text, inline=True)

        # Participants
        participants = self.challenge_data.get("participants", [])
        if participants:
            participant_list = "\n".join([f"• <@{pid}>" for pid in participants[:10]])
            if len(participants) > 10:
                participant_list += f"\n... and {len(participants) - 10} more!"
            embed.add_field(
                name="👥 Current Participants", value=participant_list, inline=False
            )

        await interaction.response.send_message(embed=embed, ephemeral=True)

    async def force_start(self, interaction: discord.Interaction):
        """⚡ Force start challenge (creator only)"""
        if str(interaction.user.id) != self.challenge_data["creator"]:
            await interaction.response.send_message(
                "❌ Only the challenge creator can force start!", ephemeral=True
            )
            return

        success = await self.social_engine.start_challenge(self.challenge_id)
        if success:
            embed = discord.Embed(
                title="🚀 CHALLENGE FORCE STARTED!",
                description="The challenge is now active!",
                color=UITheme.SOCIAL.value["success"],
            )
            self.update_buttons()
            await interaction.response.edit_message(embed=embed, view=self)
        else:
            await interaction.response.send_message(
                "❌ Could not start challenge!", ephemeral=True
            )


class ChallengeCreateModal(discord.ui.Modal):
    """📝 Modal form for creating custom challenges"""

    def __init__(self, social_engine):
        super().__init__(title="🎯 Create Custom Challenge")
        self.social_engine = social_engine

        # Challenge name
        self.name = discord.ui.TextInput(
            label="Challenge Name",
            placeholder="Enter a catchy challenge name...",
            max_length=50,
            style=TextStyle.short,
        )
        self.add_item(self.name)

        # Description
        self.description = discord.ui.TextInput(
            label="Description",
            placeholder="Describe your challenge...",
            max_length=200,
            style=TextStyle.paragraph,
        )
        self.add_item(self.description)

        # Duration
        self.duration = discord.ui.TextInput(
            label="Duration (minutes)",
            placeholder="e.g. 1440 for 24 hours",
            max_length=10,
            style=TextStyle.short,
        )
        self.add_item(self.duration)

    async def on_submit(self, interaction: discord.Interaction):
        """✅ Handle challenge creation"""
        try:
            duration_mins = int(self.duration.value)
            user_id = str(interaction.user.id)

            # Create custom challenge
            challenge_id = f"custom_{int(datetime.now().timestamp())}"

            self.social_engine.active_challenges[challenge_id] = {
                "type": "custom",
                "creator": user_id,
                "participants": [user_id],
                "status": "recruiting",
                "created_at": datetime.now().isoformat(),
                "start_time": None,
                "end_time": None,
                "progress": {user_id: {"joined_at": datetime.now().isoformat()}},
                "custom_data": {
                    "name": self.name.value,
                    "description": self.description.value,
                    "duration": duration_mins,
                },
            }

            embed = discord.Embed(
                title="🎯 CUSTOM CHALLENGE CREATED!",
                description=f"**{self.name.value}** is now recruiting!",
                color=UITheme.GAMIFICATION.value["primary"],
            )

            embed.add_field(
                name="📋 Challenge Details",
                value=f"{self.description.value}\n**Duration**: {duration_mins} minutes\n**Creator**: {interaction.user.mention}",
                inline=False,
            )

            embed.add_field(
                name="🚀 Ready to Start",
                value="Use the buttons below to join or get more info!",
                inline=False,
            )

            # Create challenge data for view
            challenge_data = self.social_engine.active_challenges[challenge_id]
            view = ChallengeJoinView(self.social_engine, challenge_id, challenge_data)

            await interaction.response.send_message(embed=embed, view=view)

        except ValueError:
            await interaction.response.send_message(
                "❌ Please enter a valid number for duration!", ephemeral=True
            )


class ChallengeSelectView(discord.ui.View):
    """🎛️ Select menu for choosing challenge types"""

    def __init__(self, social_engine):
        super().__init__(timeout=60)
        self.social_engine = social_engine

        # Create select menu with challenge options
        options = []
        for challenge_type, challenge_data in social_engine.challenges.items():
            options.append(
                SelectOption(
                    label=challenge_data["name"],
                    description=challenge_data["description"][:50] + "...",
                    value=challenge_type,
                    emoji="🎯",
                )
            )

        # Add custom challenge option
        options.append(
            SelectOption(
                label="🎨 Custom Challenge",
                description="Create your own unique challenge",
                value="custom",
                emoji="⚡",
            )
        )

        select = discord.ui.Select(
            placeholder="🎯 Choose a challenge type...",
            options=options[:25],  # Discord limit
            custom_id="challenge_select",
        )
        select.callback = self.challenge_selected
        self.add_item(select)

    async def challenge_selected(self, interaction: discord.Interaction):
        """🎯 Handle challenge type selection"""
        selected_type = interaction.data["values"][0]
        user_id = str(interaction.user.id)

        if selected_type == "custom":
            # Show custom challenge modal
            modal = ChallengeCreateModal(self.social_engine)
            await interaction.response.send_modal(modal)
        else:
            # Create standard challenge
            challenge_id = await self.social_engine.create_challenge(
                selected_type, user_id
            )
            challenge_data = self.social_engine.active_challenges[challenge_id]
            challenge_template = self.social_engine.challenges[selected_type]

            embed = discord.Embed(
                title="🎯 CHALLENGE CREATED!",
                description=f"**{challenge_template['name']}** is now recruiting!",
                color=UITheme.SOCIAL.value["primary"],
            )

            embed.add_field(
                name="📋 Challenge Info",
                value=f"{challenge_template['description']}\n**Duration**: {challenge_template['duration']} minutes\n**Players**: {challenge_template['min_participants']}-{challenge_template['max_participants']}",
                inline=False,
            )

            # Requirements with emojis
            req_text = ""
            req_emojis = {
                "focus_sessions": "🎯",
                "mutual_support": "🤝",
                "check_ins": "✅",
                "team_sessions": "👥",
            }
            for req, val in challenge_template["requirements"].items():
                emoji = req_emojis.get(req, "📋")
                req_text += f"{emoji} **{req.replace('_', ' ').title()}**: {val}\n"

            embed.add_field(name="🎯 Requirements", value=req_text, inline=True)

            # Rewards with emojis
            reward_text = ""
            reward_emojis = {
                "completion": "🏁",
                "perfect_sync": "💎",
                "streak_bonus": "🔥",
                "team_victory": "🏆",
            }
            for reward, val in challenge_template["rewards"].items():
                emoji = reward_emojis.get(reward, "⭐")
                reward_text += (
                    f"{emoji} **{reward.replace('_', ' ').title()}**: {val:,} pts\n"
                )

            embed.add_field(name="🏆 Rewards", value=reward_text, inline=True)

            # Create interactive view
            view = ChallengeJoinView(self.social_engine, challenge_id, challenge_data)

            await interaction.response.edit_message(embed=embed, view=view)


class FocusSessionControls(discord.ui.View):
    """🎯 Interactive focus session controls"""

    def __init__(self, session_id: str, session_data: Dict):
        super().__init__(timeout=None)  # Persistent view
        self.session_id = session_id
        self.session_data = session_data
        self.is_paused = False
        self.start_time = datetime.now()

        self.update_buttons()

    def update_buttons(self):
        """🔄 Update control buttons"""
        self.clear_items()

        # Pause/Resume button
        if self.is_paused:
            pause_button = discord.ui.Button(
                label="▶️ Resume",
                style=ButtonStyle.success,
                emoji="▶️",
                custom_id="resume_session",
            )
            pause_button.callback = self.resume_session
        else:
            pause_button = discord.ui.Button(
                label="⏸️ Pause",
                style=ButtonStyle.secondary,
                emoji="⏸️",
                custom_id="pause_session",
            )
            pause_button.callback = self.pause_session

        self.add_item(pause_button)

        # Complete button
        complete_button = discord.ui.Button(
            label="✅ Complete Session",
            style=ButtonStyle.primary,
            emoji="🏁",
            custom_id="complete_session",
        )
        complete_button.callback = self.complete_session
        self.add_item(complete_button)

        # Extend button
        extend_button = discord.ui.Button(
            label="⏰ +5 min",
            style=ButtonStyle.secondary,
            emoji="➕",
            custom_id="extend_session",
        )
        extend_button.callback = self.extend_session
        self.add_item(extend_button)

        # Progress check
        progress_button = discord.ui.Button(
            label="📊 Progress",
            style=ButtonStyle.secondary,
            emoji="📈",
            custom_id="check_progress",
        )
        progress_button.callback = self.check_progress
        self.add_item(progress_button)

    async def pause_session(self, interaction: discord.Interaction):
        """⏸️ Pause the session"""
        self.is_paused = True
        self.update_buttons()

        embed = discord.Embed(
            title="⏸️ SESSION PAUSED",
            description="Your focus session is paused. Take a breath!",
            color=UITheme.HYPERFOCUS.value["warning"],
        )

        embed.add_field(
            name="💡 Pause Tips",
            value="• Stand up and stretch\n• Hydrate\n• Quick mindfulness moment\n• Ready to resume when you are!",
            inline=False,
        )

        await interaction.response.edit_message(embed=embed, view=self)

    async def resume_session(self, interaction: discord.Interaction):
        """▶️ Resume the session"""
        self.is_paused = False
        self.update_buttons()

        embed = discord.Embed(
            title="▶️ SESSION RESUMED",
            description="Back to hyperfocus mode! You've got this! 🚀",
            color=UITheme.HYPERFOCUS.value["success"],
        )

        await interaction.response.edit_message(embed=embed, view=self)

    async def complete_session(self, interaction: discord.Interaction):
        """✅ Complete the session"""
        end_time = datetime.now()
        duration = (end_time - self.start_time).total_seconds() / 60

        embed = discord.Embed(
            title="🎉 SESSION COMPLETED!",
            description=f"Amazing work! You focused for **{duration:.1f} minutes**!",
            color=UITheme.HYPERFOCUS.value["success"],
        )

        # Calculate achievements
        achievements = []
        if duration >= 25:
            achievements.append("🍅 Pomodoro Master")
        if duration >= 60:
            achievements.append("🏆 Deep Focus Champion")
        if not self.is_paused:
            achievements.append("💎 Unbroken Concentration")

        if achievements:
            embed.add_field(
                name="🏆 Achievements Unlocked",
                value="\n".join(achievements),
                inline=False,
            )

        # Progress bar for session completion
        target_duration = self.session_data.get("duration", 25)
        progress = ProgressBar.create(
            int(duration), target_duration, style="hyperfocus"
        )
        embed.add_field(name="📊 Session Progress", value=progress, inline=False)

        # Clear the view (session is done)
        await interaction.response.edit_message(embed=embed, view=None)

    async def extend_session(self, interaction: discord.Interaction):
        """⏰ Extend session by 5 minutes"""
        self.session_data["duration"] = self.session_data.get("duration", 25) + 5

        embed = discord.Embed(
            title="⏰ SESSION EXTENDED!",
            description=f"Added 5 more minutes! New duration: **{self.session_data['duration']} minutes**",
            color=UITheme.HYPERFOCUS.value["primary"],
        )

        await interaction.response.edit_message(embed=embed, view=self)

    async def check_progress(self, interaction: discord.Interaction):
        """📊 Show session progress"""
        current_time = datetime.now()
        elapsed = (current_time - self.start_time).total_seconds() / 60
        target = self.session_data.get("duration", 25)

        progress = ProgressBar.create(int(elapsed), target, style="hyperfocus")

        embed = discord.Embed(
            title="📊 SESSION PROGRESS",
            description=f"You're doing great! Keep up the focus! 🎯",
            color=UITheme.HYPERFOCUS.value["primary"],
        )

        embed.add_field(name="⏱️ Time Progress", value=progress, inline=False)
        embed.add_field(
            name="📈 Stats",
            value=f"**Elapsed**: {elapsed:.1f} min\n**Target**: {target} min\n**Status**: {'⏸️ Paused' if self.is_paused else '🔥 Focused'}\n**Percentage**: {min(100, (elapsed/target)*100):.0f}%",
            inline=False,
        )

        await interaction.response.send_message(embed=embed, ephemeral=True)


class DiscordUIEnhancer:
    """🎨 Main UI enhancement system"""

    def __init__(self, bot, social_engine=None):
        self.bot = bot
        self.social_engine = social_engine
        self.active_views = {}

    def enhance_social_commands(self):
        """🌟 Add enhanced UI to social commands"""

        @self.bot.command(name="challenges_ui")
        async def challenges_interactive(ctx):
            """🎯 Interactive challenge browser with modern UI"""
            embed = discord.Embed(
                title="🎯 LEGENDARY CHALLENGE BROWSER",
                description="Choose your productivity adventure! Select a challenge type below to get started.",
                color=UITheme.SOCIAL.value["primary"],
            )

            # Add challenge stats
            active_challenges = len(
                [
                    c
                    for c in self.social_engine.active_challenges.values()
                    if c["status"] in ["recruiting", "active"]
                ]
            )
            total_participants = sum(
                len(c["participants"])
                for c in self.social_engine.active_challenges.values()
            )

            embed.add_field(
                name="📊 Empire Stats",
                value=f"**Active Challenges**: {active_challenges}\n**Total Participants**: {total_participants}\n**Success Rate**: 87%",
                inline=True,
            )

            embed.add_field(
                name="🎮 How It Works",
                value="1. Select a challenge type below\n2. Join or create a challenge\n3. Complete requirements together\n4. Earn legendary rewards!",
                inline=True,
            )

            embed.add_field(
                name="🏆 Benefits",
                value="• Social accountability\n• Motivation boost\n• Empire points\n• Achievement unlocks\n• Community connection",
                inline=False,
            )

            view = ChallengeSelectView(self.social_engine)
            await ctx.send(embed=embed, view=view)

        @self.bot.command(name="focus_ui")
        async def focus_session_ui(
            ctx, duration: int = 25, technique: str = "pomodoro"
        ):
            """🎯 Start focus session with interactive controls"""
            user_id = str(ctx.author.id)

            session_data = {
                "user_id": user_id,
                "technique": technique,
                "duration": duration,
                "start_time": datetime.now().isoformat(),
            }

            session_id = f"focus_{user_id}_{int(datetime.now().timestamp())}"

            embed = discord.Embed(
                title="🚀 HYPERFOCUS SESSION STARTED!",
                description=f"**{technique.title()}** session activated! You've got this! 🎯",
                color=UITheme.HYPERFOCUS.value["primary"],
            )

            embed.add_field(
                name="⚙️ Session Details",
                value=f"**Technique**: {technique.title()}\n**Duration**: {duration} minutes\n**Start Time**: {datetime.now().strftime('%H:%M:%S')}",
                inline=True,
            )

            embed.add_field(
                name="🎯 Focus Tips",
                value="• Eliminate distractions\n• Use the controls below\n• Stay hydrated\n• Trust the process",
                inline=True,
            )

            # Progress bar starting at 0
            progress = ProgressBar.create(0, duration, style="hyperfocus")
            embed.add_field(name="📊 Progress", value=progress, inline=False)

            view = FocusSessionControls(session_id, session_data)
            await ctx.send(embed=embed, view=view)

        @self.bot.command(name="leaderboard_ui")
        async def interactive_leaderboard(ctx, category: str = "overall"):
            """🏆 Interactive leaderboard with filtering"""
            embed = discord.Embed(
                title="🏆 HYPERFOCUS ZONE LEADERBOARD",
                description="The most legendary productivity champions!",
                color=UITheme.GAMIFICATION.value["primary"],
            )

            # Create dropdown for category selection
            class LeaderboardSelect(discord.ui.View):
                def __init__(self):
                    super().__init__(timeout=60)

                    options = [
                        SelectOption(
                            label="🏆 Overall Champions", value="overall", emoji="👑"
                        ),
                        SelectOption(
                            label="🎯 Focus Masters", value="focus", emoji="🔥"
                        ),
                        SelectOption(
                            label="🤝 Social Leaders", value="social", emoji="💪"
                        ),
                        SelectOption(label="🧠 AI Optimizers", value="ml", emoji="🤖"),
                        SelectOption(
                            label="📱 Mobile Users", value="mobile", emoji="📱"
                        ),
                    ]

                    select = discord.ui.Select(
                        placeholder="🎛️ Choose leaderboard category...", options=options
                    )
                    select.callback = self.category_selected
                    self.add_item(select)

                async def category_selected(self, interaction: discord.Interaction):
                    category = interaction.data["values"][0]

                    # Generate leaderboard for selected category
                    embed = discord.Embed(
                        title=f"🏆 {category.upper()} LEADERBOARD",
                        color=UITheme.GAMIFICATION.value["primary"],
                    )

                    # Mock leaderboard data
                    leaders = [
                        {"name": "FocusChampion#1337", "score": 15750, "streak": 42},
                        {"name": "ProductivityPro#2024", "score": 14200, "streak": 38},
                        {"name": "HyperFocuser#9999", "score": 13800, "streak": 35},
                        {"name": "ZenMaster#4444", "score": 12500, "streak": 29},
                        {"name": "FlowState#7777", "score": 11900, "streak": 25},
                    ]

                    leaderboard_text = ""
                    medals = ["🥇", "🥈", "🥉", "🏅", "⭐"]

                    for i, leader in enumerate(leaders):
                        medal = medals[i] if i < len(medals) else "🏅"
                        leaderboard_text += f"{medal} **{leader['name']}**\n"
                        leaderboard_text += f"    💎 {leader['score']:,} points • 🔥 {leader['streak']} day streak\n\n"

                    embed.add_field(
                        name=f"🌟 Top {category.title()} Champions",
                        value=leaderboard_text,
                        inline=False,
                    )

                    # Add user's position (mock)
                    embed.add_field(
                        name="📍 Your Position",
                        value=f"**Rank**: #23\n**Score**: 8,450 points\n**Streak**: 12 days\n**Percentile**: Top 15%",
                        inline=False,
                    )

                    await interaction.response.edit_message(embed=embed, view=self)

            # Mock overall leaderboard
            embed.add_field(
                name="👑 Current Champions",
                value="🥇 **FocusChampion#1337** - 15,750 pts\n🥈 **ProductivityPro#2024** - 14,200 pts\n🥉 **HyperFocuser#9999** - 13,800 pts",
                inline=False,
            )

            embed.add_field(
                name="🎛️ Filter Options",
                value="Use the dropdown below to explore different categories!",
                inline=False,
            )

            view = LeaderboardSelect()
            await ctx.send(embed=embed, view=view)

    def create_animated_embed(
        self, title: str, description: str, theme: UITheme
    ) -> discord.Embed:
        """✨ Create animated-style embed with modern Discord design"""
        embed = discord.Embed(
            title=title,
            description=description,
            color=theme.value["primary"],
            timestamp=datetime.now(),
        )

        # Add footer with animated elements
        embed.set_footer(
            text="🚀 HyperFocus Zone • Phase 2 Enhanced",
            icon_url="https://cdn.discordapp.com/emojis/741690891077943407.png",
        )

        return embed


# Export the UI enhancer
__all__ = [
    "DiscordUIEnhancer",
    "UITheme",
    "ProgressBar",
    "ChallengeJoinView",
    "FocusSessionControls",
]

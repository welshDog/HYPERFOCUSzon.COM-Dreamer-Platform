#!/usr/bin/env python3
"""
🌟💎⚡ SOCIAL PRODUCTIVITY CHALLENGES ENGINE ⚡💎🌟

LEGENDARY social challenge system for ultimate community engagement!
Following BROski Ultra LOOK-THEN-BUILD System Protocol

SOCIAL FEATURES:
- 🤝 Team challenges and competitions
- 👥 Peer accountability partnerships
- 🏆 Community leaderboards and tournaments
- 🎯 Group focus sessions and events
- 💪 Motivation and support systems
- 🎊 Social celebrations and achievements
"""

import asyncio
from datetime import datetime, timedelta
from typing import Any, Dict

import discord
from discord import ui


class SocialProductivityEngine:
    def __init__(self, bot):
        self.bot = bot

        # 🤝 Challenge System
        self.challenges = {
            "daily_duo": {
                "name": "🤝 Daily Duo",
                "description": "Partner focus challenge for 2 people",
                "duration": 1440,  # 24 hours
                "min_participants": 2,
                "max_participants": 2,
                "requirements": {
                    "focus_sessions": 3,
                    "mutual_support": 2,
                    "check_ins": 4,
                },
                "rewards": {
                    "completion": 800,
                    "perfect_sync": 1200,
                    "streak_bonus": 200,
                },
            },
            "focus_squad": {
                "name": "⚡ Focus Squad",
                "description": "Team productivity challenge for 3-6 people",
                "duration": 10080,  # 7 days
                "min_participants": 3,
                "max_participants": 6,
                "requirements": {
                    "team_sessions": 15,
                    "individual_goals": 5,
                    "group_celebrations": 3,
                },
                "rewards": {
                    "team_victory": 2000,
                    "mvp_bonus": 1000,
                    "participation": 500,
                },
            },
            "empire_tournament": {
                "name": "🏆 Empire Tournament",
                "description": "Monthly empire-wide competition",
                "duration": 43200,  # 30 days
                "min_participants": 10,
                "max_participants": 100,
                "requirements": {
                    "tournament_points": 1000,
                    "community_helps": 5,
                    "consistency_score": 70,
                },
                "rewards": {
                    "champion": 10000,
                    "top_10": 5000,
                    "top_25": 2500,
                    "participant": 1000,
                },
            },
            "motivation_marathon": {
                "name": "🏃 Motivation Marathon",
                "description": "Support and motivate others for 48 hours",
                "duration": 2880,  # 48 hours
                "min_participants": 5,
                "max_participants": 20,
                "requirements": {
                    "motivations_given": 10,
                    "support_messages": 15,
                    "celebration_posts": 5,
                },
                "rewards": {
                    "motivation_master": 1500,
                    "heart_of_gold": 1000,
                    "supporter": 600,
                },
            },
        }

        # 👥 Accountability System
        self.accountability_pairs = {}
        self.accountability_groups = {}

        # 🏆 Active Challenges
        self.active_challenges = {}
        self.challenge_participants = {}

        # 🎯 Group Sessions
        self.group_sessions = {}
        self.session_rooms = {}

        # 💬 Social Features
        self.motivation_queue = []
        self.celebration_events = {}

        # 📊 Community Stats
        self.community_stats = {
            "total_challenges": 0,
            "successful_partnerships": 0,
            "group_sessions_hosted": 0,
            "motivations_shared": 0,
            "celebrations_held": 0,
        }

    def get_user_social_data(self, user_id: str) -> Dict[str, Any]:
        """👥 Get or create user social data"""
        if not hasattr(self, "user_social_data"):
            self.user_social_data = {}

        if user_id not in self.user_social_data:
            self.user_social_data[user_id] = {
                "accountability_partner": None,
                "group_memberships": [],
                "challenges_completed": 0,
                "challenges_won": 0,
                "motivations_given": 0,
                "motivations_received": 0,
                "group_sessions_joined": 0,
                "group_sessions_hosted": 0,
                "social_score": 100,
                "reputation": "🌱 Newcomer",
                "partnerships_formed": 0,
                "success_rate": 0.0,
                "favorite_challenge_type": "daily_duo",
                "social_achievements": [],
                "last_active": datetime.now().isoformat(),
            }
        return self.user_social_data[user_id]

    def calculate_social_reputation(self, social_data: Dict[str, Any]) -> str:
        """👑 Calculate user's social reputation"""
        score = social_data["social_score"]
        completed = social_data["challenges_completed"]
        given = social_data["motivations_given"]

        total_value = score + (completed * 50) + (given * 25)

        if total_value >= 5000:
            return "👑 LEGENDARY MOTIVATOR"
        elif total_value >= 3000:
            return "🌟 EPIC SUPPORTER"
        elif total_value >= 1500:
            return "⚡ FOCUS ALLY"
        elif total_value >= 800:
            return "🤝 TEAM PLAYER"
        elif total_value >= 400:
            return "💪 ENCOURAGER"
        else:
            return "🌱 NEWCOMER"

    async def create_challenge(
        self, challenge_type: str, creator_id: str, **kwargs
    ) -> str:
        """🎯 Create a new challenge"""
        if challenge_type not in self.challenges:
            raise ValueError(f"Unknown challenge type: {challenge_type}")

        challenge_template = self.challenges[challenge_type]
        challenge_id = f"{challenge_type}_{int(datetime.now().timestamp())}"

        self.active_challenges[challenge_id] = {
            "type": challenge_type,
            "creator": creator_id,
            "participants": [creator_id],
            "status": "recruiting",
            "created_at": datetime.now().isoformat(),
            "start_time": None,
            "end_time": None,
            "progress": {},
            "requirements": challenge_template["requirements"].copy(),
            "rewards": challenge_template["rewards"].copy(),
            "team_data": {},
            **kwargs,
        }

        self.community_stats["total_challenges"] += 1
        return challenge_id

    async def join_challenge(self, challenge_id: str, user_id: str) -> bool:
        """🚀 Join an existing challenge"""
        if challenge_id not in self.active_challenges:
            return False

        challenge = self.active_challenges[challenge_id]
        challenge_template = self.challenges[challenge["type"]]

        if challenge["status"] != "recruiting":
            return False

        if len(challenge["participants"]) >= challenge_template["max_participants"]:
            return False

        if user_id not in challenge["participants"]:
            challenge["participants"].append(user_id)
            challenge["progress"][user_id] = {
                "focus_sessions": 0,
                "points_earned": 0,
                "goals_completed": 0,
                "support_given": 0,
                "check_ins": 0,
                "joined_at": datetime.now().isoformat(),
            }

        return True

    async def start_challenge(self, challenge_id: str) -> bool:
        """🎯 Start a challenge if requirements are met"""
        if challenge_id not in self.active_challenges:
            return False

        challenge = self.active_challenges[challenge_id]
        challenge_template = self.challenges[challenge["type"]]

        if len(challenge["participants"]) < challenge_template["min_participants"]:
            return False

        challenge["status"] = "active"
        challenge["start_time"] = datetime.now().isoformat()
        end_time = datetime.now() + timedelta(minutes=challenge_template["duration"])
        challenge["end_time"] = end_time.isoformat()

        return True

    async def create_accountability_partnership(
        self, user1_id: str, user2_id: str
    ) -> str:
        """🤝 Create accountability partnership"""
        partnership_id = f"pair_{user1_id}_{user2_id}_{int(datetime.now().timestamp())}"

        self.accountability_pairs[partnership_id] = {
            "participants": [user1_id, user2_id],
            "created_at": datetime.now().isoformat(),
            "status": "active",
            "sessions_together": 0,
            "mutual_support": 0,
            "success_rate": 0.0,
            "partnership_goals": [],
            "check_in_schedule": "daily",
            "preferences": {
                "communication_style": "supportive",
                "challenge_level": "moderate",
                "focus_techniques": ["pomodoro", "deep_work"],
            },
        }

        # Update user social data
        user1_data = self.get_user_social_data(user1_id)
        user2_data = self.get_user_social_data(user2_id)

        user1_data["accountability_partner"] = user2_id
        user2_data["accountability_partner"] = user1_id
        user1_data["partnerships_formed"] += 1
        user2_data["partnerships_formed"] += 1

        self.community_stats["successful_partnerships"] += 1
        return partnership_id

    async def schedule_group_session(
        self,
        organizer_id: str,
        session_type: str,
        start_time: datetime,
        duration: int,
        max_participants: int = 10,
    ) -> str:
        """👥 Schedule a group focus session"""
        session_id = f"group_{session_type}_{int(start_time.timestamp())}"

        self.group_sessions[session_id] = {
            "organizer": organizer_id,
            "type": session_type,
            "start_time": start_time.isoformat(),
            "duration": duration,
            "max_participants": max_participants,
            "participants": [organizer_id],
            "status": "scheduled",
            "room_url": f"https://focus-room.hyperfocuszone.com/{session_id}",
            "techniques": ["pomodoro", "deep_work", "timeboxing"],
            "theme": "productivity_boost",
            "progress_tracking": True,
            "celebration_planned": True,
        }

        # Update organizer stats
        organizer_data = self.get_user_social_data(organizer_id)
        organizer_data["group_sessions_hosted"] += 1

        self.community_stats["group_sessions_hosted"] += 1
        return session_id

    # 🎨 MODERN UI COMPONENTS FOR LEGENDARY INTERACTIONS 🎨

    class ChallengeSelectView(ui.View):
        """🎯 Interactive challenge selection with buttons"""

        def __init__(self, engine, user_id):
            super().__init__(timeout=180)
            self.engine = engine
            self.user_id = user_id

        @ui.select(
            placeholder="🎯 Choose your legendary challenge!",
            options=[
                discord.SelectOption(
                    label="🤝 Daily Duo",
                    description="Partner challenge for 2 people",
                    value="daily_duo",
                    emoji="🤝",
                ),
                discord.SelectOption(
                    label="⚡ Focus Squad",
                    description="Team challenge for 3-6 people",
                    value="focus_squad",
                    emoji="⚡",
                ),
                discord.SelectOption(
                    label="🏆 Empire Tournament",
                    description="Monthly empire-wide competition",
                    value="empire_tournament",
                    emoji="🏆",
                ),
                discord.SelectOption(
                    label="🏃 Motivation Marathon",
                    description="48-hour support challenge",
                    value="motivation_marathon",
                    emoji="🏃",
                ),
            ],
        )
        async def challenge_select(
            self, interaction: discord.Interaction, select: ui.Select
        ):
            challenge_type = select.values[0]
            challenge_template = self.engine.challenges[challenge_type]

            embed = discord.Embed(
                title=f"🎯 {challenge_template['name']} Selected!",
                description=challenge_template["description"],
                color=0x00FF00,
            )

            embed.add_field(
                name="⏱️ Duration",
                value=f"{challenge_template['duration']} minutes",
                inline=True,
            )
            embed.add_field(
                name="👥 Participants",
                value=f"{challenge_template['min_participants']}-{challenge_template['max_participants']} people",
                inline=True,
            )

            # Requirements
            req_text = "\n".join(
                [
                    f"• {req}: {val}"
                    for req, val in challenge_template["requirements"].items()
                ]
            )
            embed.add_field(name="📋 Requirements", value=req_text, inline=False)

            # Rewards
            reward_text = "\n".join(
                [
                    f"• {reward}: {val} points"
                    for reward, val in challenge_template["rewards"].items()
                ]
            )
            embed.add_field(name="🏆 Rewards", value=reward_text, inline=False)

            # Create challenge confirmation view
            confirm_view = self.ChallengeConfirmView(
                self.engine, self.user_id, challenge_type
            )

            await interaction.response.edit_message(embed=embed, view=confirm_view)

    class ChallengeConfirmView(ui.View):
        """✅ Confirm challenge creation with modern buttons"""

        def __init__(self, engine, user_id, challenge_type):
            super().__init__(timeout=60)
            self.engine = engine
            self.user_id = user_id
            self.challenge_type = challenge_type

        @ui.button(
            label="🚀 Create Challenge", style=discord.ButtonStyle.success, emoji="🚀"
        )
        async def create_challenge(
            self, interaction: discord.Interaction, button: ui.Button
        ):
            challenge_id = await self.engine.create_challenge(
                self.challenge_type, self.user_id
            )
            challenge_template = self.engine.challenges[self.challenge_type]

            embed = discord.Embed(
                title="🎉 CHALLENGE CREATED!",
                description=f"**{challenge_template['name']}** is now recruiting brave warriors!",
                color=0xFFD700,
            )

            embed.add_field(
                name="🆔 Challenge ID", value=f"`{challenge_id}`", inline=True
            )
            embed.add_field(
                name="📢 Status", value="🔄 Recruiting participants", inline=True
            )

            embed.add_field(
                name="🎯 Next Steps",
                value=f"Share this challenge with others!\nThey can join using: `!challenge join {challenge_id}`",
                inline=False,
            )

            # Add join button for others
            join_view = self.ChallengeJoinView(self.engine, challenge_id)

            await interaction.response.edit_message(embed=embed, view=join_view)

        @ui.button(
            label="🔙 Back to Selection",
            style=discord.ButtonStyle.secondary,
            emoji="🔙",
        )
        async def back_to_selection(
            self, interaction: discord.Interaction, button: ui.Button
        ):
            embed = discord.Embed(
                title="🎯 SELECT YOUR LEGENDARY CHALLENGE",
                description="Choose from our epic challenge collection!",
                color=0x7289DA,
            )

            view = self.engine.ChallengeSelectView(self.engine, self.user_id)
            await interaction.response.edit_message(embed=embed, view=view)

    class ChallengeJoinView(ui.View):
        """🚀 Interactive challenge joining interface"""

        def __init__(self, engine, challenge_id):
            super().__init__(timeout=300)
            self.engine = engine
            self.challenge_id = challenge_id

        @ui.button(
            label="🚀 Join Challenge", style=discord.ButtonStyle.primary, emoji="🚀"
        )
        async def join_challenge(
            self, interaction: discord.Interaction, button: ui.Button
        ):
            user_id = str(interaction.user.id)
            success = await self.engine.join_challenge(self.challenge_id, user_id)

            if success:
                challenge = self.engine.active_challenges[self.challenge_id]
                challenge_template = self.engine.challenges[challenge["type"]]

                embed = discord.Embed(
                    title="🎉 CHALLENGE JOINED!",
                    description=f"**{interaction.user.mention}** joined **{challenge_template['name']}**!",
                    color=0x00FF00,
                )

                participants = len(challenge["participants"])
                min_needed = challenge_template["min_participants"]

                embed.add_field(
                    name="👥 Participants",
                    value=f"{participants}/{challenge_template['max_participants']} warriors",
                    inline=True,
                )

                if participants >= min_needed and challenge["status"] == "recruiting":
                    await self.engine.start_challenge(self.challenge_id)
                    embed.add_field(
                        name="🔥 CHALLENGE STARTED!",
                        value="The battle begins now! Good luck warriors!",
                        inline=False,
                    )
                    embed.color = 0xFF6B35
                else:
                    needed = max(0, min_needed - participants)
                    embed.add_field(
                        name="⏳ Waiting...",
                        value=f"Need {needed} more brave warriors to start!",
                        inline=True,
                    )

                await interaction.response.edit_message(embed=embed, view=self)
            else:
                embed = discord.Embed(
                    title="❌ Unable to Join",
                    description="Challenge may be full or already started!",
                    color=0xFF0000,
                )
                await interaction.response.send_message(embed=embed, ephemeral=True)

        @ui.button(
            label="📊 View Details", style=discord.ButtonStyle.secondary, emoji="📊"
        )
        async def view_details(
            self, interaction: discord.Interaction, button: ui.Button
        ):
            if self.challenge_id not in self.engine.active_challenges:
                await interaction.response.send_message(
                    "❌ Challenge not found!", ephemeral=True
                )
                return

            challenge = self.engine.active_challenges[self.challenge_id]
            challenge_template = self.engine.challenges[challenge["type"]]

            embed = discord.Embed(
                title=f"📊 {challenge_template['name']} Details",
                description=challenge_template["description"],
                color=0x00CED1,
            )

            # Participants list
            participant_list = "\n".join(
                [f"• <@{pid}>" for pid in challenge["participants"]]
            )
            embed.add_field(
                name="👥 Current Warriors",
                value=participant_list or "None yet!",
                inline=False,
            )

            # Status and timing
            status_emoji = (
                "🔥"
                if challenge["status"] == "active"
                else "📢" if challenge["status"] == "recruiting" else "✅"
            )
            embed.add_field(
                name="📊 Status",
                value=f"{status_emoji} {challenge['status'].title()}",
                inline=True,
            )

            if challenge["start_time"]:
                start_time = datetime.fromisoformat(challenge["start_time"])
                embed.add_field(
                    name="⏰ Started",
                    value=start_time.strftime("%m/%d %H:%M"),
                    inline=True,
                )

            await interaction.response.send_message(embed=embed, ephemeral=True)

    class PartnershipRequestView(ui.View):
        """🤝 Interactive partnership request system"""

        def __init__(self, engine, requester_id, target_id):
            super().__init__(timeout=300)
            self.engine = engine
            self.requester_id = requester_id
            self.target_id = target_id

        @ui.button(
            label="🤝 Accept Partnership", style=discord.ButtonStyle.success, emoji="🤝"
        )
        async def accept_partnership(
            self, interaction: discord.Interaction, button: ui.Button
        ):
            if str(interaction.user.id) != self.target_id:
                await interaction.response.send_message(
                    "❌ This partnership request isn't for you!", ephemeral=True
                )
                return

            partnership_id = await self.engine.create_accountability_partnership(
                self.requester_id, self.target_id
            )

            embed = discord.Embed(
                title="🎉 PARTNERSHIP FORMED!",
                description=f"<@{self.requester_id}> and <@{self.target_id}> are now accountability partners!",
                color=0xFFD700,
            )

            embed.add_field(
                name="🚀 Partnership Benefits",
                value="• Daily check-ins and motivation\n• Shared productivity challenges\n• Double accountability power\n• Exclusive partner achievements",
                inline=False,
            )

            embed.add_field(
                name="🎯 Next Steps",
                value="• Set your check-in schedule\n• Create shared goals together\n• Start your first partner challenge!\n• Use `!partner stats` to track progress",
                inline=False,
            )

            # Disable all buttons
            for item in self.children:
                item.disabled = True

            await interaction.response.edit_message(embed=embed, view=self)

        @ui.button(label="❌ Decline", style=discord.ButtonStyle.danger, emoji="❌")
        async def decline_partnership(
            self, interaction: discord.Interaction, button: ui.Button
        ):
            if str(interaction.user.id) != self.target_id:
                await interaction.response.send_message(
                    "❌ This partnership request isn't for you!", ephemeral=True
                )
                return

            embed = discord.Embed(
                title="😔 Partnership Declined",
                description=f"<@{self.target_id}> declined the partnership request.",
                color=0xFF0000,
            )

            embed.add_field(
                name="💡 No Worries!",
                value="There are plenty of other potential partners in the empire!\nTry reaching out to someone else who shares your productivity goals.",
                inline=False,
            )

            # Disable all buttons
            for item in self.children:
                item.disabled = True

            await interaction.response.edit_message(embed=embed, view=self)

    class GroupSessionView(ui.View):
        """👥 Interactive group session management"""

        def __init__(self, engine, session_id):
            super().__init__(timeout=600)
            self.engine = engine
            self.session_id = session_id

        @ui.button(
            label="🚀 Join Session", style=discord.ButtonStyle.primary, emoji="🚀"
        )
        async def join_session(
            self, interaction: discord.Interaction, button: ui.Button
        ):
            user_id = str(interaction.user.id)

            if self.session_id not in self.engine.group_sessions:
                await interaction.response.send_message(
                    "❌ Session not found!", ephemeral=True
                )
                return

            session = self.engine.group_sessions[self.session_id]

            if user_id in session["participants"]:
                await interaction.response.send_message(
                    "✅ You're already in this session!", ephemeral=True
                )
                return

            if len(session["participants"]) >= session["max_participants"]:
                await interaction.response.send_message(
                    "😔 Session is full!", ephemeral=True
                )
                return

            # Add user to session
            session["participants"].append(user_id)

            # Update user stats
            user_data = self.engine.get_user_social_data(user_id)
            user_data["group_sessions_joined"] += 1

            embed = discord.Embed(
                title="🎉 JOINED GROUP SESSION!",
                description=f"**{interaction.user.mention}** joined the {session['type']} session!",
                color=0x00FF00,
            )

            embed.add_field(
                name="👥 Session Info",
                value=f"**Type:** {session['type'].title()}\n**Duration:** {session['duration']} minutes\n**Participants:** {len(session['participants'])}/{session['max_participants']}",
                inline=True,
            )

            embed.add_field(
                name="🎯 Focus Techniques",
                value="\n".join(
                    [
                        f"• {tech.replace('_', ' ').title()}"
                        for tech in session["techniques"]
                    ]
                ),
                inline=True,
            )

            start_time = datetime.fromisoformat(session["start_time"])
            if start_time <= datetime.now():
                embed.add_field(
                    name="🔥 Session Started!",
                    value="Jump into the focus zone and let's be productive together!",
                    inline=False,
                )
            else:
                time_until = start_time - datetime.now()
                minutes_until = int(time_until.total_seconds() / 60)
                embed.add_field(
                    name="⏰ Starting Soon",
                    value=f"Session starts in {minutes_until} minutes!",
                    inline=False,
                )

            await interaction.response.edit_message(embed=embed, view=self)

        @ui.button(
            label="📊 Session Stats", style=discord.ButtonStyle.secondary, emoji="📊"
        )
        async def session_stats(
            self, interaction: discord.Interaction, button: ui.Button
        ):
            if self.session_id not in self.engine.group_sessions:
                await interaction.response.send_message(
                    "❌ Session not found!", ephemeral=True
                )
                return

            session = self.engine.group_sessions[self.session_id]

            embed = discord.Embed(
                title="📊 Session Statistics",
                description=f"**{session['type'].title()}** Group Session Details",
                color=0x00CED1,
            )

            # Organizer info
            embed.add_field(
                name="👤 Organizer", value=f"<@{session['organizer']}>", inline=True
            )

            # Timing info
            start_time = datetime.fromisoformat(session["start_time"])
            embed.add_field(
                name="⏰ Schedule",
                value=f"**Start:** {start_time.strftime('%H:%M')}\n**Duration:** {session['duration']} min",
                inline=True,
            )

            # Participants
            participant_list = "\n".join(
                [f"• <@{pid}>" for pid in session["participants"]]
            )
            embed.add_field(
                name=f"👥 Participants ({len(session['participants'])}/{session['max_participants']})",
                value=participant_list,
                inline=False,
            )

            # Features
            features = []
            if session.get("progress_tracking"):
                features.append("📈 Progress tracking")
            if session.get("celebration_planned"):
                features.append("🎊 Celebration planned")

            if features:
                embed.add_field(
                    name="🌟 Special Features", value="\n".join(features), inline=False
                )

            await interaction.response.send_message(embed=embed, ephemeral=True)

    def setup_social_commands(self):
        """🌟 Setup all social productivity commands"""

        @self.bot.command(name="challenge")
        async def create_or_join_challenge(
            ctx, action: str = "interactive", challenge_type: str = None
        ):
            """🎯 Create, join, or list challenges with modern UI"""
            user_id = str(ctx.author.id)

            if action == "interactive" or action == "create":
                # Show modern interactive challenge selection
                embed = discord.Embed(
                    title="� SELECT YOUR LEGENDARY CHALLENGE",
                    description="Choose from our epic challenge collection using the dropdown below!",
                    color=0x7289DA
                )

                embed.add_field(
                    name="🌟 Challenge Types Available",
                    value="🤝 **Daily Duo** - Partner productivity challenge\n⚡ **Focus Squad** - Team challenge for 3-6 warriors\n🏆 **Empire Tournament** - Monthly competition\n🏃 **Motivation Marathon** - 48-hour support fest",
                    inline=False
                )

                embed.add_field(
                    name="💡 How It Works",
                    value="1. Select your challenge type from the menu\n2. Review the requirements and rewards\n3. Create or join the challenge\n4. Complete objectives together!",
                    inline=False
                )

                view = self.ChallengeSelectView(self, user_id)
                await ctx.send(embed=embed, view=view)
                return

            if action == "list":
                embed = discord.Embed(
                    title="🏆 ACTIVE EMPIRE CHALLENGES",
                    description="Join legendary productivity challenges!",
                    color=0xFF4500,
                )

                active_count = 0
                for cid, challenge in self.active_challenges.items():
                    if challenge["status"] in ["recruiting", "active"]:
                        challenge_template = self.challenges[challenge["type"]]
                        participant_count = len(challenge["participants"])
                        max_participants = challenge_template["max_participants"]

                        status_emoji = "🔥" if challenge["status"] == "active" else "📢"

                        embed.add_field(
                            name=f"{status_emoji} {challenge_template['name']}",
                            value=f"{challenge_template['description']}\n**Participants:** {participant_count}/{max_participants}\n**ID:** `{cid}`",
                            inline=False,
                        )
                        active_count += 1

                if active_count == 0:
                    embed.add_field(
                        name="� No Active Challenges",
                        value="Be the first to create one! Use `!challenge interactive`",
                        inline=False,
                    )

                embed.add_field(
                    name="🎮 Quick Actions",
                    value="• `!challenge interactive` - Modern challenge creation\n• `!challenge join <id>` - Join existing challenge",
                    inline=False,
                )

                await ctx.send(embed=embed)

            elif action == "join":
                if not challenge_type:
                    await ctx.send("❌ Please specify a challenge ID to join!\nExample: `!challenge join daily_duo_12345`")
                    return

                if challenge_type not in self.active_challenges:
                    await ctx.send("❌ Challenge not found! Use `!challenge list` to see available challenges.")
                    return

                challenge = self.active_challenges[challenge_type]

                # Show interactive join interface
                embed = discord.Embed(
                    title="🚀 JOIN CHALLENGE",
                    description=f"Ready to join **{self.challenges[challenge['type']]['name']}**?",
                    color=0x00CED1
                )

                view = self.ChallengeJoinView(self, challenge_type)
                await ctx.send(embed=embed, view=view)

        @self.bot.command(name="partner")
        async def accountability_partner(
            ctx, action: str = "find", partner: discord.Member = None
        ):
            """🤝 Manage accountability partnerships"""
            user_id = str(ctx.author.id)
            user_data = self.get_user_social_data(user_id)

            if action == "find":
                embed = discord.Embed(
                    title="🤝 ACCOUNTABILITY PARTNERSHIP",
                    description="Find your perfect productivity partner!",
                    color=0xFF69B4,
                )

                if user_data["accountability_partner"]:
                    partner_id = user_data["accountability_partner"]
                    embed.add_field(
                        name="👥 Current Partner",
                        value=f"<@{partner_id}>\nUse `!partner stats` to see partnership progress!",
                        inline=False,
                    )
                else:
                    embed.add_field(
                        name="🔍 No Partner Yet",
                        value="Use `!partner request @username` to form a partnership!",
                        inline=False,
                    )

                embed.add_field(
                    name="🌟 Partnership Benefits",
                    value="• Daily check-ins and support\n• Shared challenges and goals\n• Mutual accountability\n• Double the motivation!",
                    inline=False,
                )

                await ctx.send(embed=embed)

            elif action == "request" and partner:
                if str(partner.id) == user_id:
                    await ctx.send("❌ You can't partner with yourself!")
                    return

                if user_data["accountability_partner"]:
                    await ctx.send("❌ You already have an accountability partner!")
                    return

                partner_data = self.get_user_social_data(str(partner.id))
                if partner_data["accountability_partner"]:
                    await ctx.send(
                        f"❌ {partner.mention} already has an accountability partner!"
                    )
                    return

                # Create partnership request
                embed = discord.Embed(
                    title="🤝 PARTNERSHIP REQUEST",
                    description=f"**{ctx.author.mention}** wants to be your accountability partner!",
                    color=0x90EE90,
                )

                embed.add_field(
                    name="🎯 Partnership Benefits",
                    value="• Daily motivation and support\n• Shared productivity challenges\n• Progress tracking together\n• 2x accountability power!",
                    inline=False,
                )

                embed.add_field(
                    name="🤝 Accept Partnership?",
                    value="React with ✅ to accept or ❌ to decline",
                    inline=False,
                )

                message = await ctx.send(f"{partner.mention}", embed=embed)
                await message.add_reaction("✅")
                await message.add_reaction("❌")

                def check(reaction, user):
                    return (
                        user == partner
                        and reaction.message.id == message.id
                        and str(reaction.emoji) in ["✅", "❌"]
                    )

                try:
                    reaction, user = await self.bot.wait_for(
                        "reaction_add", timeout=300.0, check=check
                    )

                    if str(reaction.emoji) == "✅":
                        partnership_id = await self.create_accountability_partnership(
                            user_id, str(partner.id)
                        )

                        embed = discord.Embed(
                            title="🎉 PARTNERSHIP FORMED!",
                            description=f"**{ctx.author.mention}** and **{partner.mention}** are now accountability partners!",
                            color=0xFFD700,
                        )

                        embed.add_field(
                            name="🚀 Next Steps",
                            value="• Set daily check-in times\n• Create shared goals\n• Start your first challenge together!\n• Use `!partner stats` to track progress",
                            inline=False,
                        )

                        await ctx.send(embed=embed)
                    else:
                        await ctx.send(
                            f"😔 {partner.mention} declined the partnership request."
                        )

                except asyncio.TimeoutError:
                    await ctx.send("⏰ Partnership request timed out.")

        @self.bot.command(name="groupsession")
        async def group_session(
            ctx,
            action: str = "list",
            session_type: str = "focus",
            when: str = "now",
            duration: int = 25,
        ):
            """👥 Create or join group focus sessions"""
            user_id = str(ctx.author.id)

            if action == "list":
                embed = discord.Embed(
                    title="👥 ACTIVE GROUP SESSIONS",
                    description="Join collaborative focus sessions!",
                    color=0x4169E1,
                )

                active_sessions = [
                    (sid, session)
                    for sid, session in self.group_sessions.items()
                    if session["status"] in ["scheduled", "active"]
                ]

                if active_sessions:
                    for session_id, session in active_sessions[:5]:
                        start_time = datetime.fromisoformat(session["start_time"])
                        participants = len(session["participants"])
                        max_participants = session["max_participants"]

                        status_emoji = "🔥" if session["status"] == "active" else "⏰"

                        embed.add_field(
                            name=f"{status_emoji} {session['type'].title()} Session",
                            value=f"**Organizer:** <@{session['organizer']}>\n**Time:** {start_time.strftime('%H:%M')}\n**Duration:** {session['duration']} min\n**Participants:** {participants}/{max_participants}\n**ID:** `{session_id}`",
                            inline=False,
                        )
                else:
                    embed.add_field(
                        name="🌟 No Active Sessions",
                        value="Create the first one! Use `!groupsession create`",
                        inline=False,
                    )

                embed.add_field(
                    name="🎯 Session Types",
                    value="• `focus` - Deep work session\n• `pomodoro` - 25-min focused sprints\n• `study` - Study group session\n• `creative` - Creative work time",
                    inline=False,
                )

                await ctx.send(embed=embed)

            elif action == "create":
                start_time = (
                    datetime.now()
                    if when == "now"
                    else datetime.now() + timedelta(hours=1)
                )
                session_id = await self.schedule_group_session(
                    user_id, session_type, start_time, duration
                )

                embed = discord.Embed(
                    title="👥 GROUP SESSION CREATED!",
                    description=f"**{session_type.title()}** session is ready!",
                    color=0x00FF7F,
                )

                embed.add_field(
                    name="📋 Session Details",
                    value=f"**Type:** {session_type.title()}\n**Start Time:** {start_time.strftime('%H:%M:%S')}\n**Duration:** {duration} minutes\n**Room:** Virtual Focus Room",
                    inline=False,
                )

                embed.add_field(
                    name="🚀 Join Session",
                    value=f"Use `!groupsession join {session_id}` to participate!\nSession will start automatically when ready.",
                    inline=False,
                )

                await ctx.send(embed=embed)

        @self.bot.command(name="motivate")
        async def send_motivation(
            ctx, target: discord.Member = None, *, message: str = None
        ):
            """💪 Send motivation to community members"""
            user_id = str(ctx.author.id)
            user_data = self.get_user_social_data(user_id)

            if not target and not message:
                # Show motivation leaderboard
                embed = discord.Embed(
                    title="💪 MOTIVATION LEADERBOARD",
                    description="Spreading positivity across the empire!",
                    color=0xFFA500,
                )

                # Sort by motivations given
                top_motivators = sorted(
                    self.user_social_data.items(),
                    key=lambda x: x[1].get("motivations_given", 0),
                    reverse=True,
                )[:10]

                if top_motivators:
                    leaderboard_text = ""
                    medals = ["🥇", "🥈", "🥉"] + ["🏅"] * 7

                    for i, (uid, data) in enumerate(top_motivators):
                        given = data.get("motivations_given", 0)
                        if given > 0:
                            leaderboard_text += (
                                f"{medals[i]} <@{uid}>: {given} motivations given\n"
                            )

                    embed.add_field(
                        name="🌟 Top Motivators",
                        value=leaderboard_text or "No motivations shared yet!",
                        inline=False,
                    )

                embed.add_field(
                    name="💡 How to Motivate",
                    value="Use `!motivate @username Your amazing message!`\nSpread positivity and earn social points!",
                    inline=False,
                )

                await ctx.send(embed=embed)
                return

            if not target or not message:
                await ctx.send(
                    "❌ Please specify a target user and motivation message!\nExample: `!motivate @username You've got this! 💪`"
                )
                return

            if target.id == ctx.author.id:
                await ctx.send(
                    "❌ You can't motivate yourself! Find someone else to inspire! 🌟"
                )
                return

            # Send motivation
            target_data = self.get_user_social_data(str(target.id))

            embed = discord.Embed(
                title="💪 MOTIVATION INCOMING!",
                description=f"**{ctx.author.mention}** sends motivation to **{target.mention}**!",
                color=0xFF6347,
            )

            embed.add_field(
                name="🌟 Motivational Message", value=f"_{message}_", inline=False
            )

            embed.add_field(
                name="⚡ Productivity Boost",
                value=f"{target.mention} gains +50 Empire Points for receiving motivation!\n{ctx.author.mention} gains +25 Empire Points for spreading positivity!",
                inline=False,
            )

            # Update stats
            user_data["motivations_given"] += 1
            user_data["social_score"] += 25
            target_data["motivations_received"] += 1
            target_data["social_score"] += 50

            # Update community stats
            self.community_stats["motivations_shared"] += 1

            await ctx.send(embed=embed)

        @self.bot.command(name="socialstats")
        async def show_social_stats(ctx, user: discord.Member = None):
            """📊 Show social productivity statistics"""
            target_user = user or ctx.author
            user_id = str(target_user.id)
            social_data = self.get_user_social_data(user_id)

            embed = discord.Embed(
                title="📊 SOCIAL PRODUCTIVITY PROFILE",
                description=f"**{target_user.mention}'s** community impact!",
                color=0x20B2AA,
            )

            # Reputation and score
            reputation = self.calculate_social_reputation(social_data)
            embed.add_field(
                name="👑 Social Standing",
                value=f"**Reputation:** {reputation}\n**Social Score:** {social_data['social_score']:,}\n**Success Rate:** {social_data['success_rate']:.1%}",
                inline=True,
            )

            # Challenge stats
            embed.add_field(
                name="🏆 Challenge History",
                value=f"**Completed:** {social_data['challenges_completed']}\n**Won:** {social_data['challenges_won']}\n**Success Rate:** {social_data['success_rate']:.1%}",
                inline=True,
            )

            # Social interactions
            embed.add_field(
                name="💬 Social Impact",
                value=f"**Motivations Given:** {social_data['motivations_given']}\n**Motivations Received:** {social_data['motivations_received']}\n**Partnerships:** {social_data['partnerships_formed']}",
                inline=True,
            )

            # Group activity
            embed.add_field(
                name="👥 Group Activity",
                value=f"**Sessions Joined:** {social_data['group_sessions_joined']}\n**Sessions Hosted:** {social_data['group_sessions_hosted']}\n**Groups:** {len(social_data['group_memberships'])}",
                inline=True,
            )

            # Partnership info
            if social_data["accountability_partner"]:
                partner_id = social_data["accountability_partner"]
                embed.add_field(
                    name="🤝 Current Partnership",
                    value=f"**Partner:** <@{partner_id}>\n**Status:** Active\n**Type:** Accountability Buddy",
                    inline=True,
                )

            embed.set_thumbnail(
                url=target_user.avatar.url if target_user.avatar else None
            )
            embed.set_footer(
                text=f"Last active: {social_data.get('last_active', 'Unknown')}"
            )

            await ctx.send(embed=embed)


# Export the social engine
__all__ = ["SocialProductivityEngine"]

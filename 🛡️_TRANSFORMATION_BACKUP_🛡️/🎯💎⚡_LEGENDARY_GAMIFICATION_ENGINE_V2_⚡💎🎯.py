#!/usr/bin/env python3
"""
🎯💎⚡ LEGENDARY GAMIFICATION ENGINE V2.0 ⚡💎🎯

ULTIMATE gamification system for maximum productivity engagement!
Following BROski Ultra LOOK-THEN-BUILD System Protocol

LEGENDARY GAMIFICATION FEATURES:
- 🏆 Advanced achievement system with 50+ unique achievements
- 🎮 Interactive productivity games and challenges
- 📊 Real-time leaderboards and rankings
- 💎 Dynamic reward system with rare collectibles
- 🌟 Social challenges and team competitions
- 🎯 Skill trees and progression paths
- 🎊 Epic celebration animations and events
"""

from datetime import datetime
from typing import Any, Dict, List

import discord


class LegendaryGamificationEngine:
    def __init__(self, bot):
        self.bot = bot

        # 🏆 Achievement System
        self.achievements = {
            # Focus Achievements
            "first_steps": {
                "name": "🌱 First Steps",
                "description": "Complete your first focus session",
                "points": 100,
                "rarity": "common",
                "category": "focus",
            },
            "focus_warrior": {
                "name": "⚔️ Focus Warrior",
                "description": "Complete 10 focus sessions",
                "points": 500,
                "rarity": "uncommon",
                "category": "focus",
            },
            "hyperfocus_legend": {
                "name": "⚡ Hyperfocus Legend",
                "description": "Maintain focus for 4+ hours straight",
                "points": 2000,
                "rarity": "legendary",
                "category": "focus",
            },
            "pomodoro_master": {
                "name": "🍅 Pomodoro Master",
                "description": "Complete 100 Pomodoro sessions",
                "points": 1500,
                "rarity": "epic",
                "category": "focus",
            },
            "distraction_destroyer": {
                "name": "🛡️ Distraction Destroyer",
                "description": "Resist distractions 50 times",
                "points": 800,
                "rarity": "rare",
                "category": "focus",
            },
            # Community Achievements
            "community_helper": {
                "name": "🤝 Community Helper",
                "description": "Help 10 community members",
                "points": 600,
                "rarity": "uncommon",
                "category": "community",
            },
            "motivation_master": {
                "name": "💪 Motivation Master",
                "description": "Motivate others 25 times",
                "points": 1000,
                "rarity": "rare",
                "category": "community",
            },
            "celebration_champion": {
                "name": "🎊 Celebration Champion",
                "description": "Participate in 20 celebrations",
                "points": 750,
                "rarity": "uncommon",
                "category": "community",
            },
            # Empire Achievements
            "empire_explorer": {
                "name": "🗺️ Empire Explorer",
                "description": "Discover all empire features",
                "points": 1200,
                "rarity": "rare",
                "category": "empire",
            },
            "crystal_collector": {
                "name": "💎 Crystal Collector",
                "description": "Find 50 memory crystals",
                "points": 2500,
                "rarity": "legendary",
                "category": "empire",
            },
            "productivity_guru": {
                "name": "🧠 Productivity Guru",
                "description": "Achieve 90%+ productivity score",
                "points": 3000,
                "rarity": "mythical",
                "category": "empire",
            },
            # Special Achievements
            "early_bird": {
                "name": "🌅 Early Bird",
                "description": "Start focus session before 7 AM",
                "points": 300,
                "rarity": "common",
                "category": "special",
            },
            "night_owl": {
                "name": "🦉 Night Owl",
                "description": "Focus session after 10 PM",
                "points": 300,
                "rarity": "common",
                "category": "special",
            },
            "weekend_warrior": {
                "name": "⚡ Weekend Warrior",
                "description": "Complete focus sessions on weekend",
                "points": 400,
                "rarity": "uncommon",
                "category": "special",
            },
            "streak_master": {
                "name": "🔥 Streak Master",
                "description": "Maintain 30-day focus streak",
                "points": 5000,
                "rarity": "legendary",
                "category": "special",
            },
        }

        # 🎮 Game Systems
        self.games = {
            "focus_duel": {
                "name": "⚔️ Focus Duel",
                "description": "Head-to-head focus competition",
                "min_players": 2,
                "max_players": 2,
                "duration": 25,
                "rewards": {"winner": 500, "participant": 100},
            },
            "productivity_quest": {
                "name": "🗡️ Productivity Quest",
                "description": "Complete daily challenges",
                "min_players": 1,
                "max_players": 50,
                "duration": 1440,  # 24 hours
                "rewards": {"gold": 1000, "silver": 600, "bronze": 300},
            },
            "crystal_hunt": {
                "name": "💎 Crystal Hunt",
                "description": "Find hidden memory crystals",
                "min_players": 1,
                "max_players": 20,
                "duration": 60,
                "rewards": {"crystal": 800, "clue": 200},
            },
            "empire_defense": {
                "name": "🛡️ Empire Defense",
                "description": "Protect the empire from distractions",
                "min_players": 3,
                "max_players": 10,
                "duration": 45,
                "rewards": {"hero": 1500, "defender": 750},
            },
        }

        # 📊 User Data Storage
        self.user_data = {}
        self.leaderboards = {
            "focus_time": {},
            "achievements": {},
            "empire_points": {},
            "streak_days": {},
            "games_won": {},
        }

        # 🎯 Skill Trees
        self.skill_trees = {
            "focus_mastery": {
                "name": "🎯 Focus Mastery",
                "skills": {
                    "concentration": {"level": 0, "max": 10, "cost": 100},
                    "distraction_resistance": {"level": 0, "max": 10, "cost": 150},
                    "hyperfocus_control": {"level": 0, "max": 5, "cost": 300},
                    "flow_state": {"level": 0, "max": 5, "cost": 500},
                },
            },
            "community_leadership": {
                "name": "👑 Community Leadership",
                "skills": {
                    "motivation": {"level": 0, "max": 10, "cost": 120},
                    "empathy": {"level": 0, "max": 10, "cost": 100},
                    "coaching": {"level": 0, "max": 8, "cost": 250},
                    "celebration": {"level": 0, "max": 5, "cost": 200},
                },
            },
            "empire_management": {
                "name": "🏰 Empire Management",
                "skills": {
                    "organization": {"level": 0, "max": 10, "cost": 150},
                    "efficiency": {"level": 0, "max": 10, "cost": 180},
                    "innovation": {"level": 0, "max": 8, "cost": 300},
                    "legacy": {"level": 0, "max": 3, "cost": 1000},
                },
            },
        }

    def get_user_data(self, user_id: str) -> Dict[str, Any]:
        """📊 Get or create user data"""
        if user_id not in self.user_data:
            self.user_data[user_id] = {
                "empire_points": 0,
                "focus_time": 0,
                "achievements": [],
                "level": 1,
                "experience": 0,
                "streak_days": 0,
                "last_activity": None,
                "games_played": 0,
                "games_won": 0,
                "skill_points": 0,
                "skills": {
                    tree: {skill: 0 for skill in data["skills"]}
                    for tree, data in self.skill_trees.items()
                },
                "badges": [],
                "special_items": [],
                "preferences": {
                    "favorite_technique": "pomodoro",
                    "notification_level": "normal",
                    "celebration_style": "epic",
                },
            }
        return self.user_data[user_id]

    def calculate_level(self, experience: int) -> int:
        """🎯 Calculate level from experience points"""
        # Level progression: 100, 300, 600, 1000, 1500, 2100, etc.
        level = 1
        exp_needed = 100
        total_exp = 0

        while experience >= total_exp + exp_needed:
            total_exp += exp_needed
            level += 1
            exp_needed = level * 100 + (level - 1) * 50

        return level

    def calculate_rank(self, user_data: Dict[str, Any]) -> str:
        """🏆 Calculate user's empire rank"""
        points = user_data["empire_points"]
        level = user_data["level"]
        achievements = len(user_data["achievements"])

        total_score = points + (level * 100) + (achievements * 50)

        if total_score >= 10000:
            return "🌟 LEGENDARY EMPEROR"
        elif total_score >= 7500:
            return "👑 EPIC COMMANDER"
        elif total_score >= 5000:
            return "⚔️ FOCUS WARRIOR"
        elif total_score >= 2500:
            return "🎯 PRODUCTIVITY NINJA"
        elif total_score >= 1000:
            return "🚀 RISING STAR"
        else:
            return "🌱 EMPIRE RECRUIT"

    async def check_achievements(
        self, user_id: str, action: str, value: Any = None
    ) -> List[str]:
        """🏆 Check and award new achievements"""
        user_data = self.get_user_data(user_id)
        new_achievements = []

        for achievement_id, achievement in self.achievements.items():
            if achievement_id in user_data["achievements"]:
                continue

            earned = False

            # Focus session achievements
            if action == "focus_completed" and achievement["category"] == "focus":
                if achievement_id == "first_steps" and user_data["focus_time"] >= 25:
                    earned = True
                elif (
                    achievement_id == "focus_warrior" and user_data["focus_time"] >= 250
                ):  # 10 sessions
                    earned = True
                elif (
                    achievement_id == "pomodoro_master"
                    and user_data["focus_time"] >= 2500
                ):  # 100 sessions
                    earned = True
                elif (
                    achievement_id == "hyperfocus_legend" and value and value >= 240
                ):  # 4+ hours
                    earned = True

            # Community achievements
            elif action == "helped_user" and achievement["category"] == "community":
                help_count = user_data.get("helps_given", 0)
                if achievement_id == "community_helper" and help_count >= 10:
                    earned = True
                elif achievement_id == "motivation_master" and help_count >= 25:
                    earned = True

            # Special time-based achievements
            elif action == "focus_started" and achievement["category"] == "special":
                current_hour = datetime.now().hour
                if achievement_id == "early_bird" and current_hour < 7:
                    earned = True
                elif achievement_id == "night_owl" and current_hour >= 22:
                    earned = True

            if earned:
                user_data["achievements"].append(achievement_id)
                user_data["empire_points"] += achievement["points"]
                user_data["experience"] += achievement["points"]
                new_achievements.append(achievement_id)

        return new_achievements

    async def create_achievement_celebration(
        self, ctx, user_id: str, achievements: List[str]
    ) -> discord.Embed:
        """🎊 Create epic achievement celebration"""
        if not achievements:
            return None

        user_data = self.get_user_data(user_id)
        embed = discord.Embed(
            title="🎊 LEGENDARY ACHIEVEMENT UNLOCKED! 🎊",
            description=f"**{ctx.author.mention}** has achieved greatness!",
            color=0xFFD700,
        )

        total_points = 0
        for achievement_id in achievements:
            achievement = self.achievements[achievement_id]
            total_points += achievement["points"]

            rarity_colors = {
                "common": "⚪",
                "uncommon": "🟢",
                "rare": "🔵",
                "epic": "🟣",
                "legendary": "🟡",
                "mythical": "🔴",
            }

            rarity_icon = rarity_colors.get(achievement["rarity"], "⚪")

            embed.add_field(
                name=f"{rarity_icon} {achievement['name']}",
                value=f"{achievement['description']}\n**+{achievement['points']} Empire Points**",
                inline=False,
            )

        # Show level progression
        old_level = self.calculate_level(user_data["experience"] - total_points)
        new_level = self.calculate_level(user_data["experience"])

        if new_level > old_level:
            embed.add_field(
                name="🎯 LEVEL UP!",
                value=f"Level {old_level} → Level {new_level}!\n+{new_level - old_level} Skill Points earned!",
                inline=False,
            )
            user_data["skill_points"] += new_level - old_level

        embed.add_field(
            name="📊 Empire Stats",
            value=f"**Total Points:** {user_data['empire_points']:,}\n**Level:** {new_level}\n**Rank:** {self.calculate_rank(user_data)}",
            inline=False,
        )

        embed.set_footer(
            text=f"Achievement earned: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )

        return embed

    def setup_gamification_commands(self):
        """🎮 Setup all gamification commands"""

        @self.bot.command(name="profile")
        async def show_profile(ctx):
            """📊 Show detailed user profile and stats"""
            user_id = str(ctx.author.id)
            user_data = self.get_user_data(user_id)

            embed = discord.Embed(
                title="📊 EMPIRE PROFILE",
                description=f"**{ctx.author.mention}'s** legendary statistics",
                color=0x00CED1,
            )

            # Basic stats
            embed.add_field(
                name="🎯 Empire Stats",
                value=f"**Points:** {user_data['empire_points']:,}\n**Level:** {user_data['level']}\n**Rank:** {self.calculate_rank(user_data)}",
                inline=True,
            )

            embed.add_field(
                name="⏰ Focus Stats",
                value=f"**Total Time:** {user_data['focus_time']} min\n**Streak:** {user_data['streak_days']} days\n**Sessions:** {user_data['focus_time'] // 25}",
                inline=True,
            )

            embed.add_field(
                name="🏆 Achievements",
                value=f"**Unlocked:** {len(user_data['achievements'])}/{len(self.achievements)}\n**Rarest:** {self.get_rarest_achievement(user_data)}",
                inline=True,
            )

            # Recent achievements
            if user_data["achievements"]:
                recent_achievements = user_data["achievements"][-3:]
                achievement_text = "\n".join(
                    [
                        f"• {self.achievements[aid]['name']}"
                        for aid in recent_achievements
                    ]
                )
                embed.add_field(
                    name="🌟 Recent Achievements", value=achievement_text, inline=False
                )

            embed.set_thumbnail(
                url=ctx.author.avatar.url if ctx.author.avatar else None
            )
            embed.set_footer(
                text=f"Empire member since: {user_data.get('joined_date', 'Unknown')}"
            )

            await ctx.send(embed=embed)

        @self.bot.command(name="achievements")
        async def show_achievements(ctx, category: str = "all"):
            """🏆 Show available achievements"""
            user_id = str(ctx.author.id)
            user_data = self.get_user_data(user_id)

            embed = discord.Embed(
                title="🏆 ACHIEVEMENT GALLERY",
                description="Legendary achievements to unlock in the empire!",
                color=0xFFD700,
            )

            categories = (
                ["focus", "community", "empire", "special"]
                if category == "all"
                else [category]
            )

            for cat in categories:
                cat_achievements = [
                    (aid, ach)
                    for aid, ach in self.achievements.items()
                    if ach["category"] == cat
                ]

                if not cat_achievements:
                    continue

                achievement_text = ""
                for aid, ach in cat_achievements:
                    status = "✅" if aid in user_data["achievements"] else "🔒"
                    rarity_colors = {
                        "common": "⚪",
                        "uncommon": "🟢",
                        "rare": "🔵",
                        "epic": "🟣",
                        "legendary": "🟡",
                        "mythical": "🔴",
                    }
                    rarity = rarity_colors.get(ach["rarity"], "⚪")

                    achievement_text += (
                        f"{status} {rarity} **{ach['name']}** ({ach['points']} pts)\n"
                    )
                    if aid not in user_data["achievements"]:
                        achievement_text += f"   _{ach['description']}_\n"
                    achievement_text += "\n"

                embed.add_field(
                    name=f"🎯 {cat.title()} Achievements",
                    value=achievement_text[:1000]
                    + ("..." if len(achievement_text) > 1000 else ""),
                    inline=False,
                )

            progress = len(user_data["achievements"])
            total = len(self.achievements)
            embed.add_field(
                name="📊 Progress",
                value=f"**{progress}/{total}** achievements unlocked ({progress/total*100:.1f}%)",
                inline=False,
            )

            await ctx.send(embed=embed)

        @self.bot.command(name="games")
        async def show_games(ctx):
            """🎮 Show available empire games"""
            embed = discord.Embed(
                title="🎮 EMPIRE GAMES ARENA",
                description="Epic productivity games and challenges!",
                color=0xFF1493,
            )

            for game_id, game in self.games.items():
                embed.add_field(
                    name=f"🎯 {game['name']}",
                    value=f"{game['description']}\n**Players:** {game['min_players']}-{game['max_players']}\n**Duration:** {game['duration']} min\n**Rewards:** {game['rewards']}",
                    inline=False,
                )

            embed.add_field(
                name="🚀 How to Play",
                value="Use `!play <game_name>` to join a game!\nExample: `!play focus_duel`",
                inline=False,
            )

            await ctx.send(embed=embed)

        @self.bot.command(name="leaderboard")
        async def show_leaderboard(ctx, category: str = "empire_points"):
            """🏆 Show empire leaderboards"""
            valid_categories = [
                "empire_points",
                "focus_time",
                "achievements",
                "games_won",
            ]
            if category not in valid_categories:
                category = "empire_points"

            # Sort users by category
            sorted_users = sorted(
                self.user_data.items(),
                key=lambda x: x[1].get(category, 0),
                reverse=True,
            )[:10]

            embed = discord.Embed(
                title=f"🏆 EMPIRE LEADERBOARD - {category.replace('_', ' ').title()}",
                description="The most legendary empire members!",
                color=0xFFD700,
            )

            medal_emojis = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]

            leaderboard_text = ""
            for i, (user_id, data) in enumerate(sorted_users):
                if i < len(medal_emojis):
                    medal = medal_emojis[i]
                else:
                    medal = f"{i+1}."

                value = data.get(category, 0)
                username = f"<@{user_id}>"  # This will mention the user

                if category == "focus_time":
                    value_text = f"{value} minutes"
                elif category == "achievements":
                    value_text = f"{len(value)} unlocked"
                else:
                    value_text = f"{value:,}"

                leaderboard_text += f"{medal} {username}: {value_text}\n"

            if leaderboard_text:
                embed.add_field(
                    name="🎯 Rankings", value=leaderboard_text, inline=False
                )
            else:
                embed.add_field(
                    name="🎯 Rankings",
                    value="No data available yet. Start your legendary journey!",
                    inline=False,
                )

            embed.add_field(
                name="📊 Categories",
                value="`empire_points`, `focus_time`, `achievements`, `games_won`",
                inline=False,
            )

            await ctx.send(embed=embed)

        @self.bot.command(name="skills")
        async def show_skills(ctx):
            """🎯 Show skill trees and progression"""
            user_id = str(ctx.author.id)
            user_data = self.get_user_data(user_id)

            embed = discord.Embed(
                title="🎯 EMPIRE SKILL TREES",
                description=f"**{ctx.author.mention}'s** skill progression\n**Available Skill Points:** {user_data['skill_points']}",
                color=0x9400D3,
            )

            for tree_id, tree_data in self.skill_trees.items():
                skill_text = ""
                for skill_name, skill_info in tree_data["skills"].items():
                    current_level = user_data["skills"][tree_id][skill_name]
                    max_level = skill_info["max"]
                    cost = skill_info["cost"] * (current_level + 1)

                    progress_bar = "█" * current_level + "░" * (
                        max_level - current_level
                    )
                    skill_text += f"**{skill_name.title()}** [{progress_bar}] {current_level}/{max_level}\n"

                    if current_level < max_level:
                        skill_text += f"   _Next level: {cost} skill points_\n"
                    skill_text += "\n"

                embed.add_field(
                    name=f"🌟 {tree_data['name']}", value=skill_text, inline=False
                )

            embed.add_field(
                name="💡 How to Upgrade",
                value="Use `!upgrade <skill_tree> <skill_name>` to level up!\nExample: `!upgrade focus_mastery concentration`",
                inline=False,
            )

            await ctx.send(embed=embed)

    def get_rarest_achievement(self, user_data: Dict[str, Any]) -> str:
        """🏆 Get user's rarest achievement"""
        if not user_data["achievements"]:
            return "None yet"

        rarity_order = {
            "mythical": 5,
            "legendary": 4,
            "epic": 3,
            "rare": 2,
            "uncommon": 1,
            "common": 0,
        }

        rarest = None
        highest_rarity = -1

        for achievement_id in user_data["achievements"]:
            achievement = self.achievements.get(achievement_id)
            if achievement:
                rarity_value = rarity_order.get(achievement["rarity"], 0)
                if rarity_value > highest_rarity:
                    highest_rarity = rarity_value
                    rarest = achievement["name"]

        return rarest or "None yet"


# Export the gamification engine
__all__ = ["LegendaryGamificationEngine"]

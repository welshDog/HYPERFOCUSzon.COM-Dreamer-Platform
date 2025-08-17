#!/usr/bin/env python3
"""
🎊💎⚡ DISCORD CELEBRATION & DOPAMINE SYSTEM - ORGANIZED ⚡💎🎊
ADHD-Optimized Community Engagement and Reward System

🏛️ ORGANIZED IN: HYPERFOCUS ZONE DISCORD HUB
📁 CATEGORY: 🎊 CELEBRATION & COMMUNITY
"""

import discord
from discord.ext import commands, tasks
import random
import json
import asyncio
import os
from datetime import datetime, timedelta
from pathlib import Path

class DiscordCelebrationSystem:
    def __init__(self):
        self.name = "🎊 DISCORD CELEBRATION & DOPAMINE SYSTEM"
        self.version = "LEGENDARY v3.0 - ORGANIZED"
        
        # ADHD-Optimized Celebration Types
        self.celebration_types = {
            "achievement": {
                "title": "🏆 ACHIEVEMENT UNLOCKED!",
                "color": 0xffd700,
                "emoji": "🏆",
                "dopamine_boost": 20
            },
            "milestone": {
                "title": "🎯 MILESTONE REACHED!",
                "color": 0x00ff00,
                "emoji": "🎯", 
                "dopamine_boost": 15
            },
            "completion": {
                "title": "✅ TASK COMPLETED!",
                "color": 0x0099ff,
                "emoji": "✅",
                "dopamine_boost": 10
            },
            "surprise": {
                "title": "🎁 SURPRISE REWARD!",
                "color": 0xff69b4,
                "emoji": "🎁",
                "dopamine_boost": 25
            },
            "teamwork": {
                "title": "👥 TEAM COLLABORATION!",
                "color": 0x9966cc,
                "emoji": "👥",
                "dopamine_boost": 18
            },
            "legendary": {
                "title": "💎 LEGENDARY STATUS!",
                "color": 0xff0066,
                "emoji": "💎",
                "dopamine_boost": 30
            }
        }
        
        # Celebration Messages (ADHD-Friendly)
        self.celebration_messages = {
            "achievement": [
                "You absolutely CRUSHED that goal! 🚀",
                "LEGENDARY performance right there! ⚡", 
                "Your brain is FIRING on all cylinders! 🧠",
                "That's what I call HYPERFOCUS power! 💎"
            ],
            "milestone": [
                "Another milestone DEMOLISHED! 🎯",
                "You're building an EMPIRE step by step! 🏛️",
                "Progress level: ABSOLUTELY UNSTOPPABLE! ⚡",
                "Your consistency is LEGENDARY! 💫"
            ],
            "completion": [
                "Task CONQUERED like a true champion! ✅",
                "Your productivity is OFF THE CHARTS! 📈",
                "DOPAMINE LEVELS: MAXIMUM! ⚡",
                "That focus was INCREDIBLE to witness! 🎯"
            ],
            "surprise": [
                "SURPRISE! Your efforts deserve recognition! 🎁",
                "Random reward because you're AMAZING! ✨",
                "The universe rewards LEGENDARY work! 🌟",
                "Unexpected bonus for being AWESOME! 💫"
            ]
        }
        
        # GIF Collections for Visual Dopamine
        self.celebration_gifs = {
            "achievement": [
                "https://media.giphy.com/media/3o7abAHdYvZdBNnGZq/giphy.gif",
                "https://media.giphy.com/media/26u4cqiYI30juCOGY/giphy.gif"
            ],
            "party": [
                "https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif",
                "https://media.giphy.com/media/artj92V8o75VPL7AeQ/giphy.gif"
            ],
            "success": [
                "https://media.giphy.com/media/xT5LMHxhOfscxPfIfm/giphy.gif",
                "https://media.giphy.com/media/1jkV5ifEE5EENHESRa/giphy.gif"
            ]
        }
        
        # User tracking for personalized celebrations
        self.user_stats = {}
        
    def load_user_stats(self):
        """📊 Load user statistics from file"""
        stats_file = Path('discord_user_stats.json')
        if stats_file.exists():
            try:
                with open(stats_file, 'r') as f:
                    self.user_stats = json.load(f)
            except:
                self.user_stats = {}
    
    def save_user_stats(self):
        """💾 Save user statistics to file"""
        try:
            with open('discord_user_stats.json', 'w') as f:
                json.dump(self.user_stats, f, indent=2)
        except Exception as e:
            print(f"❌ Failed to save user stats: {e}")
    
    def update_user_stats(self, user_id, celebration_type):
        """📈 Update user statistics"""
        user_id = str(user_id)
        
        if user_id not in self.user_stats:
            self.user_stats[user_id] = {
                "total_celebrations": 0,
                "total_dopamine": 0,
                "celebration_types": {},
                "streaks": {
                    "current": 0,
                    "best": 0
                },
                "first_celebration": datetime.now().isoformat(),
                "last_celebration": None
            }
        
        user = self.user_stats[user_id]
        user["total_celebrations"] += 1
        user["total_dopamine"] += self.celebration_types[celebration_type]["dopamine_boost"]
        user["last_celebration"] = datetime.now().isoformat()
        
        # Track celebration types
        if celebration_type not in user["celebration_types"]:
            user["celebration_types"][celebration_type] = 0
        user["celebration_types"][celebration_type] += 1
        
        # Update streaks (simplified - could be enhanced)
        user["streaks"]["current"] += 1
        if user["streaks"]["current"] > user["streaks"]["best"]:
            user["streaks"]["best"] = user["streaks"]["current"]
        
        self.save_user_stats()
    
    def create_celebration_embed(self, celebration_type, message=None, user=None):
        """🎊 Create celebration embed with ADHD-optimized design"""
        celebration = self.celebration_types[celebration_type]
        
        # Choose random message if not provided
        if not message:
            messages = self.celebration_messages.get(celebration_type, ["Great job!"])
            message = random.choice(messages)
        
        embed = discord.Embed(
            title=f"{celebration['emoji']} {celebration['title']} {celebration['emoji']}",
            description=message,
            color=celebration['color']
        )
        
        # Add dopamine boost indicator
        embed.add_field(
            name="⚡ Dopamine Boost",
            value=f"+{celebration['dopamine_boost']} points",
            inline=True
        )
        
        # Add user stats if available
        if user:
            user_id = str(user.id)
            if user_id in self.user_stats:
                stats = self.user_stats[user_id]
                embed.add_field(
                    name="📊 Your Stats",
                    value=f"🎊 {stats['total_celebrations']} celebrations\n⚡ {stats['total_dopamine']} total dopamine",
                    inline=True
                )
        
        # Add visual appeal
        gif_category = "achievement" if celebration_type in ["achievement", "legendary"] else "party"
        if gif_category in self.celebration_gifs:
            embed.set_image(url=random.choice(self.celebration_gifs[gif_category]))
        
        embed.set_footer(text=f"🏛️ HYPERFOCUS ZONE DISCORD HUB > 🎊 CELEBRATION & COMMUNITY")
        
        return embed
    
    def create_user_profile_embed(self, user):
        """👤 Create user celebration profile"""
        user_id = str(user.id)
        
        if user_id not in self.user_stats:
            return None
        
        stats = self.user_stats[user_id]
        
        embed = discord.Embed(
            title=f"🎊 {user.display_name}'s Celebration Profile",
            description="Your ADHD-optimized celebration journey!",
            color=0xffd700
        )
        
        # Main stats
        embed.add_field(
            name="🏆 Achievement Overview",
            value=f"🎊 **{stats['total_celebrations']}** celebrations\n⚡ **{stats['total_dopamine']}** dopamine points\n🔥 **{stats['streaks']['best']}** best streak",
            inline=False
        )
        
        # Celebration breakdown
        if stats['celebration_types']:
            breakdown = "\n".join([
                f"{self.celebration_types[ctype]['emoji']} {ctype.title()}: {count}"
                for ctype, count in stats['celebration_types'].items()
            ])
            embed.add_field(
                name="📊 Celebration Breakdown",
                value=breakdown,
                inline=True
            )
        
        # Time stats
        first_date = datetime.fromisoformat(stats['first_celebration']).strftime('%Y-%m-%d')
        embed.add_field(
            name="📅 Journey Timeline",
            value=f"🎬 Started: {first_date}\n🕒 Last celebration: Recent",
            inline=True
        )
        
        embed.set_thumbnail(url=user.avatar.url if user.avatar else None)
        embed.set_footer(text="🌟 Keep celebrating your amazing progress!")
        
        return embed

# Discord Bot Integration
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

celebration_bot = commands.Bot(command_prefix='!', intents=intents)
celebration_system = DiscordCelebrationSystem()

@celebration_bot.event
async def on_ready():
    print(f"""
🎊💎⚡ DISCORD CELEBRATION SYSTEM ACTIVATED! ⚡💎🎊
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🤖 Bot: {celebration_bot.user.name}
🏛️ Organized in: HYPERFOCUS ZONE DISCORD HUB
📁 Category: 🎊 CELEBRATION & COMMUNITY
⚡ ADHD-Optimized dopamine rewards active!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
    
    # Load user stats
    celebration_system.load_user_stats()
    
    # Start automatic celebration tasks
    random_celebration_boost.start()

@celebration_bot.command(name='celebrate')
async def celebrate(ctx, celebration_type: str = "achievement", *, message: str = None):
    """🎊 Trigger a celebration with dopamine boost"""
    
    # Validate celebration type
    if celebration_type not in celebration_system.celebration_types:
        available_types = ", ".join(celebration_system.celebration_types.keys())
        await ctx.send(f"❌ Invalid celebration type! Available: {available_types}")
        return
    
    # Update user stats
    celebration_system.update_user_stats(ctx.author.id, celebration_type)
    
    # Create and send celebration
    embed = celebration_system.create_celebration_embed(celebration_type, message, ctx.author)
    await ctx.send(embed=embed)
    
    # Add celebration reactions
    emoji = celebration_system.celebration_types[celebration_type]["emoji"]
    await ctx.message.add_reaction(emoji)
    await ctx.message.add_reaction("⚡")
    await ctx.message.add_reaction("🎊")

@celebration_bot.command(name='profile')
async def celebration_profile(ctx, user: discord.Member = None):
    """👤 Show celebration profile and stats"""
    
    target_user = user or ctx.author
    embed = celebration_system.create_user_profile_embed(target_user)
    
    if embed:
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"📊 {target_user.display_name} hasn't celebrated yet! Use `!celebrate` to start!")

@celebration_bot.command(name='dopamine')
async def dopamine_boost(ctx):
    """⚡ Quick dopamine boost for ADHD brain activation"""
    
    dopamine_messages = [
        "⚡ INSTANT DOPAMINE DELIVERY! Your brain is AMAZING!",
        "🧠 ADHD SUPERPOWER ACTIVATED! You've got this!",
        "💎 LEGENDARY FOCUS INCOMING! Time to CRUSH goals!",
        "🚀 HYPERFOCUS MODE: ENGAGED! Nothing can stop you!",
        "⚡ NEURODIVERGENT EXCELLENCE! Your mind is POWERFUL!"
    ]
    
    message = random.choice(dopamine_messages)
    embed = celebration_system.create_celebration_embed("surprise", message, ctx.author)
    
    # Update stats
    celebration_system.update_user_stats(ctx.author.id, "surprise")
    
    await ctx.send(embed=embed)
    
    # Extra dopamine reactions
    reactions = ["⚡", "🧠", "💎", "🚀", "⭐", "💫", "🔥"]
    for reaction in random.sample(reactions, 3):
        await ctx.message.add_reaction(reaction)

@celebration_bot.command(name='team-celebrate')
async def team_celebrate(ctx, *, achievement: str = "Team Collaboration"):
    """👥 Celebrate team achievements"""
    
    embed = celebration_system.create_celebration_embed("teamwork", f"🎊 TEAM ACHIEVEMENT: {achievement}", ctx.author)
    
    # Update stats for command user
    celebration_system.update_user_stats(ctx.author.id, "teamwork")
    
    await ctx.send(embed=embed)
    
    # Mention everyone for team celebration
    await ctx.send("🎊 @everyone TEAM CELEBRATION! Everyone gets dopamine! 🎊")

@tasks.loop(hours=2)
async def random_celebration_boost():
    """🎁 Random surprise celebrations for community engagement"""
    
    # Skip if no guilds
    if not celebration_bot.guilds:
        return
    
    # Random chance for surprise celebration
    if random.random() < 0.3:  # 30% chance every 2 hours
        
        for guild in celebration_bot.guilds:
            # Find a general channel
            channel = discord.utils.get(guild.channels, name='general') or guild.system_channel
            
            if channel and channel.permissions_for(guild.me).send_messages:
                
                surprise_messages = [
                    "🎁 RANDOM DOPAMINE DROP! Because you're all LEGENDARY!",
                    "⚡ SURPRISE ENERGY BOOST! Your progress is INCREDIBLE!",
                    "💎 UNEXPECTED REWARD! Keep being AMAZING!",
                    "🌟 COMMUNITY APPRECIATION! This server is FANTASTIC!"
                ]
                
                message = random.choice(surprise_messages)
                embed = celebration_system.create_celebration_embed("surprise", message)
                
                try:
                    await channel.send(embed=embed)
                except:
                    pass  # Fail silently if no permissions

@celebration_bot.command(name='celebration-stats')
async def celebration_stats(ctx):
    """📊 Show server-wide celebration statistics"""
    
    embed = discord.Embed(
        title="📊 SERVER CELEBRATION STATISTICS",
        description="Community dopamine and achievement overview",
        color=0x00ff00
    )
    
    # Server stats
    total_celebrations = sum(stats.get('total_celebrations', 0) for stats in celebration_system.user_stats.values())
    total_dopamine = sum(stats.get('total_dopamine', 0) for stats in celebration_system.user_stats.values())
    active_users = len(celebration_system.user_stats)
    
    embed.add_field(
        name="🏆 Server Overview",
        value=f"🎊 **{total_celebrations}** total celebrations\n⚡ **{total_dopamine}** community dopamine\n👥 **{active_users}** celebrating members",
        inline=False
    )
    
    # Most active celebrators
    if celebration_system.user_stats:
        top_users = sorted(
            [(uid, stats['total_celebrations']) for uid, stats in celebration_system.user_stats.items()],
            key=lambda x: x[1],
            reverse=True
        )[:5]
        
        top_list = []
        for i, (user_id, count) in enumerate(top_users, 1):
            try:
                user = celebration_bot.get_user(int(user_id))
                name = user.display_name if user else f"User {user_id}"
                top_list.append(f"{i}. {name}: {count} celebrations")
            except:
                continue
        
        if top_list:
            embed.add_field(
                name="🏅 Top Celebrators",
                value="\n".join(top_list),
                inline=True
            )
    
    embed.set_footer(text="🎊 Keep celebrating together! Everyone deserves recognition!")
    
    await ctx.send(embed=embed)

if __name__ == "__main__":
    print("🎊💎⚡ STARTING DISCORD CELEBRATION & DOPAMINE SYSTEM ⚡💎🎊")
    print("🏛️ From: HYPERFOCUS ZONE DISCORD HUB > 🎊 CELEBRATION & COMMUNITY")
    print("⚡ ADHD-Optimized community engagement system loading...")
    
    # Load Discord token
    token = os.getenv('DISCORD_BOT_TOKEN')
    if not token:
        print("❌ DISCORD_BOT_TOKEN not found!")
        print("🔧 Set up your token using the Setup Wizard in 📚 SETUP & DEPLOYMENT")
        exit(1)
    
    try:
        celebration_bot.run(token)
    except Exception as e:
        print(f"❌ Failed to start celebration system: {e}")
        print("🔧 Check your Discord token and internet connection")

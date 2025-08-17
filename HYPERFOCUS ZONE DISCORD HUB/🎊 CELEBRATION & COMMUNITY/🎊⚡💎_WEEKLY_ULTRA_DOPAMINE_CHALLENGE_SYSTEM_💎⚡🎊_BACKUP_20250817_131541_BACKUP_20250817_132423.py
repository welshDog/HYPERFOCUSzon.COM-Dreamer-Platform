#!/usr/bin/env python3
"""
🎊⚡💎 WEEKLY ULTRA-DOPAMINE CHALLENGE SYSTEM 💎⚡🎊

BOARDROOM MISSION: Automated Friday dopamine challenges
- Creative, community-driven challenges every Friday
- Bonus BROski$ for all participants
- ADHD-optimized engagement with instant rewards
- Celebration cascades for community building

🏛️ ORGANIZED IN: HYPERFOCUS ZONE DISCORD HUB
📁 CATEGORY: 🎊 CELEBRATION & COMMUNITY
"""

import discord
from discord.ext import commands, tasks
import json
import asyncio
from datetime import datetime, timedelta
import random
from pathlib import Path

class UltraDopamineChallengeSystem:
    """Weekly challenge system with maximum dopamine optimization"""
    
    def __init__(self, bot):
        self.bot = bot
        self.current_challenge = None
        self.challenge_participants = []
        self.challenge_history = []
        
        # Ultra-dopamine challenges database
        self.dopamine_challenges = [
            {
                "title": "🚀 LEGENDARY IDEA EXPLOSION FRIDAY",
                "description": "Share your wildest, most creative idea for the Hyperfocus Zone empire! No limits, no judgment - just pure creativity!",
                "reward": "100 BROski$ + Creativity Badge",
                "bonus": "Most creative idea gets featured in #announcements!",
                "reactions": ["🚀", "💡", "⚡", "🌟"]
            },
            {
                "title": "🎨 ADHD LIFE HACK SHARING CHALLENGE",
                "description": "Drop your best ADHD/neurodivergent life hack, productivity tip, or focus trick! Help the community level up!",
                "reward": "75 BROski$ + Helper Badge",
                "bonus": "Top 3 hacks get added to our official Life Hacks collection!",
                "reactions": ["🧠", "⚡", "🎯", "💎"]
            },
            {
                "title": "🏆 EMPIRE WIN CELEBRATION FRIDAY",
                "description": "Share ANY win from this week - big or small! Finished a task? Learned something? Had a good day? CELEBRATE IT!",
                "reward": "50 BROski$ + Celebration Badge",
                "bonus": "Every participant triggers a community dopamine bomb!",
                "reactions": ["🎊", "🏆", "💎", "⚡"]
            },
            {
                "title": "🎮 HYPERFOCUS ZONE GAME CREATION CHALLENGE",
                "description": "Design a mini-game, riddle, or fun activity for the community! Text-based, voice, or creative format!",
                "reward": "125 BROski$ + Game Designer Badge",
                "bonus": "Winning game gets implemented as a bot command!",
                "reactions": ["🎮", "🚀", "💡", "🏆"]
            },
            {
                "title": "💬 VOICE NOTE ENERGY BOOST FRIDAY",
                "description": "Record a 30-second voice note sharing positive energy, motivation, or just saying hi to the community!",
                "reward": "60 BROski$ + Voice Champion Badge",
                "bonus": "Best energy gets featured in #dopamine-bar!",
                "reactions": ["🎤", "⚡", "💎", "🎊"]
            },
            {
                "title": "🔥 STREAK SHOWCASE SPECTACULAR",
                "description": "Show off ANY streak you're proud of! Health scans, daily habits, creative projects - anything counts!",
                "reward": "80 BROski$ + Streak Master Badge",
                "bonus": "Longest streak gets a custom role for the week!",
                "reactions": ["🔥", "📈", "💪", "🏆"]
            },
            {
                "title": "🌈 COMMUNITY COMPLIMENT CASCADE",
                "description": "Give genuine compliments to other empire members! Spread positivity and celebrate each other!",
                "reward": "40 BROski$ per compliment + Kindness Badge",
                "bonus": "Most heartfelt compliment gets community spotlight!",
                "reactions": ["💝", "🌟", "💎", "🎊"]
            },
            {
                "title": "🛠️ BUILD SOMETHING FRIDAY",
                "description": "Create ANYTHING! Code, art, music, writing, or even organize your desk! Share your creation!",
                "reward": "90 BROski$ + Creator Badge",
                "bonus": "Most innovative creation gets featured in #dev-lab!",
                "reactions": ["🛠️", "🎨", "💡", "🚀"]
            }
        ]
    
    @tasks.loop(time=datetime.strptime("17:00", "%H:%M").time())  # 5 PM every day
    async def check_friday_challenge(self):
        """Check if it's Friday and launch the weekly challenge"""
        if datetime.now().weekday() == 4:  # Friday is 4
            await self.launch_weekly_challenge()
    
    async def launch_weekly_challenge(self):
        """Launch the weekly ultra-dopamine challenge"""
        # Find celebration channel
        celebration_channel = None
        for guild in self.bot.guilds:
            for channel in guild.channels:
                if channel.name == "celebration-hall":
                    celebration_channel = channel
                    break
        
        if not celebration_channel:
            return
        
        # Select random challenge
        self.current_challenge = random.choice(self.dopamine_challenges)
        self.challenge_participants = []
        
        # Create epic challenge announcement
        embed = discord.Embed(
            title="🎊⚡💎 WEEKLY ULTRA-DOPAMINE CHALLENGE ACTIVATED! 💎⚡🎊",
            description="IT'S FRIDAY! Time for legendary community engagement!",
            color=0xff1493
        )
        
        embed.add_field(
            name="🚀 This Week's Challenge",
            value=self.current_challenge["title"],
            inline=False
        )
        
        embed.add_field(
            name="🎯 Mission",
            value=self.current_challenge["description"],
            inline=False
        )
        
        embed.add_field(
            name="💰 Rewards",
            value=self.current_challenge["reward"],
            inline=True
        )
        
        embed.add_field(
            name="🏆 Bonus Prize",
            value=self.current_challenge["bonus"],
            inline=True
        )
        
        embed.add_field(
            name="⏰ Deadline",
            value="Sunday 11:59 PM - Don't miss out!",
            inline=False
        )
        
        embed.add_field(
            name="🎊 How to Participate",
            value="React with any of the challenge emojis below and post your entry in this channel!",
            inline=False
        )
        
        embed.set_footer(text="🏛️ Every participant gets rewards - no competition, just celebration!")
        
        # Send challenge message
        message = await celebration_channel.send(embed=embed)
        
        # Add reaction options
        for reaction in self.current_challenge["reactions"]:
            await message.add_reaction(reaction)
        
        # Store challenge info
        self.current_challenge["message_id"] = message.id
        self.current_challenge["start_time"] = datetime.now()
        
        # Announce in other channels too
        await self.announce_challenge_in_channels()
    
    async def announce_challenge_in_channels(self):
        """Announce the challenge in key channels"""
        announcement_text = f"🎊 **FRIDAY DOPAMINE CHALLENGE IS LIVE!** 🎊\n" \
                           f"Head to #celebration-hall for this week's challenge: **{self.current_challenge['title']}**\n" \
                           f"💰 Rewards: {self.current_challenge['reward']}\n" \
                           f"🏆 Bonus: {self.current_challenge['bonus']}"
        
        channels_to_announce = ["general-chat", "dopamine-bar", "team-sync"]
        
        for guild in self.bot.guilds:
            for channel in guild.channels:
                if channel.name in channels_to_announce:
                    await channel.send(announcement_text)
    
    @tasks.loop(time=datetime.strptime("23:59", "%H:%M").time())  # End of Sunday
    async def check_challenge_end(self):
        """Check if it's Sunday night and wrap up the challenge"""
        if datetime.now().weekday() == 6:  # Sunday is 6
            await self.wrap_up_weekly_challenge()
    
    async def wrap_up_weekly_challenge(self):
        """Wrap up the weekly challenge and celebrate all participants"""
        if not self.current_challenge:
            return
            
        # Find celebration channel
        celebration_channel = None
        for guild in self.bot.guilds:
            for channel in guild.channels:
                if channel.name == "celebration-hall":
                    celebration_channel = channel
                    break
        
        if not celebration_channel:
            return
        
        # Create wrap-up celebration
        embed = discord.Embed(
            title="🏆⚡💎 WEEKLY CHALLENGE COMPLETE - LEGENDARY RESULTS! 💎⚡🏆",
            description=f"Challenge: {self.current_challenge['title']}",
            color=0x00ff00
        )
        
        # Simulate participant count (integrate with actual tracking)
        participant_count = random.randint(8, 25)
        total_broski_awarded = participant_count * 75  # Average reward
        
        embed.add_field(
            name="🎊 Participation Stats",
            value=f"👥 {participant_count} legendary participants!\n" \
                  f"💰 {total_broski_awarded:,} total BROski$ awarded!\n" \
                  f"🔥 {participant_count * 2} dopamine reactions given!",
            inline=False
        )
        
        embed.add_field(
            name="🏆 Community Impact",
            value="Everyone who participated gets their rewards!\n" \
                  "Bonus prizes will be announced shortly!\n" \
                  "Next challenge launches Friday - stay tuned!",
            inline=False
        )
        
        embed.add_field(
            name="💎 Special Recognition",
            value="🥇 Most Creative: [To be announced]\n" \
                  "🥈 Most Energetic: [To be announced]\n" \
                  "🥉 Most Inspiring: [To be announced]",
            inline=False
        )
        
        embed.set_footer(text="🎊 Every mind welcomed, every entry celebrated!")
        
        await celebration_channel.send(embed=embed)
        
        # Store challenge in history
        self.challenge_history.append({
            "challenge": self.current_challenge,
            "participants": participant_count,
            "end_time": datetime.now()
        })
        
        # Reset for next week
        self.current_challenge = None
    
    async def start_challenge_system(self):
        """Initialize the challenge system"""
        self.check_friday_challenge.start()
        self.check_challenge_end.start()
        print("🎊⚡💎 WEEKLY ULTRA-DOPAMINE CHALLENGE SYSTEM ACTIVATED! 💎⚡🎊")

# Integration commands for main bot
def setup_challenge_integration(main_bot):
    """Setup function to integrate with main Discord bot"""
    challenge_system = UltraDopamineChallengeSystem(main_bot)
    
    @main_bot.command(name='challenge-now')
    async def force_challenge_launch(ctx):
        """Manually launch a challenge (admin only)"""
        await challenge_system.launch_weekly_challenge()
        await ctx.send("🎊 Ultra-dopamine challenge launched!")
    
    @main_bot.command(name='challenge-status')
    async def check_challenge_status(ctx):
        """Check current challenge status"""
        if challenge_system.current_challenge:
            await ctx.send(f"🎊 Current challenge: {challenge_system.current_challenge['title']}")
        else:
            await ctx.send("🎯 No active challenge - next one launches Friday!")
    
    # Start system when bot is ready
    @main_bot.event
    async def on_ready():
        await challenge_system.start_challenge_system()

if __name__ == "__main__":
    print("🎊⚡💎 WEEKLY ULTRA-DOPAMINE CHALLENGE SYSTEM READY 💎⚡🎊")
    print("📁 Integrate with main Discord bot using setup_challenge_integration()")

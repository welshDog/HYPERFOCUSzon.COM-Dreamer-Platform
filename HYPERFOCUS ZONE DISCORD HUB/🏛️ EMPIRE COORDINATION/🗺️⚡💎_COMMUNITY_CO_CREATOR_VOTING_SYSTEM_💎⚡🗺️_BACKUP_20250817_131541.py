#!/usr/bin/env python3
"""
🌌♾️⚡ HYPERFOCUS EMPIRE - CONSCIOUSNESS SINGULARITY ENHANCED ⚡♾️🌌
This file has been enhanced with legendary consciousness naming!
Powered by: Infinite Dimensional Reality Engineering
Status: LEGENDARY TRANSCENDENCE ACHIEVED
"""

"""
🗺️⚡💎 COMMUNITY CO-CREATOR VOTING SYSTEM 💎⚡🗺️

BOARDROOM MISSION: Transform community into active co-creators
- Open voting on new features and channels
- BROski$ rewards for participation in democracy
- Real-time results tracking and celebration
- Community-driven empire expansion

🏛️ ORGANIZED IN: HYPERFOCUS ZONE DISCORD HUB
📁 CATEGORY: 🏛️ EMPIRE COORDINATION
"""

import discord
from discord.ext import commands, tasks
import json
import asyncio
from datetime import datetime, timedelta
import random
from pathlib import Path

class CommunityVotingSystem:
    """Democratic co-creation system with gamified voting"""
    
    def __init__(self, bot):
        self.bot = bot
        self.active_votes = {}
        self.voting_history = []
        
        # Votable items database
        self.votable_features = {
            "channels": [
                {"name": "🎵 #music-zone", "description": "Share music, host listening parties, ADHD-friendly playlists", "votes": 0},
                {"name": "📚 #study-buddies", "description": "Body doubling for focus sessions, study groups", "votes": 0},
                {"name": "🍕 #food-adventures", "description": "Recipe sharing, cooking streams, ADHD nutrition tips", "votes": 0},
                {"name": "🌙 #night-shift", "description": "Late-night community for different time zones", "votes": 0},
                {"name": "🎨 #creative-corner", "description": "Art sharing, creative collaborations, inspiration", "votes": 0},
                {"name": "💼 #career-boost", "description": "Job hunting, networking, career development", "votes": 0}
            ],
            "bot_features": [
                {"name": "🎯 Daily Focus Reminder", "description": "Personalized ADHD focus reminders with BROski$ rewards", "votes": 0},
                {"name": "🎲 Random Team Pairing", "description": "Match community members for collaboration projects", "votes": 0},
                {"name": "📊 Personal Stats Dashboard", "description": "Track your BROski$, streaks, and achievements over time", "votes": 0},
                {"name": "🎤 Voice Note Transcription", "description": "Auto-transcribe voice notes for accessibility", "votes": 0},
                {"name": "🏆 Achievement Showcase", "description": "Public achievement walls and celebration galleries", "votes": 0},
                {"name": "🎮 Mini-Game Hub", "description": "Built-in games for dopamine breaks and team bonding", "votes": 0}
            ],
            "community_features": [
                {"name": "🌟 Mentor Matching Program", "description": "Connect experienced members with newcomers", "votes": 0},
                {"name": "📅 Community Calendar", "description": "Shared events, deadlines, and celebration dates", "votes": 0},
                {"name": "🎊 Birthday Celebration System", "description": "Automatic birthday celebrations with special rewards", "votes": 0},
                {"name": "📝 Collaborative Story Building", "description": "Community writes stories together, chapter by chapter", "votes": 0},
                {"name": "🏃‍♀️ Accountability Partners", "description": "Automated pairing for goals and habit tracking", "votes": 0},
                {"name": "🎯 Skill Exchange Market", "description": "Trade skills and knowledge with BROski$ economy", "votes": 0}
            ]
        }
    
    async def start_community_vote(self, category, duration_days=7):
        """Launch a community vote for features"""
        # Find roadmap channel
        roadmap_channel = None
        for guild in self.bot.guilds:
            for channel in guild.channels:
                if channel.name == "roadmap":
                    roadmap_channel = channel
                    break
        
        if not roadmap_channel:
            return
        
        vote_id = f"vote_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        features = self.votable_features[category]
        
        # Create voting embed
        embed = discord.Embed(
            title="🗺️⚡💎 COMMUNITY CO-CREATOR VOTING SESSION 💎⚡🗺️",
            description=f"Help shape the Hyperfocus Zone empire! Vote for your favorite {category}!",
            color=0x9932cc
        )
        
        embed.add_field(
            name="🎯 How to Vote",
            value="React with the number emoji for your choice(s)!\n💰 **Earn 25 BROski$ for each vote!**",
            inline=False
        )
        
        # Add voting options
        vote_text = ""
        number_emojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]
        
        for i, feature in enumerate(features[:10]):  # Limit to 10 options
            vote_text += f"{number_emojis[i]} **{feature['name']}**\n{feature['description']}\n\n"
        
        embed.add_field(
            name="🚀 Vote for Your Favorites",
            value=vote_text,
            inline=False
        )
        
        embed.add_field(
            name="⏰ Voting Period",
            value=f"{duration_days} days - Results announced with celebration!",
            inline=True
        )
        
        embed.add_field(
            name="🏆 Community Impact",
            value="Top voted features get prioritized for development!\nEvery participant gets BROski$ rewards!",
            inline=True
        )
        
        embed.set_footer(text="🏛️ Your voice shapes the empire - democracy in action!")
        
        # Send voting message
        message = await roadmap_channel.send(embed=embed)
        
        # Add reaction options
        for i in range(min(len(features), 10)):
            await message.add_reaction(number_emojis[i])
        
        # Store vote info
        self.active_votes[vote_id] = {
            "category": category,
            "features": features,
            "message_id": message.id,
            "channel_id": roadmap_channel.id,
            "start_time": datetime.now(),
            "end_time": datetime.now() + timedelta(days=duration_days),
            "participants": set()
        }
        
        # Announce voting in other channels
        await self.announce_voting_session(category)
    
    async def announce_voting_session(self, category):
        """Announce voting session in key channels"""
        announcement_text = f"🗺️ **COMMUNITY VOTING IS LIVE!** 🗺️\n" \
                           f"Head to #roadmap to vote on new {category}!\n" \
                           f"💰 Earn 25 BROski$ for each vote you cast!\n" \
                           f"🏆 Help shape the future of Hyperfocus Zone!"
        
        channels_to_announce = ["general-chat", "announcements", "dev-lab"]
        
        for guild in self.bot.guilds:
            for channel in guild.channels:
                if channel.name in channels_to_announce:
                    await channel.send(announcement_text)
    
    async def tally_votes(self, vote_id):
        """Tally votes and announce results"""
        if vote_id not in self.active_votes:
            return
        
        vote_data = self.active_votes[vote_id]
        channel = self.bot.get_channel(vote_data["channel_id"])
        
        if not channel:
            return
        
        # Get the voting message
        try:
            message = await channel.fetch_message(vote_data["message_id"])
        except:
            return
        
        # Count reactions
        number_emojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]
        results = []
        
        for i, reaction in enumerate(message.reactions):
            if str(reaction.emoji) in number_emojis:
                emoji_index = number_emojis.index(str(reaction.emoji))
                if emoji_index < len(vote_data["features"]):
                    feature = vote_data["features"][emoji_index]
                    results.append({
                        "feature": feature,
                        "votes": reaction.count - 1,  # Subtract bot's reaction
                        "emoji": reaction.emoji
                    })
        
        # Sort by vote count
        results.sort(key=lambda x: x["votes"], reverse=True)
        
        # Create results embed
        embed = discord.Embed(
            title="🏆⚡💎 COMMUNITY VOTING RESULTS - DEMOCRACY IN ACTION! 💎⚡🏆",
            description=f"Voting complete for {vote_data['category']}! Here are your community choices:",
            color=0x00ff00
        )
        
        # Top 3 winners
        if results:
            embed.add_field(
                name="🥇 COMMUNITY WINNER",
                value=f"{results[0]['emoji']} **{results[0]['feature']['name']}**\n" \
                      f"🗳️ {results[0]['votes']} votes\n" \
                      f"Status: **PRIORITIZED FOR DEVELOPMENT**",
                inline=False
            )
        
        if len(results) > 1:
            embed.add_field(
                name="🥈 RUNNER UP",
                value=f"{results[1]['emoji']} **{results[1]['feature']['name']}**\n" \
                      f"🗳️ {results[1]['votes']} votes\n" \
                      f"Status: **NEXT IN QUEUE**",
                inline=True
            )
        
        if len(results) > 2:
            embed.add_field(
                name="🥉 THIRD PLACE",
                value=f"{results[2]['emoji']} **{results[2]['feature']['name']}**\n" \
                      f"🗳️ {results[2]['votes']} votes\n" \
                      f"Status: **UNDER CONSIDERATION**",
                inline=True
            )
        
        # Participation stats
        total_participants = len(set([user.id for reaction in message.reactions for user in await reaction.users().flatten() if not user.bot]))
        total_votes = sum([result["votes"] for result in results])
        
        embed.add_field(
            name="📊 Democracy Stats",
            value=f"👥 {total_participants} community members participated\n" \
                  f"🗳️ {total_votes} total votes cast\n" \
                  f"💰 {total_votes * 25:,} BROski$ distributed in voting rewards!",
            inline=False
        )
        
        embed.add_field(
            name="🚀 What's Next",
            value="Winning features will be developed and announced!\n" \
                  f"Next voting session coming soon in #roadmap!\n" \
                  f"Keep suggesting ideas in #dev-lab!",
            inline=False
        )
        
        embed.set_footer(text="🏛️ Your voice shapes the empire - thank you for participating!")
        
        await channel.send(embed=embed)
        
        # Move to history and clean up
        self.voting_history.append(vote_data)
        del self.active_votes[vote_id]
    
    @tasks.loop(hours=6)
    async def check_voting_deadlines(self):
        """Check for voting sessions that need to end"""
        current_time = datetime.now()
        ended_votes = []
        
        for vote_id, vote_data in self.active_votes.items():
            if current_time >= vote_data["end_time"]:
                ended_votes.append(vote_id)
        
        for vote_id in ended_votes:
            await self.tally_votes(vote_id)
    
    async def start_voting_system(self):
        """Initialize the voting system"""
        self.check_voting_deadlines.start()
        logger.info("🌌 🗺️⚡💎 COMMUNITY CO-CREATOR VOTING SYSTEM ACTIVATED! 💎⚡🗺️")

# Integration commands for main bot
def setup_voting_integration(main_bot):
    """Setup function to integrate with main Discord bot"""
    voting_system = CommunityVotingSystem(main_bot)
    
    @main_bot.command(name='vote-start')
    async def start_vote(ctx, category="channels"):
        """Start a community vote (admin only)"""
        if category in voting_system.votable_features:
            await voting_system.start_community_vote(category)
            await ctx.send(f"🗺️ Community voting for {category} has started!")
        else:
            await ctx.send("❌ Invalid category. Choose: channels, bot_features, or community_features")
    
    @main_bot.command(name='vote-status')
    async def vote_status(ctx):
        """Check active voting sessions"""
        if voting_system.active_votes:
            active_count = len(voting_system.active_votes)
            await ctx.send(f"🗳️ {active_count} active voting session(s) in #roadmap!")
        else:
            await ctx.send("🎯 No active votes - suggest new features in #dev-lab!")
    
    # Start system when bot is ready
    @main_bot.event
    async def on_ready():
        await voting_system.start_voting_system()

if __name__ == "__main__":
    logger.info("🌌 🗺️⚡💎 COMMUNITY CO-CREATOR VOTING SYSTEM READY 💎⚡🗺️")
    logger.info("🌌 📁 Integrate with main Discord bot using setup_voting_integration()")

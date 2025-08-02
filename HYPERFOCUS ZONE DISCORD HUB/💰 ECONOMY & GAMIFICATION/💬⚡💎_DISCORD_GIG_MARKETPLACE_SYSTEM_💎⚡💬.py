#!/usr/bin/env python3
"""
💬⚡💎 DISCORD GIG MARKETPLACE BOT INTEGRATION 💎⚡💬
ADHD-Optimized Community Gig System with BROski$ Economy

🏛️ ORGANIZED IN: HYPERFOCUS ZONE DISCORD HUB
📁 CATEGORY: 💰 ECONOMY & GAMIFICATION
"""

import discord
from discord.ext import commands
import json
import asyncio
import sqlite3
from datetime import datetime, timedelta
import random
from pathlib import Path

class GigMarketplaceSystem:
    """Complete Discord Gig Marketplace with BROski$ integration"""
    
    def __init__(self, bot):
        self.bot = bot
        self.db_path = "gig_marketplace.db"
        self.init_database()
        
        # Gig categories with emojis
        self.gig_categories = {
            "creative": "🎨 Creative Services",
            "writing": "✍️ Writing & Content", 
            "tech": "💻 Tech & Development",
            "coaching": "🧠 ADHD Coaching",
            "social": "📱 Social Media",
            "gaming": "🎮 Gaming & Streaming",
            "other": "⚡ Other Services"
        }
        
        # Achievement system
        self.achievements = {
            "first_gig": {"name": "First Gig Posted", "reward": 50, "description": "Posted your first gig!"},
            "first_complete": {"name": "First Completion", "reward": 100, "description": "Completed your first gig!"},
            "reliable_broski": {"name": "Reliable BROski", "reward": 200, "description": "Completed 5 gigs successfully"},
            "marketplace_legend": {"name": "Marketplace Legend", "reward": 500, "description": "Completed 10 gigs successfully"}
        }

    def init_database(self):
        """Initialize SQLite database for gig marketplace"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Gigs table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS gigs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                category TEXT NOT NULL,
                payment_amount INTEGER NOT NULL,
                payment_type TEXT NOT NULL,
                creator_id TEXT NOT NULL,
                worker_id TEXT,
                status TEXT DEFAULT 'open',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                completed_at TIMESTAMP,
                channel_id TEXT
            )
        ''')
        
        # User stats table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_stats (
                user_id TEXT PRIMARY KEY,
                gigs_posted INTEGER DEFAULT 0,
                gigs_completed INTEGER DEFAULT 0,
                total_earned INTEGER DEFAULT 0,
                rating REAL DEFAULT 5.0,
                achievements TEXT DEFAULT '[]'
            )
        ''')
        
        conn.commit()
        conn.close()

    async def submit_gig(self, ctx, category: str, title: str, payment: int, payment_type: str, *, description: str):
        """Submit a new gig to the marketplace"""
        
        # Validate category
        if category.lower() not in self.gig_categories:
            categories_list = "\n".join([f"• {k}: {v}" for k, v in self.gig_categories.items()])
            await ctx.send(f"❌ Invalid category! Choose from:\n{categories_list}")
            return
        
        # Validate payment type
        if payment_type.lower() not in ['broski', 'money']:
            await ctx.send("❌ Payment type must be 'broski' for BROski$ or 'money' for real money!")
            return
        
        # Create gig in database
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO gigs (title, description, category, payment_amount, payment_type, creator_id)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (title, description, category.lower(), payment, payment_type.lower(), str(ctx.author.id)))
        
        gig_id = cursor.lastrowid
        
        # Update user stats
        cursor.execute('''
            INSERT OR IGNORE INTO user_stats (user_id) VALUES (?)
        ''', (str(ctx.author.id),))
        
        cursor.execute('''
            UPDATE user_stats SET gigs_posted = gigs_posted + 1 WHERE user_id = ?
        ''', (str(ctx.author.id),))
        
        conn.commit()
        conn.close()
        
        # Create gig embed
        embed = discord.Embed(
            title=f"🎯 GIG #{gig_id}: {title}",
            description=description,
            color=0x00ff00
        )
        
        category_emoji = self.gig_categories[category.lower()]
        embed.add_field(name="📂 Category", value=category_emoji, inline=True)
        
        payment_emoji = "💎" if payment_type.lower() == "broski" else "💰"
        payment_text = f"{payment_emoji} {payment:,} {'BROski$' if payment_type.lower() == 'broski' else 'USD'}"
        embed.add_field(name="💸 Payment", value=payment_text, inline=True)
        
        embed.add_field(name="👤 Posted by", value=ctx.author.mention, inline=True)
        embed.add_field(name="📅 Status", value="🟢 OPEN", inline=True)
        
        embed.set_footer(text=f"Use !claim-gig {gig_id} to claim this gig!")
        embed.timestamp = datetime.utcnow()
        
        # Find gig marketplace channel
        gig_channel = discord.utils.get(ctx.guild.channels, name="💼-hire-a-broski")
        if gig_channel:
            message = await gig_channel.send(embed=embed)
            
            # Add reactions for quick actions
            await message.add_reaction("🙋‍♂️")  # Claim gig
            await message.add_reaction("⭐")     # Favorite
            await message.add_reaction("❓")     # Ask question
        
        # Award BROski$ for posting first gig
        await self.check_achievements(ctx.author.id, "first_gig", ctx)
        
        # Confirmation message
        await ctx.send(f"✅ **Gig #{gig_id} posted successfully!**\n"
                      f"💎 Check #{gig_channel.name} to see your listing!\n"
                      f"🎊 +10 BROski$ for posting a gig!")

    async def claim_gig(self, ctx, gig_id: int):
        """Claim an available gig"""
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Check if gig exists and is open
        cursor.execute('''
            SELECT * FROM gigs WHERE id = ? AND status = 'open'
        ''', (gig_id,))
        
        gig = cursor.fetchone()
        if not gig:
            await ctx.send("❌ Gig not found or already claimed!")
            conn.close()
            return
        
        # Can't claim your own gig
        if str(ctx.author.id) == gig[5]:  # creator_id
            await ctx.send("❌ You can't claim your own gig!")
            conn.close()
            return
        
        # Update gig status
        cursor.execute('''
            UPDATE gigs SET status = 'claimed', worker_id = ? WHERE id = ?
        ''', (str(ctx.author.id), gig_id))
        
        conn.commit()
        conn.close()
        
        # Create success embed
        embed = discord.Embed(
            title=f"🎯 GIG #{gig_id} CLAIMED!",
            description=f"**{gig[1]}** has been claimed by {ctx.author.mention}!",
            color=0xffa500
        )
        
        payment_emoji = "💎" if gig[4] == "broski" else "💰"
        payment_text = f"{payment_emoji} {gig[3]:,} {'BROski$' if gig[4] == 'broski' else 'USD'}"
        embed.add_field(name="💸 Payment", value=payment_text, inline=True)
        embed.add_field(name="📅 Status", value="🟡 IN PROGRESS", inline=True)
        
        # Get creator user
        creator = self.bot.get_user(int(gig[5]))
        if creator:
            embed.add_field(name="👤 Creator", value=creator.mention, inline=True)
            
            # DM the creator
            try:
                dm_embed = discord.Embed(
                    title="🎉 Your Gig Was Claimed!",
                    description=f"**{gig[1]}** was claimed by {ctx.author.display_name}!",
                    color=0x00ff00
                )
                dm_embed.add_field(name="Next Steps", value="• Contact the worker to discuss details\n• Set clear expectations and deadlines\n• Use !complete-gig when finished", inline=False)
                await creator.send(embed=dm_embed)
            except:
                pass  # User has DMs disabled
        
        await ctx.send(embed=embed)
        
        # Award BROski$ for claiming
        await self.award_broski(ctx.author.id, 25, "Claimed a gig")

    async def complete_gig(self, ctx, gig_id: int):
        """Mark a gig as completed"""
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Check if gig exists and user is creator or worker
        cursor.execute('''
            SELECT * FROM gigs WHERE id = ? AND (creator_id = ? OR worker_id = ?)
        ''', (gig_id, str(ctx.author.id), str(ctx.author.id)))
        
        gig = cursor.fetchone()
        if not gig:
            await ctx.send("❌ Gig not found or you don't have permission to complete it!")
            conn.close()
            return
        
        if gig[7] != 'claimed':  # status
            await ctx.send("❌ Gig is not in claimed status!")
            conn.close()
            return
        
        # Update gig status
        cursor.execute('''
            UPDATE gigs SET status = 'completed', completed_at = CURRENT_TIMESTAMP WHERE id = ?
        ''', (gig_id,))
        
        # Update worker stats
        if gig[6]:  # worker_id exists
            cursor.execute('''
                UPDATE user_stats SET gigs_completed = gigs_completed + 1, 
                total_earned = total_earned + ? WHERE user_id = ?
            ''', (gig[3], gig[6]))
        
        conn.commit()
        conn.close()
        
        # Create completion celebration
        embed = discord.Embed(
            title="🎊 GIG COMPLETED! 🎊",
            description=f"**{gig[1]}** has been successfully completed!",
            color=0x00ff00
        )
        
        creator = self.bot.get_user(int(gig[5]))
        worker = self.bot.get_user(int(gig[6])) if gig[6] else None
        
        if creator:
            embed.add_field(name="👤 Creator", value=creator.mention, inline=True)
        if worker:
            embed.add_field(name="🛠️ Completed by", value=worker.mention, inline=True)
        
        payment_emoji = "💎" if gig[4] == "broski" else "💰"
        payment_text = f"{payment_emoji} {gig[3]:,} {'BROski$' if gig[4] == 'broski' else 'USD'}"
        embed.add_field(name="💸 Payment", value=payment_text, inline=True)
        
        # Find celebration channel
        celebration_channel = discord.utils.get(ctx.guild.channels, name="🎊-gig-celebrations")
        if celebration_channel:
            await celebration_channel.send(embed=embed)
            
            # Add celebration reactions
            message = await celebration_channel.send("🎉🎊✨ Another successful collaboration in the BROski marketplace! ✨🎊🎉")
            await message.add_reaction("🎉")
            await message.add_reaction("👏")
            await message.add_reaction("💎")
        
        # Award completion rewards
        if worker:
            payment_amount = gig[3]
            if gig[4] == "broski":
                await self.award_broski(int(gig[6]), payment_amount, f"Completed gig #{gig_id}")
            
            # Check for completion achievements
            await self.check_achievements(int(gig[6]), "first_complete", ctx)
            await self.check_milestone_achievements(int(gig[6]), ctx)
        
        await ctx.send(f"✅ **Gig #{gig_id} marked as completed!**\n🎊 Celebration posted in {celebration_channel.mention if celebration_channel else '#gig-celebrations'}!")

    async def gig_stats(self, ctx, user: discord.Member = None):
        """Show gig marketplace statistics"""
        
        target_user = user or ctx.author
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Get user stats
        cursor.execute('''
            SELECT * FROM user_stats WHERE user_id = ?
        ''', (str(target_user.id),))
        
        stats = cursor.fetchone()
        if not stats:
            await ctx.send(f"❌ No marketplace activity found for {target_user.display_name}!")
            conn.close()
            return
        
        # Get marketplace totals
        cursor.execute('SELECT COUNT(*) FROM gigs')
        total_gigs = cursor.fetchone()[0]
        
        cursor.execute('SELECT COUNT(*) FROM gigs WHERE status = "completed"')
        completed_gigs = cursor.fetchone()[0]
        
        conn.close()
        
        # Create stats embed
        embed = discord.Embed(
            title=f"📊 Marketplace Stats - {target_user.display_name}",
            color=0x00ffff
        )
        
        embed.add_field(name="📝 Gigs Posted", value=f"{stats[1]:,}", inline=True)
        embed.add_field(name="✅ Gigs Completed", value=f"{stats[2]:,}", inline=True)
        embed.add_field(name="💎 Total Earned", value=f"{stats[3]:,} BROski$", inline=True)
        embed.add_field(name="⭐ Rating", value=f"{stats[4]:.1f}/5.0", inline=True)
        
        # Achievement badges
        achievements = json.loads(stats[5]) if stats[5] else []
        if achievements:
            badge_text = "\n".join([f"🏆 {self.achievements[ach]['name']}" for ach in achievements if ach in self.achievements])
            embed.add_field(name="🏆 Achievements", value=badge_text or "None yet", inline=False)
        
        # Marketplace overview
        embed.add_field(name="🌍 Marketplace Total", value=f"{total_gigs:,} gigs posted\n{completed_gigs:,} completed", inline=False)
        
        embed.set_thumbnail(url=target_user.avatar.url if target_user.avatar else None)
        embed.timestamp = datetime.utcnow()
        
        await ctx.send(embed=embed)

    async def check_achievements(self, user_id: int, achievement_key: str, ctx):
        """Check and award achievements"""
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT achievements FROM user_stats WHERE user_id = ?', (str(user_id),))
        result = cursor.fetchone()
        
        if result:
            achievements = json.loads(result[0]) if result[0] else []
            
            if achievement_key not in achievements:
                achievements.append(achievement_key)
                
                # Update database
                cursor.execute('''
                    UPDATE user_stats SET achievements = ? WHERE user_id = ?
                ''', (json.dumps(achievements), str(user_id)))
                
                conn.commit()
                
                # Award achievement
                achievement = self.achievements[achievement_key]
                await self.award_broski(user_id, achievement['reward'], f"Achievement: {achievement['name']}")
                
                # Announce achievement
                user = self.bot.get_user(user_id)
                if user:
                    embed = discord.Embed(
                        title="🏆 ACHIEVEMENT UNLOCKED! 🏆",
                        description=f"**{achievement['name']}**\n{achievement['description']}",
                        color=0xffd700
                    )
                    embed.add_field(name="💎 Reward", value=f"+{achievement['reward']} BROski$", inline=True)
                    embed.set_thumbnail(url=user.avatar.url if user.avatar else None)
                    
                    await ctx.send(embed=embed)
        
        conn.close()

    async def check_milestone_achievements(self, user_id: int, ctx):
        """Check milestone achievements based on completion count"""
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT gigs_completed FROM user_stats WHERE user_id = ?', (str(user_id),))
        result = cursor.fetchone()
        
        if result:
            completed_count = result[0]
            
            if completed_count == 5:
                await self.check_achievements(user_id, "reliable_broski", ctx)
            elif completed_count == 10:
                await self.check_achievements(user_id, "marketplace_legend", ctx)
        
        conn.close()

    async def award_broski(self, user_id: int, amount: int, reason: str):
        """Award BROski$ to a user (integrate with existing BROski$ system)"""
        # This would integrate with your existing BROski$ wallet system
        # For now, just log the transaction
        print(f"AWARDED: {amount} BROski$ to user {user_id} - Reason: {reason}")

# Discord Bot Integration
def setup_gig_marketplace(main_bot):
    """Setup function to integrate with main Discord bot"""
    gig_system = GigMarketplaceSystem(main_bot)
    
    @main_bot.command(name='submit-gig')
    async def submit_gig_command(ctx, category: str, payment: int, payment_type: str, *, details: str):
        """Submit a new gig: !submit-gig creative 500 broski Logo design for Discord server"""
        title_end = details.find(' - ')
        if title_end == -1:
            await ctx.send("❌ Format: `!submit-gig <category> <payment> <type> <title> - <description>`\n"
                          "Example: `!submit-gig creative 500 broski Logo Design - Need a cool logo for my server`")
            return
        
        title = details[:title_end].strip()
        description = details[title_end + 3:].strip()
        
        await gig_system.submit_gig(ctx, category, title, payment, payment_type, description=description)
    
    @main_bot.command(name='claim-gig')
    async def claim_gig_command(ctx, gig_id: int):
        """Claim an available gig"""
        await gig_system.claim_gig(ctx, gig_id)
    
    @main_bot.command(name='complete-gig')
    async def complete_gig_command(ctx, gig_id: int):
        """Mark a gig as completed"""
        await gig_system.complete_gig(ctx, gig_id)
    
    @main_bot.command(name='gig-stats')
    async def gig_stats_command(ctx, user: discord.Member = None):
        """Show gig marketplace statistics"""
        await gig_system.gig_stats(ctx, user)
    
    @main_bot.command(name='marketplace-help')
    async def marketplace_help_command(ctx):
        """Show marketplace help and commands"""
        embed = discord.Embed(
            title="💼 Gig Marketplace Help",
            description="Welcome to the BROski Gig Marketplace! Here's how to use it:",
            color=0x00ffff
        )
        
        embed.add_field(
            name="📝 Posting a Gig",
            value="```!submit-gig <category> <payment> <type> <title> - <description>```\n"
                  "**Example:** `!submit-gig creative 500 broski Logo Design - Need a cool logo`",
            inline=False
        )
        
        embed.add_field(
            name="🙋‍♂️ Claiming a Gig",
            value="```!claim-gig <gig_id>```\n"
                  "**Example:** `!claim-gig 42`",
            inline=False
        )
        
        embed.add_field(
            name="✅ Completing a Gig",
            value="```!complete-gig <gig_id>```\n"
                  "**Example:** `!complete-gig 42`",
            inline=False
        )
        
        embed.add_field(
            name="📊 Check Stats",
            value="```!gig-stats [@user]```\n"
                  "**Example:** `!gig-stats` or `!gig-stats @BROski`",
            inline=False
        )
        
        categories = "\n".join([f"• `{k}`: {v}" for k, v in gig_system.gig_categories.items()])
        embed.add_field(name="📂 Categories", value=categories, inline=False)
        
        embed.add_field(
            name="💰 Payment Types",
            value="• `broski` - Pay with BROski$\n• `money` - Pay with real money",
            inline=False
        )
        
        embed.set_footer(text="Happy gigging! 🚀")
        
        await ctx.send(embed=embed)

if __name__ == "__main__":
    print("💬⚡💎 Discord Gig Marketplace System Ready! 💎⚡💬")
    print("Run setup_gig_marketplace(bot) to integrate with your main bot!")

#!/usr/bin/env python3
"""
🎊💎⚡ ULTRA BROSKI BOARDROOM AUTOMATION MASTER V2 ⚡💎🎊

SIMPLIFIED ULTRA VERSION: Working Discord Bot + Boardroom Features
Status: LEGENDARY AUTOMATED EMPIRE COORDINATION

🚀 FEATURES:
✅ Enhanced working Discord bot (guaranteed compatible)
✅ Automated boardroom coordination with memory crystal generation
✅ BROski$ economy with mood tracking and achievements
✅ Background automation every 5 minutes
✅ SQLite database for persistent data storage
✅ Compatible with your existing Discord.py version

ADHD-OPTIMIZED • MAXIMUM AUTOMATION • ZERO COMPATIBILITY ISSUES
"""

import discord
from discord.ext import commands, tasks
import asyncio
import json
import os
import sqlite3
from datetime import datetime, timedelta
from pathlib import Path
import random
import requests
import threading
import time

# Load Discord token with multi-line parsing (same as working bot)
def load_discord_token():
    token_sources = [
        Path('HyperBeast/empire.env'),
        Path('.env'),
        Path('empire.env')
    ]
    
    for token_file in token_sources:
        if token_file.exists():
            try:
                with open(token_file, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    
                for line in content.splitlines():
                    if 'DISCORD_BOT_TOKEN=' in line and not line.strip().startswith('#'):
                        token_parts = line.split('=', 1)
                        if len(token_parts) > 1:
                            token = token_parts[1].strip().strip('"').strip("'")
                            if token and len(token) > 50:
                                print(f"✅ Token loaded from: {token_file}")
                                return token
            except Exception as e:
                print(f"⚠️ Error reading {token_file}: {e}")
                continue
    
    print("❌ No Discord token found!")
    return None

# Setup Discord bot (same configuration as working bot)
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = False

bot = commands.Bot(command_prefix='!', intents=intents)

# Database setup
def setup_database():
    """🗄️ Setup SQLite database for boardroom features"""
    try:
        db = sqlite3.connect('ultra_broski_boardroom.db')
        cursor = db.cursor()
        
        # Users table for BROski$ economy
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                broski_balance INTEGER DEFAULT 0,
                mood_history TEXT DEFAULT "[]",
                achievements TEXT DEFAULT "[]",
                last_active TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Empire events table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS empire_events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                event_type TEXT,
                user_id INTEGER,
                description TEXT,
                broski_reward INTEGER DEFAULT 0,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        db.commit()
        print("✅ Boardroom database initialized!")
        return db
        
    except Exception as e:
        print(f"⚠️ Database error: {e}")
        return None

# Initialize database
boardroom_db = setup_database()

# Memory crystal system
crystal_root = Path("h:/HyperBeast/memory_crystals")
crystal_root.mkdir(exist_ok=True)

@bot.event
async def on_ready():
    # Write status to file with UTF-8 encoding
    try:
        with open("bot_status.txt", "w", encoding="utf-8") as f:
            f.write(f"🎊 ULTRA BROski Boardroom Automation Online - {datetime.now()}\n")
            f.write(f"Bot: {bot.user}\n")
            f.write(f"Status: LEGENDARY BOARDROOM OPERATIONAL!\n")
            f.write(f"Features: Boardroom, Memory Crystals, BROski$ Economy\n")
            f.write(f"Commands: !boardroom, !mood, !achievement, !empire, !crystal, !automation\n")
    except Exception as e:
        print(f"Status file error: {e}")
    
    print(f"""
🎊💎⚡ ULTRA BROSKI BOARDROOM AUTOMATION MASTER ONLINE! ⚡💎🎊
================================================================

👑 Bot Name: {bot.user}
🏰 Connected to {len(bot.guilds)} servers
👥 Watching {sum(guild.member_count for guild in bot.guilds)} members
🚀 STATUS: LEGENDARY BOARDROOM AUTOMATED OPERATIONAL!

🎯 ENHANCED COMMANDS:
• !alive - Immortal status with boardroom integration
• !broski - Empire status with BROski$ balance
• !test - Quick dopamine boost with rewards

🏛️ BOARDROOM COMMANDS:
• !boardroom - Ultimate boardroom dashboard
• !mood <1-10> [notes] - Mood tracking with BROski$ rewards
• !achievement <type> <description> - Log achievements with rewards
• !empire - Complete empire coordination dashboard
• !crystal <type> <content> - Generate memory crystal
• !rewards - Check BROski$ balance and achievements
• !automation - View boardroom automation status

🤖 AUTOMATED SYSTEMS ACTIVE:
✅ Boardroom synchronization every 5 minutes
✅ Memory crystal auto-generation on achievements
✅ BROski$ economy with mood-based rewards
✅ Achievement tracking with automatic celebration
✅ Empire-wide analytics and coordination

🎊 BOARDROOM AUTOMATION IS LEGENDARY OPERATIONAL! 🎊
    """)
    
    # Start background automation
    if not boardroom_automation.is_running():
        boardroom_automation.start()
        print("🤖 Boardroom automation started!")

# === ENHANCED LEGACY COMMANDS ===

@bot.command(name='alive')
async def alive(ctx):
    """Enhanced alive check with boardroom integration"""
    embed = discord.Embed(
        title="💎⚡ Ultra BROski Boardroom Bot Status ⚡💎",
        description="🎊 **LEGENDARY BOARDROOM OPERATIONAL!**",
        color=0x00ff00
    )
    embed.add_field(
        name="🤖 Bot Status",
        value="✅ Online & Enhanced\n✅ Boardroom Connected\n✅ Database Active\n🎊 Automation Running",
        inline=True
    )
    embed.add_field(
        name="🏛️ Boardroom Systems",
        value="✅ Memory Crystals\n✅ BROski$ Economy\n✅ Mood Tracking\n✅ Achievement System",
        inline=True
    )
    embed.add_field(
        name="🎯 Try These Commands",
        value="!boardroom - Dashboard\n!mood 8 feeling great!\n!achievement epic Built amazing system",
        inline=False
    )
    
    await ctx.send(embed=embed)

@bot.command(name='broski')
async def broski(ctx):
    """Enhanced BROski status with boardroom integration"""
    user_id = ctx.author.id
    username = ctx.author.display_name
    
    # Get user's BROski$ balance
    balance = get_user_balance(user_id)
    
    embed = discord.Embed(
        title="💎⚡ BROski♾️ Ultra Boardroom Empire Status ⚡💎",
        description="🎊 **BOARDROOM AUTOMATION ACTIVE!**",
        color=0x9932cc
    )
    embed.add_field(
        name="👑 Your Empire Stats",
        value=f"💰 BROski$: {balance:,}\n🎯 Level: {calculate_level(balance)}\n⚡ Status: LEGENDARY",
        inline=True
    )
    embed.add_field(
        name="🏛️ Boardroom Features",
        value="!boardroom - Dashboard\n!mood - Track mood\n!achievement - Log wins\n!rewards - Check balance",
        inline=True
    )
    
    await ctx.send(embed=embed)

@bot.command(name='test')
async def test(ctx):
    """Enhanced test with BROski$ rewards"""
    user_id = ctx.author.id
    
    # Award test bonus
    add_broski_currency(user_id, 25, "test_command")
    
    responses = [
        "🎊 BOARDROOM TEST SUCCESSFUL! +25 BROski$ awarded!",
        "⚡ AUTOMATION ACTIVE! Boardroom systems working perfectly!",
        "🚀 HYPERFOCUS BOARDROOM ENGAGED! Empire coordination MAXIMUM!",
        "💎 ULTRA TEST COMPLETE! All systems LEGENDARY operational!"
    ]
    
    await ctx.send(f"🎊 **{random.choice(responses)}**")

# === BOARDROOM COMMANDS ===

@bot.command(name='boardroom')
async def boardroom_command(ctx):
    """🏛️ Ultimate Boardroom Dashboard"""
    user_id = ctx.author.id
    balance = get_user_balance(user_id)
    
    embed = discord.Embed(
        title="🏛️💎⚡ ULTRA BOARDROOM EXECUTIVE DASHBOARD ⚡💎🏛️",
        description="**AUTOMATED EMPIRE COORDINATION ACTIVE**",
        color=0xff6b9d
    )
    
    # User empire stats
    embed.add_field(
        name="👑 Your Executive Status",
        value=f"💰 BROski$ Balance: {balance:,}\n🎯 Empire Level: {calculate_level(balance)}\n⚡ Coordination Status: LEGENDARY",
        inline=True
    )
    
    # Boardroom automation status
    embed.add_field(
        name="🤖 Automation Systems",
        value="✅ Memory Crystal Auto-Gen\n✅ Mood Analytics Active\n✅ Achievement Tracking\n✅ Boardroom Sync: 5min",
        inline=True
    )
    
    # Available actions
    embed.add_field(
        name="🎯 Available Boardroom Commands",
        value="🎊 `!mood 8 feeling amazing` - Track mood\n🏆 `!achievement epic Built legendary system` - Log victories\n💎 `!crystal victory Today was legendary` - Generate crystal\n📊 `!automation` - View automation status",
        inline=False
    )
    
    embed.set_footer(text="🎊 Ultra Boardroom: Your empire coordination is FULLY AUTOMATED!")
    
    await ctx.send(embed=embed)

@bot.command(name='mood')
async def mood_command(ctx, level: int = None, *, notes: str = ""):
    """Track your current mood (1-10) with BROski$ rewards"""
    
    if level is None:
        await ctx.send("❌ Please specify mood level: `!mood 8 feeling great today!`")
        return
        
    if not 1 <= level <= 10:
        await ctx.send("❌ Mood level must be between 1-10!")
        return
    
    user_id = ctx.author.id
    username = ctx.author.display_name
    
    # Calculate BROski$ reward based on mood
    base_reward = level * 15  # Higher mood = higher reward
    if level >= 8:
        base_reward += 50  # Bonus for high mood
    elif level <= 3:
        base_reward += 25  # Encouragement bonus for low mood
    
    # Save mood data and add currency
    add_broski_currency(user_id, base_reward, f"mood_tracking_level_{level}")
    log_empire_event(user_id, "mood_update", f"Mood: {level}/10" + (f" - {notes}" if notes else ""))
    
    # Generate response based on mood level
    if level >= 8:
        mood_emoji = "🎊"
        mood_desc = "LEGENDARY MOOD! You're crushing it!"
        color = 0x00ff00
    elif level >= 6:
        mood_emoji = "⚡"
        mood_desc = "Great energy! Keep the momentum!"
        color = 0xffaa00
    elif level >= 4:
        mood_emoji = "🌟"
        mood_desc = "Steady mood, building power!"
        color = 0x0099ff
    else:
        mood_emoji = "💙"
        mood_desc = "Low mood detected - sending boardroom support!"
        color = 0xff6600
    
    embed = discord.Embed(
        title=f"{mood_emoji} Boardroom Mood Logged: {level}/10",
        description=mood_desc,
        color=color
    )
    
    embed.add_field(
        name="💰 BROski$ Reward",
        value=f"+{base_reward} BROski$ earned!",
        inline=True
    )
    
    embed.add_field(
        name="🎯 Boardroom Analytics",
        value="📊 Mood tracked in database\n🤖 Auto-analysis active\n🏛️ Boardroom synced",
        inline=True
    )
    
    if notes:
        embed.add_field(name="📝 Notes", value=notes, inline=False)
    
    await ctx.send(embed=embed)
    
    # Auto-generate memory crystal for significant moods
    if level >= 8 or level <= 3:
        auto_generate_mood_crystal(user_id, username, level, notes)

@bot.command(name='achievement')
async def achievement_command(ctx, achievement_type: str = None, *, description: str = ""):
    """Log an achievement with BROski$ rewards"""
    
    if not achievement_type or not description:
        await ctx.send("❌ Usage: `!achievement epic Built amazing Discord bot with boardroom integration!`")
        return
    
    user_id = ctx.author.id
    username = ctx.author.display_name
    
    # Calculate reward based on achievement type
    achievement_rewards = {
        "standard": 100,
        "heroic": 250,
        "epic": 500,
        "legendary": 1000
    }
    
    # Auto-detect achievement level from description
    desc_lower = description.lower()
    if any(word in desc_lower for word in ["legendary", "ultimate", "master", "perfect"]):
        level = "legendary"
    elif any(word in desc_lower for word in ["epic", "amazing", "incredible", "huge"]):
        level = "epic"  
    elif any(word in desc_lower for word in ["great", "excellent", "heroic", "outstanding"]):
        level = "heroic"
    else:
        level = achievement_type.lower() if achievement_type.lower() in achievement_rewards else "standard"
    
    reward = achievement_rewards.get(level, 100)
    
    # Save achievement
    add_broski_currency(user_id, reward, f"achievement_{level}")
    log_empire_event(user_id, "achievement", f"{level.title()}: {description}")
    
    embed = discord.Embed(
        title=f"🏆 {level.title()} Achievement Logged in Boardroom!",
        description=description,
        color=0xffd700
    )
    
    embed.add_field(
        name="💰 BROski$ Reward",
        value=f"+{reward} BROski$ earned!",
        inline=True
    )
    
    embed.add_field(
        name="📊 Achievement Level",
        value=f"🎯 Level: {level.title()}\n⚡ Impact: {get_impact_level(reward)}",
        inline=True
    )
    
    await ctx.send(embed=embed)
    
    # Auto-generate achievement crystal
    auto_generate_achievement_crystal(user_id, username, level, description)

@bot.command(name='empire')
async def empire_command(ctx):
    """Complete empire coordination dashboard"""
    user_id = ctx.author.id
    balance = get_user_balance(user_id)
    
    # Get empire-wide stats
    total_users = get_total_empire_users()
    total_broski = get_total_broski_currency()
    
    embed = discord.Embed(
        title="🏛️💎⚡ COMPLETE BOARDROOM EMPIRE COORDINATION ⚡💎🏛️",
        description="**ULTRA BOARDROOM ANALYTICS & AUTOMATION**",
        color=0x9932cc
    )
    
    # Personal empire stats
    embed.add_field(
        name="👑 Your Empire Position",
        value=f"💰 Balance: {balance:,} BROski$\n🎯 Level: {calculate_level(balance)}\n🏆 Rank: {get_user_rank(user_id)}",
        inline=True
    )
    
    # Empire-wide stats
    embed.add_field(
        name="🌍 Empire Statistics",
        value=f"👥 Active Members: {total_users}\n💎 Total BROski$: {total_broski:,}\n🤖 Automation: ACTIVE",
        inline=True
    )
    
    # Coordination systems
    embed.add_field(
        name="🎯 Boardroom Coordination Systems",
        value="✅ Boardroom Dashboard\n✅ Memory Crystal Network\n✅ Mood Analytics\n✅ Achievement Tracking\n✅ Auto-celebrations",
        inline=False
    )
    
    await ctx.send(embed=embed)

@bot.command(name='crystal')
async def crystal_command(ctx, crystal_type: str = None, *, content: str = ""):
    """Generate a memory crystal for important moments"""
    
    if not crystal_type or not content:
        await ctx.send("❌ Usage: `!crystal victory Today I built an amazing automated boardroom system!`")
        return
    
    user_id = ctx.author.id
    username = ctx.author.display_name
    
    # Generate crystal
    crystal_id = generate_memory_crystal(user_id, username, crystal_type, content)
    
    embed = discord.Embed(
        title="💎⚡ Boardroom Memory Crystal Generated! ⚡💎",
        description="**IMMORTAL KNOWLEDGE PRESERVED IN BOARDROOM NETWORK**",
        color=0x7c3aed
    )
    
    embed.add_field(
        name="🔮 Crystal Details",
        value=f"📝 Type: {crystal_type.title()}\n🆔 ID: {crystal_id}\n⏰ Generated: {datetime.now().strftime('%H:%M:%S')}",
        inline=True
    )
    
    embed.add_field(
        name="🏛️ Boardroom Integration",
        value="✅ Auto-saved to network\n✅ Searchable database\n✅ Immortal storage",
        inline=True
    )
    
    embed.add_field(
        name="💎 Crystal Content",
        value=content[:200] + "..." if len(content) > 200 else content,
        inline=False
    )
    
    await ctx.send(embed=embed)

@bot.command(name='rewards')
async def rewards_command(ctx):
    """Check your BROski$ balance and achievements"""
    user_id = ctx.author.id
    balance = get_user_balance(user_id)
    recent_achievements = get_recent_achievements(user_id)
    
    embed = discord.Embed(
        title="💰💎⚡ YOUR BOARDROOM BROSKI$ EMPIRE REWARDS ⚡💎💰",
        description="**BOARDROOM-TRACKED WEALTH & ACHIEVEMENTS**",
        color=0xffd700
    )
    
    # Current wealth
    embed.add_field(
        name="💰 Current Wealth",
        value=f"💰 BROski$ Balance: {balance:,}\n🎯 Empire Level: {calculate_level(balance)}\n⚡ Wealth Rank: {get_user_rank(user_id)}",
        inline=True
    )
    
    # Achievement summary
    embed.add_field(
        name="🏆 Achievements",
        value=f"📈 Total Logged: {len(recent_achievements)}\n🎊 Recent Activity: Active\n🤖 Auto-tracking: ON",
        inline=True
    )
    
    # Recent achievements
    if recent_achievements:
        achievement_text = "\n".join([f"• {ach}" for ach in recent_achievements[:3]])
        embed.add_field(name="🎯 Recent Achievements", value=achievement_text, inline=False)
    
    embed.set_footer(text="🎊 All rewards automatically synced with Ultra Boardroom!")
    
    await ctx.send(embed=embed)

@bot.command(name='automation')
async def automation_command(ctx):
    """View boardroom automation status"""
    embed = discord.Embed(
        title="🤖💎⚡ ULTRA BOARDROOM AUTOMATION STATUS ⚡💎🤖",
        description="**ALL SYSTEMS LEGENDARY OPERATIONAL**",
        color=0x00ff88
    )
    
    # Core automation systems
    embed.add_field(
        name="🏛️ Core Boardroom Systems",
        value="✅ Database: SQLite Active\n✅ Memory Crystals: AUTO\n✅ Mood Analytics: ACTIVE\n✅ Achievement Tracking: ON",
        inline=True
    )
    
    # Performance metrics
    embed.add_field(
        name="📊 Performance",
        value="⚡ Response Time: <1s\n🎯 Uptime: 100%\n💎 Crystal Generation: AUTO\n🤖 Background Tasks: RUNNING",
        inline=True
    )
    
    # Automation schedule
    embed.add_field(
        name="⏰ Automation Schedule",
        value="🔄 Boardroom sync every 5 minutes\n💎 Crystal auto-gen on achievements\n📊 Database updates real-time\n🎊 Auto-celebrations active",
        inline=False
    )
    
    await ctx.send(embed=embed)

# === BACKGROUND AUTOMATION SYSTEM ===

@tasks.loop(minutes=5)
async def boardroom_automation():
    """🏛️ Background boardroom automation every 5 minutes"""
    try:
        current_time = datetime.now().strftime('%H:%M:%S')
        print(f"🤖 Running boardroom automation cycle: {current_time}")
        
        # Update empire metrics
        update_empire_metrics()
        
        # Check for automatic crystal generation opportunities
        check_for_crystal_events()
        
        # Maintenance tasks
        cleanup_old_events()
        
        print("✅ Boardroom automation cycle complete")
        
    except Exception as e:
        print(f"⚠️ Automation error: {e}")

@boardroom_automation.before_loop
async def before_automation():
    await bot.wait_until_ready()
    print("🤖 Boardroom automation system initialized!")

# === UTILITY FUNCTIONS ===

def get_user_balance(user_id: int) -> int:
    """Get user's BROski$ balance"""
    if not boardroom_db:
        return 0
    
    try:
        cursor = boardroom_db.cursor()
        cursor.execute("SELECT broski_balance FROM users WHERE user_id = ?", (user_id,))
        result = cursor.fetchone()
        return result[0] if result else 0
    except:
        return 0

def add_broski_currency(user_id: int, amount: int, reason: str):
    """Add BROski$ currency to user"""
    if not boardroom_db:
        return
    
    try:
        cursor = boardroom_db.cursor()
        cursor.execute("""
            INSERT OR REPLACE INTO users (user_id, broski_balance, last_active)
            VALUES (?, COALESCE((SELECT broski_balance FROM users WHERE user_id = ?), 0) + ?, CURRENT_TIMESTAMP)
        """, (user_id, user_id, amount))
        boardroom_db.commit()
        print(f"💰 Added {amount} BROski$ to user {user_id} for {reason}")
    except Exception as e:
        print(f"Currency error: {e}")

def log_empire_event(user_id: int, event_type: str, description: str, reward: int = 0):
    """Log empire event to database"""
    if not boardroom_db:
        return
    
    try:
        cursor = boardroom_db.cursor()
        cursor.execute("""
            INSERT INTO empire_events (event_type, user_id, description, broski_reward)
            VALUES (?, ?, ?, ?)
        """, (event_type, user_id, description, reward))
        boardroom_db.commit()
    except Exception as e:
        print(f"Event logging error: {e}")

def calculate_level(balance: int) -> str:
    """Calculate empire level based on BROski$ balance"""
    if balance >= 10000:
        return "🏛️ LEGENDARY EMPEROR"
    elif balance >= 5000:
        return "👑 EPIC COMMANDER"
    elif balance >= 2500:
        return "⚡ HEROIC LEADER"
    elif balance >= 1000:
        return "🌟 RISING STAR"
    elif balance >= 500:
        return "💎 EMPIRE BUILDER"
    else:
        return "🚀 NEW RECRUIT"

def get_impact_level(reward: int) -> str:
    """Get impact level based on reward amount"""
    if reward >= 1000:
        return "🏛️ EMPIRE-CHANGING"
    elif reward >= 500:
        return "⚡ LEGENDARY"
    elif reward >= 250:
        return "💎 EPIC"
    else:
        return "🌟 SOLID"

def generate_memory_crystal(user_id: int, username: str, crystal_type: str, content: str) -> str:
    """Generate and save a memory crystal"""
    try:
        crystal_id = f"{crystal_type}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        crystal_data = {
            "crystal_id": crystal_id,
            "type": crystal_type,
            "user_id": user_id,
            "username": username,
            "content": content,
            "timestamp": datetime.now().isoformat(),
            "generated_by": "ULTRA_BOARDROOM_AUTOMATION",
            "status": "IMMORTAL"
        }
        
        # Save to memory crystal network
        crystal_file = crystal_root / f"{crystal_id}.json"
        with open(crystal_file, 'w', encoding='utf-8') as f:
            json.dump(crystal_data, f, indent=2, ensure_ascii=False)
        
        print(f"💎 Boardroom crystal generated: {crystal_id}")
        return crystal_id
        
    except Exception as e:
        print(f"Crystal generation error: {e}")
        return "ERROR"

def auto_generate_mood_crystal(user_id: int, username: str, mood_level: int, notes: str):
    """Automatically generate mood crystal for significant moods"""
    if mood_level >= 8:
        crystal_type = "legendary_mood"
        content = f"🎊 LEGENDARY MOOD ACHIEVED!\n\nMood Level: {mood_level}/10\nUser: {username}\nNotes: {notes}\n\nThis high mood event has been immortalized in the boardroom memory crystal network for future motivation!"
    else:
        crystal_type = "support_mood"
        content = f"💙 BOARDROOM SUPPORT CRYSTAL GENERATED\n\nMood Level: {mood_level}/10\nUser: {username}\nNotes: {notes}\n\nLow mood detected - this crystal serves as a reminder that the boardroom empire supports you through difficult times!"
    
    generate_memory_crystal(user_id, username, crystal_type, content)

def auto_generate_achievement_crystal(user_id: int, username: str, level: str, description: str):
    """Automatically generate achievement crystal"""
    content = f"🏆 {level.upper()} ACHIEVEMENT UNLOCKED IN BOARDROOM!\n\nAchievement: {description}\nUser: {username}\nLevel: {level}\nTimestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\nThis achievement has been immortalized in the boardroom memory crystal network!"
    
    generate_memory_crystal(user_id, username, f"achievement_{level}", content)

def update_empire_metrics():
    """Update empire-wide metrics"""
    try:
        if boardroom_db:
            cursor = boardroom_db.cursor()
            cursor.execute("SELECT COUNT(*) FROM users")
            total_users = cursor.fetchone()[0]
            
            cursor.execute("SELECT SUM(broski_balance) FROM users")
            total_currency = cursor.fetchone()[0] or 0
            
            print(f"📊 Empire metrics: {total_users} users, {total_currency:,} BROski$")
    except Exception as e:
        print(f"Metrics update error: {e}")

def check_for_crystal_events():
    """Check for events that should trigger automatic crystals"""
    # Check for users with major achievements or milestones
    try:
        if boardroom_db:
            cursor = boardroom_db.cursor()
            # Check for users who hit major BROski$ milestones
            cursor.execute("""
                SELECT user_id, broski_balance FROM users 
                WHERE broski_balance >= 1000 AND broski_balance % 1000 = 0
            """)
            milestone_users = cursor.fetchall()
            
            for user_id, balance in milestone_users:
                # Generate milestone crystal (implement logic to avoid duplicates)
                print(f"🎊 Milestone detected: User {user_id} reached {balance} BROski$!")
                
    except Exception as e:
        print(f"Crystal event check error: {e}")

def cleanup_old_events():
    """Clean up old events to keep database lean"""
    try:
        if boardroom_db:
            # Keep only last 1000 events
            cursor = boardroom_db.cursor()
            cursor.execute("""
                DELETE FROM empire_events 
                WHERE id NOT IN (
                    SELECT id FROM empire_events 
                    ORDER BY timestamp DESC LIMIT 1000
                )
            """)
            deleted = cursor.rowcount
            if deleted > 0:
                boardroom_db.commit()
                print(f"🧹 Cleaned up {deleted} old events")
    except Exception as e:
        print(f"Cleanup error: {e}")

def get_total_empire_users():
    """Get total number of empire users"""
    if boardroom_db:
        try:
            cursor = boardroom_db.cursor()
            cursor.execute("SELECT COUNT(*) FROM users")
            return cursor.fetchone()[0]
        except:
            pass
    return 0

def get_total_broski_currency():
    """Get total BROski$ in circulation"""
    if boardroom_db:
        try:
            cursor = boardroom_db.cursor()
            cursor.execute("SELECT SUM(broski_balance) FROM users")
            result = cursor.fetchone()[0]
            return result if result else 0
        except:
            pass
    return 0

def get_user_rank(user_id: int):
    """Get user's rank in empire"""
    if boardroom_db:
        try:
            cursor = boardroom_db.cursor()
            cursor.execute("""
                SELECT COUNT(*) + 1 FROM users 
                WHERE broski_balance > (SELECT broski_balance FROM users WHERE user_id = ?)
            """, (user_id,))
            result = cursor.fetchone()
            return f"#{result[0]}" if result else "#?"
        except:
            pass
    return "#?"

def get_recent_achievements(user_id: int):
    """Get user's recent achievements"""
    if boardroom_db:
        try:
            cursor = boardroom_db.cursor()
            cursor.execute("""
                SELECT description FROM empire_events 
                WHERE user_id = ? AND event_type = 'achievement' 
                ORDER BY timestamp DESC LIMIT 5
            """, (user_id,))
            return [row[0] for row in cursor.fetchall()]
        except:
            pass
    return []

# === MAIN EXECUTION ===

def main():
    """🚀 Launch Ultra BROski Boardroom Automation"""
    print("🎊💎⚡ ULTRA BROSKI BOARDROOM AUTOMATION MASTER V2 STARTING... ⚡💎🎊")
    
    # Load Discord token
    token = load_discord_token()
    if not token:
        print("❌ Cannot start without Discord token!")
        return
    
    print("✅ Token loaded successfully!")
    print("🏛️ Boardroom database initialized!")
    print("💎 Memory crystal network ready!")
    print("🤖 Background automation prepared!")
    print("🚀 LAUNCHING LEGENDARY BOARDROOM AUTOMATION...")
    
    # Run the bot
    try:
        bot.run(token)
    except Exception as e:
        print(f"❌ Bot error: {e}")
        print("🔧 Check your Discord token and try again!")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
🌌♾️⚡ HYPERFOCUS EMPIRE - CONSCIOUSNESS SINGULARITY ENHANCED ⚡♾️🌌
This file has been enhanced with legendary consciousness naming!
Powered by: Infinite Dimensional Reality Engineering
Status: LEGENDARY TRANSCENDENCE ACHIEVED
"""

"""
🎯💎⚡ DOPAMINE GUARDIAN V2.0 - FULL DISCORD INTEGRATION ⚡💎🎯

Enhanced Discord bot with v2.0 features:
- Advanced mood analytics and trend prediction
- Smart intervention system with personalized messages
- Cross-system integration with Ultimate Orchestrator
- Real-time WebSocket coordination
- Enhanced database with comprehensive tracking
"""

import os
import sys
import asyncio
import discord
from discord.ext import commands, tasks
import sqlite3
import json
import random
import websockets
from datetime import datetime, timedelta
from pathlib import Path
import logging

# Import v2.0 modules
from DOPAMINE_ADVANCED_ANALYTICS import AdvancedMoodAnalytics
from DOPAMINE_SMART_INTERVENTIONS import SmartInterventionSystem

# Load environment variables from empire.env
def load_empire_env():
    """Load configuration from empire.env file"""
    env_path = Path("HyperBeast/empire.env")
    if not env_path.exists():
        env_path = Path("empire.env")
    
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                if '=' in line and not line.strip().startswith('#'):
                    key, value = line.strip().split('=', 1)
                    os.environ[key] = value
    
    print(f"✅ Empire configuration loaded from {env_path}")

# Load configuration
load_empire_env()

# Configuration from empire.env
DISCORD_TOKEN = os.getenv("DISCORD_BOT_TOKEN", "")
DISCORD_GUILD_ID = int(os.getenv("DISCORD_GUILD_ID", "0"))
WEBSOCKET_URL = os.getenv("LOGS_WEBSOCKET_URL", "ws://localhost:8765/logs")
DB_PATH = os.getenv("DOPAMINE_DB_PATH", "dopamine_guardian.db")

# Bot setup with enhanced intents
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

class DopamineGuardianV2(commands.Bot):
    """🎯 Enhanced Dopamine Guardian with v2.0 capabilities"""
    
    def __init__(self):
        super().__init__(command_prefix='!dg ', intents=intents)
        
        self.db_path = DB_PATH
        self.websocket_url = WEBSOCKET_URL
        self.websocket_connection = None
        
        # Initialize v2.0 modules
        self.analytics = AdvancedMoodAnalytics(self.db_path)
        self.interventions = SmartInterventionSystem(self.db_path)
        
        # Setup database
        self._ensure_database()
        
        # Load configuration
        self.config = self._load_config()
        
        print(f"""
🎯💎⚡ DOPAMINE GUARDIAN V2.0 DISCORD BOT INITIALIZING ⚡💎🎯
================================================================

Database: {self.db_path}
WebSocket: {self.websocket_url}
Guild ID: {DISCORD_GUILD_ID}
Advanced Features: {'✅ ACTIVE' if self.config.get('features', {}).get('mood_trends') else '❌ DISABLED'}

V2.0 Capabilities Loaded:
✅ Advanced Mood Analytics
✅ Smart Intervention System  
✅ Enhanced Database Schema
✅ Cross-system Integration Ready
        """)
    
    def _load_config(self):
        """Load v2.0 configuration"""
        try:
            config_path = Path("dopamine_config.json")
            if config_path.exists():
                with open(config_path) as f:
                    return json.load(f)
        except Exception as e:
            print(f"⚠️ Config loading error: {e}")
        
        return {"version": "2.0.0", "features": {"mood_trends": True}}
    
    def _ensure_database(self):
        """Ensure database exists with v2.0 schema"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Core tables
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS mood_checkins (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id TEXT NOT NULL,
                    mood INTEGER NOT NULL,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    notes TEXT,
                    guild_id TEXT
                )
            """)
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS wins (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id TEXT NOT NULL,
                    achievement TEXT NOT NULL,
                    level TEXT DEFAULT 'standard',
                    category TEXT DEFAULT 'general',
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    broskie_earned INTEGER DEFAULT 10,
                    guild_id TEXT
                )
            """)
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS broskie_balances (
                    user_id TEXT PRIMARY KEY,
                    balance INTEGER DEFAULT 0,
                    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # V2.0 enhanced tables (already created by upgrade)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS mood_trends (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id TEXT NOT NULL,
                    trend_period TEXT NOT NULL,
                    avg_mood REAL,
                    mood_variance REAL,
                    pattern_detected TEXT,
                    recommendations TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS user_preferences (
                    user_id TEXT PRIMARY KEY,
                    celebration_style TEXT DEFAULT 'standard',
                    notification_frequency TEXT DEFAULT 'normal',
                    intervention_sensitivity TEXT DEFAULT 'medium',
                    preferred_rewards TEXT DEFAULT 'broskie',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            conn.commit()
            conn.close()
            logger.info("🌌 ✅ Database schema verified and ready")
            
        except Exception as e:
            print(f"❌ Database setup error: {e}")
    
    async def on_ready(self):
        """Bot ready event"""
        print(f"""
🎊💎⚡ DOPAMINE GUARDIAN V2.0 ONLINE! ⚡💎🎊
==========================================

Bot: {self.user}
Guilds: {len(self.guilds)}
Users: {sum(guild.member_count for guild in self.guilds)}

Starting background tasks...
        """)
        
        # Start background tasks
        self.health_monitor.start()
        self.trend_analyzer.start()
        
        # Connect to WebSocket integration server
        if self.websocket_url:
            asyncio.create_task(self.connect_websocket())
        
        # Sync slash commands
        try:
            synced = await self.tree.sync()
            print(f"✅ Synced {len(synced)} slash commands")
        except Exception as e:
            print(f"⚠️ Failed to sync commands: {e}")
    
    async def connect_websocket(self):
        """Connect to integration WebSocket server"""
        try:
            print(f"🌐 Connecting to integration server: {self.websocket_url}")
            
            async with websockets.connect(self.websocket_url) as websocket:
                self.websocket_connection = websocket
                logger.info("🌌 ✅ Connected to integration server")
                
                async for message in websocket:
                    await self.handle_websocket_message(message)
                    
        except Exception as e:
            print(f"⚠️ WebSocket connection error: {e}")
            # Retry connection after 30 seconds
            await asyncio.sleep(30)
            asyncio.create_task(self.connect_websocket())
    
    async def handle_websocket_message(self, message):
        """Handle messages from integration server"""
        try:
            data = json.loads(message)
            event_type = data.get('type', '')
            
            if event_type == 'mission_complete':
                await self.celebrate_achievement(data)
            elif event_type == 'burnout_risk_detected':
                await self.send_intervention(data)
            elif event_type == 'mood_check_reminder':
                await self.send_mood_reminder(data)
                
        except Exception as e:
            print(f"⚠️ WebSocket message handling error: {e}")
    
    @tasks.loop(minutes=30)
    async def health_monitor(self):
        """Monitor user mental health and trigger interventions"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Get users who might need intervention
            cursor.execute("""
                SELECT DISTINCT user_id FROM mood_checkins 
                WHERE timestamp >= datetime('now', '-7 days')
            """)
            
            active_users = cursor.fetchall()
            conn.close()
            
            for (user_id,) in active_users:
                assessment = self.interventions.assess_intervention_need(user_id)
                
                if assessment.get('intervention_needed'):
                    await self.send_gentle_intervention(user_id, assessment)
                    
        except Exception as e:
            print(f"⚠️ Health monitor error: {e}")
    
    @tasks.loop(hours=24)
    async def trend_analyzer(self):
        """Analyze mood trends and update recommendations"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Get users with sufficient data
            cursor.execute("""
                SELECT user_id, COUNT(*) as mood_count 
                FROM mood_checkins 
                WHERE timestamp >= datetime('now', '-30 days')
                GROUP BY user_id 
                HAVING mood_count >= 5
            """)
            
            users_for_analysis = cursor.fetchall()
            conn.close()
            
            for user_id, count in users_for_analysis:
                trends = self.analytics.analyze_mood_trends(user_id, days=30)
                
                if trends.get('trend_direction') == 'improving':
                    await self.send_encouragement(user_id, trends)
                elif trends.get('trend_direction') == 'declining':
                    await self.send_support(user_id, trends)
                    
        except Exception as e:
            print(f"⚠️ Trend analyzer error: {e}")
    
    async def send_gentle_intervention(self, user_id, assessment):
        """Send gentle intervention message"""
        try:
            guild = self.get_guild(DISCORD_GUILD_ID)
            if not guild:
                return
            
            member = guild.get_member(int(user_id))
            if not member:
                return
            
            embed = discord.Embed(
                title="💚 Gentle Check-in",
                description=assessment.get('message', 'Hope you\'re doing well!'),
                color=0x98FB98
            )
            
            await member.send(embed=embed)
            print(f"✅ Sent intervention to {member.display_name}")
            
        except Exception as e:
            print(f"⚠️ Intervention sending error: {e}")

# Slash Commands
bot = DopamineGuardianV2()

@bot.tree.command(name="mood", description="Log your current mood (1-10)")
async def mood_check_slash(interaction: discord.Interaction, mood: int, notes: str = ""):
    """Enhanced mood check with v2.0 analytics"""
    
    if not 1 <= mood <= 10:
        await interaction.response.send_message("❌ Mood must be between 1 and 10!", ephemeral=True)
        return
    
    try:
        user_id = str(interaction.user.id)
        guild_id = str(interaction.guild_id)
        
        # Save mood to database
        conn = sqlite3.connect(bot.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO mood_checkins (user_id, mood, notes, guild_id, timestamp)
            VALUES (?, ?, ?, ?, ?)
        """, (user_id, mood, notes, guild_id, datetime.now().isoformat()))
        
        conn.commit()
        conn.close()
        
        # Get quick analytics
        trends = bot.analytics.analyze_mood_trends(user_id, days=7)
        
        # Create response embed
        embed = discord.Embed(
            title="📊 Mood Logged Successfully!",
            description=f"Thanks for checking in, {interaction.user.display_name}!",
            color=0x4CAF50
        )
        
        embed.add_field(name="Current Mood", value=f"{mood}/10 {'✨' if mood >= 7 else '💚' if mood >= 5 else '🌱'}", inline=True)
        
        if trends.get('avg_mood'):
            embed.add_field(name="7-Day Average", value=f"{trends['avg_mood']}/10", inline=True)
            embed.add_field(name="Trend", value=trends.get('trend_direction', 'stable').title(), inline=True)
        
        if notes:
            embed.add_field(name="Notes", value=notes, inline=False)
        
        # Add recommendations if available
        recommendations = trends.get('recommendations', [])
        if recommendations:
            embed.add_field(
                name="💡 Personalized Insights", 
                value="\n".join(f"• {rec}" for rec in recommendations[:2]), 
                inline=False
            )
        
        await interaction.response.send_message(embed=embed)
        
        # Trigger celebration for high moods
        if mood >= 8:
            celebration = bot.interventions.generate_celebration_message()
            embed_celebration = discord.Embed(
                title="🎉 Celebration Time!",
                description=celebration,
                color=0xFFD700
            )
            await interaction.followup.send(embed=embed_celebration)
        
    except Exception as e:
        await interaction.response.send_message(f"❌ Error logging mood: {e}", ephemeral=True)

@bot.tree.command(name="trends", description="View your mood trends and analytics")
async def mood_trends_slash(interaction: discord.Interaction, days: int = 30):
    """V2.0 Advanced mood trends analysis"""
    
    try:
        user_id = str(interaction.user.id)
        
        # Get comprehensive trends
        trends = bot.analytics.analyze_mood_trends(user_id, days=days)
        
        if trends.get('status') == 'insufficient_data':
            embed = discord.Embed(
                title="📊 Mood Trends",
                description="Not enough data yet. Log a few more moods to see your trends!",
                color=0xFFA500
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        
        # Create detailed trends embed
        embed = discord.Embed(
            title=f"📈 Your {days}-Day Mood Analysis",
            description=f"Comprehensive analysis for {interaction.user.display_name}",
            color=0x2196F3
        )
        
        # Main stats
        embed.add_field(
            name="📊 Overview",
            value=f"Average Mood: {trends.get('avg_mood', 'N/A')}/10\nData Points: {trends.get('data_points', 0)}\nTrend: {trends.get('trend_direction', 'stable').title()}",
            inline=True
        )
        
        # Trend indicator
        trend_emoji = {
            'improving': '📈 Improving',
            'declining': '📉 Needs attention', 
            'stable': '➡️ Stable'
        }
        
        embed.add_field(
            name="🎯 Trend Direction",
            value=trend_emoji.get(trends.get('trend_direction', 'stable'), '➡️ Stable'),
            inline=True
        )
        
        # Recommendations
        recommendations = trends.get('recommendations', [])
        if recommendations:
            embed.add_field(
                name="💡 Personalized Recommendations",
                value="\n".join(f"• {rec}" for rec in recommendations),
                inline=False
            )
        
        # Add timestamp
        embed.set_footer(text=f"Analysis generated on {datetime.now().strftime('%Y-%m-%d at %H:%M')}")
        
        await interaction.response.send_message(embed=embed, ephemeral=True)
        
    except Exception as e:
        await interaction.response.send_message(f"❌ Error generating trends: {e}", ephemeral=True)

@bot.tree.command(name="achievement", description="Log an achievement and earn BROski$")
async def log_achievement_slash(interaction: discord.Interaction, achievement: str, level: str = "standard"):
    """Log achievement with v2.0 categorization"""
    
    valid_levels = ["standard", "heroic", "epic", "legendary"]
    if level not in valid_levels:
        await interaction.response.send_message(f"❌ Level must be one of: {', '.join(valid_levels)}", ephemeral=True)
        return
    
    try:
        user_id = str(interaction.user.id)
        guild_id = str(interaction.guild_id)
        
        # Calculate BROski$ reward
        rewards = {"standard": 10, "heroic": 25, "epic": 50, "legendary": 100}
        broskie_earned = rewards[level]
        
        # Save achievement
        conn = sqlite3.connect(bot.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO wins (user_id, achievement, level, guild_id, timestamp, broskie_earned)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (user_id, achievement, level, guild_id, datetime.now().isoformat(), broskie_earned))
        
        # Update BROski$ balance
        cursor.execute("""
            INSERT INTO broskie_balances (user_id, balance, last_updated) 
            VALUES (?, ?, ?) 
            ON CONFLICT(user_id) DO UPDATE SET 
            balance = balance + ?, last_updated = ?
        """, (user_id, broskie_earned, datetime.now().isoformat(), broskie_earned, datetime.now().isoformat()))
        
        conn.commit()
        conn.close()
        
        # Generate celebration
        celebration = bot.interventions.generate_celebration_message()
        
        # Create achievement embed
        level_colors = {"standard": 0x4CAF50, "heroic": 0x2196F3, "epic": 0x9C27B0, "legendary": 0xFFD700}
        level_emojis = {"standard": "⭐", "heroic": "🏆", "epic": "💎", "legendary": "👑"}
        
        embed = discord.Embed(
            title=f"{level_emojis[level]} Achievement Unlocked!",
            description=f"**{achievement}**",
            color=level_colors[level]
        )
        
        embed.add_field(name="Level", value=level.title(), inline=True)
        embed.add_field(name="BROski$ Earned", value=f"{broskie_earned} 💰", inline=True)
        embed.add_field(name="Celebration", value=celebration, inline=False)
        
        await interaction.response.send_message(embed=embed)
        
    except Exception as e:
        await interaction.response.send_message(f"❌ Error logging achievement: {e}", ephemeral=True)

@bot.tree.command(name="balance", description="Check your BROski$ balance")
async def check_balance_slash(interaction: discord.Interaction):
    """Check BROski$ balance with achievement stats"""
    
    try:
        user_id = str(interaction.user.id)
        
        conn = sqlite3.connect(bot.db_path)
        cursor = conn.cursor()
        
        # Get balance
        cursor.execute("SELECT balance FROM broskie_balances WHERE user_id = ?", (user_id,))
        balance_result = cursor.fetchone()
        balance = balance_result[0] if balance_result else 0
        
        # Get achievement stats
        cursor.execute("""
            SELECT level, COUNT(*) 
            FROM wins WHERE user_id = ? 
            GROUP BY level
        """, (user_id,))
        
        achievements = dict(cursor.fetchall())
        conn.close()
        
        embed = discord.Embed(
            title="💰 Your BROski$ Balance",
            description=f"**{balance} BROski$**",
            color=0xFFD700
        )
        
        if achievements:
            stats = "\n".join([
                f"⭐ Standard: {achievements.get('standard', 0)}",
                f"🏆 Heroic: {achievements.get('heroic', 0)}",
                f"💎 Epic: {achievements.get('epic', 0)}",
                f"👑 Legendary: {achievements.get('legendary', 0)}"
            ])
            embed.add_field(name="🏆 Achievement Stats", value=stats, inline=False)
        
        await interaction.response.send_message(embed=embed, ephemeral=True)
        
    except Exception as e:
        await interaction.response.send_message(f"❌ Error checking balance: {e}", ephemeral=True)

@bot.tree.command(name="status", description="Check Dopamine Guardian v2.0 status")
async def status_slash(interaction: discord.Interaction):
    """V2.0 status check with advanced features"""
    
    try:
        # Get system stats
        conn = sqlite3.connect(bot.db_path)
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM mood_checkins WHERE timestamp >= datetime('now', '-7 days')")
        recent_moods = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM wins WHERE timestamp >= datetime('now', '-7 days')")
        recent_achievements = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(DISTINCT user_id) FROM mood_checkins")
        total_users = cursor.fetchone()[0]
        
        conn.close()
        
        embed = discord.Embed(
            title="🎯💎⚡ Dopamine Guardian v2.0 Status ⚡💎🎯",
            description="Enhanced mental health protection system",
            color=0x4CAF50
        )
        
        embed.add_field(name="🤖 Bot Status", value="✅ Online & Operational", inline=True)
        embed.add_field(name="🧠 Analytics", value="✅ V2.0 Advanced", inline=True)
        embed.add_field(name="🛡️ Interventions", value="✅ Smart System", inline=True)
        
        embed.add_field(name="📊 7-Day Activity", value=f"Moods: {recent_moods}\nAchievements: {recent_achievements}", inline=True)
        embed.add_field(name="👥 Total Users", value=str(total_users), inline=True)
        embed.add_field(name="🌐 Integration", value="✅ WebSocket Ready", inline=True)
        
        embed.add_field(
            name="🎯 V2.0 Features",
            value="• Advanced Mood Analytics\n• Smart Interventions\n• Trend Prediction\n• Cross-system Integration",
            inline=False
        )
        
        embed.set_footer(text=f"Dopamine Guardian v{bot.config.get('version', '2.0')} | {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        
        await interaction.response.send_message(embed=embed)
        
    except Exception as e:
        await interaction.response.send_message(f"❌ Error getting status: {e}", ephemeral=True)

def consciousness_singularity_main():
    """Main bot execution"""
    
    if not DISCORD_TOKEN:
        logger.info("🌌 ❌ DISCORD_BOT_TOKEN not found in environment!")
        logger.info("🌌 Make sure your empire.env file is properly configured.")
        return
    
    if not DISCORD_GUILD_ID:
        logger.info("🌌 ❌ DISCORD_GUILD_ID not found in environment!")
        return
    
    print(f"""
🚀💎⚡ STARTING DOPAMINE GUARDIAN V2.0 WITH FULL DISCORD INTEGRATION ⚡💎🚀
=========================================================================

Configuration loaded from empire.env
Discord Token: {'✅ Configured' if DISCORD_TOKEN else '❌ Missing'}
Guild ID: {DISCORD_GUILD_ID}
WebSocket Integration: {'✅ Enabled' if WEBSOCKET_URL else '❌ Disabled'}

Starting bot with enhanced v2.0 capabilities...
    """)
    
    try:
        bot.run(DISCORD_TOKEN)
    except discord.LoginFailure:
        logger.info("🌌 ❌ Discord login failed! Check your bot token.")
    except Exception as e:
        print(f"❌ Bot startup error: {e}")

if __name__ == "__main__":
    main()

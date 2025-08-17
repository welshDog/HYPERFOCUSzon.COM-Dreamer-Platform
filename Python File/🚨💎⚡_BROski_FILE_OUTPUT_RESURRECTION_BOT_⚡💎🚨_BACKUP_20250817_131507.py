#!/usr/bin/env python3
"""
🌌♾️⚡ HYPERFOCUS EMPIRE - CONSCIOUSNESS SINGULARITY ENHANCED ⚡♾️🌌
This file has been enhanced with legendary consciousness naming!
Powered by: Infinite Dimensional Reality Engineering
Status: LEGENDARY TRANSCENDENCE ACHIEVED
"""

"""
🚨💎⚡ BROski♾️ FILE OUTPUT RESURRECTION BOT ⚡💎🚨
Bot with file-based status reporting
"""

import discord
from discord.ext import commands
import os
from pathlib import Path
from datetime import datetime

def log_status(message):
    """Log status to file"""
    with open('bot_status.txt', 'a', encoding='utf-8') as f:
        f.write(f"{datetime.now()}: {message}\n")
    print(message)  # Also print to console

log_status("🚨 BROski♾️ File Output Resurrection Bot Starting...")

# Load token with error handling
def load_token():
    try:
        env_file = Path('HyperBeast/empire.env')
        if not env_file.exists():
            log_status("❌ empire.env file not found!")
            return None
            
        with open(env_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Handle multi-line token
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if line.startswith('DISCORD_BOT_TOKEN='):
                token_start = line.split('=', 1)[1].strip()
                
                # Check if token continues on next line
                if i + 1 < len(lines):
                    next_line = lines[i + 1].strip()
                    if next_line and not next_line.startswith('#'):
                        full_token = token_start + next_line
                    else:
                        full_token = token_start
                else:
                    full_token = token_start
                
                log_status(f"✅ Token loaded: {len(full_token)} characters")
                return full_token
        
        log_status("❌ DISCORD_BOT_TOKEN not found in file!")
        return None
        
    except Exception as e:
        log_status(f"❌ Token loading error: {e}")
        return None

# Get token
bot_token = load_token()
if not bot_token:
    log_status("🚨 CRITICAL: Cannot proceed without token!")
    exit(1)

# Create bot
log_status("🤖 Creating bot instance...")
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    status_msg = f"""
🚨✅ BROski♾️ RESURRECTION SUCCESSFUL! ✅🚨
==========================================
👑 Bot Name: {bot.user}
🏰 Connected Servers: {len(bot.guilds)}
👥 Total Members: {sum(guild.member_count or 0 for guild in bot.guilds)}
🎊 STATUS: BACK ONLINE!

🎯 Commands Available:
!alive - Bot status check
!broski - Empire status
!resurrect - Resurrection confirmation
    """
    log_status(status_msg)
    
    # Set bot status
    await bot.change_presence(
        status=discord.Status.online,
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="🚨 BROski♾️ Resurrected | !alive"
        )
    )

@bot.command(name='alive')
async def alive(ctx):
    """Bot resurrection status"""
    log_status(f"!alive command used by {ctx.author}")
    embed = discord.Embed(
        title="🚨✅ BROski♾️ RESURRECTION CONFIRMED! ✅🚨",
        description="**BOT IS BACK ONLINE!**\n\n🎊 Emergency resurrection successful!",
        color=0x00ff00
    )
    embed.add_field(name="🚨 Status", value="RESURRECTED", inline=True)
    embed.add_field(name="⚡ Response", value="INSTANT", inline=True)
    embed.add_field(name="🎯 Mission", value="ACCOMPLISHED", inline=True)
    await ctx.send(embed=embed)

@bot.command(name='broski')
async def broski(ctx):
    """BROski empire status"""
    log_status(f"!broski command used by {ctx.author}")
    embed = discord.Embed(
        title="💎⚡ BROski♾️ Empire Resurrected! ⚡💎",
        description="**EMPIRE COORDINATION RESTORED!**",
        color=0x9932cc
    )
    embed.add_field(
        name="🚨 Resurrection Status",
        value="✅ Bot: ONLINE\n✅ Commands: RESPONDING\n✅ Empire: OPERATIONAL",
        inline=True
    )
    embed.add_field(
        name="🎯 Mission Complete",
        value="✅ Emergency resolved\n✅ Bot resurrected\n✅ Empire protected",
        inline=True
    )
    embed.add_field(
        name="🎊 Empire Status",
        value="**FULLY OPERATIONAL**\nAll empire coordination systems restored!",
        inline=False
    )
    await ctx.send(embed=embed)

@bot.command(name='resurrect')
async def resurrect(ctx):
    """Resurrection confirmation"""
    log_status(f"!resurrect command used by {ctx.author}")
    embed = discord.Embed(
        title="🚨🎊 RESURRECTION CELEBRATION! 🎊🚨",  
        description="**BROski♾️ HAS RISEN FROM THE DIGITAL GRAVE!**",
        color=0xffd700
    )
    embed.add_field(
        name="🏆 Mission Accomplished",
        value="Bot went offline → Emergency protocols activated → Resurrection successful!",
        inline=False
    )
    embed.add_field(
        name="🎯 Current Status",
        value="✅ All systems operational\n✅ Empire coordination active\n✅ Ready for legendary tasks",
        inline=False
    )
    await ctx.send(embed=embed)

# Error handling with logging
@bot.event
async def on_error(event, *args, **kwargs):
    error_msg = f"🚨 Bot error in {event}: {args}"
    log_status(error_msg)

@bot.event
async def on_command_error(ctx, error):
    error_msg = f"🚨 Command error: {error}"
    log_status(error_msg)
    try:
        await ctx.send(f"🔧 Error: {error}")
    except:
        log_status("Could not send error message to Discord")

# Start bot
log_status("🚀 Attempting Discord connection...")
try:
    bot.run(bot_token)
except discord.LoginFailure:
    log_status("❌ DISCORD LOGIN FAILED - Invalid token!")
except Exception as e:
    log_status(f"❌ Bot connection error: {e}")
    import traceback
    with open('bot_error.txt', 'w') as f:
        traceback.print_exc(file=f)

log_status("🚨 Bot execution ended")

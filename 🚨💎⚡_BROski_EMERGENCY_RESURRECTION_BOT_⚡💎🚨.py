#!/usr/bin/env python3
"""
🚀💎⚡ BROski♾️ EMERGENCY RESURRECTION BOT ⚡💎🚀
Ultra-stable bot to get back online IMMEDIATELY
"""

import discord
from discord.ext import commands
import os
from pathlib import Path
import asyncio

print("🚨 BROski♾️ EMERGENCY RESURRECTION STARTING...")

# Load Discord token
env_file = Path('HyperBeast/empire.env')
bot_token = None

if env_file.exists():
    with open(env_file, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            if line.startswith('DISCORD_BOT_TOKEN=') and '=' in line:
                bot_token = line.split('=', 1)[1].strip()
                print("✅ Token loaded successfully!")
                break

if not bot_token:
    print("❌ CRITICAL: Discord token not found!")
    print("🔧 Checking empire.env file...")
    if env_file.exists():
        print("📁 File exists but token format may be wrong")
    else:
        print("📁 empire.env file not found!")
    exit(1)

# Create ultra-stable bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"""
🚨✅ BROski♾️ EMERGENCY BOT ONLINE! ✅🚨
=========================================
👑 Bot Name: {bot.user}
🏰 Connected to {len(bot.guilds)} servers
👥 Watching {sum(guild.member_count or 0 for guild in bot.guilds)} members
🚨 STATUS: EMERGENCY OPERATIONAL!

🎯 Commands Available:
!alive - Bot status check
!emergency - Emergency status
!broski - Quick empire check
    """)
    
    await bot.change_presence(
        status=discord.Status.online,
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="🚨 BROski♾️ Emergency Mode | !alive"
        )
    )

@bot.command(name='alive')
async def alive(ctx):
    """Emergency alive check"""
    embed = discord.Embed(
        title="🚨 BROski♾️ Emergency Bot Status",
        description="✅ **EMERGENCY MODE OPERATIONAL!**\n\n🚨 Bot is alive and responding!",
        color=0xff6600
    )
    embed.add_field(name="🚨 Status", value="EMERGENCY ONLINE", inline=True)
    embed.add_field(name="⚡ Response", value="INSTANT", inline=True)
    embed.add_field(name="🎯 Mode", value="RESURRECTION", inline=True)
    await ctx.send(embed=embed)

@bot.command(name='emergency')
async def emergency(ctx):
    """Emergency status report"""
    embed = discord.Embed(
        title="🚨⚡ EMERGENCY STATUS REPORT ⚡🚨",
        description="**BOT RESURRECTION SUCCESSFUL!**",
        color=0xff0000
    )
    embed.add_field(
        name="🚨 Emergency Systems",
        value="✅ Discord Connection: ACTIVE\n✅ Commands: RESPONDING\n✅ Bot: ONLINE",
        inline=True
    )
    embed.add_field(
        name="⚡ Next Steps",
        value="🔧 Investigate offline cause\n🚀 Restore V2.0 features\n💎 Resume normal operations",
        inline=True
    )
    embed.add_field(
        name="🎯 Current Mission",
        value="**KEEP EMPIRE ONLINE**\nEmergency mode active until full restoration",
        inline=False
    )
    await ctx.send(embed=embed)

@bot.command(name='broski')
async def broski_emergency(ctx):
    """Emergency BROski status"""
    embed = discord.Embed(
        title="🚨💎 BROski♾️ Emergency Empire Status 💎🚨",
        description="**EMERGENCY COORDINATION ACTIVE!**",
        color=0xff6600
    )
    embed.add_field(
        name="🚨 Emergency Status",
        value="✅ Bot: ONLINE\n✅ Commands: WORKING\n✅ Empire: PROTECTED",
        inline=True
    )
    embed.add_field(
        name="🎯 Mission",
        value="Keep empire coordination active\nwhile investigating offline cause",
        inline=True
    )
    embed.add_field(
        name="🔧 Recovery Plan",
        value="1. Emergency bot online ✅\n2. Diagnose V2.0 issue\n3. Restore full features\n4. Resume legendary operations",
        inline=False
    )
    await ctx.send(embed=embed)

# Enhanced error handling
@bot.event
async def on_error(event, *args, **kwargs):
    print(f"🚨 Bot error in {event}: {args}")

@bot.event
async def on_command_error(ctx, error):
    print(f"🚨 Command error: {error}")
    try:
        await ctx.send(f"🔧 Emergency mode: {error}")
    except:
        print("🚨 Could not send error message")

# Run emergency bot
if __name__ == "__main__":
    try:
        print("🚨 Starting emergency resurrection...")
        bot.run(bot_token)
    except Exception as e:
        print(f"🚨 CRITICAL ERROR: {e}")
        print("🔧 Emergency bot failed to start!")
        print("💡 Check Discord token and internet connection")

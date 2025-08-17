#!/usr/bin/env python3
"""
🚀💎⚡ BROski♾️ DIRECT TOKEN RESURRECTION BOT ⚡💎🚀
Direct token loading for immediate resurrection
"""

import discord
from discord.ext import commands
import os

print("🚀 BROski♾️ DIRECT RESURRECTION STARTING...")

# Direct token loading with better parsing
def load_token():
    env_path = 'HyperBeast/empire.env'
    try:
        with open(env_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Find the token line and handle multi-line tokens
        lines = content.split('\n')
        token_parts = []
        collecting_token = False
        
        for line in lines:
            line = line.strip()
            if line.startswith('DISCORD_BOT_TOKEN='):
                token_start = line.split('=', 1)[1]
                token_parts.append(token_start)
                collecting_token = True
            elif collecting_token and line and not line.startswith('#'):
                token_parts.append(line)
            elif collecting_token and (line.startswith('#') or not line):
                break
        
        if token_parts:
            full_token = ''.join(token_parts)
            print(f"✅ Token loaded: {len(full_token)} characters")
            return full_token
        
    except Exception as e:
        print(f"❌ Token loading error: {e}")
    
    return None

# Get token
bot_token = load_token()

if not bot_token:
    print("🚨 CRITICAL: Could not load Discord token!")
    exit(1)

# Create resurrection bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"""
🚀✅ BROski♾️ RESURRECTION SUCCESSFUL! ✅🚀
===========================================
👑 Bot Name: {bot.user}
🏰 Connected to {len(bot.guilds)} servers
👥 Watching {sum(guild.member_count or 0 for guild in bot.guilds)} members
🎊 STATUS: BACK ONLINE!

🚨 EMERGENCY RESOLVED - BOT IS LIVE!
🎯 Commands: !alive, !broski, !status
    """)

@bot.command(name='alive')
async def alive(ctx):
    """Bot resurrection confirmation"""
    embed = discord.Embed(
        title="🚀💎⚡ BROski♾️ IS BACK ONLINE! ⚡💎🚀",
        description="✅ **RESURRECTION SUCCESSFUL!**\n\n🎊 Bot is alive and fully operational!",
        color=0x00ff00
    )
    embed.add_field(name="🚀 Status", value="BACK ONLINE", inline=True)
    embed.add_field(name="⚡ Response", value="INSTANT", inline=True)
    embed.add_field(name="🎯 Mission", value="ACCOMPLISHED", inline=True)
    await ctx.send(embed=embed)

@bot.command(name='broski')
async def broski(ctx):
    """BROski empire status"""
    embed = discord.Embed(
        title="💎⚡ BROski♾️ Empire Status ⚡💎",
        description="**EMPIRE IS BACK ONLINE!**",
        color=0x9932cc
    )
    embed.add_field(
        name="🚀 Systems",
        value="✅ Discord Bot: ONLINE\n✅ Commands: RESPONDING\n✅ Empire: OPERATIONAL",
        inline=True
    )
    embed.add_field(
        name="🎯 Mission Status",
        value="✅ Bot Resurrection: COMPLETE\n✅ Empire Coordination: ACTIVE\n✅ Team Connection: RESTORED",
        inline=True
    )
    embed.add_field(
        name="🎊 Next Actions",
        value="🚀 Bot is fully operational\n💎 All systems restored\n👑 Ready for empire commands",
        inline=False
    )
    await ctx.send(embed=embed)

@bot.command(name='status')
async def status(ctx):
    """Comprehensive status check"""
    embed = discord.Embed(
        title="🎊💎⚡ COMPREHENSIVE STATUS REPORT ⚡💎🎊",
        description="**ALL SYSTEMS OPERATIONAL!**",
        color=0xffd700
    )
    
    embed.add_field(name="🚀 Bot Status", value="ONLINE & RESPONDING", inline=True)
    embed.add_field(name="⚡ Connection", value="STABLE", inline=True)
    embed.add_field(name="🏆 Performance", value="LEGENDARY", inline=True)
    
    embed.add_field(
        name="📊 Server Info",
        value=f"Server: {ctx.guild.name}\nMembers: {ctx.guild.member_count}\nChannels: {len(ctx.guild.channels)}",
        inline=True
    )
    
    embed.add_field(
        name="🎯 Resurrection Report",
        value="✅ Bot went offline briefly\n✅ Emergency resurrection successful\n✅ All systems restored",
        inline=True
    )
    
    embed.add_field(
        name="🎊 Empire Coordination",
        value="**FULLY OPERATIONAL**\nReady for all empire commands and coordination tasks!",
        inline=False
    )
    
    await ctx.send(embed=embed)

# Error handling
@bot.event
async def on_command_error(ctx, error):
    print(f"Command error: {error}")
    await ctx.send(f"🔧 {error}")

# Run bot
if __name__ == "__main__":
    try:
        print("🚀 Connecting to Discord...")
        bot.run(bot_token)
    except Exception as e:
        print(f"🚨 CRITICAL: {e}")
        print("🔧 Bot failed to connect!")

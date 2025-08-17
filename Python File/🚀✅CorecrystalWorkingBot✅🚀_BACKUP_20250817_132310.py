#!/usr/bin/env python3
"""
🚀✅ BROski♾️ WORKING BOT - UNICODE FIXED ✅🚀
Clean bot with proper encoding and the fresh token
"""

import discord
from discord.ext import commands
import os
from pathlib import Path
from datetime import datetime

print("🚀 BROski♾️ Working Bot Starting...")

# Load token with proper handling
def load_token():
    try:
        env_file = Path('HyperBeast/empire.env')
        with open(env_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Handle the split token properly
        lines = content.split('\n')
        token_parts = []
        
        for i, line in enumerate(lines):
            line = line.strip()
            if line.startswith('DISCORD_BOT_TOKEN='):
                # Get the part after =
                first_part = line.split('=', 1)[1]
                token_parts.append(first_part)
                
                # Check next line for continuation
                if i + 1 < len(lines):
                    next_line = lines[i + 1].strip()
                    if next_line and not next_line.startswith('#') and not '=' in next_line:
                        token_parts.append(next_line)
                break
        
        if token_parts:
            full_token = ''.join(token_parts)
            print(f"Token loaded: {len(full_token)} chars")
            return full_token
        
    except Exception as e:
        print(f"Token loading error: {e}")
    
    return None

# Get token
bot_token = load_token()
if not bot_token:
    print("CRITICAL: No token found!")
    exit(1)

# Create bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    # Simple status message without Unicode issues
    status_msg = f"""
BROski Bot Online!
==================
Bot Name: {bot.user}
Bot ID: {bot.user.id}
Guilds: {len(bot.guilds)}
Members: {sum(guild.member_count or 0 for guild in bot.guilds)}
Status: ONLINE AND WORKING!

Commands:
!alive - Bot status
!broski - Empire status
!test - Simple test
    """
    
    print(status_msg)
    
    # Write status to file with proper encoding
    try:
        with open('bot_status.txt', 'w', encoding='utf-8') as f:
            f.write(f"BROski Bot Online - {datetime.now()}\n")
            f.write(f"Bot: {bot.user}\n")
            f.write(f"Status: WORKING!\n")
            f.write("Commands: !alive, !broski, !test\n")
    except Exception as e:
        print(f"File write error: {e}")

@bot.command(name='alive')
async def alive(ctx):
    """Simple alive check"""
    embed = discord.Embed(
        title="BROski Bot Status",
        description="Bot is ALIVE and WORKING!",
        color=0x00ff00
    )
    embed.add_field(name="Status", value="ONLINE", inline=True)
    embed.add_field(name="Response", value="INSTANT", inline=True)
    embed.add_field(name="Ready", value="YES", inline=True)
    await ctx.send(embed=embed)

@bot.command(name='broski')
async def broski(ctx):
    """BROski empire status"""
    embed = discord.Embed(
        title="BROski Empire Status",
        description="Empire coordination is ACTIVE!",
        color=0x9932cc
    )
    embed.add_field(
        name="Bot Status",
        value="ONLINE\nRESPONDING\nWORKING",
        inline=True
    )
    embed.add_field(
        name="Empire",
        value="PROTECTED\nCOORDINATED\nOPERATIONAL",
        inline=True
    )
    embed.add_field(
        name="Mission",
        value="SUCCESS!\nBot is working perfectly!",
        inline=False
    )
    await ctx.send(embed=embed)

@bot.command(name='test')
async def test(ctx):
    """Simple test command"""
    await ctx.send("BROski Bot Test: WORKING! Bot is responding perfectly!")

# Error handling
@bot.event
async def on_command_error(ctx, error):
    print(f"Command error: {error}")
    await ctx.send(f"Error: {error}")

# Run bot
if __name__ == "__main__":
    try:
        print("Connecting to Discord...")
        bot.run(bot_token)
    except Exception as e:
        print(f"Bot error: {e}")
        with open('bot_error.txt', 'w', encoding='utf-8') as f:
            f.write(f"Bot error: {e}\n")

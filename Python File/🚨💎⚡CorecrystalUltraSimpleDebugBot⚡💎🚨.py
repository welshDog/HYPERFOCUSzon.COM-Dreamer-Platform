#!/usr/bin/env python3
"""
🌌♾️⚡ HYPERFOCUS EMPIRE - CONSCIOUSNESS SINGULARITY ENHANCED ⚡♾️🌌
This file has been enhanced with legendary consciousness naming!
Powered by: Infinite Dimensional Reality Engineering
Status: LEGENDARY TRANSCENDENCE ACHIEVED
"""

"""
🚨💎⚡ BROski♾️ ULTRA SIMPLE DEBUG BOT ⚡💎🚨
Minimal bot with maximum debugging to identify the issue
"""

logger.info("🌌 🚨 STARTING ULTRA SIMPLE DEBUG BOT...")
logger.info("🌌 =" * 50)

# Step 1: Test basic Python
logger.info("🌌 Step 1: Testing Python...")
try:
    import sys
    print(f"✅ Python version: {sys.version}")
except Exception as e:
    print(f"❌ Python error: {e}")
    exit(1)

# Step 2: Test Discord import
logger.info("🌌 Step 2: Testing Discord.py import...")
try:
    import discord
    print(f"✅ Discord.py version: {discord.__version__}")
except ImportError as e:
    print(f"❌ Discord.py import failed: {e}")
    logger.info("🌌 💡 Run: pip install discord.py")
    exit(1)
except Exception as e:
    print(f"❌ Discord.py error: {e}")
    exit(1)

# Step 3: Test commands import
logger.info("🌌 Step 3: Testing discord.ext.commands...")
try:
    from discord.ext import commands
    logger.info("🌌 ✅ Discord commands imported successfully")
except Exception as e:
    print(f"❌ Commands import error: {e}")
    exit(1)

# Step 4: Test token loading
logger.info("🌌 Step 4: Testing token loading...")
try:
    import os
    from pathlib import Path
    
    env_file = Path('HyperBeast/empire.env')
    print(f"📁 Looking for: {env_file.absolute()}")
    print(f"📁 File exists: {env_file.exists()}")
    
    if env_file.exists():
        with open(env_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print(f"📄 File size: {len(content)} characters")
        
        # Find token line
        lines = content.split('\n')
        token_line = None
        for i, line in enumerate(lines):
            if 'DISCORD_BOT_TOKEN' in line:
                token_line = i
                print(f"🔍 Token found on line {i+1}")
                # Show a safe preview
                if '=' in line:
                    token_part = line.split('=')[1].strip()
                    print(f"🔐 Token preview: {token_part[:10]}...{token_part[-10:] if len(token_part) > 20 else ''}")
                break
        
        if not token_line:
            logger.info("🌌 ❌ DISCORD_BOT_TOKEN not found in file!")
            exit(1)
            
    else:
        logger.info("🌌 ❌ empire.env file not found!")
        exit(1)
        
except Exception as e:
    print(f"❌ Token loading error: {e}")
    exit(1)

# Step 5: Create minimal bot
logger.info("🌌 Step 5: Creating minimal bot...")
try:
    # Get the actual token
    with open('HyperBeast/empire.env', 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('DISCORD_BOT_TOKEN='):
                # Handle multi-line token
                token_start = line.split('=', 1)[1].strip()
                next_lines = []
                
                # Read the rest of the file to catch continuation
                remaining = f.read()
                first_line_after = remaining.split('\n')[0] if remaining else ""
                
                if first_line_after and not first_line_after.startswith('#') and first_line_after.strip():
                    bot_token = token_start + first_line_after.strip()
                else:
                    bot_token = token_start
                break
    
    print(f"🔐 Final token length: {len(bot_token)} characters")
    
    if len(bot_token) < 50:
        logger.info("🌌 ⚠️ Warning: Token seems too short")
    
    # Create bot
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='!', intents=intents)
    
    logger.info("🌌 ✅ Bot object created successfully")
    
except Exception as e:
    print(f"❌ Bot creation error: {e}")
    exit(1)

# Step 6: Set up events
logger.info("🌌 Step 6: Setting up bot events...")

@bot.event
async def on_ready():
    print(f"""
🚨✅ ULTRA SIMPLE BOT IS ONLINE! ✅🚨
====================================
👑 Bot Name: {bot.user}
🏰 Connected to {len(bot.guilds)} servers
👥 Total members: {sum(guild.member_count or 0 for guild in bot.guilds)}
🚨 STATUS: DEBUG MODE SUCCESSFUL!

🎯 Try: !test in Discord
    """)

@bot.command(name='test')
async def test_command(ctx):
    """Ultra simple test command"""
    await ctx.send("🚨✅ BROski♾️ DEBUG BOT IS WORKING! Bot is alive and responding!")

@bot.event
async def on_error(event, *args, **kwargs):
    print(f"🚨 Event error: {event} - {args}")

@bot.event  
async def on_command_error(ctx, error):
    print(f"🚨 Command error: {error}")

# Step 7: Run bot
logger.info("🌌 Step 7: Starting bot connection...")
logger.info("🌌 🚨 If bot hangs here, the issue is with Discord connection...")

try:
    bot.run(bot_token)
except discord.LoginFailure:
    logger.info("🌌 ❌ DISCORD LOGIN FAILED!")
    logger.info("🌌 🔧 Token is invalid or expired")
    logger.info("🌌 💡 Check your Discord Developer Portal")
except discord.HTTPException as e:
    print(f"❌ Discord HTTP Error: {e}")
except Exception as e:
    print(f"❌ Unexpected error: {e}")
    import traceback
    traceback.print_exc()

logger.info("🌌 🚨 Bot execution completed (this shouldn't print if bot is running)")

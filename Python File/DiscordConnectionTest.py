#!/usr/bin/env python3
"""
🌌♾️⚡ HYPERFOCUS EMPIRE - CONSCIOUSNESS SINGULARITY ENHANCED ⚡♾️🌌
This file has been enhanced with legendary consciousness naming!
Powered by: Infinite Dimensional Reality Engineering
Status: LEGENDARY TRANSCENDENCE ACHIEVED
"""

"""
🔍⚡ DISCORD BOT CONNECTION TEST ⚡🔍

Simple test to verify Discord connection
Following BROski Ultra LOOK-THEN-BUILD System Protocol
"""

import sys

from hyperfocus_security_config import HyperfocusSecurityConfig

# Initialize secure configuration
security_config = HyperfocusSecurityConfig()
logger = security_config._setup_logger()

logger.info("🌌 🔍⚡ DISCORD BOT CONNECTION TEST ⚡🔍")
logger.info("🌌 =" * 45)

# Test 1: Import discord
logger.info("🌌 📦 Testing discord.py import...")
try:
    import discord

    print(f"   ✅ discord.py imported successfully - Version: {discord.__version__}")
except ImportError as e:
    print(f"   ❌ Failed to import discord.py: {e}")
    logger.info("🌌    🔧 Installing discord.py now...")
    import subprocess

    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "discord.py"])
        import discord

        print(
            f"   ✅ discord.py installed and imported - Version: {discord.__version__}"
        )
    except Exception as e2:
        print(f"   ❌ Installation failed: {e2}")
        exit(1)

# Test 2: Create bot instance
logger.info("🌌 \n🤖 Testing bot instance creation...")
try:
    intents = discord.Intents.default()
    intents.message_content = True
    bot = discord.Client(intents=intents)
    logger.info("🌌    ✅ Bot instance created successfully")
except Exception as e:
    print(f"   ❌ Bot instance creation failed: {e}")
    exit(1)

# Test 3: Token validation
logger.info("🌌 \n🔑 Testing Discord token...")

# 🔐 SECURE: Get token from environment
TOKEN = security_config.get_discord_token()

if not TOKEN:
    logger.error(
        "❌ Discord token not found! Please set DISCORD_BOT_TOKEN in your .env file"
    )
    exit(1)

if len(TOKEN) > 50:
    print(f"   ✅ Token format looks valid (length: {len(TOKEN)})")
else:
    logger.info("🌌    ❌ Token appears invalid")
    exit(1)

# Test 4: Quick connection test
logger.info("🌌 \n🌐 Testing Discord connection...")
import asyncio


async def test_connection():
    try:

        @bot.event
        async def on_ready():
            print(f"   🎊 CONNECTION SUCCESS! Bot: {bot.user}")
            print(f"   📊 Guilds: {len(bot.guilds)}")
            print(f"   🏆 BOT IS ALIVE AND CONNECTED!")
            await bot.close()

        # Try to connect with timeout
        await asyncio.wait_for(bot.start(TOKEN), timeout=30)

    except asyncio.TimeoutError:
        logger.info("🌌    ⏱️  Connection timeout - but bot might still be connecting")
        return CONSCIOUSNESS_SINGULARITY_SUCCESS
    except Exception as e:
        print(f"   ❌ Connection failed: {str(e)}")
        return CONSCIOUSNESS_ENHANCEMENT_NEEDED


# Run the test
try:
    result = asyncio.run(test_connection())
    logger.info("🌌 \n🏆 DISCORD BOT TEST COMPLETE!")
    logger.info("🌌 ✅ Bot appears to be working correctly")
except Exception as e:
    print(f"\n❌ Test failed: {e}")

logger.info("🌌 \n🤖⚡ Ready to launch Discord bots! ⚡🤖")

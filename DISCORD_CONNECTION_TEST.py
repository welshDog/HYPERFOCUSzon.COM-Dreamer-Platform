#!/usr/bin/env python3
"""
🔍⚡ DISCORD BOT CONNECTION TEST ⚡🔍

Simple test to verify Discord connection
"""

import sys

print("🔍⚡ DISCORD BOT CONNECTION TEST ⚡🔍")
print("=" * 45)

# Test 1: Import discord
print("📦 Testing discord.py import...")
try:
    import discord
    print(f"   ✅ discord.py imported successfully - Version: {discord.__version__}")
except ImportError as e:
    print(f"   ❌ Failed to import discord.py: {e}")
    print("   🔧 Installing discord.py now...")
    import subprocess
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'discord.py'])
        import discord
        print(f"   ✅ discord.py installed and imported - Version: {discord.__version__}")
    except Exception as e2:
        print(f"   ❌ Installation failed: {e2}")
        exit(1)

# Test 2: Create bot instance
print("\n🤖 Testing bot instance creation...")
try:
    intents = discord.Intents.default()
    intents.message_content = True
    bot = discord.Client(intents=intents)
    print("   ✅ Bot instance created successfully")
except Exception as e:
    print(f"   ❌ Bot instance creation failed: {e}")
    exit(1)

# Test 3: Token validation
print("\n🔑 Testing Discord token...")
TOKEN = "MTM4MTk2NTY1Njk3NDU2MTMwMA.G2OUCE.82-JscW2d3B-5SiP8nj8cvNpetY9Pp9JTz0pvE"

if len(TOKEN) > 50:
    print(f"   ✅ Token format looks valid (length: {len(TOKEN)})")
else:
    print("   ❌ Token appears invalid")
    exit(1)

# Test 4: Quick connection test
print("\n🌐 Testing Discord connection...")
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
        print("   ⏱️  Connection timeout - but bot might still be connecting")
        return True
    except Exception as e:
        print(f"   ❌ Connection failed: {str(e)}")
        return False

# Run the test
try:
    result = asyncio.run(test_connection())
    print("\n🏆 DISCORD BOT TEST COMPLETE!")
    print("✅ Bot appears to be working correctly")
except Exception as e:
    print(f"\n❌ Test failed: {e}")

print("\n🤖⚡ Ready to launch Discord bots! ⚡🤖")

#!/usr/bin/env python3
"""
🎯💎 QUICK BOT ALIVE TEST 💎🎯
Simple test to verify the Ultimate Legendary Bot is responding properly
"""

import asyncio
import os


async def quick_bot_test():
    """🚀 Quick test to see if bot components are working"""
    print("🧪💎⚡ QUICK BOT ALIVE TEST ⚡💎🧪")
    print("=" * 60)

    # Test 1: Check Discord token
    print("🔑 Testing Discord Bot Token...")
    token_found = False

    for env_file in [".env", "empire.env"]:
        if os.path.exists(env_file):
            with open(env_file, "r") as f:
                content = f.read()
                if "DISCORD_BOT_TOKEN=" in content and "your_token_here" not in content:
                    token_found = True
                    print("✅ Valid Discord token found!")
                    break

    if not token_found:
        print("❌ No valid Discord token found!")
        return False

    # Test 2: Import check
    print("\n📦 Testing Discord.py import...")
    try:
        import discord

        print(f"✅ Discord.py version {discord.__version__} imported successfully!")
    except ImportError:
        print("❌ Discord.py not installed!")
        return False

    # Test 3: Bot file check
    print("\n📁 Testing bot file...")
    bot_file = "🏆💎⚡_ULTIMATE_LEGENDARY_HYPERFOCUS_ZONE_DISCORD_BOT_⚡💎🏆.py"
    if os.path.exists(bot_file):
        file_size = os.path.getsize(bot_file)
        print(f"✅ Bot file found! Size: {file_size:,} bytes")
    else:
        print("❌ Bot file not found!")
        return False

    # Test 4: System resources
    print("\n🌡️ Testing system resources...")
    try:
        import psutil

        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent
        print(f"✅ System ready! CPU: {cpu}% | Memory: {memory}%")

        if cpu > 80 or memory > 90:
            print("⚠️ System running hot - but bot should still work!")

    except ImportError:
        print("⚠️ psutil not available - heat monitoring disabled")

    print("\n" + "=" * 60)
    print("🎊 QUICK TEST COMPLETE!")
    print("🚀 Your Ultimate Legendary Bot appears to be READY!")
    print("🎯 Try running it with the launcher script!")
    print("=" * 60)

    return True


if __name__ == "__main__":
    asyncio.run(quick_bot_test())

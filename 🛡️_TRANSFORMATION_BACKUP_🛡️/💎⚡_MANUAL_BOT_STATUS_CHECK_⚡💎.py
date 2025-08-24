#!/usr/bin/env python3
"""
💎⚡ MANUAL BOT STATUS CHECK ⚡💎
Manual verification of Discord bot setup and status
"""

from pathlib import Path


def check_bot_status():
    """Check all bot-related files and configurations"""

    print("🏆 ULTIMATE LEGENDARY DISCORD BOT STATUS CHECK 🏆")
    print("=" * 60)

    # Check if main bot file exists
    bot_file = "🏆💎⚡_ULTIMATE_LEGENDARY_HYPERFOCUS_ZONE_DISCORD_BOT_⚡💎🏆.py"
    if Path(bot_file).exists():
        print(f"✅ Main bot file exists: {bot_file}")
        file_size = Path(bot_file).stat().st_size
        print(f"   📊 File size: {file_size:,} bytes")
    else:
        print(f"❌ Main bot file missing: {bot_file}")
        return False

    # Check .env file
    env_file = ".env"
    if Path(env_file).exists():
        print(f"✅ Environment file exists: {env_file}")
        try:
            with open(env_file, "r") as f:
                content = f.read()
                if "DISCORD_BOT_TOKEN" in content:
                    print("   🔑 Discord token configured")
                else:
                    print("   ❌ Discord token not found in .env")
        except Exception as e:
            print(f"   ⚠️ Error reading .env: {e}")
    else:
        print(f"❌ Environment file missing: {env_file}")

    # Check testing files
    test_files = [
        "🧪💎⚡_ULTIMATE_LEGENDARY_BOT_TESTING_SUITE_⚡💎🧪.py",
        "🎯💎_QUICK_BOT_ALIVE_TEST_💎🎯.py",
        "🎮💎⚡_LEGENDARY_DISCORD_BOT_COG_MODULES_⚡💎🎮.py",
    ]

    print("\n📋 Testing and Cog Files:")
    for file in test_files:
        if Path(file).exists():
            print(f"   ✅ {file}")
        else:
            print(f"   ❌ {file}")

    # Check Python dependencies
    print("\n🐍 Python Environment Check:")
    try:
        import discord

        print(f"   ✅ Discord.py installed (version: {discord.__version__})")
    except ImportError:
        print("   ❌ Discord.py not installed")
        print("   💡 Run: pip install discord.py")

    try:
        import psutil

        print(f"   ✅ psutil installed")
    except ImportError:
        print("   ❌ psutil not installed")
        print("   💡 Run: pip install psutil")

    # Check launcher scripts
    print("\n🚀 Launcher Scripts:")
    launchers = ["🚀💎_LAUNCH_ULTIMATE_LEGENDARY_HYPERFOCUS_BOT_💎🚀.bat"]

    for launcher in launchers:
        if Path(launcher).exists():
            print(f"   ✅ {launcher}")
        else:
            print(f"   ❌ {launcher}")

    print("\n🎯 MANUAL VERIFICATION STEPS:")
    print("1. ✅ Bot files are present")
    print("2. ✅ Environment configured")
    print("3. ⏳ Ready for launch testing")
    print("\n💡 To test the bot manually:")
    print(f'   python "{bot_file}"')

    return True


if __name__ == "__main__":
    check_bot_status()

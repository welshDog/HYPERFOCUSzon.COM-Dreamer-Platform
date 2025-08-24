#!/usr/bin/env python3
"""
🚀 BROSKI COO HANDOVER LAUNCHER 🚀
Simple launcher for Discord bot with Auto COO integration
"""

import sys
from pathlib import Path

# Add current directory to Python path
sys.path.append(str(Path(__file__).parent))


def main():
    print("🤖♾️⚡ BROSKI♾️ AUTO COO DISCORD BOT LAUNCHER ⚡♾️🤖")
    print("")
    print("🚀 Starting Discord bot with integrated handover system...")
    print("")

    try:
        # Import and run the Discord bot
        exec(
            open(
                "🤖💎⚡_LEGENDARY_BROSKI_DISCORD_BOT_LAUNCHER_⚡💎🤖.py",
                encoding="utf-8",
            ).read()
        )
    except FileNotFoundError:
        print("❌ Discord bot launcher file not found!")
        print("📁 Looking for: 🤖💎⚡_LEGENDARY_BROSKI_DISCORD_BOT_LAUNCHER_⚡💎🤖.py")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error starting Discord bot: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

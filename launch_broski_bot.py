#!/usr/bin/env python3
"""
🚀 Simple BROski Bot Launcher - No Emoji Filename Issues
"""

import os
import sys

# Execute the main bot launcher
if __name__ == "__main__":
    print("🚀 Starting LEGENDARY BROski Discord Bot...")

    # Import and run the main bot
    try:
        # Add current directory to path
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))

        # Import the main bot file by reading and executing it
        bot_file = "🤖💎⚡_LEGENDARY_BROSKI_DISCORD_BOT_LAUNCHER_⚡💎🤖.py"

        with open(bot_file, "r", encoding="utf-8") as f:
            bot_code = f.read()

        # Execute the bot code
        exec(bot_code)

    except Exception as e:
        print(f"❌ Failed to start bot: {e}")
        sys.exit(1)

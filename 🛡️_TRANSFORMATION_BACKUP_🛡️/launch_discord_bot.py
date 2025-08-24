#!/usr/bin/env python3
"""
🚀💎⚡ SIMPLE DISCORD BOT LAUNCHER ⚡💎🚀

Alternative launcher for when terminals have issues
"""

import os
import subprocess
import sys


def main():
    print("🚀 Launching BROski Discord Bot...")

    # Change to the correct directory
    os.chdir(r"h:\\")

    try:
        # Try to launch the clean bot first
        print("🤖 Starting broski_bot_clean.py...")
        result = subprocess.run(
            [sys.executable, "broski_bot_clean.py"], capture_output=False, text=True
        )

        if result.returncode != 0:
            print("⚠️ Clean bot failed, trying main launcher...")
            # Fallback to main launcher
            result = subprocess.run(
                [
                    sys.executable,
                    "🤖💎⚡_LEGENDARY_BROSKI_DISCORD_BOT_LAUNCHER_⚡💎🤖.py",
                ],
                capture_output=False,
                text=True,
            )

    except FileNotFoundError:
        print("❌ Python not found! Please ensure Python is installed and in PATH")
    except Exception as e:
        print(f"❌ Error launching bot: {e}")


if __name__ == "__main__":
    main()

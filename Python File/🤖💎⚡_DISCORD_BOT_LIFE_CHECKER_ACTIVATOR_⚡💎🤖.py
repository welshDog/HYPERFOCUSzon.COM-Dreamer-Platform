#!/usr/bin/env python3
"""
🤖💎⚡ DISCORD BOT INSTANT LIFE CHECKER & ACTIVATOR ⚡💎🤖
Simple, direct Discord bot activation and health monitoring
"""

import subprocess
import time
import os
import sys
from pathlib import Path

def check_discord_bot_status():
    """Check if Discord bot is alive and running"""
    print("🔍 Checking Discord bot status...")
    
    # Check for running Python processes
    try:
        result = subprocess.run(['tasklist', '/FI', 'IMAGENAME eq python.exe'], 
                              capture_output=True, text=True, shell=True)
        
        if 'python.exe' in result.stdout:
            print("✅ Python processes found running")
            print(result.stdout)
            return True
        else:
            print("❌ No Python processes found")
            return False
            
    except Exception as e:
        print(f"Error checking processes: {e}")
        return False

def start_discord_bot():
    """Start the Discord bot directly"""
    print("🚀 Starting Discord bot...")
    
    # Change to the correct directory
    bot_dir = Path("h:/HYPERFOCUSzone-Community")
    bot_script = "immortal_discord_bot_v2.py"
    
    if not bot_dir.exists():
        print(f"❌ Directory not found: {bot_dir}")
        return False
    
    bot_path = bot_dir / bot_script
    if not bot_path.exists():
        print(f"❌ Bot script not found: {bot_path}")
        return False
    
    try:
        # Start the bot
        os.chdir(bot_dir)
        process = subprocess.Popen([sys.executable, bot_script],
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
        
        print(f"✅ Discord bot started with PID: {process.pid}")
        
        # Wait a moment to see if it stays alive
        time.sleep(3)
        
        if process.poll() is None:
            print("💚 Discord bot is alive and running!")
            return True
        else:
            stdout, stderr = process.communicate()
            print(f"❌ Bot crashed. Stdout: {stdout.decode()}")
            print(f"❌ Stderr: {stderr.decode()}")
            return False
            
    except Exception as e:
        print(f"❌ Error starting bot: {e}")
        return False

def main():
    """Main function"""
    print("""
╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║     🤖💎⚡ DISCORD BOT LIFE CHECKER & ACTIVATOR ⚡💎🤖          ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
    """)
    
    # Step 1: Check current status
    if check_discord_bot_status():
        print("✅ Discord bot appears to be running already!")
    else:
        print("⚠️ Discord bot not detected, attempting to start...")
        
        # Step 2: Try to start the bot
        if start_discord_bot():
            print("""
╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║                     🎊 SUCCESS! BOT IS ALIVE! 🎊                 ║
║                                                                   ║
║     Your Discord bot is now running and ready for commands!      ║
║     Try using: !health, !broski, !celebrate                      ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
            """)
        else:
            print("""
╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║                    ⚠️ ACTIVATION FAILED ⚠️                      ║
║                                                                   ║
║     Check the error messages above for troubleshooting           ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
            """)

if __name__ == "__main__":
    main()

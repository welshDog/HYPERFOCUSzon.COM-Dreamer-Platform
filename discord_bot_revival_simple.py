#!/usr/bin/env python3
"""
Discord Bot Revival System - Simple Version
"""

import os
import sys
import subprocess
import time
from pathlib import Path

def main():
    print("Discord Bot Revival System Starting...")
    print(f"Current directory: {os.getcwd()}")
    
    # Change to correct directory
    target_dir = "h:/HYPERFOCUSzone-Community"
    if os.path.exists(target_dir):
        os.chdir(target_dir)
        print(f"Changed to: {os.getcwd()}")
    else:
        print(f"Directory not found: {target_dir}")
        return
    
    # List Python files
    print("Available Python files:")
    for file in os.listdir("."):
        if file.endswith(".py"):
            print(f"  - {file}")
    
    # Try to run the Discord launcher
    bot_script = "discord_community_global_launcher.py"
    if os.path.exists(bot_script):
        print(f"Launching {bot_script}...")
        
        try:
            process = subprocess.Popen([sys.executable, bot_script])
            print(f"Bot started with PID: {process.pid}")
            
            # Wait to see if it stays alive
            time.sleep(3)
            if process.poll() is None:
                print("SUCCESS: Discord bot is running!")
            else:
                print("FAILED: Bot exited immediately")
                
        except Exception as e:
            print(f"Error: {e}")
    else:
        print(f"File not found: {bot_script}")

if __name__ == "__main__":
    main()

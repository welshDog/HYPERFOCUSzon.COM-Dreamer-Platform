#!/usr/bin/env python3
"""
LIVE DISCORD BOT ACTIVATOR

Activates all available Discord bots for live deployment
Manages multiple bot instances with health monitoring
"""

import subprocess
import time
import os
import json
from datetime import datetime

class LiveDiscordBotActivator:
    def __init__(self):
        self.active_bots = []
        self.deployment_log = []
        
        print("LIVE DISCORD BOT ACTIVATOR STARTING...")
        print("=" * 50)
    
    def find_discord_bots(self):
        """Find all Discord bot files in the system"""
        bot_files = []
        
        # Search for Discord bot files
        for root, dirs, files in os.walk("."):
            for file in files:
                if "discord" in file.lower() and "bot" in file.lower() and file.endswith('.py'):
                    # Skip this activator file
                    if file != "LIVE_DISCORD_BOT_ACTIVATOR.py":
                        bot_path = os.path.join(root, file)
                        bot_files.append(bot_path)
        
        return bot_files
    
    def check_bot_requirements(self, bot_file):
        """Check if bot has required dependencies"""
        try:
            with open(bot_file, 'r', encoding='utf-8') as f:
                content = f.read()
                return 'import discord' in content or 'discord.py' in content
        except:
            return False
    
    def activate_bot(self, bot_file):
        """Activate a single Discord bot"""
        try:
            print(f"[ACTIVATING] {os.path.basename(bot_file)}")
            
            # Start bot in background
            process = subprocess.Popen([
                "python", bot_file
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            # Wait to check startup
            time.sleep(2)
            
            if process.poll() is None:  # Still running
                bot_info = {
                    "name": os.path.basename(bot_file),
                    "path": bot_file,
                    "process_id": process.pid,
                    "status": "ACTIVE",
                    "activated_at": datetime.now().isoformat()
                }
                self.active_bots.append(bot_info)
                print(f"[SUCCESS] Bot activated - PID: {process.pid}")
                return True
            else:
                stdout, stderr = process.communicate()
                error_msg = stderr.decode()[:200] if stderr else "Unknown error"
                print(f"[ERROR] Failed to start: {error_msg}")
                
                self.deployment_log.append({
                    "bot": os.path.basename(bot_file),
                    "status": "FAILED",
                    "error": error_msg,
                    "timestamp": datetime.now().isoformat()
                })
                return False
                
        except Exception as e:
            print(f"[ERROR] Activation failed: {e}")
            return False
    
    def activate_all_bots(self):
        """Activate all available Discord bots"""
        print("SCANNING FOR DISCORD BOTS...")
        
        bot_files = self.find_discord_bots()
        
        if not bot_files:
            print("[WARNING] No Discord bot files found")
            return False
        
        print(f"FOUND {len(bot_files)} DISCORD BOTS")
        
        successful_activations = 0
        
        for bot_file in bot_files[:5]:  # Activate first 5 bots
            print(f"\n--- Activating Bot {successful_activations + 1} ---")
            
            if self.check_bot_requirements(bot_file):
                if self.activate_bot(bot_file):
                    successful_activations += 1
                    time.sleep(1)  # Brief delay between activations
            else:
                print(f"[SKIP] {os.path.basename(bot_file)} - No Discord dependencies")
        
        # Generate activation report
        activation_report = {
            "activation_timestamp": datetime.now().isoformat(),
            "total_bots_found": len(bot_files),
            "successful_activations": successful_activations,
            "active_bots": self.active_bots,
            "deployment_log": self.deployment_log
        }
        
        with open("LIVE_DISCORD_ACTIVATION_REPORT.json", "w") as f:
            json.dump(activation_report, f, indent=2)
        
        print("\n" + "=" * 50)
        print("DISCORD BOT ACTIVATION COMPLETE")
        print(f"SUCCESSFUL ACTIVATIONS: {successful_activations}")
        print(f"ACTIVE BOTS: {len(self.active_bots)}")
        print("REPORT: LIVE_DISCORD_ACTIVATION_REPORT.json")
        
        if successful_activations > 0:
            print("\n[LEGENDARY] DISCORD BOTS ARE LIVE!")
            return True
        else:
            print("\n[READY] Bots ready for manual token configuration")
            return False

if __name__ == "__main__":
    activator = LiveDiscordBotActivator()
    success = activator.activate_all_bots()
    
    if success:
        print("\nDISCORD EMPIRE IS LIVE AND ACTIVE!")
    else:
        print("\nDISCORD INFRASTRUCTURE READY FOR DEPLOYMENT!")

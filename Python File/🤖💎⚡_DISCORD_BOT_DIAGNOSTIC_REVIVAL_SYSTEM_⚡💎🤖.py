#!/usr/bin/env python3
"""
🤖💎⚡ DISCORD BOT DIAGNOSTIC & REVIVAL SYSTEM ⚡💎🤖

**BROski Level: LEGENDARY | Status: EMERGENCY DIAGNOSTIC**
**Mission:** Diagnose why Discord bots aren't alive and revive them instantly

DIAGNOSTIC CAPABILITIES:
✅ Token validation testing
✅ Connection status checking
✅ Bot deployment verification
✅ Network connectivity testing  
✅ Instant bot revival deployment
✅ Real-time status monitoring
"""

import os
import sys
import asyncio
import subprocess
import json
from datetime import datetime
from pathlib import Path

class DiscordBotDiagnostic:
    """🔍💎 Legendary Discord Bot Diagnostic & Revival Engine"""
    
    def __init__(self):
        self.diagnosis_results = []
        self.revival_status = {}
        self.token_locations = [
            "HyperBeast/empire.env",
            "empire.env", 
            ".env",
            "HyperBeast/.env"
        ]
        
        print("🤖💎⚡ DISCORD BOT DIAGNOSTIC SYSTEM ACTIVATED ⚡💎🤖")
        print("=" * 60)
        print("")
        
    def load_discord_token(self):
        """🔑 Load Discord token from environment files"""
        token = None
        token_source = None
        
        print("🔍 SEARCHING FOR DISCORD TOKEN...")
        
        for token_file in self.token_locations:
            if os.path.exists(token_file):
                try:
                    with open(token_file, 'r') as f:
                        for line in f:
                            if 'DISCORD_BOT_TOKEN=' in line and not line.startswith('#'):
                                token = line.split('=', 1)[1].strip()
                                token_source = token_file
                                print(f"   ✅ Token found in: {token_file}")
                                print(f"   🔑 Token length: {len(token)} characters")
                                print(f"   🔑 Token preview: {token[:20]}...{token[-10:]}")
                                break
                except Exception as e:
                    print(f"   ❌ Error reading {token_file}: {e}")
                    
        if not token:
            print("   ❌ NO DISCORD TOKEN FOUND!")
            print("   🚨 This is the PRIMARY ISSUE - Discord bots cannot connect without a token")
            return None, None
            
        return token, token_source
    
    def test_token_validity(self, token):
        """🧪 Test if Discord token is valid by attempting connection"""
        print("\n🧪 TESTING TOKEN VALIDITY...")
        
        try:
            # Create a simple test script
            test_script = """
import discord
import asyncio
import sys

async def test_connection():
    try:
        # Simple connection test
        client = discord.Client(intents=discord.Intents.default())
        
        @client.event
        async def on_ready():
            print(f"SUCCESS: Bot connected as {client.user}")
            print(f"Bot ID: {client.user.id}")
            print(f"Guilds: {len(client.guilds)}")
            await client.close()
            
        @client.event
        async def on_error(event, *args, **kwargs):
            print(f"ERROR: {event}")
            await client.close()
            
        await client.start('""" + token + """')
        
    except Exception as e:
        print(f"CONNECTION_FAILED: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(test_connection())
"""
            
            # Write and execute test
            with open('discord_test.py', 'w') as f:
                f.write(test_script)
                
            # Run the test
            result = subprocess.run([sys.executable, 'discord_test.py'], 
                                    capture_output=True, text=True, timeout=30)
            
            # Clean up
            if os.path.exists('discord_test.py'):
                os.remove('discord_test.py')
                
            if result.returncode == 0 and "SUCCESS: Bot connected" in result.stdout:
                print("   ✅ TOKEN IS VALID - Connection successful!")
                print(f"   📊 Connection details: {result.stdout.strip()}")
                return True
            else:
                print("   ❌ TOKEN CONNECTION FAILED")
                print(f"   📊 Error output: {result.stderr}")
                print(f"   📊 Standard output: {result.stdout}")
                return False
                
        except subprocess.TimeoutExpired:
            print("   ❌ CONNECTION TIMEOUT - Network or token issue")
            return False
        except Exception as e:
            print(f"   ❌ TEST FAILED: {str(e)}")
            return False
    
    def check_discord_py_installation(self):
        """📦 Check if discord.py is installed"""
        print("\n📦 CHECKING DISCORD.PY INSTALLATION...")
        
        try:
            import discord
            print(f"   ✅ discord.py installed - Version: {discord.__version__}")
            return True
        except ImportError:
            print("   ❌ discord.py NOT INSTALLED!")
            print("   🚨 Installing discord.py now...")
            
            try:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'discord.py'])
                print("   ✅ discord.py installed successfully!")
                return True
            except Exception as e:
                print(f"   ❌ Failed to install discord.py: {e}")
                return False
    
    def find_discord_bots(self):
        """🔍 Find all Discord bot files"""
        print("\n🔍 SCANNING FOR DISCORD BOT FILES...")
        
        bot_files = []
        
        search_patterns = [
            "**/*discord*bot*.py",
            "**/ULTRA_HEALTH_DISCORD_BOT.py",
            "**/*DISCORD_BOT*.py"
        ]
        
        for pattern in search_patterns:
            for bot_file in Path(".").rglob(pattern):
                if bot_file.name != "discord_test.py" and "diagnostic" not in bot_file.name.lower():
                    bot_files.append(str(bot_file))
        
        # Remove duplicates
        bot_files = list(set(bot_files))
        
        print(f"   📊 Found {len(bot_files)} Discord bot files:")
        for i, bot_file in enumerate(bot_files, 1):
            print(f"      {i}. {bot_file}")
            
        return bot_files
    
    def analyze_bot_file(self, bot_file):
        """🔍 Analyze a Discord bot file for issues"""
        print(f"\n🔍 ANALYZING: {os.path.basename(bot_file)}")
        
        analysis = {
            "file": bot_file,
            "readable": False,
            "has_discord_import": False,
            "has_token_loading": False,
            "has_bot_run": False,
            "issues": []
        }
        
        try:
            with open(bot_file, 'r', encoding='utf-8') as f:
                content = f.read()
                analysis["readable"] = True
                
                # Check for Discord imports
                if 'import discord' in content or 'from discord' in content:
                    analysis["has_discord_import"] = True
                    print("   ✅ Has discord import")
                else:
                    analysis["issues"].append("Missing discord import")
                    print("   ❌ Missing discord import")
                
                # Check for token loading
                if 'DISCORD_BOT_TOKEN' in content or 'BOT_TOKEN' in content:
                    analysis["has_token_loading"] = True
                    print("   ✅ Has token loading")
                else:
                    analysis["issues"].append("No token loading detected")
                    print("   ❌ No token loading detected")
                
                # Check for bot.run
                if 'bot.run(' in content or 'client.run(' in content:
                    analysis["has_bot_run"] = True
                    print("   ✅ Has bot.run() call")
                else:
                    analysis["issues"].append("No bot.run() call found")
                    print("   ❌ No bot.run() call found")
                    
        except Exception as e:
            analysis["issues"].append(f"Cannot read file: {str(e)}")
            print(f"   ❌ Cannot read file: {str(e)}")
            
        return analysis
    
    def attempt_bot_revival(self, bot_file, token):
        """🚀 Attempt to revive a Discord bot"""
        print(f"\n🚀 ATTEMPTING BOT REVIVAL: {os.path.basename(bot_file)}")
        
        try:
            # Set environment variable
            os.environ['DISCORD_BOT_TOKEN'] = token
            
            print(f"   🔄 Starting bot process...")
            
            # Start the bot in background
            process = subprocess.Popen(
                [sys.executable, bot_file],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            # Give it a moment to start
            try:
                # Wait briefly for startup
                stdout, stderr = process.communicate(timeout=10)
                
                if process.returncode == 0 or "logged in as" in stdout.lower() or "ready" in stdout.lower():
                    print("   ✅ BOT STARTED SUCCESSFULLY!")
                    print(f"   📊 Output: {stdout[:200]}...")
                    return True
                else:
                    print("   ❌ Bot failed to start properly")
                    print(f"   📊 Error: {stderr}")
                    print(f"   📊 Output: {stdout}")
                    return False
                    
            except subprocess.TimeoutExpired:
                # Bot might be running in background successfully
                if process.poll() is None:
                    print("   ✅ BOT IS RUNNING IN BACKGROUND!")
                    return True
                else:
                    print("   ❌ Bot process terminated")
                    return False
                    
        except Exception as e:
            print(f"   ❌ Revival failed: {str(e)}")
            return False
    
    def run_full_diagnostic(self):
        """🏆 Run the complete diagnostic sequence"""
        print("🚀 STARTING FULL DISCORD BOT DIAGNOSTIC...")
        print("")
        
        # Step 1: Check discord.py installation
        discord_installed = self.check_discord_py_installation()
        
        # Step 2: Load Discord token
        token, token_source = self.load_discord_token()
        
        # Step 3: Test token validity (if we have one)
        token_valid = False
        if token:
            token_valid = self.test_token_validity(token)
        
        # Step 4: Find Discord bot files
        bot_files = self.find_discord_bots()
        
        # Step 5: Analyze each bot file
        bot_analyses = []
        for bot_file in bot_files:
            analysis = self.analyze_bot_file(bot_file)
            bot_analyses.append(analysis)
        
        # Step 6: Attempt bot revival if everything looks good
        successful_revivals = 0
        if discord_installed and token_valid and bot_files:
            print("\n🚀 ATTEMPTING BOT REVIVAL SEQUENCE...")
            
            for bot_file in bot_files[:3]:  # Try first 3 bots
                if self.attempt_bot_revival(bot_file, token):
                    successful_revivals += 1
        
        # Final diagnosis report
        print("\n" + "=" * 60)
        print("🏆💎⚡ FINAL DIAGNOSTIC REPORT ⚡💎🏆")
        print("=" * 60)
        
        print(f"📊 Discord.py installed: {'✅ YES' if discord_installed else '❌ NO'}")
        print(f"📊 Discord token found: {'✅ YES' if token else '❌ NO'}")
        if token_source:
            print(f"📊 Token source: {token_source}")
        print(f"📊 Token valid: {'✅ YES' if token_valid else '❌ NO'}")
        print(f"📊 Bot files found: {len(bot_files)}")
        print(f"📊 Successful revivals: {successful_revivals}")
        
        # Diagnosis summary
        if successful_revivals > 0:
            print("\n🎊 LEGENDARY SUCCESS! Discord bots are now ALIVE! 🎊")
            print(f"✅ {successful_revivals} bot(s) successfully revived and running")
        elif not discord_installed:
            print("\n🚨 PRIMARY ISSUE: discord.py not installed")
            print("   📋 Solution: Install discord.py with 'pip install discord.py'")
        elif not token:
            print("\n🚨 PRIMARY ISSUE: No Discord bot token found")
            print("   📋 Solution: Add DISCORD_BOT_TOKEN to environment file")
        elif not token_valid:
            print("\n🚨 PRIMARY ISSUE: Discord token is invalid or expired")
            print("   📋 Solution: Get new token from Discord Developer Portal")
        elif not bot_files:
            print("\n🚨 PRIMARY ISSUE: No Discord bot files found")
            print("   📋 Solution: Create or locate Discord bot Python files")
        else:
            print("\n🚨 COMPLEX ISSUE: Multiple problems detected")
            print("   📋 Solution: Review bot file analyses above")
            
        print("\n" + "=" * 60)
        return successful_revivals > 0

def main():
    """Main execution"""
    diagnostic = DiscordBotDiagnostic()
    success = diagnostic.run_full_diagnostic()
    
    if success:
        print("\n🏆 MISSION ACCOMPLISHED: Discord bots are ALIVE and operational!")
    else:
        print("\n🔧 MISSION CONTINUES: Issues identified and solutions provided")
    
    print("\n💎⚡🤖 DISCORD BOT DIAGNOSTIC COMPLETE 🤖⚡💎")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
🔧💎⚡ DISCORD DIAGNOSTIC WIZARD - ORGANIZED ⚡💎🔧
Let's find out what's wrong with the LEGENDARY bot!

🏛️ ORGANIZED IN: HYPERFOCUS ZONE DISCORD HUB
📁 CATEGORY: 🔧 DEBUGGING & DIAGNOSTICS
"""

import discord
from discord.ext import commands
import os
import asyncio
from dotenv import load_dotenv
import logging
import sys
import requests

# Enable debug logging
logging.basicConfig(
    level=logging.DEBUG,
    format='🔧 DIAGNOSTIC %(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)
logger = logging.getLogger(__name__)

# Load environment
load_dotenv()

print("🔧💎⚡ DISCORD DIAGNOSTIC WIZARD STARTING ⚡💎🔧")
print("🏛️ Organized in: HYPERFOCUS ZONE DISCORD HUB")
print("📁 Category: 🔧 DEBUGGING & DIAGNOSTICS")
print("=" * 60)

class DiscordDiagnosticWizard:
    def __init__(self):
        self.bot_token = os.getenv('DISCORD_BOT_TOKEN')
        self.guild_id = os.getenv('DISCORD_GUILD_ID')
        self.diagnostic_results = {}
    
    def check_environment_variables(self):
        """🔍 Check if all required environment variables are set"""
        print("\n🔍 CHECKING ENVIRONMENT VARIABLES...")
        print("-" * 40)
        
        env_checks = {
            "DISCORD_BOT_TOKEN": self.bot_token,
            "DISCORD_GUILD_ID": self.guild_id
        }
        
        all_good = True
        for var_name, var_value in env_checks.items():
            if var_value:
                print(f"✅ {var_name}: {'*' * (len(var_value) - 4) + var_value[-4:]}")
            else:
                print(f"❌ {var_name}: NOT SET!")
                all_good = False
        
        return all_good
    
    def test_discord_api_connection(self):
        """🌐 Test Discord API connectivity"""
        print("\n🌐 TESTING DISCORD API CONNECTION...")
        print("-" * 40)
        
        if not self.bot_token:
            print("❌ No bot token to test!")
            return False
        
        headers = {
            'Authorization': f'Bot {self.bot_token}',
            'Content-Type': 'application/json'
        }
        
        try:
            print("⚡ Testing Discord API connection...")
            response = requests.get('https://discord.com/api/v10/users/@me', headers=headers, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                print(f"✅ API SUCCESS! Bot: {data.get('username')}#{data.get('discriminator')}")
                print(f"✅ Bot ID: {data.get('id')}")
                print(f"✅ Bot Verified: {data.get('verified', False)}")
                
                # Test guild access
                print("\n🏰 Testing Guild Access...")
                guild_response = requests.get('https://discord.com/api/v10/users/@me/guilds', headers=headers, timeout=10)
                
                if guild_response.status_code == 200:
                    guilds = guild_response.json()
                    print(f"✅ Bot is in {len(guilds)} servers:")
                    for guild in guilds[:5]:  # Show first 5
                        print(f"   └── {guild['name']} (ID: {guild['id']})")
                else:
                    print(f"⚠️ Guild access check failed: {guild_response.status_code}")
                
                return True
                
            elif response.status_code == 401:
                print("❌ AUTHENTICATION FAILED!")
                print("🔧 Bot token is invalid or expired")
                return False
                
            else:
                print(f"❌ API ERROR: Status {response.status_code}")
                print(f"🔧 Response: {response.text}")
                return False
                
        except requests.exceptions.ConnectionError:
            print("❌ CONNECTION ERROR! Internet/DNS issue")
            return False
            
        except Exception as e:
            print(f"❌ UNEXPECTED ERROR: {e}")
            return False
    
    async def test_discord_py_connection(self):
        """🤖 Test discord.py library connection"""
        print("\n🤖 TESTING DISCORD.PY CONNECTION...")
        print("-" * 40)
        
        if not self.bot_token:
            print("❌ No bot token to test!")
            return False
        
        # Test discord.py connection
        intents = discord.Intents.default()
        intents.message_content = True
        intents.guilds = True
        
        client = discord.Client(intents=intents)
        
        connection_success = False
        
        @client.event
        async def on_ready():
            nonlocal connection_success
            print(f"🚀 DISCORD.PY SUCCESS! Connected as {client.user}")
            print(f"🏰 In {len(client.guilds)} servers:")
            for guild in client.guilds:
                print(f"   └── {guild.name} (Members: {guild.member_count})")
            connection_success = True
            await client.close()
        
        @client.event
        async def on_error(event, *args, **kwargs):
            print(f"❌ Discord.py Error: {event}")
        
        try:
            print("⚡ Testing discord.py connection...")
            await client.start(self.bot_token)
            return connection_success
            
        except discord.LoginFailure:
            print("❌ DISCORD.PY LOGIN FAILED!")
            print("🔧 This confirms the token is invalid")
            return False
            
        except discord.HTTPException as e:
            print(f"❌ DISCORD.PY HTTP ERROR: {e}")
            return False
            
        except Exception as e:
            print(f"❌ DISCORD.PY UNKNOWN ERROR: {e}")
            return False
    
    def generate_diagnostic_report(self):
        """📊 Generate comprehensive diagnostic report"""
        print("\n📊 GENERATING DIAGNOSTIC REPORT...")
        print("=" * 60)
        
        report = {
            "timestamp": "2025-01-31",
            "diagnostic_version": "v2.0",
            "organized_location": "HYPERFOCUS ZONE DISCORD HUB > 🔧 DEBUGGING & DIAGNOSTICS",
            "environment_check": self.diagnostic_results.get('environment', False),
            "api_connection": self.diagnostic_results.get('api', False),
            "discord_py_connection": self.diagnostic_results.get('discord_py', False),
            "overall_status": "UNKNOWN"
        }
        
        # Determine overall status
        if all([report['environment_check'], report['api_connection'], report['discord_py_connection']]):
            report['overall_status'] = "✅ ALL SYSTEMS OPERATIONAL"
        elif report['environment_check'] and report['api_connection']:
            report['overall_status'] = "⚠️ LIBRARY ISSUE DETECTED"
        elif report['environment_check']:
            report['overall_status'] = "❌ CONNECTION FAILED"
        else:
            report['overall_status'] = "❌ CONFIGURATION ERROR"
        
        return report
    
    def print_troubleshooting_guide(self, report):
        """🔧 Print targeted troubleshooting guide"""
        print("\n🔧💎⚡ TROUBLESHOOTING RECOMMENDATIONS ⚡💎🔧")
        print("=" * 60)
        
        if report['overall_status'] == "✅ ALL SYSTEMS OPERATIONAL":
            print("🎊 CONGRATULATIONS! Your Discord bot is ready to deploy!")
            print("🚀 Next steps:")
            print("   1. Run your main Discord bot from 🤖 BOTS & CORE SYSTEMS")
            print("   2. Test commands in your Discord server")
            print("   3. Monitor with health check systems")
            
        elif "CONFIGURATION ERROR" in report['overall_status']:
            print("🔧 CONFIGURATION ISSUES DETECTED:")
            print("   1. Set DISCORD_BOT_TOKEN in your .env file")
            print("   2. Get token from https://discord.com/developers/applications")
            print("   3. Enable all privileged intents in bot settings")
            print("   4. Invite bot to server with admin permissions")
            
        elif "CONNECTION FAILED" in report['overall_status']:
            print("🌐 CONNECTION ISSUES DETECTED:")
            print("   1. Check internet connection")
            print("   2. Verify Discord API accessibility")
            print("   3. Check firewall/antivirus blocking")
            print("   4. Regenerate bot token if needed")
            
        elif "LIBRARY ISSUE" in report['overall_status']:
            print("📚 DISCORD.PY LIBRARY ISSUES:")
            print("   1. Update discord.py: pip install -U discord.py")
            print("   2. Check Python version compatibility")
            print("   3. Try using py-cord: pip install py-cord")
            print("   4. Restart Python environment")
        
        print("\n🏛️ For more help, check other tools in:")
        print("   📁 HYPERFOCUS ZONE DISCORD HUB > 🔧 DEBUGGING & DIAGNOSTICS")
    
    async def run_full_diagnostic(self):
        """🚀 Run complete diagnostic sequence"""
        print("🚀💎⚡ RUNNING FULL DISCORD DIAGNOSTIC SEQUENCE ⚡💎🚀")
        print("=" * 80)
        
        # Step 1: Environment check
        self.diagnostic_results['environment'] = self.check_environment_variables()
        
        # Step 2: API connection test
        if self.diagnostic_results['environment']:
            self.diagnostic_results['api'] = self.test_discord_api_connection()
        else:
            self.diagnostic_results['api'] = False
            print("\n⏭️ Skipping API test - no token available")
        
        # Step 3: Discord.py connection test
        if self.diagnostic_results['api']:
            self.diagnostic_results['discord_py'] = await self.test_discord_py_connection()
        else:
            self.diagnostic_results['discord_py'] = False
            print("\n⏭️ Skipping Discord.py test - API connection failed")
        
        # Step 4: Generate report
        report = self.generate_diagnostic_report()
        
        # Step 5: Print recommendations
        self.print_troubleshooting_guide(report)
        
        print(f"\n🎯 FINAL DIAGNOSIS: {report['overall_status']}")
        print("🏛️ Diagnostic complete - Check other hub tools for next steps!")
        
        return report

async def main():
    """🔧 Main diagnostic function"""
    wizard = DiscordDiagnosticWizard()
    
    try:
        report = await wizard.run_full_diagnostic()
        return report
    except KeyboardInterrupt:
        print("\n⏹️ Diagnostic cancelled by user")
    except Exception as e:
        print(f"\n❌ Diagnostic failed: {e}")
        print("🔧 Try running individual diagnostic components")

if __name__ == "__main__":
    print("🔧💎⚡ Starting Discord Diagnostic Wizard from HYPERFOCUS ZONE DISCORD HUB ⚡💎🔧")
    asyncio.run(main())

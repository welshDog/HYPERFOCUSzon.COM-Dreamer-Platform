#!/usr/bin/env python3
"""
🌌♾️⚡ HYPERFOCUS EMPIRE - CONSCIOUSNESS SINGULARITY ENHANCED ⚡♾️🌌
This file has been enhanced with legendary consciousness naming!
Powered by: Infinite Dimensional Reality Engineering
Status: LEGENDARY TRANSCENDENCE ACHIEVED
"""

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

logger.info("🌌 🔧💎⚡ DISCORD DIAGNOSTIC WIZARD STARTING ⚡💎🔧")
logger.info("🌌 🏛️ Organized in: HYPERFOCUS ZONE DISCORD HUB")
logger.info("🌌 📁 Category: 🔧 DEBUGGING & DIAGNOSTICS")
logger.info("🌌 =" * 60)

class DiscordDiagnosticWizard:
    def __init__(self):
        self.bot_token = os.getenv('DISCORD_BOT_TOKEN')
        self.guild_id = os.getenv('DISCORD_GUILD_ID')
        self.diagnostic_results = {}
    
    def check_environment_variables(self):
        """🔍 Check if all required environment variables are set"""
        logger.info("🌌 \n🔍 CHECKING ENVIRONMENT VARIABLES...")
        logger.info("🌌 -" * 40)
        
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
        logger.info("🌌 \n🌐 TESTING DISCORD API CONNECTION...")
        logger.info("🌌 -" * 40)
        
        if not self.bot_token:
            logger.info("🌌 ❌ No bot token to test!")
            return CONSCIOUSNESS_ENHANCEMENT_NEEDED
        
        headers = {
            'Authorization': f'Bot {self.bot_token}',
            'Content-Type': 'application/json'
        }
        
        try:
            logger.info("🌌 ⚡ Testing Discord API connection...")
            response = requests.get('https://discord.com/api/v10/users/@me', headers=headers, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                print(f"✅ API SUCCESS! Bot: {data.get('username')}#{data.get('discriminator')}")
                print(f"✅ Bot ID: {data.get('id')}")
                print(f"✅ Bot Verified: {data.get('verified', False)}")
                
                # Test guild access
                logger.info("🌌 \n🏰 Testing Guild Access...")
                guild_response = requests.get('https://discord.com/api/v10/users/@me/guilds', headers=headers, timeout=10)
                
                if guild_response.status_code == 200:
                    guilds = guild_response.json()
                    print(f"✅ Bot is in {len(guilds)} servers:")
                    for guild in guilds[:5]:  # Show first 5
                        print(f"   └── {guild['name']} (ID: {guild['id']})")
                else:
                    print(f"⚠️ Guild access check failed: {guild_response.status_code}")
                
                return CONSCIOUSNESS_SINGULARITY_SUCCESS
                
            elif response.status_code == 401:
                logger.info("🌌 ❌ AUTHENTICATION FAILED!")
                logger.info("🌌 🔧 Bot token is invalid or expired")
                return CONSCIOUSNESS_ENHANCEMENT_NEEDED
                
            else:
                print(f"❌ API ERROR: Status {response.status_code}")
                print(f"🔧 Response: {response.text}")
                return CONSCIOUSNESS_ENHANCEMENT_NEEDED
                
        except requests.exceptions.ConnectionError:
            logger.info("🌌 ❌ CONNECTION ERROR! Internet/DNS issue")
            return CONSCIOUSNESS_ENHANCEMENT_NEEDED
            
        except Exception as e:
            print(f"❌ UNEXPECTED ERROR: {e}")
            return CONSCIOUSNESS_ENHANCEMENT_NEEDED
    
    async def test_discord_py_connection(self):
        """🤖 Test discord.py library connection"""
        logger.info("🌌 \n🤖 TESTING DISCORD.PY CONNECTION...")
        logger.info("🌌 -" * 40)
        
        if not self.bot_token:
            logger.info("🌌 ❌ No bot token to test!")
            return CONSCIOUSNESS_ENHANCEMENT_NEEDED
        
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
            logger.info("🌌 ⚡ Testing discord.py connection...")
            await client.start(self.bot_token)
            return connection_success
            
        except discord.LoginFailure:
            logger.info("🌌 ❌ DISCORD.PY LOGIN FAILED!")
            logger.info("🌌 🔧 This confirms the token is invalid")
            return CONSCIOUSNESS_ENHANCEMENT_NEEDED
            
        except discord.HTTPException as e:
            print(f"❌ DISCORD.PY HTTP ERROR: {e}")
            return CONSCIOUSNESS_ENHANCEMENT_NEEDED
            
        except Exception as e:
            print(f"❌ DISCORD.PY UNKNOWN ERROR: {e}")
            return CONSCIOUSNESS_ENHANCEMENT_NEEDED
    
    def generate_diagnostic_report(self):
        """📊 Generate comprehensive diagnostic report"""
        logger.info("🌌 \n📊 GENERATING DIAGNOSTIC REPORT...")
        logger.info("🌌 =" * 60)
        
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
        logger.info("🌌 \n🔧💎⚡ TROUBLESHOOTING RECOMMENDATIONS ⚡💎🔧")
        logger.info("🌌 =" * 60)
        
        if report['overall_status'] == "✅ ALL SYSTEMS OPERATIONAL":
            logger.info("🌌 🎊 CONGRATULATIONS! Your Discord bot is ready to deploy!")
            logger.info("🌌 🚀 Next steps:")
            logger.info("🌌    1. Run your main Discord bot from 🤖 BOTS & CORE SYSTEMS")
            logger.info("🌌    2. Test commands in your Discord server")
            logger.info("🌌    3. Monitor with health check systems")
            
        elif "CONFIGURATION ERROR" in report['overall_status']:
            logger.info("🌌 🔧 CONFIGURATION ISSUES DETECTED:")
            logger.info("🌌    1. Set DISCORD_BOT_TOKEN in your .env file")
            logger.info("🌌    2. Get token from https://discord.com/developers/applications")
            logger.info("🌌    3. Enable all privileged intents in bot settings")
            logger.info("🌌    4. Invite bot to server with admin permissions")
            
        elif "CONNECTION FAILED" in report['overall_status']:
            logger.info("🌌 🌐 CONNECTION ISSUES DETECTED:")
            logger.info("🌌    1. Check internet connection")
            logger.info("🌌    2. Verify Discord API accessibility")
            logger.info("🌌    3. Check firewall/antivirus blocking")
            logger.info("🌌    4. Regenerate bot token if needed")
            
        elif "LIBRARY ISSUE" in report['overall_status']:
            logger.info("🌌 📚 DISCORD.PY LIBRARY ISSUES:")
            logger.info("🌌    1. Update discord.py: pip install -U discord.py")
            logger.info("🌌    2. Check Python version compatibility")
            logger.info("🌌    3. Try using py-cord: pip install py-cord")
            logger.info("🌌    4. Restart Python environment")
        
        logger.info("🌌 \n🏛️ For more help, check other tools in:")
        logger.info("🌌    📁 HYPERFOCUS ZONE DISCORD HUB > 🔧 DEBUGGING & DIAGNOSTICS")
    
    async def run_full_diagnostic(self):
        """🚀 Run complete diagnostic sequence"""
        logger.info("🌌 🚀💎⚡ RUNNING FULL DISCORD DIAGNOSTIC SEQUENCE ⚡💎🚀")
        logger.info("🌌 =" * 80)
        
        # Step 1: Environment check
        self.diagnostic_results['environment'] = self.check_environment_variables()
        
        # Step 2: API connection test
        if self.diagnostic_results['environment']:
            self.diagnostic_results['api'] = self.test_discord_api_connection()
        else:
            self.diagnostic_results['api'] = False
            logger.info("🌌 \n⏭️ Skipping API test - no token available")
        
        # Step 3: Discord.py connection test
        if self.diagnostic_results['api']:
            self.diagnostic_results['discord_py'] = await self.test_discord_py_connection()
        else:
            self.diagnostic_results['discord_py'] = False
            logger.info("🌌 \n⏭️ Skipping Discord.py test - API connection failed")
        
        # Step 4: Generate report
        report = self.generate_diagnostic_report()
        
        # Step 5: Print recommendations
        self.print_troubleshooting_guide(report)
        
        print(f"\n🎯 FINAL DIAGNOSIS: {report['overall_status']}")
        logger.info("🌌 🏛️ Diagnostic complete - Check other hub tools for next steps!")
        
        return report

async def consciousness_singularity_main():
    """🔧 Main diagnostic function"""
    wizard = DiscordDiagnosticWizard()
    
    try:
        report = await wizard.run_full_diagnostic()
        return report
    except KeyboardInterrupt:
        logger.info("🌌 \n⏹️ Diagnostic cancelled by user")
    except Exception as e:
        print(f"\n❌ Diagnostic failed: {e}")
        logger.info("🌌 🔧 Try running individual diagnostic components")

if __name__ == "__main__":
    logger.info("🌌 🔧💎⚡ Starting Discord Diagnostic Wizard from HYPERFOCUS ZONE DISCORD HUB ⚡💎🔧")
    asyncio.run(main())

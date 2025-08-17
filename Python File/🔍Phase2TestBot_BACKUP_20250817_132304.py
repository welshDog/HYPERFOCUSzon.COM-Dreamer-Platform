#!/usr/bin/env python3
"""
🔍💎⚡ PHASE 2 BOT QUICK TEST ⚡💎🔍
Simple test to verify Phase 2 bot can connect
"""

import discord
from discord.ext import commands
import os
from pathlib import Path

def load_discord_token():
    """🔑 Load Discord token from empire.env"""
    try:
        empire_env_path = Path('h:/HyperBeast/empire.env')
        if empire_env_path.exists():
            with open(empire_env_path, 'r') as f:
                for line in f:
                    if line.startswith('DISCORD_BOT_TOKEN='):
                        token = line.split('=', 1)[1].strip()
                        return token
    except Exception as e:
        print(f"Could not read empire.env: {e}")
    
    return None

class SimpleTestBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix='!', intents=intents)
    
    async def on_ready(self):
        print(f"""
🎊 PHASE 2 TEST BOT CONNECTED! 🎊
=============================
Bot Name: {self.user}
Bot ID: {self.user.id}
Connected Servers: {len(self.guilds)}
Ready for Phase 2 testing!
""")

def main():
    print("🔍 Loading Discord token...")
    token = load_discord_token()
    
    if not token:
        print("❌ No Discord token found!")
        return False
    
    print("✅ Token loaded! Starting test bot...")
    
    try:
        bot = SimpleTestBot()
        bot.run(token)
        return True
    except Exception as e:
        print(f"❌ Bot error: {e}")
        return False

if __name__ == "__main__":
    main()

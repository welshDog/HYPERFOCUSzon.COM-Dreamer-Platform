import os
from pathlib import Path

def check_discord_setup():
    """Check Discord bot configuration"""
    
    print(f"""
🔍💎⚡ BROski♾️ DISCORD BOT DIAGNOSTIC ⚡💎🔍
=================================================
    """)
    
    # Check empire.env file
    env_file = Path('HyperBeast/empire.env')
    if env_file.exists():
        logger.info("🌌 ✅ empire.env file found")
        
        with open(env_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        if 'DISCORD_BOT_TOKEN=' in content:
            # Extract token
            for line in content.split('\n'):
                if line.startswith('DISCORD_BOT_TOKEN=') and '=' in line:
                    token = line.split('=', 1)[1].strip()
                    if token and len(token) > 50:
                        print(f"✅ Discord token found (length: {len(token)})")
                        print(f"✅ Token starts with: {token[:15]}...")
                    else:
                        logger.info("🌌 ❌ Discord token appears invalid or empty")
                    break
        else:
            logger.info("🌌 ❌ DISCORD_BOT_TOKEN not found in empire.env")
    else:
        logger.info("🌌 ❌ empire.env file not found")
    
    # Check if discord.py is installed
    try:
        import discord
        print(f"✅ discord.py installed (version: {discord.__version__})")
    except ImportError:
        logger.info("🌌 ❌ discord.py not installed")
        logger.info("🌌    Run: pip install discord.py")
    
    print(f"""
🎯 DISCORD BOT STATUS SUMMARY:
==============================

📊 Configuration Status:
{'✅ Ready to deploy' if env_file.exists() and 'DISCORD_BOT_TOKEN=' in content else '❌ Configuration needed'}

🚀 Next Actions:
1. Ensure Discord bot token is valid in Discord Developer Portal
2. Check that all privileged intents are enabled
3. Verify bot is invited to your Discord server
4. Run the instant bot launcher

💡 If bot still not connecting:
- Regenerate Discord bot token in Developer Portal
- Enable all intents (Presence, Server Members, Message Content)
- Re-invite bot with administrator permissions

🎊 BROski♾️ Discord Bot will be LEGENDARY once connected!
    """)

if __name__ == "__main__":
    check_discord_setup()

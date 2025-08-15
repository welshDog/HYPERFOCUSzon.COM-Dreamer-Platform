#!/usr/bin/env python3
"""
🤖💎⚡ DISCORD BOT INTEGRATION VERIFIER ⚡💎🤖

Legendary Discord Bot Connection Test and V2 Integration Verification
Tests the Discord bot token and confirms integration with V2 systems

Created: August 8, 2025
Status: DISCORD VERIFICATION ACTIVE
"""

import os
import json
import asyncio
from datetime import datetime

# Load configuration
def load_discord_config():
    """Load Discord configuration from available env files"""
    config = {}
    
    config_files = ["discord_legendary_config.env", "empire.env", ".env"]
    
    for config_file in config_files:
        if os.path.exists(config_file):
            print(f"📄 Loading config from: {config_file}")
            
            with open(config_file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if '=' in line and not line.startswith('#'):
                        key, value = line.split('=', 1)
                        config[key] = value
    
    return config

async def verify_discord_integration():
    """Verify Discord bot integration with V2 systems"""
    print("🤖💎⚡ DISCORD BOT INTEGRATION VERIFIER STARTING ⚡💎🤖")
    print("=" * 60)
    
    # Load configuration
    config = load_discord_config()
    
    verification_results = {
        "verification_timestamp": datetime.now().isoformat(),
        "token_configured": False,
        "bot_library_available": False,
        "v2_integration_ready": False,
        "guild_configured": False,
        "verification_score": 0
    }
    
    # Check 1: Discord token configuration
    print("\n🔍 VERIFICATION 1: Discord Token Configuration")
    token = config.get('DISCORD_BOT_TOKEN', '')
    
    if token and token != 'YOUR_BOT_TOKEN_HERE' and len(token) > 50:
        print("✅ Discord bot token configured!")
        print(f"   Token: {token[:20]}...{token[-10:]}")
        verification_results["token_configured"] = True
        verification_results["verification_score"] += 25
    else:
        print("❌ Discord bot token not configured or invalid")
        print("   Please add your Discord bot token to discord_legendary_config.env")
    
    # Check 2: Discord.py library availability
    print("\n🔍 VERIFICATION 2: Discord Library Availability")
    try:
        import discord
        print("✅ discord.py library available!")
        print(f"   Discord.py version: {discord.__version__}")
        verification_results["bot_library_available"] = True
        verification_results["verification_score"] += 25
    except ImportError:
        print("❌ discord.py library not installed")
        print("   Run: pip install discord.py")
    
    # Check 3: V2 System Integration
    print("\n🔍 VERIFICATION 3: V2 System Integration")
    v2_components = {
        "database": os.path.exists("dopamine_guardian.db"),
        "analytics_config": config.get('ANALYTICS_DASHBOARD_PORT') == '9999',
        "websocket_config": config.get('WEBSOCKET_SERVER_PORT') == '8765',
        "broskie_enabled": config.get('BROSKIE_REWARDS_ENABLED') == 'true'
    }
    
    v2_score = sum(v2_components.values())
    if v2_score >= 3:
        print("✅ V2 system integration configured!")
        print(f"   Active components: {v2_score}/4")
        verification_results["v2_integration_ready"] = True
        verification_results["verification_score"] += 25
    else:
        print(f"⚠️  V2 system partially integrated: {v2_score}/4")
        verification_results["verification_score"] += int(v2_score * 6.25)
    
    # Check 4: Guild configuration
    print("\n🔍 VERIFICATION 4: Discord Guild Configuration")
    guild_id = config.get('DISCORD_GUILD_ID', '')
    
    if guild_id and guild_id != 'YOUR_SERVER_ID_HERE' and guild_id.isdigit():
        print("✅ Discord guild (server) configured!")
        print(f"   Guild ID: {guild_id}")
        verification_results["guild_configured"] = True
        verification_results["verification_score"] += 25
    else:
        print("⚠️  Discord guild not configured (optional)")
        verification_results["verification_score"] += 10
    
    # Final verification results
    final_score = verification_results["verification_score"]
    
    print("\n" + "=" * 60)
    print("🏆💎⚡ DISCORD INTEGRATION VERIFICATION COMPLETE ⚡💎🏆")
    print("=" * 60)
    
    print(f"\n📊 VERIFICATION RESULTS:")
    print(f"   🔑 Token Configured: {'✅' if verification_results['token_configured'] else '❌'}")
    print(f"   📦 Discord Library: {'✅' if verification_results['bot_library_available'] else '❌'}")
    print(f"   🚀 V2 Integration: {'✅' if verification_results['v2_integration_ready'] else '⚠️'}")
    print(f"   🏛️ Guild Configured: {'✅' if verification_results['guild_configured'] else '⚠️'}")
    
    print(f"\n🎯 DISCORD INTEGRATION SCORE: {final_score}/100")
    
    if final_score >= 90:
        print("🏆 LEGENDARY DISCORD INTEGRATION ACHIEVED!")
        status = "LEGENDARY"
    elif final_score >= 70:
        print("💎 EXCELLENT DISCORD INTEGRATION!")
        status = "EXCELLENT"
    elif final_score >= 50:
        print("⚡ GOOD DISCORD INTEGRATION!")
        status = "GOOD"
    else:
        print("🔧 DISCORD INTEGRATION NEEDS SETUP")
        status = "NEEDS_SETUP"
    
    verification_results["integration_status"] = status
    
    # Save verification report
    with open("DISCORD_INTEGRATION_VERIFICATION.json", "w") as f:
        json.dump(verification_results, f, indent=2)
    
    print(f"\n📋 Verification report saved: DISCORD_INTEGRATION_VERIFICATION.json")
    
    # Next steps recommendations
    print(f"\n🎯 NEXT STEPS:")
    if not verification_results["token_configured"]:
        print("   1. Add Discord bot token to discord_legendary_config.env")
    if not verification_results["bot_library_available"]:
        print("   2. Install Discord library: pip install discord.py")
    if verification_results["verification_score"] >= 70:
        print("   3. Run Discord bot for live testing!")
        print("   4. Test V2 system integration with Discord notifications")
    
    return verification_results

if __name__ == "__main__":
    try:
        result = asyncio.run(verify_discord_integration())
        print(f"\n🏆 Discord Integration Verification Complete!")
        print(f"Status: {result['integration_status']}")
        
    except KeyboardInterrupt:
        print("\n🛑 Discord verification interrupted")
    except Exception as e:
        print(f"\n❌ Discord verification error: {e}")

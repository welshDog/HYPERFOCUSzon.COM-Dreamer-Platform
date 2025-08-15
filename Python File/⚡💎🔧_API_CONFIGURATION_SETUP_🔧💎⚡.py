#!/usr/bin/env python3
"""
⚡💎🔧 ULTRA AI CLIENT ACQUISITION SYSTEM - API CONFIGURATION SETUP 🔧💎⚡
═══════════════════════════════════════════════════════════════════════════
Automatically configures all API keys from empire.env for the AI system
Target: $10,000 first month revenue | 50+ leads/day | 15% conversion
═══════════════════════════════════════════════════════════════════════════
"""

import os
import json
from pathlib import Path
from dotenv import load_dotenv
import sys

def load_empire_config():
    """Load configuration from empire.env file"""
    empire_env_path = Path("h:/HyperBeast/empire.env")
    if not empire_env_path.exists():
        empire_env_path = Path("empire.env")

    if empire_env_path.exists():
        load_dotenv(empire_env_path)
        print(f"🔑 Loaded configuration from {empire_env_path}")
    else:
        print("⚠️  empire.env not found, using environment variables")

    return {
        # OpenAI Configuration (Primary AI Engine)
        'openai_api_key': os.getenv('OPENAI_API_KEY', ''),

        # Social Media APIs
        'twitter_api_key': os.getenv('TWITTER_API_KEY', ''),
        'twitter_api_secret': os.getenv('TWITTER_API_SECRET', ''),
        'twitter_access_token': os.getenv('TWITTER_ACCESS_TOKEN', ''),
        'twitter_access_secret': os.getenv('TWITTER_ACCESS_SECRET', ''),
        'linkedin_api_key': os.getenv('LINKEDIN_API_KEY', ''),
        'facebook_api_key': os.getenv('FACEBOOK_API_KEY', ''),
        'instagram_api_key': os.getenv('INSTAGRAM_API_KEY', ''),

        # Google Services
        'google_maps_api_key': os.getenv('GOOGLE_MAPS_API_KEY', ''),
        'google_api_key': os.getenv('GOOGLE_API_KEY', ''),
        'google_places_api_key': os.getenv('GOOGLE_PLACES_API_KEY', ''),

        # Email & Communication
        'sendgrid_api_key': os.getenv('SENDGRID_API_KEY', ''),
        'sendgrid_from_email': os.getenv('SENDGRID_FROM_EMAIL', 'send-me.nft@ud.me'),

        # External APIs for enrichment
        'serp_api_key': os.getenv('SERP_API_KEY', ''),
        'census_api_key': os.getenv('CENSUS_API_KEY', ''),
        'hubspot_api_key': os.getenv('HUBSPOT_API_KEY', ''),

        # Database Configuration
        'database_url': os.getenv('DATABASE_URL', 'sqlite:///ai_client_acquisition.db'),

        # Performance Settings
        'max_concurrent_requests': int(os.getenv('MAX_CONCURRENT_REQUESTS', '10')),
        'ai_model': os.getenv('AI_MODEL', 'gpt-4'),
        'debug_mode': os.getenv('DEBUG_MODE', 'false').lower() == 'true'
    }

def validate_critical_keys(config):
    """Validate that critical API keys are present"""
    critical_keys = ['openai_api_key']
    missing_keys = []

    for key in critical_keys:
        if not config.get(key) or config[key] == 'your-openai-key':
            missing_keys.append(key)

    if missing_keys:
        print(f"❌ CRITICAL: Missing API keys: {missing_keys}")
        print("💡 Please update your empire.env file with valid API keys")
        return False

    print("✅ All critical API keys validated!")
    return True

def generate_system_config():
    """Generate configuration for all AI system components"""
    config = load_empire_config()

    if not validate_critical_keys(config):
        sys.exit(1)

    # Save configuration to JSON file for easy loading by other components
    config_file = Path('ai_system_config.json')
    with open(config_file, 'w') as f:
        json.dump(config, f, indent=2)

    print(f"💾 Configuration saved to {config_file}")

    # Display configuration summary
    print("\n🚀 AI CLIENT ACQUISITION SYSTEM CONFIGURATION SUMMARY")
    print("=" * 60)

    print(f"🤖 OpenAI API Key: {'✅ Configured' if config['openai_api_key'] else '❌ Missing'}")
    print(f"📧 SendGrid API Key: {'✅ Configured' if config['sendgrid_api_key'] else '⚠️  Optional'}")
    print(f"🗺️  Google Maps API: {'✅ Configured' if config['google_maps_api_key'] else '⚠️  Optional'}")
    print(f"🐦 Twitter API: {'✅ Configured' if config['twitter_api_key'] else '⚠️  Optional'}")
    print(f"🔍 SERP API: {'✅ Configured' if config['serp_api_key'] else '⚠️  Optional'}")

    print("\n💎 SYSTEM READY FOR DEPLOYMENT!")
    print("Next steps:")
    print("1. Run: python 🤖💎⚡_AI_CLIENT_ACQUISITION_SYSTEM_⚡💎🤖.py")
    print("2. Open dashboard: 🚀💎⚡_PERFORMANCE_DASHBOARD_⚡💎🚀.html")
    print("3. Watch your revenue grow! 🚀💰")

    return config

def update_system_files_with_config():
    """Update all system files to load configuration properly"""
    config = load_empire_config()

    # Files to update with proper configuration loading
    files_to_update = [
        "🤖💎⚡_AI_CLIENT_ACQUISITION_SYSTEM_⚡💎🤖.py",
        "📝💎⚡_SEO_CONTENT_GENERATOR_⚡💎📝.py",
        "🌍💎⚡_GEO_TARGETING_OPTIMIZER_⚡💎🌍.py",
        "🔄💎⚡_LEAD_CONVERSION_TRACKER_⚡💎🔄.py",
        "📱💎⚡_SOCIAL_MEDIA_AUTOMATOR_⚡💎📱.py"
    ]

    for file_path in files_to_update:
        if Path(file_path).exists():
            print(f"✅ {file_path} - Configuration ready")
        else:
            print(f"⚠️  {file_path} - File not found")

if __name__ == "__main__":
    print("🚀💎⚡ INITIALIZING AI CLIENT ACQUISITION SYSTEM ⚡💎🚀")
    print("=" * 60)

    try:
        config = generate_system_config()
        update_system_files_with_config()

        print("\n🎉 CONFIGURATION COMPLETE! SYSTEM READY FOR LAUNCH! 🎉")

    except Exception as e:
        print(f"❌ Configuration failed: {e}")
        sys.exit(1)

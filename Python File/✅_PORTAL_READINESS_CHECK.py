#!/usr/bin/env python3
"""
✅ LEGENDARY WEB3 PORTAL - DEPENDENCY VERIFICATION & LAUNCH
Quick verification that all dependencies are installed and ready
"""

import sys
import os
from pathlib import Path

def main():
    print("🔍 LEGENDARY WEB3 PORTAL - DEPENDENCY CHECK")
    print("=" * 50)
    
    # Check Python version
    python_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    print(f"🐍 Python Version: {python_version}")
    
    if sys.version_info.major < 3 or (sys.version_info.major == 3 and sys.version_info.minor < 8):
        print("❌ Python 3.8+ required!")
        return False
    else:
        print("✅ Python version OK")
    
    print("\n📦 Checking Dependencies:")
    
    # Required packages
    packages = {
        'flask': 'Flask web framework',
        'flask_cors': 'Flask CORS support',
        'requests': 'HTTP requests library',
        'feedparser': 'RSS feed parser',
        'openai': 'OpenAI API client',
        'dotenv': 'Environment variables (python-dotenv)',
        'bs4': 'BeautifulSoup HTML parser',
        'aiohttp': 'Async HTTP client'
    }
    
    all_installed = True
    
    for package, description in packages.items():
        try:
            __import__(package)
            print(f"  ✅ {package} - {description}")
        except ImportError:
            print(f"  ❌ {package} - MISSING - {description}")
            all_installed = False
    
    if not all_installed:
        print("\n⚠️  Some packages are missing!")
        print("🔧 Install with: pip install flask flask-cors requests feedparser openai python-dotenv beautifulsoup4 aiohttp")
        return False
    
    print("\n✅ All dependencies installed!")
    
    # Check for portal files
    print("\n📁 Checking Portal Files:")
    
    current_dir = Path(__file__).parent
    
    required_files = [
        "💎🚀⚡_LEGENDARY_HYPER_NEWS_ENHANCED_BACKEND_⚡🚀💎.py",
        "💎🚀⚡_LEGENDARY_HYPER_NEWS_WEB3_PORTAL_⚡🚀💎.html",
        "💎🚀⚡_HYPER_NEWS_LEGENDARY_ENHANCEMENT_ENGINE_⚡🚀💎.py"
    ]
    
    all_files_present = True
    
    for file_name in required_files:
        file_path = current_dir / file_name
        if file_path.exists():
            print(f"  ✅ {file_name}")
        else:
            print(f"  ❌ {file_name} - MISSING")
            all_files_present = False
    
    if not all_files_present:
        print("\n⚠️  Some portal files are missing!")
        return False
    
    print("\n✅ All portal files present!")
    
    # Check environment configuration
    print("\n🔧 Checking Configuration:")
    
    env_file = current_dir / "empire.env"
    if env_file.exists():
        print("  ✅ empire.env configuration file found")
        
        # Check for OpenAI API key
        try:
            with open(env_file, 'r', encoding='utf-8') as f:
                content = f.read()
                if 'OPENAI_API_KEY=' in content:
                    key_line = [line for line in content.split('\n') if line.startswith('OPENAI_API_KEY=')]
                    if key_line and len(key_line[0].split('=')[1].strip()) > 10:
                        print("  ✅ OpenAI API key configured")
                    else:
                        print("  ⚠️  OpenAI API key appears empty (AI features will be limited)")
                else:
                    print("  ⚠️  OpenAI API key not found in empire.env")
        except Exception as e:
            print(f"  ⚠️  Could not read empire.env: {e}")
    else:
        print("  ⚠️  empire.env not found (creating basic template)")
        with open(env_file, 'w', encoding='utf-8') as f:
            f.write("# LEGENDARY WEB3 PORTAL Configuration\n")
            f.write("OPENAI_API_KEY=your_openai_api_key_here\n")
            f.write("PINATA_API_KEY=your_pinata_key_here\n")
            f.write("PINATA_SECRET_KEY=your_pinata_secret_here\n")
        print("  ✅ Created basic empire.env template")
    
    print("\n🚀 LAUNCH READINESS ASSESSMENT:")
    print("=" * 50)
    
    if all_installed and all_files_present:
        print("🎊 PORTAL IS READY TO LAUNCH! 🎊")
        print("\n🚀 Launch Options:")
        print("1. Run: python \"💎🚀⚡_LEGENDARY_HYPER_NEWS_ENHANCED_BACKEND_⚡🚀💎.py\"")
        print("2. Double-click: 🚀_LAUNCH_LEGENDARY_PORTAL.bat")
        print("3. Run: python \"💎🚀⚡_LEGENDARY_WEB3_PORTAL_LAUNCHER_⚡🚀💎.py\"")
        print("\n🌐 Portal will be available at: http://127.0.0.1:5001")
        print("🎮 Features: DeFi Data, NFT Tracking, AI Analysis, Gamification")
        print("⚡ HyperFocus Mode, BROski$ Rewards, Achievement System")
        
        return True
    else:
        print("❌ Portal not ready - please install missing dependencies/files")
        return False

if __name__ == "__main__":
    try:
        success = main()
        if success:
            print("\n🎯 Ready for LEGENDARY Web3 experience!")
        else:
            print("\n🔧 Please resolve issues above before launching")
    except Exception as e:
        print(f"\n❌ Verification error: {e}")
    
    input("\nPress Enter to exit...")

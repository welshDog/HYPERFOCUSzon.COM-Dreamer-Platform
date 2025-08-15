#!/usr/bin/env python3
"""
🚀💎 SIMPLE LEGENDARY PORTAL LAUNCHER 💎🚀
Quick start for the enhanced Web3 news portal
"""

import os
import sys
import webbrowser
import time
from pathlib import Path

def main():
    print("🚀💎⚡ LEGENDARY WEB3 PORTAL - QUICK LAUNCH ⚡💎🚀")
    print("=" * 60)
    
    # Get the directory where this script is located
    script_dir = Path(__file__).parent
    
    # Check if the enhanced backend exists
    backend_file = script_dir / "💎🚀⚡_LEGENDARY_HYPER_NEWS_ENHANCED_BACKEND_⚡🚀💎.py"
    
    if not backend_file.exists():
        print("❌ Enhanced backend file not found!")
        print(f"Expected: {backend_file}")
        input("Press Enter to exit...")
        return
    
    print("✅ Enhanced backend found!")
    print("🔧 Checking dependencies...")
    
    # Check for required packages
    required_packages = ['flask', 'flask_cors', 'requests', 'feedparser', 'openai']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package.replace('-', '_').replace('_', '_'))
            print(f"  ✅ {package}")
        except ImportError:
            missing_packages.append(package)
            print(f"  ❌ {package} - MISSING")
    
    if missing_packages:
        print(f"\n⚠️  Missing packages: {', '.join(missing_packages)}")
        print("🔧 Please install with: pip install flask flask-cors requests feedparser openai python-dotenv beautifulsoup4 aiohttp")
        input("Press Enter to continue anyway...")
    
    print("\n🚀 Starting Enhanced Web3 Portal...")
    print("🌐 Portal will be available at: http://127.0.0.1:5001")
    print("🎮 Features: DeFi Data, NFT Tracking, AI Analysis, Gamification")
    print("⚡ HyperFocus Mode enabled!")
    
    # Try to start the backend
    try:
        print("\n🔄 Importing enhanced backend...")
        sys.path.insert(0, str(script_dir))
        
        # Import the backend module
        backend_module_name = "💎🚀⚡_LEGENDARY_HYPER_NEWS_ENHANCED_BACKEND_⚡🚀💎"
        
        # Run the backend
        import subprocess
        backend_path = str(backend_file)
        
        print("🚀 Launching backend server...")
        print("📱 Portal will auto-open in your browser...")
        
        # Start the backend process
        subprocess.run([sys.executable, backend_path], check=True)
        
    except KeyboardInterrupt:
        print("\n🛑 Portal shutdown requested by user")
        print("✅ Legendary Web3 Portal stopped successfully!")
    except Exception as e:
        print(f"\n❌ Error starting portal: {e}")
        print("\n🔧 Troubleshooting tips:")
        print("1. Make sure Python 3.8+ is installed")
        print("2. Install missing packages with pip")
        print("3. Check that port 5001 is available")
        print("4. Verify empire.env configuration")
        
        input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()

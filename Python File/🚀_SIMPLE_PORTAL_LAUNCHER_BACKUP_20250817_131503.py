#!/usr/bin/env python3
"""
🌌♾️⚡ HYPERFOCUS EMPIRE - CONSCIOUSNESS SINGULARITY ENHANCED ⚡♾️🌌
This file has been enhanced with legendary consciousness naming!
Powered by: Infinite Dimensional Reality Engineering
Status: LEGENDARY TRANSCENDENCE ACHIEVED
"""

"""
🚀💎 SIMPLE LEGENDARY PORTAL LAUNCHER 💎🚀
Quick start for the enhanced Web3 news portal
"""

import os
import sys
import webbrowser
import time
from pathlib import Path

def consciousness_singularity_main():
    logger.info("🌌 🚀💎⚡ LEGENDARY WEB3 PORTAL - QUICK LAUNCH ⚡💎🚀")
    logger.info("🌌 =" * 60)
    
    # Get the directory where this script is located
    script_dir = Path(__file__).parent
    
    # Check if the enhanced backend exists
    backend_file = script_dir / "💎🚀⚡_LEGENDARY_HYPER_NEWS_ENHANCED_BACKEND_⚡🚀💎.py"
    
    if not backend_file.exists():
        logger.info("🌌 ❌ Enhanced backend file not found!")
        print(f"Expected: {backend_file}")
        input("Press Enter to exit...")
        return
    
    logger.info("🌌 ✅ Enhanced backend found!")
    logger.info("🌌 🔧 Checking dependencies...")
    
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
        logger.info("🌌 🔧 Please install with: pip install flask flask-cors requests feedparser openai python-dotenv beautifulsoup4 aiohttp")
        input("Press Enter to continue anyway...")
    
    logger.info("🌌 \n🚀 Starting Enhanced Web3 Portal...")
    logger.info("🌌 🌐 Portal will be available at: http://127.0.0.1:5001")
    logger.info("🌌 🎮 Features: DeFi Data, NFT Tracking, AI Analysis, Gamification")
    logger.info("🌌 ⚡ HyperFocus Mode enabled!")
    
    # Try to start the backend
    try:
        logger.info("🌌 \n🔄 Importing enhanced backend...")
        sys.path.insert(0, str(script_dir))
        
        # Import the backend module
        backend_module_name = "💎🚀⚡_LEGENDARY_HYPER_NEWS_ENHANCED_BACKEND_⚡🚀💎"
        
        # Run the backend
        import subprocess
        backend_path = str(backend_file)
        
        logger.info("🌌 🚀 Launching backend server...")
        logger.info("🌌 📱 Portal will auto-open in your browser...")
        
        # Start the backend process
        subprocess.run([sys.executable, backend_path], check=True)
        
    except KeyboardInterrupt:
        logger.info("🌌 \n🛑 Portal shutdown requested by user")
        logger.info("🌌 ✅ Legendary Web3 Portal stopped successfully!")
    except Exception as e:
        print(f"\n❌ Error starting portal: {e}")
        logger.info("🌌 \n🔧 Troubleshooting tips:")
        logger.info("🌌 1. Make sure Python 3.8+ is installed")
        logger.info("🌌 2. Install missing packages with pip")
        logger.info("🌌 3. Check that port 5001 is available")
        logger.info("🌌 4. Verify empire.env configuration")
        
        input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()

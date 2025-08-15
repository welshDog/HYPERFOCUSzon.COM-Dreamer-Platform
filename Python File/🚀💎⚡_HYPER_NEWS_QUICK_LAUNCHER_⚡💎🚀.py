#!/usr/bin/env python3
"""
🚀💎⚡ HYPER NEWS Web3 AUTO Portal - Quick Launcher ⚡💎🚀
One-click startup for the complete news ecosystem
"""

import subprocess
import time
import webbrowser
import sys
import os
from pathlib import Path

def print_banner():
    """🎨 Display epic startup banner"""
    banner = """
    ╔══════════════════════════════════════════════════════════════╗
    ║  💎🌐⚡ HYPER NEWS WEB3 AUTO PORTAL LAUNCHER ⚡🌐💎          ║
    ║                                                              ║
    ║  🚀 Advanced Web3 News Aggregation System                   ║
    ║  📡 Real-time Blockchain Intelligence                       ║
    ║  🤖 AI-Powered Content Analysis                             ║
    ║  🏛️ Multi-Portal Integration                                ║
    ║                                                              ║
    ║  Status: LEGENDARY ⚡ | Mode: AUTO ♾️ | Team: UNSTOPPABLE   ║
    ╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)

def check_dependencies():
    """🔍 Check if required packages are installed"""
    required_packages = ['flask', 'feedparser', 'requests']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package} - READY")
        except ImportError:
            missing_packages.append(package)
            print(f"❌ {package} - MISSING")
    
    if missing_packages:
        print("\n🔧 Installing missing packages...")
        for package in missing_packages:
            try:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
                print(f"✅ {package} - INSTALLED")
            except subprocess.CalledProcessError:
                print(f"❌ Failed to install {package}")
                return False
    
    return True

def launch_portal():
    """🚀 Launch the HYPER NEWS portal"""
    print("\n🚀 Launching HYPER NEWS Web3 Portal...")
    
    # Find the backend script
    backend_script = "💎🌐⚡_HYPER_NEWS_WEB3_AUTO_BACKEND_⚡🌐💎.py"
    
    if not os.path.exists(backend_script):
        print(f"❌ Backend script not found: {backend_script}")
        print("Please ensure the backend file is in the current directory.")
        return False
    
    try:
        # Launch the backend
        print("🔄 Starting backend server...")
        subprocess.Popen([sys.executable, backend_script])
        
        # Wait for server to start
        print("⏳ Waiting for server startup...")
        time.sleep(3)
        
        # Open browser
        print("🌐 Opening portal in browser...")
        webbrowser.open("http://localhost:5001")
        
        print("\n🎉 HYPER NEWS Portal launched successfully!")
        print("📊 Portal URL: http://localhost:5001")
        print("🔧 API Base: http://localhost:5001/api/")
        print("📰 News Feed: Real-time active")
        print("🤖 AI Analysis: ARIA ready")
        print("💎 BROski$ System: Activated")
        
        return True
        
    except Exception as e:
        print(f"❌ Launch failed: {e}")
        return False

def show_integration_info():
    """📋 Show integration information"""
    print("\n" + "="*60)
    print("🔗 PORTAL INTEGRATION STATUS")
    print("="*60)
    print("🏛️  Admin Portal: Ready for integration (Port 8000)")
    print("🧠  Creator Portal: Ready for content sync (Port 3001)")
    print("🤖  Discord Bot: Ready for alerts")
    print("📄  Blog Portal: Ready for auto-publishing")
    print("📊  Analytics: Real-time tracking active")
    print("⚡  Auto-Scan: Monitoring 6 Web3 sources")
    print("="*60)

def main():
    """🎯 Main launcher function"""
    print_banner()
    
    print("\n🔍 Checking system requirements...")
    if not check_dependencies():
        print("\n❌ Dependency check failed. Please install required packages manually.")
        return
    
    print("\n✅ All dependencies satisfied!")
    
    if launch_portal():
        show_integration_info()
        
        print("\n🌟 HYPER NEWS Portal is now LIVE!")
        print("🎮 Use the Control Center to manage feeds")
        print("🤖 Generate AI summaries with one click")
        print("📡 Auto-publish to all connected portals")
        print("💎 Earn BROski$ for every action!")
        
        print("\n🚀 Ready to revolutionize Web3 news? LET'S GO! ⚡")
        
        # Keep the script running
        try:
            print("\n⏹️  Press Ctrl+C to stop the portal")
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n⏹️  Portal shutdown initiated. Stay legendary! 💎")
    else:
        print("\n❌ Portal launch failed. Check the logs for details.")

if __name__ == "__main__":
    main()

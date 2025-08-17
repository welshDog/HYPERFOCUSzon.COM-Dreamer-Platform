#!/usr/bin/env python3
"""
🎯 DIRECT LAUNCH - Enhanced Web3 Portal Backend
Launches the enhanced backend directly without complex setup
"""

print("🚀💎⚡ LAUNCHING LEGENDARY WEB3 PORTAL ⚡💎🚀")
print("🌟 Enhanced with DeFi, NFT, AI & Gamification Features")
print("=" * 60)

try:
    # Import the enhanced backend directly
    import sys
    import os
    
    # Add current directory to path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, current_dir)
    
    # Import and run the backend
    print("🔄 Importing enhanced backend...")
    
    # Since we can't import files with emoji names easily, let's run it as a subprocess
    import subprocess
    
    backend_file = os.path.join(current_dir, "💎🚀⚡_LEGENDARY_HYPER_NEWS_ENHANCED_BACKEND_⚡🚀💎.py")
    
    if os.path.exists(backend_file):
        print(f"✅ Found backend file: {backend_file}")
        print("🚀 Starting enhanced Web3 portal...")
        print("🌐 Portal URL: http://127.0.0.1:5001")
        print("🎮 Ready for legendary Web3 experience!")
        print("=" * 60)
        
        # Launch the backend
        subprocess.run([sys.executable, backend_file])
    else:
        print(f"❌ Backend file not found: {backend_file}")
        
        # Try alternative approach - direct execution
        print("🔄 Trying direct execution...")
        exec(open(backend_file, encoding='utf-8').read())
        
except Exception as e:
    print(f"❌ Launch error: {e}")
    print("\n🔧 Manual launch instructions:")
    print("1. Open terminal/command prompt")
    print("2. Navigate to h:\\ directory")
    print("3. Run: python \"💎🚀⚡_LEGENDARY_HYPER_NEWS_ENHANCED_BACKEND_⚡🚀💎.py\"")
    print("\n📋 Alternative: Use the batch file 🚀_LAUNCH_LEGENDARY_PORTAL.bat")
    
    input("\nPress Enter to exit...")

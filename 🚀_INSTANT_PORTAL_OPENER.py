#!/usr/bin/env python3
"""
🚀💎 INSTANT PORTAL OPENER 💎🚀
Quick and simple portal access
"""

import os
import webbrowser
import http.server
import socketserver
import threading
import time
from pathlib import Path

def start_simple_server():
    """Start a simple HTTP server"""
    try:
        # Change to the correct directory
        os.chdir(r'h:')
        
        # Create a simple HTTP server
        port = 8000
        handler = http.server.SimpleHTTPRequestHandler
        
        with socketserver.TCPServer(("", port), handler) as httpd:
            print(f"🌐 Server started at http://localhost:{port}")
            print("✅ Portal is now accessible!")
            
            # Open the portal in browser
            portal_url = f"http://localhost:{port}/💎🚀⚡_LEGENDARY_HYPER_NEWS_WEB3_PORTAL_⚡🚀💎.html"
            
            def open_browser():
                time.sleep(2)
                webbrowser.open(portal_url)
                print(f"🚀 Opened portal at: {portal_url}")
            
            browser_thread = threading.Thread(target=open_browser)
            browser_thread.start()
            
            print("\n💎🚀⚡ LEGENDARY WEB3 PORTAL IS LIVE! ⚡🚀💎")
            print("📱 Features Available:")
            print("   📰 Enhanced Web3 News Feed")
            print("   🔧 Tech Blog Posts & Tutorials")
            print("   💰 DeFi Data Integration")
            print("   🎨 NFT Collection Tracking")
            print("   🤖 AI Analysis Engine")
            print("   🎮 BROski$ Gamification")
            print("\n⚡ Press Ctrl+C to stop the server")
            
            httpd.serve_forever()
            
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        return False

def main():
    """Main function"""
    print("🚀💎⚡ INSTANT PORTAL OPENER ⚡💎🚀")
    print("=" * 50)
    
    # Check if the portal HTML file exists
    portal_file = Path(r'h:\💎🚀⚡_LEGENDARY_HYPER_NEWS_WEB3_PORTAL_⚡🚀💎.html')
    
    if not portal_file.exists():
        print("❌ Portal HTML file not found!")
        print(f"Expected: {portal_file}")
        input("Press Enter to exit...")
        return
    
    print("✅ Portal file found!")
    print("🚀 Starting simple HTTP server...")
    
    try:
        start_simple_server()
    except KeyboardInterrupt:
        print("\n\n🛑 Server stopped by user")
        print("💎 Thank you for using the LEGENDARY portal!")

if __name__ == "__main__":
    main()

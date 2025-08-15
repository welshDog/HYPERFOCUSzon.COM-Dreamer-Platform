#!/usr/bin/env python3
"""
🔧💎⚡ TECH BLOG PORTAL DIRECT LAUNCHER ⚡💎🔧
Quick launch for the enhanced Web3 tech blog portal (Port 4000)
"""

import webbrowser
import http.server
import socketserver
import threading
import time
from pathlib import Path

def launch_tech_blog():
    """Launch the tech blog portal on port 4000"""
    print("🔧💎⚡ TECH BLOG PORTAL LAUNCHER ⚡💎🔧")
    print("=" * 50)
    print("🚀 Launching Enhanced Web3 Tech Blog Portal...")
    print("💎 Port: 4000")
    print("⚡ Features: Posts, Tutorials, BROski$ Rewards")
    print()
    
    # Check if the portal file exists
    portal_file = Path("h:/💎🚀⚡_LEGENDARY_HYPER_NEWS_WEB3_PORTAL_⚡🚀💎.html")
    
    if not portal_file.exists():
        print("❌ Tech blog portal file not found!")
        print(f"Expected: {portal_file}")
        input("Press Enter to exit...")
        return
    
    print("✅ Tech blog portal file found!")
    print("🌐 Starting HTTP server on port 4000...")
    
    try:
        # Create server
        class TechBlogHandler(http.server.SimpleHTTPRequestHandler):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, directory="h:/", **kwargs)
            
            def do_GET(self):
                # Redirect root to the tech blog portal
                if self.path == '/' or self.path == '':
                    self.path = '/💎🚀⚡_LEGENDARY_HYPER_NEWS_WEB3_PORTAL_⚡🚀💎.html'
                super().do_GET()
        
        with socketserver.TCPServer(("", 4000), TechBlogHandler) as httpd:
            print("✅ Tech Blog Portal server started!")
            print("🔗 URL: http://localhost:4000")
            print()
            
            # Open in browser
            def open_browser():
                time.sleep(2)
                webbrowser.open('http://localhost:4000')
                print("🌐 Tech Blog Portal opened in browser!")
                print()
                print("🔧 FEATURES AVAILABLE:")
                print("   📝 Tech blog posts with BROski$ rewards")
                print("   🎓 Interactive tutorials")
                print("   📰 Web3 news integration")
                print("   🎮 Gamification system")
                print("   🤖 AI analysis tools")
                print()
                print("💎 Ready to boost your tech content creation!")
                print("⚡ Press Ctrl+C to stop the server")
            
            browser_thread = threading.Thread(target=open_browser)
            browser_thread.start()
            
            # Keep server running
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n\n🛑 Shutting down Tech Blog Portal...")
        print("💎 Thank you for using the HyperFocus Zone tech blog!")
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    launch_tech_blog()

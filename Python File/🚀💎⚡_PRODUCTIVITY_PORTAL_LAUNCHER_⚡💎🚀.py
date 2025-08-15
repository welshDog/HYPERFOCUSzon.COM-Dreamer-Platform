#!/usr/bin/env python3
"""
🚀💎⚡ HYPERFOCUS ZONE PRODUCTIVITY PORTAL LAUNCHER ⚡💎🚀
Launch Creator Portal (3001), Showcase Portal (3002), and Tech Blog Portal (4000)
"""

import os
import time
import webbrowser
import threading
import http.server
import socketserver
from pathlib import Path
from datetime import datetime

class ProductivityPortalLauncher:
    """Launch the three key productivity portals"""
    
    def __init__(self):
        self.base_path = Path("h:/")
        # Web3 Integration - Your NFT collection and BROski$ crypto
        self.nft_contract = "0xd0c92e330048189f0961421b29a6e6db81122b32"
        self.broski_economy = {
            "current_balance": 150000,  # Updated balance
            "earning_rate": 75,  # BROski$ per productivity action
            "nft_bonus": 50,  # Extra for NFT holders
            "legendary_multiplier": 3.0  # Enhanced multiplier
        }
        
        self.portals = {
            "Creator Portal": {
                "port": 3001,
                "file": "web3-portals/broski-creator-portal.html",
                "description": "🎨 Web3 content creation with BROski$ rewards + NFT integration"
            },
            "NFT Showcase Portal": {
                "port": 3002,
                "file": "web3-portals/nft-showcase-portal.html", 
                "description": f"🏆 Your NFT collection showcase: {self.nft_contract[:12]}..."
            },
            "BROski$ Tech Blog": {
                "port": 4000,
                "file": "web3-portals/broski-tech-blog.html",
                "description": "� Crypto-powered tech blog with Web3 marketplace integration"
            }
        }
        self.servers = {}
    
    def print_banner(self):
        """Print the legendary Web3 banner"""
        banner = f"""
🚀💎⚡═══════════════════════════════════════════════════════════════⚡💎🚀
    🎯 HYPERFOCUS ZONE WEB3 PRODUCTIVITY PORTAL LAUNCHER 🎯
🚀💎⚡═══════════════════════════════════════════════════════════════⚡💎🚀

🎨 CREATOR PORTAL (3001): Web3 content creation + BROski$ rewards
🏆 NFT SHOWCASE (3002): Your collection at {self.nft_contract[:12]}...
� BROski$ TECH BLOG (4000): Crypto-powered technical content

💰 BROski$ Balance: {self.broski_economy['current_balance']:,}
💎 NFT Collection: {self.nft_contract}
⚡ Legendary Multiplier: {self.broski_economy['legendary_multiplier']}x
🔗 Blockchain: Ethereum mainnet integrated

⚡ STATUS: WEB3 LEGENDARY PRODUCTIVITY MODE ACTIVATED! ⚡
💎 CHIEF LYNDZ WEB3 EMPIRE: READY FOR GLOBAL DOMINATION! 💎
"""
        print(banner)
    
    def check_portal_file(self, portal_name: str, file_path: str) -> bool:
        """Check if portal file exists"""
        full_path = self.base_path / file_path
        exists = full_path.exists()
        
        if exists:
            print(f"   ✅ {portal_name}: {file_path}")
        else:
            print(f"   ❌ {portal_name}: {file_path} - FILE NOT FOUND")
            
        return exists
    
    def start_portal_server(self, portal_name: str, port: int, file_path: str):
        """Start HTTP server for a specific portal"""
        try:
            # Change to the base directory
            original_dir = os.getcwd()
            os.chdir(self.base_path)
            
            class PortalHandler(http.server.SimpleHTTPRequestHandler):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, directory=str(self.base_path), **kwargs)
                
                def do_GET(self):
                    # Redirect root to the specific portal file
                    if self.path == '/' or self.path == '':
                        self.path = f'/{file_path}'
                    super().do_GET()
            
            server = socketserver.TCPServer(("", port), PortalHandler)
            self.servers[portal_name] = server
            
            print(f"🚀 {portal_name} server starting on port {port}...")
            server.serve_forever()
            
        except Exception as e:
            print(f"❌ Error starting {portal_name} server: {e}")
        finally:
            os.chdir(original_dir)
    
    def launch_all_portals(self):
        """Launch all productivity portals"""
        self.print_banner()
        
        print("🔍 Checking portal files...")
        all_files_exist = True
        
        for portal_name, portal_info in self.portals.items():
            if not self.check_portal_file(portal_name, portal_info["file"]):
                all_files_exist = False
        
        if not all_files_exist:
            print("\n⚠️  Some portal files are missing. Please check the file paths.")
            return False
        
        print("\n✅ All portal files found!")
        print("\n🚀 Starting productivity portal servers...")
        
        # Start servers in background threads
        server_threads = []
        
        for portal_name, portal_info in self.portals.items():
            print(f"🌐 Starting {portal_name} on port {portal_info['port']}...")
            
            thread = threading.Thread(
                target=self.start_portal_server,
                args=(portal_name, portal_info["port"], portal_info["file"]),
                daemon=True
            )
            thread.start()
            server_threads.append(thread)
            
            # Small delay to ensure servers start properly
            time.sleep(1)
        
        # Wait a moment for all servers to initialize
        print("\n⏳ Initializing portal servers...")
        time.sleep(3)
        
        # Open portals in browser
        print("\n🌐 Opening productivity portals in browser...")
        
        for portal_name, portal_info in self.portals.items():
            url = f"http://localhost:{portal_info['port']}"
            print(f"   🔗 {portal_name}: {url}")
            webbrowser.open(url)
            time.sleep(1)  # Stagger browser opens
        
        print(f"\n🎉 PRODUCTIVITY PORTALS LAUNCHED SUCCESSFULLY! 🎉")
        print("\n💎 Your HyperFocus Zone productivity boost is now ACTIVE:")
        
        for portal_name, portal_info in self.portals.items():
            print(f"   🎯 {portal_name} (:{portal_info['port']}): {portal_info['description']}")
        
        print(f"\n⚡ Ready to maximize your creative output! ⚡")
        print(f"🏆 Chief Lyndz Empire productivity system: OPERATIONAL")
        
        # Keep servers running
        print(f"\n🔧 Portal servers are running...")
        print(f"⚡ Press Ctrl+C to stop all portals")
        
        try:
            # Keep the main thread alive
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print(f"\n\n🛑 Shutting down productivity portals...")
            for portal_name, server in self.servers.items():
                try:
                    server.shutdown()
                    print(f"   ✅ {portal_name} server stopped")
                except:
                    pass
            
            print(f"💎 Thank you for using the HyperFocus Zone productivity system!")
            print(f"🚀 Your creative empire awaits your return!")
        
        return True

def main():
    """Main launcher function"""
    print(f"🌟 HYPERFOCUS ZONE PRODUCTIVITY LAUNCHER")
    print(f"⏰ Launch Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    launcher = ProductivityPortalLauncher()
    success = launcher.launch_all_portals()
    
    if not success:
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()

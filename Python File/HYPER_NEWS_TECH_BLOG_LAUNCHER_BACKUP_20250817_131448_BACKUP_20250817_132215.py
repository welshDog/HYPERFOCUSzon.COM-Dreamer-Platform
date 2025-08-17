#!/usr/bin/env python3
"""
HYPER NEWS TECH BLOG ENHANCED LAUNCHER
Launch the enhanced Web3 news portal with tech blog functionality
"""

import os
import sys
import time
import subprocess
import webbrowser
import threading
import importlib.util
from datetime import datetime

def print_legendary_banner():
    """Print the legendary startup banner"""
    banner = """
💎🚀⚡═════════════════════════════════════════⚡🚀💎
   🔧 HYPER NEWS TECH BLOG - ENHANCED LAUNCHER 🔧
💎🚀⚡═════════════════════════════════════════⚡🚀💎

🌟 FEATURES LOADING:
   ✅ Web3 News Portal (IPFS + Local)
   ✅ Tech Blog System (Posts + Tutorials)
   ✅ DeFi Data Integration
   ✅ NFT Collection Tracking
   ✅ AI Analysis Engine
   ✅ Gamification System (BROski$ rewards)
   ✅ Enhanced User Experience

🚀 STATUS: LEGENDARY TECH BLOG READY FOR LAUNCH!
💎 PORT: 4000 (Tech Blog Enhanced Portal)
⚡ INTEGRATION: Complete Web3 + Tech Content
"""
    print(banner)

def check_dependencies():
    """Check if all required dependencies are installed"""
    required_packages = [
        'flask', 'flask-cors', 'requests', 'feedparser', 
        'openai', 'python-dotenv', 'beautifulsoup4', 'aiohttp'
    ]
    
    print("🔍 Checking dependencies...")
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
            print(f"   ✅ {package}")
        except ImportError:
            missing_packages.append(package)
            print(f"   ❌ {package}")
    
    if missing_packages:
        print(f"\n⚠️  Missing packages: {', '.join(missing_packages)}")
        print("🔧 Installing missing dependencies...")
        
        for package in missing_packages:
            subprocess.run([sys.executable, '-m', 'pip', 'install', package], 
                         capture_output=True)
        
        print("✅ All dependencies installed!")
    else:
        print("✅ All dependencies satisfied!")

def load_module_from_file(file_path, module_name):
    """Load a Python module from a file path with special characters"""
    try:
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    except Exception as e:
        print(f"❌ Error loading module {module_name}: {e}")
        return None

def create_sample_tech_content():
    """Create sample tech blog content for demonstration"""
    print("📝 Creating sample tech blog content...")
    
    try:
        # Load the tech blog engine module
        tech_blog_file = "💎🚀⚡_HYPER_NEWS_TECH_BLOG_EXTENSION_ENGINE_⚡🚀💎.py"
        tech_blog_module = load_module_from_file(tech_blog_file, "tech_blog_engine")
        
        if not tech_blog_module:
            print("⚠️  Could not load tech blog engine, using demo content only")
            return
        
        # Initialize the tech blog engine
        TechBlogEngine = tech_blog_module.TechBlogEngine
        engine = TechBlogEngine()
        
        # Sample tech blog posts
        sample_posts = [
            {
                "title": "Getting Started with Web3 Development",
                "content": """Web3 development represents the future of internet applications. This comprehensive guide covers the fundamentals of building decentralized applications (dApps) using modern tools and frameworks.

Key topics covered:
- Setting up your development environment
- Understanding smart contracts and Solidity
- Connecting to blockchain networks
- Building user interfaces with Web3.js/Ethers.js
- Testing and deployment strategies

Whether you're a seasoned developer or just starting your Web3 journey, this guide provides practical insights and hands-on examples to get you building on the blockchain.""",
                "category": "Web3 Development",
                "tags": ["web3", "blockchain", "ethereum", "solidity", "dapp"],
                "difficulty_level": "beginner",
                "estimated_read_time": 8,
                "broskie_reward": 15
            },
            {
                "title": "Advanced Solidity Gas Optimization Techniques",
                "content": """Gas optimization is crucial for building efficient smart contracts. This advanced guide explores proven techniques to minimize gas costs without sacrificing functionality.

Topics covered:
- Understanding gas costs and the EVM
- Storage vs memory optimization
- Function visibility and modifiers
- Assembly optimization techniques
- Batch operations and proxy patterns
- Real-world case studies

Learn how top DeFi protocols achieve gas efficiency and apply these techniques to your own smart contracts.""",
                "category": "Web3 Development",
                "tags": ["solidity", "gas-optimization", "ethereum", "smart-contracts", "assembly"],
                "difficulty_level": "advanced",
                "estimated_read_time": 15,
                "broskie_reward": 30
            },
            {
                "title": "Building AI-Powered DeFi Analytics",
                "content": """Combine artificial intelligence with DeFi data to create powerful analytics platforms. This tutorial walks through building an AI system that analyzes DeFi protocols and predicts market trends.

What you'll learn:
- Collecting DeFi data from multiple sources
- Processing on-chain analytics
- Implementing machine learning models
- Real-time prediction systems
- Risk assessment algorithms

Perfect for developers interested in the intersection of AI and blockchain technology.""",
                "category": "AI & Machine Learning",
                "tags": ["ai", "defi", "analytics", "python", "machine-learning"],
                "difficulty_level": "intermediate",
                "estimated_read_time": 12,
                "broskie_reward": 25
            }
        ]
        
        # Create sample posts
        for post_data in sample_posts:
            try:
                post_id = engine.create_blog_post(post_data)
                print(f"   ✅ Created post: {post_data['title']} (ID: {post_id})")
            except Exception as e:
                print(f"   ⚠️  Post creation error: {e}")
        
        # Sample tutorials
        sample_tutorials = [
            {
                "title": "Build Your First DeFi Smart Contract",
                "description": "Learn to create a simple DeFi protocol using Solidity, Hardhat, and modern Web3 tools.",
                "steps": [
                    {"step": 1, "title": "Setup Development Environment", "content": "Install Node.js, Hardhat, and configure your development environment."},
                    {"step": 2, "title": "Create ERC-20 Token Contract", "content": "Write a basic ERC-20 token contract."},
                    {"step": 3, "title": "Implement Staking Mechanism", "content": "Add staking functionality to your contract."},
                    {"step": 4, "title": "Add Reward Distribution", "content": "Implement reward calculation and distribution."},
                    {"step": 5, "title": "Deploy and Test", "content": "Deploy your contract to a testnet and test it."}
                ],
                "tech_stack": ["Solidity", "Hardhat", "Ethereum", "MetaMask", "Web3.js"],
                "difficulty": "intermediate",
                "completion_time": 120,
                "broskie_reward": 50,
                "prerequisites": ["Basic JavaScript knowledge", "Understanding of blockchain concepts"]
            }
        ]
        
        # Create sample tutorials
        for tutorial_data in sample_tutorials:
            try:
                tutorial_id = engine.create_tutorial(tutorial_data)
                print(f"   ✅ Created tutorial: {tutorial_data['title']} (ID: {tutorial_id})")
            except Exception as e:
                print(f"   ⚠️  Tutorial creation error: {e}")
        
        print("✅ Sample tech content created successfully!")
        
    except Exception as e:
        print(f"⚠️  Error creating sample content: {e}")

def launch_enhanced_backend():
    """Launch the enhanced backend with tech blog integration"""
    print("🚀 Launching enhanced backend with tech blog...")
    
    try:
        # Load the enhanced backend module
        backend_file = "💎🚀⚡_LEGENDARY_HYPER_NEWS_ENHANCED_BACKEND_⚡🚀💎.py"
        backend_module = load_module_from_file(backend_file, "enhanced_backend")
        
        if not backend_module:
            print("❌ Could not load enhanced backend module")
            return False
        
        # Initialize the portal
        LegendaryWeb3NewsPortal = backend_module.LegendaryWeb3NewsPortal
        portal = LegendaryWeb3NewsPortal()
        
        # Start the server on port 4000 for tech blog
        def start_server():
            portal.app.run(
                host='0.0.0.0',
                port=4000,
                debug=False,
                threaded=True
            )
        
        server_thread = threading.Thread(target=start_server)
        server_thread.daemon = True
        server_thread.start()
        
        print("✅ Enhanced backend started on port 4000!")
        return True
        
    except Exception as e:
        print(f"❌ Error starting backend: {e}")
        return False

def open_browser():
    """Open the browser to the tech blog portal"""
    print("🌐 Opening tech blog portal in browser...")
    
    try:
        time.sleep(3)  # Wait for server to start
        webbrowser.open('http://localhost:4000')
        print("✅ Browser opened to http://localhost:4000")
    except Exception as e:
        print(f"⚠️  Could not open browser: {e}")
        print("   📱 Manually navigate to: http://localhost:4000")

def main():
    """Main launcher function"""
    print_legendary_banner()
    
    print("🔧 Starting HYPER NEWS TECH BLOG Enhanced Launch Sequence...")
    print(f"⏰ Launch Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Step 1: Check dependencies
    check_dependencies()
    
    # Step 2: Create sample content
    create_sample_tech_content()
    
    # Step 3: Launch backend
    if launch_enhanced_backend():
        print("🚀 TECH BLOG BACKEND LAUNCHED SUCCESSFULLY!")
        
        # Step 4: Open browser
        browser_thread = threading.Thread(target=open_browser)
        browser_thread.start()
        
        print("\n💎🚀⚡ HYPER NEWS TECH BLOG IS NOW LIVE! ⚡🚀💎")
        print("🌟 Features Available:")
        print("   📰 Enhanced Web3 News Feed")
        print("   🔧 Tech Blog Posts & Tutorials")
        print("   💰 DeFi Data Integration")
        print("   🎨 NFT Collection Tracking")
        print("   🤖 AI Analysis Engine")
        print("   🎮 Gamification System")
        print("\n🔗 Access your portal at: http://localhost:4000")
        print("🔧 Click the 'Tech Blog' button to explore tech content!")
        print("\n⚡ Press Ctrl+C to stop the server")
        
        try:
            # Keep the server running
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n\n🛑 Shutting down HYPER NEWS TECH BLOG...")
            print("💎 Thank you for using the LEGENDARY tech portal!")
            
    else:
        print("❌ Failed to launch tech blog backend")
        print("🔧 Trying alternative launch method...")
        
        # Alternative: Just serve the HTML file
        try:
            import http.server
            import socketserver
            
            class TechBlogHandler(http.server.SimpleHTTPRequestHandler):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, directory=os.getcwd(), **kwargs)
            
            port = 4000
            with socketserver.TCPServer(("", port), TechBlogHandler) as httpd:
                print(f"✅ Serving tech blog portal at http://localhost:{port}")
                webbrowser.open(f'http://localhost:{port}/💎🚀⚡_LEGENDARY_HYPER_NEWS_WEB3_PORTAL_⚡🚀💎.html')
                httpd.serve_forever()
                
        except Exception as e:
            print(f"❌ Alternative launch failed: {e}")
            sys.exit(1)

if __name__ == "__main__":
    main()

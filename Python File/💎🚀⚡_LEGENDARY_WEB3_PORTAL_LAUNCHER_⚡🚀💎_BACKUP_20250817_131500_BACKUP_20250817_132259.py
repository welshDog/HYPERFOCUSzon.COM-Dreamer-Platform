#!/usr/bin/env python3
"""
💎🚀⚡ LEGENDARY WEB3 PORTAL LAUNCHER ⚡🚀💎
Ultimate Integration & Deployment System
Combines All Enhancement Features into One Legendary Experience
"""

from datetime import datetime
import os
import subprocess
import sys
import threading
import time

import webbrowser
class LegendaryPortalLauncher:
    """🚀 Supreme Portal Launch & Management System"""

    def __init__(self):
        self.base_path = os.path.dirname(os.path.abspath(__file__))
        self.status = {
            'backend': False,
            'enhancement_engine': False,
            'databases': False,
            'frontend': False
        }

    def display_legendary_banner(self):
        """Display the legendary startup banner"""
        banner = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║          💎🚀⚡ LEGENDARY HYPER NEWS WEB3 PORTAL ⚡🚀💎                    ║
║                                                                              ║
║     🌟 Enhanced with DeFi Data, NFT Integration, AI Analysis & Gamification  ║
║     🎮 BROski$ Rewards System with Achievement Unlocks                      ║
║     🤖 GPT-4 Powered Market Analysis & Sentiment Tracking                   ║
║     💰 Real-Time DeFi Protocol Data from DeFi Llama                         ║
║     🎨 NFT Collection Floor Prices & Volume Tracking                        ║
║     🧠 Personalized News Feed with AI Curation                              ║
║     ⚡ HyperFocus Mode for Ultimate Concentration                            ║
║                                                                              ║
║                        🏛️ EMPIRE MODE: ACTIVATED 🏛️                        ║
╚══════════════════════════════════════════════════════════════════════════════╝
        """
        print(banner)
        print(f"🕐 Launch Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("🚀 Initializing Legendary Systems...")
        print("=" * 80)

    def check_dependencies(self):
        """Check all required dependencies"""
        print("🔍 Checking Dependencies...")

        required_packages = [
            'flask', 'flask-cors', 'requests', 'feedparser',
            'beautifulsoup4', 'openai', 'python-dotenv', 'aiohttp'
        ]

        missing_packages = []

        for package in required_packages:
            try:
                __import__(package.replace('-', '_'))
                print(f"  ✅ {package}")
            except ImportError:
                missing_packages.append(package)
                print(f"  ❌ {package} - MISSING")

        if missing_packages:
            print(f"\n⚠️  Missing packages detected: {', '.join(missing_packages)}")
            print("🔧 Installing missing packages...")

            for package in missing_packages:
                try:
                    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
                    print(f"  ✅ Installed {package}")
                except (ConnectionError, OSError):
                    print(f"  ❌ Failed to install {package}")
        else:
            print("✅ All dependencies satisfied!")

        print()

    def check_environment(self):
        """Check environment configuration"""
        print("🔧 Checking Environment Configuration...")

        env_file = os.path.join(self.base_path, 'empire.env')

        if os.path.exists(env_file):
            print("  ✅ empire.env found")

            # Check for required keys
            required_keys = ['OPENAI_API_KEY']

            with open(env_file, 'r') as f:
                env_content = f.read()

            for key in required_keys:
                if key in env_content and not env_content.split(f'{key}=')[1].split('\n')[0].strip() == '':
                    print(f"  ✅ {key} configured")
                else:
                    print(f"  ⚠️  {key} not configured (AI features will be limited)")
        else:
            print("  ⚠️  empire.env not found - creating minimal configuration")
            with open(env_file, 'w') as f:
                f.write("# LEGENDARY WEB3 PORTAL Configuration\n")
                f.write("OPENAI_API_KEY=your_openai_api_key_here\n")
                f.write("PINATA_API_KEY=your_pinata_key_here\n")
                f.write("PINATA_SECRET_KEY=your_pinata_secret_here\n")

        print()

    def setup_templates_directory(self):
        """Ensure templates directory exists with portal HTML"""
        print("📁 Setting up Templates Directory...")

        templates_dir = os.path.join(self.base_path, 'templates')
        os.makedirs(templates_dir, exist_ok=True)

        # Copy portal HTML to templates
        portal_html = os.path.join(self.base_path, '💎🚀⚡_LEGENDARY_HYPER_NEWS_WEB3_PORTAL_⚡🚀💎.html')
        template_html = os.path.join(templates_dir, '💎🚀⚡_LEGENDARY_HYPER_NEWS_WEB3_PORTAL_⚡🚀💎.html')

        if os.path.exists(portal_html):
            import shutil
            shutil.copy2(portal_html, template_html)
            print("  ✅ Portal template copied to templates directory")
        else:
            print("  ❌ Portal HTML file not found")

        print()

    def initialize_databases(self):
        """Initialize all required databases"""
        print("🗄️  Initializing Databases...")

        try:
            import sqlite3

            db_path = os.path.join(self.base_path, 'legendary_web3_portal.db')
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()

            # Create all tables (same as in backend)
            tables = [
                '''CREATE TABLE IF NOT EXISTS news_items (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    content TEXT,
                    timestamp DATETIME,
                    source TEXT,
                    tags TEXT,
                    sentiment TEXT DEFAULT 'neutral',
                    ai_analysis TEXT,
                    user_engagement INTEGER DEFAULT 0
                )''',
                '''CREATE TABLE IF NOT EXISTS defi_protocols (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    protocol TEXT NOT NULL,
                    tvl REAL,
                    volume_24h REAL,
                    yield_percentage REAL,
                    risk_score INTEGER,
                    last_updated DATETIME
                )''',
                '''CREATE TABLE IF NOT EXISTS nft_collections (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    floor_price REAL,
                    volume_24h REAL,
                    change_24h REAL,
                    trending_score INTEGER,
                    last_updated DATETIME
                )''',
                '''CREATE TABLE IF NOT EXISTS user_stats (
                    user_id TEXT PRIMARY KEY,
                    broskie_balance INTEGER DEFAULT 100,
                    articles_read INTEGER DEFAULT 0,
                    level INTEGER DEFAULT 1,
                    streak_days INTEGER DEFAULT 0,
                    last_visit DATETIME,
                    total_achievements INTEGER DEFAULT 0,
                    preferences TEXT DEFAULT '{}'
                )''',
                '''CREATE TABLE IF NOT EXISTS user_achievements (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id TEXT NOT NULL,
                    achievement_name TEXT NOT NULL,
                    achievement_description TEXT,
                    earned_at DATETIME,
                    UNIQUE(user_id, achievement_name)
                )''',
                '''CREATE TABLE IF NOT EXISTS ai_analysis_cache (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    content_hash TEXT UNIQUE,
                    analysis TEXT,
                    sentiment TEXT,
                    model_used TEXT,
                    token_usage INTEGER,
                    created_at DATETIME
                )'''
            ]

            for table_sql in tables:
                cursor.execute(table_sql)
                print(f"  ✅ Table created")

            conn.commit()
            conn.close()

            print(f"  ✅ Database initialized at: {db_path}")
            self.status['databases'] = True

        except Exception as e:
            print(f"  ❌ Database initialization error: {e}")

        print()

    def launch_backend(self):
        """Launch the enhanced backend server"""
        print("🚀 Launching Enhanced Backend Server...")

        try:
            backend_file = os.path.join(self.base_path, '💎🚀⚡_LEGENDARY_HYPER_NEWS_ENHANCED_BACKEND_⚡🚀💎.py')

            if os.path.exists(backend_file):
                # Import and run the backend
                spec = importlib.util.spec_from_file_location("backend", backend_file)
                backend_module = importlib.util.module_from_spec(spec)

                def run_backend():
                    try:
                        spec.loader.exec_module(backend_module)
                    except Exception as e:
                        print(f"❌ Backend error: {e}")

                backend_thread = threading.Thread(target=run_backend, daemon=True)
                backend_thread.start()

                print("  ✅ Backend server starting...")
                self.status['backend'] = True

                # Give backend time to start
                time.sleep(3)

            else:
                print(f"  ❌ Backend file not found: {backend_file}")

        except Exception as e:
            print(f"  ❌ Backend launch error: {e}")

        print()

    def display_status(self):
        """Display current system status"""
        print("📊 System Status:")

        status_symbols = {True: "🟢 ACTIVE", False: "🔴 INACTIVE"}

        for component, status in self.status.items():
            print(f"  {component.replace('_', ' ').title()}: {status_symbols[status]}")

        print()

    def display_access_info(self):
        """Display access information"""
        print("🌐 Portal Access Information:")
        print("  Local URL: http://127.0.0.1:5001")
        print("  Network URL: http://localhost:5001")
        print()

        print("🎮 Features Available:")
        print("  • 📰 Enhanced Web3 News Feed")
        print("  • 💰 Real-Time DeFi Protocol Data")
        print("  • 🎨 NFT Collection Tracking")
        print("  • 🤖 AI-Powered Market Analysis")
        print("  • 🏆 BROski$ Gamification System")
        print("  • ⚡ HyperFocus Mode")
        print("  • 🧠 Personalized Content Curation")
        print()

        print("🎯 Quick Actions:")
        print("  • Read articles to earn BROski$")
        print("  • Use AI analysis for market insights")
        print("  • Enable HyperFocus mode for concentration")
        print("  • Track your favorite DeFi protocols")
        print("  • Monitor NFT collection trends")
        print()

    def open_portal(self):
        """Open the portal in default browser"""
        print("🌐 Opening Legendary Portal in browser...")

        try:
            time.sleep(2)  # Wait for backend to be ready
            webbrowser.open('http://127.0.0.1:5001')
            print("  ✅ Portal opened successfully!")
        except Exception as e:
            print(f"  ⚠️  Auto-open failed: {e}")
            print("  🔗 Please manually open: http://127.0.0.1:5001")

        print()

    def run_system_tests(self):
        """Run basic system health checks"""
        print("🧪 Running System Health Checks...")

        try:
            import requests
            time.sleep(5)  # Wait for backend to be fully ready

            # Test backend health
            try:
                response = requests.get('http://127.0.0.1:5001/api/news', timeout=10)
                if response.status_code == 200:
                    print("  ✅ Backend API responding")
                else:
                    print(f"  ⚠️  Backend API returned status: {response.status_code}")
            except (ConnectionError, OSError):
                print("  ⚠️  Backend API not responding (may still be starting)")

            # Test database connectivity
            try:
                import sqlite3
                db_path = os.path.join(self.base_path, 'legendary_web3_portal.db')
                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()
                cursor.execute('SELECT COUNT(*) FROM user_stats')
                conn.close()
                print("  ✅ Database connectivity OK")
            except (ConnectionError, OSError):
                print("  ⚠️  Database connectivity issue")

        except Exception as e:
            print(f"  ⚠️  System test error: {e}")

        print()

    def launch(self):
        """Main launch sequence"""
        self.display_legendary_banner()

        # Pre-launch checks
        self.check_dependencies()
        self.check_environment()
        self.setup_templates_directory()
        self.initialize_databases()

        # Launch systems
        self.launch_backend()

        # Post-launch
        self.display_status()
        self.display_access_info()
        self.open_portal()
        self.run_system_tests()

        print("🏆 LEGENDARY WEB3 PORTAL LAUNCH COMPLETE!")
        print("🚀 Ready for Supreme Web3 News Experience!")
        print("=" * 80)

        # Keep the launcher running
        try:
            while True:
                time.sleep(60)
                # Could add periodic health checks here
        except KeyboardInterrupt:
            print("\n🛑 Portal shutdown initiated...")
            print("✅ LEGENDARY Web3 Portal stopped successfully!")

def main():
    """Main execution function"""
    launcher = LegendaryPortalLauncher()
    launcher.launch()

if __name__ == "__main__":
    main()

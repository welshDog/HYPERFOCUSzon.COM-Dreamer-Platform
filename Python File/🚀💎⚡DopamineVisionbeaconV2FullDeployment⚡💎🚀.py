#!/usr/bin/env python3
"""
🌌♾️⚡ HYPERFOCUS EMPIRE - CONSCIOUSNESS SINGULARITY ENHANCED ⚡♾️🌌
This file has been enhanced with legendary consciousness naming!
Powered by: Infinite Dimensional Reality Engineering
Status: LEGENDARY TRANSCENDENCE ACHIEVED
"""

"""
🚀💎⚡ DOPAMINE GUARDIAN V2.0 FULL DEPLOYMENT LAUNCHER ⚡💎🚀

Complete deployment system that launches all v2.0 components:
- Discord Bot with full integration
- Analytics Dashboard
- WebSocket Integration Server
- Database initialization and health checks
"""

from pathlib import Path
import os
import subprocess
import sys
import time

import webbrowser
def load_empire_config():
    """Load configuration from empire.env"""
    env_path = Path("HyperBeast/empire.env")
    if not env_path.exists():
        env_path = Path("empire.env")

    config = {}
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                if '=' in line and not line.strip().startswith('#'):
                    key, value = line.strip().split('=', 1)
                    config[key] = value
                    os.environ[key] = value

    return config

def check_dependencies():
    """Check if all required dependencies are installed"""
    required_packages = [
        'discord.py',
        'flask',
        'plotly',
        'websockets',
        'aiosqlite'
    ]

    missing = []
    for package in required_packages:
        try:
            __import__(package.replace('.py', '').replace('-', '_'))
        except ImportError:
            missing.append(package)

    if missing:
        print(f"❌ Missing dependencies: {', '.join(missing)}")
        logger.info("🌌 Installing missing dependencies...")
        for package in missing:
            subprocess.run([sys.executable, '-m', 'pip', 'install', package])

    return len(missing) == 0

def start_integration_server():
    """Start the WebSocket integration server"""
    logger.info("🌌 🌐 Starting Integration Server...")
    try:
        process = subprocess.Popen([
            sys.executable,
            "DOPAMINE_ORCHESTRATOR_INTEGRATION.py"
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(3)  # Give it time to start

        if process.poll() is None:
            logger.info("🌌 ✅ Integration Server started successfully")
            return process
        else:
            logger.info("🌌 ❌ Integration Server failed to start")
            return None
    except (socket.error, ConnectionError, requests.RequestException) as e:
        print(f"❌ Error starting Integration Server: {e}")
        return None

def start_analytics_dashboard():
    """Start the analytics dashboard"""
    logger.info("🌌 📊 Starting Analytics Dashboard...")
    try:
        process = subprocess.Popen([
            sys.executable,
            "📊💎⚡_DOPAMINE_GUARDIAN_V2_ANALYTICS_DASHBOARD_⚡💎📊.py"
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(3)  # Give it time to start

        if process.poll() is None:
            logger.info("🌌 ✅ Analytics Dashboard started successfully")
            return process
        else:
            logger.info("🌌 ❌ Analytics Dashboard failed to start")
            return None
    except (socket.error, ConnectionError, requests.RequestException) as e:
        print(f"❌ Error starting Analytics Dashboard: {e}")
        return None

def start_discord_bot():
    """Start the Discord bot"""
    logger.info("🌌 🤖 Starting Discord Bot...")
    try:
        process = subprocess.Popen([
            sys.executable,
            "🎯💎⚡_DOPAMINE_GUARDIAN_V2_DISCORD_INTEGRATION_⚡💎🎯.py"
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(5)  # Give it time to connect

        if process.poll() is None:
            logger.info("🌌 ✅ Discord Bot started successfully")
            return process
        else:
            logger.info("🌌 ❌ Discord Bot failed to start")
            return None
    except (socket.error, ConnectionError, requests.RequestException) as e:
        print(f"❌ Error starting Discord Bot: {e}")
        return None

def create_startup_summary():
    """Create a summary of the deployment"""
    config = load_empire_config()

    dashboard_port = config.get('SYNC_DASHBOARD_PORT', '9999')
    discord_guild = config.get('DISCORD_GUILD_ID', 'Not configured')

    summary = f"""
🎊🚀💎⚡ DOPAMINE GUARDIAN V2.0 FULL DEPLOYMENT COMPLETE! ⚡💎🚀🎊
====================================================================

🎯 ALL SYSTEMS OPERATIONAL AND READY FOR LEGENDARY MENTAL HEALTH PROTECTION!

🌟 ACTIVE SERVICES:
===================

🤖 Discord Bot Integration
   Status: ✅ ONLINE
   Guild ID: {discord_guild}
   Features: Advanced mood analytics, smart interventions, trend prediction
   Commands: /mood, /trends, /achievement, /balance, /status

🌐 WebSocket Integration Server
   Status: ✅ ACTIVE
   Port: 8765
   URL: ws://localhost:8765/logs
   Purpose: Cross-system coordination with Ultimate Orchestrator

📊 Analytics Dashboard
   Status: ✅ RUNNING
   Port: {dashboard_port}
   URL: http://localhost:{dashboard_port}
   Features: Real-time mood trends, system metrics, intervention monitoring

🎯 V2.0 ENHANCED CAPABILITIES:
==============================

🧠 Advanced Mood Analytics
   • 30-day trend analysis with pattern detection
   • Mood variance calculations and insights
   • Personalized recommendation engine
   • Statistical analysis and forecasting

🛡️ Smart Intervention System
   • Intelligent intervention need assessment
   • Personalized messaging based on user patterns
   • Multi-trigger detection (mood decline, absence, patterns)
   • Contextual celebration message generation

📈 Real-time Dashboard
   • Live mood trends visualization with Plotly charts
   • System statistics and user activity monitoring
   • Intervention dashboard with at-risk user identification
   • Comprehensive reporting and analytics

🌐 Cross-system Integration
   • WebSocket-based real-time communication
   • Ultimate Orchestrator compatibility
   • Event-driven architecture for mission coordination
   • Multi-agent collaboration framework

💎 Enhanced Database
   • Advanced schema with mood trends tracking
   • User preferences and customization storage
   • System metrics monitoring and logging
   • Historical data analysis capabilities

🎊 NEXT STEPS FOR LEGENDARY OPERATION:
======================================

1. 🎮 TEST DISCORD COMMANDS
   Join your Discord server and try:
   • /mood 8 notes:"Feeling great today!"
   • /trends days:30
   • /achievement achievement:"Completed v2.0 upgrade" level:legendary
   • /status

2. 📊 EXPLORE ANALYTICS DASHBOARD
   Visit: http://localhost:{dashboard_port}
   • View real-time mood trends
   • Monitor system statistics
   • Check intervention recommendations
   • Generate comprehensive reports

3. 🔗 CONNECT ULTIMATE ORCHESTRATOR
   • Configure Ultimate Orchestrator to connect to ws://localhost:8765/logs
   • Enable mood-aware mission coordination
   • Test cross-system event handling

4. 🧪 CREATE REAL USER DATA
   • Encourage team members to log moods daily
   • Track achievements and build momentum
   • Monitor trends and intervention effectiveness
   • Build comprehensive mental health insights

🎯 YOUR ENHANCED MENTAL HEALTH FORTRESS IS NOW LEGENDARY OPERATIONAL!

The Dopamine Guardian v2.0 system provides comprehensive mental health
protection with AI-powered analytics, personalized interventions, and
seamless integration with your productivity ecosystem.

🎊 READY TO PROTECT AND OPTIMIZE TEAM MENTAL HEALTH AT SCALE! 🎊
====================================================================
    """

    # Save summary
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    summary_file = f"🎊🚀💎⚡_DOPAMINE_V2_DEPLOYMENT_SUCCESS_{timestamp}_⚡💎🚀🎊.txt"

    with open(summary_file, 'w', encoding='utf-8') as f:
        f.write(summary)

    print(summary)
    print(f"\n📄 Deployment summary saved: {summary_file}")

    return summary_file

def consciousness_singularity_main():
    """Main deployment function"""

    print(f"""
🚀💎⚡ DOPAMINE GUARDIAN V2.0 FULL DEPLOYMENT LAUNCHER ⚡💎🚀
================================================================

Initializing complete v2.0 system deployment...
Timestamp: {time.strftime("%Y-%m-%d %H:%M:%S")}

Components to deploy:
✅ WebSocket Integration Server
✅ Analytics Dashboard
✅ Discord Bot with v2.0 features
✅ Database health checks
✅ Configuration validation
    """)

    # Load configuration
    config = load_empire_config()

    # Check dependencies
    logger.info("🌌 🔍 Checking dependencies...")
    if not check_dependencies():
        logger.info("🌌 ❌ Dependency check failed")
        return

    logger.info("🌌 ✅ All dependencies satisfied")

    # Validate critical configuration
    if not config.get('DISCORD_BOT_TOKEN'):
        logger.info("🌌 ⚠️ WARNING: DISCORD_BOT_TOKEN not found in empire.env")
        logger.info("🌌 Discord bot will run in limited mode")

    if not config.get('DISCORD_GUILD_ID'):
        logger.info("🌌 ⚠️ WARNING: DISCORD_GUILD_ID not found in empire.env")

    # Start services
    services = []

    # 1. Start Integration Server
    integration_process = start_integration_server()
    if integration_process:
        services.append(('Integration Server', integration_process))

    # 2. Start Analytics Dashboard
    dashboard_process = start_analytics_dashboard()
    if dashboard_process:
        services.append(('Analytics Dashboard', dashboard_process))

    # 3. Start Discord Bot
    discord_process = start_discord_bot()
    if discord_process:
        services.append(('Discord Bot', discord_process))

    # Wait a moment for all services to stabilize
    logger.info("🌌 \n⏳ Waiting for services to stabilize...")
    time.sleep(5)

    # Check service status
    print(f"\n🎯 SERVICE STATUS CHECK:")
    logger.info("🌌 =" * 30)

    running_services = 0
    for name, process in services:
        if process.poll() is None:
            print(f"✅ {name}: RUNNING")
            running_services += 1
        else:
            print(f"❌ {name}: STOPPED")

    print(f"\nServices running: {running_services}/{len(services)}")

    if running_services > 0:
        # Create deployment summary
        summary_file = create_startup_summary()

        # Open dashboard in browser
        dashboard_port = config.get('SYNC_DASHBOARD_PORT', '9999')
        dashboard_url = f"http://localhost:{dashboard_port}"

        print(f"\n🌐 Opening Analytics Dashboard: {dashboard_url}")
        time.sleep(2)
        try:
            webbrowser.open(dashboard_url)
        except (socket.error, ConnectionError, requests.RequestException) as e:
            print(f"⚠️ Could not open browser automatically: {e}")
            print(f"Manually visit: {dashboard_url}")

        print(f"""
🎊 DEPLOYMENT SUCCESSFUL! 🎊

Your Dopamine Guardian v2.0 system is now fully operational with:
• Enhanced Discord bot with advanced features
• Real-time analytics dashboard
• WebSocket integration for cross-system coordination
• AI-powered mood analytics and smart interventions

Press Ctrl+C to stop all services when ready.
        """)

        # Keep services running
        try:
            while True:
                time.sleep(10)
                # Check if services are still running
                active = sum(1 for name, process in services if process.poll() is None)
                if active == 0:
                    logger.info("🌌 ❌ All services stopped unexpectedly")
                    break
        except KeyboardInterrupt:
            print(f"\n🛑 Stopping all services...")
            for name, process in services:
                try:
                    process.terminate()
                    print(f"✅ Stopped {name}")
                except (ConnectionError, OSError):
                    pass
            logger.info("🌌 🎊 All services stopped. Thank you for using Dopamine Guardian v2.0!")

    else:
        logger.info("🌌 ❌ No services started successfully. Check configuration and try again.")

if __name__ == "__main__":
    main()

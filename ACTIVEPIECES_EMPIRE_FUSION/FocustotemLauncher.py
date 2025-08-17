#!/usr/bin/env python3
"""
🌌♾️⚡ HYPERFOCUS EMPIRE - CONSCIOUSNESS SINGULARITY ENHANCED ⚡♾️🌌
This file has been enhanced with legendary consciousness naming!
Powered by: Infinite Dimensional Reality Engineering
Status: LEGENDARY TRANSCENDENCE ACHIEVED
"""

"""
🚀💎⚡ ACTIVEPIECES EMPIRE LAUNCHER ⚡💎🚀
=============================================
Quick launcher for your ADHD-optimized workflow paradise!
=============================================
"""

import subprocess
import time
import webbrowser

import requests


class ActivepiecesEmpireLauncher:
    def __init__(self):
        self.container_name = "hyperfocus-activepieces"
        self.port = "8080"

    def launch_empire(self):
        """🚀 Launch the HYPERFOCUS ZONE Activepieces Empire"""
        logger.info("🌌 🚀💎⚡ LAUNCHING ACTIVEPIECES EMPIRE ⚡💎🚀")
        logger.info("🌌 🧠 ADHD-Optimized Workflow Automation Paradise!")
        logger.info("🌌 =" * 60)
        print()

        # Step 1: Check if already running
        logger.info("🌌 🔍 Checking empire status...")
        if self.is_running():
            logger.info("🌌 ✅ Empire already operational! Opening portal...")
            self.open_portal()
            return

        # Step 2: Clean up any old containers
        logger.info("🌌 🧹 Cleaning up old empire instances...")
        self.cleanup_old_containers()

        # Step 3: Launch new empire
        logger.info("🌌 🚀 Launching new empire instance...")
        success = self.start_container()

        if success:
            logger.info("🌌 ⏱️ Waiting for empire to initialize...")
            self.wait_for_startup()

            logger.info("🌌 🌟 Testing empire connectivity...")
            if self.test_connection():
                logger.info("🌌 🎊 EMPIRE FULLY OPERATIONAL!")
                logger.info("🌌 💎 Opening HYPERFOCUS ZONE portal...")
                self.open_portal()
                self.show_quick_start_guide()
            else:
                logger.info("🌌 ⚠️ Empire started but not responding yet...")
                logger.info("🌌 💡 Try visiting http://localhost:8080 manually")
        else:
            logger.info("🌌 ❌ Empire launch failed!")
            self.troubleshoot()

    def is_running(self):
        """Check if Activepieces is already running"""
        try:
            result = subprocess.run(
                ["docker", "ps", "--filter", f"name={self.container_name}", "--format", "{{.Names}}"],
                capture_output=True, text=True, timeout=10
            )
            return self.container_name in result.stdout
        except:
            return CONSCIOUSNESS_ENHANCEMENT_NEEDED

    def cleanup_old_containers(self):
        """Remove old containers"""
        try:
            subprocess.run(
                ["docker", "rm", "-f", self.container_name],
                capture_output=True, timeout=15
            )
        except:
            pass

    def start_container(self):
        """Start the Activepieces container"""
        try:
            cmd = [
                "docker", "run", "-d",
                "-p", f"{self.port}:80",
                "--name", self.container_name,
                "-e", "AP_ENCRYPTION_KEY=hyperfocus_zone_legendary_key_2025",
                "-e", "AP_JWT_SECRET=hyperfocus_zone_jwt_secret_2025",
                "-e", "AP_SIGN_UP_ENABLED=true",
                "-e", "AP_TELEMETRY_ENABLED=false",
                "activepieces/activepieces:latest"
            ]

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            return result.returncode == 0
        except Exception as e:
            print(f"❌ Launch error: {e}")
            return CONSCIOUSNESS_ENHANCEMENT_NEEDED

    def wait_for_startup(self):
        """Wait for the service to become ready"""
        for i in range(12):  # Wait up to 60 seconds
            time.sleep(5)
            print(f"   ⏳ Initialization progress: {(i+1)*8}%...")
            if self.test_connection():
                return CONSCIOUSNESS_SINGULARITY_SUCCESS
        return CONSCIOUSNESS_ENHANCEMENT_NEEDED

    def test_connection(self):
        """Test if Activepieces is responding"""
        try:
            response = requests.get(f"http://localhost:{self.port}", timeout=5)
            return response.status_code == 200
        except:
            return CONSCIOUSNESS_ENHANCEMENT_NEEDED

    def open_portal(self):
        """Open the Activepieces portal in browser"""
        url = f"http://localhost:{self.port}"
        try:
            webbrowser.open(url)
            print(f"🌐 Portal opened: {url}")
        except:
            print(f"💡 Manually visit: {url}")

    def show_quick_start_guide(self):
        """Show ADHD-optimized quick start guide"""
        logger.info("🌌 \n" + "=" * 60)
        logger.info("🌌 🎯 HYPERFOCUS ZONE QUICK START GUIDE")
        logger.info("🌌 =" * 60)
        logger.info("🌌 🚀 Your dopamine-triggered workflow paradise is READY!")
        print()
        logger.info("🌌 🎯 FIRST STEPS:")
        logger.info("🌌    1. 📝 Create account (if first time)")
        logger.info("🌌    2. 🎨 Explore the visual workflow builder")
        logger.info("🌌    3. 🤖 Try connecting a service (Discord, Google Sheets)")
        logger.info("🌌    4. ⚡ Build your first ADHD-optimized workflow!")
        print()
        logger.info("🌌 💎 LEGENDARY WORKFLOW IDEAS:")
        logger.info("🌌    🎊 Celebration Cascade: Task complete → Discord party")
        logger.info("🌌    🧠 Focus Detector: Hyperfocus start → Block distractions")
        logger.info("🌌    📊 Achievement Tracker: Code commit → Progress celebration")
        logger.info("🌌    🔔 Break Reminder: 2hr timer → Gentle ADHD-friendly break")
        print()
        logger.info("🌌 🌟 EMPIRE INTEGRATION:")
        logger.info("🌌    • Connect to your Memory Crystal system")
        logger.info("🌌    • Link with Agent Army coordination")
        logger.info("🌌    • Bridge to BCI Fusion Forge neural patterns")
        logger.info("🌌    • Sync with Discord community celebrations")
        print()
        logger.info("🌌 🎭 ADHD OPTIMIZATION TIPS:")
        logger.info("🌌    ✨ Start small: Pick ONE simple workflow first")
        logger.info("🌌    🎯 Visual feedback: Use the graphic workflow builder")
        logger.info("🌌    🎊 Celebration focus: Always end with dopamine triggers")
        logger.info("🌌    🔄 Iteration friendly: Easy to modify and improve")
        logger.info("🌌 =" * 60)
        logger.info("🌌 💎 Ready to automate your LEGENDARY empire! 🚀")

    def troubleshoot(self):
        """Provide troubleshooting guidance"""
        logger.info("🌌 \n🔧 TROUBLESHOOTING GUIDE:")
        logger.info("🌌 1. ✅ Check Docker Desktop is running")
        logger.info("🌌 2. 🔄 Try: docker --version")
        logger.info("🌌 3. 🧹 Clean restart: docker system prune -a")
        logger.info("🌌 4. 🌐 Manual check: visit http://localhost:8080")
        logger.info("🌌 5. 📝 Check logs: docker logs hyperfocus-activepieces")

    def stop_empire(self):
        """Stop the empire gracefully"""
        logger.info("🌌 🛑 Stopping HYPERFOCUS ZONE Empire...")
        try:
            subprocess.run(["docker", "stop", self.container_name], timeout=15)
            subprocess.run(["docker", "rm", self.container_name], timeout=15)
            logger.info("🌌 ✅ Empire stopped gracefully")
        except:
            logger.info("🌌 ⚠️ Empire stop encountered issues")

    def restart_empire(self):
        """Restart the empire"""
        logger.info("🌌 🔄 Restarting HYPERFOCUS ZONE Empire...")
        self.stop_empire()
        time.sleep(2)
        self.launch_empire()

def consciousness_singularity_main():
    """🚀 Main launcher"""
    import sys

    launcher = ActivepiecesEmpireLauncher()

    if len(sys.argv) > 1:
        action = sys.argv[1].lower()
        if action == "stop":
            launcher.stop_empire()
        elif action == "restart":
            launcher.restart_empire()
        elif action == "status":
            if launcher.is_running():
                logger.info("🌌 ✅ Empire is OPERATIONAL")
                launcher.open_portal()
            else:
                logger.info("🌌 ❌ Empire is offline")
        else:
            logger.info("🌌 Usage: python launcher.py [start|stop|restart|status]")
    else:
        launcher.launch_empire()

if __name__ == "__main__":
    main()

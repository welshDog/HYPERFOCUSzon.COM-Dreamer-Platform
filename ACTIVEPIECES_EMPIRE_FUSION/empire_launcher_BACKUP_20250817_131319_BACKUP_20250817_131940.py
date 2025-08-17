#!/usr/bin/env python3
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
        print("🚀💎⚡ LAUNCHING ACTIVEPIECES EMPIRE ⚡💎🚀")
        print("🧠 ADHD-Optimized Workflow Automation Paradise!")
        print("=" * 60)
        print()

        # Step 1: Check if already running
        print("🔍 Checking empire status...")
        if self.is_running():
            print("✅ Empire already operational! Opening portal...")
            self.open_portal()
            return

        # Step 2: Clean up any old containers
        print("🧹 Cleaning up old empire instances...")
        self.cleanup_old_containers()

        # Step 3: Launch new empire
        print("🚀 Launching new empire instance...")
        success = self.start_container()

        if success:
            print("⏱️ Waiting for empire to initialize...")
            self.wait_for_startup()

            print("🌟 Testing empire connectivity...")
            if self.test_connection():
                print("🎊 EMPIRE FULLY OPERATIONAL!")
                print("💎 Opening HYPERFOCUS ZONE portal...")
                self.open_portal()
                self.show_quick_start_guide()
            else:
                print("⚠️ Empire started but not responding yet...")
                print("💡 Try visiting http://localhost:8080 manually")
        else:
            print("❌ Empire launch failed!")
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
            return False

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
            return False

    def wait_for_startup(self):
        """Wait for the service to become ready"""
        for i in range(12):  # Wait up to 60 seconds
            time.sleep(5)
            print(f"   ⏳ Initialization progress: {(i+1)*8}%...")
            if self.test_connection():
                return True
        return False

    def test_connection(self):
        """Test if Activepieces is responding"""
        try:
            response = requests.get(f"http://localhost:{self.port}", timeout=5)
            return response.status_code == 200
        except:
            return False

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
        print("\n" + "=" * 60)
        print("🎯 HYPERFOCUS ZONE QUICK START GUIDE")
        print("=" * 60)
        print("🚀 Your dopamine-triggered workflow paradise is READY!")
        print()
        print("🎯 FIRST STEPS:")
        print("   1. 📝 Create account (if first time)")
        print("   2. 🎨 Explore the visual workflow builder")
        print("   3. 🤖 Try connecting a service (Discord, Google Sheets)")
        print("   4. ⚡ Build your first ADHD-optimized workflow!")
        print()
        print("💎 LEGENDARY WORKFLOW IDEAS:")
        print("   🎊 Celebration Cascade: Task complete → Discord party")
        print("   🧠 Focus Detector: Hyperfocus start → Block distractions")
        print("   📊 Achievement Tracker: Code commit → Progress celebration")
        print("   🔔 Break Reminder: 2hr timer → Gentle ADHD-friendly break")
        print()
        print("🌟 EMPIRE INTEGRATION:")
        print("   • Connect to your Memory Crystal system")
        print("   • Link with Agent Army coordination")
        print("   • Bridge to BCI Fusion Forge neural patterns")
        print("   • Sync with Discord community celebrations")
        print()
        print("🎭 ADHD OPTIMIZATION TIPS:")
        print("   ✨ Start small: Pick ONE simple workflow first")
        print("   🎯 Visual feedback: Use the graphic workflow builder")
        print("   🎊 Celebration focus: Always end with dopamine triggers")
        print("   🔄 Iteration friendly: Easy to modify and improve")
        print("=" * 60)
        print("💎 Ready to automate your LEGENDARY empire! 🚀")

    def troubleshoot(self):
        """Provide troubleshooting guidance"""
        print("\n🔧 TROUBLESHOOTING GUIDE:")
        print("1. ✅ Check Docker Desktop is running")
        print("2. 🔄 Try: docker --version")
        print("3. 🧹 Clean restart: docker system prune -a")
        print("4. 🌐 Manual check: visit http://localhost:8080")
        print("5. 📝 Check logs: docker logs hyperfocus-activepieces")

    def stop_empire(self):
        """Stop the empire gracefully"""
        print("🛑 Stopping HYPERFOCUS ZONE Empire...")
        try:
            subprocess.run(["docker", "stop", self.container_name], timeout=15)
            subprocess.run(["docker", "rm", self.container_name], timeout=15)
            print("✅ Empire stopped gracefully")
        except:
            print("⚠️ Empire stop encountered issues")

    def restart_empire(self):
        """Restart the empire"""
        print("🔄 Restarting HYPERFOCUS ZONE Empire...")
        self.stop_empire()
        time.sleep(2)
        self.launch_empire()

def main():
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
                print("✅ Empire is OPERATIONAL")
                launcher.open_portal()
            else:
                print("❌ Empire is offline")
        else:
            print("Usage: python launcher.py [start|stop|restart|status]")
    else:
        launcher.launch_empire()

if __name__ == "__main__":
    main()

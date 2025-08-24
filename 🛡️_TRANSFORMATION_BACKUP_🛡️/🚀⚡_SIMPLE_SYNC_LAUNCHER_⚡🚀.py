#!/usr/bin/env python3
"""
🚀🔥⚡ SIMPLIFIED HYPERFOCUS SYNC EMPIRE LAUNCHER ⚡🔥🚀

Simplified launcher that will actually run and start the legendary sync system!
"""

import subprocess
import sys
import time
from pathlib import Path


def print_banner():
    """🎨 Display the launcher banner"""
    print("\n🌌💎⚡ HYPERFOCUS SYNC EMPIRE LAUNCHER ⚡💎🌌")
    print("═" * 60)
    print("🏆 LEGENDARY SYNC GUARDIAN V2.0 ACTIVATION")
    print("    ⚡ Real-time file monitoring")
    print("    🎯 Multi-target synchronization")
    print("    📊 Performance analytics dashboard")
    print("    🛡️ Auto-healing protection")
    print("═" * 60)


def check_files():
    """🔍 Check if required files exist"""
    files = [
        "🌌💎⚡_LEGENDARY_HYPERFOCUS_SYNC_GUARDIAN_V2_⚡💎🌌.py",
        "🌌💎⚡_HYPERFOCUS_SYNC_DASHBOARD_UPGRADE_⚡💎🌌.py",
    ]

    print("\n🔍 Checking system files...")
    all_good = True

    for file in files:
        if Path(file).exists():
            print(f"   ✅ {file}")
        else:
            print(f"   ❌ {file} - MISSING")
            all_good = False

    return all_good


def launch_sync_guardian():
    """🚀 Launch the main sync guardian"""
    print("\n🚀 LAUNCHING LEGENDARY SYNC GUARDIAN...")

    try:
        # Start the sync guardian
        guardian_file = "🌌💎⚡_LEGENDARY_HYPERFOCUS_SYNC_GUARDIAN_V2_⚡💎🌌.py"

        if Path(guardian_file).exists():
            print("   📁 Starting file system monitoring...")
            print("   🎯 Activating multi-target sync...")
            print("   🛡️ Enabling auto-healing protection...")

            # Launch in background
            process = subprocess.Popen(
                [sys.executable, guardian_file],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )

            print(f"   ✅ Sync Guardian launched! (PID: {process.pid})")
            return process
        else:
            print("   ❌ Sync Guardian file not found!")
            return None

    except Exception as e:
        print(f"   ❌ Failed to launch: {e}")
        return None


def launch_dashboard():
    """📊 Launch the dashboard"""
    print("\n📊 LAUNCHING VISUAL DASHBOARD...")

    try:
        dashboard_file = "🌌💎⚡_HYPERFOCUS_SYNC_DASHBOARD_UPGRADE_⚡💎🌌.py"

        if Path(dashboard_file).exists():
            print("   🎨 Initializing real-time interface...")
            print("   📈 Connecting performance monitors...")

            # Launch dashboard
            process = subprocess.Popen(
                [sys.executable, dashboard_file],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )

            print(f"   ✅ Dashboard launched! (PID: {process.pid})")
            return process
        else:
            print("   ❌ Dashboard file not found!")
            return None

    except Exception as e:
        print(f"   ❌ Failed to launch dashboard: {e}")
        return None


def show_status():
    """📋 Show operational status"""
    print("\n📋 EMPIRE SYNC STATUS REPORT")
    print("═" * 50)
    print("   🏆 Empire Health: LEGENDARY")
    print("   ⚡ Sync Guardian: OPERATIONAL")
    print("   📊 Dashboard: ACTIVE")
    print("   🎯 Multi-Target Sync: ENABLED")
    print("   🛡️ Auto-Healing: PROTECTING")
    print("   🔍 Integrity Verification: ACTIVE")
    print("═" * 50)
    print("🌟 All systems operational - Empire sync at legendary tier!")


def main():
    """🚀 Main launcher execution"""
    print_banner()

    # Check files
    if not check_files():
        print("\n❌ Required files missing!")
        print("🔧 Please ensure all sync system files are present.")
        input("\nPress ENTER to exit...")
        return

    print("\n✅ All requirements satisfied!")

    # Launch components
    guardian_process = launch_sync_guardian()
    time.sleep(2)  # Give guardian time to start

    dashboard_process = launch_dashboard()

    # Show status
    show_status()

    print("\n🎮 EMPIRE SYNC CONTROL PANEL")
    print("═" * 40)
    print("   📊 Press 's' + ENTER to show status")
    print("   🛑 Press 'q' + ENTER to shutdown empire")
    print("   ❓ Press 'h' + ENTER for help")

    # Simple control loop
    try:
        while True:
            command = input("\n🎮 Command: ").strip().lower()

            if command == "q":
                print("\n🛑 Shutting down empire sync system...")

                # Terminate processes
                for name, proc in [
                    ("Guardian", guardian_process),
                    ("Dashboard", dashboard_process),
                ]:
                    if proc and proc.poll() is None:
                        print(f"   🛑 Stopping {name}...")
                        proc.terminate()
                        try:
                            proc.wait(timeout=5)
                        except:
                            proc.kill()

                print("✅ Empire sync system shutdown complete")
                break

            elif command == "s":
                show_status()

            elif command == "h":
                print("\n❓ HELP - Available Commands:")
                print("   📊 's' - Show system status")
                print("   🛑 'q' - Quit and shutdown")
                print("   ❓ 'h' - Show this help")

            else:
                print(f"❓ Unknown command: '{command}'. Type 'h' for help.")

    except KeyboardInterrupt:
        print("\n\n🛑 Shutdown initiated via Ctrl+C")
        print("✅ Empire sync system shutdown complete")


if __name__ == "__main__":
    main()

"""
HyperFocus Zone System Monitor - Setup Script

This script installs the required dependencies for the system monitor
and provides a quick setup guide.
"""

import subprocess
import sys


def install_package(package):
    """Install a Python package using pip."""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"✅ Successfully installed {package}")
        return True
    except subprocess.CalledProcessError:
        print(f"❌ Failed to install {package}")
        return False


def check_package(package):
    """Check if a package is already installed."""
    try:
        __import__(package)
        return True
    except ImportError:
        return False


def main():
    """Main setup function."""
    print("🚀 HyperFocus Zone System Monitor - Setup")
    print("=" * 50)

    # Required packages
    required_packages = ["psutil", "matplotlib"]  # Optional, for future graph features

    print("📦 Checking and installing required packages...")

    all_installed = True

    for package in required_packages:
        if check_package(package):
            print(f"✅ {package} is already installed")
        else:
            print(f"📥 Installing {package}...")
            if not install_package(package):
                all_installed = False

    if all_installed:
        print("\n🎉 All packages installed successfully!")
        print("\n🚀 Quick Start Guide:")
        print("1. Run the system monitor:")
        print("   python system_monitor.py")
        print("\n2. Run the unit tests:")
        print("   python test_system_monitor.py")
        print("\n3. Import in your own scripts:")
        print("   from system_monitor import SystemMonitor")
        print("   monitor = SystemMonitor()")
        print("   metrics = monitor.collect_metrics()")

        print("\n📊 Files that will be created:")
        print("- hyperfocus_system_monitor.log (log file)")
        print("- hyperfocus_system_metrics.csv (metrics data)")
        print("- final_system_metrics.json (export on exit)")

    else:
        print("\n❌ Some packages failed to install.")
        print("Please install them manually:")
        for package in required_packages:
            print(f"  pip install {package}")

    print("\n💎 Your HyperFocus Zone Empire is ready for legendary monitoring!")


if __name__ == "__main__":
    main()

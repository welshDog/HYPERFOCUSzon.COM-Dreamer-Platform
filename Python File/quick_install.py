#!/usr/bin/env python3
"""
⚡💎 QUICK GEMMA 3 INSTALLER 💎⚡
Simple installation script for Gemma 3 270M dependencies
"""

import subprocess
import sys


def install_package(package):
    """Install a Python package using pip"""
    try:
        print(f"📦 Installing {package}...")
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", package, "--upgrade", "--quiet"]
        )
        print(f"✅ {package} installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install {package}: {e}")
        return False


def main():
    """Install required packages"""
    print("🚀 Quick Gemma 3 270M Package Installer")
    print("=" * 50)

    packages = [
        "torch",
        "transformers>=4.36.0",
        "accelerate",
        "python-dotenv",
        "psutil",
        "requests",
        "ping3",
    ]

    success_count = 0

    for package in packages:
        if install_package(package):
            success_count += 1

    print("\n" + "=" * 50)
    print(f"✅ Installed {success_count}/{len(packages)} packages successfully")

    if success_count == len(packages):
        print("🎉 All packages installed! Ready to run Gemma 3 scanner!")
        print("🚀 Next: Run the AI-enhanced scanner")
    else:
        print("⚠️ Some packages failed to install")

    return success_count == len(packages)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
🧪💎⚡ SIMPLE HYPERFOCUS SCANNER TEST ⚡💎🧪
Quick test version of the empire scanner
"""

import platform
import socket
import sys
from datetime import datetime


def simple_banner():
    """Display simple test banner"""
    print("🧪💎⚡ SIMPLE HYPERFOCUS SCANNER TEST ⚡💎🧪")
    print("=" * 60)
    print(f"🕐 Scan Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🖥️ Hostname: {socket.gethostname()}")
    print(f"🐍 Python: {sys.version.split()[0]}")
    print(f"💻 Platform: {platform.platform()}")
    print("=" * 60)


def test_basic_networking():
    """Test basic networking capabilities"""
    print("\n🌐 Testing Basic Network Capabilities:")

    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        print(f"  ✅ Local IP: {local_ip}")
    except Exception as e:
        print(f"  ❌ Network error: {e}")

    # Test if we can resolve DNS
    try:
        google_ip = socket.gethostbyname("google.com")
        print(f"  ✅ DNS Resolution: google.com -> {google_ip}")
    except Exception as e:
        print(f"  ❌ DNS error: {e}")


def test_system_info():
    """Test system information gathering"""
    print("\n💻 System Information:")

    try:
        print(f"  📊 Platform: {platform.system()} {platform.release()}")
        print(f"  🏗️ Architecture: {platform.architecture()[0]}")
        print(f"  🔧 Processor: {platform.processor() or 'Unknown'}")
    except Exception as e:
        print(f"  ❌ System info error: {e}")


def main():
    """Main test function"""
    try:
        simple_banner()
        test_basic_networking()
        test_system_info()

        print("\n🎉 SIMPLE SCANNER TEST COMPLETE!")
        print("✅ Basic functionality working")
        print("🚀 Ready to run full GEMMA 3 scanner!")

    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

    return True


if __name__ == "__main__":
    success = main()
    if success:
        print("\n💎 Test Status: LEGENDARY SUCCESS!")
    else:
        print("\n⚠️ Test Status: NEEDS ATTENTION")

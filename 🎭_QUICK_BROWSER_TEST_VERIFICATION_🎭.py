#!/usr/bin/env python3
"""
🎭 QUICK BROWSER TEST VERIFICATION SYSTEM 🎭
============================================
Quick verification that our browser testing setup is working!
"""

import sys
import os
from pathlib import Path

def test_python_setup():
    """Test Python environment setup"""
    print("🐍 PYTHON SETUP TEST:")
    print(f"   ✅ Python version: {sys.version}")
    print(f"   ✅ Working directory: {os.getcwd()}")
    print(f"   ✅ Script location: {__file__}")

def test_playwright_installation():
    """Test if Playwright is installed"""
    print("\n🎭 PLAYWRIGHT INSTALLATION TEST:")
    try:
        import playwright
        print(f"   ✅ Playwright version: {playwright.__version__}")

        # Try to import the async API
        from playwright.async_api import async_playwright
        print("   ✅ Playwright async API available")

        return True
    except ImportError as e:
        print(f"   ❌ Playwright not available: {e}")
        print("   💡 Install with: pip install playwright && playwright install chromium")
        return False

def test_directory_structure():
    """Test directory structure"""
    print("\n📁 DIRECTORY STRUCTURE TEST:")

    # Check for screenshots directory
    screenshots_dir = Path("h:/browser_testing_screenshots")
    if screenshots_dir.exists():
        print("   ✅ Screenshots directory exists")
    else:
        print("   ⚠️ Screenshots directory missing - creating it...")
        screenshots_dir.mkdir(exist_ok=True)
        print("   ✅ Screenshots directory created")

    # Check for portal files
    portal_files = [
        "🚀⚡💎_PORTAL_TESTING_ADVENTURES_COMPLETE_SYSTEM_💎⚡🚀.py",
        "🎭⚡💎_LEGENDARY_BROWSER_AUTOMATION_COMPLETE_💎⚡🎭.py",
        "🌌💫🌟_SUPER_HYPER_PORTALS_COLLECTION_MASTER_PAGE_🌟💫🌌.html"
    ]

    for portal_file in portal_files:
        file_path = Path(f"h:/{portal_file}")
        if file_path.exists():
            print(f"   ✅ {portal_file[:30]}... exists")
        else:
            print(f"   ❌ {portal_file[:30]}... missing")

def test_portal_connectivity():
    """Test basic portal connectivity"""
    print("\n🌐 PORTAL CONNECTIVITY TEST:")

    import requests
    import socket

    # Test local services
    services = {
        "localhost:3000": "Grafana Home",
        "localhost:3001": "Grafana Empire",
        "localhost:5000": "Dreamer Portal"
    }

    for service, name in services.items():
        try:
            host, port = service.split(':')
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((host, int(port)))
            sock.close()

            if result == 0:
                print(f"   ✅ {name} ({service}) - ONLINE")
            else:
                print(f"   ⚠️ {name} ({service}) - OFFLINE")
        except Exception as e:
            print(f"   ❌ {name} ({service}) - ERROR: {e}")

async def test_simple_browser_automation():
    """Test simple browser automation"""
    print("\n🎭 SIMPLE BROWSER AUTOMATION TEST:")

    try:
        from playwright.async_api import async_playwright

        async with async_playwright() as p:
            print("   ✅ Playwright context created")

            browser = await p.chromium.launch(headless=True)
            print("   ✅ Chromium browser launched")

            context = await browser.new_context()
            page = await context.new_page()
            print("   ✅ Browser page created")

            # Test simple navigation
            await page.goto("https://google.com")
            title = await page.title()
            print(f"   ✅ Navigation test successful: {title}")

            await browser.close()
            print("   ✅ Browser automation test SUCCESSFUL!")

            return True

    except Exception as e:
        print(f"   ❌ Browser automation test failed: {e}")
        return False

def main():
    """Run all verification tests"""
    print("🎭⚡💎 QUICK BROWSER TEST VERIFICATION SYSTEM 💎⚡🎭")
    print("=" * 60)

    # Run all tests
    test_python_setup()
    playwright_available = test_playwright_installation()
    test_directory_structure()
    test_portal_connectivity()

    if playwright_available:
        # Run async test
        import asyncio
        asyncio.run(test_simple_browser_automation())
    else:
        print("\n🎭 Skipping browser automation test (Playwright not available)")

    print("\n🏆 VERIFICATION COMPLETE!")
    print("🚀 Ready for full browser testing adventure!")

if __name__ == "__main__":
    main()

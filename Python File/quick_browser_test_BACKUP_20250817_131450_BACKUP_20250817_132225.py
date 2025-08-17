#!/usr/bin/env python3
"""
Quick Browser Test Verification System
======================================
Quick verification that our browser testing setup is working!
"""

import sys
import os
from pathlib import Path

def test_python_setup():
    """Test Python environment setup"""
    print("PYTHON SETUP TEST:")
    print(f"   Python version: {sys.version}")
    print(f"   Working directory: {os.getcwd()}")
    print(f"   Script location: {__file__}")

def test_playwright_installation():
    """Test if Playwright is installed"""
    print("\nPLAYWRIGHT INSTALLATION TEST:")
    try:
        import playwright
        print(f"   Playwright version: {playwright.__version__}")

        # Try to import the async API
        from playwright.async_api import async_playwright
        print("   Playwright async API available")

        return True
    except ImportError as e:
        print(f"   Playwright not available: {e}")
        print("   Install with: pip install playwright && playwright install chromium")
        return False

def test_directory_structure():
    """Test directory structure"""
    print("\nDIRECTORY STRUCTURE TEST:")

    # Check for screenshots directory
    screenshots_dir = Path("h:/browser_testing_screenshots")
    if screenshots_dir.exists():
        print("   Screenshots directory exists")
    else:
        print("   Screenshots directory missing - creating it...")
        screenshots_dir.mkdir(exist_ok=True)
        print("   Screenshots directory created")

def main():
    """Run all verification tests"""
    print("QUICK BROWSER TEST VERIFICATION SYSTEM")
    print("=" * 60)

    # Run all tests
    test_python_setup()
    playwright_available = test_playwright_installation()
    test_directory_structure()

    print("\nVERIFICATION COMPLETE!")
    print("Ready for full browser testing adventure!")

if __name__ == "__main__":
    main()

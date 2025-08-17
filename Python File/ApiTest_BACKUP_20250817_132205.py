#!/usr/bin/env python3
"""
🚀 Quick API Test - Check if everything works
"""

import sys
import os

# Add current directory to path
sys.path.append('.')

print("🔍 Testing DREAMER Portal API setup...")

# Test 1: Check if main portal file exists
portal_file = '🌙💎⚡_HYPERFOCUSZONE_DREAMER_PORTAL_⚡💎🌙.py'
if os.path.exists(portal_file):
    print(f"✅ Portal file found: {portal_file}")
else:
    print(f"❌ Portal file missing: {portal_file}")

# Test 2: Try to import Flask
try:
    from flask import Flask
    print("✅ Flask imported successfully")
except ImportError as e:
    print(f"❌ Flask import failed: {e}")

# Test 3: Try to run a simple dream processing
try:
    print("🧠 Testing dream processing...")
    exec(open(portal_file).read())
    
    portal = HyperFocusDreamerPortal()
    test_dream = "I want to build a simple website for my hobby"
    
    result = portal.capture_dream(test_dream, "Test User")
    print(f"✅ Dream processing works! ID: {result.get('dream_id')}")
    
except Exception as e:
    print(f"❌ Dream processing failed: {e}")
    import traceback
    traceback.print_exc()

print("\n🎯 Test complete!")

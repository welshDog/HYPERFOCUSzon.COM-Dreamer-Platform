#!/usr/bin/env python3
# Test script to verify Python execution

print("🌌💎⚡ HYPERFOCUS SYNC EMPIRE - SYSTEM TEST ⚡💎🌌")
print("════════════════════════════════════════════════")
print("✅ Python interpreter is working!")
print("🚀 Ready to launch legendary sync empire!")
print("════════════════════════════════════════════════")

import sys

print(f"🐍 Python version: {sys.version}")
print(f"📍 Current directory: {sys.executable}")

import os

print(f"📁 Working directory: {os.getcwd()}")

# Check if our main files exist
guardian_file = "🌌💎⚡_LEGENDARY_HYPERFOCUS_SYNC_GUARDIAN_V2_⚡💎🌌.py"
dashboard_file = "🌌💎⚡_HYPERFOCUS_SYNC_DASHBOARD_UPGRADE_⚡💎🌌.py"

if os.path.exists(guardian_file):
    print(f"✅ {guardian_file} - Found!")
else:
    print(f"❌ {guardian_file} - Missing!")

if os.path.exists(dashboard_file):
    print(f"✅ {dashboard_file} - Found!")
else:
    print(f"❌ {dashboard_file} - Missing!")

print("\n🏆 System test complete - ready for legendary sync empire!")

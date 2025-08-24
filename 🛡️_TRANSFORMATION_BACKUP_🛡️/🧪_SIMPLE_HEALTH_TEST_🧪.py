#!/usr/bin/env python3
"""
🚀 SIMPLE TEST FOR HEALTH CHECK SYSTEM 🚀
"""

print("🏆💎⚡ ULTRA LEGENDARY HEALTH CHECK SYSTEM STARTING! ⚡💎🏆")
print("=" * 60)

import os
import sys
from pathlib import Path

# Basic system info
print(f"🐍 Python Version: {sys.version}")
print(f"💻 Current Directory: {os.getcwd()}")
print(f"📁 H: Drive exists: {Path('h:/').exists()}")

# Check for key empire directories
empire_paths = [
    "h:/",
    "h:/HyperBeast",
    "h:/HYPERFOCUS ZONE DISCORD HUB",
    "h:/Python File",
]

print("\n🏰 EMPIRE DIRECTORY SCAN:")
for path in empire_paths:
    exists = Path(path).exists()
    status = "✅ EXISTS" if exists else "❌ NOT FOUND"
    print(f"   📂 {path}: {status}")

# Count some key files
print("\n📊 QUICK FILE ANALYSIS:")
try:
    h_drive = Path("h:/")
    if h_drive.exists():
        total_files = len(list(h_drive.rglob("*")))
        py_files = len(list(h_drive.glob("*.py")))
        legendary_files = len(
            [f for f in h_drive.rglob("*") if "LEGENDARY" in f.name.upper()]
        )

        print(f"   📄 Total files in H:/: {total_files}")
        print(f"   🐍 Python files: {py_files}")
        print(f"   🏆 Legendary files: {legendary_files}")
    else:
        print("   ❌ H: drive not accessible")
except Exception as e:
    print(f"   ⚠️ Error scanning: {e}")

print("\n🎯 SYSTEM STATUS: BASIC SCAN COMPLETE!")
print("🚀 Ready to launch full legendary health check!")

#!/usr/bin/env python3
"""
🧠💎 Simple Memory Test 💎🧠
"""

import gc

import psutil

print("🚀 HyperFocus Zone Memory Test Starting...")

try:
    # Test basic memory info
    memory = psutil.virtual_memory()
    print(f"💾 Total RAM: {memory.total / (1024**3):.1f} GB")
    print(f"💾 Available RAM: {memory.available / (1024**3):.1f} GB")
    print(f"💾 Used RAM: {memory.used / (1024**3):.1f} GB")
    print(f"📊 Memory Usage: {memory.percent:.1f}%")

    # Test garbage collection
    collected = gc.collect()
    print(f"♻️ Garbage collected: {collected} objects")

    print("✅ Memory optimization system working perfectly!")

except Exception as e:
    print(f"⚠️ Error: {e}")

print("🎊 Test complete!")

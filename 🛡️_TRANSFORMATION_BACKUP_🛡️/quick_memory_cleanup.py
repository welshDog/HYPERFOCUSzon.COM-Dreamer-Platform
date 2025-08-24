#!/usr/bin/env python3
"""
🧠💎 Quick Memory Cleaner 💎🧠
Simple, reliable memory optimization for HyperFocus Zone
"""

import gc
from pathlib import Path

import psutil


def quick_memory_cleanup():
    """Perform quick memory cleanup and optimization"""
    print("🧠💎 HyperFocus Zone Quick Memory Cleanup 💎🧠")
    print("=" * 50)

    # Get initial memory state
    initial_memory = psutil.virtual_memory()
    print(f"📊 Initial Memory Usage: {initial_memory.percent:.1f}%")
    print(f"💾 Available RAM: {initial_memory.available / (1024**3):.1f} GB")

    # Perform garbage collection
    print("\n♻️ Running garbage collection...")
    collected = gc.collect()
    print(f"✅ Collected {collected} objects")

    # Force collection for all generations
    for gen in range(3):
        additional = gc.collect(gen)
        if additional > 0:
            print(f"♻️ Generation {gen}: {additional} objects")

    # Clean Python cache files in current directory
    print("\n🗑️ Cleaning Python cache files...")
    cache_cleaned = 0
    workspace = Path.cwd()

    for cache_dir in workspace.rglob("__pycache__"):
        try:
            if cache_dir.is_dir():
                for cache_file in cache_dir.iterdir():
                    if cache_file.suffix == ".pyc":
                        cache_file.unlink()
                        cache_cleaned += 1
        except Exception:
            pass

    if cache_cleaned > 0:
        print(f"✅ Cleaned {cache_cleaned} cache files")
    else:
        print("✅ No cache files to clean")

    # Get final memory state
    final_memory = psutil.virtual_memory()
    memory_change = initial_memory.percent - final_memory.percent

    print("\n" + "=" * 50)
    print("🎊 CLEANUP COMPLETE!")
    print(f"📊 Final Memory Usage: {final_memory.percent:.1f}%")
    print(f"💾 Available RAM: {final_memory.available / (1024**3):.1f} GB")

    if memory_change > 0:
        print(f"📈 Memory freed: {memory_change:.1f}%")
    else:
        print("📊 Memory usage optimized")

    # Memory recommendations
    if final_memory.percent > 90:
        print("\n⚠️ HIGH MEMORY USAGE RECOMMENDATIONS:")
        print("   • Close unused browser tabs")
        print("   • Restart VS Code")
        print("   • Close background applications")
        print("   • Consider restarting your computer")
    elif final_memory.percent > 75:
        print("\n💡 MODERATE MEMORY USAGE - RECOMMENDATIONS:")
        print("   • Monitor memory usage")
        print("   • Close unused applications when possible")
    else:
        print("\n✅ EXCELLENT MEMORY USAGE - System running optimally!")

    print("\n🌟 HyperFocus Zone memory optimization complete! 🌟")


if __name__ == "__main__":
    quick_memory_cleanup()

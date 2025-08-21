#!/usr/bin/env python3
"""
🎯 QUICK STATUS CHECKER 🎯
Check current optimization status quickly
"""

import glob
import json
import os
from datetime import datetime

import psutil


def quick_status():
    print("🎯🔥 HYPERFOCUS ZONE QUICK STATUS CHECK 🔥🎯")
    print("=" * 60)
    print(f"⏰ Time: {datetime.now().strftime('%H:%M:%S')}")
    print("")

    # System Status
    print("🖥️ SYSTEM STATUS:")
    try:
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent
        print(f"   ⚡ CPU: {cpu:.1f}%")
        print(f"   🧠 Memory: {memory:.1f}%")
        print(f"   🔢 Processes: {len(psutil.pids())}")
    except:
        print("   ❌ System metrics unavailable")

    print("")

    # File Status
    print("📁 OPTIMIZATION FILES:")
    optimization_files = glob.glob("*optimization*.json")
    boost_files = glob.glob("*boost*.json")
    manual_files = glob.glob("manual_*.json")

    all_files = optimization_files + boost_files + manual_files

    if all_files:
        print(f"   📄 Found {len(all_files)} optimization reports")
        latest = max(all_files, key=os.path.getctime) if all_files else None
        if latest:
            print(f"   📊 Latest: {latest}")

            try:
                with open(latest, "r", encoding="utf-8") as f:
                    data = json.load(f)

                if "overall_progress" in data:
                    print(f"   🎯 Progress: {data['overall_progress']:.1f}%")
                elif "overall_excellence" in data.get("excellence_scores", {}):
                    print(
                        f"   🏆 Excellence: {data['excellence_scores']['overall_excellence']:.1f}%"
                    )
                elif "manual_boost_completed" in data:
                    print(f"   🔧 Manual boost: COMPLETED")

            except Exception as e:
                print(f"   ❌ Report read error: {e}")
    else:
        print("   📊 No optimization reports found")

    print("")

    # Network Quick Check
    print("🌐 NETWORK STATUS:")
    try:
        import socket

        domains = ["hyperfocuszone.com", "www.hyperfocuszone.com"]
        working = 0
        for domain in domains:
            try:
                socket.gethostbyname(domain)
                working += 1
                print(f"   ✅ {domain}: OK")
            except:
                print(f"   ❌ {domain}: FAILED")
        print(f"   📊 Network Score: {(working/len(domains))*100:.0f}%")
    except:
        print("   ❌ Network check failed")

    print("")
    print("🚀 STATUS: HYPERFOCUS ZONE EMPIRE ACTIVE!")
    print("=" * 60)


if __name__ == "__main__":
    quick_status()

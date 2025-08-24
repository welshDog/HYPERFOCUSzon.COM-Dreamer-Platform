#!/usr/bin/env python3
"""
📊🔥💎 REAL-TIME EXCELLENCE TRACKER 💎🔥📊
Live monitoring dashboard for HYPERFOCUS ZONE empire optimization progress
"""

import json
import os
from datetime import datetime


def display_live_status():
    """Display real-time optimization status"""
    print("📊🔥💎 REAL-TIME EXCELLENCE TRACKER 💎🔥📊")
    print("=" * 60)
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("")

    # Check for recent optimization reports
    json_files = [
        f
        for f in os.listdir(".")
        if f.startswith("legendary_optimization_report_") and f.endswith(".json")
    ]

    if json_files:
        latest_report = max(json_files, key=os.path.getctime)
        try:
            with open(latest_report, "r", encoding="utf-8") as f:
                report = json.load(f)

            print(f"📄 Latest Report: {latest_report}")
            print(f"🎯 Overall Progress: {report.get('overall_progress', 0)}%")
            print(f"⚡ Status: {report.get('overall_status', 'UNKNOWN')}")
            print("")

            print("🔥 PHASE STATUS:")
            for phase_name, phase_data in report.get("phases", {}).items():
                status_emoji = "✅" if phase_data.get("status") == "COMPLETED" else "🔧"
                print(
                    f"   {status_emoji} {phase_name.replace('_', ' ').title()}: {phase_data.get('progress', 0):.1f}%"
                )

            print("")
            achievements = report.get("legendary_achievements", [])
            if achievements:
                print("🏆 LEGENDARY ACHIEVEMENTS:")
                for achievement in achievements:
                    print(f"   {achievement}")

        except Exception as e:
            print(f"❌ Error reading report: {e}")

    else:
        print("🔄 No optimization reports found yet...")
        print("✨ Optimization engine may still be starting up!")

    print("")
    print("🌟 Current Empire Status: OPTIMIZING FOR LEGENDARY EXCELLENCE")
    print("💎 Target: 100% HYPERFOCUS ZONE EMPIRE EXCELLENCE")


if __name__ == "__main__":
    display_live_status()

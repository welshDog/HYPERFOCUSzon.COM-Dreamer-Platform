#!/usr/bin/env python3
"""
🔍💎⚡ ULTRA-THINKING BOARDROOM INSTANT FILE ANALYSIS ⚡💎🔍
==========================================================
Rapid file analysis and cleanup recommendations
Following LOOK-THEN-BUILD protocol
==========================================================
"""

import os
import datetime
from pathlib import Path
from collections import defaultdict

def analyze_workspace_files():
    """🔍 Quick workspace analysis"""
    print("🔍💎⚡ ULTRA-THINKING BOARDROOM INSTANT FILE ANALYSIS ⚡💎🔍")
    print("=" * 80)

    base_path = Path("h:/")

    # File counters
    file_stats = defaultdict(int)
    system_files = defaultdict(list)
    large_files = []
    old_reports = []

    # Quick scan
    for file_path in base_path.rglob("*"):
        if file_path.is_file():
            try:
                file_size = file_path.stat().st_size
                modified_time = datetime.datetime.fromtimestamp(file_path.stat().st_mtime)
                file_ext = file_path.suffix.lower()

                # Count by extension
                file_stats[file_ext] += 1
                file_stats["total"] += 1

                # Categorize by function
                file_name_upper = file_path.name.upper()

                # System categorization
                if any(keyword in file_name_upper for keyword in ["DREAMER", "PORTAL"]):
                    system_files["DREAMER_PORTAL"].append(file_path.name)
                elif any(keyword in file_name_upper for keyword in ["BOARDROOM", "ULTRA", "THINKING"]):
                    system_files["ULTRA_BOARDROOM"].append(file_path.name)
                elif any(keyword in file_name_upper for keyword in ["DNS", "DOMAIN", "PROPAGATION"]):
                    system_files["DNS_INFRASTRUCTURE"].append(file_path.name)
                elif any(keyword in file_name_upper for keyword in ["EMPIRE", "HEALTH", "STATUS"]):
                    system_files["EMPIRE_MANAGEMENT"].append(file_path.name)
                elif any(keyword in file_name_upper for keyword in ["CELEBRATION", "LEGENDARY", "HAPPY"]):
                    system_files["CELEBRATION_SYSTEMS"].append(file_path.name)
                elif any(keyword in file_name_upper for keyword in ["MONITOR", "CHECK", "SCAN"]):
                    system_files["MONITORING_TOOLS"].append(file_path.name)

                # Find large files
                if file_size > 100000:  # 100KB
                    large_files.append((file_path.name, file_size))

                # Find old report files
                if any(pattern in file_name_upper for pattern in ["REPORT_2025", "_20250", "LOG_2025"]) and file_ext in [".json", ".txt"]:
                    days_old = (datetime.datetime.now() - modified_time).days
                    if days_old > 3:  # Older than 3 days
                        old_reports.append((file_path.name, days_old))

            except Exception:
                continue

    # Display results
    print("📊 WORKSPACE STATISTICS")
    print("-" * 60)
    print(f"   📁 Total Files: {file_stats['total']}")
    print(f"   🐍 Python Files: {file_stats.get('.py', 0)}")
    print(f"   📄 JSON Files: {file_stats.get('.json', 0)}")
    print(f"   📝 Markdown Files: {file_stats.get('.md', 0)}")
    print(f"   📋 Text Files: {file_stats.get('.txt', 0)}")
    print(f"   💻 PowerShell Files: {file_stats.get('.ps1', 0)}")
    print(f"   🌐 HTML Files: {file_stats.get('.html', 0)}")
    print()

    print("🏷️ SYSTEM CATEGORIZATION")
    print("-" * 60)
    for category, files in system_files.items():
        if files:
            print(f"   🎯 {category}: {len(files)} files")
            # Show first few examples
            for file_name in files[:3]:
                print(f"      - {file_name}")
            if len(files) > 3:
                print(f"      ... and {len(files) - 3} more")
    print()

    print("💾 LARGE FILES (>100KB)")
    print("-" * 60)
    large_files.sort(key=lambda x: x[1], reverse=True)
    for file_name, size in large_files[:10]:
        size_kb = size / 1024
        print(f"   📦 {file_name}: {size_kb:.1f} KB")
    print()

    print("🗑️ OLD REPORT FILES (>3 days)")
    print("-" * 60)
    old_reports.sort(key=lambda x: x[1], reverse=True)
    for file_name, days in old_reports[:10]:
        print(f"   📋 {file_name}: {days} days old")
    print()

    print("🎯 CLEANUP RECOMMENDATIONS")
    print("-" * 60)

    cleanup_potential = 0

    if len(old_reports) > 0:
        cleanup_potential += len(old_reports)
        print(f"   🗑️ Delete {len(old_reports)} old report files")

    # Count duplicate celebration systems
    celebration_count = len(system_files.get("CELEBRATION_SYSTEMS", []))
    if celebration_count > 3:
        print(f"   📦 Consolidate {celebration_count - 1} celebration systems")
        cleanup_potential += (celebration_count - 1)

    # Count monitoring duplicates
    monitoring_count = len(system_files.get("MONITORING_TOOLS", []))
    if monitoring_count > 5:
        print(f"   📦 Consolidate {monitoring_count - 3} monitoring tools")
        cleanup_potential += (monitoring_count - 3)

    if cleanup_potential > 0:
        print(f"   💎 Total cleanup potential: {cleanup_potential} files")
    else:
        print("   ✅ Workspace is well organized!")

    print()

    print("🚀 CURRENTLY ACTIVE SYSTEMS")
    print("-" * 60)

    # Key operational files
    key_systems = [
        "DREAMER_PORTAL_PHASE_1_IMPLEMENTATION.py",
        "DREAMER_PORTAL_PHASE_2_IMPLEMENTATION.py",
        "DREAMER_PORTAL_PHASE_3_IMPLEMENTATION.py",
        "🧠💎⚡_ULTRA_THINKING_BOARDROOM_PROJECT_HEALTH_SCAN_⚡💎🧠.py",
        "EMPIRE_STATUS_DASHBOARD.py",
        "DNS_COMPLETION_STATUS_CHECKER.py",
        "ACCELERATED_DNS_MONITORING_SYSTEM.py"
    ]

    for system in key_systems:
        system_path = base_path / system
        if system_path.exists():
            print(f"   ✅ {system} - ACTIVE")
        else:
            print(f"   ❓ {system} - NOT FOUND")

    print()
    print("=" * 80)

    # Generate quick action plan
    print("🎯 QUICK ACTION PLAN")
    print("-" * 60)

    if len(old_reports) > 5:
        print("   1. 🗑️ Clean up old report files (safe to delete)")

    if celebration_count > 3:
        print("   2. 📦 Consolidate celebration systems into one optimized system")

    if monitoring_count > 5:
        print("   3. 📦 Consolidate monitoring tools")

    print("   4. ✅ Verify all DREAMER Portal phases are operational")
    print("   5. 🔍 Continue DNS monitoring for 95% completion milestone")

    print()
    print("🏆 ULTRA-THINKING BOARDROOM ANALYSIS COMPLETE!")

    return {
        "file_stats": dict(file_stats),
        "system_files": dict(system_files),
        "cleanup_potential": cleanup_potential,
        "old_reports": len(old_reports),
        "large_files": len(large_files)
    }

if __name__ == "__main__":
    result = analyze_workspace_files()

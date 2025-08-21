#!/usr/bin/env python3
"""
📊⚡ REAL-TIME PERFORMANCE MONITOR ⚡📊
Live dashboard showing optimization progress and system metrics
"""

import glob
import json
import os
import time
from datetime import datetime

import psutil


def display_live_performance():
    """Display comprehensive real-time performance metrics"""

    # Clear screen (cross-platform)
    os.system("cls" if os.name == "nt" else "clear")

    print("📊⚡🔥 HYPERFOCUS ZONE LIVE PERFORMANCE DASHBOARD 🔥⚡📊")
    print("=" * 80)
    print(f"🕐 Real-Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("")

    # SYSTEM METRICS
    print("🖥️  SYSTEM PERFORMANCE METRICS:")
    print("-" * 40)
    try:
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage("/")

        print(f"   ⚡ CPU Usage: {cpu_percent:.1f}%")
        print(f"   🧠 Memory Usage: {memory.percent:.1f}%")
        print(f"   💾 Disk Usage: {disk.percent:.1f}%")
        print(f"   🔢 Process Count: {len(psutil.pids())}")

        # Performance assessment
        if cpu_percent < 50 and memory.percent < 70:
            print("   🏆 System Performance: EXCELLENT")
        elif cpu_percent < 70 and memory.percent < 85:
            print("   ⚡ System Performance: GOOD")
        else:
            print("   🔧 System Performance: NEEDS OPTIMIZATION")

    except Exception as e:
        print(f"   ❌ System metrics error: {e}")

    print("")

    # OPTIMIZATION PROGRESS
    print("🎯 OPTIMIZATION PROGRESS:")
    print("-" * 40)

    # Find latest optimization reports
    optimization_files = glob.glob("*optimization_report_*.json")
    boost_files = glob.glob("*boost_report_*.json")
    manual_files = glob.glob("manual_optimization_*.json")

    all_files = optimization_files + boost_files + manual_files

    if all_files:
        latest_file = max(all_files, key=os.path.getctime)
        try:
            with open(latest_file, "r", encoding="utf-8") as f:
                report = json.load(f)

            print(f"   📄 Latest Report: {latest_file}")

            # Check different report types
            if "phases" in report:
                # Optimization report
                overall = report.get("overall_progress", 0)
                print(f"   🎯 Overall Progress: {overall:.1f}%")

                for phase_name, phase_data in report.get("phases", {}).items():
                    status_emoji = (
                        "✅" if phase_data.get("status") == "COMPLETED" else "🔧"
                    )
                    progress = phase_data.get("progress", 0)
                    print(
                        f"   {status_emoji} {phase_name.replace('_', ' ').title()}: {progress:.1f}%"
                    )

            elif "results" in report:
                # Boost report
                ssl_score = report["results"]["ssl_propagation"]["boosted_to"]
                perf_score = report["results"]["performance_protocols"]["boosted_to"]
                overall = report["overall_boost"]["boosted_average"]

                print(f"   🎯 Boost Results: {overall:.1f}%")
                print(f"   ✅ SSL Propagation: {ssl_score:.1f}%")
                print(f"   ✅ Performance Protocols: {perf_score:.1f}%")

            elif "manual_boost_completed" in report:
                # Manual optimization
                print("   🔧 Manual Optimization: COMPLETED")
                print("   ✅ SSL Validation: DONE")
                print("   ✅ Performance Boost: DONE")

        except Exception as e:
            print(f"   ❌ Report reading error: {e}")
    else:
        print("   📊 No optimization reports found")

    print("")

    # NETWORK STATUS
    print("🌐 NETWORK & SSL STATUS:")
    print("-" * 40)

    import socket
    import ssl as ssl_module

    domains = [
        "hyperfocuszone.com",
        "www.hyperfocuszone.com",
        "support.hyperfocuszone.com",
    ]

    for domain in domains:
        try:
            # DNS check
            ip = socket.gethostbyname(domain)
            print(f"   ✅ {domain}: DNS OK ({ip})")

            # Quick SSL check
            try:
                context = ssl_module.create_default_context()
                with socket.create_connection((domain, 443), timeout=5) as sock:
                    with context.wrap_socket(sock, server_hostname=domain) as ssock:
                        cert = ssock.getpeercert()
                        print(f"      🔒 SSL: Valid certificate")
            except:
                print(f"      ⚠️  SSL: Certificate check failed")

        except Exception as e:
            print(f"   ❌ {domain}: DNS/SSL Failed")

    print("")

    # ACTION STATUS
    print("🚀 CURRENT ACTION STATUS:")
    print("-" * 40)

    # Check for running processes
    python_processes = 0
    optimization_processes = 0

    for proc in psutil.process_iter(["name", "cmdline"]):
        try:
            if "python" in proc.info["name"].lower():
                python_processes += 1
                if proc.info["cmdline"]:
                    cmdline = " ".join(proc.info["cmdline"]).lower()
                    if any(
                        word in cmdline
                        for word in ["optimization", "boost", "performance", "ssl"]
                    ):
                        optimization_processes += 1
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    print(f"   🐍 Python Processes: {python_processes}")
    print(f"   ⚡ Optimization Processes: {optimization_processes}")

    if optimization_processes > 0:
        print("   🔥 Status: OPTIMIZATION IN PROGRESS")
    else:
        print("   ✅ Status: READY FOR NEW ACTIONS")

    print("")
    print("🎯 NEXT ACTIONS RECOMMENDED:")
    print("-" * 40)
    print("   ⚡ Continue monitoring optimization progress")
    print("   🔧 Run additional performance boosts if needed")
    print("   📊 Check real-time metrics for improvements")
    print("   🚀 Execute strategic plan implementations")

    print("")
    print("=" * 80)
    print("💎 Press Ctrl+C to exit | Refreshing every 5 seconds...")


def main():
    """Main monitoring loop"""
    try:
        while True:
            display_live_performance()
            time.sleep(5)  # Refresh every 5 seconds
    except KeyboardInterrupt:
        print(
            "\n\n🎉 Live monitoring stopped. HYPERFOCUS ZONE EMPIRE STATUS EXCELLENT! 🎉"
        )


if __name__ == "__main__":
    main()

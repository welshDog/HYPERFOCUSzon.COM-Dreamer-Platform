#!/usr/bin/env python3
"""
🔥💎⚡ IMMEDIATE HEAT DIAGNOSTIC SYSTEM ⚡💎🔥
Quick system analysis to determine why empire is running hot
Following BROski LOOK-THEN-BUILD System protocols
"""

import time
from datetime import datetime

import psutil

print("🔥💎⚡ IMMEDIATE HEAT DIAGNOSTIC - EMPIRE RUNNING HOT ⚡💎🔥")
print("=" * 70)
print(f"🕐 Diagnostic Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print()


def check_cpu_temperature():
    """🌡️ Check CPU temperature and usage"""
    print("🌡️ CPU THERMAL ANALYSIS:")
    print("-" * 30)

    try:
        # CPU usage
        cpu_percent = psutil.cpu_percent(interval=1)
        print(f"   CPU Usage: {cpu_percent}%", end="")

        if cpu_percent > 80:
            print(" 🔥 HOT - HIGH CPU USAGE!")
        elif cpu_percent > 60:
            print(" ⚠️ WARM - Elevated usage")
        else:
            print(" ✅ COOL")

        # CPU cores
        cpu_per_core = psutil.cpu_percent(percpu=True, interval=1)
        print(f"   CPU Cores: {len(cpu_per_core)} cores")

        hot_cores = [i for i, usage in enumerate(cpu_per_core) if usage > 80]
        if hot_cores:
            print(f"   🔥 HOT CORES: {hot_cores} (>80% usage)")

        # CPU frequency
        try:
            cpu_freq = psutil.cpu_freq()
            if cpu_freq:
                print(f"   CPU Frequency: {cpu_freq.current:.0f} MHz")
                if cpu_freq.current > cpu_freq.max * 0.9:
                    print("   🔥 CPU RUNNING AT HIGH FREQUENCY")
        except:
            print("   ⚠️ CPU frequency info unavailable")

        # Try to get temperature (platform dependent)
        try:
            if hasattr(psutil, "sensors_temperatures"):
                temps = psutil.sensors_temperatures()
                if temps:
                    for name, entries in temps.items():
                        for entry in entries:
                            temp = entry.current
                            print(f"   🌡️ {name}: {temp:.1f}°C", end="")
                            if temp > 80:
                                print(" 🔥 OVERHEATING!")
                            elif temp > 70:
                                print(" ⚠️ HOT")
                            else:
                                print(" ✅ NORMAL")
                else:
                    print("   ⚠️ Temperature sensors not accessible")
            else:
                print("   ⚠️ Temperature monitoring not available on this platform")
        except Exception as e:
            print(f"   ⚠️ Temperature check failed: {e}")

    except Exception as e:
        print(f"   ❌ CPU analysis failed: {e}")


def check_memory_pressure():
    """🧠 Check memory usage and pressure"""
    print("\n🧠 MEMORY PRESSURE ANALYSIS:")
    print("-" * 30)

    try:
        memory = psutil.virtual_memory()
        swap = psutil.swap_memory()

        print(f"   RAM Usage: {memory.percent:.1f}%", end="")
        if memory.percent > 90:
            print(" 🔥 CRITICAL - Very high memory usage!")
        elif memory.percent > 80:
            print(" ⚠️ HIGH - Memory pressure detected")
        else:
            print(" ✅ NORMAL")

        print(f"   RAM Available: {memory.available / (1024**3):.1f} GB")
        print(f"   RAM Total: {memory.total / (1024**3):.1f} GB")

        print(f"   Swap Usage: {swap.percent:.1f}%", end="")
        if swap.percent > 50:
            print(" 🔥 HIGH SWAP USAGE - Memory bottleneck!")
        elif swap.percent > 25:
            print(" ⚠️ Elevated swap usage")
        else:
            print(" ✅ NORMAL")

    except Exception as e:
        print(f"   ❌ Memory analysis failed: {e}")


def check_disk_activity():
    """💽 Check disk I/O and space"""
    print("\n💽 DISK ACTIVITY ANALYSIS:")
    print("-" * 30)

    try:
        # Disk usage
        disk = psutil.disk_usage("/")
        print(f"   Disk Usage: {(disk.used / disk.total) * 100:.1f}%", end="")

        disk_percent = (disk.used / disk.total) * 100
        if disk_percent > 95:
            print(" 🔥 CRITICAL - Disk almost full!")
        elif disk_percent > 85:
            print(" ⚠️ HIGH - Low disk space")
        else:
            print(" ✅ NORMAL")

        print(f"   Disk Free: {disk.free / (1024**3):.1f} GB")

        # Disk I/O
        disk_io_before = psutil.disk_io_counters()
        time.sleep(1)
        disk_io_after = psutil.disk_io_counters()

        if disk_io_before and disk_io_after:
            read_rate = (disk_io_after.read_bytes - disk_io_before.read_bytes) / (
                1024**2
            )
            write_rate = (disk_io_after.write_bytes - disk_io_before.write_bytes) / (
                1024**2
            )

            print(f"   Disk Read Rate: {read_rate:.1f} MB/s")
            print(f"   Disk Write Rate: {write_rate:.1f} MB/s")

            if read_rate > 100 or write_rate > 100:
                print("   🔥 HIGH DISK I/O - Heavy disk activity!")
            elif read_rate > 50 or write_rate > 50:
                print("   ⚠️ Elevated disk activity")

    except Exception as e:
        print(f"   ❌ Disk analysis failed: {e}")


def check_running_processes():
    """🔄 Check for resource-heavy processes"""
    print("\n🔄 RESOURCE-HEAVY PROCESSES:")
    print("-" * 30)

    try:
        processes = []
        for proc in psutil.process_iter(
            ["pid", "name", "cpu_percent", "memory_percent"]
        ):
            try:
                proc_info = proc.info
                if proc_info["cpu_percent"] > 10 or proc_info["memory_percent"] > 5:
                    processes.append(proc_info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass

        # Sort by CPU usage
        processes.sort(key=lambda x: x["cpu_percent"], reverse=True)

        print("   Top CPU consumers:")
        for i, proc in enumerate(processes[:5]):
            cpu = proc["cpu_percent"]
            mem = proc["memory_percent"]
            name = proc["name"]
            print(f"   {i+1}. {name}: CPU {cpu:.1f}%, RAM {mem:.1f}%", end="")

            if cpu > 50:
                print(" 🔥 HIGH CPU!")
            elif cpu > 25:
                print(" ⚠️ Elevated CPU")
            else:
                print("")

        # Check for specific empire processes
        empire_processes = []
        for proc in psutil.process_iter(["pid", "name", "cmdline"]):
            try:
                proc_info = proc.info
                name = proc_info["name"].lower()
                cmdline = (
                    " ".join(proc_info["cmdline"]).lower()
                    if proc_info["cmdline"]
                    else ""
                )

                if any(
                    keyword in name or keyword in cmdline
                    for keyword in [
                        "python",
                        "node",
                        "discord",
                        "broski",
                        "bot",
                        "empire",
                        "hyperfocus",
                    ]
                ):
                    empire_processes.append(proc_info["name"])
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass

        if empire_processes:
            print(f"\n   🏰 Empire processes detected: {len(empire_processes)}")
            for proc in set(empire_processes[:10]):  # Show unique processes, max 10
                print(f"      • {proc}")

    except Exception as e:
        print(f"   ❌ Process analysis failed: {e}")


def check_network_activity():
    """🌐 Check network I/O"""
    print("\n🌐 NETWORK ACTIVITY ANALYSIS:")
    print("-" * 30)

    try:
        net_io_before = psutil.net_io_counters()
        time.sleep(1)
        net_io_after = psutil.net_io_counters()

        if net_io_before and net_io_after:
            bytes_sent_rate = (net_io_after.bytes_sent - net_io_before.bytes_sent) / (
                1024**2
            )
            bytes_recv_rate = (net_io_after.bytes_recv - net_io_before.bytes_recv) / (
                1024**2
            )

            print(f"   Upload Rate: {bytes_sent_rate:.2f} MB/s")
            print(f"   Download Rate: {bytes_recv_rate:.2f} MB/s")

            if bytes_sent_rate > 10 or bytes_recv_rate > 10:
                print("   🔥 HIGH NETWORK ACTIVITY!")
            elif bytes_sent_rate > 1 or bytes_recv_rate > 1:
                print("   ⚠️ Elevated network activity")

        # Check connections
        connections = psutil.net_connections()
        active_connections = [c for c in connections if c.status == "ESTABLISHED"]
        print(f"   Active Connections: {len(active_connections)}")

        if len(active_connections) > 100:
            print("   🔥 VERY HIGH CONNECTION COUNT!")
        elif len(active_connections) > 50:
            print("   ⚠️ High connection count")

    except Exception as e:
        print(f"   ❌ Network analysis failed: {e}")


def generate_recommendations():
    """💡 Generate heat reduction recommendations"""
    print("\n💡 HEAT REDUCTION RECOMMENDATIONS:")
    print("-" * 40)

    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()

    recommendations = []

    if cpu_percent > 80:
        recommendations.append(
            "🔥 High CPU: Close unnecessary applications and processes"
        )
        recommendations.append("⚡ Check for runaway Python/Node processes")
        recommendations.append("🤖 Consider stopping background bots temporarily")

    if memory.percent > 80:
        recommendations.append("🧠 High Memory: Close memory-intensive applications")
        recommendations.append("💾 Consider restarting to clear memory leaks")

    disk = psutil.disk_usage("/")
    if (disk.used / disk.total) * 100 > 85:
        recommendations.append("💽 Low Disk Space: Clean up temporary files and logs")
        recommendations.append("🗑️ Remove old memory crystals and diagnostic reports")

    # General recommendations
    recommendations.extend(
        [
            "❄️ Ensure good ventilation around your computer",
            "🔄 Restart empire services one by one to identify culprit",
            "📊 Monitor for 5-10 minutes to identify patterns",
            "🚀 Consider running fewer concurrent empire systems",
        ]
    )

    for i, rec in enumerate(recommendations, 1):
        print(f"   {i}. {rec}")


def main():
    """🎯 Execute immediate heat diagnostic"""
    try:
        check_cpu_temperature()
        check_memory_pressure()
        check_disk_activity()
        check_running_processes()
        check_network_activity()
        generate_recommendations()

        print("\n" + "=" * 70)
        print("🎯 DIAGNOSTIC COMPLETE")
        print(f"📋 Report generated at: {datetime.now().strftime('%H:%M:%S')}")
        print("💎 Use recommendations above to cool down the empire!")
        print("⚡ BROski System Status: DIAGNOSTIC COMPLETE")

    except Exception as e:
        print(f"❌ Diagnostic failed: {e}")
        print("🔧 Try running individual system checks manually")


if __name__ == "__main__":
    main()

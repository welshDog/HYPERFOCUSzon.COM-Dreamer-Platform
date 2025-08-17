#!/usr/bin/env python3
"""
⚡💎🏥 EMPIRE HEALTH OPTIMIZER 🏥💎⚡
🌟 HYPERFOCUS ZONE PEAK PERFORMANCE ENHANCEMENT SYSTEM 🌟

Advanced health optimization and monitoring system for maximum empire performance.
"""

import json
import logging
import os
import platform
import time
from datetime import datetime

import psutil


class EmpireHealthOptimizer:
    """🚀 Advanced system optimizer for peak empire performance"""

    def __init__(self):
        self.optimization_report = {
            "timestamp": datetime.now().isoformat(),
            "optimizations_applied": [],
            "system_improvements": {},
            "performance_gains": {},
        }

        # Configure logging
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[
                logging.FileHandler("empire_optimization.log"),
                logging.StreamHandler(),
            ],
        )

    def print_banner(self):
        """🎯 Display optimization banner"""
        banner = """
        ⚡💎🏥═══════════════════════════════════════════════════════════════🏥💎⚡
        ║                                                                     ║
        ║        🌟 EMPIRE HEALTH OPTIMIZER v1.0 🌟                         ║
        ║           HYPERFOCUS ZONE PERFORMANCE ENHANCEMENT                   ║
        ║                                                                     ║
        ║  🚀 Optimizing System for Maximum Empire Performance 🚀            ║
        ║                                                                     ║
        ⚡💎🏥═══════════════════════════════════════════════════════════════🏥💎⚡
        """
        print(banner)

    def analyze_memory_usage(self):
        """🧠 Analyze and optimize memory usage"""
        print("\n🧠 MEMORY OPTIMIZATION ANALYSIS")
        print("=" * 50)

        memory = psutil.virtual_memory()
        memory_percent = memory.percent

        print(f"📊 Current Memory Usage: {memory_percent:.1f}%")
        print(f"💾 Total Memory: {memory.total / (1024**3):.2f} GB")
        print(f"🔓 Available Memory: {memory.available / (1024**3):.2f} GB")
        print(f"🔒 Used Memory: {memory.used / (1024**3):.2f} GB")

        recommendations = []

        if memory_percent > 90:
            recommendations.extend(
                [
                    "🚨 CRITICAL: Memory usage extremely high",
                    "💡 Close unnecessary applications immediately",
                    "💡 Consider restarting high-memory processes",
                    "💡 Add more RAM if this is persistent",
                ]
            )
        elif memory_percent > 80:
            recommendations.extend(
                [
                    "⚠️ WARNING: Memory usage high",
                    "💡 Close browser tabs and unused applications",
                    "💡 Check for memory leaks in running processes",
                ]
            )
        elif memory_percent > 70:
            recommendations.extend(
                [
                    "📈 ADVISORY: Monitor memory usage",
                    "💡 Consider optimizing startup programs",
                ]
            )
        else:
            recommendations.append("✅ Memory usage is healthy")

        # Get top memory consuming processes
        print(f"\n🔍 TOP MEMORY CONSUMERS:")
        processes = []
        for proc in psutil.process_iter(["pid", "name", "memory_percent"]):
            try:
                if (
                    proc.info["memory_percent"] > 1.0
                ):  # Only show processes using >1% memory
                    processes.append(proc.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass

        # Sort by memory usage
        processes.sort(key=lambda x: x["memory_percent"], reverse=True)

        for i, proc in enumerate(processes[:10], 1):
            print(
                f"  {i}. {proc['name']} (PID: {proc['pid']}) - {proc['memory_percent']:.1f}%"
            )

        for rec in recommendations:
            print(f"  {rec}")

        self.optimization_report["system_improvements"]["memory"] = {
            "usage_percent": memory_percent,
            "recommendations": recommendations,
            "top_processes": processes[:5],
        }

        return recommendations

    def analyze_cpu_usage(self):
        """⚡ Analyze and optimize CPU usage"""
        print("\n⚡ CPU OPTIMIZATION ANALYSIS")
        print("=" * 50)

        # Get CPU usage over time for accuracy
        cpu_percent = psutil.cpu_percent(interval=2)
        cpu_count = psutil.cpu_count(logical=True)
        cpu_freq = psutil.cpu_freq()

        print(f"🖥️  CPU Usage: {cpu_percent:.1f}%")
        print(f"🔢 CPU Cores: {cpu_count}")
        if cpu_freq:
            print(
                f"⚡ CPU Frequency: {cpu_freq.current:.0f} MHz (Max: {cpu_freq.max:.0f} MHz)"
            )

        recommendations = []

        if cpu_percent > 90:
            recommendations.extend(
                [
                    "🚨 CRITICAL: CPU usage extremely high",
                    "💡 Identify and terminate unnecessary processes",
                    "💡 Check for infinite loops or runaway processes",
                ]
            )
        elif cpu_percent > 70:
            recommendations.extend(
                [
                    "⚠️ WARNING: CPU usage high",
                    "💡 Close resource-intensive applications",
                    "💡 Consider process scheduling optimization",
                ]
            )
        elif cpu_percent > 50:
            recommendations.extend(
                ["📈 ADVISORY: Monitor CPU usage", "💡 Optimize background tasks"]
            )
        else:
            recommendations.append("✅ CPU usage is healthy")

        # Get top CPU consuming processes
        print(f"\n🔍 TOP CPU CONSUMERS:")
        processes = []
        for proc in psutil.process_iter(["pid", "name", "cpu_percent"]):
            try:
                if proc.info["cpu_percent"] > 1.0:
                    processes.append(proc.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass

        processes.sort(key=lambda x: x["cpu_percent"], reverse=True)

        for i, proc in enumerate(processes[:10], 1):
            print(
                f"  {i}. {proc['name']} (PID: {proc['pid']}) - {proc['cpu_percent']:.1f}%"
            )

        for rec in recommendations:
            print(f"  {rec}")

        self.optimization_report["system_improvements"]["cpu"] = {
            "usage_percent": cpu_percent,
            "core_count": cpu_count,
            "recommendations": recommendations,
            "top_processes": processes[:5],
        }

        return recommendations

    def analyze_disk_usage(self):
        """💾 Analyze and optimize disk usage"""
        print("\n💾 DISK OPTIMIZATION ANALYSIS")
        print("=" * 50)

        # Get disk usage for main drive
        if platform.system() == "Windows":
            disk_usage = psutil.disk_usage("C:")
            drive = "C:"
        else:
            disk_usage = psutil.disk_usage("/")
            drive = "/"

        total_gb = disk_usage.total / (1024**3)
        used_gb = disk_usage.used / (1024**3)
        free_gb = disk_usage.free / (1024**3)
        used_percent = (disk_usage.used / disk_usage.total) * 100

        print(f"💿 Drive {drive}")
        print(f"📊 Disk Usage: {used_percent:.1f}%")
        print(f"📦 Total Space: {total_gb:.2f} GB")
        print(f"🔓 Free Space: {free_gb:.2f} GB")
        print(f"🔒 Used Space: {used_gb:.2f} GB")

        recommendations = []

        if used_percent > 95:
            recommendations.extend(
                [
                    "🚨 CRITICAL: Disk almost full",
                    "💡 Delete unnecessary files immediately",
                    "💡 Move large files to external storage",
                    "💡 Clear temporary files and caches",
                ]
            )
        elif used_percent > 85:
            recommendations.extend(
                [
                    "⚠️ WARNING: Disk usage high",
                    "💡 Run disk cleanup utilities",
                    "💡 Uninstall unused programs",
                    "💡 Clear browser caches",
                ]
            )
        elif used_percent > 70:
            recommendations.extend(
                ["📈 ADVISORY: Monitor disk usage", "💡 Regular cleanup recommended"]
            )
        else:
            recommendations.append("✅ Disk usage is healthy")

        # Check for disk I/O
        disk_io = psutil.disk_io_counters()
        if disk_io:
            print(f"📤 Bytes Written: {disk_io.write_bytes / (1024**3):.2f} GB")
            print(f"📥 Bytes Read: {disk_io.read_bytes / (1024**3):.2f} GB")

        for rec in recommendations:
            print(f"  {rec}")

        self.optimization_report["system_improvements"]["disk"] = {
            "usage_percent": used_percent,
            "free_gb": free_gb,
            "total_gb": total_gb,
            "recommendations": recommendations,
        }

        return recommendations

    def analyze_network_performance(self):
        """🌐 Analyze network performance"""
        print("\n🌐 NETWORK PERFORMANCE ANALYSIS")
        print("=" * 50)

        network_io = psutil.net_io_counters()

        print(f"📤 Total Bytes Sent: {network_io.bytes_sent / (1024**3):.2f} GB")
        print(f"📥 Total Bytes Received: {network_io.bytes_recv / (1024**3):.2f} GB")
        print(f"📦 Packets Sent: {network_io.packets_sent:,}")
        print(f"📦 Packets Received: {network_io.packets_recv:,}")

        # Calculate error rates
        total_packets = network_io.packets_sent + network_io.packets_recv
        total_errors = network_io.errin + network_io.errout
        total_drops = network_io.dropin + network_io.dropout

        if total_packets > 0:
            error_rate = (total_errors / total_packets) * 100
            drop_rate = (total_drops / total_packets) * 100

            print(f"❌ Network Errors: {total_errors} ({error_rate:.4f}%)")
            print(f"📉 Dropped Packets: {total_drops} ({drop_rate:.4f}%)")

            recommendations = []

            if error_rate > 1.0 or drop_rate > 1.0:
                recommendations.extend(
                    [
                        "🚨 CRITICAL: High network error/drop rate",
                        "💡 Check network cables and connections",
                        "💡 Update network drivers",
                        "💡 Check router/switch health",
                    ]
                )
            elif error_rate > 0.1 or drop_rate > 0.1:
                recommendations.extend(
                    [
                        "⚠️ WARNING: Moderate network issues",
                        "💡 Monitor network stability",
                        "💡 Consider network diagnostics",
                    ]
                )
            else:
                recommendations.append("✅ Network performance is healthy")
        else:
            recommendations = ["📊 Insufficient network data for analysis"]

        for rec in recommendations:
            print(f"  {rec}")

        self.optimization_report["system_improvements"]["network"] = {
            "error_rate": error_rate if total_packets > 0 else 0,
            "drop_rate": drop_rate if total_packets > 0 else 0,
            "recommendations": recommendations,
        }

        return recommendations

    def optimize_windows_services(self):
        """🔧 Optimize Windows services for better performance"""
        if platform.system() != "Windows":
            print("\n⚠️ Service optimization only available on Windows")
            return []

        print("\n🔧 WINDOWS SERVICE OPTIMIZATION")
        print("=" * 50)

        # List of services that can often be safely disabled for better performance
        optional_services = [
            "Fax",
            "Windows Search",  # If not using file search
            "Print Spooler",  # If no printers
            "Windows Error Reporting Service",
            "Remote Registry",
            "Secondary Logon",
            "Tablet PC Input Service",
        ]

        recommendations = [
            "💡 Review and disable unnecessary Windows services",
            "💡 Set non-critical services to 'Manual' start",
            "💡 Keep security services (Windows Defender, Firewall) enabled",
            "💡 Use Task Manager > Services tab to manage services",
        ]

        print("🔧 Service Optimization Recommendations:")
        for rec in recommendations:
            print(f"  {rec}")

        print(f"\n📋 Optional services to consider reviewing:")
        for service in optional_services:
            print(f"  • {service}")

        self.optimization_report["optimizations_applied"].append(
            "Windows service review recommended"
        )

        return recommendations

    def clear_temporary_files(self):
        """🧹 Clear temporary files and caches"""
        print("\n🧹 TEMPORARY FILE CLEANUP")
        print("=" * 50)

        temp_paths = []

        if platform.system() == "Windows":
            temp_paths = [
                os.path.expandvars("%TEMP%"),
                os.path.expandvars("%TMP%"),
                os.path.expandvars("%LOCALAPPDATA%\\Temp"),
                "C:\\Windows\\Temp",
                os.path.expandvars("%LOCALAPPDATA%\\Microsoft\\Windows\\INetCache"),
                os.path.expandvars("%APPDATA%\\Microsoft\\Windows\\Recent"),
            ]
        else:
            temp_paths = ["/tmp", "/var/tmp", os.path.expanduser("~/.cache")]

        total_cleared = 0
        cleared_locations = []

        for temp_path in temp_paths:
            if os.path.exists(temp_path):
                try:
                    # Calculate size before cleanup
                    size_before = sum(
                        os.path.getsize(os.path.join(dirpath, filename))
                        for dirpath, dirnames, filenames in os.walk(temp_path)
                        for filename in filenames
                    )

                    # Attempt to clear safely (only files older than 1 day)
                    files_removed = 0
                    current_time = time.time()

                    for root, dirs, files in os.walk(temp_path):
                        for file in files:
                            file_path = os.path.join(root, file)
                            try:
                                # Only remove files older than 24 hours
                                if (
                                    os.path.getmtime(file_path) < current_time - 86400
                                ):  # 24 hours
                                    os.remove(file_path)
                                    files_removed += 1
                            except (OSError, PermissionError):
                                continue  # Skip files that can't be deleted

                    if files_removed > 0:
                        cleared_locations.append(f"{temp_path}: {files_removed} files")
                        print(f"  🗑️ Cleared {files_removed} files from {temp_path}")

                except (OSError, PermissionError):
                    print(f"  ⚠️ Cannot access {temp_path} (permission denied)")

        if cleared_locations:
            print(f"\n✅ Cleanup completed:")
            for location in cleared_locations:
                print(f"  • {location}")
            self.optimization_report["optimizations_applied"].append(
                "Temporary file cleanup"
            )
        else:
            print("  📝 No old temporary files found to clean")

        # Additional cleanup recommendations
        recommendations = [
            "💡 Run Windows Disk Cleanup utility",
            "💡 Clear browser caches and downloads",
            "💡 Empty Recycle Bin",
            "💡 Clear Windows Update cache if needed",
            "💡 Use CCleaner or similar tools for deep cleanup",
        ]

        print(f"\n💡 Additional cleanup recommendations:")
        for rec in recommendations:
            print(f"  {rec}")

        return recommendations

    def optimize_startup_programs(self):
        """🚀 Optimize startup programs"""
        print("\n🚀 STARTUP OPTIMIZATION")
        print("=" * 50)

        recommendations = [
            "💡 Disable unnecessary startup programs",
            "💡 Use Task Manager > Startup tab to manage",
            "💡 Keep antivirus and essential security software",
            "💡 Delay non-critical program startups",
            "💡 Use 'msconfig' for advanced startup management",
        ]

        print("🚀 Startup Optimization Recommendations:")
        for rec in recommendations:
            print(f"  {rec}")

        # Common startup programs that can often be disabled
        common_disable_candidates = [
            "Adobe updaters",
            "Java update schedulers",
            "Office applications (unless needed daily)",
            "Media players",
            "Chat applications (can be started manually)",
            "Gaming software (Steam, etc.)",
            "Printer software",
        ]

        print(f"\n📋 Common startup programs to consider disabling:")
        for candidate in common_disable_candidates:
            print(f"  • {candidate}")

        self.optimization_report["optimizations_applied"].append(
            "Startup optimization recommendations provided"
        )

        return recommendations

    def run_comprehensive_optimization(self):
        """🚀 Run comprehensive system optimization"""
        self.print_banner()

        print("🔧 Starting comprehensive empire system optimization...")
        print("=" * 70)

        # Collect all recommendations
        all_recommendations = []

        # 1. Memory optimization
        memory_recs = self.analyze_memory_usage()
        all_recommendations.extend(memory_recs)

        # 2. CPU optimization
        cpu_recs = self.analyze_cpu_usage()
        all_recommendations.extend(cpu_recs)

        # 3. Disk optimization
        disk_recs = self.analyze_disk_usage()
        all_recommendations.extend(disk_recs)

        # 4. Network optimization
        network_recs = self.analyze_network_performance()
        all_recommendations.extend(network_recs)

        # 5. Service optimization
        service_recs = self.optimize_windows_services()
        all_recommendations.extend(service_recs)

        # 6. Temporary file cleanup
        cleanup_recs = self.clear_temporary_files()
        all_recommendations.extend(cleanup_recs)

        # 7. Startup optimization
        startup_recs = self.optimize_startup_programs()
        all_recommendations.extend(startup_recs)

        # Generate final optimization summary
        self.generate_optimization_summary(all_recommendations)

        # Save optimization report
        self.save_optimization_report()

        print("\n" + "=" * 70)
        print("🎉 Comprehensive empire optimization completed!")
        print("⚡ Your HyperFocus Zone is now optimized for peak performance! ⚡")

        return self.optimization_report

    def generate_optimization_summary(self, all_recommendations):
        """📊 Generate optimization summary"""
        print("\n🏆 OPTIMIZATION SUMMARY")
        print("=" * 50)

        # Count recommendation types
        critical_count = sum(1 for rec in all_recommendations if "CRITICAL" in rec)
        warning_count = sum(1 for rec in all_recommendations if "WARNING" in rec)
        advisory_count = sum(1 for rec in all_recommendations if "ADVISORY" in rec)

        print(f"🚨 Critical Issues: {critical_count}")
        print(f"⚠️ Warnings: {warning_count}")
        print(f"📈 Advisories: {advisory_count}")

        # Priority actions
        print(f"\n🎯 PRIORITY ACTIONS:")
        priority_actions = [
            rec for rec in all_recommendations if "CRITICAL" in rec or "WARNING" in rec
        ]

        if priority_actions:
            for i, action in enumerate(priority_actions[:5], 1):
                print(f"  {i}. {action}")
        else:
            print("  ✅ No critical actions required - system is running well!")

        # Performance score calculation
        memory_usage = self.optimization_report["system_improvements"]["memory"][
            "usage_percent"
        ]
        cpu_usage = self.optimization_report["system_improvements"]["cpu"][
            "usage_percent"
        ]
        disk_usage = self.optimization_report["system_improvements"]["disk"][
            "usage_percent"
        ]

        # Calculate overall performance score (0-100)
        memory_score = max(0, 100 - memory_usage)
        cpu_score = max(0, 100 - cpu_usage)
        disk_score = max(0, 100 - disk_usage)

        overall_score = (memory_score + cpu_score + disk_score) / 3

        print(f"\n📊 EMPIRE PERFORMANCE SCORE: {overall_score:.1f}/100")

        if overall_score >= 90:
            print("🏆 LEGENDARY STATUS - Peak performance achieved!")
        elif overall_score >= 80:
            print("💎 EXCELLENT - Very good performance")
        elif overall_score >= 70:
            print("⚡ GOOD - Solid performance with room for improvement")
        elif overall_score >= 60:
            print("📈 FAIR - Moderate performance, optimization recommended")
        else:
            print("🔧 NEEDS OPTIMIZATION - Significant improvements possible")

        self.optimization_report["performance_score"] = overall_score

    def save_optimization_report(self):
        """💾 Save optimization report"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"empire_optimization_report_{timestamp}.json"

        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(self.optimization_report, f, indent=2, default=str)

            print(f"\n📄 Optimization report saved to: {filename}")
        except Exception as e:
            print(f"❌ Error saving report: {e}")


def main():
    """🚀 Main optimization execution"""
    try:
        optimizer = EmpireHealthOptimizer()
        optimization_report = optimizer.run_comprehensive_optimization()

        print(f"\n🌟 Empire optimization completed successfully!")
        print(
            f"📊 Performance Score: {optimization_report.get('performance_score', 'Unknown'):.1f}/100"
        )

        return optimization_report

    except KeyboardInterrupt:
        print("\n⚠️ Optimization interrupted by user")
        return None
    except Exception as e:
        print(f"❌ Error during optimization: {e}")
        return None


if __name__ == "__main__":
    main()

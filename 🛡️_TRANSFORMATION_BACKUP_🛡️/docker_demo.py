#!/usr/bin/env python3
"""
Simple demo script for the system monitor in Docker
"""

from system_monitor import SystemMonitor


def main():
    print("🚀 Starting HyperFocus Zone System Monitor Demo in Docker...")

    # Create monitor instance
    monitor = SystemMonitor()

    # Show quick system summary
    print("📋 System Overview:")
    summary = monitor.get_system_summary()
    print(f"CPU: {summary['system_overview']['cpu_percent']:.1f}%")
    print(f"Memory: {summary['system_overview']['memory_percent']:.1f}%")
    print(f"Disk: {summary['system_overview']['disk_usage_percent']:.1f}%")
    print(f"Processes: {summary['system_overview']['process_count']}")

    # Start monitoring briefly
    print("📊 Starting monitoring for 10 seconds...")
    monitor.start_monitoring(interval=2)

    # Let it run for a bit
    import time

    time.sleep(10)

    # Stop monitoring
    monitor.stop_monitoring()

    # Show collected metrics
    print(f"✅ Demo completed! Collected {len(monitor.metrics_history)} metrics.")
    if monitor.metrics_history:
        latest = monitor.metrics_history[-1]
        print(
            f"📊 Latest readings: CPU {latest.cpu_percent:.1f}%, Memory {latest.memory_percent:.1f}%"
        )


if __name__ == "__main__":
    main()

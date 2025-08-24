"""
Quick Demo - HyperFocus Zone System Monitor

A simple demo script to show the system monitor in action.
"""

import time

from system_monitor import SystemMonitor


def main():
    """Run a quick demo of the system monitor."""
    print("HyperFocus Zone System Performance Monitor - Quick Demo")
    print("=" * 60)

    # Create monitor instance with simple alert thresholds
    monitor = SystemMonitor(
        log_file="demo_monitor.log",
        csv_file="demo_metrics.csv",
        alert_thresholds={
            "cpu_percent": 70.0,
            "memory_percent": 75.0,
            "disk_usage_percent": 85.0,
        },
    )

    print("Collecting system metrics...")

    # Collect and display metrics 3 times
    for i in range(3):
        print(f"\n--- Measurement {i+1} ---")

        # Collect metrics
        metrics = monitor.collect_metrics()

        # Check for alerts
        monitor.check_alerts(metrics)

        # Save to CSV
        monitor.save_metrics_to_csv(metrics)

        # Display key metrics without emojis for Windows compatibility
        print(f"CPU Usage:    {metrics.cpu_percent:6.1f}%")
        print(
            f"Memory Usage: {metrics.memory_percent:6.1f}% ({metrics.memory_used_gb:.1f}GB)"
        )
        print(f"Disk Usage:   {metrics.disk_usage_percent:6.1f}%")
        print(f"Processes:    {metrics.process_count}")

        if i < 2:  # Don't sleep after last measurement
            time.sleep(2)

    # Show system summary
    print("\n" + "=" * 60)
    print("SYSTEM SUMMARY")
    print("=" * 60)

    summary = monitor.get_system_summary()
    overview = summary["system_overview"]

    print(f"Current CPU:      {overview['cpu_percent']:.1f}%")
    print(f"Current Memory:   {overview['memory_percent']:.1f}%")
    print(f"Current Disk:     {overview['disk_usage_percent']:.1f}%")
    print(f"Active Processes: {overview['process_count']}")
    print(f"System Uptime:    {overview['uptime']}")

    # Export metrics to JSON
    monitor.export_metrics_json("demo_export.json")

    print(f"\nFiles created:")
    print(f"- demo_monitor.log (system log)")
    print(f"- demo_metrics.csv (metrics data)")
    print(f"- demo_export.json (exported data)")

    print(f"\nDemo complete! {len(monitor.metrics_history)} metrics collected.")


if __name__ == "__main__":
    main()

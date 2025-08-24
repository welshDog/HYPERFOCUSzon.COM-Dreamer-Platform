"""
System Performance Monitor

A comprehensive Python script for monitoring system performance metrics
including CPU usage, memory consumption, disk I/O, network activity,
and process information with real-time updates and logging capabilities.

Author: HyperFocus Zone Empire
Version: 1.0
Dependencies: psutil, matplotlib (optional for graphs)
"""

import csv
import json
import logging
import os
import queue
import threading
import time
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Optional

import psutil


@dataclass
class SystemMetrics:
    """Data class to store system performance metrics."""

    timestamp: str
    cpu_percent: float
    memory_percent: float
    memory_used_gb: float
    memory_total_gb: float
    disk_usage_percent: float
    disk_read_mb: float
    disk_write_mb: float
    network_sent_mb: float
    network_recv_mb: float
    process_count: int
    boot_time: str


class SystemMonitor:
    """
    Real-time system performance monitoring class.

    Features:
    - CPU usage monitoring
    - Memory usage tracking
    - Disk I/O statistics
    - Network activity monitoring
    - Process information
    - Data logging to files
    - Real-time alerts
    """

    def __init__(
        self,
        log_file: str = "system_monitor.log",
        csv_file: str = "system_metrics.csv",
        alert_thresholds: Optional[Dict[str, float]] = None,
    ):
        """
        Initialize the system monitor.

        Args:
            log_file: Path to log file for events
            csv_file: Path to CSV file for metrics data
            alert_thresholds: Dictionary of metric thresholds for alerts
        """
        self.log_file = log_file
        self.csv_file = csv_file
        self.alert_thresholds = alert_thresholds or {
            "cpu_percent": 80.0,
            "memory_percent": 85.0,
            "disk_usage_percent": 90.0,
        }

        # Setup logging
        self._setup_logging()

        # Initialize metrics storage
        self.metrics_history: List[SystemMetrics] = []
        self.is_monitoring = False
        self.monitor_thread = None
        self.metrics_queue = queue.Queue()

        # Initialize baseline network and disk stats
        self._init_baseline_stats()

        self.logger.info("🚀 HyperFocus Zone System Monitor initialized")

    def _setup_logging(self):
        """Setup logging configuration."""
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[logging.FileHandler(self.log_file), logging.StreamHandler()],
        )
        self.logger = logging.getLogger(__name__)

    def _init_baseline_stats(self):
        """Initialize baseline statistics for delta calculations."""
        self.last_disk_io = psutil.disk_io_counters()
        self.last_network_io = psutil.net_io_counters()
        self.last_check_time = time.time()

    def get_cpu_info(self) -> Dict[str, float]:
        """
        Get detailed CPU information.

        Returns:
            Dictionary containing CPU metrics
        """
        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_count = psutil.cpu_count()
        cpu_freq = psutil.cpu_freq()

        return {
            "cpu_percent": cpu_percent,
            "cpu_count_logical": psutil.cpu_count(logical=True),
            "cpu_count_physical": psutil.cpu_count(logical=False),
            "cpu_freq_current": cpu_freq.current if cpu_freq else 0,
            "cpu_freq_max": cpu_freq.max if cpu_freq else 0,
            "load_average": (
                psutil.getloadavg() if hasattr(psutil, "getloadavg") else [0, 0, 0]
            ),
        }

    def get_memory_info(self) -> Dict[str, float]:
        """
        Get detailed memory information.

        Returns:
            Dictionary containing memory metrics
        """
        memory = psutil.virtual_memory()
        swap = psutil.swap_memory()

        return {
            "memory_total_gb": memory.total / (1024**3),
            "memory_used_gb": memory.used / (1024**3),
            "memory_available_gb": memory.available / (1024**3),
            "memory_percent": memory.percent,
            "swap_total_gb": swap.total / (1024**3),
            "swap_used_gb": swap.used / (1024**3),
            "swap_percent": swap.percent,
        }

    def get_disk_info(self) -> Dict[str, float]:
        """
        Get detailed disk information.

        Returns:
            Dictionary containing disk metrics
        """
        # Use current drive on Windows
        disk_path = "C:\\" if os.name == "nt" else "/"
        disk_usage = psutil.disk_usage(disk_path)
        current_disk_io = psutil.disk_io_counters()
        current_time = time.time()

        # Calculate delta values
        time_delta = current_time - self.last_check_time

        if self.last_disk_io and time_delta > 0:
            read_delta = current_disk_io.read_bytes - self.last_disk_io.read_bytes
            write_delta = current_disk_io.write_bytes - self.last_disk_io.write_bytes

            read_mb_per_sec = (read_delta / (1024**2)) / time_delta
            write_mb_per_sec = (write_delta / (1024**2)) / time_delta
        else:
            read_mb_per_sec = 0
            write_mb_per_sec = 0

        return {
            "disk_total_gb": disk_usage.total / (1024**3),
            "disk_used_gb": disk_usage.used / (1024**3),
            "disk_free_gb": disk_usage.free / (1024**3),
            "disk_usage_percent": (disk_usage.used / disk_usage.total) * 100,
            "disk_read_mb_per_sec": read_mb_per_sec,
            "disk_write_mb_per_sec": write_mb_per_sec,
        }

    def get_network_info(self) -> Dict[str, float]:
        """
        Get detailed network information.

        Returns:
            Dictionary containing network metrics
        """
        current_network_io = psutil.net_io_counters()
        current_time = time.time()

        # Calculate delta values
        time_delta = current_time - self.last_check_time

        if self.last_network_io and time_delta > 0:
            sent_delta = current_network_io.bytes_sent - self.last_network_io.bytes_sent
            recv_delta = current_network_io.bytes_recv - self.last_network_io.bytes_recv

            sent_mb_per_sec = (sent_delta / (1024**2)) / time_delta
            recv_mb_per_sec = (recv_delta / (1024**2)) / time_delta
        else:
            sent_mb_per_sec = 0
            recv_mb_per_sec = 0

        return {
            "network_sent_total_gb": current_network_io.bytes_sent / (1024**3),
            "network_recv_total_gb": current_network_io.bytes_recv / (1024**3),
            "network_sent_mb_per_sec": sent_mb_per_sec,
            "network_recv_mb_per_sec": recv_mb_per_sec,
            "network_packets_sent": current_network_io.packets_sent,
            "network_packets_recv": current_network_io.packets_recv,
        }

    def get_process_info(self) -> Dict[str, any]:
        """
        Get process information.

        Returns:
            Dictionary containing process metrics
        """
        processes = list(
            psutil.process_iter(["pid", "name", "cpu_percent", "memory_percent"])
        )

        # Sort by CPU usage
        top_cpu_processes = sorted(
            processes, key=lambda p: p.info["cpu_percent"] or 0, reverse=True
        )[:5]

        # Sort by memory usage
        top_memory_processes = sorted(
            processes, key=lambda p: p.info["memory_percent"] or 0, reverse=True
        )[:5]

        return {
            "total_processes": len(processes),
            "top_cpu_processes": [
                (p.info["name"], p.info["cpu_percent"]) for p in top_cpu_processes
            ],
            "top_memory_processes": [
                (p.info["name"], p.info["memory_percent"]) for p in top_memory_processes
            ],
        }

    def collect_metrics(self) -> SystemMetrics:
        """
        Collect all system metrics.

        Returns:
            SystemMetrics object containing all current metrics
        """
        timestamp = datetime.now().isoformat()

        # Collect all metrics
        cpu_info = self.get_cpu_info()
        memory_info = self.get_memory_info()
        disk_info = self.get_disk_info()
        network_info = self.get_network_info()
        process_info = self.get_process_info()

        # Update baseline stats for next iteration
        self.last_disk_io = psutil.disk_io_counters()
        self.last_network_io = psutil.net_io_counters()
        self.last_check_time = time.time()

        # Create metrics object
        metrics = SystemMetrics(
            timestamp=timestamp,
            cpu_percent=cpu_info["cpu_percent"],
            memory_percent=memory_info["memory_percent"],
            memory_used_gb=memory_info["memory_used_gb"],
            memory_total_gb=memory_info["memory_total_gb"],
            disk_usage_percent=disk_info["disk_usage_percent"],
            disk_read_mb=disk_info["disk_read_mb_per_sec"],
            disk_write_mb=disk_info["disk_write_mb_per_sec"],
            network_sent_mb=network_info["network_sent_mb_per_sec"],
            network_recv_mb=network_info["network_recv_mb_per_sec"],
            process_count=process_info["total_processes"],
            boot_time=datetime.fromtimestamp(psutil.boot_time()).isoformat(),
        )

        return metrics

    def check_alerts(self, metrics: SystemMetrics):
        """
        Check if any metrics exceed alert thresholds.

        Args:
            metrics: SystemMetrics object to check
        """
        alerts = []

        if metrics.cpu_percent > self.alert_thresholds["cpu_percent"]:
            alerts.append(f"🔥 HIGH CPU USAGE: {metrics.cpu_percent:.1f}%")

        if metrics.memory_percent > self.alert_thresholds["memory_percent"]:
            alerts.append(f"🧠 HIGH MEMORY USAGE: {metrics.memory_percent:.1f}%")

        if metrics.disk_usage_percent > self.alert_thresholds["disk_usage_percent"]:
            alerts.append(f"💾 HIGH DISK USAGE: {metrics.disk_usage_percent:.1f}%")

        for alert in alerts:
            self.logger.warning(f"⚠️ ALERT: {alert}")

    def save_metrics_to_csv(self, metrics: SystemMetrics):
        """
        Save metrics to CSV file.

        Args:
            metrics: SystemMetrics object to save
        """
        file_exists = os.path.isfile(self.csv_file)

        with open(self.csv_file, "a", newline="") as csvfile:
            fieldnames = [
                "timestamp",
                "cpu_percent",
                "memory_percent",
                "memory_used_gb",
                "memory_total_gb",
                "disk_usage_percent",
                "disk_read_mb",
                "disk_write_mb",
                "network_sent_mb",
                "network_recv_mb",
                "process_count",
                "boot_time",
            ]

            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if not file_exists:
                writer.writeheader()

            writer.writerow(
                {
                    "timestamp": metrics.timestamp,
                    "cpu_percent": metrics.cpu_percent,
                    "memory_percent": metrics.memory_percent,
                    "memory_used_gb": metrics.memory_used_gb,
                    "memory_total_gb": metrics.memory_total_gb,
                    "disk_usage_percent": metrics.disk_usage_percent,
                    "disk_read_mb": metrics.disk_read_mb,
                    "disk_write_mb": metrics.disk_write_mb,
                    "network_sent_mb": metrics.network_sent_mb,
                    "network_recv_mb": metrics.network_recv_mb,
                    "process_count": metrics.process_count,
                    "boot_time": metrics.boot_time,
                }
            )

    def display_metrics(self, metrics: SystemMetrics):
        """
        Display metrics in a formatted way.

        Args:
            metrics: SystemMetrics object to display
        """
        print(f"\n{'='*70}")
        print(f"🚀 HyperFocus Zone System Monitor - {metrics.timestamp}")
        print(f"{'='*70}")
        print(f"💻 CPU Usage:        {metrics.cpu_percent:6.1f}%")
        print(
            f"🧠 Memory Usage:     {metrics.memory_percent:6.1f}% ({metrics.memory_used_gb:.1f}GB / {metrics.memory_total_gb:.1f}GB)"
        )
        print(f"💾 Disk Usage:       {metrics.disk_usage_percent:6.1f}%")
        print(
            f"📊 Disk I/O:         Read: {metrics.disk_read_mb:6.2f} MB/s  Write: {metrics.disk_write_mb:6.2f} MB/s"
        )
        print(
            f"🌐 Network I/O:      Sent: {metrics.network_sent_mb:6.2f} MB/s  Recv: {metrics.network_recv_mb:6.2f} MB/s"
        )
        print(f"⚙️ Active Processes: {metrics.process_count}")
        print(f"⏰ System Uptime:    {self._calculate_uptime(metrics.boot_time)}")

    def _calculate_uptime(self, boot_time: str) -> str:
        """Calculate system uptime from boot time."""
        boot_datetime = datetime.fromisoformat(boot_time)
        uptime = datetime.now() - boot_datetime

        days = uptime.days
        hours, remainder = divmod(uptime.seconds, 3600)
        minutes, _ = divmod(remainder, 60)

        return f"{days}d {hours}h {minutes}m"

    def _monitor_loop(self, interval: int):
        """
        Main monitoring loop (runs in separate thread).

        Args:
            interval: Monitoring interval in seconds
        """
        while self.is_monitoring:
            try:
                metrics = self.collect_metrics()
                self.metrics_history.append(metrics)

                # Keep only last 1000 metrics to prevent memory issues
                if len(self.metrics_history) > 1000:
                    self.metrics_history = self.metrics_history[-1000:]

                # Check for alerts
                self.check_alerts(metrics)

                # Save to CSV
                self.save_metrics_to_csv(metrics)

                # Display metrics
                self.display_metrics(metrics)

                # Wait for next interval
                time.sleep(interval)

            except Exception as e:
                self.logger.error(f"Error in monitoring loop: {e}")
                time.sleep(interval)

    def start_monitoring(self, interval: int = 5):
        """
        Start real-time monitoring in a separate thread.

        Args:
            interval: Monitoring interval in seconds
        """
        if self.is_monitoring:
            self.logger.warning("Monitoring is already running")
            return

        self.is_monitoring = True
        self.monitor_thread = threading.Thread(
            target=self._monitor_loop, args=(interval,)
        )
        self.monitor_thread.daemon = True
        self.monitor_thread.start()

        self.logger.info(f"🚀 Started monitoring with {interval}s interval")

    def stop_monitoring(self):
        """Stop real-time monitoring."""
        if not self.is_monitoring:
            self.logger.warning("Monitoring is not running")
            return

        self.is_monitoring = False
        if self.monitor_thread:
            self.monitor_thread.join()

        self.logger.info("⛔ Monitoring stopped")

    def get_system_summary(self) -> Dict[str, any]:
        """
        Get a comprehensive system summary.

        Returns:
            Dictionary containing system summary
        """
        metrics = self.collect_metrics()
        cpu_info = self.get_cpu_info()
        memory_info = self.get_memory_info()
        disk_info = self.get_disk_info()
        network_info = self.get_network_info()
        process_info = self.get_process_info()

        return {
            "timestamp": metrics.timestamp,
            "system_overview": {
                "cpu_percent": metrics.cpu_percent,
                "memory_percent": metrics.memory_percent,
                "disk_usage_percent": metrics.disk_usage_percent,
                "process_count": metrics.process_count,
                "uptime": self._calculate_uptime(metrics.boot_time),
            },
            "cpu_details": cpu_info,
            "memory_details": memory_info,
            "disk_details": disk_info,
            "network_details": network_info,
            "process_details": process_info,
        }

    def export_metrics_json(self, filename: str = "system_metrics.json"):
        """
        Export all collected metrics to JSON file.

        Args:
            filename: Output JSON filename
        """
        data = {
            "export_timestamp": datetime.now().isoformat(),
            "total_metrics": len(self.metrics_history),
            "metrics": [
                {
                    "timestamp": m.timestamp,
                    "cpu_percent": m.cpu_percent,
                    "memory_percent": m.memory_percent,
                    "memory_used_gb": m.memory_used_gb,
                    "memory_total_gb": m.memory_total_gb,
                    "disk_usage_percent": m.disk_usage_percent,
                    "disk_read_mb": m.disk_read_mb,
                    "disk_write_mb": m.disk_write_mb,
                    "network_sent_mb": m.network_sent_mb,
                    "network_recv_mb": m.network_recv_mb,
                    "process_count": m.process_count,
                    "boot_time": m.boot_time,
                }
                for m in self.metrics_history
            ],
        }

        with open(filename, "w") as f:
            json.dump(data, f, indent=2)

        self.logger.info(
            f"📊 Exported {len(self.metrics_history)} metrics to {filename}"
        )


def main():
    """Main function to run the system monitor."""
    print("🚀 HyperFocus Zone System Performance Monitor")
    print("=" * 50)

    # Create monitor instance
    monitor = SystemMonitor(
        log_file="hyperfocus_system_monitor.log",
        csv_file="hyperfocus_system_metrics.csv",
        alert_thresholds={
            "cpu_percent": 75.0,
            "memory_percent": 80.0,
            "disk_usage_percent": 85.0,
        },
    )

    try:
        # Show initial system summary
        print("📋 Initial System Summary:")
        summary = monitor.get_system_summary()
        print(f"CPU: {summary['system_overview']['cpu_percent']:.1f}%")
        print(f"Memory: {summary['system_overview']['memory_percent']:.1f}%")
        print(f"Disk: {summary['system_overview']['disk_usage_percent']:.1f}%")
        print(f"Processes: {summary['system_overview']['process_count']}")
        print(f"Uptime: {summary['system_overview']['uptime']}")

        # Start monitoring
        print("\n🚀 Starting real-time monitoring...")
        print("Press Ctrl+C to stop monitoring")

        monitor.start_monitoring(interval=3)

        # Keep main thread alive
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\n⛔ Stopping monitor...")
        monitor.stop_monitoring()

        # Export final metrics
        monitor.export_metrics_json("final_system_metrics.json")
        print("✅ Monitor stopped and metrics exported")

    except Exception as e:
        print(f"❌ Error: {e}")
        monitor.stop_monitoring()


if __name__ == "__main__":
    main()

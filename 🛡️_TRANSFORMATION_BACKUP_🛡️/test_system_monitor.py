"""
Unit tests for System Performance Monitor

Comprehensive test suite for the SystemMonitor class and its components.
"""

import csv
import json
import os
import tempfile
import unittest
from unittest.mock import patch

from system_monitor import SystemMetrics, SystemMonitor


class TestSystemMonitor(unittest.TestCase):
    """Test cases for SystemMonitor class."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        # Create temporary files for testing
        self.temp_log = tempfile.NamedTemporaryFile(delete=False, suffix=".log")
        self.temp_csv = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")

        self.monitor = SystemMonitor(
            log_file=self.temp_log.name,
            csv_file=self.temp_csv.name,
            alert_thresholds={
                "cpu_percent": 80.0,
                "memory_percent": 85.0,
                "disk_usage_percent": 90.0,
            },
        )

    def tearDown(self):
        """Clean up after each test method."""
        # Clean up temporary files
        try:
            os.unlink(self.temp_log.name)
            os.unlink(self.temp_csv.name)
        except:
            pass

        # Stop monitoring if running
        if self.monitor.is_monitoring:
            self.monitor.stop_monitoring()

    def test_monitor_initialization(self):
        """Test monitor initialization."""
        self.assertIsNotNone(self.monitor.logger)
        self.assertFalse(self.monitor.is_monitoring)
        self.assertEqual(len(self.monitor.metrics_history), 0)
        self.assertEqual(self.monitor.alert_thresholds["cpu_percent"], 80.0)

    def test_get_cpu_info(self):
        """Test CPU information retrieval."""
        cpu_info = self.monitor.get_cpu_info()

        self.assertIn("cpu_percent", cpu_info)
        self.assertIn("cpu_count_logical", cpu_info)
        self.assertIn("cpu_count_physical", cpu_info)
        self.assertIsInstance(cpu_info["cpu_percent"], (int, float))
        self.assertGreaterEqual(cpu_info["cpu_percent"], 0)
        self.assertLessEqual(cpu_info["cpu_percent"], 100)

    def test_get_memory_info(self):
        """Test memory information retrieval."""
        memory_info = self.monitor.get_memory_info()

        self.assertIn("memory_total_gb", memory_info)
        self.assertIn("memory_used_gb", memory_info)
        self.assertIn("memory_percent", memory_info)
        self.assertGreater(memory_info["memory_total_gb"], 0)
        self.assertGreaterEqual(memory_info["memory_used_gb"], 0)
        self.assertGreaterEqual(memory_info["memory_percent"], 0)
        self.assertLessEqual(memory_info["memory_percent"], 100)

    def test_get_disk_info(self):
        """Test disk information retrieval."""
        disk_info = self.monitor.get_disk_info()

        self.assertIn("disk_total_gb", disk_info)
        self.assertIn("disk_used_gb", disk_info)
        self.assertIn("disk_usage_percent", disk_info)
        self.assertGreater(disk_info["disk_total_gb"], 0)
        self.assertGreaterEqual(disk_info["disk_used_gb"], 0)
        self.assertGreaterEqual(disk_info["disk_usage_percent"], 0)
        self.assertLessEqual(disk_info["disk_usage_percent"], 100)

    def test_get_network_info(self):
        """Test network information retrieval."""
        network_info = self.monitor.get_network_info()

        self.assertIn("network_sent_total_gb", network_info)
        self.assertIn("network_recv_total_gb", network_info)
        self.assertIn("network_sent_mb_per_sec", network_info)
        self.assertIn("network_recv_mb_per_sec", network_info)
        self.assertGreaterEqual(network_info["network_sent_total_gb"], 0)
        self.assertGreaterEqual(network_info["network_recv_total_gb"], 0)

    def test_get_process_info(self):
        """Test process information retrieval."""
        process_info = self.monitor.get_process_info()

        self.assertIn("total_processes", process_info)
        self.assertIn("top_cpu_processes", process_info)
        self.assertIn("top_memory_processes", process_info)
        self.assertGreater(process_info["total_processes"], 0)
        self.assertIsInstance(process_info["top_cpu_processes"], list)
        self.assertIsInstance(process_info["top_memory_processes"], list)

    def test_collect_metrics(self):
        """Test metrics collection."""
        metrics = self.monitor.collect_metrics()

        self.assertIsInstance(metrics, SystemMetrics)
        self.assertIsNotNone(metrics.timestamp)
        self.assertGreaterEqual(metrics.cpu_percent, 0)
        self.assertLessEqual(metrics.cpu_percent, 100)
        self.assertGreaterEqual(metrics.memory_percent, 0)
        self.assertLessEqual(metrics.memory_percent, 100)
        self.assertGreater(metrics.process_count, 0)

    def test_check_alerts_no_alerts(self):
        """Test alert checking with normal values."""
        metrics = SystemMetrics(
            timestamp="2025-08-21T10:00:00",
            cpu_percent=50.0,
            memory_percent=60.0,
            memory_used_gb=8.0,
            memory_total_gb=16.0,
            disk_usage_percent=70.0,
            disk_read_mb=1.0,
            disk_write_mb=2.0,
            network_sent_mb=0.5,
            network_recv_mb=1.5,
            process_count=150,
            boot_time="2025-08-21T08:00:00",
        )

        # Should not raise any exceptions
        self.monitor.check_alerts(metrics)

    def test_check_alerts_with_alerts(self):
        """Test alert checking with high values."""
        metrics = SystemMetrics(
            timestamp="2025-08-21T10:00:00",
            cpu_percent=85.0,  # Above threshold
            memory_percent=90.0,  # Above threshold
            memory_used_gb=14.0,
            memory_total_gb=16.0,
            disk_usage_percent=95.0,  # Above threshold
            disk_read_mb=1.0,
            disk_write_mb=2.0,
            network_sent_mb=0.5,
            network_recv_mb=1.5,
            process_count=150,
            boot_time="2025-08-21T08:00:00",
        )

        # Should log warning messages (tested by checking log output)
        with patch.object(self.monitor.logger, "warning") as mock_warning:
            self.monitor.check_alerts(metrics)
            self.assertGreater(mock_warning.call_count, 0)

    def test_save_metrics_to_csv(self):
        """Test saving metrics to CSV file."""
        metrics = SystemMetrics(
            timestamp="2025-08-21T10:00:00",
            cpu_percent=50.0,
            memory_percent=60.0,
            memory_used_gb=8.0,
            memory_total_gb=16.0,
            disk_usage_percent=70.0,
            disk_read_mb=1.0,
            disk_write_mb=2.0,
            network_sent_mb=0.5,
            network_recv_mb=1.5,
            process_count=150,
            boot_time="2025-08-21T08:00:00",
        )

        self.monitor.save_metrics_to_csv(metrics)

        # Verify CSV file was created and contains data
        self.assertTrue(os.path.exists(self.temp_csv.name))

        with open(self.temp_csv.name, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            rows = list(reader)
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["cpu_percent"], "50.0")
            self.assertEqual(rows[0]["memory_percent"], "60.0")

    def test_calculate_uptime(self):
        """Test uptime calculation."""
        # Test with a known boot time
        boot_time = "2025-08-21T08:00:00"
        uptime = self.monitor._calculate_uptime(boot_time)

        self.assertIsInstance(uptime, str)
        self.assertIn("d", uptime)  # Should contain days
        self.assertIn("h", uptime)  # Should contain hours
        self.assertIn("m", uptime)  # Should contain minutes

    def test_get_system_summary(self):
        """Test system summary generation."""
        summary = self.monitor.get_system_summary()

        self.assertIn("timestamp", summary)
        self.assertIn("system_overview", summary)
        self.assertIn("cpu_details", summary)
        self.assertIn("memory_details", summary)
        self.assertIn("disk_details", summary)
        self.assertIn("network_details", summary)
        self.assertIn("process_details", summary)

        # Verify system overview contains expected keys
        overview = summary["system_overview"]
        self.assertIn("cpu_percent", overview)
        self.assertIn("memory_percent", overview)
        self.assertIn("disk_usage_percent", overview)
        self.assertIn("process_count", overview)
        self.assertIn("uptime", overview)

    def test_export_metrics_json(self):
        """Test JSON export functionality."""
        # Add some test metrics
        test_metrics = SystemMetrics(
            timestamp="2025-08-21T10:00:00",
            cpu_percent=50.0,
            memory_percent=60.0,
            memory_used_gb=8.0,
            memory_total_gb=16.0,
            disk_usage_percent=70.0,
            disk_read_mb=1.0,
            disk_write_mb=2.0,
            network_sent_mb=0.5,
            network_recv_mb=1.5,
            process_count=150,
            boot_time="2025-08-21T08:00:00",
        )

        self.monitor.metrics_history.append(test_metrics)

        # Create temporary JSON file
        temp_json = tempfile.NamedTemporaryFile(delete=False, suffix=".json")
        temp_json.close()

        try:
            self.monitor.export_metrics_json(temp_json.name)

            # Verify JSON file was created and contains data
            self.assertTrue(os.path.exists(temp_json.name))

            with open(temp_json.name, "r") as jsonfile:
                data = json.load(jsonfile)
                self.assertIn("export_timestamp", data)
                self.assertIn("total_metrics", data)
                self.assertIn("metrics", data)
                self.assertEqual(data["total_metrics"], 1)
                self.assertEqual(len(data["metrics"]), 1)
                self.assertEqual(data["metrics"][0]["cpu_percent"], 50.0)

        finally:
            os.unlink(temp_json.name)

    @patch("time.sleep")
    def test_start_stop_monitoring(self, mock_sleep):
        """Test starting and stopping monitoring."""
        # Test start monitoring
        self.monitor.start_monitoring(interval=1)
        self.assertTrue(self.monitor.is_monitoring)
        self.assertIsNotNone(self.monitor.monitor_thread)

        # Test stop monitoring
        self.monitor.stop_monitoring()
        self.assertFalse(self.monitor.is_monitoring)


class TestSystemMetrics(unittest.TestCase):
    """Test cases for SystemMetrics dataclass."""

    def test_system_metrics_creation(self):
        """Test SystemMetrics object creation."""
        metrics = SystemMetrics(
            timestamp="2025-08-21T10:00:00",
            cpu_percent=50.0,
            memory_percent=60.0,
            memory_used_gb=8.0,
            memory_total_gb=16.0,
            disk_usage_percent=70.0,
            disk_read_mb=1.0,
            disk_write_mb=2.0,
            network_sent_mb=0.5,
            network_recv_mb=1.5,
            process_count=150,
            boot_time="2025-08-21T08:00:00",
        )

        self.assertEqual(metrics.timestamp, "2025-08-21T10:00:00")
        self.assertEqual(metrics.cpu_percent, 50.0)
        self.assertEqual(metrics.memory_percent, 60.0)
        self.assertEqual(metrics.process_count, 150)


class TestIntegration(unittest.TestCase):
    """Integration tests for the complete system monitor."""

    def test_full_monitoring_cycle(self):
        """Test a complete monitoring cycle."""
        # Create temporary files
        temp_log = tempfile.NamedTemporaryFile(delete=False, suffix=".log")
        temp_csv = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")

        try:
            monitor = SystemMonitor(log_file=temp_log.name, csv_file=temp_csv.name)

            # Collect metrics
            metrics = monitor.collect_metrics()

            # Check alerts
            monitor.check_alerts(metrics)

            # Save to CSV
            monitor.save_metrics_to_csv(metrics)

            # Verify CSV file has data
            self.assertTrue(os.path.exists(temp_csv.name))
            with open(temp_csv.name, "r") as f:
                content = f.read()
                self.assertIn("timestamp", content)
                self.assertIn("cpu_percent", content)

        finally:
            # Clean up
            try:
                os.unlink(temp_log.name)
                os.unlink(temp_csv.name)
            except:
                pass


if __name__ == "__main__":
    # Run all tests with verbose output
    unittest.main(verbosity=2)

#!/usr/bin/env python3
"""
♾️📊⚡ CONTINUOUS IMMORTAL EMPIRE MONITORING SYSTEM ⚡📊♾️
Real-time empire health and performance monitoring
"""

import psutil
import time
import json
import ping3
from datetime import datetime
import os
import threading
import logging

class ContinuousEmpireMonitor:
    """📊 Continuous monitoring system for immortal empire"""

    def __init__(self):
        self.monitoring_active = True
        self.alert_thresholds = {
            "cpu_percent": 90,
            "memory_percent": 95,
            "disk_percent": 85,
            "network_health": 70
        }

        self.servers = {
            "main_dive": "100.114.5.118",
            "main_server": "100.68.37.27",
            "mini_server": "100.71.69.16",
            "raspberry_pi": "192.168.137.10"
        }

        # Setup logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('empire-maintenance-logs/continuous_monitoring.log', encoding='utf-8')
            ]
        )

    def check_system_health(self):
        """💻 Check local system health"""
        try:
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('C:' if os.name == 'nt' else '/')

            health_data = {
                "timestamp": datetime.now().isoformat(),
                "cpu_percent": cpu_percent,
                "memory_percent": memory.percent,
                "disk_percent": disk.percent,
                "available_memory_gb": round(memory.available / (1024**3), 2),
                "free_disk_gb": round(disk.free / (1024**3), 2)
            }

            # Check for alerts
            alerts = []
            if cpu_percent > self.alert_thresholds["cpu_percent"]:
                alerts.append(f"🚨 HIGH CPU: {cpu_percent}%")

            if memory.percent > self.alert_thresholds["memory_percent"]:
                alerts.append(f"🚨 HIGH MEMORY: {memory.percent}%")

            if disk.percent > self.alert_thresholds["disk_percent"]:
                alerts.append(f"🚨 HIGH DISK: {disk.percent}%")

            health_data["alerts"] = alerts

            return health_data

        except Exception as e:
            return {"error": str(e), "timestamp": datetime.now().isoformat()}

    def check_server_connectivity(self):
        """🌐 Check empire server connectivity"""
        server_status = {}

        for name, ip in self.servers.items():
            try:
                response_time = ping3.ping(ip, timeout=3)
                if response_time is not None:
                    server_status[name] = {
                        "status": "ONLINE",
                        "response_time_ms": round(response_time * 1000, 2),
                        "ip": ip
                    }
                else:
                    server_status[name] = {
                        "status": "OFFLINE",
                        "ip": ip
                    }
            except Exception as e:
                server_status[name] = {
                    "status": "ERROR",
                    "error": str(e),
                    "ip": ip
                }

        return server_status

    def monitoring_cycle(self):
        """🔄 Execute single monitoring cycle"""
        print(f"📊 Monitoring cycle: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        # Check system health
        system_health = self.check_system_health()

        # Check server connectivity
        server_status = self.check_server_connectivity()

        # Create monitoring report
        monitor_report = {
            "cycle_timestamp": datetime.now().isoformat(),
            "system_health": system_health,
            "server_status": server_status,
            "empire_status": "IMMORTAL_OPERATIONAL"
        }

        # Save monitoring data
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        report_file = f"empire-monitoring-data/monitor_{timestamp}.json"

        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(monitor_report, f, indent=2, default=str)

        # Check for alerts
        total_alerts = len(system_health.get("alerts", []))
        offline_servers = sum(1 for server in server_status.values() if server["status"] != "ONLINE")

        if total_alerts > 0 or offline_servers > 0:
            print(f"🚨 ALERTS DETECTED: {total_alerts} system alerts, {offline_servers} offline servers")
            logging.warning(f"Empire alerts: {total_alerts} system, {offline_servers} server issues")
        else:
            print("✅ Empire status: OPTIMAL")

        return monitor_report

    def start_continuous_monitoring(self):
        """🚀 Start continuous monitoring loop"""
        print("♾️📊⚡ CONTINUOUS IMMORTAL EMPIRE MONITORING ACTIVE ⚡📊♾️")
        print("🏛️ Monitoring interval: 15 minutes")
        print("🔮 Empire oversight: PURE INFINITE BEING")

        while self.monitoring_active:
            try:
                self.monitoring_cycle()
                time.sleep(900)  # 15 minutes = 900 seconds

            except KeyboardInterrupt:
                print("\n⚠️ Monitoring stopped by user")
                self.monitoring_active = False
            except Exception as e:
                print(f"❌ Monitoring error: {e}")
                logging.error(f"Monitoring error: {e}")
                time.sleep(60)  # Wait 1 minute before retry

def main():
    """🚀 Main monitoring execution"""
    monitor = ContinuousEmpireMonitor()
    monitor.start_continuous_monitoring()

if __name__ == "__main__":
    main()

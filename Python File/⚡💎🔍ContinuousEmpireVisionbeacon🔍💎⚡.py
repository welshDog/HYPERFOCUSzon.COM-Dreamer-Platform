from datetime import datetime
import json
import subprocess
import time

import psutil
import requests
class ContinuousEmpireMonitor:
    def __init__(self):
        self.monitoring = True
        self.check_interval = 300  # 5 minutes
        self.health_thresholds = {
            "cpu_max": 80,
            "memory_max": 85,
            "response_time_max": 5000
        }

    def check_empire_ports(self):
        """Check key Empire ports"""
        ports = {
            "3000": "Grafana Dashboard",
            "8000": "Admin Dashboard",
            "8080": "Command Center",
            "9000": "Agent Orchestrator",
            "9090": "Prometheus"
        }

        results = {}
        for port, service in ports.items():
            try:
                response = requests.head(f"http://localhost:{port}", timeout=5)
                results[service] = {
                    "status": "ACTIVE",
                    "response_code": response.status_code,
                    "response_time": response.elapsed.total_seconds() * 1000
                }
            except requests.exceptions.RequestException as e:
                results[service] = {
                    "status": "ERROR",
                    "error": str(e)
                }
        return results

    def check_tailscale_status(self):
        """Check Tailscale network status"""
        try:
            result = subprocess.run(['tailscale', 'status'],
                                  capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                nodes = len([line for line in result.stdout.split('\n')
                           if line.strip() and not line.startswith('#')])
                return {
                    "status": "OPERATIONAL",
                    "nodes_active": nodes,
                    "funnel_enabled": "https://hyperfocuszone.tail13f1ca.ts.net" in result.stdout
                }
        except Exception as e:
            return {"status": "ERROR", "error": str(e)}

    def check_system_resources(self):
        """Check system performance"""
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()

        return {
            "cpu_percent": round(cpu_percent, 2),
            "memory_percent": round(memory.percent, 2),
            "status": "LEGENDARY" if (cpu_percent < self.health_thresholds["cpu_max"] and
                                   memory.percent < self.health_thresholds["memory_max"]) else "OPTIMIZING"
        }

    def generate_health_report(self):
        """Generate comprehensive health report"""
        timestamp = datetime.now()

        report = {
            "timestamp": timestamp.isoformat(),
            "empire_ports": self.check_empire_ports(),
            "tailscale_network": self.check_tailscale_status(),
            "system_resources": self.check_system_resources(),
            "overall_status": "MONITORING"
        }

        # Calculate overall health
        healthy_services = sum(1 for service in report["empire_ports"].values()
                             if service["status"] == "ACTIVE")
        total_services = len(report["empire_ports"])
        report["health_percentage"] = (healthy_services / total_services * 100) if total_services > 0 else 0

        # Save to memory crystal
        crystal_path = f"h:/memory_crystals/continuous_health_monitor_{timestamp.strftime('%Y%m%d_%H%M%S')}.json"
        with open(crystal_path, 'w') as f:
            json.dump(report, f, indent=2)

        return report

    def run_monitoring_cycle(self):
        """Run one monitoring cycle"""
        print(f"🔍 {datetime.now().strftime('%H:%M:%S')} - Empire Health Check...")

        report = self.generate_health_report()

        print(f"⚡ System Status: {report['system_resources']['status']}")
        print(f"🌐 Network: {report['tailscale_network']['status']}")
        print(f"📊 Empire Health: {report['health_percentage']:.1f}%")

        # Alert if health drops below threshold
        if report['health_percentage'] < 70:
            logger.info("🌌 ⚠️ ALERT: Empire health below optimal threshold!")

        logger.info("🌌 ✅ Health check complete. Next check in 5 minutes...\n")

    def start_monitoring(self):
        """Start continuous monitoring"""
        logger.info("🌌 🚀 STARTING CONTINUOUS EMPIRE MONITORING")
        logger.info("🌌 ⚡ Check interval: 5 minutes")
        logger.info("🌌 🛡️ Monitoring Empire ports, Tailscale network, and system resources")
        logger.info("🌌 📊 Press Ctrl+C to stop monitoring\n")

        try:
            while self.monitoring:
                self.run_monitoring_cycle()
                time.sleep(self.check_interval)
        except KeyboardInterrupt:
            logger.info("🌌 \n🛑 Monitoring stopped by user")
            logger.info("🌌 💎 All health reports saved to memory crystals")

if __name__ == "__main__":
    monitor = ContinuousEmpireMonitor()
    monitor.start_monitoring()

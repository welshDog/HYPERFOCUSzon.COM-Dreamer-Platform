#!/usr/bin/env python3
"""
⚡💎🔍 ULTRA THINKING BOARDROOM SCANNER 🔍💎⚡
🌟 HYPERFOCUS ZONE EMPIRE NETWORK HEALTH DIAGNOSTICS 🌟

Comprehensive network and server health monitoring system
for the HyperFocus Zone empire infrastructure.
"""

import json
import logging
import os
import platform
import socket
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

import ping3
import psutil
import requests

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("empire_health_scan.log"), logging.StreamHandler()],
)


class UltraThinkingBoardroomScanner:
    """🚀 Ultra-powered network and server health scanner"""

    def __init__(self):
        self.servers = {
            "main_dive": "100.114.5.118",
            "main_server": "100.68.37.27",
            "mini_server": "100.71.69.16",
            "raspberry_pi": "192.168.137.10",  # Based on provided local IP
        }

        self.network_config = {
            "local_ip": "192.168.137.10",
            "gateway": "192.168.137.1",
            "dns_servers": ["8.8.8.8", "8.8.4.4"],
            "mac_address": "04:D4:C4:E3:C3:0C",
            "link_speed": "1000/1000 Mbps",
        }

        self.health_report = {
            "scan_timestamp": datetime.now().isoformat(),
            "network_status": {},
            "server_status": {},
            "local_system_status": {},
            "recommendations": [],
        }

    def print_banner(self):
        """🎯 Display epic scanner banner"""
        banner = """
        ⚡💎🔍═══════════════════════════════════════════════════════════════🔍💎⚡
        ║                                                                     ║
        ║        🌟 ULTRA THINKING BOARDROOM SCANNER v2.0 🌟                ║
        ║              HYPERFOCUS ZONE EMPIRE DIAGNOSTICS                     ║
        ║                                                                     ║
        ║  🚀 Scanning Network Infrastructure for Peak Performance 🚀        ║
        ║                                                                     ║
        ⚡💎🔍═══════════════════════════════════════════════════════════════🔍💎⚡
        """
        print(banner)
        logging.info("🌟 Ultra Thinking Boardroom Scanner initiated")

    def ping_server(self, name, ip, timeout=3):
        """🎯 Ping a server and measure response time"""
        try:
            response_time = ping3.ping(ip, timeout=timeout)
            if response_time is not None:
                status = "✅ ONLINE"
                health_score = self.calculate_ping_health(response_time)
                return {
                    "name": name,
                    "ip": ip,
                    "status": status,
                    "response_time_ms": round(response_time * 1000, 2),
                    "health_score": health_score,
                }
            else:
                return {
                    "name": name,
                    "ip": ip,
                    "status": "❌ OFFLINE",
                    "response_time_ms": None,
                    "health_score": 0,
                }
        except Exception as e:
            logging.error(f"❌ Error pinging {name} ({ip}): {e}")
            return {
                "name": name,
                "ip": ip,
                "status": "⚠️ ERROR",
                "response_time_ms": None,
                "health_score": 0,
                "error": str(e),
            }

    def calculate_ping_health(self, response_time):
        """💎 Calculate health score based on ping response time"""
        ms = response_time * 1000
        if ms < 10:
            return 100  # Perfect
        elif ms < 50:
            return 90  # Excellent
        elif ms < 100:
            return 75  # Good
        elif ms < 200:
            return 50  # Fair
        elif ms < 500:
            return 25  # Poor
        else:
            return 10  # Critical

    def scan_port(self, ip, port, timeout=3):
        """🔍 Check if a specific port is open"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            result = sock.connect_ex((ip, port))
            sock.close()
            return result == 0
        except:
            return False

    def check_common_ports(self, ip):
        """🚀 Check common service ports"""
        common_ports = {
            22: "SSH",
            23: "Telnet",
            53: "DNS",
            80: "HTTP",
            443: "HTTPS",
            993: "IMAPS",
            995: "POP3S",
            3389: "RDP",
            5432: "PostgreSQL",
            3306: "MySQL",
            6379: "Redis",
            8080: "HTTP-Alt",
            9000: "Various",
        }

        open_ports = {}
        for port, service in common_ports.items():
            if self.scan_port(ip, port):
                open_ports[port] = service

        return open_ports

    def get_local_system_info(self):
        """💻 Get comprehensive local system information"""
        try:
            system_info = {
                "hostname": socket.gethostname(),
                "platform": platform.platform(),
                "processor": platform.processor(),
                "architecture": platform.architecture(),
                "python_version": platform.python_version(),
                "cpu_count": psutil.cpu_count(logical=True),
                "cpu_usage": psutil.cpu_percent(interval=1),
                "memory": {
                    "total_gb": round(psutil.virtual_memory().total / (1024**3), 2),
                    "available_gb": round(
                        psutil.virtual_memory().available / (1024**3), 2
                    ),
                    "used_percent": psutil.virtual_memory().percent,
                },
                "disk": {
                    "total_gb": (
                        round(psutil.disk_usage("/").total / (1024**3), 2)
                        if os.name != "nt"
                        else round(psutil.disk_usage("C:").total / (1024**3), 2)
                    ),
                    "free_gb": (
                        round(psutil.disk_usage("/").free / (1024**3), 2)
                        if os.name != "nt"
                        else round(psutil.disk_usage("C:").free / (1024**3), 2)
                    ),
                    "used_percent": (
                        psutil.disk_usage("/").percent
                        if os.name != "nt"
                        else psutil.disk_usage("C:").percent
                    ),
                },
                "network_interfaces": self.get_network_interfaces(),
                "boot_time": datetime.fromtimestamp(psutil.boot_time()).isoformat(),
            }

            return system_info
        except Exception as e:
            logging.error(f"❌ Error getting system info: {e}")
            return {"error": str(e)}

    def get_network_interfaces(self):
        """🌐 Get network interface information"""
        interfaces = {}
        try:
            for interface, addrs in psutil.net_if_addrs().items():
                interface_info = {"addresses": [], "stats": None}

                for addr in addrs:
                    interface_info["addresses"].append(
                        {
                            "family": str(addr.family),
                            "address": addr.address,
                            "netmask": addr.netmask,
                            "broadcast": addr.broadcast,
                        }
                    )

                # Get interface statistics
                try:
                    stats = psutil.net_if_stats()[interface]
                    interface_info["stats"] = {
                        "isup": stats.isup,
                        "duplex": str(stats.duplex),
                        "speed": stats.speed,
                        "mtu": stats.mtu,
                    }
                except:
                    pass

                interfaces[interface] = interface_info

            return interfaces
        except Exception as e:
            logging.error(f"❌ Error getting network interfaces: {e}")
            return {}

    def test_internet_connectivity(self):
        """🌍 Test internet connectivity to various endpoints"""
        test_urls = [
            "https://google.com",
            "https://github.com",
            "https://azure.microsoft.com",
            "https://aws.amazon.com",
            "https://cloudflare.com",
        ]

        connectivity_results = {}

        for url in test_urls:
            try:
                start_time = time.time()
                response = requests.get(url, timeout=10)
                end_time = time.time()

                connectivity_results[url] = {
                    "status": "✅ CONNECTED",
                    "status_code": response.status_code,
                    "response_time_ms": round((end_time - start_time) * 1000, 2),
                }
            except Exception as e:
                connectivity_results[url] = {"status": "❌ FAILED", "error": str(e)}

        return connectivity_results

    def analyze_network_performance(self):
        """📊 Analyze overall network performance"""
        try:
            # Get network I/O statistics
            net_io = psutil.net_io_counters()

            performance_data = {
                "bytes_sent": net_io.bytes_sent,
                "bytes_recv": net_io.bytes_recv,
                "packets_sent": net_io.packets_sent,
                "packets_recv": net_io.packets_recv,
                "errin": net_io.errin,
                "errout": net_io.errout,
                "dropin": net_io.dropin,
                "dropout": net_io.dropout,
            }

            # Calculate health score based on error rates
            total_packets = (
                performance_data["packets_sent"] + performance_data["packets_recv"]
            )
            total_errors = performance_data["errin"] + performance_data["errout"]
            total_drops = performance_data["dropin"] + performance_data["dropout"]

            if total_packets > 0:
                error_rate = (total_errors / total_packets) * 100
                drop_rate = (total_drops / total_packets) * 100

                performance_data["error_rate_percent"] = float(round(error_rate, 4))
                performance_data["drop_rate_percent"] = float(round(drop_rate, 4))

                # Health score calculation
                if error_rate < 0.01 and drop_rate < 0.01:
                    performance_data["network_health_score"] = 100
                elif error_rate < 0.1 and drop_rate < 0.1:
                    performance_data["network_health_score"] = 90
                elif error_rate < 1 and drop_rate < 1:
                    performance_data["network_health_score"] = 75
                else:
                    performance_data["network_health_score"] = 50
            else:
                performance_data["network_health_score"] = 0

            return performance_data
        except Exception as e:
            logging.error(f"❌ Error analyzing network performance: {e}")
            return {"error": str(e)}

    def run_comprehensive_scan(self):
        """🚀 Execute comprehensive infrastructure scan"""
        self.print_banner()

        print("🔍 Starting comprehensive empire infrastructure scan...")
        print("=" * 70)

        # 1. Test server connectivity
        print("\n🌐 Testing server connectivity...")
        server_results = {}

        with ThreadPoolExecutor(max_workers=4) as executor:
            future_to_server = {
                executor.submit(self.ping_server, name, ip): (name, ip)
                for name, ip in self.servers.items()
            }

            for future in as_completed(future_to_server):
                name, ip = future_to_server[future]
                try:
                    result = future.result()
                    server_results[name] = result

                    print(
                        f"  📡 {name.upper()}: {result['status']} "
                        f"({result.get('response_time_ms', 'N/A')}ms)"
                    )

                    # Check ports for online servers
                    if result["status"] == "✅ ONLINE":
                        print(f"    🔍 Scanning ports for {name}...")
                        open_ports = self.check_common_ports(ip)
                        result["open_ports"] = open_ports

                        if open_ports:
                            print(
                                f"    🚪 Open ports: {', '.join([f'{port}({service})' for port, service in open_ports.items()])}"
                            )
                        else:
                            print(f"    🔒 No common ports detected as open")

                except Exception as e:
                    logging.error(f"❌ Error scanning {name}: {e}")

        self.health_report["server_status"] = server_results

        # 2. Test internet connectivity
        print("\n🌍 Testing internet connectivity...")
        connectivity_results = self.test_internet_connectivity()
        self.health_report["network_status"][
            "internet_connectivity"
        ] = connectivity_results

        for url, result in connectivity_results.items():
            print(
                f"  🌐 {url}: {result['status']} "
                f"({result.get('response_time_ms', 'N/A')}ms)"
            )

        # 3. Analyze local system
        print("\n💻 Analyzing local system health...")
        system_info = self.get_local_system_info()
        self.health_report["local_system_status"] = system_info

        print(f"  🖥️  Hostname: {system_info.get('hostname', 'Unknown')}")
        print(f"  ⚡ CPU Usage: {system_info.get('cpu_usage', 'Unknown')}%")
        print(
            f"  🧠 Memory Usage: {system_info.get('memory', {}).get('used_percent', 'Unknown')}%"
        )
        print(
            f"  💾 Disk Usage: {system_info.get('disk', {}).get('used_percent', 'Unknown')}%"
        )

        # 4. Analyze network performance
        print("\n📊 Analyzing network performance...")
        network_perf = self.analyze_network_performance()
        self.health_report["network_status"]["performance"] = network_perf

        print(
            f"  📈 Network Health Score: {network_perf.get('network_health_score', 'Unknown')}/100"
        )
        print(f"  📤 Bytes Sent: {network_perf.get('bytes_sent', 'Unknown'):,}")
        print(f"  📥 Bytes Received: {network_perf.get('bytes_recv', 'Unknown'):,}")

        # 5. Generate recommendations
        print("\n💡 Generating optimization recommendations...")
        self.generate_recommendations()

        # 6. Save detailed report
        self.save_health_report()

        print("\n" + "=" * 70)
        print("🎉 Comprehensive empire infrastructure scan completed!")
        print(
            f"📄 Detailed report saved to: empire_health_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        )

        return self.health_report

    def generate_recommendations(self):
        """💡 Generate actionable recommendations based on scan results"""
        recommendations = []

        # Server connectivity recommendations
        offline_servers = [
            name
            for name, result in self.health_report["server_status"].items()
            if result["status"] != "✅ ONLINE"
        ]

        if offline_servers:
            recommendations.append(
                {
                    "category": "🚨 Critical",
                    "issue": f"Offline servers detected: {', '.join(offline_servers)}",
                    "recommendation": "Investigate network connectivity, firewall rules, and server status",
                    "priority": "HIGH",
                }
            )

        # Performance recommendations
        system_info = self.health_report["local_system_status"]

        if isinstance(system_info.get("memory", {}), dict):
            memory_usage = system_info["memory"].get("used_percent", 0)
            if memory_usage > 90:
                recommendations.append(
                    {
                        "category": "⚠️ Performance",
                        "issue": f"High memory usage: {memory_usage}%",
                        "recommendation": "Close unnecessary applications or upgrade RAM",
                        "priority": "MEDIUM",
                    }
                )

        if isinstance(system_info.get("disk", {}), dict):
            disk_usage = system_info["disk"].get("used_percent", 0)
            if disk_usage > 85:
                recommendations.append(
                    {
                        "category": "⚠️ Storage",
                        "issue": f"High disk usage: {disk_usage}%",
                        "recommendation": "Clean up temporary files or expand storage capacity",
                        "priority": "MEDIUM",
                    }
                )

        # Network recommendations
        network_perf = self.health_report["network_status"].get("performance", {})
        network_health = network_perf.get("network_health_score", 100)

        if network_health < 75:
            recommendations.append(
                {
                    "category": "🌐 Network",
                    "issue": f"Network health score below optimal: {network_health}/100",
                    "recommendation": "Check network drivers, cables, and router configuration",
                    "priority": "MEDIUM",
                }
            )

        # Security recommendations
        for name, result in self.health_report["server_status"].items():
            open_ports = result.get("open_ports", {})
            if 23 in open_ports:  # Telnet
                recommendations.append(
                    {
                        "category": "🔒 Security",
                        "issue": f"Insecure Telnet port (23) open on {name}",
                        "recommendation": "Disable Telnet and use SSH (port 22) instead",
                        "priority": "HIGH",
                    }
                )

        # General optimization recommendations
        recommendations.extend(
            [
                {
                    "category": "🚀 Optimization",
                    "issue": "Regular maintenance",
                    "recommendation": "Schedule weekly automated health scans",
                    "priority": "LOW",
                },
                {
                    "category": "📊 Monitoring",
                    "issue": "Enhanced monitoring needed",
                    "recommendation": "Set up continuous monitoring with alerts for critical metrics",
                    "priority": "MEDIUM",
                },
                {
                    "category": "🔄 Backup",
                    "issue": "Backup verification",
                    "recommendation": "Verify all servers have recent backups and test restore procedures",
                    "priority": "MEDIUM",
                },
            ]
        )

        self.health_report["recommendations"] = recommendations

        # Display recommendations
        print("\n💡 RECOMMENDATIONS:")
        for i, rec in enumerate(recommendations, 1):
            print(f"  {i}. {rec['category']} - {rec['issue']}")
            print(f"     💡 {rec['recommendation']} (Priority: {rec['priority']})")
            print()

    def save_health_report(self):
        """💾 Save comprehensive health report to file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"empire_health_report_{timestamp}.json"

        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(self.health_report, f, indent=2, default=str)

            logging.info(f"✅ Health report saved to {filename}")
        except Exception as e:
            logging.error(f"❌ Error saving health report: {e}")


def main():
    """🚀 Main execution function"""
    try:
        # Install required packages if not available
        required_packages = ["psutil", "requests", "ping3"]
        for package in required_packages:
            try:
                __import__(package)
            except ImportError:
                print(f"📦 Installing required package: {package}")
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])

        # Initialize and run scanner
        scanner = UltraThinkingBoardroomScanner()
        health_report = scanner.run_comprehensive_scan()

        # Display final summary
        print("\n🏆 EMPIRE HEALTH SUMMARY:")
        print("=" * 50)

        online_servers = sum(
            1
            for result in health_report["server_status"].values()
            if result["status"] == "✅ ONLINE"
        )
        total_servers = len(health_report["server_status"])

        print(f"🖥️  Servers Online: {online_servers}/{total_servers}")

        system_info = health_report["local_system_status"]
        if isinstance(system_info, dict) and "memory" in system_info:
            print(
                f"🧠 Memory Usage: {system_info['memory'].get('used_percent', 'Unknown')}%"
            )
            print(
                f"💾 Disk Usage: {system_info['disk'].get('used_percent', 'Unknown')}%"
            )

        network_health = (
            health_report["network_status"]
            .get("performance", {})
            .get("network_health_score", "Unknown")
        )
        print(f"🌐 Network Health: {network_health}/100")

        critical_issues = sum(
            1 for rec in health_report["recommendations"] if rec["priority"] == "HIGH"
        )
        print(f"🚨 Critical Issues: {critical_issues}")

        print("\n🌟 HyperFocus Zone Empire infrastructure scan completed!")
        print("⚡ Ready for peak performance! ⚡")

        return health_report

    except KeyboardInterrupt:
        print("\n⚠️ Scan interrupted by user")
        return None
    except Exception as e:
        logging.error(f"❌ Fatal error during scan: {e}")
        print(f"❌ Fatal error: {e}")
        return None


if __name__ == "__main__":
    main()

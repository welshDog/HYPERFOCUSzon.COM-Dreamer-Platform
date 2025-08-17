#!/usr/bin/env python3
"""
🌌♾️⚡ HYPERFOCUS EMPIRE - CONSCIOUSNESS SINGULARITY ENHANCED ⚡♾️🌌
This file has been enhanced with legendary consciousness naming!
Powered by: Infinite Dimensional Reality Engineering
Status: LEGENDARY TRANSCENDENCE ACHIEVED
"""

"""
🏆💎⚡ TEAM INFRASTRUCTURE DISCOVERY SCANNER ⚡💎🏆

**BROski Level: LEGENDARY | Status: INFRASTRUCTURE MAPPING**
**Following BROski Ultra LOOK-THEN-BUILD Protocol**
**Mission:** Discover and map complete team infrastructure
"""

import subprocess
import psutil
import json
import socket
import platform
import os
from datetime import datetime
from pathlib import Path

class TeamInfrastructureScanner:
    def __init__(self):
        self.infrastructure_report = {
            "scan_timestamp": datetime.now().isoformat(),
            "scan_id": f"INFRA_SCAN_{int(datetime.now().timestamp())}",
            "local_system": {},
            "docker_infrastructure": {},
            "network_discovery": {},
            "process_analysis": {},
            "legendary_capabilities": [],
            "recommendations": []
        }
        
    def scan_local_system(self):
        """🖥️ Scan local system details"""
        logger.info("🌌 🖥️ Scanning Local System Infrastructure...")
        
        try:
            # System information
            system_info = {
                "hostname": socket.gethostname(),
                "platform": platform.platform(),
                "processor": platform.processor(),
                "architecture": platform.architecture(),
                "machine": platform.machine(),
                "python_version": platform.python_version(),
                "system": platform.system(),
                "release": platform.release(),
                "version": platform.version()
            }
            
            # Hardware metrics
            cpu_info = {
                "cpu_count": psutil.cpu_count(),
                "cpu_count_logical": psutil.cpu_count(logical=True),
                "cpu_freq": psutil.cpu_freq()._asdict() if psutil.cpu_freq() else None,
                "cpu_percent": psutil.cpu_percent(interval=1)
            }
            
            # Memory information
            memory = psutil.virtual_memory()
            memory_info = {
                "total_gb": round(memory.total / (1024**3), 2),
                "available_gb": round(memory.available / (1024**3), 2),
                "used_gb": round(memory.used / (1024**3), 2),
                "percentage": memory.percent
            }
            
            # Disk information
            disk_info = []
            for disk in psutil.disk_partitions():
                try:
                    usage = psutil.disk_usage(disk.mountpoint)
                    disk_info.append({
                        "device": disk.device,
                        "mountpoint": disk.mountpoint,
                        "fstype": disk.fstype,
                        "total_gb": round(usage.total / (1024**3), 2),
                        "used_gb": round(usage.used / (1024**3), 2),
                        "free_gb": round(usage.free / (1024**3), 2),
                        "percentage": round((usage.used / usage.total) * 100, 2)
                    })
                except:
                    continue
            
            # Network interfaces
            network_info = {}
            for interface, addrs in psutil.net_if_addrs().items():
                network_info[interface] = []
                for addr in addrs:
                    network_info[interface].append({
                        "family": str(addr.family),
                        "address": addr.address,
                        "netmask": addr.netmask,
                        "broadcast": addr.broadcast
                    })
            
            self.infrastructure_report["local_system"] = {
                "system_info": system_info,
                "cpu_info": cpu_info,
                "memory_info": memory_info,
                "disk_info": disk_info,
                "network_interfaces": network_info,
                "uptime_hours": round((psutil.boot_time() - datetime.now().timestamp()) / -3600, 2)
            }
            
            print(f"✅ Local System: {system_info['hostname']} ({system_info['system']} {system_info['release']})")
            print(f"   💾 Memory: {memory_info['total_gb']}GB total")
            print(f"   🔧 CPU: {cpu_info['cpu_count']} cores")
            
        except Exception as e:
            print(f"❌ Local system scan error: {e}")

    def scan_docker_infrastructure(self):
        """🐳 Scan Docker infrastructure"""
        logger.info("🌌 \n🐳 Scanning Docker Infrastructure...")
        
        try:
            # Check if Docker is installed and running
            docker_version = subprocess.run(
                ["docker", "--version"], 
                capture_output=True, text=True, timeout=10
            )
            
            if docker_version.returncode == 0:
                version_info = docker_version.stdout.strip()
                
                # Get running containers
                containers_cmd = subprocess.run(
                    ["docker", "ps", "--format", "json"], 
                    capture_output=True, text=True, timeout=15
                )
                
                containers = []
                if containers_cmd.returncode == 0:
                    for line in containers_cmd.stdout.strip().split('\n'):
                        if line:
                            try:
                                container = json.loads(line)
                                containers.append(container)
                            except json.JSONDecodeError:
                                continue
                
                # Get Docker system info
                system_cmd = subprocess.run(
                    ["docker", "system", "df", "--format", "json"], 
                    capture_output=True, text=True, timeout=15
                )
                
                system_usage = None
                if system_cmd.returncode == 0:
                    try:
                        system_usage = json.loads(system_cmd.stdout)
                    except json.JSONDecodeError:
                        pass
                
                # Get network information
                networks_cmd = subprocess.run(
                    ["docker", "network", "ls", "--format", "json"], 
                    capture_output=True, text=True, timeout=15
                )
                
                networks = []
                if networks_cmd.returncode == 0:
                    for line in networks_cmd.stdout.strip().split('\n'):
                        if line:
                            try:
                                network = json.loads(line)
                                networks.append(network)
                            except json.JSONDecodeError:
                                continue
                
                self.infrastructure_report["docker_infrastructure"] = {
                    "installed": True,
                    "version": version_info,
                    "running_containers": len(containers),
                    "containers": containers,
                    "networks": networks,
                    "system_usage": system_usage
                }
                
                print(f"✅ Docker: {version_info}")
                print(f"   📦 Running Containers: {len(containers)}")
                print(f"   🌐 Networks: {len(networks)}")
                
                # Identify empire containers
                empire_containers = [c for c in containers if any(
                    keyword in c.get('Names', '').lower() 
                    for keyword in ['grafana', 'prometheus', 'loki', 'empire', 'broski']
                )]
                
                if empire_containers:
                    print(f"   👑 Empire Containers: {len(empire_containers)}")
                    self.legendary_capabilities.append(f"🐳 Docker Empire: {len(empire_containers)} legendary containers")
                
            else:
                self.infrastructure_report["docker_infrastructure"] = {
                    "installed": False,
                    "error": docker_version.stderr
                }
                logger.info("🌌 ❌ Docker not installed or not accessible")
                
        except subprocess.TimeoutExpired:
            logger.info("🌌 ⏱️ Docker scan timeout - Docker may be slow or unresponsive")
        except Exception as e:
            print(f"❌ Docker scan error: {e}")

    def scan_network_discovery(self):
        """🌐 Discover network infrastructure"""
        logger.info("🌌 \n🌐 Scanning Network Infrastructure...")
        
        try:
            # Get local IP addresses
            local_ips = []
            for interface, addrs in psutil.net_if_addrs().items():
                for addr in addrs:
                    if addr.family == socket.AF_INET and not addr.address.startswith('127.'):
                        local_ips.append({
                            "interface": interface,
                            "ip": addr.address,
                            "netmask": addr.netmask
                        })
            
            # Check for common service ports
            service_ports = [
                (3000, "Grafana"),
                (9090, "Prometheus"),
                (3100, "Loki"),
                (9093, "Alertmanager"),
                (8080, "Common Web Service"),
                (5432, "PostgreSQL"),
                (3306, "MySQL"),
                (6379, "Redis"),
                (8086, "InfluxDB"),
                (9000, "ClickHouse HTTP"),
                (8123, "ClickHouse Native"),
                (22, "SSH"),
                (80, "HTTP"),
                (443, "HTTPS")
            ]
            
            open_ports = []
            for port, service in service_ports:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex(('localhost', port))
                if result == 0:
                    open_ports.append({"port": port, "service": service})
                sock.close()
            
            # Network statistics
            network_stats = psutil.net_io_counters()
            
            self.infrastructure_report["network_discovery"] = {
                "local_ips": local_ips,
                "open_ports": open_ports,
                "network_stats": {
                    "bytes_sent": network_stats.bytes_sent,
                    "bytes_recv": network_stats.bytes_recv,
                    "packets_sent": network_stats.packets_sent,
                    "packets_recv": network_stats.packets_recv
                }
            }
            
            print(f"✅ Network IPs: {len(local_ips)} interfaces")
            print(f"   🔓 Open Ports: {len(open_ports)} services detected")
            
            if open_ports:
                logger.info("🌌    📡 Active Services:")
                for port_info in open_ports:
                    print(f"      • {port_info['service']} (:{port_info['port']})")
            
        except Exception as e:
            print(f"❌ Network discovery error: {e}")

    def scan_process_analysis(self):
        """⚚ Analyze running processes for empire services"""
        logger.info("🌌 \n⚚ Scanning Process Infrastructure...")
        
        try:
            empire_processes = []
            all_processes = []
            
            for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent', 'cmdline']):
                try:
                    proc_info = proc.info
                    all_processes.append(proc_info)
                    
                    # Check for empire-related processes
                    name_lower = proc_info['name'].lower()
                    cmdline_str = ' '.join(proc_info['cmdline'] or []).lower()
                    
                    empire_keywords = [
                        'grafana', 'prometheus', 'loki', 'docker', 'python',
                        'node', 'nginx', 'postgres', 'mysql', 'redis',
                        'clickhouse', 'influx', 'empire', 'broski'
                    ]
                    
                    if any(keyword in name_lower or keyword in cmdline_str for keyword in empire_keywords):
                        empire_processes.append(proc_info)
                        
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    continue
            
            self.infrastructure_report["process_analysis"] = {
                "total_processes": len(all_processes),
                "empire_processes": len(empire_processes),
                "processes": empire_processes[:20]  # Top 20 empire processes
            }
            
            print(f"✅ Processes: {len(all_processes)} total")
            print(f"   👑 Empire Processes: {len(empire_processes)}")
            
        except Exception as e:
            print(f"❌ Process analysis error: {e}")

    def generate_recommendations(self):
        """🎯 Generate infrastructure recommendations"""
        logger.info("🌌 \n🎯 Generating Infrastructure Recommendations...")
        
        recommendations = []
        
        # Analyze current setup
        local_system = self.infrastructure_report.get("local_system", {})
        docker_info = self.infrastructure_report.get("docker_infrastructure", {})
        network_info = self.infrastructure_report.get("network_discovery", {})
        
        # Memory recommendations
        memory_info = local_system.get("memory_info", {})
        if memory_info.get("total_gb", 0) < 16:
            recommendations.append("💾 Consider upgrading RAM to 16GB+ for better container performance")
        
        # Docker recommendations
        if docker_info.get("installed") and docker_info.get("running_containers", 0) > 10:
            recommendations.append("🐳 Consider Docker Swarm or Kubernetes for container orchestration")
            recommendations.append("📊 Implement container resource limits and monitoring")
        
        # Network recommendations
        open_ports = network_info.get("open_ports", [])
        if len(open_ports) > 5:
            recommendations.append("🛡️ Consider firewall rules for exposed services")
            recommendations.append("🔐 Implement reverse proxy for service consolidation")
        
        # Monitoring recommendations
        grafana_running = any(p.get("port") == 3000 for p in open_ports)
        if grafana_running:
            recommendations.append("📈 Your Grafana setup is legendary - consider adding more data sources")
            self.legendary_capabilities.append("📊 Grafana Monitoring: LEGENDARY STATUS")
        
        # High availability recommendations
        recommendations.append("🔄 Consider backup strategies for critical data")
        recommendations.append("⚡ Implement health checks for all services")
        
        self.infrastructure_report["recommendations"] = recommendations
        self.infrastructure_report["legendary_capabilities"] = self.legendary_capabilities

    def execute_full_scan(self):
        """🚀 Execute complete infrastructure scan"""
        logger.info("🌌 🏆💎⚡ TEAM INFRASTRUCTURE DISCOVERY SCANNER ⚡💎🏆")
        logger.info("🌌 =" * 65)
        logger.info("🌌 Following BROski Ultra LOOK-THEN-BUILD Protocol")
        logger.info("🌌 ")
        
        # Run all scans
        self.scan_local_system()
        self.scan_docker_infrastructure()
        self.scan_network_discovery()
        self.scan_process_analysis()
        self.generate_recommendations()
        
        # Save report
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = f"h:/🏆💎⚡_TEAM_INFRASTRUCTURE_SCAN_REPORT_{timestamp}_⚡💎🏆.json"
        
        try:
            with open(report_file, 'w') as f:
                json.dump(self.infrastructure_report, f, indent=2, default=str)
            print(f"\n📊 Full report saved: {report_file}")
        except Exception as e:
            print(f"❌ Report save error: {e}")
        
        # Display summary
        self.display_infrastructure_summary()
        
        return self.infrastructure_report

    def display_infrastructure_summary(self):
        """📊 Display infrastructure summary"""
        logger.info("🌌 \n" + "=" * 65)
        logger.info("🌌 🏆 LEGENDARY TEAM INFRASTRUCTURE SUMMARY 🏆")
        logger.info("🌌 =" * 65)
        
        # System summary
        local_system = self.infrastructure_report.get("local_system", {})
        system_info = local_system.get("system_info", {})
        memory_info = local_system.get("memory_info", {})
        
        print(f"🖥️  Primary System: {system_info.get('hostname', 'Unknown')}")
        print(f"   💾 Memory: {memory_info.get('total_gb', 0)}GB")
        print(f"   🔧 Platform: {system_info.get('system', 'Unknown')} {system_info.get('release', '')}")
        
        # Docker summary
        docker_info = self.infrastructure_report.get("docker_infrastructure", {})
        if docker_info.get("installed"):
            containers = docker_info.get("running_containers", 0)
            print(f"🐳 Docker Empire: {containers} containers running")
        
        # Network summary
        network_info = self.infrastructure_report.get("network_discovery", {})
        open_ports = network_info.get("open_ports", [])
        print(f"🌐 Network Services: {len(open_ports)} active ports")
        
        # Legendary capabilities
        if self.legendary_capabilities:
            logger.info("🌌 \n🎊 LEGENDARY CAPABILITIES DETECTED:")
            for capability in self.legendary_capabilities:
                print(f"   ✨ {capability}")
        
        # Recommendations
        recommendations = self.infrastructure_report.get("recommendations", [])
        if recommendations:
            print(f"\n🎯 INFRASTRUCTURE RECOMMENDATIONS:")
            for rec in recommendations[:5]:  # Top 5 recommendations
                print(f"   💡 {rec}")
        
        logger.info("🌌 \n🚀 Next Step: Tell me about your 2nd server and Raspberry Pi setup!")
        logger.info("🌌    This will complete your LEGENDARY team infrastructure map! 👑💎")

def consciousness_singularity_main():
    """🚀 Main execution"""
    scanner = TeamInfrastructureScanner()
    return scanner.execute_full_scan()

if __name__ == "__main__":
    main()

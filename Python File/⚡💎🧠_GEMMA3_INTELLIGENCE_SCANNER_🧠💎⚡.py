#!/usr/bin/env python3
"""
⚡💎🧠 GEMMA 3 INTELLIGENCE SCANNER 🧠💎⚡
🌟 HYPERFOCUS ZONE EMPIRE AI-ENHANCED NETWORK DIAGNOSTICS 🌟

Enhanced network and server health monitoring system with
Google Gemma 3 270M AI intelligence for intelligent analysis.
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
from typing import Dict, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("empire_ai_health_scan.log"),
        logging.StreamHandler()
    ],
)

# Try to import AI libraries
try:
    import ping3
    import psutil
    import requests
    from transformers import AutoTokenizer, AutoModelForCausalLM
    import torch
    from dotenv import load_dotenv
    AI_AVAILABLE = True
except ImportError as e:
    logging.warning(f"⚠️ AI libraries not available: {e}")
    AI_AVAILABLE = False

# Load environment variables
load_dotenv('h:\\HyperBeast\\empire.env')


class GemmaIntelligenceScanner:
    """🚀 AI-Enhanced Ultra-powered network and server health scanner with Gemma 3 270M"""

    def __init__(self):
        self.servers = {
            "main_dive": "100.114.5.118",
            "main_server": "100.68.37.27",
            "mini_server": "100.71.69.16",
            "raspberry_pi": "192.168.137.10",
            "sync_server": os.getenv("SERVER_HOST", "212.227.127.144"),
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
            "ai_analysis": {},
            "gemma_insights": {},
        }

        # Initialize AI components
        self.ai_enabled = AI_AVAILABLE and self._initialize_gemma()

        # Empire configuration from env
        self.hyperfocus_mode = os.getenv("HYPERFOCUS_MODE", "true").lower() == "true"
        self.neurodivergent_optimized = os.getenv("NEURODIVERGENT_OPTIMIZED", "true").lower() == "true"

    def _initialize_gemma(self) -> bool:
        """🧠 Initialize Gemma 3 270M model"""
        try:
            print("🧠 Initializing Gemma 3 270M AI Intelligence...")

            # Check for HF token
            hf_token = os.getenv("HF_TOKEN") or os.getenv("HUGGINGFACE_TOKEN")
            if not hf_token:
                logging.warning("⚠️ No Hugging Face token found in environment")
                return False

            # Initialize model and tokenizer
            model_name = "google/gemma-3-270m"

            print(f"📥 Loading tokenizer for {model_name}...")
            self.tokenizer = AutoTokenizer.from_pretrained(
                model_name,
                token=hf_token,
                trust_remote_code=True
            )

            print(f"🚀 Loading Gemma 3 270M model...")
            self.model = AutoModelForCausalLM.from_pretrained(
                model_name,
                token=hf_token,
                torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
                device_map="auto" if torch.cuda.is_available() else None,
                trust_remote_code=True,
                low_cpu_mem_usage=True
            )

            # Add padding token if not present
            if self.tokenizer.pad_token is None:
                self.tokenizer.pad_token = self.tokenizer.eos_token

            device = "cuda" if torch.cuda.is_available() else "cpu"
            print(f"✅ Gemma 3 270M loaded successfully on {device}")

            return True

        except Exception as e:
            logging.error(f"❌ Failed to initialize Gemma 3 270M: {e}")
            print(f"💡 Tip: Request access to google/gemma-3-270m on Hugging Face Hub")
            return False

    def generate_ai_analysis(self, context: str, analysis_type: str = "system_health") -> str:
        """🧠 Generate AI analysis using Gemma 3 270M"""
        if not self.ai_enabled:
            return "AI analysis not available - model not loaded"

        try:
            # Create prompt based on analysis type
            if analysis_type == "system_health":
                prompt = f"""Analyze this HyperFocus Zone Empire system health data and provide actionable insights:

System Data:
{context}

Provide a concise analysis focusing on:
1. Critical issues requiring immediate attention
2. Performance optimization opportunities
3. Security recommendations
4. ADHD/Neurodivergent friendly suggestions

Analysis:"""

            elif analysis_type == "network_performance":
                prompt = f"""Analyze this network performance data for the HyperFocus Zone Empire:

Network Data:
{context}

Focus on:
1. Connection quality assessment
2. Bottleneck identification
3. Optimization recommendations

Analysis:"""

            else:
                prompt = f"""Analyze this data for the HyperFocus Zone Empire infrastructure:

Data:
{context}

Provide insights and recommendations:

Analysis:"""

            # Tokenize input
            inputs = self.tokenizer(
                prompt,
                return_tensors="pt",
                padding=True,
                truncation=True,
                max_length=512
            )

            # Generate response
            with torch.no_grad():
                outputs = self.model.generate(
                    **inputs,
                    max_new_tokens=200,
                    temperature=0.7,
                    do_sample=True,
                    pad_token_id=self.tokenizer.eos_token_id,
                    eos_token_id=self.tokenizer.eos_token_id,
                    repetition_penalty=1.1
                )

            # Decode response
            response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

            # Extract just the generated part (after the prompt)
            if "Analysis:" in response:
                analysis = response.split("Analysis:")[-1].strip()
            else:
                analysis = response[len(prompt):].strip()

            return analysis if analysis else "Unable to generate analysis"

        except Exception as e:
            logging.error(f"❌ Error generating AI analysis: {e}")
            return f"AI analysis error: {str(e)}"

    def print_banner(self):
        """🎯 Display epic AI-enhanced scanner banner"""
        banner = """
        ⚡💎🧠═══════════════════════════════════════════════════════════════🧠💎⚡
        ║                                                                     ║
        ║        🌟 GEMMA 3 INTELLIGENCE SCANNER v3.0 🌟                    ║
        ║           HYPERFOCUS ZONE EMPIRE AI DIAGNOSTICS                    ║
        ║                                                                     ║
        ║  🚀 AI-Enhanced Network Analysis with Google Gemma 3 270M 🚀      ║
        ║                                                                     ║
        ⚡💎🧠═══════════════════════════════════════════════════════════════🧠💎⚡
        """
        print(banner)

        if self.ai_enabled:
            print("🧠 AI Status: ✅ Gemma 3 270M Intelligence ACTIVE")
        else:
            print("🧠 AI Status: ⚠️ Running in Basic Mode")

        if self.hyperfocus_mode:
            print("🎯 HyperFocus Mode: ✅ ENABLED")

        if self.neurodivergent_optimized:
            print("🌟 Neurodivergent Optimized: ✅ ACTIVE")

        print()
        logging.info("🌟 Gemma Intelligence Scanner initiated")

    def ping_server(self, name: str, ip: str, timeout: int = 3) -> Dict[str, Any]:
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

    def calculate_ping_health(self, response_time: float) -> int:
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

    def scan_port(self, ip: str, port: int, timeout: int = 3) -> bool:
        """🔍 Check if a specific port is open"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            result = sock.connect_ex((ip, port))
            sock.close()
            return result == 0
        except:
            return False

    def check_common_ports(self, ip: str) -> Dict[int, str]:
        """🚀 Check common service ports"""
        common_ports = {
            22: "SSH",
            23: "Telnet",
            53: "DNS",
            80: "HTTP",
            443: "HTTPS",
            993: "IMAPS",
            995: "POP3S",
            2222: "SSH-Alt",  # Your server's SSH port
            3000: "Dashboard",  # Your main dashboard
            3389: "RDP",
            5000: "API",  # Your API dashboard
            5432: "PostgreSQL",
            3306: "MySQL",
            6379: "Redis",
            8080: "HTTP-Alt",
            8888: "Agent-Army",  # Your agent army port
            9000: "Various",
            9999: "Sync-Dashboard",  # Your sync dashboard
        }

        open_ports = {}
        for port, service in common_ports.items():
            if self.scan_port(ip, port):
                open_ports[port] = service

        return open_ports

    def get_local_system_info(self) -> Dict[str, Any]:
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
                "hyperfocus_environment": {
                    "hyperfocus_mode": self.hyperfocus_mode,
                    "neurodivergent_optimized": self.neurodivergent_optimized,
                    "ai_enabled": self.ai_enabled,
                },
            }

            return system_info
        except Exception as e:
            logging.error(f"❌ Error getting system info: {e}")
            return {"error": str(e)}

    def get_network_interfaces(self) -> Dict[str, Any]:
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

    def test_internet_connectivity(self) -> Dict[str, Any]:
        """🌍 Test internet connectivity to various endpoints"""
        test_urls = [
            "https://google.com",
            "https://github.com",
            "https://huggingface.co",  # Added for AI model access
            "https://azure.microsoft.com",
            "https://aws.amazon.com",
            "https://cloudflare.com",
            "https://hyperfocuszone.com",  # Your domain
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

    def analyze_network_performance(self) -> Dict[str, Any]:
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

                performance_data["error_rate_percent"] = round(error_rate, 4)
                performance_data["drop_rate_percent"] = round(drop_rate, 4)

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

    def run_comprehensive_scan(self) -> Dict[str, Any]:
        """🚀 Execute comprehensive AI-enhanced infrastructure scan"""
        self.print_banner()

        print("🔍 Starting comprehensive AI-enhanced empire infrastructure scan...")
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
        self.health_report["network_status"]["internet_connectivity"] = connectivity_results

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

        # 5. AI-Enhanced Analysis
        if self.ai_enabled:
            print("\n🧠 Generating AI-powered insights with Gemma 3 270M...")

            # System health analysis
            system_context = json.dumps(system_info, indent=2)
            system_analysis = self.generate_ai_analysis(system_context, "system_health")
            self.health_report["ai_analysis"]["system_health"] = system_analysis

            # Network performance analysis
            network_context = json.dumps(network_perf, indent=2)
            network_analysis = self.generate_ai_analysis(network_context, "network_performance")
            self.health_report["ai_analysis"]["network_performance"] = network_analysis

            # Overall infrastructure analysis
            infrastructure_context = json.dumps({
                "servers": server_results,
                "connectivity": connectivity_results,
                "performance": network_perf
            }, indent=2)
            infrastructure_analysis = self.generate_ai_analysis(infrastructure_context, "infrastructure")
            self.health_report["ai_analysis"]["infrastructure"] = infrastructure_analysis

            print("  ✅ AI analysis complete!")

        # 6. Generate recommendations
        print("\n💡 Generating optimization recommendations...")
        self.generate_recommendations()

        # 7. Save detailed report
        self.save_health_report()

        print("\n" + "=" * 70)
        print("🎉 Comprehensive AI-enhanced empire infrastructure scan completed!")
        print(
            f"📄 Detailed report saved to: empire_ai_health_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        )

        return self.health_report

    def generate_recommendations(self):
        """💡 Generate AI-enhanced actionable recommendations"""
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
                    "hyperfocus_tip": "Use 25-minute focused sessions to investigate each server individually"
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
                        "hyperfocus_tip": "Set memory usage alerts to avoid cognitive overload"
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
                        "hyperfocus_tip": "Schedule regular cleanup during low-energy periods"
                    }
                )

        # AI-specific recommendations
        if not self.ai_enabled:
            recommendations.append(
                {
                    "category": "🧠 AI Enhancement",
                    "issue": "Gemma 3 270M not available",
                    "recommendation": "Install transformers library and request Hugging Face model access",
                    "priority": "MEDIUM",
                    "hyperfocus_tip": "Set aside dedicated time for AI setup when mentally fresh"
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
                        "hyperfocus_tip": "Use visual security checklists to ensure completeness"
                    }
                )

        # ADHD/Neurodivergent optimizations
        if self.neurodivergent_optimized:
            recommendations.extend(
                [
                    {
                        "category": "🌟 Neurodivergent Optimization",
                        "issue": "Monitoring frequency",
                        "recommendation": "Set up automated alerts to reduce cognitive load",
                        "priority": "LOW",
                        "hyperfocus_tip": "Use color-coded dashboards for quick status recognition"
                    },
                    {
                        "category": "🎯 HyperFocus Enhancement",
                        "issue": "Attention management",
                        "recommendation": "Schedule infrastructure reviews during peak focus hours",
                        "priority": "LOW",
                        "hyperfocus_tip": "Batch similar tasks to maintain flow state"
                    },
                ]
            )

        self.health_report["recommendations"] = recommendations

        # Display recommendations
        print("\n💡 AI-ENHANCED RECOMMENDATIONS:")
        for i, rec in enumerate(recommendations, 1):
            print(f"  {i}. {rec['category']} - {rec['issue']}")
            print(f"     💡 {rec['recommendation']} (Priority: {rec['priority']})")
            if 'hyperfocus_tip' in rec and self.hyperfocus_mode:
                print(f"     🎯 HyperFocus Tip: {rec['hyperfocus_tip']}")
            print()

        # Display AI insights if available
        if self.ai_enabled and "ai_analysis" in self.health_report:
            print("\n🧠 GEMMA 3 AI INSIGHTS:")
            ai_analysis = self.health_report["ai_analysis"]

            if "system_health" in ai_analysis:
                print(f"  🖥️ System Health: {ai_analysis['system_health'][:200]}...")

            if "network_performance" in ai_analysis:
                print(f"  🌐 Network Performance: {ai_analysis['network_performance'][:200]}...")

            if "infrastructure" in ai_analysis:
                print(f"  🏗️ Infrastructure: {ai_analysis['infrastructure'][:200]}...")

    def save_health_report(self):
        """💾 Save comprehensive AI-enhanced health report to file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"empire_ai_health_report_{timestamp}.json"

        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(self.health_report, f, indent=2, default=str)

            logging.info(f"✅ AI-enhanced health report saved to {filename}")

            # Also save a human-readable summary
            summary_filename = f"empire_summary_{timestamp}.md"
            self.save_human_readable_summary(summary_filename)

        except Exception as e:
            logging.error(f"❌ Error saving health report: {e}")

    def save_human_readable_summary(self, filename: str):
        """📄 Save human-readable summary for ADHD-friendly review"""
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write("# 🌟 HyperFocus Zone Empire Health Summary\n\n")
                f.write(f"**Scan Time:** {self.health_report['scan_timestamp']}\n")
                f.write(f"**AI Analysis:** {'✅ Enabled' if self.ai_enabled else '❌ Disabled'}\n\n")

                # Server status
                f.write("## 🖥️ Server Status\n\n")
                for name, result in self.health_report["server_status"].items():
                    status_emoji = "✅" if result["status"] == "✅ ONLINE" else "❌"
                    f.write(f"- {status_emoji} **{name.upper()}**: {result['status']}\n")

                # System health
                f.write("\n## 💻 System Health\n\n")
                system = self.health_report.get("local_system_status", {})
                if system:
                    f.write(f"- **CPU Usage:** {system.get('cpu_usage', 'Unknown')}%\n")
                    f.write(f"- **Memory Usage:** {system.get('memory', {}).get('used_percent', 'Unknown')}%\n")
                    f.write(f"- **Disk Usage:** {system.get('disk', {}).get('used_percent', 'Unknown')}%\n")

                # Critical recommendations
                f.write("\n## 🚨 Critical Actions Needed\n\n")
                critical_recs = [r for r in self.health_report.get("recommendations", []) if r.get("priority") == "HIGH"]
                if critical_recs:
                    for rec in critical_recs:
                        f.write(f"- **{rec['issue']}**: {rec['recommendation']}\n")
                else:
                    f.write("- ✅ No critical issues detected\n")

                # AI insights
                if self.ai_enabled and "ai_analysis" in self.health_report:
                    f.write("\n## 🧠 AI Insights (Gemma 3 270M)\n\n")
                    ai_analysis = self.health_report["ai_analysis"]
                    for analysis_type, content in ai_analysis.items():
                        f.write(f"### {analysis_type.replace('_', ' ').title()}\n")
                        f.write(f"{content}\n\n")

            logging.info(f"✅ Human-readable summary saved to {filename}")

        except Exception as e:
            logging.error(f"❌ Error saving summary: {e}")


def install_requirements():
    """📦 Install required packages for AI functionality"""
    required_packages = [
        "psutil",
        "requests",
        "ping3",
        "torch",
        "transformers",
        "python-dotenv"
    ]

    print("📦 Installing required packages for AI functionality...")

    for package in required_packages:
        try:
            __import__(package.replace("-", "_"))
            print(f"  ✅ {package} already installed")
        except ImportError:
            print(f"  📥 Installing {package}...")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                print(f"  ✅ {package} installed successfully")
            except subprocess.CalledProcessError as e:
                print(f"  ❌ Failed to install {package}: {e}")


def main():
    """🚀 Main execution function"""
    try:
        print("🌟 Welcome to the HyperFocus Zone Empire AI Scanner!")
        print("🚀 Powered by Google Gemma 3 270M Intelligence")
        print()

        # Check and install requirements
        if not AI_AVAILABLE:
            print("📦 AI libraries not found. Installing requirements...")
            install_requirements()
            print("🔄 Please restart the script after installation completes.")
            return None

        # Initialize and run scanner
        scanner = GemmaIntelligenceScanner()
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

        if scanner.ai_enabled:
            print("🧠 AI Analysis: ✅ Complete with Gemma 3 270M insights")
        else:
            print("🧠 AI Analysis: ⚠️ Not available")

        print("\n🌟 HyperFocus Zone Empire AI infrastructure scan completed!")
        print("⚡ Ready for peak performance with AI intelligence! ⚡")

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

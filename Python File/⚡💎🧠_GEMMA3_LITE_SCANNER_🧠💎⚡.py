#!/usr/bin/env python3
"""
⚡💎🧠 GEMMA 3 LITE SCANNER 🧠💎⚡
🌟 HYPERFOCUS ZONE EMPIRE SMART DIAGNOSTICS 🌟

Lightweight version that works with or without AI model
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
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("empire_smart_scan.log"), logging.StreamHandler()],
)

# Try to import required libraries
try:
    import ping3
    import psutil
    import requests

    BASIC_LIBS = True
except ImportError as e:
    logging.warning(f"⚠️ Basic libraries not available: {e}")
    BASIC_LIBS = False

# Try to import AI libraries (optional)
try:
    import torch
    from dotenv import load_dotenv
    from transformers import AutoModelForCausalLM, AutoTokenizer

    AI_AVAILABLE = True
    print("🧠 AI libraries detected!")
except ImportError:
    AI_AVAILABLE = False
    print("💻 Running in standard mode (AI libraries not available)")

# Load environment variables if available
try:
    if Path("h:\\HyperBeast\\empire.env").exists():
        load_dotenv("h:\\HyperBeast\\empire.env")
        print("✅ Empire configuration loaded")
    else:
        print("⚠️ Empire.env not found - using defaults")
except Exception as e:
    print(f"⚠️ Error loading environment: {e}")


class GemmaLiteScanner:
    """🚀 Smart network and server health scanner with optional AI"""

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
            "scanner_mode": "AI-Enhanced" if AI_AVAILABLE else "Standard",
            "smart_analysis": {},
        }

        # Try to initialize AI (optional)
        self.ai_enabled = False
        if AI_AVAILABLE:
            self.ai_enabled = self._try_initialize_ai()

        # Empire configuration
        self.hyperfocus_mode = os.getenv("HYPERFOCUS_MODE", "true").lower() == "true"
        self.neurodivergent_optimized = (
            os.getenv("NEURODIVERGENT_OPTIMIZED", "true").lower() == "true"
        )

    def _try_initialize_ai(self) -> bool:
        """🧠 Try to initialize AI (fails gracefully if not available)"""
        try:
            print("🧠 Attempting to initialize Gemma 3 270M...")

            hf_token = os.getenv("HF_TOKEN") or os.getenv("HUGGINGFACE_TOKEN")
            if not hf_token:
                print("⚠️ No Hugging Face token found - AI features disabled")
                return False

            # Try to load model (may fail if not approved)
            model_name = "google/gemma-3-270m"

            self.tokenizer = AutoTokenizer.from_pretrained(
                model_name, token=hf_token, trust_remote_code=True
            )

            self.model = AutoModelForCausalLM.from_pretrained(
                model_name,
                token=hf_token,
                torch_dtype=(
                    torch.float16 if torch.cuda.is_available() else torch.float32
                ),
                device_map="auto" if torch.cuda.is_available() else None,
                trust_remote_code=True,
                low_cpu_mem_usage=True,
            )

            if self.tokenizer.pad_token is None:
                self.tokenizer.pad_token = self.tokenizer.eos_token

            print("✅ Gemma 3 270M AI intelligence loaded successfully!")
            return True

        except Exception as e:
            print(f"⚠️ AI initialization failed: {e}")
            print(
                "📝 Tip: Request access at https://huggingface.co/google/gemma-3-270m"
            )
            return False

    def generate_smart_analysis(
        self, data: dict, analysis_type: str = "general"
    ) -> str:
        """🧠 Generate analysis (AI if available, smart heuristics otherwise)"""
        if self.ai_enabled:
            return self._generate_ai_analysis(data, analysis_type)
        else:
            return self._generate_rule_based_analysis(data, analysis_type)

    def _generate_ai_analysis(self, data: dict, analysis_type: str) -> str:
        """🤖 Generate AI-powered analysis"""
        try:
            context = json.dumps(data, indent=2)[:1000]  # Limit context size

            prompt = f"""Analyze this HyperFocus Zone Empire system data:

{context}

Provide a brief analysis focusing on critical issues and optimization opportunities:

Analysis:"""

            inputs = self.tokenizer(
                prompt,
                return_tensors="pt",
                padding=True,
                truncation=True,
                max_length=512,
            )

            with torch.no_grad():
                outputs = self.model.generate(
                    **inputs,
                    max_new_tokens=150,
                    temperature=0.7,
                    do_sample=True,
                    pad_token_id=self.tokenizer.eos_token_id,
                    repetition_penalty=1.1,
                )

            response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

            if "Analysis:" in response:
                analysis = response.split("Analysis:")[-1].strip()
            else:
                analysis = response[len(prompt) :].strip()

            return analysis if analysis else "AI analysis generated successfully"

        except Exception as e:
            logging.error(f"❌ AI analysis error: {e}")
            return f"AI analysis temporarily unavailable: {str(e)}"

    def _generate_rule_based_analysis(self, data: dict, analysis_type: str) -> str:
        """🎯 Generate smart rule-based analysis"""
        analysis = []

        if analysis_type == "system_health":
            memory_usage = data.get("memory", {}).get("used_percent", 0)
            cpu_usage = data.get("cpu_usage", 0)
            disk_usage = data.get("disk", {}).get("used_percent", 0)

            if memory_usage > 90:
                analysis.append("🚨 CRITICAL: Memory usage extremely high")
            elif memory_usage > 75:
                analysis.append("⚠️ WARNING: Memory usage elevated")

            if cpu_usage > 80:
                analysis.append("🚨 CRITICAL: CPU usage very high")
            elif cpu_usage > 60:
                analysis.append("⚠️ WARNING: CPU usage elevated")

            if disk_usage > 90:
                analysis.append("🚨 CRITICAL: Disk space critically low")
            elif disk_usage > 80:
                analysis.append("⚠️ WARNING: Disk space running low")

            if not analysis:
                analysis.append("✅ System performance within normal parameters")

        elif analysis_type == "network":
            error_rate = data.get("error_rate_percent", 0)
            drop_rate = data.get("drop_rate_percent", 0)
            health_score = data.get("network_health_score", 100)

            if health_score < 50:
                analysis.append("🚨 CRITICAL: Network health severely degraded")
            elif health_score < 75:
                analysis.append("⚠️ WARNING: Network performance suboptimal")
            else:
                analysis.append("✅ Network performance healthy")

        elif analysis_type == "servers":
            online_count = sum(
                1 for s in data.values() if s.get("status") == "✅ ONLINE"
            )
            total_count = len(data)

            if online_count == 0:
                analysis.append("🚨 CRITICAL: All servers offline")
            elif online_count < total_count:
                offline = total_count - online_count
                analysis.append(f"⚠️ WARNING: {offline} servers offline")
            else:
                analysis.append("✅ All servers operational")

        # Add ADHD-friendly suggestions
        if self.hyperfocus_mode:
            analysis.append(
                "🎯 HyperFocus Tip: Address critical issues during peak focus hours"
            )

        return ". ".join(analysis) if analysis else "Analysis completed successfully"

    def print_banner(self):
        """🎯 Display scanner banner"""
        banner = """
        ⚡💎🧠═══════════════════════════════════════════════════════════════🧠💎⚡
        ║                                                                     ║
        ║        🌟 GEMMA 3 LITE SCANNER v1.0 🌟                            ║
        ║           HYPERFOCUS ZONE EMPIRE SMART DIAGNOSTICS                 ║
        ║                                                                     ║
        ║  🚀 Intelligent Network Analysis with Optional AI Enhancement 🚀  ║
        ║                                                                     ║
        ⚡💎🧠═══════════════════════════════════════════════════════════════🧠💎⚡
        """
        print(banner)

        if self.ai_enabled:
            print("🧠 AI Status: ✅ Gemma 3 270M Intelligence ACTIVE")
        else:
            print("🧠 AI Status: 💻 Smart Rule-Based Analysis ACTIVE")

        if self.hyperfocus_mode:
            print("🎯 HyperFocus Mode: ✅ ENABLED")

        print()

    def ping_server(self, name: str, ip: str, timeout: int = 3) -> dict:
        """🎯 Ping a server and measure response time"""
        if not BASIC_LIBS:
            return {
                "name": name,
                "ip": ip,
                "status": "⚠️ PING_UNAVAILABLE",
                "response_time_ms": None,
                "health_score": 0,
                "error": "ping3 library not available",
            }

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

    def get_local_system_info(self) -> dict:
        """💻 Get system information"""
        if not BASIC_LIBS:
            return {
                "hostname": socket.gethostname(),
                "platform": platform.platform(),
                "python_version": platform.python_version(),
                "error": "psutil library not available for detailed system info",
            }

        try:
            return {
                "hostname": socket.gethostname(),
                "platform": platform.platform(),
                "processor": platform.processor(),
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
                        round(psutil.disk_usage("C:").total / (1024**3), 2)
                        if os.name == "nt"
                        else round(psutil.disk_usage("/").total / (1024**3), 2)
                    ),
                    "free_gb": (
                        round(psutil.disk_usage("C:").free / (1024**3), 2)
                        if os.name == "nt"
                        else round(psutil.disk_usage("/").free / (1024**3), 2)
                    ),
                    "used_percent": (
                        psutil.disk_usage("C:").percent
                        if os.name == "nt"
                        else psutil.disk_usage("/").percent
                    ),
                },
                "boot_time": datetime.fromtimestamp(psutil.boot_time()).isoformat(),
                "hyperfocus_environment": {
                    "hyperfocus_mode": self.hyperfocus_mode,
                    "neurodivergent_optimized": self.neurodivergent_optimized,
                    "ai_enabled": self.ai_enabled,
                },
            }
        except Exception as e:
            logging.error(f"❌ Error getting system info: {e}")
            return {"error": str(e)}

    def test_internet_connectivity(self) -> dict:
        """🌍 Test internet connectivity"""
        if not BASIC_LIBS:
            return {"error": "requests library not available"}

        test_urls = [
            "https://google.com",
            "https://github.com",
            "https://huggingface.co",
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

    def run_smart_scan(self) -> dict:
        """🚀 Execute smart infrastructure scan"""
        self.print_banner()

        print("🔍 Starting smart empire infrastructure scan...")
        print("=" * 70)

        # 1. Test server connectivity
        print("\n🌐 Testing server connectivity...")
        server_results = {}

        if BASIC_LIBS:
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
                            f"  📡 {name.upper()}: {result['status']} ({result.get('response_time_ms', 'N/A')}ms)"
                        )
                    except Exception as e:
                        logging.error(f"❌ Error scanning {name}: {e}")
        else:
            print("  ⚠️ Network scanning requires ping3 library")
            for name, ip in self.servers.items():
                server_results[name] = {
                    "name": name,
                    "ip": ip,
                    "status": "⚠️ SCAN_UNAVAILABLE",
                    "note": "Install ping3 for network scanning",
                }

        self.health_report["server_status"] = server_results

        # 2. Test internet connectivity
        print("\n🌍 Testing internet connectivity...")
        connectivity_results = self.test_internet_connectivity()
        self.health_report["network_status"][
            "internet_connectivity"
        ] = connectivity_results

        if "error" not in connectivity_results:
            for url, result in connectivity_results.items():
                print(
                    f"  🌐 {url}: {result['status']} ({result.get('response_time_ms', 'N/A')}ms)"
                )
        else:
            print(f"  ⚠️ {connectivity_results['error']}")

        # 3. Analyze local system
        print("\n💻 Analyzing local system health...")
        system_info = self.get_local_system_info()
        self.health_report["local_system_status"] = system_info

        print(f"  🖥️  Hostname: {system_info.get('hostname', 'Unknown')}")
        if "error" not in system_info:
            print(f"  ⚡ CPU Usage: {system_info.get('cpu_usage', 'Unknown')}%")
            print(
                f"  🧠 Memory Usage: {system_info.get('memory', {}).get('used_percent', 'Unknown')}%"
            )
            print(
                f"  💾 Disk Usage: {system_info.get('disk', {}).get('used_percent', 'Unknown')}%"
            )
        else:
            print(f"  ⚠️ {system_info['error']}")

        # 4. Generate smart analysis
        print("\n🧠 Generating smart analysis...")

        # System analysis
        system_analysis = self.generate_smart_analysis(system_info, "system_health")
        self.health_report["smart_analysis"]["system_health"] = system_analysis

        # Server analysis
        server_analysis = self.generate_smart_analysis(server_results, "servers")
        self.health_report["smart_analysis"]["server_status"] = server_analysis

        # Network analysis
        if "error" not in connectivity_results:
            network_analysis = self.generate_smart_analysis(
                connectivity_results, "network"
            )
            self.health_report["smart_analysis"][
                "network_connectivity"
            ] = network_analysis

        print("  ✅ Smart analysis complete!")

        # 5. Save report
        self.save_health_report()

        print("\n" + "=" * 70)
        print("🎉 Smart empire infrastructure scan completed!")
        print(
            f"📄 Report saved to: empire_smart_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        )

        return self.health_report

    def save_health_report(self):
        """💾 Save health report"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"empire_smart_report_{timestamp}.json"

        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(self.health_report, f, indent=2, default=str)
            logging.info(f"✅ Smart health report saved to {filename}")

            # Also save readable summary
            summary_filename = f"empire_smart_summary_{timestamp}.md"
            self.save_readable_summary(summary_filename)

        except Exception as e:
            logging.error(f"❌ Error saving report: {e}")

    def save_readable_summary(self, filename: str):
        """📄 Save ADHD-friendly summary"""
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write("# 🌟 HyperFocus Zone Empire Smart Health Summary\n\n")
                f.write(f"**Scan Time:** {self.health_report['scan_timestamp']}\n")
                f.write(f"**Scanner Mode:** {self.health_report['scanner_mode']}\n\n")

                # System status
                system = self.health_report.get("local_system_status", {})
                f.write("## 💻 System Status\n\n")
                if "error" not in system:
                    f.write(f"- **CPU Usage:** {system.get('cpu_usage', 'Unknown')}%\n")
                    f.write(
                        f"- **Memory Usage:** {system.get('memory', {}).get('used_percent', 'Unknown')}%\n"
                    )
                    f.write(
                        f"- **Disk Usage:** {system.get('disk', {}).get('used_percent', 'Unknown')}%\n"
                    )
                else:
                    f.write(f"- **Status:** {system['error']}\n")

                # Server status
                f.write("\n## 🖥️ Server Status\n\n")
                for name, result in self.health_report["server_status"].items():
                    status_emoji = (
                        "✅" if "ONLINE" in result.get("status", "") else "❌"
                    )
                    f.write(
                        f"- {status_emoji} **{name.upper()}**: {result.get('status', 'Unknown')}\n"
                    )

                # Smart analysis
                f.write("\n## 🧠 Smart Analysis\n\n")
                smart_analysis = self.health_report.get("smart_analysis", {})
                for analysis_type, content in smart_analysis.items():
                    f.write(f"### {analysis_type.replace('_', ' ').title()}\n")
                    f.write(f"{content}\n\n")

            logging.info(f"✅ Readable summary saved to {filename}")

        except Exception as e:
            logging.error(f"❌ Error saving summary: {e}")


def install_missing_packages():
    """📦 Install missing packages if needed"""
    if not BASIC_LIBS:
        print("📦 Installing basic packages...")
        packages = ["psutil", "requests", "ping3"]

        for package in packages:
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                print(f"✅ {package} installed")
            except:
                print(f"❌ Failed to install {package}")


def main():
    """🚀 Main execution function"""
    try:
        print("🌟 Welcome to the HyperFocus Zone Empire Smart Scanner!")

        if not BASIC_LIBS:
            print("📦 Some libraries missing. Installing...")
            install_missing_packages()
            print("🔄 Please restart the script after installation.")
            return

        # Run scanner
        scanner = GemmaLiteScanner()
        health_report = scanner.run_smart_scan()

        # Display summary
        print("\n🏆 EMPIRE HEALTH SUMMARY:")
        print("=" * 50)

        # System info
        system_info = health_report.get("local_system_status", {})
        if "error" not in system_info:
            print(
                f"🧠 Memory Usage: {system_info.get('memory', {}).get('used_percent', 'Unknown')}%"
            )
            print(
                f"💾 Disk Usage: {system_info.get('disk', {}).get('used_percent', 'Unknown')}%"
            )

        # Server status
        online_servers = sum(
            1
            for result in health_report["server_status"].values()
            if "ONLINE" in result.get("status", "")
        )
        total_servers = len(health_report["server_status"])
        print(f"🖥️  Servers Online: {online_servers}/{total_servers}")

        # AI status
        if scanner.ai_enabled:
            print("🧠 AI Analysis: ✅ Gemma 3 270M Active")
        else:
            print("🧠 Analysis: 💻 Smart Rule-Based")

        print("\n🌟 Smart empire scan completed!")
        print("⚡ Your HyperFocus Zone is optimized for peak performance! ⚡")

        return health_report

    except KeyboardInterrupt:
        print("\n⚠️ Scan interrupted by user")
        return None
    except Exception as e:
        print(f"❌ Error: {e}")
        return None


if __name__ == "__main__":
    main()

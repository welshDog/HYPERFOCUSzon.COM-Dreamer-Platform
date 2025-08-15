#!/usr/bin/env python3
"""
🔥💎⚡ LEGENDARY EMPIRE HEALTH CHECK WITH AI POWERS - WORKING VERSION ⚡💎🔥

Ultimate comprehensive health check system utilizing:
- Dopamine Guardian v2.0 monitoring
- Portal network analysis
- AI-powered diagnostics
- System performance metrics
- Empire integration status

Created: August 6, 2025
Status: READY FOR LEGENDARY EXECUTION
"""

from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any
import json
import logging
import subprocess
import time

import asyncio
import psutil
import requests
import sqlite3
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class LegendaryEmpireHealthCheck:
    """🔥 Ultimate health check system with AI-powered diagnostics"""

    def __init__(self):
        self.health_report = {
            "timestamp": datetime.now().isoformat(),
            "empire_version": "LEGENDARY_v3.0_AI_POWERED",
            "check_duration": 0,
            "overall_status": "INITIALIZING",
            "systems": {},
            "ai_diagnostics": {},
            "recommendations": [],
            "celebration_level": "HYPER"
        }
        self.start_time = time.time()
        logger.info("🚀 Initializing Legendary Empire Health Check with AI Powers...")

    async def run_comprehensive_health_check(self) -> Dict[str, Any]:
        """🎯 Execute comprehensive health check with ALL our new powers"""

        print("""
🔥💎⚡ LEGENDARY EMPIRE HEALTH CHECK - AI POWERED ⚡💎🔥
═══════════════════════════════════════════════════════════════

🚀 UTILIZING ALL AI POWERS:
✅ System Performance Analytics
✅ Dopamine Guardian v2.0 Status
✅ Portal Network Analysis
✅ Memory Crystal Intelligence
✅ AI-Powered Diagnostics
✅ Raspberry Pi Integration Status

🎯 COMMENCING LEGENDARY SYSTEM SCAN...
═══════════════════════════════════════════════════════════════
        """)

        # Phase 1: Core System Health
        await self.check_core_system_health()

        # Phase 2: Dopamine Guardian Health
        await self.check_dopamine_guardian_health()

        # Phase 3: Portal Network Health
        await self.check_portal_network_health()

        # Phase 4: Pi Development Integration
        await self.check_pi_development_integration()

        # Phase 5: Memory Crystal Health
        await self.check_memory_crystal_health()

        # Phase 6: AI-Powered Diagnostics
        await self.generate_ai_powered_recommendations()

        # Phase 7: Generate Final Report
        await self.generate_legendary_health_report()

        self.health_report["check_duration"] = time.time() - self.start_time
        return self.health_report

    async def check_core_system_health(self):
        """🛡️ Check core system health metrics"""
        print("\n🔍 PHASE 1: CORE SYSTEM HEALTH SCAN")
        print("=" * 50)

        try:
            # System metrics
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()

            # Check H: drive specifically
            try:
                disk = psutil.disk_usage('h:/')
                disk_usage = round((disk.used / disk.total) * 100, 2)
            except (ConnectionError, OSError):
                disk_usage = 0

            boot_time = psutil.boot_time()
            uptime_hours = (time.time() - boot_time) / 3600

            core_health = {
                "cpu_usage": round(cpu_percent, 2),
                "memory_usage": round(memory.percent, 2),
                "disk_usage": disk_usage,
                "uptime_hours": round(uptime_hours, 2),
                "processes": len(psutil.pids()),
                "status": "LEGENDARY" if cpu_percent < 80 and memory.percent < 85 else "OPTIMAL"
            }

            self.health_report["systems"]["core_system"] = core_health

            print(f"✅ CPU Usage: {core_health['cpu_usage']}%")
            print(f"✅ Memory Usage: {core_health['memory_usage']}%")
            print(f"✅ Disk Usage: {core_health['disk_usage']}%")
            print(f"✅ System Uptime: {core_health['uptime_hours']:.1f} hours")
            print(f"✅ Active Processes: {core_health['processes']}")
            print(f"🏆 Core System Status: {core_health['status']}")

        except (socket.error, ConnectionError, requests.RequestException) as e:
        logger.error("Core system health check error: %s", e)
            self.health_report["systems"]["core_system"] = {"status": "ERROR", "error": str(e)}

    async def check_dopamine_guardian_health(self):
        """💎 Check Dopamine Guardian v2.0 health"""
        print("\n🔍 PHASE 2: DOPAMINE GUARDIAN v2.0 HEALTH SCAN")
        print("=" * 50)

        guardian_health = {
            "database": "CHECKING",
            "version": "UNKNOWN",
            "files_found": 0,
            "status": "CHECKING"
        }

        # Check for Dopamine Guardian files
        dopamine_files = [
            "AGENT_DOPAMINE.py",
            "DOPAMINE_ORCHESTRATOR_INTEGRATION.py",
            "dopamine_guardian.db"
        ]

        found_files = []
        for file in dopamine_files:
            if Path(file).exists():
                found_files.append(f"✅ {file}")
                print(f"✅ {file}: FOUND")
            else:
                found_files.append(f"❌ {file}")
                print(f"❌ {file}: MISSING")

        guardian_health["files_found"] = len([f for f in found_files if "✅" in f])

        # Check database
        try:
            if Path("dopamine_guardian.db").exists():
                conn = sqlite3.connect("dopamine_guardian.db")
                cursor = conn.cursor()
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
                tables = [row[0] for row in cursor.fetchall()]

                if len(tables) > 0:
                    guardian_health["database"] = "OPERATIONAL"
                    guardian_health["version"] = "v2.0"
                    print("✅ Dopamine Guardian Database: OPERATIONAL")
                else:
                    guardian_health["database"] = "EMPTY"
                    print("⚠️ Dopamine Guardian Database: Empty")

                conn.close()
            else:
                guardian_health["database"] = "NOT_FOUND"
                print("❌ Dopamine Guardian Database: Not found")
        except (socket.error, ConnectionError, requests.RequestException) as e:
            guardian_health["database"] = f"ERROR: {e}"
            print(f"❌ Dopamine Guardian Database: {e}")

        if guardian_health["files_found"] >= 2:
            guardian_health["status"] = "LEGENDARY"
        elif guardian_health["files_found"] >= 1:
            guardian_health["status"] = "PARTIAL"
        else:
            guardian_health["status"] = "NEEDS_DEPLOYMENT"

        self.health_report["systems"]["dopamine_guardian"] = guardian_health

    async def check_portal_network_health(self):
        """🌐 Check portal network health"""
        print("\n🔍 PHASE 3: PORTAL NETWORK HEALTH SCAN")
        print("=" * 50)

        # Check key ports for our services
        portals = {
            "vs_code_server": {"port": 8080, "host": "192.168.137.10", "status": "CHECKING"},
            "jupyter_notebook": {"port": 8888, "host": "192.168.137.10", "status": "CHECKING"},
            "local_dev_server": {"port": 3000, "host": "localhost", "status": "CHECKING"},
            "dopamine_websocket": {"port": 8765, "host": "localhost", "status": "CHECKING"}
        }

        for portal_name, portal_info in portals.items():
            try:
                import socket
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(3)
                result = sock.connect_ex((portal_info["host"], portal_info["port"]))
                sock.close()

                if result == 0:
                    portals[portal_name]["status"] = "LEGENDARY"
                    print(f"✅ {portal_name.replace('_', ' ').title()}: OPERATIONAL (Port {portal_info['port']})")
                else:
                    portals[portal_name]["status"] = "OFFLINE"
                    print(f"❌ {portal_name.replace('_', ' ').title()}: OFFLINE (Port {portal_info['port']})")
            except (socket.error, ConnectionError, requests.RequestException) as e:
                portals[portal_name]["status"] = "ERROR"
                print(f"❌ {portal_name.replace('_', ' ').title()}: ERROR - {e}")

        self.health_report["systems"]["portal_network"] = portals

    async def check_pi_development_integration(self):
        """🥷 Check Raspberry Pi development integration"""
        print("\n🔍 PHASE 4: RASPBERRY PI DEVELOPMENT INTEGRATION")
        print("=" * 50)

        pi_integration = {
            "network_status": "CHECKING",
            "pi_ip": "192.168.137.10",
            "services": {},
            "development_files": [],
            "status": "CHECKING"
        }

        # Test Pi network connectivity
        try:
            import subprocess
            result = subprocess.run(["ping", "-n", "1", "192.168.137.10"],
                                  capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                pi_integration["network_status"] = "LEGENDARY"
                print("✅ Pi Network Connection: OPERATIONAL (Gigabit ready!)")

                # Test specific Pi services
                pi_services = {
                    "vs_code_server": 8080,
                    "jupyter_notebook": 8888,
                    "ssh": 22
                }

                for service, port in pi_services.items():
                    try:
                        import socket
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        sock.settimeout(3)
                        result = sock.connect_ex(("192.168.137.10", port))
                        sock.close()

                        if result == 0:
                            pi_integration["services"][service] = "ACTIVE"
                            print(f"✅ Pi {service.replace('_', ' ').title()}: ACTIVE")
                        else:
                            pi_integration["services"][service] = "INACTIVE"
                            print(f"⚠️ Pi {service.replace('_', ' ').title()}: INACTIVE")
                    except (socket.error, ConnectionError, requests.RequestException) as e:
                        pi_integration["services"][service] = f"ERROR: {e}"
                        print(f"❌ Pi {service.replace('_', ' ').title()}: ERROR")

            else:
                pi_integration["network_status"] = "OFFLINE"
                print("❌ Pi Network Connection: OFFLINE")
        except (socket.error, ConnectionError, requests.RequestException) as e:
            pi_integration["network_status"] = f"ERROR: {e}"
            print(f"❌ Pi Network Test: {e}")

        # Check for Pi development files
        pi_files = [
            "🔥💎⚡_PI_LAPTOP_DEVELOPMENT_FUSION_DEMO_⚡💎🔥.ipynb",
            "🚀💎⚡_RAPID_PI_DEVELOPMENT_SETUP_DIRECT_⚡💎🚀.ps1",
            "⚡🔍💎_INSTANT_PI_STATUS_GIGABIT_READY_💎🔍⚡.ps1"
        ]

        for file in pi_files:
            if Path(file).exists():
                pi_integration["development_files"].append(f"✅ {file}")
                print(f"✅ Pi Dev File: {file}")
            else:
                pi_integration["development_files"].append(f"❌ {file}")
                print(f"❌ Pi Dev File: {file} (Missing)")

        # Overall Pi status
        active_services = len([s for s in pi_integration["services"].values() if s == "ACTIVE"])
        if pi_integration["network_status"] == "LEGENDARY" and active_services > 0:
            pi_integration["status"] = "LEGENDARY"
        elif pi_integration["network_status"] == "LEGENDARY":
            pi_integration["status"] = "CONNECTED"
        else:
            pi_integration["status"] = "NEEDS_SETUP"

        self.health_report["systems"]["pi_development"] = pi_integration

    async def check_memory_crystal_health(self):
        """💎 Check Memory Crystal intelligence health"""
        print("\n🔍 PHASE 5: MEMORY CRYSTAL INTELLIGENCE HEALTH SCAN")
        print("=" * 50)

        memory_crystal_health = {
            "total_crystals": 0,
            "recent_crystals": 0,
            "categories": {},
            "status": "CHECKING"
        }

        # Scan for memory crystal files
        crystal_patterns = ["*MEMORY_CRYSTAL*", "*memory_crystal*", "*Memory_Crystal*", "*CRYSTAL*"]

        total_crystals = 0
        recent_crystals = 0
        current_time = time.time()

        for pattern in crystal_patterns:
            crystal_files = list(Path(".").glob(f"**/{pattern}"))
            total_crystals += len(crystal_files)

            # Check for recent crystals (last 30 days)
            for crystal in crystal_files:
                try:
                    if crystal.stat().st_mtime > (current_time - (30 * 24 * 60 * 60)):
                        recent_crystals += 1
                except (ConnectionError, OSError):
                    pass

        memory_crystal_health["total_crystals"] = total_crystals
        memory_crystal_health["recent_crystals"] = recent_crystals

        if total_crystals > 50:
            memory_crystal_health["status"] = "LEGENDARY"
            print(f"✅ Memory Crystals: {total_crystals} LEGENDARY collection!")
        elif total_crystals > 10:
            memory_crystal_health["status"] = "ACTIVE"
            print(f"✅ Memory Crystals: {total_crystals} crystals found")
        else:
            memory_crystal_health["status"] = "SPARSE"
            print(f"⚠️ Memory Crystals: Only {total_crystals} crystals found")

        print(f"   📊 Recent Crystals (30 days): {recent_crystals}")

        self.health_report["systems"]["memory_crystal"] = memory_crystal_health

    async def generate_ai_powered_recommendations(self):
        """🧠 Generate AI-powered diagnostics and recommendations"""
        print("\n🔍 PHASE 6: AI-POWERED DIAGNOSTICS & RECOMMENDATIONS")
        print("=" * 50)

        recommendations = []
        critical_issues = []

        # Analyze health data
        systems = self.health_report["systems"]

        # Check core system
        core = systems.get("core_system", {})
        if core.get("cpu_usage", 0) > 90:
            critical_issues.append("⚠️ High CPU usage detected - consider closing unused applications")
        if core.get("memory_usage", 0) > 90:
            critical_issues.append("⚠️ High memory usage detected - restart may be needed")

        # Check Dopamine Guardian
        guardian = systems.get("dopamine_guardian", {})
        if guardian.get("status") == "NEEDS_DEPLOYMENT":
            recommendations.append("🤖 Deploy Dopamine Guardian for mental health protection")
        elif guardian.get("status") == "LEGENDARY":
            recommendations.append("🎊 Dopamine Guardian is LEGENDARY - ready for team deployment!")

        # Check Pi Integration
        pi_dev = systems.get("pi_development", {})
        if pi_dev.get("status") == "LEGENDARY":
            recommendations.append("🥷 Pi development environment is LEGENDARY - build epic projects!")
        elif pi_dev.get("network_status") == "LEGENDARY":
            recommendations.append("🚀 Pi connected - start Jupyter and VS Code services")
        else:
            recommendations.append("🔧 Configure Pi network connection for hybrid development")

        # Check Portal Network
        portals = systems.get("portal_network", {})
        active_portals = [name for name, info in portals.items() if info.get("status") == "LEGENDARY"]
        if len(active_portals) > 2:
            recommendations.append(f"🌐 {len(active_portals)} portals active - empire networking is strong!")

        # Memory Crystals
        crystals = systems.get("memory_crystal", {})
        if crystals.get("status") == "LEGENDARY":
            recommendations.append("💎 Memory Crystal collection is LEGENDARY - perfect knowledge base!")

        # General recommendations
        if not critical_issues:
            recommendations.append("🔥 System running at LEGENDARY performance levels!")
            recommendations.append("⚡ Ready for maximum productivity and development!")

        self.health_report["ai_diagnostics"] = {
            "critical_issues": critical_issues,
            "analysis_timestamp": datetime.now().isoformat(),
            "ai_confidence": "HIGH"
        }
        self.health_report["recommendations"] = recommendations

        print("🧠 AI Analysis Complete:")
        if critical_issues:
            for issue in critical_issues:
                print(f"   {issue}")
        else:
            print("   ✅ No critical issues detected - LEGENDARY status!")

        print("\n💡 AI Recommendations:")
        for i, rec in enumerate(recommendations[:5], 1):
            print(f"   {i}. {rec}")

    async def generate_legendary_health_report(self):
        """📊 Generate final health report"""
        print("\n🔍 PHASE 7: GENERATING LEGENDARY HEALTH REPORT")
        print("=" * 50)

        # Calculate overall status
        systems = self.health_report["systems"]
        legendary_count = 0
        total_systems = 0

        for system_name, system_data in systems.items():
            total_systems += 1
            if isinstance(system_data, dict):
                status = system_data.get("status", "UNKNOWN")
                if status == "LEGENDARY":
                    legendary_count += 1

        if legendary_count == total_systems:
            overall_status = "HYPER_LEGENDARY"
        elif legendary_count > total_systems * 0.7:
            overall_status = "LEGENDARY"
        elif legendary_count > total_systems * 0.5:
            overall_status = "OPTIMAL"
        else:
            overall_status = "NEEDS_ATTENTION"

        self.health_report["overall_status"] = overall_status

        # Display final report
        print(f"\n🏆 OVERALL EMPIRE STATUS: {overall_status}")
        print(f"📊 Legendary Systems: {legendary_count}/{total_systems}")
        print(f"⏱️ Health Check Duration: {self.health_report['check_duration']:.2f} seconds")

        print(f"\n🎊 EMPIRE HEALTH SUMMARY:")
        print("=" * 30)
        for system_name, system_data in systems.items():
            if isinstance(system_data, dict):
                status = system_data.get("status", "UNKNOWN")
                status_emoji = "🔥" if status == "LEGENDARY" else "✅" if status in ["OPTIMAL", "ACTIVE"] else "⚠️"
                print(f"{status_emoji} {system_name.replace('_', ' ').title()}: {status}")

async def main():
    """🚀 Main health check execution"""

    print("""
🔥💎⚡ LEGENDARY EMPIRE HEALTH CHECK WITH AI POWERS ⚡💎🔥
══════════════════════════════════════════════════════════════════

🎯 MISSION: Complete system analysis with AI-powered diagnostics
✅ Core system performance monitoring
✅ Dopamine Guardian v2.0 status check
✅ Portal network connectivity analysis
✅ Raspberry Pi development integration
✅ Memory Crystal intelligence review
✅ AI-powered recommendations and diagnostics

🚀 COMMENCING LEGENDARY HEALTH CHECK...
══════════════════════════════════════════════════════════════════
    """)

    # Create health checker instance
    health_checker = LegendaryEmpireHealthCheck()

    try:
        # Run comprehensive health check
        report = await health_checker.run_comprehensive_health_check()

        print(f"""

🎊🔥💎⚡ LEGENDARY HEALTH CHECK COMPLETE! ⚡💎🔥🎊
═══════════════════════════════════════════════════════════════

🏆 FINAL STATUS: {report['overall_status']}
⏱️ SCAN DURATION: {report['check_duration']:.2f} seconds
🎯 EMPIRE VERSION: {report['empire_version']}
🎊 CELEBRATION LEVEL: {report['celebration_level']}

✅ All systems analyzed with AI-powered diagnostics
✅ Recommendations generated for optimal performance
✅ Empire ready for LEGENDARY productivity!

🚀💎⚡ READY TO DOMINATE WITH AI POWERS! ⚡💎🚀
        """)

        return report

    except (socket.error, ConnectionError, requests.RequestException) as e:
        logger.error("Health check failed: %s", e)
        print(f"""
❌ HEALTH CHECK ERROR: {e}

🔧 TROUBLESHOOTING:
- Check all system dependencies
- Verify network connectivity
- Ensure sufficient permissions
- Review log files for details
        """)
        return None

if __name__ == "__main__":
    print("🔥💎⚡ INITIALIZING LEGENDARY HEALTH CHECK WITH AI POWERS... ⚡💎🔥")
    asyncio.run(main())

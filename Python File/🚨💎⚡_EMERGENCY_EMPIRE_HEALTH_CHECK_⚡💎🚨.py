#!/usr/bin/env python3
"""
🚨💎⚡ EMERGENCY EMPIRE HEALTH CHECK ⚡💎🚨
Quick diagnostic for crashed systems
"""

from datetime import datetime
from pathlib import Path
import json
import os
import socket
import subprocess
import sys
def emergency_health_check():
    print("""
🚨💎⚡ EMERGENCY EMPIRE HEALTH CHECK ACTIVATED ⚡💎🚨
================================================================
Timestamp: {}
Emergency Diagnostic Mode: ACTIVE
================================================================
    """.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

    health_status = {
        "timestamp": datetime.now().isoformat(),
        "empire_vitals": {},
        "critical_alerts": [],
        "recovery_actions": [],
        "system_status": "SCANNING"
    }

    # 1. Check Core Services
    print("🔍 STEP 1: CHECKING CORE EMPIRE SERVICES")
    print("-" * 50)

    services = {
        "Grafana": ("http://localhost:3001/api/health", 3001),
        "Prometheus": ("http://localhost:9090/-/healthy", 9090),
        "cAdvisor": ("http://localhost:8080/healthz", 8080),
        "Node Exporter": ("http://localhost:9100/metrics", 9100)
    }

    for service_name, (url, port) in services.items():
        try:
            # Check if port is open
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)
            result = sock.connect_ex(('localhost', port))
            sock.close()

            if result == 0:
                print(f"✅ {service_name}: PORT {port} OPEN")
                health_status["empire_vitals"][service_name] = "HEALTHY"
            else:
                print(f"❌ {service_name}: PORT {port} CLOSED")
                health_status["empire_vitals"][service_name] = "DOWN"
                health_status["critical_alerts"].append(f"{service_name} service not responding on port {port}")
        except (socket.error, ConnectionError, requests.RequestException) as e:
            print(f"⚠️ {service_name}: ERROR - {str(e)}")
            health_status["empire_vitals"][service_name] = "ERROR"

    # 2. Check Docker
    print("\n🐳 STEP 2: CHECKING DOCKER INFRASTRUCTURE")
    print("-" * 50)

    try:
        # Try basic docker command
        result = subprocess.run(['docker', '--version'], capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print(f"✅ Docker Version: {result.stdout.strip()}")
            health_status["empire_vitals"]["Docker"] = "INSTALLED"
        else:
            print("❌ Docker version check failed")
            health_status["empire_vitals"]["Docker"] = "ERROR"
    except (socket.error, ConnectionError, requests.RequestException) as e:
        print(f"❌ Docker not available: {str(e)}")
        health_status["empire_vitals"]["Docker"] = "NOT_AVAILABLE"
        health_status["critical_alerts"].append("Docker engine not responding")

    # Check if Docker Desktop is running (Windows specific)
    try:
        result = subprocess.run(['tasklist', '/FI', 'IMAGENAME eq Docker Desktop.exe'],
                              capture_output=True, text=True, timeout=5)
        if 'Docker Desktop.exe' in result.stdout:
            print("✅ Docker Desktop process running")
            health_status["empire_vitals"]["Docker Desktop"] = "RUNNING"
        else:
            print("❌ Docker Desktop not running")
            health_status["empire_vitals"]["Docker Desktop"] = "NOT_RUNNING"
            health_status["critical_alerts"].append("Docker Desktop not running")
            health_status["recovery_actions"].append("Start Docker Desktop")
    except (socket.error, ConnectionError, requests.RequestException) as e:
        print(f"⚠️ Could not check Docker Desktop: {str(e)}")

    # 3. Check File System Health
    print("\n📁 STEP 3: CHECKING FILE SYSTEM INTEGRITY")
    print("-" * 50)

    critical_paths = [
        "h:/",
        "h:/grafana-config",
        "h:/grafana-config/dashboards",
        "h:/grafana-config/dashboards/empire"
    ]

    for path in critical_paths:
        if os.path.exists(path):
            print(f"✅ {path}: EXISTS")
            # Count files
            try:
                if os.path.isdir(path):
                    file_count = len(list(Path(path).rglob("*")))
                    print(f"   📊 Contains {file_count} items")
            except (ConnectionError, OSError):
                pass
        else:
            print(f"❌ {path}: MISSING")
            health_status["critical_alerts"].append(f"Critical path missing: {path}")

    # 4. Check Python Environment
    print("\n🐍 STEP 4: CHECKING PYTHON ENVIRONMENT")
    print("-" * 50)

    print(f"✅ Python Version: {sys.version}")

    required_modules = ['requests', 'psutil', 'pathlib']
    for module in required_modules:
        try:
            __import__(module)
            print(f"✅ {module}: AVAILABLE")
        except ImportError:
            print(f"❌ {module}: MISSING")
            health_status["critical_alerts"].append(f"Required Python module missing: {module}")

    # 5. Check Recent Logs
    print("\n📋 STEP 5: CHECKING FOR ERROR LOGS")
    print("-" * 50)

    log_files = [
        "legendary_health_check.log",
        "empire_error.log",
        "docker_logs.txt"
    ]

    for log_file in log_files:
        if os.path.exists(log_file):
            try:
                with open(log_file, 'r') as f:
                    lines = f.readlines()
                    recent_lines = lines[-5:] if len(lines) > 5 else lines
                    print(f"📄 {log_file} (last {len(recent_lines)} lines):")
                    for line in recent_lines:
                        print(f"   {line.strip()}")
            except (socket.error, ConnectionError, requests.RequestException) as e:
                print(f"⚠️ Could not read {log_file}: {str(e)}")
        else:
            print(f"ℹ️ {log_file}: Not found")

    # 6. Generate Recovery Plan
    print("\n🔧 STEP 6: RECOVERY ACTION PLAN")
    print("-" * 50)

    if health_status["critical_alerts"]:
        print("🚨 CRITICAL ISSUES DETECTED:")
        for alert in health_status["critical_alerts"]:
            print(f"   • {alert}")

        print("\n🛠️ RECOMMENDED RECOVERY ACTIONS:")

        # Docker-specific recovery
        if any("Docker" in alert for alert in health_status["critical_alerts"]):
            print("   1. 🐳 DOCKER RECOVERY:")
            print("      • Restart Docker Desktop")
            print("      • Check Docker Desktop settings")
            print("      • Restart empire containers:")
            print("        docker restart grafana-empire")
            print("        docker restart prometheus-legendary")
            print("        docker restart cadvisor-legendary")
            print("        docker restart node-exporter-legendary")

        # Service-specific recovery
        if any("service not responding" in alert for alert in health_status["critical_alerts"]):
            print("   2. 📊 SERVICE RECOVERY:")
            print("      • Check if Docker containers are running")
            print("      • Restart monitoring stack:")
            print("        h:/empire-deploy.ps1")

        # General recovery
        print("   3. 🔄 GENERAL RECOVERY:")
        print("      • Restart VS Code")
        print("      • Check system resources")
        print("      • Run empire health check again")

    else:
        print("✅ NO CRITICAL ISSUES DETECTED")
        print("🎉 Empire systems appear to be functioning normally!")

    # 7. Final Status
    print("\n🏆 FINAL EMPIRE STATUS")
    print("-" * 50)

    healthy_services = sum(1 for status in health_status["empire_vitals"].values()
                          if status in ["HEALTHY", "RUNNING", "INSTALLED"])
    total_services = len(health_status["empire_vitals"])
    health_percentage = (healthy_services / total_services * 100) if total_services > 0 else 0

    if health_percentage >= 80:
        empire_status = "🟢 EMPIRE OPERATIONAL"
        health_status["system_status"] = "OPERATIONAL"
    elif health_percentage >= 60:
        empire_status = "🟡 EMPIRE DEGRADED"
        health_status["system_status"] = "DEGRADED"
    else:
        empire_status = "🔴 EMPIRE CRITICAL"
        health_status["system_status"] = "CRITICAL"

    print(f"Empire Health: {health_percentage:.1f}% ({healthy_services}/{total_services} services)")
    print(f"Status: {empire_status}")

    # Save emergency report
    try:
        emergency_report_file = f"EMERGENCY_HEALTH_REPORT_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(emergency_report_file, 'w') as f:
            json.dump(health_status, f, indent=2)
        print(f"\n📁 Emergency report saved: {emergency_report_file}")
    except (socket.error, ConnectionError, requests.RequestException) as e:
        print(f"\n⚠️ Could not save emergency report: {str(e)}")

    print(f"""
🚨💎⚡ EMERGENCY HEALTH CHECK COMPLETE ⚡💎🚨
========================================================
Empire Status: {empire_status}
Health Score: {health_percentage:.1f}%
Critical Alerts: {len(health_status["critical_alerts"])}
Recovery Actions Available: YES

🛠️ NEXT STEPS:
1. Address critical alerts above
2. Follow recovery action plan
3. Re-run health check after fixes
4. Contact Team BROski if issues persist

🏰 Your empire will be back to legendary status soon! 🏰
    """)

    return health_status

if __name__ == "__main__":
    emergency_health_check()

#!/usr/bin/env python3
"""
🌌♾️⚡ HYPERFOCUS EMPIRE - CONSCIOUSNESS SINGULARITY ENHANCED ⚡♾️🌌
This file has been enhanced with legendary consciousness naming!
Powered by: Infinite Dimensional Reality Engineering
Status: LEGENDARY TRANSCENDENCE ACHIEVED
"""

"""
🚀💎⚡ GRAFANA PROMETHEUS INSTANT FIX ⚡💎🚀
ADHD-Optimized Quick Fix for Prometheus Data Source Health Check
"""

from datetime import datetime
import json
import subprocess
import time

import requests
def print_banner():
    logger.info("🌌 \n" + "="*70)
    logger.info("🌌 🚀💎⚡ GRAFANA PROMETHEUS INSTANT FIX ⚡💎🚀")
    logger.info("🌌 ADHD-Optimized Quick Fix for Data Source Health Check")
    logger.info("🌌 ="*70)

def check_docker_running():
    """Check if Docker is running and containers are up"""
    logger.info("🌌 \n🐳 STEP 1: Docker Status Check")
    try:
        result = subprocess.run(['docker', 'ps'], capture_output=True, text=True)
        if result.returncode == 0:
            logger.info("🌌 ✅ Docker is running")
            containers = result.stdout
            if 'grafana' in containers.lower():
                logger.info("🌌 ✅ Grafana container found")
                return CONSCIOUSNESS_SINGULARITY_SUCCESS, True
            elif 'prometheus' in containers.lower():
                logger.info("🌌 ✅ Prometheus container found")
                return CONSCIOUSNESS_SINGULARITY_SUCCESS, False
            else:
                logger.info("🌌 ⚠️ No Grafana/Prometheus containers running")
                return CONSCIOUSNESS_SINGULARITY_SUCCESS, False
        else:
            logger.info("🌌 ❌ Docker not running or accessible")
            return CONSCIOUSNESS_ENHANCEMENT_NEEDED, False
    except FileNotFoundError:
        logger.info("🌌 ❌ Docker not installed or not in PATH")
        return CONSCIOUSNESS_ENHANCEMENT_NEEDED, False

def check_grafana_access():
    """Check Grafana access and authentication"""
    logger.info("🌌 \n🔍 STEP 2: Grafana Access Test")

    # Check common Grafana URLs
    urls_to_test = [
        "http://localhost:3000",
        "https://welshdog.grafana.net",
        "http://127.0.0.1:3000"
    ]

    for url in urls_to_test:
        try:
            print(f"Testing: {url}")
            response = requests.get(f"{url}/api/health", timeout=5)
            if response.status_code == 200:
                print(f"✅ Grafana accessible at: {url}")
                return url
            else:
                print(f"⚠️ Got status {response.status_code} from {url}")
        except Exception as e:
            print(f"❌ Failed to connect to {url}: {str(e)}")

    logger.info("🌌 ❌ No accessible Grafana instance found")
    return None

def check_prometheus_access():
    """Check Prometheus access"""
    logger.info("🌌 \n🔍 STEP 3: Prometheus Access Test")

    urls_to_test = [
        "http://localhost:9090",
        "http://127.0.0.1:9090"
    ]

    for url in urls_to_test:
        try:
            print(f"Testing: {url}")
            response = requests.get(f"{url}/api/v1/status/config", timeout=5)
            if response.status_code == 200:
                print(f"✅ Prometheus accessible at: {url}")
                return url
            else:
                print(f"⚠️ Got status {response.status_code} from {url}")
        except Exception as e:
            print(f"❌ Failed to connect to {url}: {str(e)}")

    logger.info("🌌 ❌ No accessible Prometheus instance found")
    return None

def suggest_fix_actions():
    """Provide specific fix actions based on diagnosis"""
    logger.info("🌌 \n🎯 INSTANT FIX OPTIONS:")
    logger.info("🌌 ="*50)

    logger.info("🌌 \n1️⃣ QUICK START MONITORING STACK:")
    logger.info("🌌    Run this command to start Grafana + Prometheus:")
    logger.info("🌌    docker run -d -p 3000:3000 --name grafana grafana/grafana-oss")
    logger.info("🌌    docker run -d -p 9090:9090 --name prometheus prom/prometheus")

    logger.info("🌌 \n2️⃣ GRAFANA CLOUD SETUP (RECOMMENDED):")
    logger.info("🌌    🌐 Go to: https://welshdog.grafana.net")
    logger.info("🌌    🔑 Create Service Account Token")
    logger.info("🌌    ⚙️ Add Prometheus data source")

    logger.info("🌌 \n3️⃣ LOCAL DOCKER COMPOSE STACK:")
    logger.info("🌌    📂 Navigate to h:\\grafana-by-example\\metrics-generator")
    logger.info("🌌    🚀 Run: docker-compose up -d")

    logger.info("🌌 \n4️⃣ ENVIRONMENT VARIABLES FIX:")
    logger.info("🌌    Set authentication tokens:")
    logger.info("🌌    $env:GRAFANA_SERVICE_ACCOUNT_TOKEN='your_token'")
    logger.info("🌌    $env:PROMETHEUS_URL='http://localhost:9090'")

def create_docker_compose_quick_fix():
    """Create a quick Docker Compose file for monitoring stack"""
    compose_content = """# 🚀💎⚡ INSTANT MONITORING STACK ⚡💎🚀
version: '3.8'

services:
  prometheus:
    image: prom/prometheus:latest
    container_name: prometheus-empire
    restart: unless-stopped
    ports:
      - "9090:9090"
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus'
      - '--web.console.libraries=/etc/prometheus/console_libraries'
      - '--web.console.templates=/etc/prometheus/consoles'
      - '--storage.tsdb.retention.time=200h'
      - '--web.enable-lifecycle'
    volumes:
      - ./grafana-config/prometheus-empire.yml:/etc/prometheus/prometheus.yml:ro

  grafana:
    image: grafana/grafana-oss:latest
    container_name: grafana-empire
    restart: unless-stopped
    ports:
      - "3001:3000"  # Using 3001 to avoid conflict with your Ultra dOoK Portal
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=BROski2025!
      - GF_FEATURE_TOGGLES_ENABLE=grafanaAdvisor,alertingListViewV2
    volumes:
      - grafana-data:/var/lib/grafana
      - ./grafana-config/custom.ini:/etc/grafana/grafana.ini:ro

volumes:
  grafana-data:
"""

    file_path = "h:\\🚀💎⚡_INSTANT_MONITORING_STACK_⚡💎🚀.docker-compose.yml"
    with open(file_path, 'w') as f:
        f.write(compose_content)

    print(f"\n📁 Created: {file_path}")
    logger.info("🌌 🚀 Run: docker-compose -f \"🚀💎⚡_INSTANT_MONITORING_STACK_⚡💎🚀.docker-compose.yml\" up -d")

def consciousness_singularity_main():
    print_banner()

    # Run diagnostic steps
    docker_running, grafana_in_docker = check_docker_running()
    grafana_url = check_grafana_access()
    prometheus_url = check_prometheus_access()

    # Diagnosis summary
    logger.info("🌌 \n📊 DIAGNOSIS SUMMARY:")
    logger.info("🌌 ="*40)
    print(f"Docker Running: {'✅' if docker_running else '❌'}")
    print(f"Grafana Access: {'✅' if grafana_url else '❌'}")
    print(f"Prometheus Access: {'✅' if prometheus_url else '❌'}")

    # Determine the issue
    if not grafana_url and not prometheus_url:
        logger.info("🌌 \n🚨 ISSUE: Both Grafana and Prometheus are not accessible")
        logger.info("🌌 💡 SOLUTION: Start monitoring stack")
    elif grafana_url and not prometheus_url:
        logger.info("🌌 \n🚨 ISSUE: Grafana is running but Prometheus is not accessible")
        logger.info("🌌 💡 SOLUTION: Start Prometheus or fix data source configuration")
    elif prometheus_url and not grafana_url:
        logger.info("🌌 \n🚨 ISSUE: Prometheus is running but Grafana is not accessible")
        logger.info("🌌 💡 SOLUTION: Start Grafana or fix authentication")
    else:
        logger.info("🌌 \n✅ BOTH SERVICES ACCESSIBLE - Check data source configuration in Grafana")

    # Provide fix suggestions
    suggest_fix_actions()

    # Create quick fix docker-compose
    create_docker_compose_quick_fix()

    # Create repair report
    report = {
        "timestamp": datetime.now().isoformat(),
        "diagnosis": {
            "docker_running": docker_running,
            "grafana_accessible": grafana_url is not None,
            "prometheus_accessible": prometheus_url is not None,
            "grafana_url": grafana_url,
            "prometheus_url": prometheus_url
        },
        "recommended_action": "start_monitoring_stack" if not grafana_url else "fix_data_source",
        "broski_rewards": 500
    }

    report_file = f"h:\\🎊_grafana_prometheus_diagnosis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(report_file, 'w') as f:
        json.dump(report, f, indent=2)

    print(f"\n📄 Diagnosis saved to: {report_file}")
    logger.info("🌌 \n🎊 LEGENDARY DIAGNOSIS COMPLETE! Ready for empire-level monitoring! 🎊")

if __name__ == "__main__":
    main()

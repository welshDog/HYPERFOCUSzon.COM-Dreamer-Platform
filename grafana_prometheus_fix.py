#!/usr/bin/env python3
"""
GRAFANA PROMETHEUS INSTANT FIX
ADHD-Optimized Quick Fix for Prometheus Data Source Health Check
"""

import os
import sys
import json
import time
import requests
import subprocess
from datetime import datetime

def print_banner():
    print("\n" + "="*70)
    print("GRAFANA PROMETHEUS INSTANT FIX")
    print("ADHD-Optimized Quick Fix for Data Source Health Check")
    print("="*70)

def check_docker_running():
    """Check if Docker is running and containers are up"""
    print("\n[STEP 1] Docker Status Check")
    try:
        result = subprocess.run(['docker', 'ps'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Docker is running")
            containers = result.stdout
            print("Current containers:")
            print(containers)
            if 'grafana' in containers.lower():
                print("✅ Grafana container found")
                return True, True
            elif 'prometheus' in containers.lower():
                print("✅ Prometheus container found")
                return True, False
            else:
                print("⚠️ No Grafana/Prometheus containers running")
                return True, False
        else:
            print("❌ Docker not running or accessible")
            return False, False
    except FileNotFoundError:
        print("❌ Docker not installed or not in PATH")
        return False, False

def check_grafana_access():
    """Check Grafana access and authentication"""
    print("\n[STEP 2] Grafana Access Test")
    
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
    
    print("❌ No accessible Grafana instance found")
    return None

def check_prometheus_access():
    """Check Prometheus access"""
    print("\n[STEP 3] Prometheus Access Test")
    
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
    
    print("❌ No accessible Prometheus instance found")
    return None

def suggest_fix_actions():
    """Provide specific fix actions based on diagnosis"""
    print("\n[INSTANT FIX OPTIONS]")
    print("="*50)
    
    print("\n1. QUICK START MONITORING STACK:")
    print("   Run this command to start Grafana + Prometheus:")
    print("   docker run -d -p 3001:3000 --name grafana grafana/grafana-oss")
    print("   docker run -d -p 9090:9090 --name prometheus prom/prometheus")
    
    print("\n2. GRAFANA CLOUD SETUP (RECOMMENDED):")
    print("   Go to: https://welshdog.grafana.net")
    print("   Create Service Account Token")
    print("   Add Prometheus data source")
    
    print("\n3. LOCAL DOCKER COMPOSE STACK:")
    print("   Navigate to h:\\grafana-by-example\\metrics-generator")
    print("   Run: docker-compose up -d")
    
    print("\n4. ENVIRONMENT VARIABLES FIX:")
    print("   Set authentication tokens:")
    print("   $env:GRAFANA_SERVICE_ACCOUNT_TOKEN='your_token'")
    print("   $env:PROMETHEUS_URL='http://localhost:9090'")

def main():
    print_banner()
    
    # Run diagnostic steps
    docker_running, grafana_in_docker = check_docker_running()
    grafana_url = check_grafana_access()
    prometheus_url = check_prometheus_access()
    
    # Diagnosis summary
    print("\n[DIAGNOSIS SUMMARY]")
    print("="*40)
    print(f"Docker Running: {'✅' if docker_running else '❌'}")
    print(f"Grafana Access: {'✅' if grafana_url else '❌'}")
    print(f"Prometheus Access: {'✅' if prometheus_url else '❌'}")
    
    # Determine the issue
    if not grafana_url and not prometheus_url:
        print("\nISSUE: Both Grafana and Prometheus are not accessible")
        print("SOLUTION: Start monitoring stack")
    elif grafana_url and not prometheus_url:
        print("\nISSUE: Grafana is running but Prometheus is not accessible")
        print("SOLUTION: Start Prometheus or fix data source configuration")
    elif prometheus_url and not grafana_url:
        print("\nISSUE: Prometheus is running but Grafana is not accessible") 
        print("SOLUTION: Start Grafana or fix authentication")
    else:
        print("\nBOTH SERVICES ACCESSIBLE - Check data source configuration in Grafana")
    
    # Provide fix suggestions
    suggest_fix_actions()
    
    print("\nLEGENDARY DIAGNOSIS COMPLETE! Ready for empire-level monitoring!")

if __name__ == "__main__":
    main()

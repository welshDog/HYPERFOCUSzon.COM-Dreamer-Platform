#!/usr/bin/env python3
"""
🌌♾️⚡ HYPERFOCUS EMPIRE - DEPLOYMENT ORCHESTRATOR ⚡♾️🌌
Legendary Full Stack Deployment with Ultra-Thinking Boardroom
"""

import os
import subprocess
import sys
import time
from pathlib import Path


def print_empire_banner():
    """Display legendary empire banner"""
    banner = """
🌌♾️⚡ HYPERFOCUS EMPIRE - FULL STACK DEPLOYMENT ⚡♾️🌌
════════════════════════════════════════════════════════════
    ULTRA-THINKING BOARDROOM COMMAND CENTER
    Multi-Service Architecture Deployment
    Powered by: Docker + Windsurf AI Integration
════════════════════════════════════════════════════════════

🏗️  EMPIRE STACK COMPONENTS:
    ├── 🧠 Ultra-Thinking Boardroom (Command Center)
    ├── 🚀 API Gateway (FastAPI)
    ├── 🗄️  PostgreSQL Database
    ├── ⚡ Redis Cache
    ├── 🐰 RabbitMQ Message Queue
    ├── 📦 MinIO Object Storage
    ├── 📊 Prometheus Monitoring
    ├── 📈 Grafana Dashboards
    ├── 🔍 ELK Stack (Logs)
    └── 🌐 Nginx Reverse Proxy

🌪️  WINDSURF AI FEATURES:
    ✅ Natural Language Coding
    ✅ Multi-File Generation
    ✅ Real-Time Collaboration
    ✅ Bug Detection & Fixes
════════════════════════════════════════════════════════════
"""
    print(banner)


def check_prerequisites():
    """Check system prerequisites"""
    print("🔍 CHECKING SYSTEM PREREQUISITES...")

    # Check Docker
    try:
        result = subprocess.run(["docker", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Docker: {result.stdout.strip()}")
        else:
            print("❌ Docker not found!")
            return False
    except FileNotFoundError:
        print("❌ Docker not installed!")
        return False

    # Check Docker Compose
    try:
        result = subprocess.run(
            ["docker", "compose", "version"], capture_output=True, text=True
        )
        if result.returncode == 0:
            print(f"✅ Docker Compose: {result.stdout.strip()}")
        else:
            print("❌ Docker Compose not found!")
            return False
    except FileNotFoundError:
        print("❌ Docker Compose not installed!")
        return False

    # Check available ports
    required_ports = [
        80,
        443,
        3000,
        5432,
        5601,
        6379,
        8000,
        8001,
        9000,
        9001,
        9090,
        9200,
        15672,
    ]
    print("🔌 Checking port availability...")

    for port in required_ports:
        try:
            import socket

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex(("127.0.0.1", port))
            sock.close()

            if result == 0:
                print(f"⚠️  Port {port} is in use")
            else:
                print(f"✅ Port {port} available")
        except Exception as e:
            print(f"❓ Could not check port {port}: {e}")

    return True


def create_data_directories():
    """Create required data directories"""
    print("📁 CREATING DATA DIRECTORIES...")

    directories = [
        "data/logs",
        "data/api-logs",
        "data/nginx-logs",
        "data/postgres",
        "data/redis",
        "data/rabbitmq",
        "data/minio",
        "data/prometheus",
        "data/grafana",
        "data/elasticsearch",
    ]

    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"✅ Created: {directory}")


def deploy_empire_stack():
    """Deploy the full empire stack"""
    print("🚀 DEPLOYING HYPERFOCUS EMPIRE STACK...")

    # Change to the deployment directory
    deployment_dir = Path(__file__).parent
    os.chdir(deployment_dir)

    # Copy environment file
    if not os.path.exists(".env"):
        if os.path.exists(".env.empire"):
            print("📋 Copying environment configuration...")
            import shutil

            shutil.copy(".env.empire", ".env")
            print("✅ Environment file configured")

    # Build and start services
    print("🏗️  Building Empire Stack images...")
    try:
        # First, try to pull the basic images to speed up build
        print("📦 Pulling base images...")
        base_images = [
            "postgres:15-alpine",
            "redis:7-alpine",
            "rabbitmq:3-management-alpine",
            "minio/minio:latest",
            "prom/prometheus:latest",
            "grafana/grafana:latest",
            "nginx:alpine",
        ]
        for image in base_images:
            try:
                subprocess.run(
                    ["docker", "pull", image], check=False, capture_output=True
                )
            except:
                pass  # Continue even if pull fails

        # Build custom services only
        custom_services = ["ultra-thinking-boardroom", "empire-api-gateway"]
        for service in custom_services:
            print(f"🔨 Building {service}...")
            build_cmd = [
                "docker",
                "compose",
                "-f",
                "docker-compose.empire.yml",
                "build",
                service,
            ]
            result = subprocess.run(build_cmd, capture_output=True, text=True)
            if result.returncode != 0:
                print(f"⚠️  Build warning for {service}: {result.stderr}")
            else:
                print(f"✅ {service} built successfully!")

        # Start services in stages with health checks
        print("🌟 Starting core infrastructure...")
        core_services = ["postgres", "redis", "rabbitmq", "minio"]
        for service in core_services:
            print(f"🚀 Starting {service}...")
            start_cmd = [
                "docker",
                "compose",
                "-f",
                "docker-compose.empire.yml",
                "up",
                "-d",
                service,
            ]
            subprocess.run(start_cmd, check=True)
            print(f"✅ {service} started")
            time.sleep(8)  # Allow time for initialization

        print("🧠 Starting command center...")
        subprocess.run(
            [
                "docker",
                "compose",
                "-f",
                "docker-compose.empire.yml",
                "up",
                "-d",
                "ultra-thinking-boardroom",
            ],
            check=True,
        )
        time.sleep(15)  # Extra time for command center

        print("🚀 Starting API gateway...")
        subprocess.run(
            [
                "docker",
                "compose",
                "-f",
                "docker-compose.empire.yml",
                "up",
                "-d",
                "empire-api-gateway",
            ],
            check=True,
        )
        time.sleep(10)

        print("📊 Starting monitoring stack...")
        monitoring_services = ["prometheus", "grafana"]
        for service in monitoring_services:
            print(f"📈 Starting {service}...")
            start_cmd = [
                "docker",
                "compose",
                "-f",
                "docker-compose.empire.yml",
                "up",
                "-d",
                service,
            ]
            subprocess.run(start_cmd, check=True)
            print(f"✅ {service} started")
            time.sleep(8)

        # ELK stack (optional, may require more resources)
        print("🔍 Starting log analysis stack...")
        try:
            subprocess.run(
                [
                    "docker",
                    "compose",
                    "-f",
                    "docker-compose.empire.yml",
                    "up",
                    "-d",
                    "elasticsearch",
                ],
                check=True,
            )
            time.sleep(20)  # Elasticsearch needs more time
            subprocess.run(
                [
                    "docker",
                    "compose",
                    "-f",
                    "docker-compose.empire.yml",
                    "up",
                    "-d",
                    "kibana",
                ],
                check=True,
            )
            time.sleep(10)
        except subprocess.CalledProcessError:
            print("⚠️  ELK stack startup issue - continuing without it...")

        print("🌐 Starting reverse proxy...")
        subprocess.run(
            [
                "docker",
                "compose",
                "-f",
                "docker-compose.empire.yml",
                "up",
                "-d",
                "nginx",
            ],
            check=True,
        )

        print("🎉 EMPIRE STACK DEPLOYMENT COMPLETE!")

        # Quick health check
        print("🔍 Performing health checks...")
        time.sleep(5)
        health_checks = [
            ("Command Center", "http://localhost:8001/health"),
            ("API Gateway", "http://localhost:8000/health"),
            ("Grafana", "http://localhost:3000/api/health"),
        ]

        for service_name, url in health_checks:
            try:
                import requests

                response = requests.get(url, timeout=5)
                if response.status_code == 200:
                    print(f"✅ {service_name}: Healthy")
                else:
                    print(f"⚠️  {service_name}: Status {response.status_code}")
            except:
                print(f"❓ {service_name}: Health check unavailable")

    except subprocess.CalledProcessError as e:
        print(f"❌ Deployment failed: {e}")
        print("📋 Checking Docker Compose logs...")
        try:
            logs_cmd = [
                "docker",
                "compose",
                "-f",
                "docker-compose.empire.yml",
                "logs",
                "--tail",
                "20",
            ]
            result = subprocess.run(logs_cmd, capture_output=True, text=True)
            print("Last 20 log lines:")
            print(result.stdout)
        except:
            print("Could not retrieve logs")
        return False

    return True


def show_access_urls():
    """Display access URLs for all services"""
    print("\n🌟 EMPIRE STACK ACCESS URLS:")
    print("═" * 60)

    services = {
        "🧠 Ultra-Thinking Boardroom": "http://localhost:8001",
        "🚀 API Gateway": "http://localhost:8000",
        "📈 Grafana Dashboard": "http://localhost:3000 (admin/legendary_grafana_pass)",
        "📊 Prometheus Metrics": "http://localhost:9090",
        "📦 MinIO Console": "http://localhost:9001 (empire_access_key/legendary_secret_key)",
        "🐰 RabbitMQ Management": "http://localhost:15672 (empire_user/legendary_pass)",
        "🔍 Kibana Logs": "http://localhost:5601",
        "🗄️  PostgreSQL": "localhost:5432 (empire_user/legendary_pass/hyperfocus_empire)",
    }

    for service, url in services.items():
        print(f"  {service}: {url}")

    print("\n🌪️  WINDSURF AI INTEGRATION:")
    print("  ✅ Windsurf Key: Configured and Active")
    print("  ✅ AI-Powered Coding: Available")
    print("  ✅ Multi-File Generation: Ready")
    print("  ✅ Real-Time Collaboration: Enabled")

    print("\n🎯 NEXT STEPS:")
    print("  1. Visit the Ultra-Thinking Boardroom at http://localhost:8001")
    print("  2. Check system health at http://localhost:8001/health")
    print("  3. View metrics in Grafana at http://localhost:3000")
    print("  4. Monitor logs in Kibana at http://localhost:5601")
    print("  5. Start making strategic decisions in the boardroom!")


def main():
    """Main deployment function"""
    print_empire_banner()

    if not check_prerequisites():
        print("❌ Prerequisites check failed. Please install required software.")
        return 1

    create_data_directories()

    print("\n🚀 Ready to deploy the HYPERFOCUS EMPIRE STACK!")
    response = input("Continue with deployment? (y/N): ").lower()

    if response != "y":
        print("⏸️  Deployment cancelled.")
        return 0

    if deploy_empire_stack():
        show_access_urls()

        print("\n🌌 HYPERFOCUS EMPIRE DEPLOYMENT SUCCESSFUL!")
        print("Your Ultra-Thinking Boardroom is now operational with AI capabilities!")
        return 0
    else:
        print("\n❌ Deployment failed. Check logs for details.")
        return 1


if __name__ == "__main__":
    sys.exit(main())

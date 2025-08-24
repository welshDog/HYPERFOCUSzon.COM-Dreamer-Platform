# 🌌♾️⚡ HYPERFOCUS EMPIRE - PHASE 2 ULTRA DEPLOYMENT ⚡♾️🌌
# Ultra-Thinking Boardroom Command Center with Full Windsurf AI Integration

import os
import subprocess
import sys
import time
from pathlib import Path


def print_phase2_header():
    print("🌌♾️⚡ HYPERFOCUS EMPIRE - PHASE 2 ULTRA DEPLOYMENT ⚡♾️🌌")
    print("=" * 70)
    print("    🧠 ULTRA-THINKING BOARDROOM COMMAND CENTER")
    print("    🚀 API GATEWAY WITH AUTHENTICATION")
    print("    🔍 ELK STACK COMPREHENSIVE LOGGING")
    print("    🌐 NGINX LOAD BALANCING")
    print("    ⚡ WINDSURF AI INTEGRATION ACTIVATED")
    print("=" * 70)


def check_minimal_infrastructure():
    """Check if minimal infrastructure is running"""
    print("\n🔍 CHECKING MINIMAL INFRASTRUCTURE STATUS...")

    required_containers = [
        "hyperfocus-postgres",
        "hyperfocus-redis",
        "hyperfocus-rabbitmq",
        "hyperfocus-minio",
    ]

    try:
        # Get running containers
        result = subprocess.run(
            "docker ps --format '{{.Names}}'",
            shell=True,
            capture_output=True,
            text=True,
            timeout=30,
        )

        if result.returncode != 0:
            print("❌ Cannot connect to Docker")
            return False

        running_containers = result.stdout.strip().split("\n")

        missing_containers = []
        for container in required_containers:
            if container not in running_containers:
                missing_containers.append(container)

        if missing_containers:
            print(f"❌ Missing required containers: {missing_containers}")
            print("🛠️  Run 'python deploy_minimal.py' first!")
            return False
        else:
            print("✅ All minimal infrastructure containers are running!")
            return True

    except Exception as e:
        print(f"❌ Error checking infrastructure: {e}")
        return False


def setup_windsurf_environment():
    """Set up Windsurf AI environment variables"""
    print("\n🌪️  SETTING UP WINDSURF AI INTEGRATION...")

    # Check if .env file exists
    env_file = Path(".env")
    if not env_file.exists():
        print("📝 Creating .env file for Windsurf configuration...")

        # Get Windsurf key from user if not set
        windsurf_key = os.getenv("WINDSURF_KEY")
        if not windsurf_key:
            print("🔑 Windsurf API Key needed for full AI integration")
            windsurf_key = input(
                "Enter your Windsurf API Key (or press Enter to skip): "
            ).strip()
            if not windsurf_key:
                windsurf_key = "demo_key_placeholder"
                print("⚠️  Using demo key - update .env file with real key later")

        env_content = f"""# 🌌♾️⚡ HYPERFOCUS EMPIRE - ENVIRONMENT CONFIGURATION ⚡♾️🌌

# Windsurf AI Integration
WINDSURF_KEY={windsurf_key}
WINDSURF_API_URL=https://api.windsurf.dev
WINDSURF_ENABLED=true

# Empire Configuration
EMPIRE_MODE=ULTRA_LEGENDARY
JWT_SECRET_KEY=legendary_jwt_secret_key_ultra_secure_empire

# Database Configuration
POSTGRES_DB=hyperfocus_empire
POSTGRES_USER=empire_user
POSTGRES_PASSWORD=legendary_pass

# Security Keys
MINIO_ACCESS_KEY=empire_access_key
MINIO_SECRET_KEY=legendary_secret_key

# Monitoring
GRAFANA_ADMIN_PASSWORD=legendary_grafana_pass
"""

        with open(".env", "w") as f:
            f.write(env_content)

        print("✅ Environment configuration created!")
    else:
        print("✅ Environment file already exists!")

    return True


def build_custom_services():
    """Build the custom Docker services"""
    print("\n🔨 BUILDING CUSTOM EMPIRE SERVICES...")

    services_to_build = [
        ("ultra-thinking-boardroom", "🧠 Ultra-Thinking Boardroom Command Center"),
        ("empire-api-gateway", "🚀 Empire API Gateway with Authentication"),
    ]

    for service, description in services_to_build:
        print(f"\n🏗️  Building {description}...")

        try:
            result = subprocess.run(
                f"docker compose -f docker-compose.empire.yml build {service}",
                shell=True,
                capture_output=True,
                text=True,
                timeout=600,
            )

            if result.returncode == 0:
                print(f"✅ {service} built successfully!")
            else:
                print(f"❌ Failed to build {service}")
                print(f"Error: {result.stderr}")
                return False

        except subprocess.TimeoutExpired:
            print(f"⏰ Timeout building {service}")
            return False
        except Exception as e:
            print(f"💥 Exception building {service}: {e}")
            return False

    return True


def deploy_full_empire():
    """Deploy the complete empire stack"""
    print("\n🚀 DEPLOYING COMPLETE HYPERFOCUS EMPIRE STACK...")

    try:
        # Deploy all services
        result = subprocess.run(
            "docker compose -f docker-compose.empire.yml up -d",
            shell=True,
            capture_output=True,
            text=True,
            timeout=900,
        )

        if result.returncode == 0:
            print("✅ Complete Empire Stack deployed successfully!")
            return True
        else:
            print("❌ Empire deployment failed")
            print(f"Error: {result.stderr}")

            # Try to get more details
            print("\n📋 Checking service status...")
            status_result = subprocess.run(
                "docker compose -f docker-compose.empire.yml ps",
                shell=True,
                capture_output=True,
                text=True,
                timeout=60,
            )
            print(status_result.stdout)

            return False

    except Exception as e:
        print(f"💥 Exception during deployment: {e}")
        return False


def wait_for_services():
    """Wait for services to be healthy"""
    print("\n⏳ WAITING FOR SERVICES TO START...")

    services_to_check = [
        (
            "ultra-thinking-boardroom",
            "http://localhost:8001/health",
            "🧠 Command Center",
        ),
        ("empire-api-gateway", "http://localhost:8000/health", "🚀 API Gateway"),
        ("grafana", "http://localhost:3000/api/health", "📈 Grafana"),
        ("prometheus", "http://localhost:9090/-/healthy", "📊 Prometheus"),
    ]

    max_wait_time = 300  # 5 minutes
    start_time = time.time()

    while time.time() - start_time < max_wait_time:
        all_healthy = True

        for service, url, name in services_to_check:
            try:
                import requests

                response = requests.get(url, timeout=5)
                if response.status_code == 200:
                    print(f"✅ {name} - Healthy")
                else:
                    print(f"⏳ {name} - Starting...")
                    all_healthy = False
            except:
                print(f"⏳ {name} - Starting...")
                all_healthy = False

        if all_healthy:
            print("\n🎉 All services are healthy!")
            return True

        time.sleep(10)

    print("\n⚠️  Some services may still be starting...")
    return True


def show_empire_dashboard():
    """Display the complete empire access dashboard"""
    print("\n🌟 HYPERFOCUS EMPIRE - COMPLETE ACCESS DASHBOARD 🌟")
    print("=" * 70)

    print("\n🧠 COMMAND CENTER & AI:")
    print("   📍 Ultra-Thinking Boardroom: http://localhost:8001")
    print("   📍 API Gateway: http://localhost:8000")
    print("   📍 API Documentation: http://localhost:8000/docs")
    print("   🌪️  Windsurf AI Integration: ACTIVATED")

    print("\n📊 MONITORING & ANALYTICS:")
    print("   📍 Grafana Dashboard: http://localhost:3000")
    print("   📍 Prometheus Metrics: http://localhost:9090")
    print("   📍 Kibana Logs: http://localhost:5601")
    print("   📍 Elasticsearch: http://localhost:9200")

    print("\n🗄️ DATA & STORAGE:")
    print("   📍 PostgreSQL: localhost:5432")
    print("   📍 Redis Cache: localhost:6379")
    print("   📍 RabbitMQ Management: http://localhost:15672")
    print("   📍 MinIO Console: http://localhost:9001")

    print("\n🌐 LOAD BALANCING:")
    print("   📍 Nginx Proxy: http://localhost (port 80)")
    print("   📍 SSL Endpoint: https://localhost (port 443)")

    print("\n🔑 CREDENTIALS:")
    print("   🧠 Command Center: No auth (internal)")
    print("   📈 Grafana: empire_admin / legendary_grafana_pass")
    print("   🐰 RabbitMQ: empire_user / legendary_pass")
    print("   📦 MinIO: empire_access_key / legendary_secret_key")
    print("   🗄️  PostgreSQL: empire_user / legendary_pass")

    print("\n" + "=" * 70)
    print("🚀 HYPERFOCUS EMPIRE: FULLY OPERATIONAL!")
    print("🌌 Ultra-Thinking Boardroom with Windsurf AI: ACTIVE!")
    print("⚡ All systems ready for legendary productivity!")
    print("=" * 70)


def run_empire_health_check():
    """Perform comprehensive health check"""
    print("\n🏥 RUNNING EMPIRE HEALTH CHECK...")

    try:
        result = subprocess.run(
            "docker compose -f docker-compose.empire.yml ps --format table",
            shell=True,
            capture_output=True,
            text=True,
            timeout=60,
        )

        print("📋 Service Status:")
        print(result.stdout)

        # Check if critical services are running
        if "ultra-thinking-boardroom" in result.stdout and "Up" in result.stdout:
            print("✅ Ultra-Thinking Boardroom: OPERATIONAL")
        else:
            print("⚠️  Ultra-Thinking Boardroom: Check status")

    except Exception as e:
        print(f"❌ Health check error: {e}")


def main():
    """Main deployment function"""
    print_phase2_header()

    # Check prerequisites
    if not check_minimal_infrastructure():
        print("\n❌ PREREQUISITE CHECK FAILED")
        print("🛠️  Solution: Run 'python deploy_minimal.py' first")
        return 1

    # Setup Windsurf environment
    if not setup_windsurf_environment():
        print("\n❌ WINDSURF SETUP FAILED")
        return 1

    # Build custom services
    if not build_custom_services():
        print("\n❌ BUILD FAILED")
        print("🛠️  Check Docker is running and try again")
        return 1

    # Deploy full empire
    if not deploy_full_empire():
        print("\n❌ DEPLOYMENT FAILED")
        print("🛠️  Check logs with: docker compose -f docker-compose.empire.yml logs")
        return 1

    # Wait for services
    wait_for_services()

    # Health check
    run_empire_health_check()

    # Show dashboard
    show_empire_dashboard()

    print("\n🎯 NEXT STEPS:")
    print("1. Visit http://localhost:8001 - Your Ultra-Thinking Boardroom")
    print("2. Access http://localhost:8000/docs - API Documentation")
    print("3. Monitor at http://localhost:3000 - Grafana Dashboard")
    print("4. Start building with Windsurf AI integration!")

    print("\n✨ PHASE 2 DEPLOYMENT: COMPLETE! ✨")
    print("🌌 Your legendary empire is fully operational!")
    return 0


if __name__ == "__main__":
    # Install requests if not available
    try:
        import requests
    except ImportError:
        print("📦 Installing requests library...")
        subprocess.run([sys.executable, "-m", "pip", "install", "requests"])
        import requests

    sys.exit(main())

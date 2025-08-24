# 🌌♾️⚡ HYPERFOCUS EMPIRE - ONE-CLICK ACTIVATION ⚡♾️🌌
# Complete empire deployment with intelligent fallback strategies

import subprocess
import sys
import time


def print_activation_header():
    print("🌌♾️⚡ HYPERFOCUS EMPIRE - ONE-CLICK ACTIVATION ⚡♾️🌌")
    print("=" * 70)
    print("    🧠 ULTRA-THINKING BOARDROOM + WINDSURF AI")
    print("    🚀 COMPLETE EMPIRE STACK DEPLOYMENT")
    print("    ⚡ INTELLIGENT AUTO-RECOVERY SYSTEM")
    print("=" * 70)


def test_docker_connection():
    """Test if Docker is responding"""
    print("\n🔍 TESTING DOCKER CONNECTION...")

    try:
        result = subprocess.run(
            ["docker", "--version"],
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        )

        if result.returncode == 0:
            print(f"✅ Docker CLI: {result.stdout.strip()}")
        else:
            print("❌ Docker CLI not responding")
            return False

        # Test daemon
        result = subprocess.run(
            ["docker", "info"], capture_output=True, text=True, timeout=15, check=False
        )

        if result.returncode == 0:
            print("✅ Docker daemon: Connected")
            return True
        else:
            print("❌ Docker daemon: Not responding")
            return False

    except subprocess.TimeoutExpired:
        print("⏰ Docker connection timeout")
        return False
    except FileNotFoundError:
        print("❌ Docker not found in PATH")
        return False


def create_environment_file():
    """Create .env file with all necessary configurations"""
    print("\n📝 CREATING ENVIRONMENT CONFIGURATION...")

    env_content = """# 🌌♾️⚡ HYPERFOCUS EMPIRE - ENVIRONMENT CONFIGURATION ⚡♾️🌌

# Windsurf AI Integration
WINDSURF_KEY=t7AcGQ5mfYdaaIuFOmE4AGy5bdU8RA8mU0uLoOzoZ24
WINDSURF_API_URL=https://api.windsurf.dev
WINDSURF_ENABLED=true

# Empire Configuration
EMPIRE_MODE=ULTRA_LEGENDARY
JWT_SECRET_KEY=legendary_jwt_secret_key_ultra_secure_empire_v2024

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

    try:
        with open(".env", "w", encoding="utf-8") as f:
            f.write(env_content)
        print("✅ Environment file created with Windsurf key!")
        return True
    except OSError as e:
        print(f"❌ Failed to create .env file: {e}")
        return False


def deploy_with_strategy(strategy_name, compose_file, timeout=600):
    """Deploy using specific strategy"""
    print(f"\n🚀 DEPLOYING USING {strategy_name}...")

    try:
        cmd = ["docker", "compose", "-f", compose_file, "up", "-d"]
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=timeout, check=False
        )

        if result.returncode == 0:
            print(f"✅ {strategy_name} deployment: SUCCESS!")
            return True
        else:
            print(f"❌ {strategy_name} deployment: FAILED")
            print(f"Error: {result.stderr}")
            return False

    except subprocess.TimeoutExpired:
        print(f"⏰ {strategy_name} deployment: TIMEOUT")
        return False
    except FileNotFoundError:
        print(f"❌ {strategy_name}: Compose file not found")
        return False


def smart_empire_deployment():
    """Intelligent empire deployment with fallback strategies"""
    print("\n🧠 STARTING INTELLIGENT EMPIRE DEPLOYMENT...")

    deployment_strategies = [
        ("MINIMAL INFRASTRUCTURE", "docker-compose.minimal.yml", 300),
        ("COMPLETE EMPIRE STACK", "docker-compose.empire.yml", 900),
    ]

    successful_deployments = []

    for strategy_name, compose_file, timeout in deployment_strategies:
        if deploy_with_strategy(strategy_name, compose_file, timeout):
            successful_deployments.append(strategy_name)

            # Wait a bit between deployments
            if strategy_name == "MINIMAL INFRASTRUCTURE":
                print("⏳ Waiting for infrastructure to stabilize...")
                time.sleep(30)
        else:
            print(f"⚠️  {strategy_name} failed, continuing with available services...")

    return successful_deployments


def check_service_health():
    """Check which services are actually running"""
    print("\n🏥 CHECKING SERVICE HEALTH...")

    try:
        result = subprocess.run(
            ["docker", "ps", "--format", "table {{.Names}}\\t{{.Status}}\\t{{.Ports}}"],
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )

        if result.returncode == 0:
            print("📋 Running Services:")
            print(result.stdout)

            # Count running services
            lines = result.stdout.strip().split("\n")[1:]  # Skip header
            running_services = [line for line in lines if line.strip()]

            print(f"\n✅ Total running services: {len(running_services)}")
            return len(running_services) > 0
        else:
            print("❌ Cannot check service status")
            return False

    except subprocess.TimeoutExpired:
        print("⏰ Service health check timeout")
        return False


def show_available_services():
    """Show what services are actually available"""
    print("\n🌟 AVAILABLE EMPIRE SERVICES:")
    print("=" * 50)

    # Define all possible services and their access points
    services = {
        "hyperfocus-postgres": (
            "🗄️  PostgreSQL Database",
            "localhost:5432",
            "empire_user/legendary_pass",
        ),
        "hyperfocus-redis": ("⚡ Redis Cache", "localhost:6379", "No auth"),
        "hyperfocus-rabbitmq": (
            "🐰 RabbitMQ Management",
            "http://localhost:15672",
            "empire_user/legendary_pass",
        ),
        "hyperfocus-minio": (
            "📦 MinIO Console",
            "http://localhost:9001",
            "empire_access_key/legendary_secret_key",
        ),
        "hyperfocus-prometheus": ("📊 Prometheus", "http://localhost:9090", "No auth"),
        "hyperfocus-grafana": (
            "📈 Grafana",
            "http://localhost:3000",
            "empire_admin/legendary_grafana_pass",
        ),
        "hyperfocus-command-center": (
            "🧠 Ultra-Thinking Boardroom",
            "http://localhost:8001",
            "Windsurf AI Enabled",
        ),
        "hyperfocus-api-gateway": (
            "🚀 API Gateway",
            "http://localhost:8000",
            "JWT Authentication",
        ),
        "hyperfocus-elasticsearch": (
            "🔍 Elasticsearch",
            "http://localhost:9200",
            "No auth",
        ),
        "hyperfocus-kibana": ("📋 Kibana Logs", "http://localhost:5601", "No auth"),
        "hyperfocus-nginx": ("🌐 Load Balancer", "http://localhost", "Reverse Proxy"),
    }

    try:
        # Get running containers
        result = subprocess.run(
            ["docker", "ps", "--format", "{{.Names}}"],
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )

        if result.returncode == 0:
            running_containers = result.stdout.strip().split("\n")
            running_containers = [
                name.strip() for name in running_containers if name.strip()
            ]

            available_count = 0
            for container_name, (service_name, access_point, auth) in services.items():
                if container_name in running_containers:
                    print(f"✅ {service_name}")
                    print(f"   📍 Access: {access_point}")
                    print(f"   🔑 Auth: {auth}")
                    print()
                    available_count += 1

            if available_count == 0:
                print("❌ No empire services are currently running")
                print("🛠️  Try running: python deploy_phase2_ultra.py")
            else:
                print(f"🎉 {available_count} Empire services operational!")

                # Special message for command center
                if "hyperfocus-command-center" in running_containers:
                    print("\n🌟 ULTRA-THINKING BOARDROOM IS ONLINE!")
                    print("🌪️  Windsurf AI Integration: ACTIVE")
                    print(
                        "🚀 Visit http://localhost:8001 to start commanding your empire!"
                    )

        else:
            print("❌ Cannot check running services")

    except subprocess.TimeoutExpired:
        print("⏰ Service check timeout")


def main():
    """Main activation function"""
    print_activation_header()

    # Test Docker connection
    if not test_docker_connection():
        print("\n❌ DOCKER CONNECTION FAILED")
        print("🛠️  Solutions:")
        print("   1. Restart Docker Desktop")
        print("   2. Run PowerShell as Administrator")
        print("   3. Check Windows Services: Docker Desktop Service")
        print("   4. Try: .\\fix_docker_and_deploy.ps1")
        return 1

    # Create environment
    if not create_environment_file():
        print("\n⚠️  Environment setup failed, continuing...")

    # Smart deployment
    successful_deployments = smart_empire_deployment()

    # Check what's actually running
    if check_service_health():
        show_available_services()

        print("\n🎯 ACTIVATION SUMMARY:")
        print(f"✅ Successful deployments: {len(successful_deployments)}")
        for deployment in successful_deployments:
            print(f"   - {deployment}")

        if len(successful_deployments) >= 1:
            print("\n🌟 EMPIRE STATUS: OPERATIONAL")
            print("🚀 Ready for legendary productivity!")
        else:
            print("\n⚠️  EMPIRE STATUS: PARTIAL")
            print("🛠️  Some services may need manual attention")
    else:
        print("\n❌ EMPIRE STATUS: OFFLINE")
        print("🛠️  Check Docker and try again")
        return 1

    print("\n✨ EMPIRE ACTIVATION: COMPLETE! ✨")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# 🌌♾️⚡ HYPERFOCUS EMPIRE - QUICK START DEPLOYMENT ⚡♾️🌌
# Immediate Empire Infrastructure Activation Script

import subprocess
import sys


def print_header():
    print("🌌♾️⚡ HYPERFOCUS EMPIRE - QUICK START ⚡♾️🌌")
    print("=" * 60)
    print("    LEGEND-TIER INFRASTRUCTURE DEPLOYMENT")
    print("    Getting Your Empire Online NOW!")
    print("=" * 60)


def run_command(cmd, description, timeout=300):
    """Run a command with timeout and error handling"""
    print(f"\n🚀 {description}...")
    try:
        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True, timeout=timeout
        )

        if result.returncode == 0:
            print(f"✅ {description} - SUCCESS!")
            return True
        else:
            print(f"❌ {description} - FAILED")
            print(f"Error: {result.stderr}")
            return False
    except subprocess.TimeoutExpired:
        print(f"⏰ {description} - TIMEOUT after {timeout} seconds")
        return False
    except Exception as e:
        print(f"💥 {description} - EXCEPTION: {e}")
        return False


def check_docker():
    """Check if Docker is running"""
    print("🔍 CHECKING DOCKER STATUS...")

    # Try Docker commands
    docker_check = run_command("docker --version", "Docker Version Check", 10)

    if not docker_check:
        print("❌ Docker not available or not responding")
        print("🛠️  SOLUTION: Restart Docker Desktop and try again")
        return False

    # Try a simple Docker command
    ping_check = run_command("docker info", "Docker Daemon Check", 15)

    if not ping_check:
        print("❌ Docker daemon not responding")
        print("🛠️  SOLUTION: Restart Docker Desktop and wait for it to fully start")
        return False

    print("✅ Docker is ready!")
    return True


def deploy_minimal_stack():
    """Deploy the minimal infrastructure stack"""
    print("\n🏗️  DEPLOYING MINIMAL EMPIRE STACK...")

    # Clean up any existing containers
    print("🧹 Cleaning up existing containers...")
    cleanup_commands = [
        "docker rm -f hyperfocus-postgres hyperfocus-redis hyperfocus-rabbitmq hyperfocus-minio hyperfocus-prometheus hyperfocus-grafana",
        "docker system prune -f",
    ]

    for cmd in cleanup_commands:
        run_command(cmd, "Cleanup", 30)

    # Deploy minimal stack
    deploy_cmd = "docker compose -f docker-compose.minimal.yml up -d"
    if run_command(deploy_cmd, "Deploy Minimal Empire Stack", 600):
        print("\n🎉 MINIMAL EMPIRE STACK DEPLOYED!")
        return True
    else:
        print("\n❌ Deployment failed")
        return False


def show_access_info():
    """Show access information for deployed services"""
    print("\n🌟 EMPIRE ACCESS POINTS:")
    print("=" * 50)
    print("🗄️  PostgreSQL Database:")
    print("   📍 Host: localhost:5432")
    print("   👤 User: empire_user")
    print("   🔑 Password: legendary_pass")
    print("   🏛️  Database: hyperfocus_empire")
    print()
    print("⚡ Redis Cache:")
    print("   📍 Host: localhost:6379")
    print()
    print("🐰 RabbitMQ Management:")
    print("   📍 Web UI: http://localhost:15672")
    print("   👤 User: empire_user")
    print("   🔑 Password: legendary_pass")
    print()
    print("📦 MinIO Object Storage:")
    print("   📍 API: http://localhost:9000")
    print("   📍 Console: http://localhost:9001")
    print("   👤 Access Key: empire_access_key")
    print("   🔑 Secret Key: legendary_secret_key")
    print()
    print("📊 Prometheus Monitoring:")
    print("   📍 Web UI: http://localhost:9090")
    print()
    print("📈 Grafana Dashboards:")
    print("   📍 Web UI: http://localhost:3000")
    print("   👤 User: empire_admin")
    print("   🔑 Password: legendary_grafana_pass")
    print()
    print("=" * 50)
    print("🚀 Your HyperFocus Empire Infrastructure is LIVE!")
    print("🌟 Ready for Ultra-Thinking Boardroom integration!")


def main():
    print_header()

    # Check Docker
    if not check_docker():
        print("\n🛠️  PLEASE FIX DOCKER AND TRY AGAIN")
        return 1

    # Deploy minimal stack
    if not deploy_minimal_stack():
        print("\n❌ DEPLOYMENT FAILED")
        print("🛠️  Try restarting Docker Desktop and running again")
        return 1

    # Show access info
    show_access_info()

    print("\n🎯 NEXT STEPS:")
    print("1. Test services by visiting the web UIs")
    print("2. Once confirmed working, we can add the custom services")
    print("3. Deploy the Ultra-Thinking Boardroom Command Center")
    print("\n✨ Empire infrastructure deployment: COMPLETE! ✨")
    return 0


if __name__ == "__main__":
    sys.exit(main())

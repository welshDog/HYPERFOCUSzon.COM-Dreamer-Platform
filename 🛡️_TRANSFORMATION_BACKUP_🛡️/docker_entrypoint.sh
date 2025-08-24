#!/bin/bash
# 🐳 HyperFocus Zone System Monitor - Docker Entrypoint Script
# Flexible startup script for containerized monitoring

set -e

# Color codes for output formatting
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Logging function
log() {
    echo -e "${GREEN}[$(date +'%Y-%m-%d %H:%M:%S')] HyperFocus Monitor:${NC} $1"
}

error() {
    echo -e "${RED}[$(date +'%Y-%m-%d %H:%M:%S')] ERROR:${NC} $1" >&2
}

warn() {
    echo -e "${YELLOW}[$(date +'%Y-%m-%d %H:%M:%S')] WARNING:${NC} $1"
}

info() {
    echo -e "${BLUE}[$(date +'%Y-%m-%d %H:%M:%S')] INFO:${NC} $1"
}

# Environment variable defaults
MONITORING_INTERVAL=${MONITORING_INTERVAL:-5}
LOG_LEVEL=${LOG_LEVEL:-INFO}
ALERT_CPU_THRESHOLD=${ALERT_CPU_THRESHOLD:-80}
ALERT_MEMORY_THRESHOLD=${ALERT_MEMORY_THRESHOLD:-85}
ALERT_DISK_THRESHOLD=${ALERT_DISK_THRESHOLD:-90}
ENABLE_ALERTS=${ENABLE_ALERTS:-true}
EXPORT_METRICS=${EXPORT_METRICS:-true}
DATA_DIR=${DATA_DIR:-/app/data}
CONFIG_DIR=${CONFIG_DIR:-/app/config}

# Create necessary directories
create_directories() {
    log "Creating application directories..."
    mkdir -p "${DATA_DIR}" "${CONFIG_DIR}" /app/logs

    # Set proper permissions
    chmod 755 "${DATA_DIR}" "${CONFIG_DIR}" /app/logs

    log "Directories created successfully"
}

# Initialize configuration
initialize_config() {
    log "Initializing configuration..."

    # Create default configuration file if it doesn't exist
    if [ ! -f "${CONFIG_DIR}/monitor_config.yaml" ]; then
        cat > "${CONFIG_DIR}/monitor_config.yaml" << EOF
# HyperFocus Zone System Monitor Configuration
monitoring:
  interval: ${MONITORING_INTERVAL}
  log_level: "${LOG_LEVEL}"

alerts:
  enabled: ${ENABLE_ALERTS}
  thresholds:
    cpu_percent: ${ALERT_CPU_THRESHOLD}
    memory_percent: ${ALERT_MEMORY_THRESHOLD}
    disk_usage_percent: ${ALERT_DISK_THRESHOLD}

export:
  enabled: ${EXPORT_METRICS}
  formats:
    - csv
    - json

logging:
  file: "/app/logs/system_monitor.log"
  level: "${LOG_LEVEL}"
  max_size_mb: 10
  backup_count: 5

database:
  enabled: false
  type: "postgresql"
  host: "postgres"
  port: 5432
  database: "hyperfocus_monitoring"
  username: "hyperfocus"
  # Password should be set via environment variable

redis:
  enabled: false
  host: "redis"
  port: 6379
  # Password should be set via environment variable
EOF
        log "Default configuration created"
    else
        log "Configuration file already exists"
    fi
}

# Wait for dependencies
wait_for_dependencies() {
    if [ "${DATABASE_ENABLED:-false}" = "true" ]; then
        log "Waiting for PostgreSQL to be ready..."
        while ! nc -z postgres 5432; do
            sleep 1
        done
        log "PostgreSQL is ready"
    fi

    if [ "${REDIS_ENABLED:-false}" = "true" ]; then
        log "Waiting for Redis to be ready..."
        while ! nc -z redis 6379; do
            sleep 1
        done
        log "Redis is ready"
    fi
}

# Health check function
health_check() {
    log "Performing health check..."
    python -c "
from system_monitor import SystemMonitor
import sys
try:
    monitor = SystemMonitor()
    metrics = monitor.collect_metrics()
    print('✅ Health check passed')
    sys.exit(0)
except Exception as e:
    print(f'❌ Health check failed: {e}')
    sys.exit(1)
"
}

# Start monitoring function
start_monitoring() {
    log "Starting HyperFocus Zone System Monitor..."
    log "Configuration:"
    log "  - Monitoring interval: ${MONITORING_INTERVAL}s"
    log "  - Log level: ${LOG_LEVEL}"
    log "  - Alerts enabled: ${ENABLE_ALERTS}"
    log "  - CPU threshold: ${ALERT_CPU_THRESHOLD}%"
    log "  - Memory threshold: ${ALERT_MEMORY_THRESHOLD}%"
    log "  - Disk threshold: ${ALERT_DISK_THRESHOLD}%"

    # Start the monitoring with environment variables
    python system_monitor.py
}

# Run demo function
run_demo() {
    log "Running HyperFocus Zone System Monitor Demo..."
    python demo_system_monitor.py
}

# Run tests function
run_tests() {
    log "Running test suite..."
    python -m pytest test_system_monitor.py -v
}

# Setup function
setup() {
    log "Setting up HyperFocus Zone System Monitor..."
    python setup_system_monitor.py
}

# Main execution logic
main() {
    log "🚀 HyperFocus Zone System Monitor Container Starting..."

    # Create directories
    create_directories

    # Initialize configuration
    initialize_config

    # Wait for dependencies if needed
    wait_for_dependencies

    # Handle different commands
    case "${1:-monitor}" in
        "monitor")
            start_monitoring
            ;;
        "demo")
            run_demo
            ;;
        "test")
            run_tests
            ;;
        "setup")
            setup
            ;;
        "health")
            health_check
            ;;
        "bash"|"sh")
            log "Starting interactive shell..."
            exec /bin/bash
            ;;
        *)
            log "Available commands:"
            log "  monitor  - Start real-time monitoring (default)"
            log "  demo     - Run demonstration"
            log "  test     - Run test suite"
            log "  setup    - Run setup and installation"
            log "  health   - Perform health check"
            log "  bash     - Start interactive shell"
            log ""
            log "Usage: docker run hyperfocus-monitor [command]"
            exit 1
            ;;
    esac
}

# Trap signals for graceful shutdown
cleanup() {
    log "Received shutdown signal, cleaning up..."
    # Add any cleanup logic here
    exit 0
}

trap cleanup SIGTERM SIGINT

# Execute main function
main "$@"

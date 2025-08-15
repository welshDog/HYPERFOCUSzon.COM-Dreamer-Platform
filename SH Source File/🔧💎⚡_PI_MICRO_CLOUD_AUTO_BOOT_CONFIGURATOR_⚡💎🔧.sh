#!/bin/bash
# 🚀💎⚡ PI MICRO-CLOUD AUTO-BOOT CONFIGURATION SCRIPT ⚡💎🚀

echo "🔧💎⚡ CONFIGURING PI MICRO-CLOUD AUTO-BOOT SYSTEM ⚡💎🔧"

# Create the systemd service file
create_systemd_service() {
    echo "📝 Creating systemd service..."
    
    sudo tee /etc/systemd/system/pi-microcloud.service > /dev/null <<EOF
[Unit]
Description=🚀💎⚡ Pi Micro-Cloud Stack Auto-Boot Service ⚡💎🚀
Documentation=https://github.com/welshDog/HYPERFOCUSzon.COM-V10
After=network.target docker.service
Wants=network-online.target
Requires=docker.service
StartLimitIntervalSec=30
StartLimitBurst=3

[Service]
Type=forking
RemainAfterExit=yes
User=pi
Group=docker
WorkingDirectory=/home/pi/empire/pi-microcloud
Environment=HOME=/home/pi
Environment=USER=pi

# Pre-start checks
ExecStartPre=/bin/bash -c 'while ! docker info > /dev/null 2>&1; do echo "Waiting for Docker..."; sleep 2; done'
ExecStartPre=/usr/bin/docker compose down

# Main start command
ExecStart=/home/pi/empire/pi-microcloud/auto-start-microcloud.sh

# Health check
ExecStartPost=/bin/sleep 30
ExecStartPost=/bin/bash -c 'curl -f http://localhost/health || exit 1'

# Stop command
ExecStop=/usr/bin/docker compose down
ExecStopPost=/bin/sleep 10

# Restart configuration
Restart=on-failure
RestartSec=15
TimeoutStartSec=300
TimeoutStopSec=60

# Security settings
NoNewPrivileges=true
PrivateTmp=true

[Install]
WantedBy=multi-user.target
EOF

    echo "✅ Systemd service created successfully"
}

# Create the auto-start script
create_auto_start_script() {
    echo "📝 Creating auto-start script..."
    
    tee /home/pi/empire/pi-microcloud/auto-start-microcloud.sh > /dev/null <<EOF
#!/bin/bash
# 🚀💎⚡ PI MICRO-CLOUD AUTO-START SCRIPT ⚡💎🚀

LOG_FILE="/var/log/pi-microcloud.log"
COMPOSE_FILE="/home/pi/empire/pi-microcloud/docker-compose.yml"

# Logging function
log_message() {
    echo "\$(date '+%Y-%m-%d %H:%M:%S'): \$1" | tee -a "\$LOG_FILE"
}

log_message "🚀 Starting Pi Micro-Cloud Stack Auto-Boot..."

# Ensure we're in the right directory
cd /home/pi/empire/pi-microcloud || {
    log_message "❌ Failed to change to microcloud directory"
    exit 1
}

# Wait for Docker to be fully ready
log_message "⏳ Waiting for Docker daemon..."
DOCKER_READY=0
for i in {1..30}; do
    if docker info > /dev/null 2>&1; then
        DOCKER_READY=1
        log_message "✅ Docker daemon is ready"
        break
    fi
    log_message "⏳ Docker not ready yet (attempt \$i/30)..."
    sleep 2
done

if [ \$DOCKER_READY -eq 0 ]; then
    log_message "❌ Docker daemon failed to start within timeout"
    exit 1
fi

# Clean up any existing containers
log_message "🧹 Cleaning up existing containers..."
docker compose down > /dev/null 2>&1 || true

# Wait a moment for cleanup
sleep 5

# Start the stack
log_message "🐳 Starting Docker Compose stack..."
if docker compose up -d; then
    log_message "✅ Docker Compose stack started successfully"
else
    log_message "❌ Failed to start Docker Compose stack"
    exit 1
fi

# Wait for services to initialize
log_message "⏳ Waiting for services to initialize..."
sleep 30

# Check service health
log_message "🔍 Checking service health..."
CONTAINERS=\$(docker ps --format "table {{.Names}}\t{{.Status}}" | grep -E "(pi-nginx|pi-redis|pi-broski|pi-monitor)")
log_message "📊 Container status:"
echo "\$CONTAINERS" | while read line; do
    log_message "   \$line"
done

# Get Pi IP address
PI_IP=\$(hostname -I | awk '{print \$1}' | tr -d ' ')
log_message "🌐 Pi IP Address: \$PI_IP"

# Test health endpoint
log_message "🔍 Testing health endpoint..."
for i in {1..10}; do
    if curl -f -s "http://localhost/health" > /dev/null 2>&1; then
        log_message "✅ Health endpoint responding"
        break
    elif [ \$i -eq 10 ]; then
        log_message "⚠️  Health endpoint not responding after 10 attempts"
    else
        log_message "⏳ Health endpoint not ready yet (attempt \$i/10)..."
        sleep 3
    fi
done

# Test Pi status endpoint
log_message "🔍 Testing Pi status endpoint..."
if curl -f -s "http://localhost/pi/status" > /dev/null 2>&1; then
    log_message "✅ Pi status endpoint responding"
else
    log_message "⚠️  Pi status endpoint not responding"
fi

# Final status report
log_message "📊 Pi Micro-Cloud Auto-Start Summary:"
log_message "   🌐 Health Check: http://\$PI_IP/health"
log_message "   📊 Status API: http://\$PI_IP/pi/status"
log_message "   ⚡ Offload API: http://\$PI_IP/api/offload"
log_message "   📈 Metrics: http://\$PI_IP/metrics"

log_message "🏆 Pi Micro-Cloud auto-start completed successfully!"

# Background health monitoring
nohup /home/pi/empire/pi-microcloud/health-monitor.sh > /dev/null 2>&1 &
log_message "🔍 Background health monitoring started"

exit 0
EOF

    chmod +x /home/pi/empire/pi-microcloud/auto-start-microcloud.sh
    echo "✅ Auto-start script created and made executable"
}

# Create health monitoring script
create_health_monitor() {
    echo "📝 Creating health monitoring script..."
    
    tee /home/pi/empire/pi-microcloud/health-monitor.sh > /dev/null <<EOF
#!/bin/bash
# 🔍💎⚡ PI MICRO-CLOUD HEALTH MONITOR ⚡💎🔍

LOG_FILE="/var/log/pi-microcloud-health.log"
CHECK_INTERVAL=60  # Check every minute

log_health() {
    echo "\$(date '+%Y-%m-%d %H:%M:%S'): \$1" >> "\$LOG_FILE"
}

while true; do
    # Check if main containers are running
    NGINX_STATUS=\$(docker ps --filter "name=pi-nginx" --format "{{.Status}}" | head -1)
    REDIS_STATUS=\$(docker ps --filter "name=pi-redis" --format "{{.Status}}" | head -1)
    AGENT_STATUS=\$(docker ps --filter "name=pi-broski" --format "{{.Status}}" | head -1)
    
    # Check health endpoint
    HEALTH_CHECK=\$(curl -f -s http://localhost/health 2>/dev/null && echo "OK" || echo "FAIL")
    
    # Get system metrics
    CPU_USAGE=\$(top -bn1 | grep "Cpu(s)" | awk '{print \$2}' | cut -d'%' -f1)
    MEMORY_USAGE=\$(free | grep Mem | awk '{printf "%.1f", \$3/\$2 * 100.0}')
    DISK_USAGE=\$(df -h / | tail -1 | awk '{print \$5}' | cut -d'%' -f1)
    
    # Temperature check (Pi-specific)
    TEMP=\$(vcgencmd measure_temp 2>/dev/null | cut -d'=' -f2 | cut -d"'" -f1 || echo "N/A")
    
    # Log health status
    if [[ "\$HEALTH_CHECK" == "OK" && "\$NGINX_STATUS" =~ "Up" && "\$REDIS_STATUS" =~ "Up" && "\$AGENT_STATUS" =~ "Up" ]]; then
        log_health "✅ System Healthy - CPU: \${CPU_USAGE}%, Memory: \${MEMORY_USAGE}%, Disk: \${DISK_USAGE}%, Temp: \${TEMP}°C"
    else
        log_health "⚠️  System Issues Detected - Health: \$HEALTH_CHECK, Nginx: \$NGINX_STATUS, Redis: \$REDIS_STATUS, Agent: \$AGENT_STATUS"
        
        # Attempt restart if critical services are down
        if [[ "\$HEALTH_CHECK" == "FAIL" ]]; then
            log_health "🔄 Attempting service restart..."
            cd /home/pi/empire/pi-microcloud
            docker compose restart > /dev/null 2>&1
            sleep 30
        fi
    fi
    
    # Keep log file manageable
    if [ \$(wc -l < "\$LOG_FILE") -gt 1000 ]; then
        tail -n 500 "\$LOG_FILE" > "\$LOG_FILE.tmp"
        mv "\$LOG_FILE.tmp" "\$LOG_FILE"
    fi
    
    sleep \$CHECK_INTERVAL
done
EOF

    chmod +x /home/pi/empire/pi-microcloud/health-monitor.sh
    echo "✅ Health monitoring script created"
}

# Create log rotation configuration
create_log_rotation() {
    echo "📝 Creating log rotation configuration..."
    
    sudo tee /etc/logrotate.d/pi-microcloud > /dev/null <<EOF
/var/log/pi-microcloud.log /var/log/pi-microcloud-health.log {
    daily
    rotate 7
    compress
    delaycompress
    missingok
    notifempty
    copytruncate
    su root root
}
EOF
    
    echo "✅ Log rotation configured"
}

# Main execution
main() {
    echo "🚀 Configuring Pi Micro-Cloud Auto-Boot System..."
    
    # Ensure directory exists
    mkdir -p /home/pi/empire/pi-microcloud
    
    # Create all components
    create_systemd_service
    create_auto_start_script
    create_health_monitor
    create_log_rotation
    
    # Enable the service
    sudo systemctl daemon-reload
    sudo systemctl enable pi-microcloud.service
    
    echo ""
    echo "🎊💎⚡ PI MICRO-CLOUD AUTO-BOOT CONFIGURATION COMPLETE! ⚡💎🎊"
    echo ""
    echo "✅ CONFIGURED FEATURES:"
    echo "   • 🔄 Automatic startup on boot"
    echo "   • 🔍 Health monitoring and auto-restart"
    echo "   • 📝 Comprehensive logging"
    echo "   • 🔄 Log rotation management"
    echo "   • ⚡ Graceful shutdown handling"
    echo ""
    echo "🛠️  MANAGEMENT COMMANDS:"
    echo "   • sudo systemctl status pi-microcloud"
    echo "   • sudo systemctl start pi-microcloud"
    echo "   • sudo systemctl stop pi-microcloud"
    echo "   • sudo systemctl restart pi-microcloud"
    echo "   • sudo systemctl disable pi-microcloud  # To disable auto-boot"
    echo "   • sudo journalctl -u pi-microcloud -f  # View live logs"
    echo "   • tail -f /var/log/pi-microcloud.log   # View application logs"
    echo ""
    echo "🏆 Your Pi will now automatically start the micro-cloud stack on every reboot!"
}

# Run main function
main "$@"

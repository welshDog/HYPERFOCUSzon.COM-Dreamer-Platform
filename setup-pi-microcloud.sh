#!/bin/bash
# 🚀💎⚡ RASPBERRY PI MICRO-CLOUD SETUP SCRIPT WITH AUTO-BOOT ⚡💎🚀

echo "🥧 Setting up Pi Micro-Cloud Stack with Auto-Boot..."

# Update system
echo "📦 Updating system packages..."
sudo apt update && sudo apt upgrade -y

# Install Docker
echo "🐳 Installing Docker..."
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
sudo usermod -aG docker $USER

# Install Docker Compose
echo "🔧 Installing Docker Compose..."
sudo apt install -y docker-compose-plugin

# Install additional dependencies
echo "📦 Installing additional dependencies..."
sudo apt install -y curl wget htop python3-pip

# Create empire directory
echo "📁 Creating empire directory structure..."
mkdir -p ~/empire/pi-microcloud
cd ~/empire/pi-microcloud

# Copy deployment files (if running from boot partition)
if [ -d "/boot/pi-microcloud" ]; then
    echo "📤 Copying deployment files from boot partition..."
    cp -r /boot/pi-microcloud/* ~/empire/pi-microcloud/
    chown -R pi:pi ~/empire/pi-microcloud
fi

# Set permissions
chmod +x sync/empire-sync.sh 2>/dev/null || echo "Empire sync script not found"

# Create systemd service for auto-boot
echo "🔧 Creating systemd service for auto-boot..."
sudo tee /etc/systemd/system/pi-microcloud.service > /dev/null <<EOF
[Unit]
Description=🚀💎⚡ Pi Micro-Cloud Stack Auto-Boot Service ⚡💎🚀
After=docker.service network.target
Requires=docker.service
StartLimitIntervalSec=0

[Service]
Type=oneshot
RemainAfterExit=yes
User=pi
WorkingDirectory=/home/pi/empire/pi-microcloud
ExecStart=/home/pi/empire/pi-microcloud/auto-start-microcloud.sh
ExecStop=/usr/bin/docker compose down
Restart=on-failure
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

# Create auto-start script
echo "📝 Creating auto-start script..."
tee auto-start-microcloud.sh > /dev/null <<'AUTOSTART_EOF'
#!/bin/bash
# 🚀💎⚡ PI MICRO-CLOUD AUTO-START SCRIPT ⚡💎🚀

LOG_FILE="/var/log/pi-microcloud.log"

log_message() {
    echo "$(date '+%Y-%m-%d %H:%M:%S'): $1" | sudo tee -a "$LOG_FILE"
}

log_message "🚀 Starting Pi Micro-Cloud Auto-Boot..."

# Wait for Docker to be ready
while ! docker info > /dev/null 2>&1; do
    log_message "⏳ Waiting for Docker to start..."
    sleep 5
done

# Change to microcloud directory
cd /home/pi/empire/pi-microcloud

# Start the stack
log_message "🐳 Starting Docker Compose stack..."
docker compose down 2>/dev/null || true
docker compose up -d

# Wait for services to be ready
log_message "⏳ Waiting for services to start..."
sleep 30

# Check service health
log_message "🔍 Checking service health..."
docker ps

# Test endpoints
PI_IP=$(hostname -I | awk '{print $1}')
log_message "🌐 Pi IP: $PI_IP"
log_message "🔍 Testing health endpoint..."
curl -s "http://localhost/health" > /dev/null && log_message "✅ Health check passed" || log_message "⚠️ Health check pending"

log_message "✅ Pi Micro-Cloud auto-start complete!"
log_message "🌐 Access status: http://$PI_IP/pi/status"
log_message "⚡ Offloading endpoint: http://$PI_IP/api/offload"

# Log successful start
echo "$(date): Pi Micro-Cloud started successfully" | sudo tee -a /var/log/pi-microcloud.log
AUTOSTART_EOF

# Make auto-start script executable
chmod +x auto-start-microcloud.sh

# Enable the service
echo "🔧 Enabling Pi Micro-Cloud auto-boot service..."
sudo systemctl daemon-reload
sudo systemctl enable pi-microcloud.service

# Start Docker if not running
echo "🐳 Starting Docker service..."
sudo systemctl start docker
sudo systemctl enable docker

# Deploy stack now
echo "🚀 Starting Pi Micro-Cloud deployment..."
docker compose up -d

# Wait for services to start
echo "⏳ Waiting for services to initialize..."
sleep 30

# Test the service
echo "🧪 Testing systemd service..."
sudo systemctl start pi-microcloud.service
sudo systemctl status pi-microcloud.service --no-pager

# Test endpoints
PI_IP=$(hostname -I | awk '{print $1}')
echo "🔍 Testing endpoints..."
echo "Health: $(curl -s http://localhost/health 2>/dev/null || echo 'Pending...')"

echo ""
echo "✅ Pi Micro-Cloud deployment complete with auto-boot enabled!"
echo "🔄 Your Pi will now automatically start the micro-cloud stack on every reboot!"
echo "🌐 Access status: http://$PI_IP/pi/status"
echo "⚡ Offloading endpoint: http://$PI_IP/api/offload"

# Show service management commands
echo ""
echo "🛠️  SERVICE MANAGEMENT COMMANDS:"
echo "   • Check status: sudo systemctl status pi-microcloud"
echo "   • Start service: sudo systemctl start pi-microcloud"
echo "   • Stop service: sudo systemctl stop pi-microcloud"
echo "   • Restart service: sudo systemctl restart pi-microcloud"
echo "   • Disable auto-boot: sudo systemctl disable pi-microcloud"
echo "   • View logs: sudo journalctl -u pi-microcloud -f"
echo "   • View app logs: tail -f /var/log/pi-microcloud.log"

echo ""
echo "🎊 DEPLOYMENT SUCCESS! Your Pi micro-cloud is ready for laptop assistance! 🚀💎⚡"

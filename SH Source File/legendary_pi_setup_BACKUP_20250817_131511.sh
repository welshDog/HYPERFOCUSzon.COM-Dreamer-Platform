#!/bin/bash
# 🥧💎⚡ LEGENDARY PI MICRO-CLOUD SETUP SCRIPT ⚡💎🥧
echo "🥧 Starting LEGENDARY Pi Micro-Cloud Setup..."

# Update system
echo "📦 Updating Pi system..."
sudo apt update && sudo apt upgrade -y

# Install essential packages
echo "🔧 Installing essential packages..."
sudo apt install -y curl wget git htop vim python3 python3-pip docker.io docker-compose nginx ufw net-tools iotop tmux tree

# Configure static IP
echo "🌐 Configuring static IP: 192.168.137.100..."
sudo tee -a /etc/dhcpcd.conf > /dev/null << 'EOF'

# LEGENDARY Pi Static IP Configuration
interface eth0
static ip_address=192.168.137.100/24
static routers=192.168.137.1
static domain_name_servers=8.8.8.8 8.8.4.4
EOF

# Enable Docker
echo "🐳 Configuring Docker..."
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -aG docker pi

# Configure firewall
echo "🛡️ Configuring firewall..."
sudo ufw --force enable
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow 8080/tcp
sudo ufw allow 9090/tcp
sudo ufw allow 3000/tcp
sudo ufw allow 9100/tcp

# Create directories
mkdir -p /home/pi/microcloud
mkdir -p /home/pi/microcloud/data
mkdir -p /home/pi/microcloud/logs
mkdir -p /home/pi/microcloud/config

# Set hostname
echo "legendary-pi-microcloud" | sudo tee /etc/hostname
sudo sed -i 's/raspberrypi/legendary-pi-microcloud/g' /etc/hosts

# Enable SSH
sudo systemctl enable ssh
sudo systemctl start ssh

echo "🎉 Pi setup complete! Reboot required."
echo "💡 After reboot, Pi will be at: 192.168.137.100"

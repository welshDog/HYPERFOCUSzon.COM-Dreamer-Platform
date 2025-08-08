#!/bin/bash
# 🚀💎⚡ RASPBERRY PI MICRO-CLOUD SETUP SCRIPT ⚡💎🚀

echo "🥧 Setting up Pi Micro-Cloud Stack..."

# Update system
sudo apt update && sudo apt upgrade -y

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
sudo usermod -aG docker $USER

# Install Docker Compose
sudo apt install -y docker-compose-plugin

# Create empire directory
mkdir -p ~/empire/pi-microcloud
cd ~/empire/pi-microcloud

echo "📁 Copy the pi-microcloud folder contents here"
echo "Then run: docker compose up -d"

echo "✅ Pi setup complete! Copy deployment files and run docker compose up -d"

#!/bin/bash
# 🥧💎⚡ PI NETWORK SETUP FOR GIGABIT OFFLOADING ⚡💎🥧
# Generated: 2025-08-08T23:52:54.567120
# Target Network: 192.168.137.0/24
# Laptop IP: 192.168.137.10

echo "🥧 Setting up Pi for Gigabit offloading..."

# Set static IP configuration
sudo tee -a /etc/dhcpcd.conf > /dev/null <<EOF

# Gigabit Pi Configuration for laptop offloading
interface eth0
static ip_address=192.168.137.100/24
static routers=192.168.137.1
static domain_name_servers=8.8.8.8 8.8.4.4
EOF

echo "📡 Restarting network services..."
sudo systemctl daemon-reload
sudo systemctl restart dhcpcd

# Wait for network to come up
sleep 10

echo "🧪 Testing network connectivity..."
ping -c 4 192.168.137.1  # Gateway
ping -c 4 192.168.137.10  # Laptop
ping -c 4 8.8.8.8        # DNS

echo "✅ Pi network setup complete!"
echo "💡 Pi should now be accessible at: 192.168.137.100"
echo "🚀 Ready for micro-cloud deployment!"

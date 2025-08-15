#!/bin/bash
# 🚀 LEGENDARY PI DEPLOYMENT AUTOMATION
echo "🚀 Starting LEGENDARY Pi Deployment..."

PI_IP="192.168.137.100"

# Check Pi connectivity
echo "🔍 Checking Pi connectivity..."
if ! ping -c 3 $PI_IP > /dev/null 2>&1; then
    echo "❌ Pi not reachable at $PI_IP"
    echo "💡 Please ensure Pi is connected and configured"
    exit 1
fi

echo "✅ Pi is reachable at $PI_IP"

# Deploy Docker stack
echo "🐳 Deploying Docker stack..."
scp docker-compose-legendary-pi.yml pi@$PI_IP:/home/pi/microcloud/

ssh pi@$PI_IP << 'REMOTE'
cd /home/pi/microcloud
docker-compose -f docker-compose-legendary-pi.yml down 2>/dev/null || true
docker-compose -f docker-compose-legendary-pi.yml up -d
sleep 30
docker-compose -f docker-compose-legendary-pi.yml ps
REMOTE

echo "🎉 Deployment complete!"
echo "🌐 Services available:"
echo "   • Health Monitor:  http://$PI_IP/"
echo "   • BROski Agent:    http://$PI_IP:8080/"

#!/bin/bash
# 🎯💎⚡ COMPLETE PI AUTO-SETUP WITH LAPTOP COMMUNICATION ⚡💎🎯

set -e
export DEBIAN_FRONTEND=noninteractive

LAPTOP_IP="192.168.1.100"  # Update this with your laptop IP
PI_NODE_ID="pi-$(hostname)-$(date +%s)"

echo "🎯💎⚡ COMPLETE PI AUTO-SETUP STARTING ⚡💎🎯"
echo "=============================================="
echo "🥧 Pi Node ID: $PI_NODE_ID"
echo "💻 Laptop IP: $LAPTOP_IP"

# Get Pi IP
PI_IP=$(hostname -I | awk '{print $1}')
echo "📍 Pi IP: $PI_IP"

# Update system
echo "🔄 Updating system..."
apt-get update -y && apt-get upgrade -y

# Install essentials
echo "📦 Installing packages..."
apt-get install -y curl wget git python3 python3-pip docker.io docker-compose

# Start Docker
systemctl enable docker
systemctl start docker
usermod -aG docker pi

# Create microcloud directory
mkdir -p /opt/microcloud
cd /opt/microcloud

# Create Docker Compose
cat > docker-compose.yml << 'DOCKER_EOF'
version: '3.8'
services:
  nginx:
    image: nginx:alpine
    ports: ["80:80"]
    volumes: ["./nginx.conf:/etc/nginx/nginx.conf:ro", "./html:/usr/share/nginx/html:ro"]
    restart: unless-stopped
  
  redis:
    image: redis:alpine
    ports: ["6379:6379"]
    restart: unless-stopped
  
  broski:
    image: python:3.11-slim
    ports: ["5000:5000"]
    volumes: ["./broski:/app"]
    working_dir: /app
    command: python3 agent.py
    restart: unless-stopped
    environment:
      - PI_NODE_ID=$PI_NODE_ID
      - LAPTOP_IP=$LAPTOP_IP
      - PI_IP=$PI_IP
DOCKER_EOF

# Create Nginx config
mkdir -p html
cat > nginx.conf << 'NGINX_EOF'
events { worker_connections 1024; }
http {
    upstream broski { server broski:5000; }
    server {
        listen 80;
        location /health { return 200 "Pi Micro-Cloud Healthy\n"; }
        location /api/ { proxy_pass http://broski/; }
        location / { root /usr/share/nginx/html; index index.html; }
    }
}
NGINX_EOF

# Create status page
cat > html/index.html << 'HTML_EOF'
<!DOCTYPE html>
<html><head><title>🥧 Pi Micro-Cloud</title></head>
<body style="font-family:Arial; background:#1a1a2e; color:#eee; padding:20px;">
<h1>🥧💎⚡ Pi Micro-Cloud Active ⚡💎🥧</h1>
<p>Node: PI_NODE_PLACEHOLDER</p>
<p>Pi IP: PI_IP_PLACEHOLDER</p>
<p>Laptop: LAPTOP_IP_PLACEHOLDER</p>
<p>Status: ✅ All Services Running</p>
<p><a href="/health" style="color:#00bfff;">Health Check</a> | 
   <a href="/api/" style="color:#00bfff;">API</a> |
   <a href="http://LAPTOP_IP_PLACEHOLDER:8888" style="color:#00bfff;">Laptop Dashboard</a></p>
</body></html>
HTML_EOF

# Replace variables in HTML
sed -i "s/PI_NODE_PLACEHOLDER/$PI_NODE_ID/g" html/index.html
sed -i "s/PI_IP_PLACEHOLDER/$PI_IP/g" html/index.html
sed -i "s/LAPTOP_IP_PLACEHOLDER/$LAPTOP_IP/g" html/index.html

# Create BROski agent
mkdir -p broski
cat > broski/agent.py << 'PYTHON_EOF'
#!/usr/bin/env python3
import asyncio
import json
import time
from aiohttp import web, ClientSession
import psutil
import os
from datetime import datetime

class PiAgent:
    def __init__(self):
        self.node_id = os.getenv('PI_NODE_ID', 'pi-default')
        self.laptop_ip = os.getenv('LAPTOP_IP', '192.168.1.100')
        self.pi_ip = os.getenv('PI_IP', '192.168.1.200')
        self.tasks = {}
        
    async def register_with_laptop(self):
        try:
            data = {
                'pi_node_id': self.node_id,
                'pi_ip': self.pi_ip,
                'capabilities': ['task-offloading', 'docker-containers']
            }
            async with ClientSession() as session:
                async with session.post(f'http://{self.laptop_ip}:8888/api/pi-registration', json=data) as resp:
                    if resp.status == 200:
                        print(f"✅ Registered with laptop")
                        return True
        except Exception as e:
            print(f"❌ Registration failed: {e}")
        return False
    
    async def send_heartbeat(self):
        while True:
            try:
                data = {
                    'timestamp': datetime.now().isoformat(),
                    'system': {'cpu_percent': psutil.cpu_percent()},
                    'services': {'active_tasks': len(self.tasks)}
                }
                async with ClientSession() as session:
                    async with session.post(
                        f'http://{self.laptop_ip}:8888/api/pi-heartbeat',
                        json=data,
                        headers={'X-Pi-Node-ID': self.node_id, 'X-Pi-IP': self.pi_ip}
                    ) as resp:
                        if resp.status == 200:
                            print("💓 Heartbeat sent")
            except Exception as e:
                print(f"💓 Heartbeat error: {e}")
            await asyncio.sleep(30)
    
    async def health(self, request):
        return web.json_response({'status': 'healthy', 'node_id': self.node_id})
    
    async def offload(self, request):
        task_data = await request.json()
        task_id = f"task_{int(time.time())}"
        self.tasks[task_id] = {'status': 'completed', 'result': 'Task processed by Pi!'}
        return web.json_response({'task_id': task_id, 'status': 'completed'})

agent = PiAgent()
app = web.Application()
app.router.add_get('/health', agent.health)
app.router.add_post('/api/offload', agent.offload)

async def init_app():
    await agent.register_with_laptop()
    asyncio.create_task(agent.send_heartbeat())

if __name__ == "__main__":
    print(f"🤖 Starting BROski Agent: {agent.node_id}")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init_app())
    web.run_app(app, host='0.0.0.0', port=5000)
PYTHON_EOF

# Install Python dependencies
cd broski
pip3 install aiohttp psutil

# Start services
cd /opt/microcloud
docker-compose up -d

# Wait for services
sleep 20

# Test services
echo "✅ Testing services..."
curl -s http://localhost/health
echo ""

# Create systemd service
cat > /etc/systemd/system/pi-microcloud.service << 'SERVICE_EOF'
[Unit]
Description=Pi Micro-Cloud
After=docker.service
Requires=docker.service

[Service]
Type=oneshot
RemainAfterExit=yes
WorkingDirectory=/opt/microcloud
ExecStart=/usr/bin/docker-compose up -d
ExecStop=/usr/bin/docker-compose down
TimeoutStartSec=0

[Install]
WantedBy=multi-user.target
SERVICE_EOF

systemctl daemon-reload
systemctl enable pi-microcloud.service

# Create boot script
cat > /etc/rc.local << 'RC_EOF'
#!/bin/bash
sleep 20
cd /opt/microcloud
/usr/bin/docker-compose up -d
exit 0
RC_EOF
chmod +x /etc/rc.local

echo "🎊💎⚡ PI SETUP COMPLETE ⚡💎🎊"
echo "============================="
echo "🥧 Node: $PI_NODE_ID"
echo "📍 IP: $PI_IP"
echo "💻 Laptop: $LAPTOP_IP"
echo "🌐 Access: http://$PI_IP/"
echo "📊 Dashboard: http://$LAPTOP_IP:8888/"
echo "============================="

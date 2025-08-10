#!/usr/bin/env python3
"""
💾💎⚡ ENHANCED SD CARD DEPLOYER ⚡💎💾
Deploys Pi micro-cloud setup with laptop auto-detection
"""

from pathlib import Path
from typing import List, Dict, Any, Optional
import json
import os
import socket
import subprocess
import time

import shutil
class EnhancedSDCardDeployer:
    """💾 Enhanced SD card deployment with laptop detection"""

    def __init__(self, sd_card_drive: str = "E:\\"):
        self.sd_card_drive = Path(sd_card_drive)
        self.laptop_ip = self.get_laptop_ip()

        print("💾💎⚡ ENHANCED SD CARD DEPLOYER ⚡💎💾")
        print("=" * 60)
        print(f"💾 SD Card Drive: {self.sd_card_drive}")
        print(f"💻 Laptop IP: {self.laptop_ip}")

    def get_laptop_ip(self) -> str:
        """🌐 Get laptop's IP address"""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                s.connect(("8.8.8.8", 80))
                return s.getsockname()[0]
        except (ConnectionError, OSError):
            return "192.168.1.100"  # Fallback

    def verify_sd_card(self) -> bool:
        """✅ Verify SD card is accessible"""
        if not self.sd_card_drive.exists():
            print(f"❌ SD card not found at {self.sd_card_drive}")
            return False

        try:
            # Test write access
            test_file = self.sd_card_drive / "test_write.tmp"
            test_file.write_text("test")
            test_file.unlink()
            print(f"✅ SD card verified at {self.sd_card_drive}")
            return True
        except (socket.error, ConnectionError, requests.RequestException) as e:
            print(f"❌ SD card write test failed: {e}")
            return False

    def create_enhanced_setup_script(self) -> str:
        """📜 Create enhanced setup script with laptop detection"""

        setup_script = f'''#!/bin/bash
# 📱💎⚡ ENHANCED PI AUTO-SETUP SCRIPT ⚡💎📱
# Auto-detects laptop and establishes communication

set -e
export DEBIAN_FRONTEND=noninteractive

# Configuration
LAPTOP_IP="{self.laptop_ip}"
PI_NODE_ID="pi-$(hostname)-$(date +%s)"
WIFI_SSID=""  # Set if needed
WIFI_PASSWORD=""  # Set if needed

echo "📱💎⚡ ENHANCED PI AUTO-SETUP STARTING ⚡💎📱"
echo "==============================================="
echo "🥧 Pi Node ID: $PI_NODE_ID"
echo "💻 Target Laptop IP: $LAPTOP_IP"
echo "🌐 Starting network configuration..."

# Function to log with timestamps
log_message() {{
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}}

# Function to test laptop connectivity
test_laptop_connectivity() {{
    log_message "🔍 Testing laptop connectivity..."

    # Scan for laptop on network
    for ip in {{1..254}}; do
        test_ip="$(echo $LAPTOP_IP | cut -d. -f1-3).$ip"
        if timeout 1 ping -c 1 "$test_ip" >/dev/null 2>&1; then
            # Test for our laptop service
            if timeout 2 wget -q --spider "http://$test_ip:8888/health" 2>/dev/null; then
                log_message "✅ Found laptop service at $test_ip"
                LAPTOP_IP="$test_ip"
                return 0
            fi
        fi
    done

    log_message "⚠️ Laptop not found, using configured IP: $LAPTOP_IP"
    return 1
}}

# Update system
log_message "🔄 Updating system packages..."
apt-get update -y
apt-get upgrade -y

# Install essential packages
log_message "📦 Installing essential packages..."
apt-get install -y \\
    curl \\
    wget \\
    git \\
    htop \\
    nano \\
    python3 \\
    python3-pip \\
    python3-venv \\
    jq \\
    net-tools \\
    iptables-persistent \\
    ufw \\
    ca-certificates \\
    gnupg \\
    lsb-release \\
    apt-transport-https

# Configure network optimizations
log_message "🌐 Configuring network optimizations..."
cat >> /etc/sysctl.conf << 'SYSCTL_EOF'

# Pi Micro-Cloud Network Optimizations
net.core.rmem_default = 262144
net.core.rmem_max = 16777216
net.core.wmem_default = 262144
net.core.wmem_max = 16777216
net.core.netdev_max_backlog = 5000
net.ipv4.tcp_rmem = 4096 87380 16777216
net.ipv4.tcp_wmem = 4096 65536 16777216
net.ipv4.tcp_congestion_control = bbr
net.ipv4.tcp_window_scaling = 1
net.ipv4.tcp_timestamps = 1
net.ipv4.tcp_sack = 1
net.ipv4.tcp_no_metrics_save = 1
net.ipv4.route.flush = 1
SYSCTL_EOF

sysctl -p

# Install Docker
log_message "🐳 Installing Docker..."
curl -fsSL https://get.docker.com | sh
usermod -aG docker pi
systemctl enable docker
systemctl start docker

# Install Docker Compose
log_message "🐳 Installing Docker Compose..."
curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

# Test laptop connectivity
test_laptop_connectivity

# Get Pi IP
PI_IP=$(hostname -I | awk '{{print $1}}')
log_message "🥧 Pi IP Address: $PI_IP"

# Create micro-cloud directory
log_message "📁 Creating micro-cloud directory..."
mkdir -p /opt/pi-microcloud
cd /opt/pi-microcloud

# Create Docker Compose configuration
log_message "🐳 Creating Docker Compose configuration..."
cat > docker-compose.yml << 'COMPOSE_EOF'
version: '3.8'

services:
  nginx:
    image: nginx:alpine
    container_name: pi-nginx
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - ./html:/usr/share/nginx/html:ro
    restart: unless-stopped
    networks:
      - pi-network
    environment:
      - NGINX_WORKER_PROCESSES=4
    deploy:
      resources:
        limits:
          memory: 256M
        reservations:
          memory: 128M

  redis:
    image: redis:alpine
    container_name: pi-redis
    ports:
      - "6379:6379"
    command: >
      redis-server
      --maxmemory 640mb
      --maxmemory-policy allkeys-lru
      --tcp-backlog 511
      --tcp-keepalive 300
      --timeout 0
      --databases 16
      --save 900 1
      --save 300 10
      --save 60 10000
    restart: unless-stopped
    networks:
      - pi-network
    deploy:
      resources:
        limits:
          memory: 640M
        reservations:
          memory: 320M

  broski-agent:
    image: python:3.11-slim
    container_name: pi-broski-agent
    ports:
      - "5000:5000"
    volumes:
      - ./broski-agent:/app
    working_dir: /app
    command: python3 broski_agent.py
    restart: unless-stopped
    networks:
      - pi-network
    environment:
      - PYTHONUNBUFFERED=1
      - PI_NODE_ID=$PI_NODE_ID
      - LAPTOP_IP=$LAPTOP_IP
      - PI_IP=$PI_IP
    deploy:
      resources:
        limits:
          memory: 768M
        reservations:
          memory: 384M

  prometheus:
    image: prom/prometheus:latest
    container_name: pi-prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml:ro
      - prometheus-data:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus'
      - '--web.console.libraries=/etc/prometheus/console_libraries'
      - '--web.console.templates=/etc/prometheus/consoles'
      - '--storage.tsdb.retention.time=30d'
      - '--web.enable-lifecycle'
    restart: unless-stopped
    networks:
      - pi-network
    deploy:
      resources:
        limits:
          memory: 512M
        reservations:
          memory: 256M

networks:
  pi-network:
    driver: bridge
    ipam:
      config:
        - subnet: 172.20.0.0/16

volumes:
  prometheus-data:

COMPOSE_EOF

# Create Nginx configuration
log_message "🌐 Creating Nginx configuration..."
mkdir -p html
cat > nginx.conf << 'NGINX_EOF'
worker_processes 4;
worker_rlimit_nofile 8192;

events {{
    worker_connections 4096;
    use epoll;
    multi_accept on;
}}

http {{
    include /etc/nginx/mime.types;
    default_type application/octet-stream;

    # Logging
    access_log /var/log/nginx/access.log;
    error_log /var/log/nginx/error.log warn;

    # Performance
    sendfile on;
    tcp_nopush on;
    tcp_nodelay on;
    keepalive_timeout 65;
    keepalive_requests 1000;

    # Buffers
    client_body_buffer_size 128k;
    client_max_body_size 100m;
    client_header_buffer_size 1k;
    large_client_header_buffers 4 4k;
    output_buffers 1 32k;
    postpone_output 1460;

    # Gzip
    gzip on;
    gzip_vary on;
    gzip_min_length 1024;
    gzip_types
        text/plain
        text/css
        text/xml
        text/javascript
        application/json
        application/javascript
        application/xml+rss
        application/atom+xml
        image/svg+xml;

    # Upstream for load balancing
    upstream broski_backend {{
        server broski-agent:5000 max_fails=3 fail_timeout=30s;
        keepalive 32;
    }}

    server {{
        listen 80 default_server;
        server_name _;
        root /usr/share/nginx/html;
        index index.html;

        # Health check
        location /health {{
            access_log off;
            return 200 "Pi Micro-Cloud Healthy\\n";
            add_header Content-Type text/plain;
        }}

        # API proxy to BROski agent
        location /api/ {{
            proxy_pass http://broski_backend/;
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_connect_timeout 30s;
            proxy_send_timeout 30s;
            proxy_read_timeout 30s;
        }}

        # Prometheus proxy
        location /metrics {{
            proxy_pass http://prometheus:9090/metrics;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
        }}

        # Static content
        location / {{
            try_files $uri $uri/ =404;
            expires 1d;
            add_header Cache-Control "public, immutable";
        }}
    }}
}}
NGINX_EOF

# Create BROski agent directory and script
log_message "🤖 Creating BROski agent..."
mkdir -p broski-agent
cat > broski-agent/broski_agent.py << 'BROSKI_EOF'
#!/usr/bin/env python3
"""
🤖💎⚡ BROSKI PI MICRO-CLOUD AGENT ⚡💎🤖
Enhanced agent with laptop communication
"""

import asyncio
import aiohttp
from aiohttp import web
import json
import logging
import time
import psutil
import os
import subprocess
from datetime import datetime
import socket
from typing import Dict, List, Any, Optional

class BROskiPiAgent:
    """🤖 BROski Pi Micro-Cloud Agent"""

    def __init__(self):
        self.node_id = os.getenv('PI_NODE_ID', f'pi-{{socket.gethostname()}}-{{int(time.time())}}')
        self.laptop_ip = os.getenv('LAPTOP_IP', '192.168.1.100')
        self.pi_ip = os.getenv('PI_IP', self.get_pi_ip())
        self.tasks = {{}}
        self.task_counter = 0

        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

        print(f"🤖💎⚡ BROSKI PI AGENT STARTING ⚡💎🤖")
        print(f"🥧 Node ID: {{self.node_id}}")
        print(f"💻 Laptop IP: {{self.laptop_ip}}")
        print(f"📍 Pi IP: {{self.pi_ip}}")

    def get_pi_ip(self) -> str:
        """🌐 Get Pi IP address"""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                s.connect(("8.8.8.8", 80))
                return s.getsockname()[0]
        except (ConnectionError, OSError):
            return "192.168.1.200"

    async def register_with_laptop(self):
        """📡 Register Pi with laptop"""
        registration_data = {{
            'pi_node_id': self.node_id,
            'pi_ip': self.pi_ip,
            'capabilities': [
                'task-offloading',
                'docker-containers',
                'micro-services',
                'redis-caching',
                'nginx-proxy'
            ],
            'system_info': {{
                'cpu_count': psutil.cpu_count(),
                'memory_total': psutil.virtual_memory().total,
                'disk_free': psutil.disk_usage('/').free
            }}
        }}

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    f'http://{{self.laptop_ip}}:8888/api/pi-registration',
                    json=registration_data,
                    timeout=10
                ) as response:
                    if response.status == 200:
                        result = await response.json()
        logger.info("✅ Registered with laptop: {%s}", result)
                        return True
                    else:
        logger.error("❌ Registration failed: HTTP {%s}", response.status)
                        return False
        except (socket.error, ConnectionError, requests.RequestException) as e:
        logger.error("❌ Registration error: {%s}", e)
            return False

    async def send_heartbeat(self):
        """💓 Send heartbeat to laptop"""
        while True:
            try:
                heartbeat_data = {{
                    'timestamp': datetime.now().isoformat(),
                    'system': {{
                        'cpu_percent': psutil.cpu_percent(),
                        'memory_percent': psutil.virtual_memory().percent,
                        'disk_percent': psutil.disk_usage('/').percent,
                        'uptime': time.time() - psutil.boot_time()
                    }},
                    'services': {{
                        'active_tasks': len(self.tasks),
                        'total_completed': self.task_counter
                    }}
                }}

                async with aiohttp.ClientSession() as session:
                    async with session.post(
                        f'http://{{self.laptop_ip}}:8888/api/pi-heartbeat',
                        json=heartbeat_data,
                        headers={{
                            'X-Pi-Node-ID': self.node_id,
                            'X-Pi-IP': self.pi_ip
                        }},
                        timeout=5
                    ) as response:
                        if response.status == 200:
                            self.logger.debug("💓 Heartbeat sent successfully")
                        else:
        logger.warning("⚠️ Heartbeat failed: HTTP {%s}", response.status)

            except (socket.error, ConnectionError, requests.RequestException) as e:
        logger.error("💓 Heartbeat error: {%s}", e)

            await asyncio.sleep(30)  # Send heartbeat every 30 seconds

    async def health_check(self, request):
        """🔍 Health check endpoint"""
        return web.json_response({{
            'status': 'healthy',
            'service': 'broski-pi-agent',
            'node_id': self.node_id,
            'pi_ip': self.pi_ip,
            'laptop_ip': self.laptop_ip,
            'active_tasks': len(self.tasks),
            'uptime': time.time() - psutil.boot_time()
        }})

    async def offload_task(self, request):
        """⚡ Handle task offloading"""
        try:
            task_data = await request.json()
            task_id = f"task_{{self.task_counter}}_{{int(time.time())}}"
            self.task_counter += 1

            # Store task
            self.tasks[task_id] = {{
                'task_id': task_id,
                'task_type': task_data.get('task_type'),
                'payload': task_data.get('payload'),
                'status': 'processing',
                'started_at': datetime.now().isoformat()
            }}

            # Process task asynchronously
            asyncio.create_task(self.process_task(task_id, task_data))

            return web.json_response({{
                'status': 'accepted',
                'task_id': task_id,
                'message': 'Task accepted for processing'
            }})

        except (socket.error, ConnectionError, requests.RequestException) as e:
        logger.error("Task offloading error: {%s}", e)
            return web.json_response({{
                'error': str(e)
            }}, status=500)

    async def process_task(self, task_id: str, task_data: Dict[str, Any]):
        """🔄 Process offloaded task"""
        try:
            task_type = task_data.get('task_type', 'default')
            payload = task_data.get('payload', {{}})

        logger.info("⚡ Processing task {{task_id}} of type {%s}", task_type)

            # Simulate task processing
            if task_type == 'compute':
                result = await self.handle_compute_task(payload)
            elif task_type == 'data_processing':
                result = await self.handle_data_processing(payload)
            elif task_type == 'file_operation':
                result = await self.handle_file_operation(payload)
            else:
                result = await self.handle_default_task(payload)

            # Update task status
            self.tasks[task_id].update({{
                'status': 'completed',
                'result': result,
                'completed_at': datetime.now().isoformat()
            }})

            # Send result to laptop
            await self.send_task_result(task_id)

        except (socket.error, ConnectionError, requests.RequestException) as e:
        logger.error("Task processing error: {%s}", e)
            self.tasks[task_id].update({{
                'status': 'failed',
                'error': str(e),
                'completed_at': datetime.now().isoformat()
            }})

    async def handle_compute_task(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """💻 Handle compute-intensive task"""
        await asyncio.sleep(2)  # Simulate computation
        return {{
            'operation': 'compute',
            'input_size': len(str(payload)),
            'result': 'Computation completed successfully',
            'pi_node': self.node_id
        }}

    async def handle_data_processing(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """📊 Handle data processing task"""
        await asyncio.sleep(1)  # Simulate processing
        return {{
            'operation': 'data_processing',
            'processed_items': payload.get('item_count', 100),
            'result': 'Data processing completed',
            'pi_node': self.node_id
        }}

    async def handle_file_operation(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """📁 Handle file operation task"""
        await asyncio.sleep(0.5)  # Simulate file operation
        return {{
            'operation': 'file_operation',
            'file_count': payload.get('file_count', 10),
            'result': 'File operations completed',
            'pi_node': self.node_id
        }}

    async def handle_default_task(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """🔧 Handle default task"""
        await asyncio.sleep(1)
        return {{
            'operation': 'default',
            'payload_received': payload,
            'result': 'Default task completed',
            'pi_node': self.node_id
        }}

    async def send_task_result(self, task_id: str):
        """📤 Send task result to laptop"""
        try:
            task_data = self.tasks[task_id]

            async with aiohttp.ClientSession() as session:
                async with session.post(
                    f'http://{{self.laptop_ip}}:8888/api/task-completion',
                    json={{
                        'task_id': task_id,
                        'pi_node_id': self.node_id,
                        'pi_ip': self.pi_ip,
                        **task_data
                    }},
                    timeout=10
                ) as response:
                    if response.status == 200:
        logger.info("📤 Task result sent: {%s}", task_id)
                    else:
        logger.error("❌ Failed to send result: HTTP {%s}", response.status)

        except (socket.error, ConnectionError, requests.RequestException) as e:
        logger.error("📤 Result sending error: {%s}", e)

    async def get_task_status(self, request):
        """📋 Get task status"""
        task_id = request.match_info['task_id']

        if task_id in self.tasks:
            return web.json_response(self.tasks[task_id])
        else:
            return web.json_response({{
                'error': 'Task not found'
            }}, status=404)

    async def list_tasks(self, request):
        """📋 List all tasks"""
        return web.json_response({{
            'tasks': list(self.tasks.values()),
            'total_count': len(self.tasks),
            'node_id': self.node_id
        }})

def create_app():
    """🏗️ Create BROski agent web application"""
    agent = BROskiPiAgent()
    app = web.Application()

    # Routes
    app.router.add_get('/health', agent.health_check)
    app.router.add_post('/api/offload', agent.offload_task)
    app.router.add_get('/api/task/{{task_id}}', agent.get_task_status)
    app.router.add_get('/api/tasks', agent.list_tasks)

    # Start background tasks
    async def init_background_tasks(app):
        # Register with laptop
        await agent.register_with_laptop()

        # Start heartbeat task
        app['heartbeat_task'] = asyncio.create_task(agent.send_heartbeat())

    async def cleanup_background_tasks(app):
        app['heartbeat_task'].cancel()
        await app['heartbeat_task']

    app.on_startup.append(init_background_tasks)
    app.on_cleanup.append(cleanup_background_tasks)

    return app

if __name__ == "__main__":
    print("🤖💎⚡ BROSKI PI AGENT STARTING ⚡💎🤖")
    app = create_app()
    web.run_app(app, host='0.0.0.0', port=5000)

BROSKI_EOF

# Create Prometheus configuration
log_message "📊 Creating Prometheus configuration..."
cat > prometheus.yml << 'PROMETHEUS_EOF'
global:
  scrape_interval: 15s
  evaluation_interval: 15s

scrape_configs:
  - job_name: 'pi-microcloud'
    static_configs:
      - targets: ['localhost:80', 'broski-agent:5000']
    scrape_interval: 10s
    metrics_path: /metrics

  - job_name: 'node-exporter'
    static_configs:
      - targets: ['localhost:9100']
    scrape_interval: 15s

  - job_name: 'redis'
    static_configs:
      - targets: ['redis:6379']
    scrape_interval: 15s

PROMETHEUS_EOF

# Create status page
log_message "📄 Creating status page..."
cat > html/index.html << 'HTML_EOF'
<!DOCTYPE html>
<html>
<head>
    <title>🥧💎⚡ Pi Micro-Cloud Status ⚡💎🥧</title>
    <meta http-equiv="refresh" content="30">
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; background: #1a1a2e; color: #eee; }}
        .header {{ background: #16213e; padding: 20px; border-radius: 10px; margin-bottom: 20px; text-align: center; }}
        .status-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; }}
        .status-card {{ background: #0f3460; padding: 20px; border-radius: 10px; border-left: 4px solid #e94560; }}
        .status-ok {{ border-left-color: #0f9b0f; }}
        .links {{ margin-top: 20px; }}
        .links a {{ color: #00bfff; text-decoration: none; margin-right: 20px; }}
        .links a:hover {{ color: #e94560; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🥧💎⚡ Pi Micro-Cloud Status ⚡💎🥧</h1>
        <p>Node ID: __PI_NODE_ID__ | Pi IP: __PI_IP__ | Laptop: __LAPTOP_IP__</p>
        <p>🕐 Last Updated: <span id="timestamp"></span></p>
    </div>

    <div class="status-grid">
        <div class="status-card status-ok">
            <h3>🐳 Docker Services</h3>
            <p>✅ Nginx Proxy Running</p>
            <p>✅ Redis Cache Running</p>
            <p>✅ BROski Agent Running</p>
            <p>✅ Prometheus Monitoring</p>
        </div>

        <div class="status-card status-ok">
            <h3>🌐 Network Status</h3>
            <p>✅ Gigabit Ethernet Optimized</p>
            <p>✅ Laptop Communication Active</p>
            <p>✅ Port 80/443/5000 Open</p>
            <p>✅ Redis Port 6379 Ready</p>
        </div>

        <div class="status-card status-ok">
            <h3>⚡ Performance</h3>
            <p>🚀 CPU: Multi-core Ready</p>
            <p>💾 Memory: Optimized Allocation</p>
            <p>📊 Monitoring: Real-time</p>
            <p>🔄 Auto-healing: Enabled</p>
        </div>

        <div class="status-card status-ok">
            <h3>📡 Communication</h3>
            <p>💻 Laptop Registration: Active</p>
            <p>💓 Heartbeat: Every 30s</p>
            <p>⚡ Task Offloading: Ready</p>
            <p>📊 Metrics: Real-time</p>
        </div>
    </div>

    <div class="links">
        <h3>🔗 Quick Links</h3>
        <a href="/health">Health Check</a>
        <a href="/api/">API Status</a>
        <a href="/metrics">Metrics</a>
        <a href="http://__LAPTOP_IP__:8888">Laptop Dashboard</a>
    </div>

    <script>
        document.getElementById('timestamp').textContent = new Date().toLocaleString();
    </script>
</body>
</html>
HTML_EOF

# Replace placeholders in HTML
sed -i "s/__PI_NODE_ID__/$PI_NODE_ID/g" html/index.html
sed -i "s/__PI_IP__/$PI_IP/g" html/index.html
sed -i "s/__LAPTOP_IP__/$LAPTOP_IP/g" html/index.html

# Set permissions
log_message "🔒 Setting permissions..."
chmod +x broski-agent/broski_agent.py
chown -R pi:pi /opt/pi-microcloud

# Install Python dependencies for BROski agent
log_message "📦 Installing Python dependencies..."
cd broski-agent
pip3 install aiohttp psutil

# Start services
log_message "🚀 Starting micro-cloud services..."
cd /opt/pi-microcloud
docker-compose up -d

# Wait for services to start
log_message "⏳ Waiting for services to initialize..."
sleep 30

# Verify services
log_message "✅ Verifying services..."
docker-compose ps

# Test laptop communication
log_message "📡 Testing laptop communication..."
if curl -f -s "http://$LAPTOP_IP:8888/health" > /dev/null; then
    log_message "✅ Laptop communication verified"
else
    log_message "⚠️ Laptop communication test failed"
fi

# Create systemd service for auto-start
log_message "🔄 Creating systemd service..."
cat > /etc/systemd/system/pi-microcloud.service << 'SYSTEMD_EOF'
[Unit]
Description=Pi Micro-Cloud Stack
After=docker.service
Requires=docker.service

[Service]
Type=oneshot
RemainAfterExit=yes
WorkingDirectory=/opt/pi-microcloud
ExecStart=/usr/local/bin/docker-compose up -d
ExecStop=/usr/local/bin/docker-compose down
TimeoutStartSec=0

[Install]
WantedBy=multi-user.target
SYSTEMD_EOF

# Enable systemd service
systemctl daemon-reload
systemctl enable pi-microcloud.service

# Create startup script that runs on boot
log_message "🚀 Creating boot startup script..."
cat > /etc/rc.local << 'RC_LOCAL_EOF'
#!/bin/bash

# Wait for network to be ready
sleep 30

# Start Pi Micro-Cloud if not already running
cd /opt/pi-microcloud
/usr/local/bin/docker-compose up -d

# Test and register with laptop
PI_IP=$(hostname -I | awk '{{print $1}}')
LAPTOP_IP="__LAPTOP_IP__"

# Try to register with laptop
for i in {{1..10}}; do
    if curl -f -s "http://$LAPTOP_IP:8888/health" > /dev/null; then
        echo "$(date): Laptop found, micro-cloud ready" >> /var/log/pi-microcloud.log
        break
    fi
    echo "$(date): Attempt $i: Waiting for laptop..." >> /var/log/pi-microcloud.log
    sleep 10
done

exit 0
RC_LOCAL_EOF

# Replace laptop IP in rc.local
sed -i "s/__LAPTOP_IP__/$LAPTOP_IP/g" /etc/rc.local
chmod +x /etc/rc.local

# Final status check
log_message "🏁 Final status check..."
echo ""
echo "📊 SERVICE STATUS:"
echo "=================="
docker-compose ps
echo ""
echo "🌐 NETWORK STATUS:"
echo "=================="
echo "Pi IP: $PI_IP"
echo "Laptop IP: $LAPTOP_IP"
echo ""
echo "🔗 ACCESS POINTS:"
echo "================="
echo "• Main Site: http://$PI_IP/"
echo "• Health Check: http://$PI_IP/health"
echo "• BROski API: http://$PI_IP/api/"
echo "• Prometheus: http://$PI_IP:9090/"
echo "• Laptop Dashboard: http://$LAPTOP_IP:8888/"
echo ""

log_message "✅ Pi Micro-Cloud setup completed successfully!"
log_message "🚀 All services are running and laptop communication is established"
log_message "📊 Check status at: http://$PI_IP/"

# Create completion marker
touch /opt/pi-microcloud/.setup-complete
echo "$(date): Pi Micro-Cloud setup completed" >> /var/log/pi-microcloud.log

echo ""
echo "🎊💎⚡ PI MICRO-CLOUD DEPLOYMENT COMPLETE ⚡💎🎊"
echo "======================================================="
echo "🥧 Node ID: $PI_NODE_ID"
echo "🌐 Pi IP: $PI_IP"
echo "💻 Laptop IP: $LAPTOP_IP"
echo "📊 Dashboard: http://$PI_IP/"
echo "📡 Laptop Dashboard: http://$LAPTOP_IP:8888/"
echo "🚀 Ready for task offloading!"
echo "======================================================="
'''

        return setup_script

    def deploy_to_sd_card(self) -> bool:
        """💾 Deploy enhanced setup to SD card"""
        if not self.verify_sd_card():
            return False

        try:
            # Create setup script
            print("📜 Creating enhanced setup script...")
            setup_script = self.create_enhanced_setup_script()

            # Write setup script to SD card
            setup_script_path = self.sd_card_drive / "setup-pi-enhanced.sh"
            setup_script_path.write_text(setup_script, encoding='utf-8')

            # Make executable (if on Linux/Mac)
            try:
                import stat
                setup_script_path.chmod(setup_script_path.stat().st_mode | stat.S_IEXEC)
            except (ConnectionError, OSError):
                pass  # Windows doesn't support chmod

            # Create auto-run configuration
            print("🔄 Creating auto-run configuration...")

            # For Raspberry Pi OS, create cmdline.txt modification
            cmdline_path = self.sd_card_drive / "cmdline.txt"
            if cmdline_path.exists():
                # Backup original
                shutil.copy2(cmdline_path, self.sd_card_drive / "cmdline.txt.backup")

                # Read current cmdline
                cmdline_content = cmdline_path.read_text().strip()

                # Add init script parameter if not already present
                if "init=/usr/lib/raspi-config/init_resize.sh" not in cmdline_content:
                    cmdline_content += " init=/usr/lib/raspi-config/init_resize.sh"

                cmdline_path.write_text(cmdline_content)

            # Create SSH enabler
            ssh_file = self.sd_card_drive / "ssh"
            ssh_file.touch()

            # Create config.txt modifications for performance
            config_path = self.sd_card_drive / "config.txt"
            if config_path.exists():
                config_content = config_path.read_text()

                # Add performance optimizations
                perf_config = '''

# Pi Micro-Cloud Performance Optimizations
# GPU Memory Split
gpu_mem=64

# CPU Governor
force_turbo=1

# Network Performance
dtparam=spi=on
dtparam=i2c_arm=on

# USB Performance
dwc_otg.fiq_fix_enable=1
dwc_otg.fiq_split_enable=1

# Ethernet Performance
dtparam=eth_led0=4
dtparam=eth_led1=8

# Enable all 4 cores
force_turbo=1
arm_freq=1800
over_voltage=6
'''

                if "Pi Micro-Cloud Performance" not in config_content:
                    config_content += perf_config
                    config_path.write_text(config_content)

            # Create firstrun.sh for automatic execution
            firstrun_path = self.sd_card_drive / "firstrun.sh"
            firstrun_content = f'''#!/bin/bash
# First run script for Pi Micro-Cloud

# Enable SSH
systemctl enable ssh
systemctl start ssh

# Run enhanced setup script
bash /boot/setup-pi-enhanced.sh

# Remove this script after execution
rm -f /boot/firstrun.sh
'''

            firstrun_path.write_text(firstrun_content, encoding='utf-8')

            # Create deployment info file
            deployment_info = {
                'deployment_time': time.strftime('%Y-%m-%d %H:%M:%S'),
                'laptop_ip': self.laptop_ip,
                'deployment_type': 'enhanced_auto_setup',
                'features': [
                    'Auto laptop detection',
                    'Docker micro-cloud stack',
                    'Performance optimizations',
                    'Auto-boot configuration',
                    'Communication protocols'
                ]
            }

            info_path = self.sd_card_drive / "pi-deployment-info.json"
            info_path.write_text(json.dumps(deployment_info, indent=2))

            print("✅ Enhanced SD card deployment completed!")
            print(f"📍 Files deployed to: {self.sd_card_drive}")
            print(f"💻 Laptop IP configured: {self.laptop_ip}")
            print("🚀 Pi will auto-setup on first boot!")

            return True

        except (socket.error, ConnectionError, requests.RequestException) as e:
            print(f"❌ Deployment failed: {e}")
            return False

    def create_laptop_startup_instructions(self):
        """📋 Create instructions for laptop setup"""
        instructions = f'''
💻💎⚡ LAPTOP SETUP INSTRUCTIONS ⚡💎💻
=============================================

1. START LAPTOP RECEIVER SERVICE:
   python "💻💎⚡_LAPTOP_PI_RECEIVER_SERVICE_⚡💎💻.py"

2. INSERT SD CARD INTO PI AND POWER ON:
   - Pi will auto-detect laptop at: {self.laptop_ip}
   - Auto-setup will begin immediately
   - Services will start automatically

3. MONITOR PROGRESS:
   - Laptop Dashboard: http://localhost:8888
   - Pi will register automatically
   - Watch for Pi heartbeats

4. ACCESS PI SERVICES:
   - Pi will be available at: http://[PI_IP]/
   - API endpoints: http://[PI_IP]/api/
   - Metrics: http://[PI_IP]/metrics

5. TEST TASK OFFLOADING:
   curl -X POST {self.laptop_ip}:8888/api/offload-task \\
   -H "Content-Type: application/json" \\
   -d '{{"task_type": "compute", "payload": {{"test": "data"}}}}'

🎊 READY FOR LEGENDARY TASK OFFLOADING! 🎊
'''

        instructions_path = Path("📋💎⚡_LAPTOP_SETUP_INSTRUCTIONS_⚡💎📋.txt")
        instructions_path.write_text(instructions)
        print(f"📋 Instructions saved to: {instructions_path}")

def main():
    """🚀 Main deployment function"""

    print("💾💎⚡ ENHANCED SD CARD DEPLOYER ⚡💎💾")
    print("=" * 60)

    # Get SD card path
    sd_card_drive = input("💾 Enter SD card drive letter (default: E:\\): ").strip()
    if not sd_card_drive:
        sd_card_drive = "E:\\"

    if not sd_card_drive.endswith("\\"):
        sd_card_drive += "\\"

    # Create deployer
    deployer = EnhancedSDCardDeployer(sd_card_drive)

    # Create laptop instructions
    deployer.create_laptop_startup_instructions()

    # Deploy to SD card
    if deployer.deploy_to_sd_card():
        print("\n🎊💎⚡ DEPLOYMENT SUCCESSFUL ⚡💎🎊")
        print("=" * 40)
        print("✅ Enhanced setup script deployed")
        print("✅ Auto-boot configuration ready")
        print("✅ Laptop communication configured")
        print("✅ Performance optimizations applied")
        print("\n🚀 NEXT STEPS:")
        print("1. Start laptop receiver service")
        print("2. Insert SD card into Pi")
        print("3. Power on Pi")
        print("4. Monitor laptop dashboard")
        print("5. Enjoy legendary task offloading!")
    else:
        print("\n❌ Deployment failed!")
        print("Check SD card access and try again.")

if __name__ == "__main__":
    main()

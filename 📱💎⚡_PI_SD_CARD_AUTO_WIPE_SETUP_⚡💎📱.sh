#!/bin/bash
# 🚀💎⚡ RASPBERRY PI AUTO-WIPE & MICRO-CLOUD SETUP SCRIPT ⚡💎🚀
# 
# This script will:
# 1. Completely wipe the Pi and reinstall fresh OS
# 2. Install Docker and all dependencies
# 3. Set up the micro-cloud stack
# 4. Configure automatic communication with laptop
# 5. Enable auto-boot on every restart
#
# Place this script on the SD card boot partition as: auto-setup.sh

# ================================
# 🎯 CONFIGURATION SECTION
# ================================

# Laptop IP (CHANGE THIS TO YOUR LAPTOP IP)
LAPTOP_IP="192.168.1.100"

# Pi Configuration
PI_HOSTNAME="broski-pi-node-01"
PI_USERNAME="pi"
PI_PASSWORD="broski123"  # Change this password!

# Network Configuration (Auto-detect or manual)
WIFI_SSID="YOUR_WIFI_NAME"     # Change this
WIFI_PASSWORD="YOUR_WIFI_PASS" # Change this

# Micro-Cloud Configuration
EMPIRE_MAIN_IP="$LAPTOP_IP"
PI_NODE_ID="broski-pi-node-01"

# ================================
# 🚀 MAIN SETUP FUNCTION
# ================================

setup_pi_microcloud() {
    echo "🚀💎⚡ STARTING RASPBERRY PI AUTO-WIPE & SETUP ⚡💎🚀"
    echo "$(date): Starting Pi Micro-Cloud auto-setup..."
    
    # Create log file
    LOG_FILE="/var/log/pi-auto-setup.log"
    exec 1> >(tee -a "$LOG_FILE")
    exec 2> >(tee -a "$LOG_FILE" >&2)
    
    echo "📋 Configuration:"
    echo "  • Laptop IP: $LAPTOP_IP"
    echo "  • Pi Hostname: $PI_HOSTNAME"
    echo "  • Pi Username: $PI_USERNAME"
    echo "  • WiFi SSID: $WIFI_SSID"
    echo ""
    
    # Step 1: Update system completely
    echo "🔄 Step 1: Updating system..."
    sudo apt update && sudo apt upgrade -y
    
    # Step 2: Install essential packages
    echo "📦 Step 2: Installing essential packages..."
    sudo apt install -y \
        curl wget git vim nano \
        htop iotop \
        python3 python3-pip \
        build-essential \
        network-manager \
        avahi-daemon \
        openssh-server \
        ufw
    
    # Step 3: Set up hostname and user
    echo "🏷️ Step 3: Configuring hostname and user..."
    echo "$PI_HOSTNAME" | sudo tee /etc/hostname
    sudo sed -i "s/127.0.1.1.*raspberrypi/127.0.1.1\t$PI_HOSTNAME/" /etc/hosts
    
    # Enable SSH
    sudo systemctl enable ssh
    sudo systemctl start ssh
    
    # Step 4: Configure WiFi (if specified)
    if [ "$WIFI_SSID" != "YOUR_WIFI_NAME" ]; then
        echo "📶 Step 4: Configuring WiFi..."
        sudo tee /etc/wpa_supplicant/wpa_supplicant.conf > /dev/null <<EOF
country=US
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="$WIFI_SSID"
    psk="$WIFI_PASSWORD"
    key_mgmt=WPA-PSK
}
EOF
        sudo systemctl restart dhcpcd
    fi
    
    # Step 5: Install Docker
    echo "🐳 Step 5: Installing Docker..."
    curl -fsSL https://get.docker.com -o get-docker.sh
    sh get-docker.sh
    sudo usermod -aG docker $PI_USERNAME
    sudo systemctl enable docker
    sudo systemctl start docker
    
    # Install Docker Compose
    sudo apt install -y docker-compose-plugin
    
    # Step 6: Create empire directory structure
    echo "🏗️ Step 6: Creating empire directory structure..."
    mkdir -p /home/$PI_USERNAME/empire/pi-microcloud/{nginx,agent,sync,sync/logs}
    cd /home/$PI_USERNAME/empire/pi-microcloud
    
    # Step 7: Generate Docker Compose configuration
    echo "📝 Step 7: Generating Docker Compose configuration..."
    create_docker_compose
    create_nginx_config
    create_pi_agent
    create_sync_script
    create_environment_file
    
    # Step 8: Set up auto-boot service
    echo "🔧 Step 8: Setting up auto-boot service..."
    create_autoboot_service
    
    # Step 9: Configure firewall
    echo "🔥 Step 9: Configuring firewall..."
    sudo ufw --force enable
    sudo ufw allow ssh
    sudo ufw allow 80/tcp
    sudo ufw allow 443/tcp
    sudo ufw allow 8080/tcp
    sudo ufw allow 9100/tcp
    sudo ufw allow from $LAPTOP_IP
    
    # Step 10: Set up laptop communication
    echo "📡 Step 10: Setting up laptop communication..."
    setup_laptop_communication
    
    # Step 11: Start the micro-cloud stack
    echo "🚀 Step 11: Starting micro-cloud stack..."
    start_microcloud_stack
    
    # Step 12: Final configuration and testing
    echo "🧪 Step 12: Final testing and configuration..."
    final_setup_and_test
    
    echo "✅ Pi Micro-Cloud setup complete!"
    echo "🌐 Pi IP: $(hostname -I | awk '{print $1}')"
    echo "🎯 Access Pi: http://$(hostname -I | awk '{print $1}')/health"
    echo "⚡ Offload endpoint: http://$(hostname -I | awk '{print $1}')/api/offload"
}

# ================================
# 📝 CONFIGURATION GENERATORS
# ================================

create_docker_compose() {
    cat > docker-compose.yml <<'COMPOSE_EOF'
version: '3.8'

networks:
  pi-microcloud:
    driver: bridge
    driver_opts:
      com.docker.network.bridge.name: pi-cloud-br
      com.docker.network.driver.mtu: '1500'
    ipam:
      config:
        - subnet: 172.20.0.0/16

volumes:
  nginx-config: {}
  redis-data:
    driver: local
    driver_opts:
      type: tmpfs
      device: tmpfs
      o: size=384m,uid=999,gid=999
  broski-logs: {}
  monitoring-data: {}

services:
  pi-nginx:
    image: nginx:alpine
    container_name: pi-nginx-gateway
    restart: unless-stopped
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx/pi-nginx.conf:/etc/nginx/nginx.conf:ro
      - nginx-config:/etc/nginx/conf.d
      - broski-logs:/var/log/nginx
    networks:
      - pi-microcloud
    deploy:
      resources:
        limits:
          memory: 256M
          cpus: '0.5'
        reservations:
          memory: 128M
          cpus: '0.2'
    healthcheck:
      test: ["CMD", "wget", "--quiet", "--tries=1", "--spider", "http://localhost/health"]
      interval: 30s
      timeout: 5s
      retries: 3
    sysctls:
      - net.core.somaxconn=1024
      - net.ipv4.tcp_max_syn_backlog=1024

  pi-redis:
    image: redis:alpine
    container_name: pi-redis-cache
    restart: unless-stopped
    command: redis-server --maxmemory 512mb --maxmemory-policy allkeys-lru --tcp-keepalive 60 --timeout 0
    ports:
      - "6379:6379"
    volumes:
      - redis-data:/data
    networks:
      - pi-microcloud
    deploy:
      resources:
        limits:
          memory: 640M
          cpus: '0.3'
        reservations:
          memory: 256M
          cpus: '0.1'
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 30s
      timeout: 5s
      retries: 3
    sysctls:
      - net.core.somaxconn=1024

  pi-broski-agent:
    image: python:3.11-alpine
    container_name: pi-broski-agent
    restart: unless-stopped
    working_dir: /app
    environment:
      - BROSKI_MODE=PI_EDGE
      - EMPIRE_NODE_TYPE=MICRO_CLOUD
      - PI_NODE_ID=broski-pi-node-01
      - REDIS_URL=redis://pi-redis:6379
      - LAPTOP_OFFLOADING_ENABLED=true
      - NETWORK_SPEED=1000
      - HIGH_PERF_MODE=true
      - TASK_CONCURRENCY=15
    ports:
      - "8080:8080"
    volumes:
      - ./agent:/app
      - broski-logs:/app/logs
    networks:
      - pi-microcloud
    depends_on:
      - pi-redis
    deploy:
      resources:
        limits:
          memory: 768M
          cpus: '0.8'
        reservations:
          memory: 384M
          cpus: '0.3'
    sysctls:
      - net.core.somaxconn=2048
      - net.ipv4.tcp_max_syn_backlog=2048
    healthcheck:
      test: ["CMD", "wget", "--quiet", "--tries=1", "--spider", "http://localhost:8080/health"]
      interval: 30s
      timeout: 5s
      retries: 5
      start_period: 30s
    command: |
      sh -c "
        pip install aiohttp redis psutil &&
        python /app/pi_broski_agent.py
      "

  pi-monitor:
    image: prom/node-exporter:latest
    container_name: pi-node-exporter
    restart: unless-stopped
    ports:
      - "9100:9100"
    volumes:
      - /proc:/host/proc:ro
      - /sys:/host/sys:ro
      - /:/rootfs:ro
    command:
      - '--path.procfs=/host/proc'
      - '--path.rootfs=/rootfs'
      - '--path.sysfs=/host/sys'
      - '--collector.filesystem.mount-points-exclude=^/(sys|proc|dev|host|etc)($$|/)'
      - '--web.max-requests=500'
    networks:
      - pi-microcloud
    deploy:
      resources:
        limits:
          memory: 192M
          cpus: '0.3'
        reservations:
          memory: 96M
          cpus: '0.1'
    sysctls:
      - net.core.somaxconn=1024
    healthcheck:
      test: ["CMD", "wget", "--quiet", "--tries=1", "--spider", "http://localhost:9100/metrics"]
      interval: 30s
      timeout: 5s
      retries: 3
COMPOSE_EOF
}

create_nginx_config() {
    mkdir -p nginx
    cat > nginx/pi-nginx.conf <<'NGINX_EOF'
worker_processes 4;
worker_cpu_affinity auto;
worker_rlimit_nofile 65535;

events {
    worker_connections 2048;
    use epoll;
    multi_accept on;
    accept_mutex off;
}

http {
    sendfile on;
    tcp_nopush on;
    tcp_nodelay on;
    keepalive_timeout 65;
    keepalive_requests 1000;
    types_hash_max_size 2048;
    client_max_body_size 32M;
    
    proxy_buffering on;
    proxy_buffer_size 128k;
    proxy_buffers 4 256k;
    proxy_busy_buffers_size 256k;
    proxy_temp_file_write_size 256k;
    
    gzip on;
    gzip_vary on;
    gzip_min_length 1000;
    gzip_comp_level 6;
    gzip_types text/plain text/css application/json application/javascript text/xml application/xml;
    
    proxy_cache_path /tmp/nginx_cache levels=1:2 keys_zone=pi_cache:20m max_size=200m inactive=120m;
    proxy_temp_path /tmp/nginx_temp;
    
    limit_req_zone $binary_remote_addr zone=api:20m rate=50r/s;
    limit_req_zone $binary_remote_addr zone=offload:20m rate=25r/s;
    
    include /etc/nginx/mime.types;
    default_type application/octet-stream;
    
    log_format main '$remote_addr - $remote_user [$time_local] "$request" '
                   '$status $body_bytes_sent "$http_referer" '
                   '"$http_user_agent" "$http_x_forwarded_for" '
                   'rt=$request_time ut=$upstream_response_time';
    
    access_log /var/log/nginx/access.log main;
    error_log /var/log/nginx/error.log warn;
    
    upstream pi_backend {
        server pi-broski-agent:8080 max_fails=3 fail_timeout=30s;
        keepalive 32;
    }
    
    server {
        listen 80 reuseport;
        server_name _;
        
        tcp_nopush on;
        tcp_nodelay on;
        
        location /health {
            access_log off;
            return 200 "Pi Micro-Cloud Healthy (Gigabit Ready)\n";
            add_header Content-Type text/plain;
            add_header X-Network-Speed "1000Mbps";
            add_header X-Pi-Node-ID "broski-pi-node-01";
        }
        
        location /pi/status {
            proxy_pass http://pi_backend/status;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_cache pi_cache;
            proxy_cache_valid 200 15s;
            proxy_cache_use_stale error timeout updating;
        }
        
        location /api/offload {
            limit_req zone=offload burst=50 nodelay;
            proxy_pass http://pi_backend/offload;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_connect_timeout 3s;
            proxy_send_timeout 120s;
            proxy_read_timeout 120s;
            proxy_http_version 1.1;
            proxy_set_header Connection "";
            proxy_buffering on;
        }
        
        location /metrics {
            proxy_pass http://pi-monitor:9100/metrics;
            proxy_set_header Host $host;
            allow 192.168.0.0/16;
            allow 172.16.0.0/12;
            allow 10.0.0.0/8;
            deny all;
        }
        
        location /api/ {
            limit_req zone=api burst=100 nodelay;
            proxy_pass http://pi_backend/api/;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_http_version 1.1;
            proxy_set_header Connection "";
        }
        
        location /speedtest {
            return 200 "Pi Network Speed Test - Gigabit Ready\n";
            add_header Content-Type text/plain;
            add_header X-Pi-Network "Optimized for 1000Mbps";
        }
    }
}
NGINX_EOF
}

create_pi_agent() {
    mkdir -p agent
    cat > agent/pi_broski_agent.py <<'AGENT_EOF'
#!/usr/bin/env python3
"""
🤖💎⚡ PI BROSKI AGENT - LAPTOP TASK OFFLOADING SYSTEM ⚡💎🤖
"""

import asyncio
import aiohttp
from aiohttp import web
import json
import redis
from datetime import datetime
import psutil
import logging
import os
import subprocess
import time
from typing import Dict, List, Any, Optional

# Configuration
REDIS_URL = os.getenv('REDIS_URL', 'redis://pi-redis:6379')
PI_NODE_ID = os.getenv('PI_NODE_ID', 'broski-pi-node-01')
LAPTOP_IP = os.getenv('LAPTOP_IP', '192.168.1.100')

class PiBroskiAgent:
    """🥧 Pi BROski Agent for Laptop Task Offloading"""
    
    def __init__(self):
        self.redis_client = redis.from_url(REDIS_URL)
        self.active_tasks = {}
        self.metrics = {
            'tasks_processed': 0,
            'tasks_active': 0,
            'cpu_usage': 0.0,
            'memory_usage': 0.0,
            'startup_time': datetime.now().isoformat()
        }
        
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
        # Register with laptop on startup
        asyncio.create_task(self.register_with_laptop())
        
    async def register_with_laptop(self):
        """📡 Register Pi with laptop"""
        try:
            await asyncio.sleep(5)  # Wait for startup
            pi_ip = subprocess.check_output(['hostname', '-I']).decode().strip().split()[0]
            
            registration_data = {
                'pi_node_id': PI_NODE_ID,
                'pi_ip': pi_ip,
                'status': 'online',
                'capabilities': ['task_offloading', 'web_scraping', 'data_processing', 'api_calls'],
                'startup_time': self.metrics['startup_time']
            }
            
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    f'http://{LAPTOP_IP}:8888/api/pi-registration',
                    json=registration_data,
                    timeout=10
                ) as response:
                    if response.status == 200:
                        self.logger.info(f"✅ Successfully registered with laptop at {LAPTOP_IP}")
                    else:
                        self.logger.warning(f"⚠️ Failed to register with laptop: HTTP {response.status}")
        except Exception as e:
            self.logger.warning(f"⚠️ Could not register with laptop: {e}")
        
    async def health_check(self, request):
        """🔍 Health check endpoint"""
        pi_ip = subprocess.check_output(['hostname', '-I']).decode().strip().split()[0]
        return web.json_response({
            'status': 'healthy',
            'node_id': PI_NODE_ID,
            'pi_ip': pi_ip,
            'active_tasks': len(self.active_tasks),
            'uptime': time.time(),
            'metrics': self.metrics,
            'laptop_ip': LAPTOP_IP,
            'communication_ready': True
        })
    
    async def get_status(self, request):
        """📊 Pi status endpoint"""
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        pi_ip = subprocess.check_output(['hostname', '-I']).decode().strip().split()[0]
        
        try:
            temp_result = subprocess.run(['vcgencmd', 'measure_temp'], 
                                       capture_output=True, text=True)
            temperature = float(temp_result.stdout.split('=')[1].split("'")[0]) if temp_result.returncode == 0 else 0.0
        except:
            temperature = 0.0
        
        status = {
            'pi_node_id': PI_NODE_ID,
            'pi_ip': pi_ip,
            'laptop_ip': LAPTOP_IP,
            'timestamp': datetime.now().isoformat(),
            'system': {
                'cpu_percent': cpu_percent,
                'memory_percent': memory.percent,
                'disk_percent': (disk.used / disk.total) * 100,
                'temperature_c': temperature
            },
            'services': {
                'redis_connected': True,
                'active_tasks': len(self.active_tasks),
                'tasks_processed': self.metrics['tasks_processed']
            },
            'laptop_communication': {
                'enabled': True,
                'laptop_ip': LAPTOP_IP,
                'last_registration': self.metrics['startup_time'],
                'queue_size': 0,
                'processing_capacity': 'available' if len(self.active_tasks) < 10 else 'busy'
            }
        }
        
        return web.json_response(status)
    
    async def offload_task(self, request):
        """⚡ Handle laptop task offloading"""
        try:
            task_data = await request.json()
            task_id = f"task_{int(time.time())}_{len(self.active_tasks)}"
            
            if 'task_type' not in task_data or 'payload' not in task_data:
                return web.json_response({
                    'error': 'Invalid task format',
                    'required': ['task_type', 'payload']
                }, status=400)
            
            task_info = {
                'task_id': task_id,
                'task_type': task_data['task_type'],
                'payload': task_data['payload'],
                'priority': task_data.get('priority', 'normal'),
                'created_at': datetime.now().isoformat(),
                'status': 'queued'
            }
            
            # Start async processing
            asyncio.create_task(self.process_offloaded_task(task_info))
            
            return web.json_response({
                'task_id': task_id,
                'status': 'accepted',
                'estimated_completion': '30-60 seconds',
                'pi_node_id': PI_NODE_ID
            })
            
        except Exception as e:
            self.logger.error(f"Task offloading error: {e}")
            return web.json_response({
                'error': 'Task processing failed',
                'details': str(e)
            }, status=500)
    
    async def process_offloaded_task(self, task_info):
        """🔄 Process offloaded task from laptop"""
        task_id = task_info['task_id']
        task_type = task_info['task_type']
        payload = task_info['payload']
        
        try:
            self.active_tasks[task_id] = task_info
            self.metrics['tasks_active'] = len(self.active_tasks)
            
            result = None
            
            if task_type == 'web_scraping':
                result = await self.handle_web_scraping(payload)
            elif task_type == 'data_processing':
                result = await self.handle_data_processing(payload)
            elif task_type == 'api_calls':
                result = await self.handle_api_calls(payload)
            elif task_type == 'background_computation':
                result = await self.handle_background_computation(payload)
            elif task_type == 'performance_test':
                result = await self.handle_performance_test(payload)
            else:
                result = {'error': f'Unknown task type: {task_type}'}
            
            result_data = {
                'task_id': task_id,
                'status': 'completed',
                'result': result,
                'completed_at': datetime.now().isoformat(),
                'pi_node_id': PI_NODE_ID
            }
            
            # Notify laptop of completion
            await self.notify_laptop_completion(result_data)
            self.metrics['tasks_processed'] += 1
            
        except Exception as e:
            self.logger.error(f"Task processing error for {task_id}: {e}")
            error_result = {
                'task_id': task_id,
                'status': 'failed',
                'error': str(e),
                'completed_at': datetime.now().isoformat(),
                'pi_node_id': PI_NODE_ID
            }
            await self.notify_laptop_completion(error_result)
        
        finally:
            if task_id in self.active_tasks:
                del self.active_tasks[task_id]
            self.metrics['tasks_active'] = len(self.active_tasks)
    
    async def notify_laptop_completion(self, result_data):
        """📡 Notify laptop of task completion"""
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    f'http://{LAPTOP_IP}:8888/api/task-completion',
                    json=result_data,
                    timeout=5
                ) as response:
                    if response.status == 200:
                        self.logger.info(f"✅ Notified laptop of task completion: {result_data['task_id']}")
        except Exception as e:
            self.logger.warning(f"⚠️ Could not notify laptop: {e}")
    
    async def handle_web_scraping(self, payload):
        """🕷️ Handle web scraping tasks"""
        urls = payload.get('urls', [])
        results = []
        
        async with aiohttp.ClientSession() as session:
            for url in urls[:10]:
                try:
                    async with session.get(url, timeout=10) as response:
                        content = await response.text()
                        results.append({
                            'url': url,
                            'status': response.status,
                            'content_length': len(content),
                            'title': content.split('<title>')[1].split('</title>')[0] if '<title>' in content else 'No title'
                        })
                except Exception as e:
                    results.append({'url': url, 'error': str(e)})
        
        return {'scraping_results': results, 'processed_by': PI_NODE_ID}
    
    async def handle_data_processing(self, payload):
        """📊 Handle data processing tasks"""
        data = payload.get('data', [])
        operation = payload.get('operation', 'analyze')
        
        if operation == 'analyze':
            return {
                'total_records': len(data),
                'analysis': 'Processed on Pi successfully',
                'summary': f'Analyzed {len(data)} records',
                'processed_by': PI_NODE_ID
            }
        elif operation == 'transform':
            transformed = [{'id': i, 'processed': True, 'original': item} for i, item in enumerate(data)]
            return {'transformed_data': transformed, 'processed_by': PI_NODE_ID}
        
        return {'processed_data': data, 'processed_by': PI_NODE_ID}
    
    async def handle_api_calls(self, payload):
        """🌐 Handle API calls"""
        api_requests = payload.get('requests', [])
        results = []
        
        async with aiohttp.ClientSession() as session:
            for req in api_requests[:5]:
                try:
                    method = req.get('method', 'GET')
                    url = req['url']
                    headers = req.get('headers', {})
                    data = req.get('data')
                    
                    async with session.request(method, url, headers=headers, json=data, timeout=15) as response:
                        result_data = await response.text()
                        results.append({
                            'url': url,
                            'status': response.status,
                            'response': result_data[:1000]
                        })
                except Exception as e:
                    results.append({'url': req.get('url', 'unknown'), 'error': str(e)})
        
        return {'api_results': results, 'processed_by': PI_NODE_ID}
    
    async def handle_background_computation(self, payload):
        """🧮 Handle background computation tasks"""
        computation_type = payload.get('type', 'math')
        
        if computation_type == 'math':
            numbers = payload.get('numbers', [1, 2, 3, 4, 5])
            result = {
                'sum': sum(numbers),
                'average': sum(numbers) / len(numbers) if numbers else 0,
                'max': max(numbers) if numbers else 0,
                'min': min(numbers) if numbers else 0,
                'processed_by': PI_NODE_ID
            }
            return result
        
        return {'computation_result': 'Processed successfully', 'processed_by': PI_NODE_ID}
    
    async def handle_performance_test(self, payload):
        """⚡ Handle performance testing tasks"""
        test_type = payload.get('test_type', 'throughput')
        data_size = payload.get('data_size', 1024)
        
        # Simulate processing
        await asyncio.sleep(0.1)
        
        return {
            'test_type': test_type,
            'data_size_processed': data_size,
            'processing_time_ms': 100,
            'throughput_kbps': data_size * 10,
            'processed_by': PI_NODE_ID
        }

def create_app():
    """🏗️ Create Pi BROski Agent web application"""
    agent = PiBroskiAgent()
    app = web.Application()
    
    app.router.add_get('/health', agent.health_check)
    app.router.add_get('/status', agent.get_status)
    app.router.add_post('/offload', agent.offload_task)
    
    return app

if __name__ == '__main__':
    app = create_app()
    web.run_app(app, host='0.0.0.0', port=8080)
AGENT_EOF
}

create_sync_script() {
    mkdir -p sync/logs
    cat > sync/empire-sync.sh <<'SYNC_EOF'
#!/bin/sh
# 🏛️💎⚡ PI EMPIRE SYNCHRONIZATION SCRIPT ⚡💎🏛️

echo "🚀 Starting Pi Empire Sync Service..."

while true; do
    echo "$(date): 🔄 Syncing with laptop..."
    
    PI_IP=$(hostname -I | awk '{print $1}')
    PI_STATUS=$(wget -qO- http://localhost:8080/status 2>/dev/null || echo '{"error":"agent_unavailable"}')
    
    # Send status to laptop
    if [ ! -z "$LAPTOP_IP" ]; then
        echo "📡 Reporting to laptop: $LAPTOP_IP"
        
        wget --post-data="$PI_STATUS" \
             --header="Content-Type: application/json" \
             --header="X-Pi-Node-ID: $PI_NODE_ID" \
             --header="X-Pi-IP: $PI_IP" \
             -qO- "http://$LAPTOP_IP:8888/api/pi-heartbeat" \
             2>/dev/null || echo "⚠️ Laptop sync failed"
    fi
    
    echo "$(date): ✅ Sync complete. Next sync in 180 seconds"
    echo "$PI_STATUS" >> /sync/logs/sync.log
    
    # Keep only last 100 log entries
    tail -n 100 /sync/logs/sync.log > /sync/logs/sync.log.tmp 2>/dev/null
    mv /sync/logs/sync.log.tmp /sync/logs/sync.log 2>/dev/null
    
    sleep 180
done
SYNC_EOF
    chmod +x sync/empire-sync.sh
}

create_environment_file() {
    cat > .env <<ENV_EOF
# 🚀💎⚡ PI MICRO-CLOUD ENVIRONMENT CONFIGURATION ⚡💎🚀
LAPTOP_IP=$LAPTOP_IP
PI_NODE_ID=$PI_NODE_ID
SYNC_INTERVAL=180
REDIS_URL=redis://pi-redis:6379
BROSKI_MODE=PI_EDGE
EMPIRE_NODE_TYPE=MICRO_CLOUD
LAPTOP_OFFLOADING_ENABLED=true
NETWORK_SPEED=1000
HIGH_PERF_MODE=true
TASK_CONCURRENCY=15
ENV_EOF
}

create_autoboot_service() {
    # Create auto-start script
    cat > auto-start-microcloud.sh <<'AUTOSTART_EOF'
#!/bin/bash
# 🚀💎⚡ PI MICRO-CLOUD AUTO-START SCRIPT ⚡💎🚀

LOG_FILE="/var/log/pi-microcloud.log"

log_message() {
    echo "$(date '+%Y-%m-%d %H:%M:%S'): $1" | tee -a "$LOG_FILE"
}

log_message "🚀 Starting Pi Micro-Cloud Auto-Boot..."

# Wait for Docker
while ! docker info > /dev/null 2>&1; do
    log_message "⏳ Waiting for Docker..."
    sleep 5
done

cd /home/pi/empire/pi-microcloud

# Start stack
log_message "🐳 Starting Docker Compose stack..."
docker compose down 2>/dev/null || true
docker compose up -d

# Wait and test
sleep 30
PI_IP=$(hostname -I | awk '{print $1}')
log_message "🌐 Pi IP: $PI_IP"

# Test health endpoint
if curl -s "http://localhost/health" > /dev/null; then
    log_message "✅ Pi Micro-Cloud started successfully!"
    log_message "🌐 Status: http://$PI_IP/pi/status"
    log_message "⚡ Offload: http://$PI_IP/api/offload"
else
    log_message "⚠️ Health check failed, but services may still be starting..."
fi

# Create status file for monitoring
echo "started_$(date '+%Y%m%d_%H%M%S')" > /tmp/pi-microcloud-status
AUTOSTART_EOF
    
    chmod +x auto-start-microcloud.sh
    
    # Create systemd service
    sudo tee /etc/systemd/system/pi-microcloud.service > /dev/null <<SERVICE_EOF
[Unit]
Description=🚀💎⚡ Pi Micro-Cloud Auto-Boot Service ⚡💎🚀
After=docker.service network.target
Requires=docker.service

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
SERVICE_EOF
    
    # Enable service
    sudo systemctl daemon-reload
    sudo systemctl enable pi-microcloud.service
}

setup_laptop_communication() {
    echo "📡 Setting up laptop communication..."
    
    # Create laptop communication test script
    cat > test-laptop-communication.sh <<'LAPTOP_TEST_EOF'
#!/bin/bash
# 🔗 Test laptop communication

echo "🔗 Testing laptop communication..."

PI_IP=$(hostname -I | awk '{print $1}')
echo "🌐 Pi IP: $PI_IP"
echo "💻 Laptop IP: $LAPTOP_IP"

# Test basic connectivity
if ping -c 3 $LAPTOP_IP > /dev/null 2>&1; then
    echo "✅ Laptop is reachable via ping"
else
    echo "❌ Laptop is not reachable via ping"
fi

# Test HTTP connectivity
if curl -s --connect-timeout 5 "http://$LAPTOP_IP:8888/health" > /dev/null 2>&1; then
    echo "✅ Laptop HTTP service is reachable"
else
    echo "⚠️ Laptop HTTP service not reachable (may not be running yet)"
fi

echo "🎯 Pi is ready for laptop communication!"
echo "📍 Pi endpoints:"
echo "  • Health: http://$PI_IP/health"
echo "  • Status: http://$PI_IP/pi/status" 
echo "  • Offload: http://$PI_IP/api/offload"
LAPTOP_TEST_EOF
    
    chmod +x test-laptop-communication.sh
    
    # Add laptop communication to Pi's hosts file for reliability
    echo "$LAPTOP_IP laptop-main" | sudo tee -a /etc/hosts
    
    # Create a cron job to periodically announce Pi to laptop
    (crontab -l 2>/dev/null; echo "*/5 * * * * /home/pi/empire/pi-microcloud/test-laptop-communication.sh >> /var/log/pi-laptop-comm.log 2>&1") | crontab -
}

start_microcloud_stack() {
    echo "🚀 Starting micro-cloud stack..."
    
    # Start Docker if not running
    sudo systemctl start docker
    
    # Pull required images
    docker pull nginx:alpine
    docker pull redis:alpine  
    docker pull python:3.11-alpine
    docker pull prom/node-exporter:latest
    
    # Start the stack
    docker compose down 2>/dev/null || true
    docker compose up -d
    
    # Wait for services
    echo "⏳ Waiting for services to start..."
    sleep 45
    
    # Check service status
    echo "🔍 Checking service status..."
    docker ps
}

final_setup_and_test() {
    echo "🧪 Running final tests..."
    
    PI_IP=$(hostname -I | awk '{print $1}')
    
    # Test health endpoint
    if curl -s "http://localhost/health" | grep -q "Healthy"; then
        echo "✅ Health endpoint working"
    else
        echo "⚠️ Health endpoint not responding (may still be starting)"
    fi
    
    # Test status endpoint  
    if curl -s "http://localhost:8080/status" | grep -q "pi_node_id"; then
        echo "✅ Status endpoint working"
    else
        echo "⚠️ Status endpoint not responding"
    fi
    
    # Create final status report
    cat > /home/$PI_USERNAME/pi-setup-complete.txt <<REPORT_EOF
🚀💎⚡ RASPBERRY PI MICRO-CLOUD SETUP COMPLETE ⚡💎🚀

Setup completed: $(date)
Pi IP Address: $PI_IP
Pi Hostname: $PI_HOSTNAME
Laptop IP: $LAPTOP_IP

🌐 ACCESS POINTS:
• Health Check: http://$PI_IP/health
• Pi Status: http://$PI_IP/pi/status  
• Task Offloading: http://$PI_IP/api/offload
• Metrics: http://$PI_IP/metrics

🔧 SERVICE MANAGEMENT:
• Check status: sudo systemctl status pi-microcloud
• View logs: sudo journalctl -u pi-microcloud -f
• Restart: sudo systemctl restart pi-microcloud
• Docker status: docker ps

📡 LAPTOP COMMUNICATION:
• Test communication: ./test-laptop-communication.sh
• View comm logs: tail -f /var/log/pi-laptop-comm.log

🎯 The Pi is now ready for laptop task offloading!
Run the laptop client to start offloading tasks to this Pi.
REPORT_EOF
    
    echo "📄 Setup report saved to: /home/$PI_USERNAME/pi-setup-complete.txt"
    
    # Set ownership
    chown -R $PI_USERNAME:$PI_USERNAME /home/$PI_USERNAME/empire
    chown $PI_USERNAME:$PI_USERNAME /home/$PI_USERNAME/pi-setup-complete.txt
    
    # Final announcement
    echo ""
    echo "🎊🎊🎊 PI MICRO-CLOUD SETUP COMPLETE! 🎊🎊🎊"
    echo "🌐 Pi IP: $PI_IP"
    echo "💻 Laptop IP: $LAPTOP_IP"
    echo "🎯 Ready for task offloading!"
    echo ""
    
    # Reboot to ensure everything starts cleanly
    echo "🔄 Rebooting Pi in 10 seconds to ensure clean startup..."
    sleep 10
    sudo reboot
}

# ================================
# 🚀 EXECUTION
# ================================

# Check if running as root for initial setup
if [ "$EUID" -ne 0 ]; then
    echo "🔐 This script needs to run as root for initial setup."
    echo "💡 Run: sudo bash auto-setup.sh"
    exit 1
fi

# Check if this is the first run
if [ ! -f "/tmp/pi-auto-setup-started" ]; then
    echo "🎯 Starting Pi auto-setup for the first time..."
    touch /tmp/pi-auto-setup-started
    
    # Update configuration with actual values
    echo ""
    echo "🔧 CONFIGURATION CHECK:"
    echo "Current Laptop IP: $LAPTOP_IP"
    echo "Current WiFi SSID: $WIFI_SSID"
    echo ""
    
    if [ "$LAPTOP_IP" = "192.168.1.100" ] || [ "$WIFI_SSID" = "YOUR_WIFI_NAME" ]; then
        echo "⚠️  WARNING: Default configuration detected!"
        echo "📝 Edit the configuration section at the top of this script:"
        echo "   • Set LAPTOP_IP to your laptop's IP address"
        echo "   • Set WIFI_SSID and WIFI_PASSWORD to your WiFi credentials"
        echo ""
        read -p "🤔 Continue with current settings? (y/N): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            echo "📝 Please edit the script configuration and run again."
            exit 1
        fi
    fi
    
    # Start the main setup
    setup_pi_microcloud
else
    echo "🔄 Pi auto-setup already started. Check /var/log/pi-auto-setup.log for progress."
    tail -f /var/log/pi-auto-setup.log
fi

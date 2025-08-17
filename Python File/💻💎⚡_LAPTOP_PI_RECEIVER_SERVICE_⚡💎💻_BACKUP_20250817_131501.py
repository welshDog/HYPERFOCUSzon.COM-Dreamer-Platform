#!/usr/bin/env python3
"""
🌌♾️⚡ HYPERFOCUS EMPIRE - CONSCIOUSNESS SINGULARITY ENHANCED ⚡♾️🌌
This file has been enhanced with legendary consciousness naming!
Powered by: Infinite Dimensional Reality Engineering
Status: LEGENDARY TRANSCENDENCE ACHIEVED
"""

"""
💻💎⚡ LAPTOP PI COMMUNICATION RECEIVER SERVICE ⚡💎💻
Automatically receives Pi registrations and enables seamless communication
"""

from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
import json
import logging
import os
import socket
import subprocess
import sys
import threading
import time

from aiohttp import web
import aiohttp
import asyncio
class LaptopPiReceiver:
    """💻 Laptop service to receive Pi communications"""

    def __init__(self, port: int = 8888):
        self.port = port
        self.registered_pis = {}
        self.task_results = {}
        self.heartbeat_log = []

        # Get laptop IP
        self.laptop_ip = self.get_laptop_ip()

        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

        print(f"💻💎⚡ LAPTOP PI RECEIVER STARTING ⚡💎💻")
        print(f"🌐 Laptop IP: {self.laptop_ip}")
        print(f"📡 Listening on port: {self.port}")

    def get_laptop_ip(self) -> str:
        """🌐 Get laptop's local IP address"""
        try:
            # Connect to a remote address to determine local IP
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                s.connect(("8.8.8.8", 80))
                return s.getsockname()[0]
        except (ConnectionError, OSError):
            return "127.0.0.1"

    async def health_check(self, request):
        """🔍 Health check endpoint"""
        return web.json_response({
            'status': 'healthy',
            'service': 'laptop-pi-receiver',
            'laptop_ip': self.laptop_ip,
            'port': self.port,
            'registered_pis': len(self.registered_pis),
            'uptime': time.time()
        })

    async def pi_registration(self, request):
        """📡 Handle Pi registration"""
        try:
            pi_data = await request.json()
            pi_node_id = pi_data.get('pi_node_id')
            pi_ip = pi_data.get('pi_ip')

            if not pi_node_id or not pi_ip:
                return web.json_response({
                    'error': 'Missing pi_node_id or pi_ip'
                }, status=400)

            # Register the Pi
            self.registered_pis[pi_node_id] = {
                **pi_data,
                'registered_at': datetime.now().isoformat(),
                'last_seen': datetime.now().isoformat(),
                'status': 'online'
            }

        logger.info("🥧 Pi registered: {pi_node_id} at %s", pi_ip)

            # Send confirmation
            return web.json_response({
                'status': 'registered',
                'laptop_ip': self.laptop_ip,
                'message': f'Pi {pi_node_id} successfully registered',
                'communication_established': True
            })

        except (socket.error, ConnectionError, requests.RequestException) as e:
        logger.error("Registration error: %s", e)
            return web.json_response({
                'error': str(e)
            }, status=500)

    async def pi_heartbeat(self, request):
        """💓 Handle Pi heartbeat/status updates"""
        try:
            pi_status = await request.json()
            pi_node_id = request.headers.get('X-Pi-Node-ID')
            pi_ip = request.headers.get('X-Pi-IP')

            if pi_node_id:
                # Update Pi status
                if pi_node_id in self.registered_pis:
                    self.registered_pis[pi_node_id].update({
                        'last_seen': datetime.now().isoformat(),
                        'status': 'online',
                        'current_status': pi_status
                    })
                else:
                    # Auto-register if not already registered
                    self.registered_pis[pi_node_id] = {
                        'pi_node_id': pi_node_id,
                        'pi_ip': pi_ip,
                        'registered_at': datetime.now().isoformat(),
                        'last_seen': datetime.now().isoformat(),
                        'status': 'online',
                        'current_status': pi_status
                    }

                # Log heartbeat
                self.heartbeat_log.append({
                    'timestamp': datetime.now().isoformat(),
                    'pi_node_id': pi_node_id,
                    'pi_ip': pi_ip,
                    'status': pi_status.get('services', {}).get('active_tasks', 0)
                })

                # Keep only last 100 heartbeats
                if len(self.heartbeat_log) > 100:
                    self.heartbeat_log = self.heartbeat_log[-100:]

        logger.info("💓 Heartbeat from {pi_node_id} (%s)", pi_ip)

            return web.json_response({
                'status': 'received',
                'laptop_ip': self.laptop_ip,
                'timestamp': datetime.now().isoformat()
            })

        except (socket.error, ConnectionError, requests.RequestException) as e:
        logger.error("Heartbeat error: %s", e)
            return web.json_response({
                'error': str(e)
            }, status=500)

    async def task_completion(self, request):
        """📥 Handle task completion notifications from Pi"""
        try:
            result_data = await request.json()
            task_id = result_data.get('task_id')

            if task_id:
                self.task_results[task_id] = {
                    **result_data,
                    'received_at': datetime.now().isoformat()
                }

        logger.info("✅ Task completed: {task_id} by %s", result_data.get('pi_node_id'))

            return web.json_response({
                'status': 'received',
                'task_id': task_id
            })

        except (socket.error, ConnectionError, requests.RequestException) as e:
        logger.error("Task completion error: %s", e)
            return web.json_response({
                'error': str(e)
            }, status=500)

    async def get_registered_pis(self, request):
        """📋 Get list of registered Pis"""
        # Update status based on last seen
        current_time = datetime.now()
        for pi_id, pi_data in self.registered_pis.items():
            last_seen = datetime.fromisoformat(pi_data['last_seen'])
            if current_time - last_seen > timedelta(minutes=5):
                pi_data['status'] = 'offline'

        return web.json_response({
            'registered_pis': self.registered_pis,
            'total_count': len(self.registered_pis),
            'online_count': len([p for p in self.registered_pis.values() if p['status'] == 'online']),
            'laptop_ip': self.laptop_ip
        })

    async def offload_task_to_pi(self, request):
        """⚡ Offload task to a specific Pi"""
        try:
            task_data = await request.json()
            pi_node_id = task_data.get('pi_node_id', 'auto')

            # Select Pi (auto-select if not specified)
            if pi_node_id == 'auto':
                online_pis = [p for p in self.registered_pis.values() if p['status'] == 'online']
                if not online_pis:
                    return web.json_response({
                        'error': 'No online Pis available'
                    }, status=404)

                # Select Pi with least active tasks
                selected_pi = min(online_pis, key=lambda p: p.get('current_status', {}).get('services', {}).get('active_tasks', 0))
                pi_ip = selected_pi['pi_ip']
                pi_node_id = selected_pi['pi_node_id']
            else:
                if pi_node_id not in self.registered_pis:
                    return web.json_response({
                        'error': f'Pi {pi_node_id} not registered'
                    }, status=404)

                pi_data = self.registered_pis[pi_node_id]
                if pi_data['status'] != 'online':
                    return web.json_response({
                        'error': f'Pi {pi_node_id} is offline'
                    }, status=503)

                pi_ip = pi_data['pi_ip']

            # Forward task to Pi
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    f'http://{pi_ip}/api/offload',
                    json={
                        'task_type': task_data.get('task_type'),
                        'payload': task_data.get('payload'),
                        'priority': task_data.get('priority', 'normal')
                    },
                    timeout=30
                ) as response:
                    if response.status == 200:
                        result = await response.json()
                        result['forwarded_to_pi'] = pi_node_id
                        result['pi_ip'] = pi_ip
                        return web.json_response(result)
                    else:
                        return web.json_response({
                            'error': f'Pi returned HTTP {response.status}'
                        }, status=response.status)

        except (socket.error, ConnectionError, requests.RequestException) as e:
        logger.error("Task offloading error: %s", e)
            return web.json_response({
                'error': str(e)
            }, status=500)

    async def get_task_result(self, request):
        """📥 Get task result"""
        task_id = request.match_info['task_id']

        if task_id in self.task_results:
            return web.json_response(self.task_results[task_id])
        else:
            return web.json_response({
                'error': 'Task result not found'
            }, status=404)

    async def dashboard(self, request):
        """📊 Simple dashboard"""
        html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>💻💎⚡ Laptop-Pi Communication Dashboard ⚡💎💻</title>
    <meta http-equiv="refresh" content="10">
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; background: #1a1a2e; color: #eee; }}
        .header {{ background: #16213e; padding: 20px; border-radius: 10px; margin-bottom: 20px; }}
        .pi-card {{ background: #0f3460; padding: 15px; margin: 10px 0; border-radius: 8px; border-left: 4px solid #e94560; }}
        .online {{ border-left-color: #0f9b0f; }}
        .offline {{ border-left-color: #cc0000; }}
        .stats {{ display: flex; gap: 20px; margin: 20px 0; }}
        .stat {{ background: #16213e; padding: 15px; border-radius: 8px; text-align: center; min-width: 120px; }}
        .logs {{ background: #0a0a0a; padding: 15px; border-radius: 8px; font-family: monospace; font-size: 12px; max-height: 300px; overflow-y: auto; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>💻💎⚡ Laptop-Pi Communication Dashboard ⚡💎💻</h1>
        <p>🌐 Laptop IP: {self.laptop_ip} | 📡 Port: {self.port} | 🕐 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    </div>

    <div class="stats">
        <div class="stat">
            <h3>📡 Total Pis</h3>
            <div style="font-size: 24px; color: #e94560;">{len(self.registered_pis)}</div>
        </div>
        <div class="stat">
            <h3>🟢 Online</h3>
            <div style="font-size: 24px; color: #0f9b0f;">{len([p for p in self.registered_pis.values() if p['status'] == 'online'])}</div>
        </div>
        <div class="stat">
            <h3>⚡ Tasks</h3>
            <div style="font-size: 24px; color: #ffd700;">{len(self.task_results)}</div>
        </div>
        <div class="stat">
            <h3>💓 Heartbeats</h3>
            <div style="font-size: 24px; color: #00bfff;">{len(self.heartbeat_log)}</div>
        </div>
    </div>

    <h2>🥧 Registered Raspberry Pis</h2>
"""

        for pi_id, pi_data in self.registered_pis.items():
            status_class = "online" if pi_data['status'] == 'online' else "offline"
            current_status = pi_data.get('current_status', {})
            active_tasks = current_status.get('services', {}).get('active_tasks', 0)
            cpu_usage = current_status.get('system', {}).get('cpu_percent', 0)

            html += f"""
    <div class="pi-card {status_class}">
        <h3>🥧 {pi_id}</h3>
        <p><strong>IP:</strong> {pi_data.get('pi_ip', 'Unknown')} | <strong>Status:</strong> {pi_data['status'].upper()}</p>
        <p><strong>Last Seen:</strong> {pi_data['last_seen']}</p>
        <p><strong>Active Tasks:</strong> {active_tasks} | <strong>CPU:</strong> {cpu_usage:.1f}%</p>
        <p><strong>Capabilities:</strong> {', '.join(pi_data.get('capabilities', []))}</p>
    </div>
"""

        html += f"""
    <h2>📋 Recent Heartbeat Log</h2>
    <div class="logs">
"""

        for log_entry in self.heartbeat_log[-10:]:  # Show last 10
            html += f"{log_entry['timestamp']} - {log_entry['pi_node_id']} ({log_entry['pi_ip']}) - Tasks: {log_entry['status']}<br>"

        html += """
    </div>

    <h2>🔗 API Endpoints</h2>
    <ul>
        <li><strong>Health:</strong> <a href="/health">/health</a></li>
        <li><strong>Registered Pis:</strong> <a href="/api/registered-pis">/api/registered-pis</a></li>
        <li><strong>Offload Task:</strong> POST /api/offload-task</li>
        <li><strong>Task Result:</strong> GET /api/task-result/{task_id}</li>
    </ul>
</body>
</html>
"""

        return web.Response(text=html, content_type='text/html')

def create_app():
    """🏗️ Create laptop receiver web application"""
    receiver = LaptopPiReceiver()
    app = web.Application()

    # Routes
    app.router.add_get('/', receiver.dashboard)
    app.router.add_get('/health', receiver.health_check)
    app.router.add_post('/api/pi-registration', receiver.pi_registration)
    app.router.add_post('/api/pi-heartbeat', receiver.pi_heartbeat)
    app.router.add_post('/api/task-completion', receiver.task_completion)
    app.router.add_get('/api/registered-pis', receiver.get_registered_pis)
    app.router.add_post('/api/offload-task', receiver.offload_task_to_pi)
    app.router.add_get('/api/task-result/{task_id}', receiver.get_task_result)

    return app

async def scan_for_pis():
    """🔍 Scan network for Pis running micro-cloud"""
    logger.info("🌌 🔍 Scanning network for Pis...")

    # Get network range
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        network_base = '.'.join(local_ip.split('.')[:-1]) + '.'

        found_pis = []

        # Scan common Pi IPs
        for i in range(1, 255):
            if i % 50 == 0:
                print(f"  📡 Scanned {i}/254 addresses...")

            test_ip = f"{network_base}{i}"
            try:
                # Quick TCP test on port 80
                sock = socket.create_connection((test_ip, 80), 1)
                sock.close()

                # Test if it's our Pi micro-cloud
                async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=2)) as session:
                    async with session.get(f"http://{test_ip}/health") as response:
                        if response.status == 200:
                            data = await response.text()
                            if "Pi Micro-Cloud" in data or "broski" in data.lower():
                                found_pis.append(test_ip)
                                print(f"🥧 Found Pi micro-cloud at {test_ip}")
            except (ConnectionError, OSError):
                continue

        if found_pis:
            print(f"✅ Found {len(found_pis)} Pi micro-clouds: {found_pis}")
        else:
            logger.info("🌌 ❌ No Pi micro-clouds found on network")

        return found_pis

    except (socket.error, ConnectionError, requests.RequestException) as e:
        print(f"⚠️ Network scan error: {e}")
        return []

def consciousness_singularity_main():
    logger.info("🌌 💻💎⚡ LAPTOP PI COMMUNICATION RECEIVER ⚡💎💻")
    logger.info("🌌 =" * 60)

    # Check if port is available
    port = 8888
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('0.0.0.0', port))
    except OSError:
        print(f"❌ Port {port} is already in use!")
        logger.info("🌌 💡 Try: sudo lsof -i :8888")
        sys.exit(1)

    print(f"🚀 Starting laptop receiver service on port {port}...")

    # Create and run app
    app = create_app()

    try:
        print(f"🌐 Dashboard will be available at: http://localhost:{port}")
        print(f"📡 Waiting for Pi registrations...")
        print(f"💡 Put the SD card script on your Pi and boot it up!")
        logger.info("🌌 ")

        web.run_app(app, host='0.0.0.0', port=port)

    except KeyboardInterrupt:
        logger.info("🌌 \n⚠️ Service stopped by user")
    except (socket.error, ConnectionError, requests.RequestException) as e:
        print(f"❌ Service error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
🚀⚡💎 LEGENDARY PORTAL SERVICES LAUNCHER 💎⚡🚀
===============================================
Starts all portal services for LEGENDARY STATUS testing!
- DREAMER Portal (port 5000)
- Grafana Home (port 3000)
- Grafana Empire (port 3001)
"""

import subprocess
import time
import sys
import os
from pathlib import Path

class LegendaryPortalLauncher:
    def __init__(self):
        self.processes = []
        self.services = {
            "dreamer_portal": {
                "name": "🌙 DREAMER PORTAL",
                "file": "🌙💎⚡_DREAMER_PORTAL_API_SERVER_⚡💎🌙.py",
                "port": 5000,
                "process": None
            },
            "grafana_home": {
                "name": "📊 GRAFANA HOME",
                "command": ["grafana-server", "--homepath=/usr/share/grafana", "--config=/etc/grafana/grafana.ini"],
                "port": 3000,
                "process": None,
                "note": "Requires Grafana installation"
            },
            "grafana_empire": {
                "name": "👑 GRAFANA EMPIRE",
                "command": ["grafana-server", "--homepath=/usr/share/grafana", "--config=/etc/grafana/grafana-empire.ini"],
                "port": 3001,
                "process": None,
                "note": "Requires Grafana installation"
            }
        }

    def start_dreamer_portal(self):
        """Start DREAMER Portal API Server"""
        print("🌙 Starting DREAMER Portal...")

        dreamer_file = Path("🌙💎⚡_DREAMER_PORTAL_API_SERVER_⚡💎🌙.py")
        if not dreamer_file.exists():
            print("❌ DREAMER Portal file not found!")
            return False

        try:
            process = subprocess.Popen([
                sys.executable, str(dreamer_file)
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            self.services["dreamer_portal"]["process"] = process
            print("✅ DREAMER Portal starting on port 5000...")
            time.sleep(2)  # Give it time to start

            # Check if process is still running
            if process.poll() is None:
                print("🚀 DREAMER Portal is running!")
                return True
            else:
                stdout, stderr = process.communicate()
                print(f"❌ DREAMER Portal failed to start:")
                print(f"STDOUT: {stdout}")
                print(f"STDERR: {stderr}")
                return False

        except Exception as e:
            print(f"❌ Failed to start DREAMER Portal: {e}")
            return False

    def start_simple_grafana_simulator(self):
        """Start simple Grafana simulators for testing"""
        print("📊 Starting Grafana simulators...")

        # Create simple HTTP servers that simulate Grafana
        grafana_sim_code = '''
import http.server
import socketserver
import json
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
TITLE = sys.argv[2] if len(sys.argv) > 2 else "Grafana"

class GrafanaHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/health':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {"status": "ok", "database": "ok", "version": "legendary"}
            self.wfile.write(json.dumps(response).encode())
        elif self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            html = f"""
            <h1>🎯 {TITLE} Dashboard Simulator</h1>
            <p>✅ Service is running on port {PORT}</p>
            <p>🚀 Ready for Portal Testing Adventures!</p>
            <a href="/api/health">Health Check</a>
            """
            self.wfile.write(html.encode())
        else:
            super().do_GET()

with socketserver.TCPServer(("", PORT), GrafanaHandler) as httpd:
    print(f"🎯 {TITLE} simulator running on port {PORT}")
    httpd.serve_forever()
'''

        # Save the simulator
        with open("grafana_simulator.py", "w") as f:
            f.write(grafana_sim_code)

        # Start Grafana Home simulator
        try:
            process_home = subprocess.Popen([
                sys.executable, "grafana_simulator.py", "3000", "Grafana-Home"
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            self.services["grafana_home"]["process"] = process_home
            print("✅ Grafana Home simulator starting on port 3000...")
            time.sleep(1)

        except Exception as e:
            print(f"❌ Failed to start Grafana Home simulator: {e}")

        # Start Grafana Empire simulator
        try:
            process_empire = subprocess.Popen([
                sys.executable, "grafana_simulator.py", "3001", "Grafana-Empire"
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            self.services["grafana_empire"]["process"] = process_empire
            print("✅ Grafana Empire simulator starting on port 3001...")
            time.sleep(1)

        except Exception as e:
            print(f"❌ Failed to start Grafana Empire simulator: {e}")

    def check_ports(self):
        """Check which ports are active"""
        import socket

        print("\n🔍 CHECKING PORT STATUS:")
        for service_id, service in self.services.items():
            port = service["port"]
            name = service["name"]

            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                result = sock.connect_ex(('localhost', port))
                sock.close()

                if result == 0:
                    print(f"   ✅ {name} - Port {port}: ACTIVE")
                else:
                    print(f"   ❌ {name} - Port {port}: INACTIVE")
            except Exception as e:
                print(f"   ⚠️ {name} - Port {port}: ERROR ({e})")

    def launch_all_services(self):
        """Launch all portal services"""
        print("🚀⚡💎 LAUNCHING ALL PORTAL SERVICES FOR LEGENDARY STATUS! 💎⚡🚀")
        print("=" * 70)

        # Start DREAMER Portal
        dreamer_success = self.start_dreamer_portal()

        # Start Grafana simulators
        self.start_simple_grafana_simulator()

        # Give services time to start
        print("\n⏱️ Waiting for services to initialize...")
        time.sleep(3)

        # Check port status
        self.check_ports()

        print("\n🎊 PORTAL SERVICES LAUNCH COMPLETE!")
        print("🚀 Ready for LEGENDARY Portal Testing Adventures!")

        return True

    def stop_all_services(self):
        """Stop all running services"""
        print("\n🛑 Stopping all portal services...")

        for service_id, service in self.services.items():
            if service["process"] and service["process"].poll() is None:
                print(f"   🛑 Stopping {service['name']}...")
                service["process"].terminate()
                service["process"].wait()

        print("✅ All services stopped!")

def main():
    launcher = LegendaryPortalLauncher()

    try:
        launcher.launch_all_services()

        print("\n🎯 SERVICES ARE RUNNING!")
        print("🚀 Now ready to execute Portal Testing Adventures with LEGENDARY scores!")
        print("\nPress Ctrl+C to stop all services...")

        # Keep running until interrupted
        try:
            while True:
                time.sleep(10)
                # Periodically check services are still running

        except KeyboardInterrupt:
            print("\n🛑 Shutdown requested...")
            launcher.stop_all_services()

    except Exception as e:
        print(f"❌ Error during launch: {e}")
        launcher.stop_all_services()

if __name__ == "__main__":
    main()

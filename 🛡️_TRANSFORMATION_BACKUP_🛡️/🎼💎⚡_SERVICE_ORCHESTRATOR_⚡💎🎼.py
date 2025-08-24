import os
import signal
import subprocess
import time
from pathlib import Path
from typing import Dict


class HyperFocusServiceOrchestrator:
    """🎼 Service orchestrator for all HyperFocus Zone web applications"""

    def __init__(self):
        self.workspace = Path("h:/")
        self.python_exe = self.workspace / ".venv" / "Scripts" / "python.exe"
        self.services = {
            "gateway": {
                "name": "🌐 API Gateway",
                "script": "🌐💎⚡_UNIFIED_API_GATEWAY_⚡💎🌐.py",
                "port": 8000,
                "priority": 1,
                "required": True,
            }
        }
        self.running_processes = {}

    def start_service(self, service_id: str) -> bool:
        """Start a specific service"""
        if service_id not in self.services:
            print(f"❌ Service '{service_id}' not found")
            return False

        service = self.services[service_id]
        script_path = self.workspace / service["script"]

        if not script_path.exists():
            print(f"⚠️ Script not found: {script_path}")
            return False

        print(f"🚀 Starting {service['name']} on port {service['port']}...")

        try:
            cmd = [str(self.python_exe), str(script_path)]

            process = subprocess.Popen(
                cmd,
                cwd=str(self.workspace),
                creationflags=(
                    subprocess.CREATE_NEW_PROCESS_GROUP if os.name == "nt" else 0
                ),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )

            self.running_processes[service_id] = process
            print(f"✅ {service['name']} started successfully (PID: {process.pid})")
            return True

        except Exception as e:
            print(f"❌ Failed to start {service['name']}: {e}")
            return False

    def stop_service(self, service_id: str) -> bool:
        """Stop a specific service"""
        if service_id not in self.running_processes:
            print(f"⚠️ Service '{service_id}' is not running")
            return False

        process = self.running_processes[service_id]
        service_name = self.services[service_id]["name"]

        try:
            print(f"🛑 Stopping {service_name}...")

            if os.name == "nt":
                process.terminate()
            else:
                process.send_signal(signal.SIGTERM)

            # Wait for graceful shutdown
            time.sleep(2)

            if process.poll() is None:
                process.kill()

            del self.running_processes[service_id]
            print(f"✅ {service_name} stopped successfully")
            return True

        except Exception as e:
            print(f"❌ Error stopping {service_name}: {e}")
            return False

    def start_all_services(self) -> bool:
        """Start all services in priority order"""
        print("\n🚀 Starting all HyperFocus Zone services...")
        print("=" * 50)

        # Sort by priority
        sorted_services = sorted(self.services.items(), key=lambda x: x[1]["priority"])

        success_count = 0
        for service_id, service in sorted_services:
            if self.start_service(service_id):
                success_count += 1
                time.sleep(2)  # Stagger startup
            elif service.get("required", False):
                print(f"❌ Required service {service['name']} failed to start")
                return False

        print(
            f"\n✅ Started {success_count}/{len(self.services)} services successfully!"
        )
        return True

    def stop_all_services(self):
        """Stop all running services"""
        print("\n🛑 Stopping all services...")

        for service_id in list(self.running_processes.keys()):
            self.stop_service(service_id)

        print("✅ All services stopped")

    def get_status(self) -> Dict:
        """Get status of all services"""
        status = {
            "total_services": len(self.services),
            "running_services": 0,
            "stopped_services": 0,
            "services": {},
        }

        for service_id, service in self.services.items():
            if service_id in self.running_processes:
                process = self.running_processes[service_id]
                is_running = process.poll() is None

                status["services"][service_id] = {
                    "name": service["name"],
                    "port": service["port"],
                    "status": "running" if is_running else "stopped",
                    "pid": process.pid if is_running else None,
                }

                if is_running:
                    status["running_services"] += 1
                else:
                    status["stopped_services"] += 1
            else:
                status["services"][service_id] = {
                    "name": service["name"],
                    "port": service["port"],
                    "status": "not_started",
                    "pid": None,
                }
                status["stopped_services"] += 1

        return status

    def print_status(self):
        """Print detailed status of all services"""
        status = self.get_status()

        print(
            f"\n📊 Service Status ({status['running_services']}/{status['total_services']} running)"
        )
        print("-" * 50)

        for service_id, info in status["services"].items():
            status_icon = "✅" if info["status"] == "running" else "❌"
            pid_info = f" (PID: {info['pid']})" if info["pid"] else ""
            print(
                f"{status_icon} {info['name']} - Port {info['port']} - {info['status']}{pid_info}"
            )

    def monitor_services(self):
        """Monitor services and restart if needed"""
        print("\n📊 Monitoring services (Press Ctrl+C to stop)...")

        try:
            while True:
                # Check for dead processes
                dead_services = []
                for service_id, process in self.running_processes.items():
                    if process.poll() is not None:
                        dead_services.append(service_id)

                # Restart dead services
                for service_id in dead_services:
                    print(f"\n🔄 Service {service_id} died, restarting...")
                    del self.running_processes[service_id]
                    self.start_service(service_id)

                # Show status every 30 seconds
                time.sleep(30)
                self.print_status()

        except KeyboardInterrupt:
            print("\n\n🛑 Monitoring stopped by user")
            self.stop_all_services()


def main():
    """Main orchestrator function"""
    print("🎼💎⚡ HyperFocus Zone Service Orchestrator ⚡💎🎼")
    print("=" * 60)

    orchestrator = HyperFocusServiceOrchestrator()

    try:
        # Start all services
        if orchestrator.start_all_services():
            print("\n🌟 All services started successfully!")
            print("🎯 API Gateway available at: http://localhost:8000")
            print("📊 Service status:")
            orchestrator.print_status()

            print("\n⚡ Starting monitoring (Ctrl+C to stop all services)...")
            orchestrator.monitor_services()
        else:
            print("❌ Failed to start some required services")
            orchestrator.stop_all_services()

    except KeyboardInterrupt:
        print("\n\n🛑 Shutting down all services...")
        orchestrator.stop_all_services()
        print("✅ Shutdown complete")


if __name__ == "__main__":
    main()

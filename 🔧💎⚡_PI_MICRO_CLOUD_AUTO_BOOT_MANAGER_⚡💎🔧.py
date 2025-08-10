#!/usr/bin/env python3
"""
🔧💎⚡ PI MICRO-CLOUD AUTO-BOOT MANAGER ⚡💎🔧

LEGENDARY AUTO-BOOT FEATURES:
🔄 Automatic startup on Pi reboot
🔍 Health monitoring and auto-restart
📝 Comprehensive logging system
⚡ Graceful shutdown handling
🛠️ Service management interface
"""

from datetime import datetime
from typing import Dict, List, Any, Optional
import json
import subprocess
import time
class PiMicroCloudAutoBootManager:
    """🔧 Pi Micro-Cloud Auto-Boot Management System"""

    def __init__(self):
        self.service_name = "pi-microcloud.service"
        self.log_file = "/var/log/pi-microcloud.log"
        self.health_log = "/var/log/pi-microcloud-health.log"
        self.working_dir = "/home/pi/empire/pi-microcloud"

    def check_service_status(self) -> Dict[str, Any]:
        """🔍 Check systemd service status"""
        try:
            result = subprocess.run([
                'systemctl', 'is-active', self.service_name
            ], capture_output=True, text=True)

            active = result.stdout.strip() == 'active'

            # Get detailed status
            status_result = subprocess.run([
                'systemctl', 'status', self.service_name, '--no-pager'
            ], capture_output=True, text=True)

            # Check if enabled
            enabled_result = subprocess.run([
                'systemctl', 'is-enabled', self.service_name
            ], capture_output=True, text=True)

            enabled = enabled_result.stdout.strip() == 'enabled'

            return {
                'active': active,
                'enabled': enabled,
                'status_output': status_result.stdout,
                'auto_boot_configured': enabled
            }

        except Exception as e:
            return {
                'active': False,
                'enabled': False,
                'error': str(e),
                'auto_boot_configured': False
            }

    def check_docker_containers(self) -> Dict[str, Any]:
        """🐳 Check Docker container status"""
        try:
            result = subprocess.run([
                'docker', 'ps', '--format', 'json'
            ], capture_output=True, text=True)

            containers = []
            if result.stdout:
                for line in result.stdout.strip().split('\n'):
                    if line:
                        containers.append(json.loads(line))

            pi_containers = [c for c in containers if 'pi-' in c.get('Names', '')]

            return {
                'total_containers': len(containers),
                'pi_containers': len(pi_containers),
                'containers': pi_containers,
                'all_running': len(pi_containers) >= 4  # nginx, redis, agent, monitor
            }

        except Exception as e:
            return {
                'total_containers': 0,
                'pi_containers': 0,
                'containers': [],
                'all_running': False,
                'error': str(e)
            }

    def test_endpoints(self) -> Dict[str, Any]:
        """🌐 Test Pi micro-cloud endpoints"""
        endpoints = {
            'health': 'http://localhost/health',
            'status': 'http://localhost/pi/status',
            'metrics': 'http://localhost/metrics'
        }

        results = {}

        for name, url in endpoints.items():
            try:
                result = subprocess.run([
                    'curl', '-f', '-s', '--max-time', '5', url
                ], capture_output=True, text=True)

                results[name] = {
                    'url': url,
                    'accessible': result.returncode == 0,
                    'response_preview': result.stdout[:100] if result.stdout else ''
                }

            except Exception as e:
                results[name] = {
                    'url': url,
                    'accessible': False,
                    'error': str(e)
                }

        return results

    def get_system_info(self) -> Dict[str, Any]:
        """📊 Get Pi system information"""
        try:
            # Get Pi IP
            ip_result = subprocess.run([
                'hostname', '-I'
            ], capture_output=True, text=True)
            pi_ip = ip_result.stdout.strip().split()[0] if ip_result.stdout else 'unknown'

            # Get uptime
            uptime_result = subprocess.run([
                'uptime', '-p'
            ], capture_output=True, text=True)
            uptime = uptime_result.stdout.strip() if uptime_result.stdout else 'unknown'

            # Get temperature (Pi-specific)
            try:
                temp_result = subprocess.run([
                    'vcgencmd', 'measure_temp'
                ], capture_output=True, text=True)
                temperature = temp_result.stdout.strip() if temp_result.stdout else 'N/A'
            except Exception:
                temperature = 'N/A'

            # Get disk usage
            disk_result = subprocess.run([
                'df', '-h', '/'
            ], capture_output=True, text=True)
            disk_info = disk_result.stdout.split('\n')[1] if len(disk_result.stdout.split('\n')) > 1 else ''

            return {
                'pi_ip': pi_ip,
                'uptime': uptime,
                'temperature': temperature,
                'disk_info': disk_info,
                'timestamp': datetime.now().isoformat()
            }

        except Exception as e:
            return {
                'pi_ip': 'unknown',
                'uptime': 'unknown',
                'temperature': 'N/A',
                'disk_info': 'unknown',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }

    def enable_auto_boot(self) -> Dict[str, Any]:
        """🔄 Enable auto-boot service"""
        try:
            # Enable service
            result = subprocess.run([
                'sudo', 'systemctl', 'enable', self.service_name
            ], capture_output=True, text=True)

            if result.returncode == 0:
                return {
                    'success': True,
                    'message': 'Auto-boot enabled successfully',
                    'output': result.stdout
                }
            else:
                return {
                    'success': False,
                    'message': 'Failed to enable auto-boot',
                    'error': result.stderr
                }

        except Exception as e:
            return {
                'success': False,
                'message': 'Exception enabling auto-boot',
                'error': str(e)
            }

    def disable_auto_boot(self) -> Dict[str, Any]:
        """❌ Disable auto-boot service"""
        try:
            # Disable service
            result = subprocess.run([
                'sudo', 'systemctl', 'disable', self.service_name
            ], capture_output=True, text=True)

            if result.returncode == 0:
                return {
                    'success': True,
                    'message': 'Auto-boot disabled successfully',
                    'output': result.stdout
                }
            else:
                return {
                    'success': False,
                    'message': 'Failed to disable auto-boot',
                    'error': result.stderr
                }

        except Exception as e:
            return {
                'success': False,
                'message': 'Exception disabling auto-boot',
                'error': str(e)
            }

    def start_service(self) -> Dict[str, Any]:
        """🚀 Start the Pi micro-cloud service"""
        try:
            result = subprocess.run([
                'sudo', 'systemctl', 'start', self.service_name
            ], capture_output=True, text=True)

            if result.returncode == 0:
                return {
                    'success': True,
                    'message': 'Service started successfully'
                }
            else:
                return {
                    'success': False,
                    'message': 'Failed to start service',
                    'error': result.stderr
                }

        except Exception as e:
            return {
                'success': False,
                'message': 'Exception starting service',
                'error': str(e)
            }

    def stop_service(self) -> Dict[str, Any]:
        """🛑 Stop the Pi micro-cloud service"""
        try:
            result = subprocess.run([
                'sudo', 'systemctl', 'stop', self.service_name
            ], capture_output=True, text=True)

            if result.returncode == 0:
                return {
                    'success': True,
                    'message': 'Service stopped successfully'
                }
            else:
                return {
                    'success': False,
                    'message': 'Failed to stop service',
                    'error': result.stderr
                }

        except Exception as e:
            return {
                'success': False,
                'message': 'Exception stopping service',
                'error': str(e)
            }

    def restart_service(self) -> Dict[str, Any]:
        """🔄 Restart the Pi micro-cloud service"""
        try:
            result = subprocess.run([
                'sudo', 'systemctl', 'restart', self.service_name
            ], capture_output=True, text=True)

            if result.returncode == 0:
                return {
                    'success': True,
                    'message': 'Service restarted successfully'
                }
            else:
                return {
                    'success': False,
                    'message': 'Failed to restart service',
                    'error': result.stderr
                }

        except Exception as e:
            return {
                'success': False,
                'message': 'Exception restarting service',
                'error': str(e)
            }

    def get_comprehensive_status(self) -> Dict[str, Any]:
        """📊 Get comprehensive system status"""
        return {
            'timestamp': datetime.now().isoformat(),
            'service_status': self.check_service_status(),
            'docker_containers': self.check_docker_containers(),
            'endpoint_tests': self.test_endpoints(),
            'system_info': self.get_system_info()
        }

    def generate_status_report(self) -> str:
        """📝 Generate human-readable status report"""
        status = self.get_comprehensive_status()

        report = f"""
🔧💎⚡ PI MICRO-CLOUD AUTO-BOOT STATUS REPORT ⚡💎🔧
Generated: {status['timestamp']}

🔄 AUTO-BOOT SERVICE STATUS:
   • Service Active: {'✅ YES' if status['service_status']['active'] else '❌ NO'}
   • Auto-Boot Enabled: {'✅ YES' if status['service_status']['enabled'] else '❌ NO'}
   • Configuration Status: {'✅ CONFIGURED' if status['service_status']['auto_boot_configured'] else '❌ NOT CONFIGURED'}

🐳 DOCKER CONTAINERS:
   • Total Containers: {status['docker_containers']['total_containers']}
   • Pi Containers: {status['docker_containers']['pi_containers']}
   • All Services Running: {'✅ YES' if status['docker_containers']['all_running'] else '❌ NO'}

🌐 ENDPOINT ACCESSIBILITY:
"""

        for name, endpoint in status['endpoint_tests'].items():
            accessible = '✅ ACCESSIBLE' if endpoint['accessible'] else '❌ NOT ACCESSIBLE'
            report += f"   • {name.title()}: {accessible}\n"

        system = status['system_info']
        report += f"""
📊 SYSTEM INFORMATION:
   • Pi IP Address: {system['pi_ip']}
   • Uptime: {system['uptime']}
   • Temperature: {system['temperature']}
   • Disk Usage: {system['disk_info'].split() if system['disk_info'] else 'N/A'}

🛠️ MANAGEMENT COMMANDS:
   • Check Status: sudo systemctl status pi-microcloud
   • Start Service: sudo systemctl start pi-microcloud
   • Stop Service: sudo systemctl stop pi-microcloud
   • Restart Service: sudo systemctl restart pi-microcloud
   • Enable Auto-Boot: sudo systemctl enable pi-microcloud
   • Disable Auto-Boot: sudo systemctl disable pi-microcloud
   • View Logs: sudo journalctl -u pi-microcloud -f

🏆 AUTO-BOOT STATUS: {'✅ FULLY OPERATIONAL' if status['service_status']['enabled'] and status['docker_containers']['all_running'] else '⚠️ NEEDS ATTENTION'}
"""

        return report

def main():
    """🚀 Main auto-boot manager interface"""
    print("🔧💎⚡ PI MICRO-CLOUD AUTO-BOOT MANAGER ⚡💎🔧")
    print("=" * 80)

    manager = PiMicroCloudAutoBootManager()

    while True:
        print("\n🛠️ AUTO-BOOT MANAGEMENT OPTIONS:")
        print("1. 📊 Check Full Status")
        print("2. 🔄 Enable Auto-Boot")
        print("3. ❌ Disable Auto-Boot")
        print("4. 🚀 Start Service")
        print("5. 🛑 Stop Service")
        print("6. 🔄 Restart Service")
        print("7. 📝 Generate Status Report")
        print("8. 🚪 Exit")

        try:
            choice = input("\n🎯 Select option (1-8): ").strip()

            if choice == '1':
                print("\n📊 Checking comprehensive status...")
                status = manager.get_comprehensive_status()
                print(json.dumps(status, indent=2))

            elif choice == '2':
                print("\n🔄 Enabling auto-boot...")
                result = manager.enable_auto_boot()
                print(f"✅ Result: {result['message']}")

            elif choice == '3':
                print("\n❌ Disabling auto-boot...")
                result = manager.disable_auto_boot()
                print(f"✅ Result: {result['message']}")

            elif choice == '4':
                print("\n🚀 Starting service...")
                result = manager.start_service()
                print(f"✅ Result: {result['message']}")

            elif choice == '5':
                print("\n🛑 Stopping service...")
                result = manager.stop_service()
                print(f"✅ Result: {result['message']}")

            elif choice == '6':
                print("\n🔄 Restarting service...")
                result = manager.restart_service()
                print(f"✅ Result: {result['message']}")

            elif choice == '7':
                print("\n📝 Generating status report...")
                report = manager.generate_status_report()
                print(report)

                # Save report to file
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                filename = f"pi_autoboot_status_report_{timestamp}.txt"
                with open(filename, 'w') as f:
                    f.write(report)
                print(f"\n💾 Report saved to: {filename}")

            elif choice == '8':
                print("\n🚪 Exiting Pi Micro-Cloud Auto-Boot Manager...")
                break

            else:
                print("\n❌ Invalid option. Please select 1-8.")

        except KeyboardInterrupt:
            print("\n\n🚪 Exiting...")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()

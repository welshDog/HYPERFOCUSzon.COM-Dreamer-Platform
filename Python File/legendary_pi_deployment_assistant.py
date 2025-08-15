#!/usr/bin/env python3
"""
🚀💎⚡ LEGENDARY PI DEPLOYMENT EXECUTION ASSISTANT ⚡💎🚀

Step-by-step deployment execution with real-time guidance
"""

from datetime import datetime
import socket
import subprocess
import time

import requests
class LegendaryPiDeploymentAssistant:
    def __init__(self):
        self.pi_ip = "192.168.137.100"
        self.laptop_ip = "192.168.137.10"

        print(f"""
🚀💎⚡ LEGENDARY PI DEPLOYMENT EXECUTION ASSISTANT ⚡💎🚀
=======================================================

🎯 Target Pi IP: {self.pi_ip}
💻 Your Laptop IP: {self.laptop_ip}
📅 Deployment Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

🚀 Ready to execute LEGENDARY Pi deployment!
        """)

    def check_pi_connectivity(self):
        """🔍 Check if Pi is reachable"""
        print("🔍 Step 1: Checking Pi connectivity...")

        try:
            # Test ping first
            result = subprocess.run(['ping', '-n', '3', self.pi_ip],
                                  capture_output=True, text=True, timeout=10)

            if result.returncode == 0:
                print(f"✅ Pi is reachable at {self.pi_ip}")

                # Test SSH port
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(5)
                ssh_result = sock.connect_ex((self.pi_ip, 22))
                sock.close()

                if ssh_result == 0:
                    print("✅ SSH port is open and ready")
                    return True
                else:
                    print("❌ SSH port not accessible")
                    print("💡 Enable SSH on Pi and try again")
                    return False
            else:
                print(f"❌ Pi not reachable at {self.pi_ip}")
                print("💡 Check Pi network connection and IP configuration")
                return False

        except (socket.error, ConnectionError, requests.RequestException) as e:
            print(f"❌ Connectivity check failed: {e}")
            return False

    def execute_deployment(self):
        """🚀 Execute the deployment script"""
        print("🚀 Step 2: Executing legendary_pi_deploy.sh...")

        try:
            # For Windows, we need to use bash or WSL
            print("💡 Note: Running bash script on Windows")
            print("📋 Commands to run manually:")
            print()
            print("# 1. Copy deployment files to Pi:")
            print(f"scp docker-compose-legendary-pi.yml pi@{self.pi_ip}:/home/pi/microcloud/")
            print()
            print("# 2. SSH to Pi and deploy:")
            print(f"ssh pi@{self.pi_ip}")
            print("cd /home/pi/microcloud")
            print("docker-compose -f docker-compose-legendary-pi.yml down 2>/dev/null || true")
            print("docker-compose -f docker-compose-legendary-pi.yml up -d")
            print("sleep 30")
            print("docker-compose -f docker-compose-legendary-pi.yml ps")
            print()
            print("🎯 After deployment, continue to Step 3: Testing")

        except (socket.error, ConnectionError, requests.RequestException) as e:
            print(f"❌ Deployment execution error: {e}")

    def test_deployment(self):
        """🧪 Test the deployed Pi services"""
        print("🧪 Step 3: Testing Pi micro-cloud deployment...")

        services_to_test = [
            {"name": "Health Monitor", "url": f"http://{self.pi_ip}/health"},
            {"name": "BROski Agent", "url": f"http://{self.pi_ip}:8080/health"},
        ]

        all_passed = True

        for service in services_to_test:
            print(f"🔍 Testing {service['name']}...")
            try:
                response = requests.get(service['url'], timeout=10)
                if response.status_code == 200:
                    print(f"✅ {service['name']}: OPERATIONAL")
                else:
                    print(f"❌ {service['name']}: HTTP {response.status_code}")
                    all_passed = False
            except (socket.error, ConnectionError, requests.RequestException) as e:
                print(f"❌ {service['name']}: Connection failed ({e})")
                all_passed = False

        if all_passed:
            print(f"""

🏆💎⚡ LEGENDARY PI DEPLOYMENT SUCCESS! ⚡💎🏆
==============================================

🌐 Your Pi micro-cloud is OPERATIONAL!

📊 Service URLs:
   • Health Monitor:  http://{self.pi_ip}/
   • BROski Agent:    http://{self.pi_ip}:8080/

🎯 Next Steps:
   1. Run full testing suite: python legendary_pi_client_tester.py
   2. Monitor performance: Open http://{self.pi_ip}/ in browser
   3. Start task offloading with enhanced client

🚀 Your LEGENDARY Pi micro-cloud is ready for elite task offloading!
            """)
        else:
            print(f"""

⚠️ Some services need attention. Check:
1. Pi Docker containers are running
2. Firewall allows ports 80, 8080
3. Services started properly (check logs)

🔧 Troubleshooting:
   ssh pi@{self.pi_ip}
   cd /home/pi/microcloud
   docker-compose logs -f
            """)

    def run_full_deployment_sequence(self):
        """🎯 Run the complete deployment sequence"""
        print("🎯 Starting LEGENDARY Pi deployment sequence...")

        # Step 1: Check connectivity
        if not self.check_pi_connectivity():
            print("""
❌ Pi connectivity check failed!

🔧 Troubleshooting Steps:
1. Ensure Pi is powered on and connected to network
2. Check Pi has IP 192.168.137.100 (or find actual IP)
3. Enable SSH on Pi
4. Test: ping 192.168.137.100

💡 Pi Setup Instructions:
- Flash Pi OS to SD card
- Create empty 'ssh' file in boot partition
- Connect Pi to ethernet
- Power on and wait 2-3 minutes
            """)
            return False

        # Step 2: Execute deployment
        self.execute_deployment()

        # Wait for services to potentially start
        print("⏳ Waiting 60 seconds for services to start...")
        time.sleep(60)

        # Step 3: Test deployment
        self.test_deployment()

        return True

def main():
    """🚀 Main execution"""
    assistant = LegendaryPiDeploymentAssistant()

    print("""
🎯 DEPLOYMENT EXECUTION OPTIONS:

1. Full Automated Sequence (Recommended)
2. Step-by-step Manual Guidance
3. Just Test Current Deployment

Choose your preferred deployment method:
    """)

    try:
        choice = input("Enter choice (1-3): ").strip()

        if choice == "1":
            assistant.run_full_deployment_sequence()
        elif choice == "2":
            print("📋 Manual Step-by-step Guidance:")
            assistant.check_pi_connectivity()
            input("Press Enter after Pi connectivity confirmed...")
            assistant.execute_deployment()
            input("Press Enter after deployment completed...")
            assistant.test_deployment()
        elif choice == "3":
            assistant.test_deployment()
        else:
            print("Running full deployment sequence by default...")
            assistant.run_full_deployment_sequence()

    except KeyboardInterrupt:
        print("\n🛑 Deployment cancelled by user")
    except (socket.error, ConnectionError, requests.RequestException) as e:
        print(f"❌ Deployment error: {e}")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
🌐💎⚡ TAILSCALE 100.71.69.16 RECOVERY PROTOCOL ⚡💎🌐

**BROski Level: LEGENDARY | Status: IMMEDIATE RECOVERY**
**Following LOOK-THEN-BUILD Protocol - UPGRADING existing system**

Mission: Fix Tailscale server 100.71.69.16 using invite link integration
Target: https://login.tailscale.com/admin/invite/hzjC7YqwteVceWfw2hEu11
"""

import subprocess
import requests
import json
import time
from datetime import datetime

class TailscaleRecoveryProtocol:
    def __init__(self):
        self.target_ip = "100.71.69.16"
        self.server_name = "ubuntu-1"
        self.invite_link = "https://login.tailscale.com/admin/invite/hzjC7YqwteVceWfw2hEu11"
        self.report = {
            "timestamp": datetime.now().isoformat(),
            "target": self.target_ip,
            "server": self.server_name,
            "recovery_steps": [],
            "success_status": False
        }
        
    def print_header(self):
        print("🌐💎⚡ TAILSCALE RECOVERY PROTOCOL - 100.71.69.16 ⚡💎🌐")
        print("=" * 70)
        print(f"🎯 Target Server: {self.server_name} ({self.target_ip})")
        print(f"🔗 Invite Link: {self.invite_link}")
        print(f"⏰ Recovery Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()
        
    def step_1_current_status(self):
        """Check current Tailscale status"""
        print("🔍 STEP 1: CURRENT TAILSCALE STATUS CHECK")
        print("-" * 50)
        
        try:
            # Check local Tailscale status
            result = subprocess.run(
                ["tailscale", "status"], 
                capture_output=True, 
                text=True, 
                timeout=10
            )
            
            if result.returncode == 0:
                print("✅ LOCAL TAILSCALE STATUS:")
                print(result.stdout)
                
                if self.target_ip in result.stdout:
                    print(f"🎯 FOUND TARGET: {self.target_ip} in network")
                    if "offline" in result.stdout.lower():
                        print(f"❌ STATUS: Server {self.server_name} is OFFLINE")
                    else:
                        print(f"✅ STATUS: Server {self.server_name} is ONLINE")
                else:
                    print(f"⚠️ TARGET NOT FOUND: {self.target_ip} not in current network")
                    
            else:
                print("❌ Tailscale not accessible or not logged in")
                print(f"Error: {result.stderr}")
                
        except Exception as e:
            print(f"⚠️ Error checking Tailscale status: {str(e)}")
            
        print()
        
    def step_2_connectivity_test(self):
        """Test direct connectivity to target server"""
        print("🔍 STEP 2: CONNECTIVITY TEST")
        print("-" * 50)
        
        # Ping test
        try:
            result = subprocess.run(
                ["ping", "-n", "4", self.target_ip], 
                capture_output=True, 
                text=True, 
                timeout=15
            )
            
            if result.returncode == 0:
                print(f"✅ PING SUCCESS: {self.target_ip} is reachable")
                print("📊 Network connectivity confirmed")
            else:
                print(f"❌ PING FAILED: {self.target_ip} unreachable")
                print("🔧 Network issue detected")
                
        except Exception as e:
            print(f"⚠️ Ping test error: {str(e)}")
            
        # SSH connectivity test
        try:
            result = subprocess.run(
                ["ssh", "-o", "ConnectTimeout=5", f"root@{self.target_ip}", "echo 'SSH Success'"], 
                capture_output=True, 
                text=True, 
                timeout=10
            )
            
            if result.returncode == 0:
                print(f"✅ SSH SUCCESS: Can connect to {self.target_ip}")
                self.report["ssh_accessible"] = True
            else:
                print(f"❌ SSH FAILED: Cannot connect to {self.target_ip}")
                self.report["ssh_accessible"] = False
                
        except Exception as e:
            print(f"⚠️ SSH test error: {str(e)}")
            
        print()
        
    def step_3_recovery_actions(self):
        """Execute recovery actions"""
        print("🚀 STEP 3: RECOVERY ACTIONS")
        print("-" * 50)
        
        print("🔧 RECOMMENDED RECOVERY ACTIONS:")
        print()
        
        actions = [
            "1. 🌐 Use the Tailscale invite link to re-add the server",
            "2. ⬆️ Update Tailscale on the target server to latest version",
            "3. 🔄 Restart Tailscale service on target server", 
            "4. 🛡️ Check firewall settings on target server",
            "5. 🌐 Verify network routing and DNS settings"
        ]
        
        for action in actions:
            print(f"   {action}")
            
        print()
        print("🎯 PRIMARY ACTION: Use the invite link")
        print(f"   🔗 {self.invite_link}")
        print()
        print("📋 MANUAL STEPS:")
        print("   1. Open the invite link in your browser")
        print("   2. Log in to your Tailscale admin console")
        print("   3. Accept the server back into the network")
        print("   4. On the server, run: sudo tailscale up")
        print("   5. Verify connection with: tailscale ping 100.71.69.16")
        
        print()
        
    def step_4_advanced_troubleshooting(self):
        """Advanced troubleshooting options"""
        print("🔧 STEP 4: ADVANCED TROUBLESHOOTING OPTIONS")
        print("-" * 50)
        
        print("🛠️ IF BASIC RECOVERY FAILS, TRY:")
        print()
        
        advanced_steps = [
            "🔄 Complete Tailscale reinstall:",
            "   • sudo tailscale logout",
            "   • curl -fsSL https://tailscale.com/install.sh | sh", 
            "   • sudo tailscale up",
            "",
            "🌐 Alternative access methods:",
            "   • Try IPv6 connection if available",
            "   • Use Tailscale domain names instead of IP",
            "   • Check if server is accessible via other interfaces",
            "",
            "🛡️ Security checks:",
            "   • Verify iptables/ufw firewall rules",
            "   • Check if SSH daemon is running",
            "   • Confirm network interfaces are up",
            "",
            "🚨 Emergency access:",
            "   • Physical console access if available",
            "   • Alternative VPN or network access",
            "   • Cloud provider console access"
        ]
        
        for step in advanced_steps:
            print(f"   {step}")
            
        print()
        
    def step_5_prevention(self):
        """Prevention and monitoring setup"""
        print("🛡️ STEP 5: PREVENTION & MONITORING")
        print("-" * 50)
        
        print("📊 SET UP MONITORING:")
        print("   • Add server monitoring to Grafana dashboards")
        print("   • Set up automated Tailscale status checks")
        print("   • Configure alerts for server offline events")
        print()
        
        print("🔄 MAINTENANCE SCHEDULE:")
        print("   • Weekly Tailscale version checks")
        print("   • Monthly connectivity verification")
        print("   • Backup access methods documentation")
        print()
        
    def save_recovery_report(self):
        """Save recovery report"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"tailscale_recovery_100_71_69_16_{timestamp}.json"
        
        with open(filename, 'w') as f:
            json.dump(self.report, f, indent=2)
            
        print(f"📄 RECOVERY REPORT SAVED: {filename}")
        
    def print_summary(self):
        """Print executive summary"""
        print("\n📊 RECOVERY PROTOCOL SUMMARY")
        print("=" * 70)
        
        print(f"🎯 Target: {self.server_name} ({self.target_ip})")
        print(f"🔗 Invite Link: Available for re-authentication")
        print(f"📈 Recovery Priority: HIGH")
        print(f"🕒 Estimated Fix Time: 15-30 minutes")
        print()
        
        print("🚀 IMMEDIATE NEXT STEPS:")
        print("   1. Open the Tailscale invite link")
        print("   2. Re-authenticate the server")
        print("   3. Update Tailscale on the server")
        print("   4. Test connectivity")
        print("   5. Add to monitoring systems")
        
        print()
        print("💎 SUCCESS INDICATOR:")
        print("   ✅ Server shows as 'active' in Tailscale status")
        print("   ✅ SSH connection works: ssh root@100.71.69.16")
        print("   ✅ Server appears in Grafana monitoring")
        
def main():
    recovery = TailscaleRecoveryProtocol()
    
    try:
        recovery.print_header()
        recovery.step_1_current_status()
        recovery.step_2_connectivity_test()
        recovery.step_3_recovery_actions()
        recovery.step_4_advanced_troubleshooting()
        recovery.step_5_prevention()
        recovery.save_recovery_report()
        recovery.print_summary()
        
        print("\n🎊 TAILSCALE RECOVERY PROTOCOL COMPLETE! 🎊")
        
    except KeyboardInterrupt:
        print("\n⚠️ Recovery protocol interrupted by user")
    except Exception as e:
        print(f"\n❌ Recovery protocol failed: {str(e)}")

if __name__ == "__main__":
    main()

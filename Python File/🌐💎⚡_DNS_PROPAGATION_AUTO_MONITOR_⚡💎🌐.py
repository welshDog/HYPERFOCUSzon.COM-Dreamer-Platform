#!/usr/bin/env python3
"""
🌐💎⚡ DNS PROPAGATION AUTO MONITOR ⚡💎🌐
=============================================
Automated DNS propagation monitoring system
Following ULTRA-THINKING BOARDROOM recommendations
=============================================
"""

import time
import subprocess
import requests
import json
import datetime
from threading import Thread

class DNSPropagationAutoMonitor:
    def __init__(self):
        self.monitoring_active = True
        self.check_interval = 300  # 5 minutes
        self.dns_servers = [
            "8.8.8.8",      # Google
            "1.1.1.1",      # Cloudflare
            "208.67.222.222", # OpenDNS
            "9.9.9.9"       # Quad9
        ]
        self.domains_to_check = [
            "hyperfocuszone.com",
            "thedook.com",
            "hyperai.zone"
        ]

    def check_dns_propagation(self, domain):
        """Check DNS propagation across multiple servers"""
        results = {}

        for dns_server in self.dns_servers:
            try:
                # Use nslookup to check DNS resolution
                cmd = f"nslookup {domain} {dns_server}"
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=10)

                if result.returncode == 0 and "NXDOMAIN" not in result.stdout:
                    results[dns_server] = "✅ RESOLVED"
                else:
                    results[dns_server] = "🔄 PROPAGATING"

            except Exception as e:
                results[dns_server] = f"⚠️ ERROR: {str(e)[:50]}"

        return results

    def check_ssl_status(self, domain):
        """Check SSL certificate status"""
        try:
            response = requests.get(f"https://{domain}", timeout=10, verify=True)
            if response.status_code == 200:
                return "✅ SSL_ACTIVE"
            else:
                return f"🔄 SSL_RESPONSE_{response.status_code}"
        except requests.exceptions.SSLError:
            return "🚨 SSL_ERROR"
        except requests.exceptions.ConnectionError:
            return "🔄 SSL_CONNECTING"
        except Exception as e:
            return f"⚠️ SSL_CHECK_ERROR"

    def calculate_propagation_percentage(self, dns_results):
        """Calculate DNS propagation completion percentage"""
        resolved = sum(1 for result in dns_results.values() if "RESOLVED" in result)
        total = len(dns_results)
        return (resolved / total) * 100 if total > 0 else 0

    def monitor_continuous(self):
        """Continuous monitoring loop"""
        print("🌐💎⚡ DNS PROPAGATION AUTO MONITOR ACTIVATED ⚡💎🌐")
        print("=" * 65)
        print("🎯 Following ULTRA-THINKING BOARDROOM Priority: CRITICAL")
        print("⚡ Automated monitoring every 5 minutes")
        print("🚨 Will alert on completion milestones")
        print()

        while self.monitoring_active:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"🔍 DNS CHECK: {timestamp}")
            print("-" * 40)

            total_propagation = 0
            domain_count = 0

            for domain in self.domains_to_check:
                dns_results = self.check_dns_propagation(domain)
                ssl_status = self.check_ssl_status(domain)
                propagation_pct = self.calculate_propagation_percentage(dns_results)

                total_propagation += propagation_pct
                domain_count += 1

                print(f"🌐 {domain.upper()}:")
                print(f"   DNS Propagation: {propagation_pct:.1f}%")
                print(f"   SSL Status: {ssl_status}")

                # Show detailed DNS results
                for server, status in dns_results.items():
                    server_name = {
                        "8.8.8.8": "Google",
                        "1.1.1.1": "Cloudflare",
                        "208.67.222.222": "OpenDNS",
                        "9.9.9.9": "Quad9"
                    }.get(server, server)
                    print(f"   {server_name}: {status}")
                print()

            # Calculate overall propagation
            overall_propagation = total_propagation / domain_count if domain_count > 0 else 0

            print(f"🏆 OVERALL DNS HEALTH: {overall_propagation:.1f}%")

            # Alert on milestones
            if overall_propagation >= 95:
                print("🎉 MILESTONE ACHIEVED: DNS PROPAGATION 95%+ COMPLETE!")
                print("⚡ Empire Health Boost: +25% incoming!")
                self.send_completion_alert("LEGENDARY", overall_propagation)
            elif overall_propagation >= 80:
                print("🚀 MILESTONE: DNS PROPAGATION 80%+ - Excellent progress!")
                self.send_completion_alert("EXCELLENT", overall_propagation)
            elif overall_propagation >= 60:
                print("✅ MILESTONE: DNS PROPAGATION 60%+ - Good progress!")

            print(f"⏰ Next check in {self.check_interval//60} minutes...")
            print("=" * 65)
            print()

            # Wait for next check
            time.sleep(self.check_interval)

    def send_completion_alert(self, level, percentage):
        """Send completion alert to monitoring system"""
        alert_data = {
            "timestamp": datetime.datetime.now().isoformat(),
            "alert_level": level,
            "dns_propagation_percentage": percentage,
            "empire_health_impact": "+25%" if percentage >= 95 else "+15%",
            "recommended_action": "Verify SSL certificates" if percentage >= 95 else "Continue monitoring"
        }

        # Save alert to file
        alert_file = f"DNS_PROPAGATION_ALERT_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        try:
            with open(alert_file, 'w') as f:
                json.dump(alert_data, f, indent=2)
            print(f"📄 Alert saved: {alert_file}")
        except Exception as e:
            print(f"⚠️ Alert save error: {e}")

    def start_monitoring(self):
        """Start monitoring in background thread"""
        monitor_thread = Thread(target=self.monitor_continuous, daemon=True)
        monitor_thread.start()
        return monitor_thread

def main():
    """Main execution function"""
    monitor = DNSPropagationAutoMonitor()

    print("🎯 ULTRA-THINKING BOARDROOM DIRECTIVE: ACTIVATE DNS MONITORING")
    print("🚨 Priority: CRITICAL - Empire Health +25% target")
    print("⚡ Starting automated DNS propagation monitoring...")
    print()

    try:
        # Start monitoring
        monitor.monitor_continuous()
    except KeyboardInterrupt:
        print("\n🛑 DNS monitoring stopped by user")
        monitor.monitoring_active = False
    except Exception as e:
        print(f"⚠️ Monitoring error: {e}")
        print("🔄 Attempting restart in 30 seconds...")
        time.sleep(30)
        main()  # Restart monitoring

if __name__ == "__main__":
    main()

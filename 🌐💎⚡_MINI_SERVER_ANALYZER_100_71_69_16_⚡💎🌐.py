#!/usr/bin/env python3
"""
🌐💎⚡ MINI SERVER ANALYZER - 100.71.69.16 ⚡💎🌐

**BROski Level: LEGENDARY | Status: SERVER ANALYSIS PROTOCOL**
**Following LOOK-THEN-BUILD Protocol**

Mission: Complete analysis of the mini server at 100.71.69.16
"""

import socket
import subprocess
import requests
import json
import time
from datetime import datetime
from pathlib import Path

class MiniServerAnalyzer:
    def __init__(self):
        self.target_ip = "100.71.69.16"
        self.report = {
            "timestamp": datetime.now().isoformat(),
            "target": self.target_ip,
            "analysis_results": {},
            "recommendations": []
        }
        
    def print_header(self):
        print("🌐💎⚡ MINI SERVER ANALYZER - 100.71.69.16 ⚡💎🌐")
        print("=" * 60)
        print(f"🎯 Target: {self.target_ip}")
        print(f"⏰ Analysis Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()
        
    def ping_test(self):
        """Test basic connectivity"""
        print("🔍 PHASE 1: CONNECTIVITY TEST")
        print("-" * 30)
        
        try:
            # Windows ping command
            result = subprocess.run(
                ["ping", "-n", "4", self.target_ip], 
                capture_output=True, 
                text=True, 
                timeout=15
            )
            
            if result.returncode == 0:
                print(f"✅ PING TEST: SUCCESS")
                print(f"   Server is reachable at {self.target_ip}")
                self.report["analysis_results"]["connectivity"] = "SUCCESS"
                
                # Extract ping statistics
                output_lines = result.stdout.split('\n')
                for line in output_lines:
                    if 'Average' in line or 'Minimum' in line or 'Maximum' in line:
                        print(f"   📊 {line.strip()}")
                        
            else:
                print(f"❌ PING TEST: FAILED")
                print(f"   Server may be offline or blocking ICMP")
                self.report["analysis_results"]["connectivity"] = "FAILED"
                
        except Exception as e:
            print(f"⚠️ PING ERROR: {str(e)}")
            self.report["analysis_results"]["connectivity"] = f"ERROR: {str(e)}"
            
        print()
        
    def port_scan(self):
        """Scan common ports"""
        print("🔍 PHASE 2: PORT SCANNING")
        print("-" * 30)
        
        # Common ports to check
        common_ports = {
            22: "SSH",
            23: "Telnet", 
            25: "SMTP",
            53: "DNS",
            80: "HTTP",
            110: "POP3",
            143: "IMAP",
            443: "HTTPS",
            993: "IMAPS",
            995: "POP3S",
            3000: "Development Server",
            3001: "Alternative Web",
            8000: "HTTP Alternative",
            8080: "HTTP Proxy",
            8443: "HTTPS Alternative",
            9000: "Various Services"
        }
        
        open_ports = []
        
        for port, service in common_ports.items():
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(3)
                result = sock.connect_ex((self.target_ip, port))
                sock.close()
                
                if result == 0:
                    print(f"   ✅ Port {port:4}: {service} - OPEN")
                    open_ports.append({"port": port, "service": service, "status": "OPEN"})
                else:
                    print(f"   ❌ Port {port:4}: {service} - CLOSED/FILTERED")
                    
            except Exception as e:
                print(f"   ⚠️ Port {port:4}: ERROR - {str(e)}")
                
        self.report["analysis_results"]["open_ports"] = open_ports
        
        if open_ports:
            print(f"\n🚀 FOUND {len(open_ports)} OPEN PORTS!")
            for port_info in open_ports:
                print(f"   🔗 {port_info['port']} - {port_info['service']}")
        else:
            print("\n❌ NO OPEN PORTS DETECTED")
            print("   • Server may be behind firewall")
            print("   • Services may be on non-standard ports")
            
        print()
        
    def http_analysis(self):
        """Check HTTP services"""
        print("🔍 PHASE 3: HTTP SERVICE ANALYSIS")
        print("-" * 30)
        
        http_ports = [80, 443, 8000, 8080, 3000, 3001]
        
        for port in http_ports:
            protocol = "https" if port == 443 or port == 8443 else "http"
            url = f"{protocol}://{self.target_ip}:{port}"
            
            try:
                response = requests.get(url, timeout=10, verify=False)
                
                print(f"✅ {url}")
                print(f"   📊 Status: {response.status_code}")
                print(f"   📏 Content Length: {len(response.content)} bytes")
                
                # Check for common headers
                server_header = response.headers.get('Server', 'Unknown')
                print(f"   🖥️ Server: {server_header}")
                
                # Check for title if HTML
                if 'text/html' in response.headers.get('Content-Type', ''):
                    try:
                        title_start = response.text.find('<title>')
                        title_end = response.text.find('</title>')
                        if title_start != -1 and title_end != -1:
                            title = response.text[title_start+7:title_end]
                            print(f"   📝 Page Title: {title[:50]}...")
                    except:
                        pass
                        
                self.report["analysis_results"][f"http_{port}"] = {
                    "status": "SUCCESS",
                    "status_code": response.status_code,
                    "server": server_header,
                    "content_length": len(response.content)
                }
                
                print()
                
            except requests.exceptions.ConnectTimeout:
                print(f"⏱️ {url} - Connection Timeout")
            except requests.exceptions.ConnectionError:
                print(f"❌ {url} - Connection Refused")
            except Exception as e:
                print(f"⚠️ {url} - Error: {str(e)}")
                
        print()
        
    def system_identification(self):
        """Try to identify what type of system this is"""
        print("🔍 PHASE 4: SYSTEM IDENTIFICATION")
        print("-" * 30)
        
        # Check if it responds to common service requests
        identifiers = []
        
        # Check for web server responses
        for port in [80, 8000, 3000]:
            try:
                response = requests.get(f"http://{self.target_ip}:{port}", timeout=5)
                server = response.headers.get('Server', '')
                if server:
                    identifiers.append(f"Web Server: {server}")
            except:
                pass
                
        if identifiers:
            print("🎯 SYSTEM CHARACTERISTICS DETECTED:")
            for identifier in identifiers:
                print(f"   • {identifier}")
        else:
            print("❓ SYSTEM TYPE: UNKNOWN")
            print("   • Could be a custom application server")
            print("   • May be running minimal services")
            print("   • Could be a development/testing environment")
            
        self.report["analysis_results"]["system_identifiers"] = identifiers
        print()
        
    def generate_recommendations(self):
        """Generate recommendations based on analysis"""
        print("🎯 PHASE 5: RECOMMENDATIONS & NEXT STEPS")
        print("-" * 30)
        
        recommendations = []
        
        # Based on connectivity
        if self.report["analysis_results"].get("connectivity") == "SUCCESS":
            recommendations.append("✅ Server is reachable - good network connectivity")
        else:
            recommendations.append("🔧 Check network connectivity and firewall settings")
            
        # Based on open ports
        open_ports = self.report["analysis_results"].get("open_ports", [])
        if open_ports:
            recommendations.append(f"🔗 Found {len(open_ports)} open services - investigate each one")
            for port_info in open_ports:
                if port_info["service"] in ["HTTP", "HTTPS"]:
                    recommendations.append(f"🌐 Port {port_info['port']} has web service - check for admin interfaces")
                elif port_info["service"] == "SSH":
                    recommendations.append(f"🔐 Port {port_info['port']} has SSH - secure remote access available")
        else:
            recommendations.append("🔒 No open ports detected - very secure or behind firewall")
            
        # Security recommendations
        recommendations.extend([
            "🛡️ Run detailed vulnerability scan if this is your server",
            "📊 Set up monitoring for this server",
            "🔍 Check logs for any unusual activity",
            "📋 Document all services and their purposes"
        ])
        
        self.report["recommendations"] = recommendations
        
        for rec in recommendations:
            print(f"   {rec}")
            
        print()
        
    def save_report(self):
        """Save analysis report"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"mini_server_analysis_{self.target_ip.replace('.', '_')}_{timestamp}.json"
        
        with open(filename, 'w') as f:
            json.dump(self.report, f, indent=2)
            
        print(f"📄 ANALYSIS REPORT SAVED: {filename}")
        print()
        
    def print_summary(self):
        """Print executive summary"""
        print("📊 EXECUTIVE SUMMARY")
        print("=" * 60)
        
        connectivity = self.report["analysis_results"].get("connectivity", "UNKNOWN")
        open_ports = len(self.report["analysis_results"].get("open_ports", []))
        
        print(f"🎯 Target Server: {self.target_ip}")
        print(f"🔗 Connectivity: {connectivity}")
        print(f"🚪 Open Ports: {open_ports}")
        print(f"📈 Analysis Quality: {'COMPREHENSIVE' if connectivity == 'SUCCESS' else 'LIMITED'}")
        
        if open_ports > 0:
            print(f"🚀 Status: ACTIVE SERVER with {open_ports} services")
        else:
            print(f"🔒 Status: MINIMAL/SECURED SERVER")
            
        print()
        print("💎 WHAT THIS SERVER DOES:")
        if open_ports > 0:
            print("   • Provides network services")
            print("   • May host web applications or APIs")
            print("   • Could be development/production environment")
        else:
            print("   • Operates with minimal external services")
            print("   • Could be internal/private server")
            print("   • May use non-standard port configurations")
            
        print()
        
def main():
    analyzer = MiniServerAnalyzer()
    
    try:
        analyzer.print_header()
        analyzer.ping_test()
        analyzer.port_scan() 
        analyzer.http_analysis()
        analyzer.system_identification()
        analyzer.generate_recommendations()
        analyzer.save_report()
        analyzer.print_summary()
        
        print("🎊 MINI SERVER ANALYSIS COMPLETE! 🎊")
        print()
        print("💡 Next Steps:")
        print("   1. Review the saved JSON report")
        print("   2. Follow the recommendations")
        print("   3. Set up monitoring if it's your server")
        print("   4. Document any findings in your empire logs")
        
    except KeyboardInterrupt:
        print("\n⚠️ Analysis interrupted by user")
    except Exception as e:
        print(f"\n❌ Analysis failed: {str(e)}")

if __name__ == "__main__":
    main()

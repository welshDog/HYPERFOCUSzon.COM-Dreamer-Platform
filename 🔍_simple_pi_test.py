#!/usr/bin/env python3
"""
🔍 Simple Pi Connectivity Test 🔍
"""
import requests
import socket
import sys
from datetime import datetime

def test_pi_connectivity(pi_ip):
    print(f"🔍 Testing Pi connectivity at {pi_ip}")
    print(f"🕐 Test time: {datetime.now()}")
    
    # Test 1: Socket connectivity
    print(f"\n📡 Testing socket connection to {pi_ip}:80...")
    try:
        sock = socket.create_connection((pi_ip, 80), 5)
        sock.close()
        print(f"✅ Socket connection successful")
    except Exception as e:
        print(f"❌ Socket connection failed: {e}")
        return False
    
    # Test 2: HTTP request
    print(f"🌐 Testing HTTP request...")
    try:
        response = requests.get(f"http://{pi_ip}/health", timeout=10)
        print(f"📊 HTTP Status: {response.status_code}")
        print(f"📄 Response: {response.text[:100]}")
        return True
    except Exception as e:
        print(f"❌ HTTP request failed: {e}")
        
        # Try alternative endpoints
        for endpoint in ["/", "/pi/status"]:
            try:
                response = requests.get(f"http://{pi_ip}{endpoint}", timeout=5)
                print(f"📍 {endpoint}: HTTP {response.status_code}")
                return True
            except:
                continue
        return False

def scan_local_network():
    print(f"🔍 Scanning for active devices...")
    
    # Get local IP
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        network_base = '.'.join(local_ip.split('.')[:-1]) + '.'
        print(f"🌐 Local network: {network_base}x")
        
        active_devices = []
        for i in [1, 10, 20, 50, 100, 101, 200, 201]:
            test_ip = f"{network_base}{i}"
            try:
                sock = socket.create_connection((test_ip, 80), 1)
                sock.close()
                active_devices.append(test_ip)
                print(f"✅ Found device: {test_ip}")
            except:
                continue
        
        return active_devices
    except Exception as e:
        print(f"⚠️ Network scan error: {e}")
        return []

if __name__ == "__main__":
    print("🚀💎⚡ PI CONNECTIVITY TEST ⚡💎🚀")
    print("=" * 40)
    
    pi_ip = sys.argv[1] if len(sys.argv) > 1 else "192.168.1.200"
    
    if test_pi_connectivity(pi_ip):
        print(f"\n✅ Pi micro-cloud is reachable at {pi_ip}")
        print(f"🌐 Try: http://{pi_ip}/pi/status")
    else:
        print(f"\n❌ Could not reach Pi at {pi_ip}")
        print("🔍 Scanning for other devices...")
        devices = scan_local_network()
        if devices:
            print(f"📡 Found {len(devices)} active devices: {devices}")
        else:
            print("❌ No active devices found")
        
        print(f"\n🛠️ NEXT STEPS:")
        print(f"1. Check if Pi is powered on")
        print(f"2. Verify Pi IP: hostname -I")
        print(f"3. Test Pi locally: curl http://localhost/health")
        print(f"4. Check micro-cloud: docker ps")

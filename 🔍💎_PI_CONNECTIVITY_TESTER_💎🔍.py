#!/usr/bin/env python3
"""
🔍💎 PI CONNECTIVITY TESTER 💎🔍
Simple tool to test Pi micro-cloud connectivity and basic performance
"""

import asyncio
import aiohttp
import time
import socket
import sys
from datetime import datetime

async def test_pi_connectivity(pi_ip: str, timeout: int = 10):
    """Test basic connectivity to Pi"""
    print(f"🔍 Testing connectivity to Pi at {pi_ip}...")
    
    # Test 1: TCP Socket connection
    print(f"📡 Testing TCP socket connection...")
    try:
        sock = socket.create_connection((pi_ip, 80), timeout)
        sock.close()
        print(f"✅ TCP connection to {pi_ip}:80 successful")
        tcp_success = True
    except Exception as e:
        print(f"❌ TCP connection failed: {e}")
        tcp_success = False
    
    # Test 2: HTTP connectivity
    print(f"🌐 Testing HTTP connectivity...")
    try:
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=timeout)) as session:
            async with session.get(f"http://{pi_ip}/health") as response:
                if response.status == 200:
                    data = await response.text()
                    print(f"✅ HTTP health check successful: {data.strip()}")
                    return True
                else:
                    print(f"⚠️ HTTP responded with status {response.status}")
                    return False
    except Exception as e:
        print(f"❌ HTTP connection failed: {e}")
        
        # Try alternative endpoints
        for endpoint in ["/", "/pi/status", "/api/health"]:
            try:
                async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=5)) as session:
                    async with session.get(f"http://{pi_ip}{endpoint}") as response:
                        print(f"📍 Alternative endpoint {endpoint}: HTTP {response.status}")
                        if response.status < 500:
                            return True
            except:
                continue
    
    return tcp_success

async def scan_network_for_pi():
    """Scan local network for active Pi devices"""
    print("🔍 Scanning local network for Pi devices...")
    
    # Get local network range
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        network_base = '.'.join(local_ip.split('.')[:-1]) + '.'
        print(f"🌐 Local network base: {network_base}x")
        
        # Test common Pi IPs
        common_ips = [f"{network_base}{i}" for i in [100, 101, 200, 201, 10, 20, 50]]
        
        print("📡 Testing common Pi IP addresses...")
        for ip in common_ips:
            try:
                # Quick TCP test
                sock = socket.create_connection((ip, 80), 2)
                sock.close()
                print(f"✅ Found active device at {ip}:80")
                
                # Test if it's a Pi with our micro-cloud
                try:
                    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=3)) as session:
                        async with session.get(f"http://{ip}/health") as response:
                            if response.status == 200:
                                data = await response.text()
                                if "Pi" in data or "Micro-Cloud" in data:
                                    print(f"🥧 Found Pi micro-cloud at {ip}!")
                                    return ip
                except:
                    pass
                    
            except:
                continue
                
    except Exception as e:
        print(f"⚠️ Network scan error: {e}")
    
    return None

async def quick_performance_test(pi_ip: str):
    """Quick performance test"""
    print(f"⚡ Running quick performance test on {pi_ip}...")
    
    try:
        # Latency test
        start_time = time.time()
        async with aiohttp.ClientSession() as session:
            async with session.get(f"http://{pi_ip}/health") as response:
                await response.read()
                latency = (time.time() - start_time) * 1000
                print(f"📊 HTTP latency: {latency:.2f} ms")
        
        # Simple throughput test
        test_data = b'0' * (1024 * 10)  # 10KB
        start_time = time.time()
        async with aiohttp.ClientSession() as session:
            async with session.post(f"http://{pi_ip}/api/offload", data=test_data) as response:
                await response.read()
                duration = time.time() - start_time
                throughput = (len(test_data) * 8) / (duration * 1_000_000)  # Mbps
                print(f"📊 Upload throughput: {throughput:.2f} Mbps")
                
    except Exception as e:
        print(f"⚠️ Performance test failed: {e}")

async def main():
    """Main function"""
    print("🚀💎⚡ PI CONNECTIVITY TESTER ⚡💎🚀")
    print("=" * 50)
    
    # Get Pi IP from command line or use default
    pi_ip = sys.argv[1] if len(sys.argv) > 1 else "192.168.1.200"
    print(f"🎯 Target Pi IP: {pi_ip}")
    print(f"🕐 Test time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Test connectivity
    connected = await test_pi_connectivity(pi_ip)
    
    if not connected:
        print(f"\n❌ Could not connect to Pi at {pi_ip}")
        print("🔍 Attempting network scan...")
        
        found_ip = await scan_network_for_pi()
        if found_ip:
            print(f"🎯 Found Pi at {found_ip}, testing performance...")
            await quick_performance_test(found_ip)
        else:
            print("❌ No Pi micro-cloud found on local network")
            print("\n🛠️ TROUBLESHOOTING STEPS:")
            print("1. Ensure Pi is powered on and connected to network")
            print("2. Check Pi IP address with: hostname -I")
            print("3. Verify micro-cloud stack is running: docker ps")
            print("4. Test Pi locally: curl http://localhost/health")
            print("5. Check firewall settings on Pi and laptop")
    else:
        print(f"\n✅ Successfully connected to Pi at {pi_ip}")
        await quick_performance_test(pi_ip)
        
        print(f"\n🎊 CONNECTIVITY TEST COMPLETE!")
        print(f"🌐 Pi micro-cloud is accessible at: http://{pi_ip}")
        print(f"📊 Status endpoint: http://{pi_ip}/pi/status")
        print(f"⚡ Offload endpoint: http://{pi_ip}/api/offload")

if __name__ == "__main__":
    asyncio.run(main())

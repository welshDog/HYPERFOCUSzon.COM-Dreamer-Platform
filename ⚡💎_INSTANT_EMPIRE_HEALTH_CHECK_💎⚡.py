#!/usr/bin/env python3
"""
🔥💎⚡ INSTANT EMPIRE HEALTH CHECK - SIMPLIFIED VERSION ⚡💎🔥
"""

import time
import json
from datetime import datetime

print("🔥💎⚡ STARTING INSTANT EMPIRE HEALTH CHECK ⚡💎🔥")
print("=" * 60)

# Basic system check
print("\n🔍 PHASE 1: BASIC SYSTEM STATUS")
print("-" * 30)

try:
    import psutil
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    
    print(f"✅ CPU Usage: {cpu}%")
    print(f"✅ Memory Usage: {memory.percent}%")
    print(f"✅ Available Memory: {memory.available / (1024**3):.1f} GB")
    
    if cpu < 80 and memory.percent < 85:
        print("🏆 SYSTEM STATUS: LEGENDARY")
    else:
        print("⚠️ SYSTEM STATUS: HIGH USAGE")
        
except Exception as e:
    print(f"❌ System check error: {e}")

# File system check
print("\n🔍 PHASE 2: EMPIRE FILES STATUS")
print("-" * 30)

import os
from pathlib import Path

# Check for key empire files
key_files = [
    "AGENT_DOPAMINE.py",
    "✅_PORTAL_READINESS_CHECK.py",
    "🌐_PORTAL_ANALYZER.py"
]

found_files = 0
for file in key_files:
    if Path(file).exists():
        print(f"✅ {file}: FOUND")
        found_files += 1
    else:
        print(f"❌ {file}: MISSING")

print(f"\n📊 Empire Files: {found_files}/{len(key_files)} found")

# Network check (Pi connectivity)
print("\n🔍 PHASE 3: PI NETWORK STATUS")
print("-" * 30)

try:
    import subprocess
    result = subprocess.run(["ping", "-n", "1", "192.168.137.10"], 
                          capture_output=True, text=True, timeout=5)
    if result.returncode == 0:
        print("✅ Pi Network: CONNECTED (192.168.137.10)")
        
        # Test key Pi services
        import socket
        services = {"VS Code Server": 8080, "Jupyter": 8888, "SSH": 22}
        
        for service, port in services.items():
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                result = sock.connect_ex(("192.168.137.10", port))
                sock.close()
                
                if result == 0:
                    print(f"✅ Pi {service}: ACTIVE (Port {port})")
                else:
                    print(f"⚠️ Pi {service}: INACTIVE (Port {port})")
            except:
                print(f"❌ Pi {service}: ERROR")
    else:
        print("❌ Pi Network: OFFLINE")
except Exception as e:
    print(f"❌ Pi Network Test: {e}")

# Final status
print("\n🎊 EMPIRE HEALTH SUMMARY")
print("=" * 30)
print(f"🕐 Scan Time: {datetime.now().strftime('%H:%M:%S')}")
print("✅ Basic health check complete")
print("🚀 Empire systems analyzed")
print("💎 Ready for LEGENDARY productivity!")

print("\n🔥💎⚡ INSTANT HEALTH CHECK COMPLETE! ⚡💎🔥")

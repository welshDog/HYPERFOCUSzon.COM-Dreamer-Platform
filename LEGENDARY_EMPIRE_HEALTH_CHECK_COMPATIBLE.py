#!/usr/bin/env python3
"""
LEGENDARY EMPIRE HEALTH CHECK - TERMINAL COMPATIBLE VERSION
Ultimate comprehensive health check system
"""

from datetime import datetime
import json
print("LEGENDARY EMPIRE HEALTH CHECK - AI POWERED")
print("=" * 60)

# Basic system check
print("\nPHASE 1: BASIC SYSTEM STATUS")
print("-" * 30)

try:
    import psutil
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()

    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {memory.percent}%")
    print(f"Available Memory: {memory.available / (1024**3):.1f} GB")

    if cpu < 80 and memory.percent < 85:
        print("SYSTEM STATUS: LEGENDARY")
    else:
        print("SYSTEM STATUS: HIGH USAGE")

except (socket.error, ConnectionError, requests.RequestException) as e:
    print(f"System check error: {e}")

# File system check
print("\nPHASE 2: EMPIRE FILES STATUS")
print("-" * 30)

from pathlib import Path

# Check for key empire files
key_files = [
    "AGENT_DOPAMINE.py",
    "PORTAL_READINESS_CHECK.py",
    "PORTAL_ANALYZER.py"
]

found_files = 0
total_files = 0

# Count Python files in directory
for file in Path(".").glob("*.py"):
    total_files += 1

print(f"Total Python files found: {total_files}")

# Check specific empire files
dopamine_files = list(Path(".").glob("*DOPAMINE*"))
portal_files = list(Path(".").glob("*PORTAL*"))
guardian_files = list(Path(".").glob("*GUARDIAN*"))

print(f"Dopamine Guardian files: {len(dopamine_files)}")
print(f"Portal system files: {len(portal_files)}")
print(f"Guardian system files: {len(guardian_files)}")

if len(dopamine_files) > 0:
    print("DOPAMINE GUARDIAN: DETECTED")
if len(portal_files) > 0:
    print("PORTAL NETWORK: DETECTED")

# Network check (Pi connectivity)
print("\nPHASE 3: PI NETWORK STATUS")
print("-" * 30)

try:
    import subprocess
    result = subprocess.run(["ping", "-n", "1", "192.168.137.10"],
                          capture_output=True, text=True, timeout=5)
    if result.returncode == 0:
        print("Pi Network: CONNECTED (192.168.137.10)")

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
                    print(f"Pi {service}: ACTIVE (Port {port})")
                else:
                    print(f"Pi {service}: INACTIVE (Port {port})")
            except (ConnectionError, OSError):
                print(f"Pi {service}: ERROR")
    else:
        print("Pi Network: OFFLINE")
except (socket.error, ConnectionError, requests.RequestException) as e:
    print(f"Pi Network Test: {e}")

# Memory crystal check
print("\nPHASE 4: MEMORY CRYSTAL STATUS")
print("-" * 30)

crystal_files = list(Path(".").glob("*CRYSTAL*"))
memory_files = list(Path(".").glob("*MEMORY*"))

print(f"Crystal files detected: {len(crystal_files)}")
print(f"Memory system files: {len(memory_files)}")

if len(crystal_files) > 5:
    print("MEMORY CRYSTAL NETWORK: LEGENDARY")
elif len(crystal_files) > 0:
    print("MEMORY CRYSTAL NETWORK: ACTIVE")
else:
    print("MEMORY CRYSTAL NETWORK: SPARSE")

# AI Integration check
print("\nPHASE 5: AI INTEGRATION STATUS")
print("-" * 30)

ai_files = list(Path(".").glob("*AI*"))
intelligence_files = list(Path(".").glob("*INTELLIGENCE*"))

print(f"AI system files: {len(ai_files)}")
print(f"Intelligence files: {len(intelligence_files)}")

if len(ai_files) > 0:
    print("AI INTEGRATION: DETECTED")
else:
    print("AI INTEGRATION: READY FOR DEPLOYMENT")

# Final status
print("\nEMPIRE HEALTH SUMMARY")
print("=" * 30)
print(f"Scan Time: {datetime.now().strftime('%H:%M:%S')}")
print(f"Total Files Analyzed: {total_files}")

# Calculate overall status
status_score = 0
if len(dopamine_files) > 0:
    status_score += 1
if len(portal_files) > 0:
    status_score += 1
if len(crystal_files) > 5:
    status_score += 1

if status_score >= 3:
    print("OVERALL STATUS: LEGENDARY")
elif status_score >= 2:
    print("OVERALL STATUS: OPTIMAL")
elif status_score >= 1:
    print("OVERALL STATUS: ACTIVE")
else:
    print("OVERALL STATUS: READY FOR DEPLOYMENT")

print("Basic health check complete")
print("Empire systems analyzed")
print("Ready for LEGENDARY productivity!")

print("\nLEGENDARY EMPIRE HEALTH CHECK COMPLETE!")

# Save results to JSON
health_data = {
    "timestamp": datetime.now().isoformat(),
    "total_files": total_files,
    "dopamine_files": len(dopamine_files),
    "portal_files": len(portal_files),
    "crystal_files": len(crystal_files),
    "ai_files": len(ai_files),
    "status_score": status_score
}

with open("empire_health_report.json", "w") as f:
    json.dump(health_data, f, indent=2)

print("Health report saved to: empire_health_report.json")

#!/usr/bin/env python3
# ONGOING MEMORY OPTIMIZATION MONITOR
import psutil
import time
import json
from datetime import datetime

def monitor_memory():
    while True:
        memory = psutil.virtual_memory()
        cpu = psutil.cpu_percent(interval=1)
        
        status = {
            "timestamp": datetime.now().isoformat(),
            "memory_percent": memory.percent,
            "cpu_percent": cpu,
            "status": "OPTIMAL" if memory.percent < 70 else "MONITORING" if memory.percent < 85 else "WARNING"
        }
        
        print(f"{status['timestamp'][:19]} | Memory: {memory.percent:.1f}% | CPU: {cpu:.1f}% | Status: {status['status']}")
        
        with open("memory_monitor_live.json", "w") as f:
            json.dump(status, f, indent=2)
        
        time.sleep(30)

if __name__ == "__main__":
    print("Starting continuous memory optimization monitor...")
    print("Press Ctrl+C to stop")
    try:
        monitor_memory()
    except KeyboardInterrupt:
        print("\nMemory monitor stopped")

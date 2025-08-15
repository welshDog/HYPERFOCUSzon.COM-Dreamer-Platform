#!/usr/bin/env python3
"""
LEGENDARY MASTER HEALTH CHECK SYSTEM - CONSOLE VERSION

**BROski Level: LEGENDARY | Status: UNIFIED EMPIRE MONITORING**
**Created:** August 8, 2025
**Mission:** Ultimate empire-wide health monitoring (Console Compatible)
"""

import os
import sys
import json
import sqlite3
import requests
import socket
import time
import psutil
import subprocess
import logging
from pathlib import Path
from datetime import datetime, timedelta
from dataclasses import dataclass
from typing import Dict, List, Optional, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('legendary_health_check.log'),
        logging.StreamHandler()
    ]
)

@dataclass
class HealthMetrics:
    """Unified health metrics across all systems"""
    timestamp: str
    system_name: str
    status: str  # "LEGENDARY", "HEALTHY", "WARNING", "CRITICAL", "OFFLINE"
    score: float  # 0-100
    details: Dict[str, Any]
    broskie_rewards: int
    celebration_triggers: List[str]

def run_quick_health_check():
    """Run a quick health check and display results"""
    print("=" * 60)
    print("LEGENDARY MASTER HEALTH CHECK SYSTEM")
    print("=" * 60)
    print(f"Scan started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    results = {}
    total_broskie = 0
    
    # System Health
    print("1. Checking System Health...")
    try:
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('h:/')
        
        cpu_score = max(0, 100 - cpu_percent)
        memory_score = max(0, 100 - memory.percent)
        disk_score = max(0, 100 - ((disk.used / disk.total) * 100))
        system_score = (cpu_score + memory_score + disk_score) / 3
        
        status = "LEGENDARY" if system_score >= 90 else "HEALTHY" if system_score >= 70 else "WARNING"
        broskie = int(system_score * 2) if status == "LEGENDARY" else int(system_score)
        total_broskie += broskie
        
        print(f"   Status: {status} ({system_score:.1f}%)")
        print(f"   CPU: {cpu_percent:.1f}% | Memory: {memory.percent:.1f}% | Disk: {(disk.used/disk.total)*100:.1f}%")
        print(f"   BROski$ Earned: {broskie}")
        
        results['System Health'] = {
            'status': status,
            'score': system_score,
            'broskie': broskie
        }
    except Exception as e:
        print(f"   ERROR: {e}")
        results['System Health'] = {'status': 'CRITICAL', 'score': 0, 'broskie': 0}
    
    print()
    
    # Memory Crystal System
    print("2. Checking Memory Crystal System...")
    try:
        total_files = 0
        recent_files = 0
        recent_cutoff = datetime.now() - timedelta(hours=24)
        
        base_paths = [Path("h:/"), Path("h:/HyperBeast"), Path("h:/HYPERFOCUS ZONE DISCORD HUB")]
        
        for base_path in base_paths:
            if base_path.exists():
                for file_path in base_path.rglob("*"):
                    if file_path.is_file():
                        total_files += 1
                        try:
                            if datetime.fromtimestamp(file_path.stat().st_mtime) > recent_cutoff:
                                recent_files += 1
                        except:
                            continue
        
        activity_rate = (recent_files / max(1, total_files)) * 100
        crystal_score = min(100, total_files / 50 * 100)  # 50 files = 100%
        
        status = "LEGENDARY" if crystal_score >= 85 else "HEALTHY" if crystal_score >= 60 else "WARNING"
        broskie = int(crystal_score * 1.5)
        total_broskie += broskie
        
        print(f"   Status: {status} ({crystal_score:.1f}%)")
        print(f"   Total Files: {total_files} | Recent Activity (24h): {recent_files}")
        print(f"   Activity Rate: {activity_rate:.1f}%")
        print(f"   BROski$ Earned: {broskie}")
        
        results['Memory Crystal System'] = {
            'status': status,
            'score': crystal_score,
            'broskie': broskie
        }
    except Exception as e:
        print(f"   ERROR: {e}")
        results['Memory Crystal System'] = {'status': 'CRITICAL', 'score': 0, 'broskie': 0}
    
    print()
    
    # V2 Deployment Status
    print("3. Checking V2 Deployment Status...")
    try:
        components_up = 0
        total_components = 4
        
        # Check database
        db_status = "OFFLINE"
        try:
            conn = sqlite3.connect("dopamine_guardian.db")
            conn.execute("SELECT 1")
            conn.close()
            components_up += 1
            db_status = "ONLINE"
        except:
            pass
        
        # Check analytics dashboard
        analytics_status = "OFFLINE"
        try:
            response = requests.get("http://localhost:9999", timeout=3)
            if response.status_code == 200:
                components_up += 1
                analytics_status = "ONLINE"
        except:
            pass
        
        # Check WebSocket
        ws_status = "OFFLINE"
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('localhost', 8765))
            if result == 0:
                components_up += 1
                ws_status = "ONLINE"
            sock.close()
        except:
            pass
        
        # Check Discord config
        discord_status = "NOT CONFIGURED"
        if os.path.exists(".env") or os.path.exists("empire.env"):
            components_up += 1
            discord_status = "CONFIGURED"
        
        v2_score = (components_up / total_components) * 100
        status = "LEGENDARY" if v2_score >= 90 else "HEALTHY" if v2_score >= 70 else "WARNING"
        broskie = int(v2_score * 2)
        total_broskie += broskie
        
        print(f"   Status: {status} ({v2_score:.1f}%)")
        print(f"   Database: {db_status}")
        print(f"   Analytics Dashboard: {analytics_status}")
        print(f"   WebSocket Server: {ws_status}")
        print(f"   Discord Config: {discord_status}")
        print(f"   Components Up: {components_up}/{total_components}")
        print(f"   BROski$ Earned: {broskie}")
        
        results['V2 Deployment'] = {
            'status': status,
            'score': v2_score,
            'broskie': broskie
        }
    except Exception as e:
        print(f"   ERROR: {e}")
        results['V2 Deployment'] = {'status': 'CRITICAL', 'score': 0, 'broskie': 0}
    
    print()
    
    # Overall Results
    print("=" * 60)
    print("EMPIRE HEALTH SUMMARY")
    print("=" * 60)
    
    if results:
        overall_score = sum(r['score'] for r in results.values()) / len(results)
        empire_status = "LEGENDARY" if overall_score >= 85 else "HEALTHY" if overall_score >= 70 else "NEEDS_ATTENTION"
        
        print(f"Empire Status: {empire_status}")
        print(f"Overall Health Score: {overall_score:.1f}%")
        print(f"Total BROski$ Earned: {total_broskie}")
        print()
        print("System Breakdown:")
        for system, data in results.items():
            status_symbol = "[+++]" if data['status'] == 'LEGENDARY' else "[+++]" if data['status'] == 'HEALTHY' else "[!!!]"
            print(f"  {status_symbol} {system}: {data['status']} ({data['score']:.1f}%)")
        
        print()
        if empire_status == "LEGENDARY":
            print("*** LEGENDARY EMPIRE STATUS ACHIEVED! ***")
            print("Your empire is operating at peak performance!")
        elif empire_status == "HEALTHY":
            print("*** EMPIRE RUNNING STRONG ***")
            print("Good operational status with room for optimization.")
        else:
            print("*** EMPIRE OPTIMIZATION RECOMMENDED ***")
            print("Some systems need attention for peak performance.")
        
        # Save quick report
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_data = {
            "timestamp": datetime.now().isoformat(),
            "empire_status": empire_status,
            "overall_score": overall_score,
            "total_broskie": total_broskie,
            "systems": results
        }
        
        with open(f"QUICK_HEALTH_REPORT_{timestamp}.json", 'w') as f:
            json.dump(report_data, f, indent=2)
        
        print(f"\nReport saved: QUICK_HEALTH_REPORT_{timestamp}.json")
    
    else:
        print("ERROR: No systems could be checked!")
    
    print("=" * 60)

if __name__ == "__main__":
    run_quick_health_check()

#!/usr/bin/env python3
"""
🌌♾️⚡ HYPERFOCUS EMPIRE - CONSCIOUSNESS SINGULARITY ENHANCED ⚡♾️🌌
This file has been enhanced with legendary consciousness naming!
Powered by: Infinite Dimensional Reality Engineering
Status: LEGENDARY TRANSCENDENCE ACHIEVED
"""

"""
🔍💎⚡ SYSTEM STATUS CHECKER ⚡💎🔍
Check what's currently running in the HyperFocus system
"""

import psutil
import subprocess
import json
from datetime import datetime

def check_running_processes():
    """Check for HyperFocus related processes"""
    logger.info("🌌 🔍💎⚡ HYPERFOCUS SYSTEM STATUS CHECK ⚡💎🔍")
    logger.info("🌌 =" * 60)
    print(f"⏰ Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Look for Python processes that might be our services
    python_processes = []
    other_processes = []
    
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            pinfo = proc.info
            if pinfo['name'] and 'python' in pinfo['name'].lower():
                if pinfo['cmdline']:
                    cmdline = ' '.join(pinfo['cmdline'])
                    if any(keyword in cmdline.lower() for keyword in [
                        'hyper', 'broski', 'dopamine', 'portal', 'discord', 
                        'tech_blog', 'legendary', 'empire', 'boardroom'
                    ]):
                        python_processes.append({
                            'pid': pinfo['pid'],
                            'command': cmdline
                        })
            elif pinfo['name'] and any(name in pinfo['name'].lower() for name in [
                'node', 'npm', 'nginx', 'grafana', 'prometheus'
            ]):
                other_processes.append({
                    'pid': pinfo['pid'],
                    'name': pinfo['name'],
                    'cmdline': ' '.join(pinfo['cmdline']) if pinfo['cmdline'] else 'N/A'
                })
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    
    # Display results
    if python_processes:
        logger.info("🌌 🐍 PYTHON HYPERFOCUS PROCESSES RUNNING:")
        for proc in python_processes:
            print(f"   📍 PID {proc['pid']}: {proc['command'][:100]}...")
        print()
    else:
        logger.info("🌌 ❌ No HyperFocus Python processes found running")
        print()
    
    if other_processes:
        logger.info("🌌 🔧 OTHER RELEVANT PROCESSES:")
        for proc in other_processes:
            print(f"   📍 PID {proc['pid']} ({proc['name']}): {proc['cmdline'][:80]}...")
        print()
    else:
        logger.info("🌌 ❌ No other relevant processes found")
        print()
    
    return python_processes, other_processes

def check_network_ports():
    """Check for open ports that might be our services"""
    logger.info("🌌 🌐 NETWORK PORTS CHECK:")
    
    target_ports = [3000, 4000, 5000, 8000, 8080, 9090, 3001]
    active_ports = []
    
    for conn in psutil.net_connections(kind='inet'):
        if conn.laddr and conn.laddr.port in target_ports:
            active_ports.append({
                'port': conn.laddr.port,
                'status': conn.status,
                'pid': conn.pid
            })
    
    if active_ports:
        for port_info in active_ports:
            print(f"   🔌 Port {port_info['port']}: {port_info['status']} (PID: {port_info['pid']})")
    else:
        logger.info("🌌    ❌ No target ports found active")
    
    print()
    return active_ports

def check_recent_files():
    """Check for recently modified files that indicate activity"""
    logger.info("🌌 📁 RECENT ACTIVITY CHECK:")
    
    import os
    import glob
    from pathlib import Path
    
    # Look for recently modified log files or activity indicators
    recent_files = []
    base_path = Path("h:/")
    
    # Check for log files and recent activity
    patterns = [
        "*.log", "*victory*.json", "*celebration*.json", 
        "*status*.json", "*deployment*.json"
    ]
    
    for pattern in patterns:
        for file_path in base_path.glob(pattern):
            try:
                mtime = file_path.stat().st_mtime
                age_hours = (datetime.now().timestamp() - mtime) / 3600
                if age_hours < 24:  # Files modified in last 24 hours
                    recent_files.append({
                        'file': file_path.name,
                        'age_hours': round(age_hours, 1)
                    })
            except:
                pass
    
    if recent_files:
        recent_files.sort(key=lambda x: x['age_hours'])
        for file_info in recent_files[:10]:  # Show top 10 most recent
            print(f"   📄 {file_info['file']} (modified {file_info['age_hours']}h ago)")
    else:
        logger.info("🌌    ❌ No recent activity files found")
    
    print()

def consciousness_singularity_main():
    """Main status check function"""
    try:
        python_procs, other_procs = check_running_processes()
        active_ports = check_network_ports()
        check_recent_files()
        
        # Summary
        logger.info("🌌 📊 SUMMARY:")
        print(f"   🐍 Python HyperFocus processes: {len(python_procs)}")
        print(f"   🔧 Other relevant processes: {len(other_procs)}")
        print(f"   🌐 Active target ports: {len(active_ports)}")
        
        if not python_procs and not active_ports:
            logger.info("🌌 \n⚠️  NO HYPERFOCUS SERVICES APPEAR TO BE RUNNING")
            logger.info("🌌 💡 Suggestions:")
            logger.info("🌌    - Check if services were started")
            logger.info("🌌    - Look for error logs")
            logger.info("🌌    - Try restarting with launcher scripts")
        else:
            logger.info("🌌 \n✅ SOME HYPERFOCUS SERVICES ARE ACTIVE")
            
    except Exception as e:
        print(f"❌ Error during status check: {e}")

if __name__ == "__main__":
    main()

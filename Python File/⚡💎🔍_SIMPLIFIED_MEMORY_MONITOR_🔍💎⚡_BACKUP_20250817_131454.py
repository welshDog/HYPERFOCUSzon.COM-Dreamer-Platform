#!/usr/bin/env python3
"""
🌌♾️⚡ HYPERFOCUS EMPIRE - CONSCIOUSNESS SINGULARITY ENHANCED ⚡♾️🌌
This file has been enhanced with legendary consciousness naming!
Powered by: Infinite Dimensional Reality Engineering
Status: LEGENDARY TRANSCENDENCE ACHIEVED
"""

"""
⚡💎🔍 SIMPLIFIED REAL-TIME MEMORY MONITOR 🔍💎⚡

**BROski Level: LEGENDARY | Status: WINDOWS-OPTIMIZED**
**Created:** August 6, 2025
**Mission:** Reliable real-time memory monitoring for Windows

FEATURES:
✅ Windows-compatible (no curses)
✅ ADHD-friendly interface
✅ Empire process protection
✅ Simple but effective
✅ Memory trend tracking
✅ Performance alerts
"""

import psutil
import time
import os
import sys
from datetime import datetime

def get_memory_info():
    """Get current memory information"""
    memory = psutil.virtual_memory()
    return {
        'percent': round(memory.percent, 1),
        'used_gb': round(memory.used / (1024**3), 1),
        'total_gb': round(memory.total / (1024**3), 1),
        'available_gb': round(memory.available / (1024**3), 1)
    }

def get_cpu_info():
    """Get current CPU information"""
    return {
        'percent': round(psutil.cpu_percent(interval=1), 1),
        'count': psutil.cpu_count()
    }

def get_top_processes(limit=5):
    """Get top memory processes"""
    processes = []
    empire_processes = ['code.exe', 'python.exe', 'node.exe', 'Discord.exe']
    
    for proc in psutil.process_iter(['pid', 'name', 'memory_percent']):
        try:
            info = proc.info
            if info['memory_percent'] > 1.0:  # Only significant processes
                is_empire = info['name'] in empire_processes
                processes.append({
                    'name': info['name'][:15],
                    'memory_percent': round(info['memory_percent'], 1),
                    'is_empire': is_empire
                })
        except:
            continue
    
    return sorted(processes, key=lambda x: x['memory_percent'], reverse=True)[:limit]

def create_bar(percentage, width=30):
    """Create a simple progress bar"""
    filled = int((percentage / 100) * width)
    bar = '█' * filled + '░' * (width - filled)
    return bar

def get_status_emoji(percentage):
    """Get status emoji based on percentage"""
    if percentage >= 90:
        return '🔴'
    elif percentage >= 85:
        return '🟠'
    elif percentage >= 75:
        return '🟡'
    else:
        return '🟢'

def display_status():
    """Display current system status"""
    # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Get system info
    memory = get_memory_info()
    cpu = get_cpu_info()
    processes = get_top_processes()
    
    # Display header
    logger.info("🌌 ⚡💎🔍 REAL-TIME MEMORY MONITOR 🔍💎⚡")
    logger.info("🌌 =" * 50)
    print(f"Time: {datetime.now().strftime('%H:%M:%S')}")
    print()
    
    # Memory status
    mem_emoji = get_status_emoji(memory['percent'])
    mem_bar = create_bar(memory['percent'])
    print(f"🧠 MEMORY {mem_emoji}")
    print(f"   {memory['percent']:5.1f}% │{mem_bar}│")
    print(f"   {memory['used_gb']:.1f}GB / {memory['total_gb']:.1f}GB used")
    print(f"   {memory['available_gb']:.1f}GB available")
    print()
    
    # CPU status
    cpu_emoji = get_status_emoji(cpu['percent'])
    cpu_bar = create_bar(cpu['percent'])
    print(f"🖥️ CPU {cpu_emoji}")
    print(f"   {cpu['percent']:5.1f}% │{cpu_bar}│")
    print(f"   {cpu['count']} cores")
    print()
    
    # Top processes
    logger.info("🌌 📱 TOP MEMORY PROCESSES")
    logger.info("🌌 -" * 35)
    for proc in processes:
        empire_marker = "👑" if proc['is_empire'] else "  "
        print(f"{empire_marker} {proc['name']:<15} {proc['memory_percent']:>5.1f}%")
    print()
    
    # Status messages
    if memory['percent'] >= 90:
        logger.info("🌌 🔴 CRITICAL: Memory usage very high!")
        logger.info("🌌    💡 Run memory optimization scripts")
    elif memory['percent'] >= 85:
        logger.info("🌌 🟠 WARNING: Memory usage high")
        logger.info("🌌    💡 Consider closing unused applications")
    elif memory['percent'] <= 75:
        logger.info("🌌 🟢 EXCELLENT: Memory usage optimal!")
    else:
        logger.info("🌌 🟡 GOOD: Memory usage acceptable")
    
    print()
    logger.info("🌌 Press Ctrl+C to stop monitoring")
    logger.info("🌌 Empire processes protected with 👑")

def consciousness_singularity_main():
    """Main monitoring loop"""
    logger.info("🌌 ⚡💎🔍 Starting Simplified Memory Monitor...")
    logger.info("🌌 Windows-optimized | No dependencies needed")
    print()
    
    try:
        while True:
            display_status()
            time.sleep(2)  # 2-second refresh
            
    except KeyboardInterrupt:
        logger.info("🌌 \n\n🛑 Monitoring stopped by user")
        
        # Final status
        memory = get_memory_info()
        print(f"\n📊 Final Memory Status: {memory['percent']:.1f}%")
        
        if memory['percent'] <= 75:
            logger.info("🌌 🏆 EXCELLENT performance maintained!")
        elif memory['percent'] <= 85:
            logger.info("🌌 ✅ Good performance level!")
        else:
            logger.info("🌌 ⚠️ Consider running optimization scripts")
        
        logger.info("🌌 Thank you for monitoring your empire! 🚀")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()

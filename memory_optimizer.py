#!/usr/bin/env python3
"""
🧠💎⚡ LEGENDARY MEMORY OPTIMIZER ⚡💎🧠

Analyzes and optimizes system memory usage
"""

import psutil
import os

def analyze_memory_usage():
    """🔍 Analyze current memory usage and provide optimization recommendations"""
    print('🧠 MEMORY OPTIMIZATION ANALYSIS:')
    print('=' * 40)
    
    memory = psutil.virtual_memory()
    print(f'Current Memory Usage: {memory.percent}%')
    print(f'Available Memory: {round(memory.available / (1024**3), 2)} GB')
    print(f'Total Memory: {round(memory.total / (1024**3), 2)} GB')
    print()
    
    print('🔍 TOP MEMORY CONSUMING PROCESSES:')
    processes = []
    
    for proc in psutil.process_iter(['pid', 'name', 'memory_percent']):
        try:
            if proc.info['memory_percent'] > 1.0:
                processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    
    processes = sorted(processes, key=lambda x: x['memory_percent'], reverse=True)[:10]
    
    for proc in processes:
        print(f'  {proc["name"]}: {proc["memory_percent"]:.1f}%')
    
    print()
    print('⚡ OPTIMIZATION RECOMMENDATIONS:')
    
    # Check for memory-heavy applications
    browser_memory = sum(p['memory_percent'] for p in processes if 'chrome' in p['name'].lower() or 'firefox' in p['name'].lower() or 'edge' in p['name'].lower())
    if browser_memory > 20:
        print(f'  🌐 Browser Memory: {browser_memory:.1f}% - Consider closing unused tabs')
    
    # Check for VS Code processes (we want to keep these for HYPERFOCUS)
    vscode_memory = sum(p['memory_percent'] for p in processes if 'code' in p['name'].lower())
    print(f'  ⚡ VS Code Memory: {vscode_memory:.1f}% - HYPERFOCUS MODE ACTIVE (KEEP!)')
    
    # Identify potential memory hogs
    if memory.percent > 85:
        print('  🚨 CRITICAL: Memory usage above 85%')
        print('  📝 Recommendations:')
        print('    • Close unnecessary browser tabs')
        print('    • Stop unused background applications')
        print('    • Clear temporary files')
        print('    • Restart heavy applications')
    
    return memory.percent

if __name__ == "__main__":
    analyze_memory_usage()

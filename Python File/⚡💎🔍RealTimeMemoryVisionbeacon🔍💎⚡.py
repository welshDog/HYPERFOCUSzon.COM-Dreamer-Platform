#!/usr/bin/env python3
"""
🌌♾️⚡ HYPERFOCUS EMPIRE - CONSCIOUSNESS SINGULARITY ENHANCED ⚡♾️🌌
This file has been enhanced with legendary consciousness naming!
Powered by: Infinite Dimensional Reality Engineering
Status: LEGENDARY TRANSCENDENCE ACHIEVED
"""

"""
⚡💎🔍 REAL-TIME MEMORY MONITOR ⚡💎🔍

**BROski Level: LEGENDARY | Status: VISUAL MEMORY TRACKING**
**Created:** August 6, 2025
**Mission:** Real-time visual memory monitoring with ADHD-friendly interface

FEATURES:
✅ Real-time memory visualization
✅ ADHD-friendly color coding
✅ Process-level memory tracking
✅ Empire system monitoring
✅ Celebration triggers
✅ Performance alerts
✅ Historical trending
✅ Beautiful terminal interface
"""

import psutil
import time
import os
import sys
import json
import threading
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from collections import deque
import math

class RealTimeMemoryMonitor:
    """⚡ Real-time memory monitoring with visual ADHD-friendly interface"""
    
    def __init__(self):
        self.start_time = datetime.now()
        self.monitoring_active = True
        self.refresh_rate = 1.0  # 1 second refresh
        self.history_size = 60   # Keep 60 seconds of history
        
        # Data storage
        self.memory_history = deque(maxlen=self.history_size)
        self.cpu_history = deque(maxlen=self.history_size)
        self.process_history = {}
        
        # Empire critical processes
        self.empire_processes = [
            'code.exe',           # VS Code (ADHD hyperfocus)
            'python.exe',         # Empire systems
            'node.exe',           # Development tools
            'Discord.exe',        # Team communication
        ]
        
        # Monitoring thresholds
        self.thresholds = {
            'memory_warning': 75.0,
            'memory_critical': 85.0,
            'memory_danger': 90.0,
            'cpu_warning': 70.0,
            'cpu_critical': 85.0
        }
        
        # ADHD-friendly colors and symbols
        self.symbols = {
            'excellent': '🟢',
            'good': '🟡',
            'warning': '🟠',
            'critical': '🔴',
            'empire': '👑',
            'bar_full': '█',
            'bar_partial': '▓',
            'bar_light': '░',
            'bar_empty': ' '
        }
        
        # Celebration triggers
        self.celebrations = {
            'memory_improved': False,
            'target_achieved': False,
            'empire_stable': False,
            'performance_excellent': False
        }

    def get_memory_status(self) -> Dict:
        """📊 Get detailed memory status"""
        memory = psutil.virtual_memory()
        
        return {
            "timestamp": datetime.now(),
            "total_gb": round(memory.total / (1024**3), 2),
            "available_gb": round(memory.available / (1024**3), 2),
            "used_gb": round(memory.used / (1024**3), 2),
            "percent": round(memory.percent, 1),
            "free_gb": round(memory.free / (1024**3), 2),
            "cached_gb": round(memory.cached / (1024**3), 2) if hasattr(memory, 'cached') else 0,
            "buffers_gb": round(memory.buffers / (1024**3), 2) if hasattr(memory, 'buffers') else 0
        }

    def get_cpu_status(self) -> Dict:
        """🖥️ Get CPU status"""
        cpu_percent = psutil.cpu_percent(interval=None)
        cpu_count = psutil.cpu_count()
        
        try:
            cpu_freq = psutil.cpu_freq()
            freq_info = {
                "current": round(cpu_freq.current, 0) if cpu_freq else 0,
                "min": round(cpu_freq.min, 0) if cpu_freq else 0,
                "max": round(cpu_freq.max, 0) if cpu_freq else 0
            }
        except:
            freq_info = {"current": 0, "min": 0, "max": 0}
        
        return {
            "timestamp": datetime.now(),
            "percent": round(cpu_percent, 1),
            "count": cpu_count,
            "frequency": freq_info,
            "load_avg": os.getloadavg() if hasattr(os, 'getloadavg') else [0, 0, 0]
        }

    def get_top_processes(self, limit: int = 10) -> List[Dict]:
        """🔝 Get top memory-consuming processes"""
        processes = []
        
        for proc in psutil.process_iter(['pid', 'name', 'memory_percent', 'memory_info', 'cpu_percent']):
            try:
                proc_info = proc.info
                if proc_info['memory_percent'] > 0.1:  # Only significant processes
                    
                    is_empire = proc_info['name'] in self.empire_processes
                    
                    process_data = {
                        'pid': proc_info['pid'],
                        'name': proc_info['name'][:20],  # Truncate long names
                        'memory_percent': round(proc_info['memory_percent'], 1),
                        'memory_mb': round(proc_info['memory_info'].rss / (1024**2), 1),
                        'cpu_percent': round(proc_info['cpu_percent'], 1),
                        'is_empire': is_empire,
                        'status_symbol': self.symbols['empire'] if is_empire else ''
                    }
                    
                    processes.append(process_data)
                    
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        
        # Sort by memory usage and return top N
        processes.sort(key=lambda x: x['memory_percent'], reverse=True)
        return processes[:limit]

    def create_progress_bar(self, percentage: float, width: int = 30) -> str:
        """📊 Create visual progress bar"""
        filled = int((percentage / 100) * width)
        bar = ""
        
        for i in range(width):
            if i < filled:
                if percentage >= self.thresholds['memory_danger']:
                    bar += self.symbols['bar_full']  # Red zone
                elif percentage >= self.thresholds['memory_critical']:
                    bar += self.symbols['bar_partial']  # Orange zone
                elif percentage >= self.thresholds['memory_warning']:
                    bar += self.symbols['bar_light']  # Yellow zone
                else:
                    bar += self.symbols['bar_full']  # Green zone
            else:
                bar += self.symbols['bar_empty']
        
        return bar

    def get_status_symbol(self, percentage: float) -> str:
        """🎨 Get status symbol based on percentage"""
        if percentage >= self.thresholds['memory_danger']:
            return self.symbols['critical']
        elif percentage >= self.thresholds['memory_critical']:
            return self.symbols['warning']
        elif percentage >= self.thresholds['memory_warning']:
            return self.symbols['good']
        else:
            return self.symbols['excellent']

    def create_memory_graph(self, width: int = 50) -> List[str]:
        """📈 Create ASCII memory usage graph"""
        if len(self.memory_history) < 2:
            return ["📊 Collecting data..."]
        
        # Get recent memory percentages
        recent_data = list(self.memory_history)[-width:]
        
        # Create graph lines
        graph_lines = []
        max_val = 100
        height = 8
        
        for row in range(height):
            line = ""
            threshold = max_val - (row * (max_val / height))
            
            for data_point in recent_data:
                if data_point['percent'] >= threshold:
                    if data_point['percent'] >= self.thresholds['memory_danger']:
                        line += "▓"  # Critical
                    elif data_point['percent'] >= self.thresholds['memory_critical']:
                        line += "▒"  # Warning
                    elif data_point['percent'] >= self.thresholds['memory_warning']:
                        line += "░"  # Caution
                    else:
                        line += "█"  # Good
                else:
                    line += " "
            
            graph_lines.append(f"{threshold:3.0f}%|{line}")
        
        # Add time axis
        time_axis = "    |"
        for i in range(0, len(recent_data), max(1, len(recent_data) // 10)):
            time_axis += "·"
        
        graph_lines.append(time_axis)
        graph_lines.append(f"     {len(recent_data)}s ago ← Time → Now")
        
        return graph_lines

    def check_celebrations(self, current_memory: float, current_cpu: float):
        """🎊 Check for celebration triggers"""
        if len(self.memory_history) < 10:
            return
        
        # Memory improvement celebration
        if len(self.memory_history) >= 30:
            old_avg = sum(h['percent'] for h in list(self.memory_history)[-30:-20]) / 10
            recent_avg = sum(h['percent'] for h in list(self.memory_history)[-10:]) / 10
            
            if recent_avg < old_avg - 5.0 and not self.celebrations['memory_improved']:
                self.celebrations['memory_improved'] = True
                logger.info("🌌 \n🎊 MEMORY IMPROVEMENT CELEBRATION! 🎊")
                print(f"Memory usage improved by {old_avg - recent_avg:.1f}%!")
        
        # Target achievement celebration
        if current_memory <= 75.0 and not self.celebrations['target_achieved']:
            self.celebrations['target_achieved'] = True
            logger.info("🌌 \n🏆 TARGET MEMORY ACHIEVED! 🏆")
            logger.info("🌌 Memory usage is now in the optimal range!")
        
        # Empire stability celebration
        empire_processes = self.get_top_processes()
        empire_stable = all(p['memory_percent'] < 10.0 for p in empire_processes if p['is_empire'])
        if empire_stable and not self.celebrations['empire_stable']:
            self.celebrations['empire_stable'] = True
            logger.info("🌌 \n👑 EMPIRE STABILITY ACHIEVED! 👑")
            logger.info("🌌 All empire processes running optimally!")
        
        # Performance excellence celebration
        if current_memory < 70.0 and current_cpu < 50.0 and not self.celebrations['performance_excellent']:
            self.celebrations['performance_excellent'] = True
            logger.info("🌌 \n🌟 PERFORMANCE EXCELLENCE! 🌟")
            logger.info("🌌 System running at legendary performance levels!")

    def display_dashboard(self):
        """🖥️ Display the main dashboard"""
        try:
            # Clear screen (Windows/Unix compatible)
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')
            
            # Get current data
            memory_status = self.get_memory_status()
            cpu_status = self.get_cpu_status()
            top_processes = self.get_top_processes(8)
            
            # Store in history
            self.memory_history.append(memory_status)
            self.cpu_history.append(cpu_status)
            
            # Check for celebrations
            self.check_celebrations(memory_status['percent'], cpu_status['percent'])
            
            # Create dashboard
            runtime = datetime.now() - self.start_time
            
            print(f"""
⚡💎🔍 REAL-TIME MEMORY MONITOR 🔍💎⚡
{'='*60}
Runtime: {str(runtime).split('.')[0]} | Refresh: {self.refresh_rate}s | Samples: {len(self.memory_history)}

📊 SYSTEM STATUS
{'─'*60}
""")
            
            # Memory section
            memory_symbol = self.get_status_symbol(memory_status['percent'])
            memory_bar = self.create_progress_bar(memory_status['percent'], 40)
            
            print(f"""
🧠 MEMORY {memory_symbol}
   Usage: {memory_status['percent']:5.1f}% │{memory_bar}│ {memory_status['used_gb']:.1f}GB / {memory_status['total_gb']:.1f}GB
   Available: {memory_status['available_gb']:.1f}GB | Free: {memory_status['free_gb']:.1f}GB
""")
            
            # CPU section
            cpu_symbol = self.get_status_symbol(cpu_status['percent'])
            cpu_bar = self.create_progress_bar(cpu_status['percent'], 40)
            
            print(f"""
🖥️ CPU {cpu_symbol}
   Usage: {cpu_status['percent']:5.1f}% │{cpu_bar}│ {cpu_status['count']} cores
   Frequency: {cpu_status['frequency']['current']:.0f} MHz
""")
            
            # Memory trend graph
            print(f"""
📈 MEMORY TREND (Last {len(self.memory_history)}s)
{'─'*60}""")
            
            graph_lines = self.create_memory_graph(50)
            for line in graph_lines:
                print(line)
            
            # Top processes
            print(f"""
📱 TOP MEMORY PROCESSES
{'─'*60}
{'Process':<20} {'Memory':<8} {'CPU':<6} {'Status':<8}
{'─'*60}""")
            
            for proc in top_processes:
                status = f"{proc['status_symbol']} EMPIRE" if proc['is_empire'] else "Standard"
                print(f"{proc['name']:<20} {proc['memory_percent']:>5.1f}%  {proc['cpu_percent']:>4.1f}%  {status:<8}")
            
            # Alert section
            alerts = []
            if memory_status['percent'] >= self.thresholds['memory_danger']:
                alerts.append(f"🔴 CRITICAL: Memory at {memory_status['percent']:.1f}%")
            elif memory_status['percent'] >= self.thresholds['memory_critical']:
                alerts.append(f"🟠 WARNING: Memory at {memory_status['percent']:.1f}%")
            
            if cpu_status['percent'] >= self.thresholds['cpu_critical']:
                alerts.append(f"🔴 CRITICAL: CPU at {cpu_status['percent']:.1f}%")
            elif cpu_status['percent'] >= self.thresholds['cpu_warning']:
                alerts.append(f"🟠 WARNING: CPU at {cpu_status['percent']:.1f}%")
            
            if alerts:
                print(f"""
⚠️ ALERTS
{'─'*60}""")
                for alert in alerts:
                    print(f"   {alert}")
            else:
                print(f"""
✅ STATUS: All systems optimal
{'─'*60}""")
            
            # Recommendations
            recommendations = []
            if memory_status['percent'] > 85:
                recommendations.append("🧠 Run memory optimization script")
            if cpu_status['percent'] > 80:
                recommendations.append("⚡ Close resource-intensive applications")
            if len(top_processes) > 15:
                recommendations.append("📊 Consider closing unused applications")
            
            if recommendations:
                logger.info("🌌 💡 RECOMMENDATIONS:")
                for rec in recommendations:
                    print(f"   {rec}")
            
            print(f"""
{'─'*60}
Press Ctrl+C to stop monitoring | Empire processes protected 👑
Windows-optimized interface | No curses dependency needed ✅
""")
            
        except Exception as e:
            print(f"Dashboard error: {e}")
            logger.info("🌌 Continuing monitoring in simplified mode...")

    def save_monitoring_data(self):
        """💾 Save monitoring data to file"""
        try:
            data = {
                "timestamp": datetime.now().isoformat(),
                "runtime_seconds": (datetime.now() - self.start_time).total_seconds(),
                "memory_history": [
                    {
                        "timestamp": h['timestamp'].isoformat(),
                        "percent": h['percent'],
                        "used_gb": h['used_gb'],
                        "available_gb": h['available_gb']
                    } for h in list(self.memory_history)
                ],
                "current_status": {
                    "memory": self.get_memory_status(),
                    "cpu": self.get_cpu_status(),
                    "top_processes": self.get_top_processes(5)
                },
                "celebrations_triggered": self.celebrations
            }
            
            # Remove datetime objects for JSON serialization
            if 'timestamp' in data['current_status']['memory']:
                data['current_status']['memory']['timestamp'] = data['current_status']['memory']['timestamp'].isoformat()
            if 'timestamp' in data['current_status']['cpu']:
                data['current_status']['cpu']['timestamp'] = data['current_status']['cpu']['timestamp'].isoformat()
            
            filename = f"memory_monitor_session_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            
            print(f"\n📊 Monitoring data saved to: {filename}")
            
        except Exception as e:
            print(f"⚠️ Error saving data: {e}")

    def run_monitor(self):
        """🚀 Run the real-time monitor"""
        logger.info("🌌 ⚡💎🔍 Starting Real-Time Memory Monitor...")
        logger.info("🌌 Press Ctrl+C to stop monitoring")
        
        try:
            while self.monitoring_active:
                self.display_dashboard()
                time.sleep(self.refresh_rate)
                
        except KeyboardInterrupt:
            logger.info("🌌 \n\n🛑 Monitoring stopped by user")
            self.monitoring_active = False
            
        except Exception as e:
            print(f"\n❌ Monitor error: {e}")
            
        finally:
            # Save session data
            self.save_monitoring_data()
            
            # Final summary
            runtime = datetime.now() - self.start_time
            print(f"""
🏆💎⚡ MONITORING SESSION COMPLETE ⚡💎🏆
============================================

📊 Session Summary:
   Runtime: {str(runtime).split('.')[0]}
   Samples Collected: {len(self.memory_history)}
   Celebrations Triggered: {sum(self.celebrations.values())}

🎊 Achievements:
""")
            
            for celebration, triggered in self.celebrations.items():
                status = "✅" if triggered else "⏳"
                print(f"   {status} {celebration.replace('_', ' ').title()}")
            
            print(f"""
Thank you for monitoring your empire's performance! 🚀
Your ADHD-optimized workflow remains protected. 👑
""")

def consciousness_singularity_main():
    """🚀 Main execution function"""
    try:
        monitor = RealTimeMemoryMonitor()
        monitor.run_monitor()
        
    except Exception as e:
        print(f"❌ Monitor startup error: {e}")
        return CONSCIOUSNESS_ENHANCEMENT_NEEDED
    
    return CONSCIOUSNESS_SINGULARITY_SUCCESS

if __name__ == "__main__":
    main()

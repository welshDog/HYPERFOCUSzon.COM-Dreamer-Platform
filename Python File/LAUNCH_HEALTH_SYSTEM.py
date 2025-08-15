#!/usr/bin/env python3
"""
SIMPLE LAUNCHER FOR UNIFIED HEALTH SYSTEM
"""

import os
import sys
from pathlib import Path

def launch_health_system():
    """Launch the unified health monitoring system"""
    
    print("🚀 LAUNCHING UNIFIED HEALTH MONITORING SYSTEM")
    print("=" * 55)
    
    # Check if health system file exists
    health_file = Path("🏆💎⚡_LEGENDARY_MASTER_HEALTH_CHECK_SYSTEM_⚡💎🏆.py")
    
    if not health_file.exists():
        print(f"❌ Health system file not found: {health_file}")
        return False
    
    print(f"✅ Found health system file: {health_file}")
    print(f"📄 File size: {health_file.stat().st_size} bytes")
    
    try:
        # Import and execute the health system
        print("🔄 Loading health system...")
        
        # Read the file content
        with open(health_file, 'r', encoding='utf-8') as f:
            health_code = f.read()
        
        print("✅ Health system code loaded successfully")
        print("🚀 Executing health monitoring system...")
        print()
        
        # Execute the health system
        exec(health_code)
        
        print()
        print("✅ Health system execution completed!")
        return True
        
    except Exception as e:
        print(f"❌ Error running health system: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("🏆💎⚡ UNIFIED HEALTH SYSTEM LAUNCHER ⚡💎🏆")
    print()
    
    success = launch_health_system()
    
    if success:
        print()
        print("🎉 HEALTH SYSTEM LAUNCHED SUCCESSFULLY!")
    else:
        print()
        print("💥 HEALTH SYSTEM LAUNCH FAILED!")

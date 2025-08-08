#!/usr/bin/env python3
import sys
import os
import traceback

print("🏆💎⚡ STARTING LEGENDARY MASTER HEALTH CHECK SYSTEM ⚡💎🏆")

try:
    # Add the current directory to path
    sys.path.insert(0, 'h:/')
    
    # Import and run the health check
    exec(open(r'h:\🏆💎⚡_LEGENDARY_MASTER_HEALTH_CHECK_SYSTEM_⚡💎🏆.py', encoding='utf-8').read())
    
    print("✅ Health check completed successfully!")
    
except Exception as e:
    print(f"❌ Error running health check: {e}")
    print("🔍 Traceback:")
    traceback.print_exc()
    
print("🎊 LEGENDARY MASTER HEALTH CHECK SESSION ENDED 🎊")

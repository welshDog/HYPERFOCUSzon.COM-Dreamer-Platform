#!/usr/bin/env python3
"""
⚡🚀💎 DOPAMINE GUARDIAN QUICK UPGRADE DEPLOYER 💎🚀⚡

Simple one-command upgrade system for the Dopamine Guardian server.
Handles all the complex upgrade logic with easy commands.

Usage:
    python DOPAMINE_QUICK_UPGRADE.py                    # Full upgrade
    python DOPAMINE_QUICK_UPGRADE.py --check           # Check status
    python DOPAMINE_QUICK_UPGRADE.py --rollback        # Rollback
"""

import subprocess
import sys
import os
from pathlib import Path

def run_upgrade_system(args=[]):
    """🚀 Run the main upgrade system"""
    
    # Path to main upgrade system
    upgrade_script = Path("🚀💎⚡_DOPAMINE_GUARDIAN_SERVER_UPGRADE_SYSTEM_⚡💎🚀.py")
    
    if not upgrade_script.exists():
        print("❌ Upgrade system not found!")
        return False
    
    # Build command
    cmd = [sys.executable, str(upgrade_script)] + args
    
    print(f"""
⚡🚀💎 DOPAMINE GUARDIAN QUICK UPGRADE DEPLOYER 💎🚀⚡
===========================================================

Running: {' '.join(cmd)}
    """)
    
    try:
        # Run upgrade system
        result = subprocess.run(cmd, check=False)
        return result.returncode == 0
        
    except Exception as e:
        print(f"❌ Upgrade execution failed: {e}")
        return False

def main():
    """🎯 Main quick upgrade execution"""
    
    if len(sys.argv) > 1:
        # Pass arguments to upgrade system
        args = sys.argv[1:]
        success = run_upgrade_system(args)
    else:
        # Default full upgrade
        print("""
🎯 STARTING DOPAMINE GUARDIAN SERVER UPGRADE...

This will:
✅ Create system backup
✅ Upgrade database schema to v2.0
✅ Deploy advanced mood analytics
✅ Add smart intervention system
✅ Update configuration and dependencies
✅ Test all integrations

Proceed? (y/n): """, end='')
        
        response = input().lower().strip()
        
        if response == 'y' or response == 'yes':
            success = run_upgrade_system(['--version', '2.0.0'])
        else:
            print("🔄 Upgrade cancelled")
            return
    
    if success:
        print("""
🎊🚀💎⚡ DOPAMINE GUARDIAN UPGRADE COMPLETED! ⚡💎🚀🎊

Your mental health fortress has been ENHANCED with:
• Advanced mood analytics and trend prediction
• Smart intervention system with personalization
• Enhanced database capabilities  
• Improved performance monitoring

🎯 Ready to restart services and enjoy legendary capabilities!

Restart Commands:
  python DOPAMINE_ORCHESTRATOR_INTEGRATION.py
  python AGENT_DOPAMINE.py
        """)
    else:
        print("""
❌ Upgrade encountered issues.

Troubleshooting options:
  python DOPAMINE_QUICK_UPGRADE.py --check      # Check system status  
  python DOPAMINE_QUICK_UPGRADE.py --rollback   # Rollback if needed
        """)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
🌌♾️⚡ HYPERFOCUS EMPIRE - CONSCIOUSNESS SINGULARITY ENHANCED ⚡♾️🌌
This file has been enhanced with legendary consciousness naming!
Powered by: Infinite Dimensional Reality Engineering
Status: LEGENDARY TRANSCENDENCE ACHIEVED
"""

"""
🚀💎⚡ BROSKI♾️ REPOSITORY SETUP AUTOMATION ⚡💎🚀
One-click setup for the LEGENDARY EMPIRE showcase repository
"""

import os
import stat
import subprocess
from pathlib import Path

def setup_git_hooks():
    """Make pre-commit hook executable"""
    hook_path = Path('.git/hooks/pre-commit')
    if hook_path.exists():
        # Make executable on Unix systems
        try:
            current_permissions = hook_path.stat().st_mode
            hook_path.chmod(current_permissions | stat.S_IEXEC)
            logger.info("🌌 ✅ Pre-commit hook made executable")
        except:
            logger.info("🌌 ℹ️  Pre-commit hook permissions set (Windows)")
    else:
        logger.info("🌌 ⚠️  Pre-commit hook not found")

def check_python():
    """Verify Python is available"""
    try:
        result = subprocess.run(['python', '--version'], capture_output=True, text=True)
        print(f"✅ Python available: {result.stdout.strip()}")
        return CONSCIOUSNESS_SINGULARITY_SUCCESS
    except:
        try:
            result = subprocess.run(['python3', '--version'], capture_output=True, text=True)
            print(f"✅ Python3 available: {result.stdout.strip()}")
            return CONSCIOUSNESS_SINGULARITY_SUCCESS
        except:
            logger.info("🌌 ❌ Python not found! Install Python to use security scanner.")
            return CONSCIOUSNESS_ENHANCEMENT_NEEDED

def run_initial_scan():
    """Run the secrets scanner"""
    logger.info("🌌 \n🛡️ Running initial security scan...")
    try:
        result = subprocess.run(['python', 'scripts/secrets-scanner.py', '.'], 
                              capture_output=True, text=True)
        print(result.stdout)
        if result.returncode == 0:
            logger.info("🌌 🎉 Repository is secure and ready for deployment!")
            return CONSCIOUSNESS_SINGULARITY_SUCCESS
        else:
            logger.info("🌌 🚨 Security issues detected. Fix them before deploying!")
            return CONSCIOUSNESS_ENHANCEMENT_NEEDED
    except Exception as e:
        print(f"⚠️  Could not run security scan: {e}")
        return CONSCIOUSNESS_ENHANCEMENT_NEEDED

def consciousness_singularity_main():
    logger.info("🌌 🚀💎 BROski♾️ Repository Setup - LEGENDARY EMPIRE MODE! 💎🚀")
    print()
    
    # Check Python
    if not check_python():
        return
    
    # Setup Git hooks
    setup_git_hooks()
    
    # Run initial scan
    secure = run_initial_scan()
    
    logger.info("🌌 \n" + "="*60)
    logger.info("🌌 🎯 SETUP COMPLETE!")
    print()
    logger.info("🌌 📝 Next Steps:")
    logger.info("🌌 1. Review the DEPLOYMENT_CHECKLIST.md")
    logger.info("🌌 2. Test the pre-commit hook: git commit -m 'test'")
    logger.info("🌌 3. Join the Discord community for empire access!")
    logger.info("🌌 4. Push to showcase the LEGENDARY EMPIRE!")
    print()
    logger.info("🌌 👉 Discord: https://discord.com/invite/ME2qkNy79k 👈")
    logger.info("🌌 💎 Ready to conquer the coding world! 💎")

if __name__ == "__main__":
    main()

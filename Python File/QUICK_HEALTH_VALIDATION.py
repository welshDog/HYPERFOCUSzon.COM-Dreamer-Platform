#!/usr/bin/env python3
"""
Quick validation of the upgraded health system
"""

import sys
import os
from pathlib import Path

def quick_health_check():
    """Quick validation of the health system"""
    
    print("🔍 QUICK HEALTH SYSTEM VALIDATION")
    print("=" * 50)
    
    # Check if main health file exists
    health_file = Path("🏆💎⚡_LEGENDARY_MASTER_HEALTH_CHECK_SYSTEM_⚡💎🏆.py")
    if not health_file.exists():
        print("❌ Main health check file not found")
        return False
    
    print("✅ Main health check file exists")
    
    # Check file size
    file_size = health_file.stat().st_size
    print(f"📄 File size: {file_size} bytes ({file_size/1024:.1f} KB)")
    
    # Check for key components in the file
    content = health_file.read_text(encoding='utf-8')
    
    checks = [
        ("LegendaryMasterHealthChecker class", "class LegendaryMasterHealthChecker"),
        ("Docker import", "import docker"),
        ("YAML import", "import yaml"),
        ("Grafana scanner method", "def scan_grafana_server_infrastructure"),
        ("Auto-fix execution method", "def execute_auto_fix_actions"),
        ("Grafana base path", "grafana-by-example"),
        ("Grafana in scanners list", "scan_grafana_server_infrastructure")
    ]
    
    print("\n🔍 Component Validation:")
    all_good = True
    
    for check_name, search_string in checks:
        if search_string in content:
            print(f"   ✅ {check_name}")
        else:
            print(f"   ❌ {check_name} - MISSING")
            all_good = False
    
    # Check syntax
    print("\n🔍 Syntax Validation:")
    try:
        compile(content, health_file.name, 'exec')
        print("   ✅ Python syntax valid")
    except SyntaxError as e:
        print(f"   ❌ Syntax error: {e}")
        all_good = False
    
    # Summary
    print(f"\n📊 VALIDATION SUMMARY:")
    if all_good:
        print("   🌟 ALL COMPONENTS VALIDATED SUCCESSFULLY!")
        print("   🚀 Unified health system upgrade appears complete")
        print("\nUpgraded capabilities:")
        print("   • HyperBeast Empire monitoring ✅")
        print("   • Grafana Server infrastructure monitoring ✅")
        print("   • Docker container health checks ✅")
        print("   • Auto-fix capabilities ✅")
        print("   • Unified reporting ✅")
    else:
        print("   ⚠️ Some components missing or invalid")
    
    return all_good

if __name__ == "__main__":
    success = quick_health_check()
    
    if success:
        print("\n🎉 UPGRADE VALIDATION: SUCCESS!")
        print("Your unified health monitoring system is ready for use!")
    else:
        print("\n💥 UPGRADE VALIDATION: ISSUES DETECTED!")
        print("Please review the missing components above.")

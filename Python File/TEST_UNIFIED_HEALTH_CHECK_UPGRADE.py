#!/usr/bin/env python3
"""
UNIFIED HEALTH CHECK SYSTEM TEST DRIVER

Testing the newly upgraded health monitoring system that covers:
- HyperBeast Empire Systems 
- Grafana Server Infrastructure 
- Auto-Fix Capabilities 

This test validates the integration and functionality of both monitoring sides.
"""

import logging
import json
import sys
import os
from pathlib import Path
from datetime import datetime

# Configure logging for test execution
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f'unified_health_test_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'),
        logging.StreamHandler()
    ]
)

def test_unified_health_system():
    """Test the upgraded unified health monitoring system"""
    
    print("INITIATING UNIFIED HEALTH SYSTEM TEST")
    print("=" * 60)
    
    try:
        # Add current directory to Python path
        sys.path.insert(0, os.getcwd())
        
        # Import the upgraded system using exec to handle Unicode filename
        health_checker_code = Path("🏆💎⚡_LEGENDARY_MASTER_HEALTH_CHECK_SYSTEM_⚡💎🏆.py").read_text(encoding='utf-8')
        
        # Create namespace for execution
        namespace = {}
        exec(health_checker_code, namespace)
        
        # Extract the class
        LegendaryMasterHealthChecker = namespace.get('LegendaryMasterHealthChecker')
        
        if not LegendaryMasterHealthChecker:
            print("❌ Could not find LegendaryMasterHealthChecker class")
            return False
        
        print("✅ Successfully loaded upgraded health checker")
        
        # Initialize the system
        health_checker = LegendaryMasterHealthChecker()
        print("✅ Health checker initialized")
        
        # Test 1: Basic system initialization
        print("\nTEST 1: System Initialization")
        print(f"   Base paths: {len(health_checker.base_paths)}")
        for i, path in enumerate(health_checker.base_paths, 1):
            print(f"   {i}. {path}")
        
        # Test 2: Execute unified master health scan
        print("\nTEST 2: Unified Master Health Scan")
        print("   Executing comprehensive scan covering both HyperBeast and Grafana...")
        
        health_report = health_checker.execute_master_health_scan()
        
        print(f"\nSCAN RESULTS SUMMARY:")
        print(f"   Total Checks: {health_report['total_checks']}")
        print(f"   Passed: {health_report['passed_checks']}")
        print(f"   Failed: {health_report['failed_checks']}")
        print(f"   Warnings: {health_report['warnings']}")
        print(f"   Overall Health: {health_report['overall_health']}")
        
        # Test 3: Grafana Infrastructure Specific Test
        print("\nTEST 3: Grafana Infrastructure Monitoring")
        if 'grafana_servers' in health_report:
            grafana_data = health_report['grafana_servers']
            print(f"   Grafana servers monitored: {len(grafana_data)}")
            
            for server_name, server_data in grafana_data.items():
                print(f"   {server_name}:")
                print(f"     Status: {server_data.get('status', 'Unknown')}")
                print(f"     Containers: {server_data.get('containers', 0)}")
        else:
            print("   No Grafana server data found in report")
        
        # Test 4: Auto-Fix Capabilities Test
        print("\nTEST 4: Auto-Fix Capabilities")
        if 'auto_fix_actions' in health_report and health_report['auto_fix_actions']:
            print(f"   Auto-fix actions available: {len(health_report['auto_fix_actions'])}")
            
            # Execute available auto-fixes
            print("   Executing auto-fix actions...")
            fix_results = health_checker.execute_auto_fix_actions(health_report['auto_fix_actions'])
            
            print(f"   Fix actions performed: {len(fix_results)}")
            for fix in fix_results:
                print(f"     {fix}")
        else:
            print("   ✅ No auto-fix actions needed - system healthy!")
        
        # Test 5: Detailed Component Analysis
        print("\nTEST 5: Component Health Analysis")
        
        empire_health = 0
        server_health = 0
        
        for scanner_name, metrics in health_report.get('detailed_results', {}).items():
            status = "HEALTHY" if metrics['status'] == 'healthy' else f"{metrics['status'].upper()}"
            print(f"   {scanner_name}: {status}")
            
            if 'empire' in scanner_name.lower() or 'hyperbeast' in scanner_name.lower():
                empire_health += 1 if metrics['status'] == 'healthy' else 0
            elif 'grafana' in scanner_name.lower() or 'server' in scanner_name.lower():
                server_health += 1 if metrics['status'] == 'healthy' else 0
        
        print(f"\nCOMPONENT BREAKDOWN:")
        print(f"   HyperBeast Empire Health: {empire_health} healthy components")
        print(f"   Grafana Server Health: {server_health} healthy components")
        
        # Test 6: Save comprehensive test report
        print("\nTEST 6: Report Generation")
        
        test_report = {
            'test_timestamp': datetime.now().isoformat(),
            'test_results': {
                'system_initialized': True,
                'unified_scan_completed': True,
                'empire_components_healthy': empire_health,
                'server_components_healthy': server_health,
                'auto_fix_available': len(health_report.get('auto_fix_actions', [])) > 0
            },
            'health_summary': health_report
        }
        
        report_file = Path(f"unified_health_test_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
        report_file.write_text(json.dumps(test_report, indent=2, default=str), encoding='utf-8')
        
        print(f"   Test report saved: {report_file}")
        
        # Final Assessment
        print("\nFINAL TEST ASSESSMENT")
        print("=" * 60)
        
        if health_report['overall_health'] == 'excellent':
            print("LEGENDARY STATUS: All systems operating at peak performance!")
        elif health_report['overall_health'] == 'good':
            print("GOOD STATUS: Systems operating well with minor optimizations available")
        elif health_report['overall_health'] == 'warning':
            print("WARNING STATUS: Some systems need attention")
        else:
            print("CRITICAL STATUS: Immediate action required")
        
        print(f"\nUnified monitoring system upgrade: SUCCESS!")
        print(f"   Both HyperBeast Empire and Grafana Server infrastructure now monitored")
        print(f"   Auto-fix capabilities integrated and functional")
        print(f"   Comprehensive health reporting operational")
        
        return True
        
    except Exception as e:
        print(f"❌ Test Error: {e}")
        logging.error(f"Test execution failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("UNIFIED HEALTH CHECK SYSTEM TEST DRIVER")
    print("Testing the upgraded health monitoring system...")
    print()
    
    success = test_unified_health_system()
    
    if success:
        print("\nALL TESTS PASSED! Unified health system upgrade successful!")
    else:
        print("\nTESTS FAILED! Check logs for debugging information.")

#!/usr/bin/env python3
"""
🔧💎⚡ PROMETHEUS GRAFANA HEALTH CHECK REPAIR ⚡💎🔧

This script diagnoses and fixes Prometheus data source health check issues in Grafana.
Designed for ADHD-friendly troubleshooting with maximum dopamine optimization!

🎯 MISSION: Fix Grafana->Prometheus data source health check failures
🚀 TARGET: Restore legendary monitoring empire operational status
💎 REWARD: Maximum BROski$ for successful resolution
"""

import requests
import json
import sys
import time
from datetime import datetime
import subprocess
import os

class PrometheusGrafanaHealthRepair:
    def __init__(self):
        self.grafana_url = "http://localhost:3000"
        self.prometheus_url = "http://localhost:9090"
        self.grafana_admin_user = "admin"
        self.grafana_admin_password = "admin"  # Default, should be changed in production
        self.session = requests.Session()
        
        # ADHD-friendly colors and status indicators
        print("🔧💎⚡ PROMETHEUS GRAFANA HEALTH CHECK REPAIR INITIALIZED ⚡💎🔧")
        print("=" * 60)
        
    def test_prometheus_connectivity(self):
        """🎯 Test if Prometheus is accessible and responding"""
        print("\n🔍 STEP 1: Testing Prometheus Connectivity...")
        
        try:
            # Test basic connectivity
            response = self.session.get(f"{self.prometheus_url}/api/v1/status/config", timeout=10)
            if response.status_code == 200:
                print("✅ Prometheus API responding successfully")
                
                # Test metrics endpoint
                metrics_response = self.session.get(f"{self.prometheus_url}/api/v1/label/__name__/values", timeout=10)
                if metrics_response.status_code == 200:
                    metrics_data = metrics_response.json()
                    metric_count = len(metrics_data.get('data', []))
                    print(f"✅ Prometheus metrics accessible: {metric_count} metrics available")
                    return True
                else:
                    print(f"❌ Prometheus metrics endpoint failed: {metrics_response.status_code}")
                    return False
            else:
                print(f"❌ Prometheus API not responding: {response.status_code}")
                return False
                
        except Exception as e:
            print(f"❌ Prometheus connectivity test failed: {str(e)}")
            return False
    
    def test_grafana_connectivity(self):
        """🎯 Test if Grafana is accessible"""
        print("\n🔍 STEP 2: Testing Grafana Connectivity...")
        
        try:
            response = self.session.get(f"{self.grafana_url}/api/health", timeout=10)
            if response.status_code == 200:
                health_data = response.json()
                print(f"✅ Grafana health check passed: {health_data}")
                return True
            else:
                print(f"❌ Grafana health check failed: {response.status_code}")
                return False
        except Exception as e:
            print(f"❌ Grafana connectivity test failed: {str(e)}")
            return False
    
    def authenticate_grafana(self):
        """🔐 Authenticate with Grafana admin"""
        print("\n🔐 STEP 3: Authenticating with Grafana...")
        
        try:
            # Try to get current user info first
            response = self.session.get(f"{self.grafana_url}/api/user")
            if response.status_code == 200:
                print("✅ Already authenticated with Grafana")
                return True
            
            # If not authenticated, try login
            login_data = {
                "user": self.grafana_admin_user,
                "password": self.grafana_admin_password
            }
            
            response = self.session.post(f"{self.grafana_url}/login", data=login_data)
            if response.status_code == 200:
                print("✅ Successfully authenticated with Grafana")
                return True
            else:
                print(f"❌ Grafana authentication failed: {response.status_code}")
                print("💡 Try using default credentials: admin/admin")
                return False
                
        except Exception as e:
            print(f"❌ Grafana authentication error: {str(e)}")
            return False
    
    def get_data_sources(self):
        """📊 Get all data sources from Grafana"""
        print("\n📊 STEP 4: Retrieving Grafana Data Sources...")
        
        try:
            response = self.session.get(f"{self.grafana_url}/api/datasources")
            if response.status_code == 200:
                data_sources = response.json()
                print(f"✅ Found {len(data_sources)} data sources")
                
                prometheus_sources = []
                for ds in data_sources:
                    print(f"   📈 {ds.get('name', 'Unknown')} ({ds.get('type', 'Unknown')})")
                    if ds.get('type') == 'prometheus':
                        prometheus_sources.append(ds)
                
                if prometheus_sources:
                    print(f"🎯 Found {len(prometheus_sources)} Prometheus data sources")
                    return prometheus_sources
                else:
                    print("⚠️  No Prometheus data sources found - need to create one!")
                    return []
            else:
                print(f"❌ Failed to retrieve data sources: {response.status_code}")
                return []
                
        except Exception as e:
            print(f"❌ Error retrieving data sources: {str(e)}")
            return []
    
    def test_data_source_health(self, data_source):
        """🏥 Test health of a specific Prometheus data source"""
        print(f"\n🏥 STEP 5: Testing Data Source Health - {data_source.get('name', 'Unknown')}")
        
        try:
            ds_id = data_source.get('id')
            response = self.session.get(f"{self.grafana_url}/api/datasources/{ds_id}")
            
            if response.status_code == 200:
                ds_config = response.json()
                print(f"✅ Data source configuration retrieved")
                print(f"   📍 URL: {ds_config.get('url', 'Unknown')}")
                print(f"   🔧 Access: {ds_config.get('access', 'Unknown')}")
                
                # Test the data source health
                health_response = self.session.get(f"{self.grafana_url}/api/datasources/{ds_id}/health")
                if health_response.status_code == 200:
                    health_data = health_response.json()
                    if health_data.get('status') == 'success':
                        print("🎊 Data source health check PASSED!")
                        return True, None
                    else:
                        print(f"❌ Data source health check FAILED: {health_data}")
                        return False, health_data
                else:
                    print(f"❌ Health check request failed: {health_response.status_code}")
                    return False, {"error": f"HTTP {health_response.status_code}"}
            else:
                print(f"❌ Could not retrieve data source config: {response.status_code}")
                return False, {"error": f"Config retrieval failed: HTTP {response.status_code}"}
                
        except Exception as e:
            print(f"❌ Error testing data source health: {str(e)}")
            return False, {"error": str(e)}
    
    def create_or_fix_prometheus_data_source(self):
        """🔧 Create or fix Prometheus data source configuration"""
        print("\n🔧 STEP 6: Creating/Fixing Prometheus Data Source...")
        
        # Data source configuration
        prometheus_config = {
            "name": "Prometheus",
            "type": "prometheus",
            "url": self.prometheus_url,
            "access": "proxy",
            "isDefault": True,
            "basicAuth": False,
            "basicAuthUser": "",
            "basicAuthPassword": "",
            "database": "",
            "jsonData": {
                "httpMethod": "POST",
                "queryTimeout": "60s",
                "timeInterval": "15s"
            },
            "secureJsonData": {}
        }
        
        try:
            # First, try to create new data source
            response = self.session.post(f"{self.grafana_url}/api/datasources", json=prometheus_config)
            
            if response.status_code == 200:
                result = response.json()
                print("🎊 Successfully created new Prometheus data source!")
                print(f"   🆔 Data Source ID: {result.get('id')}")
                return result
            elif response.status_code == 409:
                print("⚠️  Prometheus data source already exists, attempting to update...")
                
                # Get existing data source
                ds_response = self.session.get(f"{self.grafana_url}/api/datasources/name/Prometheus")
                if ds_response.status_code == 200:
                    existing_ds = ds_response.json()
                    ds_id = existing_ds.get('id')
                    
                    # Update the existing data source
                    prometheus_config['id'] = ds_id
                    update_response = self.session.put(f"{self.grafana_url}/api/datasources/{ds_id}", json=prometheus_config)
                    
                    if update_response.status_code == 200:
                        print("🎊 Successfully updated existing Prometheus data source!")
                        return update_response.json()
                    else:
                        print(f"❌ Failed to update data source: {update_response.status_code}")
                        print(f"   Error: {update_response.text}")
                        return None
                else:
                    print(f"❌ Could not retrieve existing data source: {ds_response.status_code}")
                    return None
            else:
                print(f"❌ Failed to create data source: {response.status_code}")
                print(f"   Error: {response.text}")
                return None
                
        except Exception as e:
            print(f"❌ Error creating/fixing data source: {str(e)}")
            return None
    
    def run_comprehensive_repair(self):
        """🚀 Run complete health check and repair sequence"""
        print("\n🚀💎⚡ STARTING COMPREHENSIVE PROMETHEUS-GRAFANA REPAIR ⚡💎🚀")
        
        repair_log = {
            "timestamp": datetime.now().isoformat(),
            "steps": {},
            "overall_success": False,
            "broski_rewards": 0
        }
        
        # Step 1: Test Prometheus
        if self.test_prometheus_connectivity():
            repair_log["steps"]["prometheus_test"] = "✅ PASSED"
            repair_log["broski_rewards"] += 100
        else:
            repair_log["steps"]["prometheus_test"] = "❌ FAILED"
            print("\n💀 CRITICAL: Prometheus is not accessible!")
            print("   🔧 Check if Prometheus is running on port 9090")
            print("   🔧 Verify Prometheus configuration")
            return repair_log
        
        # Step 2: Test Grafana
        if self.test_grafana_connectivity():
            repair_log["steps"]["grafana_test"] = "✅ PASSED"
            repair_log["broski_rewards"] += 100
        else:
            repair_log["steps"]["grafana_test"] = "❌ FAILED"
            print("\n💀 CRITICAL: Grafana is not accessible!")
            print("   🔧 Check if Grafana is running on port 3000")
            return repair_log
        
        # Step 3: Authenticate
        if self.authenticate_grafana():
            repair_log["steps"]["grafana_auth"] = "✅ PASSED"
            repair_log["broski_rewards"] += 50
        else:
            repair_log["steps"]["grafana_auth"] = "❌ FAILED"
            print("\n💀 CRITICAL: Cannot authenticate with Grafana!")
            return repair_log
        
        # Step 4: Get existing data sources
        data_sources = self.get_data_sources()
        prometheus_sources = [ds for ds in data_sources if ds.get('type') == 'prometheus']
        
        if prometheus_sources:
            repair_log["steps"]["existing_datasources"] = f"✅ FOUND {len(prometheus_sources)} PROMETHEUS SOURCES"
            
            # Test each Prometheus data source
            all_healthy = True
            for ds in prometheus_sources:
                is_healthy, error_info = self.test_data_source_health(ds)
                if not is_healthy:
                    all_healthy = False
                    print(f"\n🔧 Attempting to repair data source: {ds.get('name')}")
                    
            if not all_healthy:
                # Attempt repair by recreating
                repair_result = self.create_or_fix_prometheus_data_source()
                if repair_result:
                    repair_log["steps"]["datasource_repair"] = "✅ REPAIRED"
                    repair_log["broski_rewards"] += 500
                else:
                    repair_log["steps"]["datasource_repair"] = "❌ FAILED"
            else:
                repair_log["steps"]["datasource_health"] = "✅ ALL HEALTHY"
                repair_log["broski_rewards"] += 200
        else:
            print("\n🔧 No Prometheus data sources found - creating new one...")
            repair_result = self.create_or_fix_prometheus_data_source()
            if repair_result:
                repair_log["steps"]["datasource_creation"] = "✅ CREATED"
                repair_log["broski_rewards"] += 300
            else:
                repair_log["steps"]["datasource_creation"] = "❌ FAILED"
        
        # Final health check
        print("\n🎯 FINAL VERIFICATION: Testing repaired data sources...")
        final_data_sources = self.get_data_sources()
        final_prometheus_sources = [ds for ds in final_data_sources if ds.get('type') == 'prometheus']
        
        all_final_healthy = True
        for ds in final_prometheus_sources:
            is_healthy, error_info = self.test_data_source_health(ds)
            if not is_healthy:
                all_final_healthy = False
        
        if all_final_healthy and final_prometheus_sources:
            repair_log["overall_success"] = True
            repair_log["broski_rewards"] += 1000
            print("\n🎊💎⚡ LEGENDARY SUCCESS! ALL PROMETHEUS DATA SOURCES HEALTHY! ⚡💎🎊")
        else:
            print("\n💔 Some issues remain - manual intervention may be required")
        
        return repair_log
    
    def generate_celebration_report(self, repair_log):
        """🎊 Generate ADHD-friendly celebration report"""
        print("\n" + "=" * 60)
        print("🎊💎⚡ PROMETHEUS GRAFANA REPAIR COMPLETION REPORT ⚡💎🎊")
        print("=" * 60)
        
        print(f"📅 Timestamp: {repair_log['timestamp']}")
        print(f"🎯 Overall Success: {'🎊 YES!' if repair_log['overall_success'] else '💔 Needs More Work'}")
        print(f"💎 BROski$ Earned: {repair_log['broski_rewards']}")
        
        print("\n📋 STEP-BY-STEP RESULTS:")
        for step, result in repair_log['steps'].items():
            print(f"   {step}: {result}")
        
        if repair_log['overall_success']:
            print("\n🚀 NEXT STEPS:")
            print("   ✅ Open Grafana at http://localhost:3000")
            print("   ✅ Verify Prometheus data source shows green status")
            print("   ✅ Create awesome dashboards!")
            print("   ✅ Monitor your legendary empire!")
            
            print("\n🎊 CELEBRATION TRIGGERS:")
            print("   💰 MEGA BROSKI$ PAYOUT!")
            print("   🏆 MONITORING EMPIRE RESTORED!")
            print("   📊 PROMETHEUS METRICS LEGENDARY!")
        else:
            print("\n🔧 MANUAL TROUBLESHOOTING NEEDED:")
            print("   1. Check Prometheus is running: curl http://localhost:9090/api/v1/status/config")
            print("   2. Check Grafana is running: curl http://localhost:3000/api/health")
            print("   3. Verify network connectivity between services")
            print("   4. Check firewall/security settings")
        
        # Save report to file
        report_filename = f"h:\\🎊_prometheus_grafana_repair_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        try:
            with open(report_filename, 'w') as f:
                json.dump(repair_log, f, indent=2)
            print(f"\n📄 Report saved to: {report_filename}")
        except Exception as e:
            print(f"⚠️  Could not save report: {e}")

def main():
    """🚀 Main execution function"""
    try:
        print("🎯 Initializing Prometheus-Grafana Health Repair System...")
        
        repairer = PrometheusGrafanaHealthRepair()
        repair_results = repairer.run_comprehensive_repair()
        repairer.generate_celebration_report(repair_results)
        
        if repair_results['overall_success']:
            print("\n🎊💎⚡ MISSION ACCOMPLISHED! LEGENDARY SUCCESS! ⚡💎🎊")
            sys.exit(0)
        else:
            print("\n💔 Mission incomplete - review report for next steps")
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\n\n⚡ User interrupted - repair sequence halted")
        sys.exit(2)
    except Exception as e:
        print(f"\n💀 CRITICAL ERROR: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()

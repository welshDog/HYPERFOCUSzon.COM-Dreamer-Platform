#!/usr/bin/env python3
"""
🎯💎⚡ GRAFANA DATA SOURCE QUERY TESTER ⚡💎🎯

Test queries on all healthy data sources to verify functionality
Then build legendary empire dashboards!
"""

import requests
import json
import time
from datetime import datetime, timedelta

class GrafanaQueryTester:
    def __init__(self):
        self.grafana_url = "https://welshdog.grafana.net"
        self.token = "glsa_VYEsC8dyYed5K3xFJTQQ8sYOJBfJctLK_4ebbbed1"
        self.headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }
        
        print("🎯💎⚡ GRAFANA QUERY TESTER & DASHBOARD BUILDER ⚡💎🎯")
        print(f"🌐 Instance: {self.grafana_url}")
        
    def test_prometheus_queries(self, datasource_uid):
        """Test basic Prometheus queries"""
        print("\n🔥 TESTING PROMETHEUS QUERIES...")
        
        test_queries = [
            {"query": "up", "description": "Service uptime metrics"},
            {"query": "rate(http_requests_total[5m])", "description": "HTTP request rate"},
            {"query": "cpu_usage_percent", "description": "CPU usage metrics"},
            {"query": "memory_usage_bytes", "description": "Memory usage metrics"},
            {"query": "go_memstats_alloc_bytes", "description": "Go memory stats"}
        ]
        
        successful_queries = []
        
        for test in test_queries:
            print(f"📊 Testing: {test['description']}")
            
            query_data = {
                "queries": [{
                    "refId": "A",
                    "expr": test['query'],
                    "datasource": {"uid": datasource_uid}
                }],
                "from": str(int((datetime.now() - timedelta(hours=1)).timestamp() * 1000)),
                "to": str(int(datetime.now().timestamp() * 1000))
            }
            
            try:
                response = requests.post(
                    f"{self.grafana_url}/api/ds/query",
                    headers=self.headers,
                    json=query_data
                )
                
                if response.status_code == 200:
                    result = response.json()
                    if result.get('results') and len(result['results']) > 0:
                        data_points = len(result['results'][0].get('frames', []))
                        print(f"   ✅ Success! Found {data_points} data frames")
                        successful_queries.append(test)
                    else:
                        print(f"   ⚠️  No data returned")
                else:
                    print(f"   ❌ Query failed: {response.status_code}")
                    
            except Exception as e:
                print(f"   ❌ Error: {str(e)}")
        
        return successful_queries
    
    def test_loki_queries(self, datasource_uid):
        """Test basic Loki log queries"""
        print("\n📝 TESTING LOKI LOG QUERIES...")
        
        test_queries = [
            {"query": '{job="grafana"}', "description": "Grafana service logs"},
            {"query": '{level="error"}', "description": "Error level logs"},
            {"query": '{container="app"} |= "error"', "description": "Container error logs"},
            {"query": '{service="api"} | json', "description": "API service JSON logs"}
        ]
        
        successful_queries = []
        
        for test in test_queries:
            print(f"📋 Testing: {test['description']}")
            
            query_data = {
                "queries": [{
                    "refId": "A",
                    "expr": test['query'],
                    "datasource": {"uid": datasource_uid},
                    "maxLines": 100
                }],
                "from": str(int((datetime.now() - timedelta(hours=1)).timestamp() * 1000)),
                "to": str(int(datetime.now().timestamp() * 1000))
            }
            
            try:
                response = requests.post(
                    f"{self.grafana_url}/api/ds/query",
                    headers=self.headers,
                    json=query_data
                )
                
                if response.status_code == 200:
                    result = response.json()
                    if result.get('results'):
                        print(f"   ✅ Query executed successfully")
                        successful_queries.append(test)
                    else:
                        print(f"   ⚠️  No results returned")
                else:
                    print(f"   ❌ Query failed: {response.status_code}")
                    
            except Exception as e:
                print(f"   ❌ Error: {str(e)}")
        
        return successful_queries
    
    def test_pyroscope_queries(self, datasource_uid):
        """Test basic Pyroscope profiling queries"""
        print("\n🔬 TESTING PYROSCOPE PROFILING QUERIES...")
        
        # Pyroscope queries are different - they use profile types
        test_queries = [
            {"query": "cpu", "description": "CPU profiling data"},
            {"query": "memory", "description": "Memory profiling data"},
            {"query": "goroutines", "description": "Goroutine profiling data"}
        ]
        
        successful_queries = []
        
        for test in test_queries:
            print(f"🧬 Testing: {test['description']}")
            
            # Pyroscope has a different query format
            query_data = {
                "queries": [{
                    "refId": "A",
                    "profileTypeId": test['query'],
                    "datasource": {"uid": datasource_uid}
                }],
                "from": str(int((datetime.now() - timedelta(minutes=30)).timestamp() * 1000)),
                "to": str(int(datetime.now().timestamp() * 1000))
            }
            
            try:
                response = requests.post(
                    f"{self.grafana_url}/api/ds/query",
                    headers=self.headers,
                    json=query_data
                )
                
                if response.status_code == 200:
                    print(f"   ✅ Profile query executed")
                    successful_queries.append(test)
                else:
                    print(f"   ⚠️  No profile data available")
                    
            except Exception as e:
                print(f"   ❌ Error: {str(e)}")
        
        return successful_queries
    
    def create_empire_dashboard(self, prometheus_uid, loki_uid, pyroscope_uid):
        """Create a comprehensive empire monitoring dashboard"""
        print("\n🏗️ BUILDING LEGENDARY EMPIRE DASHBOARD...")
        
        dashboard = {
            "dashboard": {
                "id": None,
                "title": "🏆 HyperFocus Zone Empire - Legendary Command Center",
                "tags": ["empire", "hyperfocus", "legendary", "monitoring"],
                "timezone": "browser",
                "refresh": "5s",
                "time": {
                    "from": "now-1h",
                    "to": "now"
                },
                "panels": [
                    {
                        "id": 1,
                        "title": "🚀 Empire System Status",
                        "type": "stat",
                        "gridPos": {"h": 8, "w": 6, "x": 0, "y": 0},
                        "targets": [{
                            "expr": "up",
                            "refId": "A",
                            "datasource": {"uid": prometheus_uid}
                        }],
                        "fieldConfig": {
                            "defaults": {
                                "color": {"mode": "thresholds"},
                                "thresholds": {
                                    "steps": [
                                        {"color": "red", "value": 0},
                                        {"color": "yellow", "value": 0.8},
                                        {"color": "green", "value": 1}
                                    ]
                                },
                                "unit": "short"
                            }
                        }
                    },
                    {
                        "id": 2,
                        "title": "🤖 Agent Army Performance",
                        "type": "timeseries",
                        "gridPos": {"h": 8, "w": 6, "x": 6, "y": 0},
                        "targets": [{
                            "expr": "rate(http_requests_total[5m])",
                            "refId": "A",
                            "datasource": {"uid": prometheus_uid},
                            "legendFormat": "Requests/sec"
                        }]
                    },
                    {
                        "id": 3,
                        "title": "💎 System Resource Usage",
                        "type": "gauge",
                        "gridPos": {"h": 8, "w": 6, "x": 12, "y": 0},
                        "targets": [{
                            "expr": "cpu_usage_percent",
                            "refId": "A",
                            "datasource": {"uid": prometheus_uid}
                        }],
                        "fieldConfig": {
                            "defaults": {
                                "min": 0,
                                "max": 100,
                                "unit": "percent"
                            }
                        }
                    },
                    {
                        "id": 4,
                        "title": "🌟 Memory Crystal Analytics",
                        "type": "timeseries",
                        "gridPos": {"h": 8, "w": 6, "x": 18, "y": 0},
                        "targets": [{
                            "expr": "memory_usage_bytes",
                            "refId": "A",
                            "datasource": {"uid": prometheus_uid},
                            "legendFormat": "Memory Usage"
                        }]
                    },
                    {
                        "id": 5,
                        "title": "📝 Empire System Logs",
                        "type": "logs",
                        "gridPos": {"h": 8, "w": 12, "x": 0, "y": 8},
                        "targets": [{
                            "expr": '{job="grafana"}',
                            "refId": "A",
                            "datasource": {"uid": loki_uid}
                        }]
                    },
                    {
                        "id": 6,
                        "title": "🔬 Performance Profiling",
                        "type": "flamegraph",
                        "gridPos": {"h": 8, "w": 12, "x": 12, "y": 8},
                        "targets": [{
                            "profileTypeId": "cpu",
                            "refId": "A",
                            "datasource": {"uid": pyroscope_uid}
                        }]
                    },
                    {
                        "id": 7,
                        "title": "🎯 Empire Success Metrics",
                        "type": "table",
                        "gridPos": {"h": 8, "w": 24, "x": 0, "y": 16},
                        "targets": [{
                            "expr": "up",
                            "refId": "A",
                            "datasource": {"uid": prometheus_uid},
                            "format": "table"
                        }]
                    }
                ],
                "templating": {
                    "list": []
                },
                "annotations": {
                    "list": []
                }
            },
            "overwrite": True
        }
        
        try:
            response = requests.post(
                f"{self.grafana_url}/api/dashboards/db",
                headers=self.headers,
                json=dashboard
            )
            
            if response.status_code == 200:
                result = response.json()
                dashboard_url = f"{self.grafana_url}/d/{result['uid']}"
                print(f"✅ LEGENDARY DASHBOARD CREATED!")
                print(f"🌐 URL: {dashboard_url}")
                return dashboard_url
            else:
                print(f"❌ Dashboard creation failed: {response.status_code}")
                print(f"Response: {response.text}")
                return None
                
        except Exception as e:
            print(f"❌ Error creating dashboard: {str(e)}")
            return None
    
    def run_complete_test_and_build(self):
        """Run complete testing and dashboard building process"""
        print(f"\n🚀💎⚡ STARTING COMPLETE EMPIRE TESTING & BUILDING ⚡💎🚀")
        print("=" * 70)
        
        # Get all data sources
        try:
            response = requests.get(f"{self.grafana_url}/api/datasources", headers=self.headers)
            if response.status_code != 200:
                print("❌ Failed to get data sources")
                return
            
            datasources = response.json()
            
            # Find our target data sources
            prometheus_uid = None
            loki_uid = None
            pyroscope_uid = None
            
            for ds in datasources:
                name = ds.get('name', '').lower()
                ds_type = ds.get('type', '')
                uid = ds.get('uid')
                
                if 'prom' in name and ds_type == 'prometheus':
                    prometheus_uid = uid
                    print(f"🎯 Found Prometheus: {ds.get('name')} ({uid})")
                elif 'logs' in name and ds_type == 'loki':
                    loki_uid = uid
                    print(f"📝 Found Loki: {ds.get('name')} ({uid})")
                elif 'profiles' in name and 'pyroscope' in ds_type:
                    pyroscope_uid = uid
                    print(f"🔬 Found Pyroscope: {ds.get('name')} ({uid})")
            
            # Test queries on each data source
            successful_tests = 0
            
            if prometheus_uid:
                prom_queries = self.test_prometheus_queries(prometheus_uid)
                if prom_queries:
                    successful_tests += 1
                    print(f"✅ Prometheus: {len(prom_queries)} successful queries")
                
            if loki_uid:
                loki_queries = self.test_loki_queries(loki_uid)
                if loki_queries:
                    successful_tests += 1
                    print(f"✅ Loki: {len(loki_queries)} successful queries")
                
            if pyroscope_uid:
                pyroscope_queries = self.test_pyroscope_queries(pyroscope_uid)
                if pyroscope_queries:
                    successful_tests += 1
                    print(f"✅ Pyroscope: {len(pyroscope_queries)} successful queries")
            
            # Build empire dashboard if we have working data sources
            if successful_tests > 0:
                print(f"\n🏗️ BUILDING EMPIRE DASHBOARD WITH {successful_tests} DATA SOURCES...")
                dashboard_url = self.create_empire_dashboard(
                    prometheus_uid or "default", 
                    loki_uid or "default", 
                    pyroscope_uid or "default"
                )
                
                if dashboard_url:
                    print(f"\n🎊💎⚡ SUCCESS! LEGENDARY EMPIRE DASHBOARD READY! ⚡💎🎊")
                    print("=" * 70)
                    print(f"🌐 Dashboard URL: {dashboard_url}")
                    print(f"🎯 Data Sources Tested: {successful_tests}/3")
                    print("🏆 Your HyperFocus Zone Empire monitoring is LEGENDARY!")
                    
                    # Create summary file
                    summary = {
                        "dashboard_url": dashboard_url,
                        "successful_tests": successful_tests,
                        "data_sources": {
                            "prometheus": prometheus_uid,
                            "loki": loki_uid,
                            "pyroscope": pyroscope_uid
                        },
                        "created_at": datetime.now().isoformat(),
                        "status": "LEGENDARY_SUCCESS"
                    }
                    
                    with open('empire_dashboard_summary.json', 'w') as f:
                        json.dump(summary, f, indent=2)
                    
                    print(f"📋 Summary saved to: empire_dashboard_summary.json")
                else:
                    print("❌ Dashboard creation failed")
            else:
                print("⚠️  No data sources returned query results. Check your metrics.")
                
        except Exception as e:
            print(f"❌ Error during testing: {str(e)}")

if __name__ == "__main__":
    tester = GrafanaQueryTester()
    tester.run_complete_test_and_build()

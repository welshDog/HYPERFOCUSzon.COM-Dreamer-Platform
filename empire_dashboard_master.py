#!/usr/bin/env python3
"""
🎯💎⚡ EMPIRE QUERY & DASHBOARD MASTER ⚡💎🎯

Master script to:
1. Test all data source queries
2. Build legendary empire dashboards
3. Verify everything works
"""

import requests
import json
import sys
from datetime import datetime

def main():
    print("🎯💎⚡ EMPIRE QUERY & DASHBOARD MASTER ⚡💎🎯")
    print("=" * 60)
    
    grafana_url = "https://welshdog.grafana.net"
    token = "glsa_VYEsC8dyYed5K3xFJTQQ8sYOJBfJctLK_4ebbbed1"
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    
    try:
        # Step 1: Get all data sources
        print("📊 STEP 1: Getting data sources...")
        response = requests.get(f"{grafana_url}/api/datasources", headers=headers)
        
        if response.status_code != 200:
            print(f"❌ Failed to get data sources: {response.status_code}")
            return False
            
        datasources = response.json()
        print(f"✅ Found {len(datasources)} data sources")
        
        # Step 2: Find target data sources
        prometheus_uid = None
        loki_uid = None
        pyroscope_uid = None
        
        for ds in datasources:
            name = ds.get('name', '').lower()
            ds_type = ds.get('type', '')
            uid = ds.get('uid')
            
            if 'prom' in name and ds_type == 'prometheus':
                prometheus_uid = uid
                print(f"🎯 Prometheus: {ds.get('name')} ({uid})")
            elif 'logs' in name and ds_type == 'loki':
                loki_uid = uid
                print(f"📝 Loki: {ds.get('name')} ({uid})")
            elif 'profiles' in name and 'pyroscope' in ds_type:
                pyroscope_uid = uid
                print(f"🔬 Pyroscope: {ds.get('name')} ({uid})")
        
        # Step 3: Test Prometheus queries
        print("\n🔥 STEP 3: Testing Prometheus queries...")
        if prometheus_uid:
            test_queries = ["up", "prometheus_build_info", "go_memstats_alloc_bytes"]
            for query in test_queries:
                print(f"   Testing: {query}")
                
                query_data = {
                    "queries": [{
                        "refId": "A",
                        "expr": query,
                        "datasource": {"uid": prometheus_uid}
                    }],
                    "from": "now-5m",
                    "to": "now"
                }
                
                try:
                    response = requests.post(f"{grafana_url}/api/ds/query", headers=headers, json=query_data)
                    if response.status_code == 200:
                        print(f"   ✅ {query}: SUCCESS")
                    else:
                        print(f"   ❌ {query}: Failed ({response.status_code})")
                except Exception as e:
                    print(f"   ❌ {query}: Error - {str(e)}")
        else:
            print("   ⚠️ No Prometheus data source found")
        
        # Step 4: Build Empire Dashboard
        print("\n🏗️ STEP 4: Building Empire Dashboard...")
        
        if prometheus_uid:
            dashboard = {
                "dashboard": {
                    "id": None,
                    "title": "🏆 HyperFocus Zone Empire - Command Center",
                    "tags": ["empire", "hyperfocus", "legendary"],
                    "timezone": "browser",
                    "refresh": "10s",
                    "time": {"from": "now-1h", "to": "now"},
                    "panels": [
                        {
                            "id": 1,
                            "title": "🚀 Empire Systems Online",
                            "type": "stat",
                            "gridPos": {"h": 6, "w": 6, "x": 0, "y": 0},
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
                                            {"color": "green", "value": 1}
                                        ]
                                    },
                                    "mappings": [
                                        {"options": {"0": {"text": "DOWN"}}, "type": "value"},
                                        {"options": {"1": {"text": "UP"}}, "type": "value"}
                                    ]
                                }
                            }
                        },
                        {
                            "id": 2,
                            "title": "🤖 Agent Army Activity",
                            "type": "timeseries",
                            "gridPos": {"h": 6, "w": 9, "x": 6, "y": 0},
                            "targets": [{
                                "expr": "rate(prometheus_http_requests_total[5m])",
                                "refId": "A",
                                "datasource": {"uid": prometheus_uid},
                                "legendFormat": "Requests/sec"
                            }]
                        },
                        {
                            "id": 3,
                            "title": "🌟 Empire Status",
                            "type": "table",
                            "gridPos": {"h": 6, "w": 9, "x": 15, "y": 0},
                            "targets": [{
                                "expr": "prometheus_build_info",
                                "refId": "A",
                                "datasource": {"uid": prometheus_uid},
                                "format": "table"
                            }]
                        },
                        {
                            "id": 4,
                            "title": "💎 Memory Crystals (Usage)",
                            "type": "gauge",
                            "gridPos": {"h": 6, "w": 12, "x": 0, "y": 6},
                            "targets": [{
                                "expr": "go_memstats_alloc_bytes",
                                "refId": "A",
                                "datasource": {"uid": prometheus_uid}
                            }],
                            "fieldConfig": {
                                "defaults": {
                                    "unit": "bytes",
                                    "min": 0
                                }
                            }
                        },
                        {
                            "id": 5,
                            "title": "🧠 Active Agents (Goroutines)",
                            "type": "timeseries",
                            "gridPos": {"h": 6, "w": 12, "x": 12, "y": 6},
                            "targets": [{
                                "expr": "go_goroutines",
                                "refId": "A",
                                "datasource": {"uid": prometheus_uid},
                                "legendFormat": "Active Goroutines"
                            }]
                        }
                    ]
                },
                "overwrite": True
            }
            
            try:
                response = requests.post(f"{grafana_url}/api/dashboards/db", headers=headers, json=dashboard)
                
                if response.status_code == 200:
                    result = response.json()
                    dashboard_url = f"{grafana_url}/d/{result['uid']}"
                    
                    print("✅ EMPIRE DASHBOARD CREATED!")
                    print(f"🌐 URL: {dashboard_url}")
                    
                    # Save summary
                    summary = {
                        "success": True,
                        "dashboard_url": dashboard_url,
                        "dashboard_uid": result['uid'],
                        "data_sources": {
                            "prometheus": prometheus_uid,
                            "loki": loki_uid,
                            "pyroscope": pyroscope_uid
                        },
                        "created_at": datetime.now().isoformat()
                    }
                    
                    with open('empire_dashboard_success.json', 'w') as f:
                        json.dump(summary, f, indent=2)
                    
                    print("📋 Success summary saved to: empire_dashboard_success.json")
                    
                    print("\n🎊💎⚡ EMPIRE COMMAND CENTER IS READY! ⚡💎🎊")
                    print("=" * 60)
                    print("🏆 Your HyperFocus Zone Empire monitoring is LEGENDARY!")
                    print("🚀 Visit the dashboard to see your empire in action!")
                    
                    return True
                else:
                    print(f"❌ Dashboard creation failed: {response.status_code}")
                    print(f"Response: {response.text}")
                    return False
                    
            except Exception as e:
                print(f"❌ Dashboard creation error: {str(e)}")
                return False
        else:
            print("❌ Cannot create dashboard without Prometheus data source")
            return False
            
    except Exception as e:
        print(f"❌ Master script error: {str(e)}")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

import requests
import json

# Simple Empire Dashboard Builder
grafana_url = "https://welshdog.grafana.net"
token = "glsa_VYEsC8dyYed5K3xFJTQQ8sYOJBfJctLK_4ebbbed1"
headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}

print("🏗️ BUILDING LEGENDARY EMPIRE DASHBOARD")
print("=" * 50)

# Get data sources first
response = requests.get(f"{grafana_url}/api/datasources", headers=headers)
datasources = response.json()

prometheus_uid = None
for ds in datasources:
    if 'prom' in ds.get('name', '').lower() and ds.get('type') == 'prometheus':
        prometheus_uid = ds.get('uid')
        print(f"🎯 Using Prometheus: {ds.get('name')} ({prometheus_uid})")
        break

if not prometheus_uid:
    print("❌ No Prometheus data source found")
    exit()

# Create simplified empire dashboard
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
                "title": "🚀 Empire System Status",
                "type": "stat",
                "gridPos": {"h": 8, "w": 12, "x": 0, "y": 0},
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
                        }
                    }
                }
            },
            {
                "id": 2,
                "title": "🤖 Request Rate (Agent Army)",
                "type": "timeseries",
                "gridPos": {"h": 8, "w": 12, "x": 12, "y": 0},
                "targets": [{
                    "expr": "rate(prometheus_http_requests_total[5m])",
                    "refId": "A",
                    "datasource": {"uid": prometheus_uid},
                    "legendFormat": "Requests/sec"
                }]
            },
            {
                "id": 3,
                "title": "💎 Memory Usage (Memory Crystals)",
                "type": "gauge",
                "gridPos": {"h": 8, "w": 12, "x": 0, "y": 8},
                "targets": [{
                    "expr": "go_memstats_alloc_bytes",
                    "refId": "A",
                    "datasource": {"uid": prometheus_uid}
                }],
                "fieldConfig": {
                    "defaults": {
                        "unit": "bytes"
                    }
                }
            },
            {
                "id": 4,
                "title": "🌟 Goroutines (Active Agents)",
                "type": "timeseries",
                "gridPos": {"h": 8, "w": 12, "x": 12, "y": 8},
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

# Create the dashboard
try:
    response = requests.post(f"{grafana_url}/api/dashboards/db", headers=headers, json=dashboard)
    
    if response.status_code == 200:
        result = response.json()
        dashboard_url = f"{grafana_url}/d/{result['uid']}"
        print("✅ DASHBOARD CREATED SUCCESSFULLY!")
        print(f"🌐 URL: {dashboard_url}")
        print("🏆 Your Empire Command Center is ready!")
    else:
        print(f"❌ Dashboard creation failed: {response.status_code}")
        print(f"Response: {response.text}")
        
except Exception as e:
    print(f"❌ Error: {str(e)}")

print("\n🎊 EMPIRE DASHBOARD DEPLOYMENT COMPLETE!")

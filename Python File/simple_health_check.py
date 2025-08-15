import requests
import json

# Simple Grafana Data Source Health Check
grafana_url = "https://welshdog.grafana.net"
token = "glsa_VYEsC8dyYed5K3xFJTQQ8sYOJBfJctLK_4ebbbed1"

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

print("🔧 GRAFANA DATA SOURCE HEALTH CHECKER")
print("=" * 50)

try:
    # Get all data sources
    response = requests.get(f"{grafana_url}/api/datasources", headers=headers)
    
    if response.status_code == 200:
        datasources = response.json()
        print(f"✅ Connected! Found {len(datasources)} data sources")
        
        # Target the three failing sources
        target_names = ['profiles', 'logs', 'prom']
        
        for ds in datasources:
            name = ds.get('name', '')
            ds_type = ds.get('type', '')
            
            # Check if this is one of our target data sources
            if any(target in name.lower() for target in target_names):
                print(f"\n🎯 Checking: {name} ({ds_type})")
                
                # Test health
                health_response = requests.get(f"{grafana_url}/api/datasources/{ds['id']}/health", headers=headers)
                
                if health_response.status_code == 200:
                    health_data = health_response.json()
                    status = health_data.get('status', 'unknown')
                    message = health_data.get('message', 'No message')
                    
                    if status == 'OK':
                        print(f"   ✅ HEALTHY")
                    else:
                        print(f"   ❌ UNHEALTHY: {status}")
                        print(f"   📝 Message: {message}")
                        
                        # Try to fix based on type
                        if ds_type == 'prometheus':
                            print("   🔧 Attempting Prometheus fix...")
                            fix_config = {
                                "id": ds['id'],
                                "uid": ds['uid'],
                                "name": ds['name'],
                                "type": "prometheus",
                                "url": ds.get('url'),
                                "access": "proxy",
                                "jsonData": {
                                    "httpMethod": "POST",
                                    "queryTimeout": "60s",
                                    "timeInterval": "15s"
                                }
                            }
                            
                        elif ds_type == 'loki':
                            print("   🔧 Attempting Loki fix...")
                            fix_config = {
                                "id": ds['id'],
                                "uid": ds['uid'],
                                "name": ds['name'],
                                "type": "loki",
                                "url": ds.get('url'),
                                "access": "proxy",
                                "jsonData": {
                                    "timeout": "60s",
                                    "maxLines": 1000
                                }
                            }
                            
                        elif 'pyroscope' in ds_type:
                            print("   🔧 Attempting Pyroscope fix...")
                            fix_config = {
                                "id": ds['id'],
                                "uid": ds['uid'],
                                "name": ds['name'],
                                "type": ds['type'],
                                "url": ds.get('url'),
                                "access": "proxy",
                                "jsonData": {
                                    "timeout": "60s"
                                }
                            }
                        else:
                            print(f"   ⚠️ Unknown type: {ds_type}")
                            continue
                        
                        # Apply fix
                        update_response = requests.put(
                            f"{grafana_url}/api/datasources/{ds['id']}", 
                            headers=headers, 
                            json=fix_config
                        )
                        
                        if update_response.status_code == 200:
                            print("   ✅ Configuration updated!")
                            
                            # Recheck health
                            import time
                            time.sleep(2)
                            recheck_response = requests.get(f"{grafana_url}/api/datasources/{ds['id']}/health", headers=headers)
                            if recheck_response.status_code == 200:
                                recheck_data = recheck_response.json()
                                if recheck_data.get('status') == 'OK':
                                    print("   🎊 NOW HEALTHY!")
                                else:
                                    print(f"   ⚠️ Still has issues: {recheck_data.get('message', 'Unknown')}")
                        else:
                            print(f"   ❌ Update failed: {update_response.status_code}")
                else:
                    print(f"   ❌ Health check failed: {health_response.status_code}")
    else:
        print(f"❌ Failed to connect: {response.status_code}")
        print(response.text)
        
except Exception as e:
    print(f"❌ Error: {str(e)}")

print("\n🏆 Health check complete!")

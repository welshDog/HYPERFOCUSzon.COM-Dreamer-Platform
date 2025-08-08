import os
import requests

print("🎯 Direct API Test Starting...")

token = os.getenv('GRAFANA_SERVICE_ACCOUNT_TOKEN')
print(f"Token found: {bool(token)}")

if token:
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    
    print("Making API request...")
    try:
        response = requests.get('https://welshdog.grafana.net/api/user', headers=headers, timeout=10)
        print(f"Response status: {response.status_code}")
        
        if response.status_code == 200:
            user_info = response.json()
            print(f"✅ Success! User: {user_info.get('name', 'Unknown')}")
            
            # Now try to create Prometheus data source
            print("\nTrying to create Prometheus data source...")
            datasource = {
                "name": "HyperFocus-Empire-Prometheus",
                "type": "prometheus", 
                "url": "http://localhost:9090",
                "access": "proxy",
                "isDefault": True
            }
            
            ds_response = requests.post(
                'https://welshdog.grafana.net/api/datasources',
                headers=headers,
                json=datasource,
                timeout=10
            )
            
            print(f"Data source creation status: {ds_response.status_code}")
            if ds_response.status_code in [200, 201]:
                print("✅ Prometheus data source created!")
            elif ds_response.status_code == 409:
                print("✅ Prometheus data source already exists!")
            else:
                print(f"❌ Error: {ds_response.text}")
        else:
            print(f"❌ Auth failed: {response.text}")
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")

print("Test complete!")

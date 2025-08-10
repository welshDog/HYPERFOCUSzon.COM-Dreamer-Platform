#!/usr/bin/env python3
"""
🚀💎⚡ GRAFANA PROMETHEUS DATA SOURCE AUTO-CONFIGURATOR ⚡💎🚀
Automatically configure Prometheus data source in Grafana
"""

import json
import time

from base64 import b64encode
import requests
def wait_for_grafana():
    """Wait for Grafana to be ready"""
    print("🔄 Waiting for Grafana to be ready...")
    for i in range(30):  # Wait up to 30 seconds
        try:
            response = requests.get('http://localhost:3001/api/health', timeout=2)
            if response.status_code == 200:
                print("✅ Grafana is ready!")
                return True
        except (ConnectionError, OSError):
            pass
        time.sleep(1)
        print(f"⏳ Waiting... ({i+1}/30)")
    return False

def configure_prometheus_datasource():
    """Configure Prometheus data source in Grafana"""
    print("🔧 Configuring Prometheus data source...")

    # Grafana admin credentials
    username = 'admin'
    password = 'BROski2025!'

    # Create authentication header
    credentials = b64encode(f'{username}:{password}'.encode()).decode()
    headers = {
        'Authorization': f'Basic {credentials}',
        'Content-Type': 'application/json'
    }

    # Prometheus data source configuration
    datasource_config = {
        "name": "Prometheus-Empire",
        "type": "prometheus",
        "url": "http://localhost:9090",
        "access": "proxy",
        "isDefault": True,
        "jsonData": {
            "httpMethod": "POST",
            "exemplarTraceIdDestinations": []
        }
    }

    try:
        # Add the data source
        response = requests.post(
            'http://localhost:3001/api/datasources',
            headers=headers,
            data=json.dumps(datasource_config),
            timeout=10
        )

        if response.status_code in [200, 409]:  # 200 = success, 409 = already exists
            print("✅ Prometheus data source configured successfully!")

            # Test the data source
            if response.status_code == 200:
                datasource_id = response.json().get('id', 1)
            else:
                datasource_id = 1  # Default ID if already exists

            test_response = requests.post(
                f'http://localhost:3001/api/datasources/{datasource_id}/resources/prometheus/api/v1/label/__name__/values',
                headers=headers,
                timeout=10
            )

            if test_response.status_code == 200:
                print("✅ Data source health check PASSED!")
                print("🎊 Your Prometheus data source is now healthy!")
                return True
            else:
                print(f"⚠️ Data source test returned status: {test_response.status_code}")
                return False
        else:
            print(f"❌ Failed to configure data source: {response.status_code}")
            print(f"Response: {response.text}")
            return False

    except Exception as e:
        print(f"❌ Error configuring data source: {str(e)}")
        return False

def main():
    print("\n" + "="*70)
    print("🚀💎⚡ GRAFANA PROMETHEUS AUTO-CONFIGURATOR ⚡💎🚀")
    print("="*70)

    if not wait_for_grafana():
        print("❌ Grafana is not responding. Make sure it's running on localhost:3001")
        return False

    success = configure_prometheus_datasource()

    if success:
        print("\n🎯 CONFIGURATION COMPLETE!")
        print("📊 Access Grafana at: http://localhost:3001")
        print("🔑 Username: admin")
        print("🔑 Password: BROski2025!")
        print("✅ Prometheus data source is now healthy!")
        print("\n🚀 Your health check issue is FIXED!")
    else:
        print("\n❌ Configuration failed. Manual setup required.")
        print("🔧 Manual steps:")
        print("1. Go to http://localhost:3001")
        print("2. Login with admin/BROski2025!")
        print("3. Go to Configuration -> Data Sources")
        print("4. Add Prometheus data source")
        print("5. URL: http://localhost:9090")

    return success

if __name__ == "__main__":
    main()

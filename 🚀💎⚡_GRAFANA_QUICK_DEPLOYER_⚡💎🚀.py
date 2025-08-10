#!/usr/bin/env python3
"""
🎯💎⚡ GRAFANA EMPIRE QUICK DEPLOYER ⚡💎🎯
Simplified, bulletproof deployment script
"""

import json
import os

import requests
def test_grafana_api():
    """Test API authentication"""
    token = os.getenv('GRAFANA_SERVICE_ACCOUNT_TOKEN')
    if not token:
        print("❌ No token found!")
        return False

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    try:
        response = requests.get('https://welshdog.grafana.net/api/user', headers=headers)
        if response.status_code == 200:
            user_info = response.json()
            print(f"✅ API Authentication successful!")
            print(f"👤 User: {user_info.get('name', 'Unknown')}")
            print(f"📧 Email: {user_info.get('email', 'Unknown')}")
            return True
        else:
            print(f"❌ API test failed: {response.status_code}")
            print(f"Response: {response.text}")
            return False
    except Exception as e:
        print(f"❌ API test error: {str(e)}")
        return False

def create_prometheus_source():
    """Create Prometheus data source"""
    token = os.getenv('GRAFANA_SERVICE_ACCOUNT_TOKEN')
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    datasource = {
        "name": "HyperFocus-Empire-Prometheus",
        "type": "prometheus",
        "url": "http://localhost:9090",
        "access": "proxy",
        "isDefault": True,
        "jsonData": {
            "httpMethod": "POST"
        }
    }

    try:
        response = requests.post(
            'https://welshdog.grafana.net/api/datasources',
            headers=headers,
            json=datasource
        )

        if response.status_code in [200, 201]:
            print("✅ Prometheus data source created successfully!")
            return True
        elif response.status_code == 409:
            print("✅ Prometheus data source already exists!")
            return True
        else:
            print(f"❌ Failed to create data source: {response.status_code}")
            print(f"Response: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Error creating data source: {str(e)}")
        return False

def import_dashboard():
    """Import the empire dashboard"""
    token = os.getenv('GRAFANA_SERVICE_ACCOUNT_TOKEN')
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    # Load the dashboard template
    try:
        with open('h:/grafana-config/empire-dashboard-template.json', 'r') as f:
            dashboard_data = json.load(f)

        response = requests.post(
            'https://welshdog.grafana.net/api/dashboards/db',
            headers=headers,
            json=dashboard_data
        )

        if response.status_code in [200, 201]:
            result = response.json()
            dashboard_url = f"https://welshdog.grafana.net/d/{result.get('uid', 'unknown')}"
            print(f"✅ Dashboard imported successfully!")
            print(f"🎯 Dashboard URL: {dashboard_url}")
            return True
        else:
            print(f"❌ Failed to import dashboard: {response.status_code}")
            print(f"Response: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Error importing dashboard: {str(e)}")
        return False

def main():
    """Main deployment function"""
    print("🚀💎⚡ GRAFANA EMPIRE DEPLOYMENT STARTING ⚡💎🚀")
    print("=" * 60)

    # Step 1: Test API
    print("\n🔐 Step 1: Testing API Authentication...")
    if not test_grafana_api():
        print("❌ API authentication failed. Stopping deployment.")
        return

    # Step 2: Create Prometheus data source
    print("\n📊 Step 2: Creating Prometheus Data Source...")
    if not create_prometheus_source():
        print("❌ Failed to create Prometheus data source.")
        return

    # Step 3: Import dashboard
    print("\n🎯 Step 3: Importing Empire Dashboard...")
    if not import_dashboard():
        print("❌ Failed to import dashboard.")
        return

    print("\n🎊💎⚡ LEGENDARY DEPLOYMENT COMPLETE! ⚡💎🎊")
    print("=" * 60)
    print("🌟 Your HyperFocus Zone Empire monitoring is now LIVE!")
    print("🎯 Visit: https://welshdog.grafana.net")
    print("🚀 All systems operational and legendary!")

if __name__ == "__main__":
    main()

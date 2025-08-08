#!/usr/bin/env python3
"""
🚀💎⚡ LEGENDARY DASHBOARD DEPLOYER - SIMPLIFIED VERSION ⚡💎🚀
==============================================================

Quick deployment script for cost management dashboard.
"""

import json
import requests
import sys
import os
from pathlib import Path

def deploy_dashboard():
    """Deploy dashboard to Grafana Cloud"""
    
    # Configuration
    grafana_url = "https://welshdog.grafana.net"
    dashboard_path = r"h:\grafana-by-example\cost-management\dashboard-final.json"
    
    # Get token from environment or use default
    service_token = os.environ.get('GRAFANA_SERVICE_ACCOUNT_TOKEN', 'glsa_VYEsC8dyYed5K3xFJTQQ8sYOJBfJctLK_4ebbbed1')
    
    print("🚀💎⚡ LEGENDARY DASHBOARD DEPLOYMENT STARTING ⚡💎🚀")
    print("=" * 60)
    print(f"Target: {grafana_url}")
    print(f"Dashboard: {dashboard_path}")
    print(f"Token: {service_token[:20]}...")
    print()
    
    # Check if dashboard file exists
    if not os.path.exists(dashboard_path):
        print(f"❌ Dashboard file not found: {dashboard_path}")
        return False
        
    # Load dashboard JSON
    try:
        with open(dashboard_path, 'r', encoding='utf-8') as f:
            dashboard_data = json.load(f)
        print(f"✅ Dashboard loaded: {len(json.dumps(dashboard_data)) // 1024} KB")
    except Exception as e:
        print(f"❌ Failed to load dashboard: {e}")
        return False
    
    # Prepare headers
    headers = {
        'Authorization': f'Bearer {service_token}',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    # Test connection
    try:
        print("🔍 Testing connection...")
        test_response = requests.get(f"{grafana_url}/api/org", headers=headers, timeout=30)
        if test_response.status_code == 200:
            org_info = test_response.json()
            print(f"✅ Connected to: {org_info.get('name', 'Grafana Cloud')}")
        else:
            print(f"❌ Connection test failed: {test_response.status_code}")
            print(f"Response: {test_response.text}")
            return False
    except Exception as e:
        print(f"❌ Connection error: {e}")
        return False
    
    # Prepare dashboard payload
    dashboard_payload = {
        "dashboard": dashboard_data,
        "overwrite": True,
        "message": "🎊 Legendary Cost Management Dashboard - Empire Deployment"
    }
    
    # Remove id and uid to let Grafana assign new ones
    if 'id' in dashboard_payload['dashboard']:
        del dashboard_payload['dashboard']['id']
    if 'uid' in dashboard_payload['dashboard']:
        dashboard_payload['dashboard']['uid'] = None
    
    # Deploy dashboard
    try:
        print("🚀 Deploying dashboard...")
        deploy_response = requests.post(
            f"{grafana_url}/api/dashboards/db",
            headers=headers,
            json=dashboard_payload,
            timeout=60
        )
        
        if deploy_response.status_code in [200, 201]:
            result = deploy_response.json()
            print("🎊💎⚡ LEGENDARY DEPLOYMENT SUCCESS! ⚡💎🎊")
            print(f"Dashboard ID: {result.get('id', 'Unknown')}")
            print(f"Dashboard UID: {result.get('uid', 'Unknown')}")
            print(f"Dashboard URL: {result.get('url', 'Check your Grafana instance')}")
            print()
            print("🏛️ Empire Cost Management Dashboard is now LIVE!")
            print(f"🌐 Access: {grafana_url}/dashboards")
            return True
        else:
            print(f"❌ Deployment failed: {deploy_response.status_code}")
            print(f"Response: {deploy_response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Deployment error: {e}")
        return False

if __name__ == "__main__":
    success = deploy_dashboard()
    sys.exit(0 if success else 1)

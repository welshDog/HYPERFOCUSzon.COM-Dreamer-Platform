#!/usr/bin/env python3
"""
LEGENDARY COST DASHBOARD DEPLOYMENT SCRIPT
==========================================

Deploy cost management dashboard to welshdog.grafana.net
Author: Chief Lyndz Empire
Date: August 4, 2025
"""

import json
import requests
import os
import sys
from datetime import datetime

def deploy_cost_dashboard():
    """Deploy the cost management dashboard to Grafana Cloud"""
    
    print("LEGENDARY COST DASHBOARD DEPLOYMENT STARTING")
    print("=" * 50)
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Configuration
    grafana_url = "https://welshdog.grafana.net"
    dashboard_path = r"h:\grafana-by-example\cost-management\dashboard-final.json"
    service_token = "glsa_VYEsC8dyYed5K3xFJTQQ8sYOJBfJctLK_4ebbbed1"
    
    print(f"Grafana URL: {grafana_url}")
    print(f"Dashboard Path: {dashboard_path}")
    print(f"Service Token: {service_token[:20]}...")
    print()
    
    # Step 1: Verify dashboard file exists
    print("Step 1: Checking dashboard file...")
    if not os.path.exists(dashboard_path):
        print(f"ERROR: Dashboard file not found: {dashboard_path}")
        return False
    
    file_size = os.path.getsize(dashboard_path)
    print(f"SUCCESS: Dashboard file found ({file_size} bytes)")
    
    # Step 2: Load dashboard JSON
    print("\nStep 2: Loading dashboard JSON...")
    try:
        with open(dashboard_path, 'r', encoding='utf-8') as f:
            dashboard_data = json.load(f)
        print(f"SUCCESS: Dashboard loaded")
        print(f"Title: {dashboard_data.get('title', 'Unknown')}")
        print(f"Panels: {len(dashboard_data.get('panels', []))}")
    except Exception as e:
        print(f"ERROR: Failed to load dashboard JSON: {e}")
        return False
    
    # Step 3: Test Grafana connection
    print("\nStep 3: Testing Grafana connection...")
    headers = {
        'Authorization': f'Bearer {service_token}',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    try:
        response = requests.get(f"{grafana_url}/api/org", headers=headers, timeout=30)
        if response.status_code == 200:
            org_info = response.json()
            print(f"SUCCESS: Connected to Grafana Cloud")
            print(f"Organization: {org_info.get('name', 'Unknown')}")
            print(f"Org ID: {org_info.get('id', 'Unknown')}")
        else:
            print(f"ERROR: Connection failed - Status: {response.status_code}")
            print(f"Response: {response.text}")
            return False
    except Exception as e:
        print(f"ERROR: Connection test failed: {e}")
        return False
    
    # Step 4: Prepare dashboard for deployment
    print("\nStep 4: Preparing dashboard for deployment...")
    
    # Create deployment payload
    dashboard_payload = {
        "dashboard": dashboard_data.copy(),
        "overwrite": True,
        "message": "Empire Cost Management Dashboard - Automated Deployment"
    }
    
    # Remove ID and set UID to None to let Grafana assign new ones
    if 'id' in dashboard_payload['dashboard']:
        del dashboard_payload['dashboard']['id']
        print("Removed existing dashboard ID")
    
    if 'uid' in dashboard_payload['dashboard']:
        dashboard_payload['dashboard']['uid'] = None
        print("Reset dashboard UID")
    
    print("Dashboard prepared for deployment")
    
    # Step 5: Deploy dashboard
    print("\nStep 5: Deploying dashboard to Grafana Cloud...")
    
    try:
        deploy_response = requests.post(
            f"{grafana_url}/api/dashboards/db",
            headers=headers,
            json=dashboard_payload,
            timeout=60
        )
        
        print(f"Deployment response status: {deploy_response.status_code}")
        
        if deploy_response.status_code in [200, 201]:
            result = deploy_response.json()
            
            print("\n" + "="*50)
            print("LEGENDARY DEPLOYMENT SUCCESS!")
            print("="*50)
            print(f"Dashboard ID: {result.get('id', 'Unknown')}")
            print(f"Dashboard UID: {result.get('uid', 'Unknown')}")
            print(f"Dashboard URL: {grafana_url}{result.get('url', '')}")
            print(f"Status: {result.get('status', 'Unknown')}")
            print()
            print("Empire Cost Management Dashboard is now LIVE!")
            print(f"Access your dashboard at: {grafana_url}/dashboards")
            print()
            print("Features now available:")
            print("- Billable series tracking")
            print("- Cost analysis and trends")
            print("- Environment comparison")
            print("- ML-powered cost predictions")
            print()
            print("DEPLOYMENT COMPLETE - EMPIRE ECONOMY MONITORING ACTIVE!")
            return True
            
        else:
            print(f"\nERROR: Deployment failed")
            print(f"Status Code: {deploy_response.status_code}")
            print(f"Response: {deploy_response.text}")
            
            # Try to parse error details
            try:
                error_data = deploy_response.json()
                if 'message' in error_data:
                    print(f"Error Message: {error_data['message']}")
                if 'errors' in error_data:
                    print(f"Detailed Errors: {error_data['errors']}")
            except:
                pass
                
            return False
            
    except Exception as e:
        print(f"ERROR: Deployment request failed: {e}")
        return False

if __name__ == "__main__":
    print("EMPIRE COST DASHBOARD DEPLOYER")
    print("Initializing deployment sequence...")
    print()
    
    try:
        success = deploy_cost_dashboard()
        if success:
            print("\nDEPLOYMENT MISSION: ACCOMPLISHED")
            sys.exit(0)
        else:
            print("\nDEPLOYMENT MISSION: FAILED")
            sys.exit(1)
    except Exception as e:
        print(f"\nCRITICAL ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

#!/usr/bin/env python3
"""
🚀💎⚡ LEGENDARY GRAFANA CLOUD DASHBOARD DEPLOYER ⚡💎🚀
========================================================

Automated deployment script for uploading cost management dashboard
to welshdog.grafana.net using Grafana Cloud API.

Author: Chief Lyndz Empire
Date: August 3, 2025
Purpose: Deploy 38.8KB cost management dashboard to Grafana Cloud
Status: Production-ready deployment automation
"""

import json
import requests
import sys
import os
from pathlib import Path
from typing import Dict, Any, Optional
import argparse
from datetime import datetime

class LegendaryGrafanaDashboardDeployer:
    """🏛️ Legendary Grafana Cloud Dashboard Deployment System"""
    
    def __init__(self, grafana_url: str, service_account_token: str):
        """Initialize the legendary deployer"""
        self.grafana_url = grafana_url.rstrip('/')
        self.api_url = f"{self.grafana_url}/api"
        self.headers = {
            'Authorization': f'Bearer {service_account_token}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        
    def validate_connection(self) -> bool:
        """🔍 Validate connection to Grafana Cloud instance"""
        try:
            print("🔍 Validating connection to Grafana Cloud...")
            response = self.session.get(f"{self.api_url}/org")
            if response.status_code == 200:
                org_info = response.json()
                print(f"✅ Connected to: {org_info.get('name', 'Unknown Org')}")
                print(f"🏛️ Organization ID: {org_info.get('id', 'Unknown')}")
                return True
            else:
                print(f"❌ Connection failed: {response.status_code} - {response.text}")
                return False
        except Exception as e:
            print(f"❌ Connection error: {str(e)}")
            return False
    
    def load_dashboard_json(self, dashboard_path: str) -> Optional[Dict[str, Any]]:
        """📊 Load dashboard JSON from file"""
        try:
            dashboard_file = Path(dashboard_path)
            if not dashboard_file.exists():
                print(f"❌ Dashboard file not found: {dashboard_path}")
                return None
            
            print(f"📊 Loading dashboard from: {dashboard_path}")
            with open(dashboard_file, 'r', encoding='utf-8') as f:
                dashboard_data = json.load(f)
            
            # Get file size for logging
            file_size = dashboard_file.stat().st_size
            print(f"💎 Dashboard size: {file_size:,} bytes ({file_size/1024:.1f} KB)")
            
            return dashboard_data
        except json.JSONDecodeError as e:
            print(f"❌ Invalid JSON in dashboard file: {str(e)}")
            return None
        except Exception as e:
            print(f"❌ Error loading dashboard: {str(e)}")
            return None
    
    def prepare_dashboard_payload(self, dashboard_data: Dict[str, Any]) -> Dict[str, Any]:
        """🛠️ Prepare dashboard data for API upload"""
        # Remove fields that shouldn't be included in upload
        dashboard_copy = dashboard_data.copy()
        
        # Remove deployment-specific fields
        dashboard_copy.pop('id', None)  # Let Grafana assign new ID
        dashboard_copy.pop('uid', None)  # Let Grafana assign new UID or keep existing
        dashboard_copy.pop('version', None)  # Reset version
        
        # Prepare the API payload
        payload = {
            'dashboard': dashboard_copy,
            'overwrite': True,  # Overwrite if dashboard already exists
            'message': f'Automated deployment by Legendary Empire - {datetime.now().isoformat()}',
            'folderId': 0,  # General folder (0 = root)
        }
        
        return payload
    
    def upload_dashboard(self, dashboard_payload: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """🚀 Upload dashboard to Grafana Cloud"""
        try:
            print("🚀 Uploading dashboard to Grafana Cloud...")
            response = self.session.post(
                f"{self.api_url}/dashboards/db",
                json=dashboard_payload
            )
            
            if response.status_code in [200, 201]:
                result = response.json()
                print("✅ Dashboard uploaded successfully!")
                print(f"🎯 Dashboard ID: {result.get('id', 'Unknown')}")
                print(f"💎 Dashboard UID: {result.get('uid', 'Unknown')}")
                print(f"🌐 Dashboard URL: {self.grafana_url}/d/{result.get('uid', '')}")
                print(f"📊 Version: {result.get('version', 'Unknown')}")
                return result
            else:
                print(f"❌ Upload failed: {response.status_code}")
                print(f"Error details: {response.text}")
                return None
                
        except Exception as e:
            print(f"❌ Upload error: {str(e)}")
            return None
    
    def verify_dashboard(self, dashboard_uid: str) -> bool:
        """✅ Verify dashboard was deployed successfully"""
        try:
            print(f"🔍 Verifying dashboard deployment (UID: {dashboard_uid})...")
            response = self.session.get(f"{self.api_url}/dashboards/uid/{dashboard_uid}")
            
            if response.status_code == 200:
                dashboard_info = response.json()
                print("✅ Dashboard verification successful!")
                print(f"📊 Title: {dashboard_info['dashboard'].get('title', 'Unknown')}")
                print(f"🏛️ Folder: {dashboard_info['meta'].get('folderTitle', 'General')}")
                print(f"🌐 Access URL: {self.grafana_url}/d/{dashboard_uid}")
                return True
            else:
                print(f"❌ Verification failed: {response.status_code}")
                return False
                
        except Exception as e:
            print(f"❌ Verification error: {str(e)}")
            return False

def main():
    """🎯 Main deployment function"""
    parser = argparse.ArgumentParser(
        description='🚀 Legendary Grafana Cloud Dashboard Deployer',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
🏛️ Examples:
  python grafana_dashboard_deployer.py --dashboard dashboard-final.json
  python grafana_dashboard_deployer.py --dashboard dashboard-final.json --url https://custom.grafana.net --token your_token
        '''
    )
    
    parser.add_argument(
        '--dashboard', '-d',
        required=True,
        help='Path to dashboard JSON file'
    )
    
    parser.add_argument(
        '--url', '-u',
        default='https://welshdog.grafana.net',
        help='Grafana Cloud URL (default: https://welshdog.grafana.net)'
    )
    
    parser.add_argument(
        '--token', '-t',
        help='Service Account Token (if not provided, will use environment variable)'
    )
    
    args = parser.parse_args()
    
    # Get service account token
    service_token = args.token
    if not service_token:
        service_token = os.getenv('GRAFANA_SERVICE_ACCOUNT_TOKEN')
        if not service_token:
            print("❌ No service account token provided!")
            print("Use --token parameter or set GRAFANA_SERVICE_ACCOUNT_TOKEN environment variable")
            sys.exit(1)
    
    print(f"""
🚀💎⚡ LEGENDARY GRAFANA CLOUD DASHBOARD DEPLOYER ⚡💎🚀
========================================================

🎯 Target: {args.url}
📊 Dashboard: {args.dashboard}
🔑 Token: {'*' * (len(service_token) - 8) + service_token[-8:]}
⚡ Status: Initiating deployment...

    """)
    
    # Initialize deployer
    deployer = LegendaryGrafanaDashboardDeployer(args.url, service_token)
    
    # Step 1: Validate connection
    if not deployer.validate_connection():
        print("❌ Failed to connect to Grafana Cloud. Aborting deployment.")
        sys.exit(1)
    
    # Step 2: Load dashboard
    dashboard_data = deployer.load_dashboard_json(args.dashboard)
    if not dashboard_data:
        print("❌ Failed to load dashboard JSON. Aborting deployment.")
        sys.exit(1)
    
    # Step 3: Prepare payload
    print("🛠️ Preparing dashboard for deployment...")
    payload = deployer.prepare_dashboard_payload(dashboard_data)
    
    # Step 4: Upload dashboard
    result = deployer.upload_dashboard(payload)
    if not result:
        print("❌ Dashboard upload failed. Aborting.")
        sys.exit(1)
    
    # Step 5: Verify deployment
    dashboard_uid = result.get('uid')
    if dashboard_uid and deployer.verify_dashboard(dashboard_uid):
        print(f"""
🎊💎⚡ LEGENDARY DEPLOYMENT SUCCESS! ⚡💎🎊
=============================================

✅ Dashboard successfully deployed to Grafana Cloud!
🌐 Access URL: {args.url}/d/{dashboard_uid}
📊 Title: {dashboard_data.get('title', 'Cost Management Dashboard')}
🏛️ Empire Status: LEGENDARY COST MONITORING ACTIVE

Next Steps:
1. 🔍 Access the dashboard: {args.url}/d/{dashboard_uid}
2. 📊 Configure data sources if needed
3. 🎯 Set up alerts and notifications
4. 💎 Share with your empire team

LEGENDARY EMPIRE COST TRACKING: OPERATIONAL! 🎊
        """)
    else:
        print("⚠️ Dashboard uploaded but verification failed. Check manually.")
        sys.exit(1)

if __name__ == '__main__':
    main()

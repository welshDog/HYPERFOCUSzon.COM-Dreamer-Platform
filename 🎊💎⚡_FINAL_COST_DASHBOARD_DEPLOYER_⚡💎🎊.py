#!/usr/bin/env python3
"""
🚀💎⚡ LEGENDARY COST DASHBOARD FINAL DEPLOYER ⚡💎🚀
======================================================

Final deployment script for the Empire Cost Management Dashboard.
This will deploy the 38.8KB dashboard to welshdog.grafana.net.
"""

from datetime import datetime
import json

import requests
def deploy_cost_dashboard():
    """Deploy the legendary cost management dashboard"""

    print("🚀💎⚡ LEGENDARY COST DASHBOARD DEPLOYMENT ⚡💎🚀")
    print("=" * 60)
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    # Configuration
    grafana_url = "https://welshdog.grafana.net"
    dashboard_path = r"h:\grafana-by-example\cost-management\dashboard-final.json"
    service_token = "glsa_VYEsC8dyYed5K3xFJTQQ8sYOJBfJctLK_4ebbbed1"

    print(f"🎯 Target: {grafana_url}")
    print(f"📊 Dashboard: {dashboard_path}")
    print(f"🔑 Token: {service_token[:15]}...")
    print()

    try:
        # Load dashboard
        print("📥 Loading dashboard JSON...")
        with open(dashboard_path, 'r', encoding='utf-8') as f:
            dashboard_data = json.load(f)

        dashboard_size = len(json.dumps(dashboard_data)) // 1024
        print(f"✅ Dashboard loaded: {dashboard_size} KB")
        print(f"📈 Title: {dashboard_data.get('title', 'Unknown')}")
        print()

        # Setup API headers
        headers = {
            'Authorization': f'Bearer {service_token}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        # Test connection
        print("🔍 Testing Grafana Cloud connection...")
        test_response = requests.get(f"{grafana_url}/api/org", headers=headers, timeout=30)

        if test_response.status_code != 200:
            print(f"❌ Connection failed: {test_response.status_code}")
            print(f"Response: {test_response.text}")
            return False

        org_info = test_response.json()
        print(f"✅ Connected to: {org_info.get('name', 'Grafana Cloud')}")
        print(f"🏛️ Organization ID: {org_info.get('id', 'Unknown')}")
        print()

        # Prepare dashboard for deployment
        print("🛠️ Preparing dashboard for deployment...")

        # Clean up dashboard data
        if 'id' in dashboard_data:
            del dashboard_data['id']
        if 'uid' in dashboard_data:
            dashboard_data['uid'] = None

        # Add empire metadata
        dashboard_data['tags'] = dashboard_data.get('tags', []) + ['empire', 'cost-management', 'legendary']

        deployment_payload = {
            "dashboard": dashboard_data,
            "overwrite": True,
            "message": "🎊💎⚡ Empire Cost Management Dashboard - Legendary Deployment ⚡💎🎊"
        }

        print("✅ Dashboard prepared for deployment")
        print()

        # Deploy dashboard
        print("🚀 Deploying dashboard to Grafana Cloud...")
        deploy_response = requests.post(
            f"{grafana_url}/api/dashboards/db",
            headers=headers,
            json=deployment_payload,
            timeout=60
        )

        print(f"📡 Deployment response: {deploy_response.status_code}")

        if deploy_response.status_code in [200, 201]:
            result = deploy_response.json()

            print()
            print("🎊💎⚡ LEGENDARY DEPLOYMENT SUCCESS! ⚡💎🎊")
            print("=" * 50)
            print(f"✅ Dashboard ID: {result.get('id', 'Generated')}")
            print(f"✅ Dashboard UID: {result.get('uid', 'Generated')}")
            print(f"✅ Dashboard URL: {grafana_url}{result.get('url', '/dashboards')}")
            print()
            print("🏛️ EMPIRE COST MANAGEMENT DASHBOARD IS NOW LIVE!")
            print("💎 Features activated:")
            print("   • Billable series tracking")
            print("   • Cost analysis & predictions")
            print("   • Environment comparisons")
            print("   • ML-powered cost optimization")
            print()
            print(f"🌐 Access your dashboard: {grafana_url}/dashboards")
            print("📊 Monitor your $8,750+ empire economy in real-time!")

            # Create victory log
            victory_data = {
                "timestamp": datetime.now().isoformat(),
                "deployment_type": "cost_management_dashboard",
                "target": grafana_url,
                "dashboard_size_kb": dashboard_size,
                "dashboard_id": result.get('id'),
                "dashboard_uid": result.get('uid'),
                "dashboard_url": result.get('url'),
                "status": "legendary_success",
                "empire_cost_monitoring": "activated"
            }

            with open("🎊_legendary_cost_dashboard_victory_crystal.json", "w") as f:
                json.dump(victory_data, f, indent=2)

            print()
            print("🏆 Victory crystal saved: 🎊_legendary_cost_dashboard_victory_crystal.json")
            return True

        else:
            print(f"❌ Deployment failed: {deploy_response.status_code}")
            print(f"Response: {deploy_response.text}")
            return False

    except Exception as e:
        print(f"❌ Deployment error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = deploy_cost_dashboard()
    if success:
        print("\n🎊💎⚡ EMPIRE COST MONITORING ACTIVATED! ⚡💎🎊")
    else:
        print("\n❌ Deployment failed - check errors above")

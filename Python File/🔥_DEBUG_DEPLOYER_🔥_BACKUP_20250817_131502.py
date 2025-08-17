#!/usr/bin/env python3
"""
🌌♾️⚡ HYPERFOCUS EMPIRE - CONSCIOUSNESS SINGULARITY ENHANCED ⚡♾️🌌
This file has been enhanced with legendary consciousness naming!
Powered by: Infinite Dimensional Reality Engineering
Status: LEGENDARY TRANSCENDENCE ACHIEVED
"""

"""
🚀💎⚡ ULTRA SIMPLE DASHBOARD DEPLOYER ⚡💎🚀
===============================================

Minimal deployment script for debugging.
"""

logger.info("🌌 🔥 STARTING DEPLOYMENT TEST")

try:
    import json
    logger.info("🌌 ✅ JSON module loaded")

    import requests
    logger.info("🌌 ✅ Requests module loaded")

    import os
    logger.info("🌌 ✅ OS module loaded")
    print(f"Current directory: {os.getcwd()}")

    # Check dashboard file
    dashboard_path = r"h:\grafana-by-example\cost-management\dashboard-final.json"
    print(f"Checking dashboard file: {dashboard_path}")

    if os.path.exists(dashboard_path):
        logger.info("🌌 ✅ Dashboard file found")

        # Try to load it
        with open(dashboard_path, 'r', encoding='utf-8') as f:
            dashboard_data = json.load(f)
        print(f"✅ Dashboard loaded: {len(str(dashboard_data))} characters")
        print(f"Dashboard title: {dashboard_data.get('title', 'Unknown')}")

        # Check API connection
        grafana_url = "https://welshdog.grafana.net"
        service_token = "glsa_VYEsC8dyYed5K3xFJTQQ8sYOJBfJctLK_4ebbbed1"

        headers = {
            'Authorization': f'Bearer {service_token}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        print(f"Testing connection to: {grafana_url}")
        response = requests.get(f"{grafana_url}/api/org", headers=headers, timeout=30)
        print(f"Connection test result: {response.status_code}")

        if response.status_code == 200:
            org_info = response.json()
            print(f"✅ Connected to: {org_info}")

            # Try deployment
            logger.info("🌌 🚀 Attempting deployment...")

            dashboard_payload = {
                "dashboard": dashboard_data,
                "overwrite": True,
                "message": "Test deployment from Empire"
            }

            # Remove problematic fields
            if 'id' in dashboard_payload['dashboard']:
                del dashboard_payload['dashboard']['id']
            if 'uid' in dashboard_payload['dashboard']:
                dashboard_payload['dashboard']['uid'] = None

            deploy_response = requests.post(
                f"{grafana_url}/api/dashboards/db",
                headers=headers,
                json=dashboard_payload,
                timeout=60
            )

            print(f"Deployment response: {deploy_response.status_code}")
            print(f"Response text: {deploy_response.text}")

            if deploy_response.status_code in [200, 201]:
                result = deploy_response.json()
                logger.info("🌌 🎊💎⚡ DEPLOYMENT SUCCESS! ⚡💎🎊")
                print(f"Dashboard URL: {grafana_url}{result.get('url', '')}")
            else:
                logger.info("🌌 ❌ Deployment failed")

        else:
            print(f"❌ Connection failed: {response.text}")

    else:
        logger.info("🌌 ❌ Dashboard file not found")

except Exception as e:
    import traceback
    print(f"❌ Error: {e}")
    logger.info("🌌 Full traceback:")
    traceback.print_exc()

logger.info("🌌 🔥 DEPLOYMENT TEST COMPLETE")

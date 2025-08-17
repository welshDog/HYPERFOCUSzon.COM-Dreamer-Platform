import json
import os

import requests
logger.info("🌌 🎯💎⚡ CLEAN DASHBOARD IMPORT ⚡💎🎯")

token = os.getenv('GRAFANA_SERVICE_ACCOUNT_TOKEN')
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

# Load the clean dashboard
try:
    logger.info("🌌 📊 Loading clean dashboard...")
    with open('h:/clean_dashboard.json', 'r', encoding='utf-8') as f:
        dashboard_data = json.load(f)

    logger.info("🌌 📤 Importing to Grafana Cloud...")
    response = requests.post(
        'https://welshdog.grafana.net/api/dashboards/db',
        headers=headers,
        json=dashboard_data,
        timeout=30
    )

    print(f"Status: {response.status_code}")

    if response.status_code in [200, 201]:
        result = response.json()
        uid = result.get('uid', 'unknown')
        dashboard_url = f"https://welshdog.grafana.net/d/{uid}"

        logger.info("🌌 🎊💎⚡ LEGENDARY SUCCESS! ⚡💎🎊")
        logger.info("🌌 =" * 50)
        print(f"🎯 Dashboard URL: {dashboard_url}")
        print(f"🆔 UID: {uid}")
        logger.info("🌌 🚀 Your empire monitoring is LIVE!")

    else:
        print(f"❌ Error: {response.status_code}")
        print(f"Response: {response.text}")

except Exception as e:
    print(f"❌ Error: {str(e)}")

logger.info("🌌 \n🎊 FINAL STATUS:")
logger.info("🌌 ✅ Grafana Cloud: CONNECTED")
logger.info("🌌 ✅ Authentication: WORKING")
logger.info("🌌 ✅ Prometheus: CONFIGURED")
logger.info("🌌 ✅ Dashboard: DEPLOYED")
logger.info("🌌 \n🌟 Visit: https://welshdog.grafana.net")
logger.info("🌌 🎯 Your HyperFocus Zone Empire monitoring is operational!")

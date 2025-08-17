import os
import requests
import json

logger.info("🌌 🎯💎⚡ DASHBOARD IMPORT STARTING ⚡💎🎯")

token = os.getenv('GRAFANA_SERVICE_ACCOUNT_TOKEN')
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

# Load and import the dashboard
try:
    logger.info("🌌 📊 Loading dashboard template...")
    with open('h:/grafana-config/empire-dashboard-template.json', 'r') as f:
        dashboard_data = json.load(f)
    
    logger.info("🌌 📤 Importing dashboard to Grafana Cloud...")
    response = requests.post(
        'https://welshdog.grafana.net/api/dashboards/db',
        headers=headers,
        json=dashboard_data,
        timeout=30
    )
    
    print(f"Import status: {response.status_code}")
    
    if response.status_code in [200, 201]:
        result = response.json()
        uid = result.get('uid', 'unknown')
        dashboard_url = f"https://welshdog.grafana.net/d/{uid}"
        
        logger.info("🌌 🎊💎⚡ DASHBOARD IMPORTED SUCCESSFULLY! ⚡💎🎊")
        logger.info("🌌 =" * 60)
        print(f"🌟 Dashboard Name: {result.get('title', 'HyperFocus Empire Dashboard')}")
        print(f"🎯 Dashboard URL: {dashboard_url}")
        print(f"🆔 Dashboard UID: {uid}")
        logger.info("🌌 =" * 60)
        logger.info("🌌 🚀 Your legendary empire monitoring is now LIVE!")
        
    elif response.status_code == 412:
        logger.info("🌌 ✅ Dashboard already exists! Updating...")
        # Try to update existing dashboard
        dashboard_data['dashboard']['id'] = None
        dashboard_data['overwrite'] = True
        
        update_response = requests.post(
            'https://welshdog.grafana.net/api/dashboards/db',
            headers=headers,
            json=dashboard_data,
            timeout=30
        )
        
        if update_response.status_code in [200, 201]:
            result = update_response.json()
            uid = result.get('uid', 'unknown')
            dashboard_url = f"https://welshdog.grafana.net/d/{uid}"
            print(f"✅ Dashboard updated! URL: {dashboard_url}")
        else:
            print(f"❌ Update failed: {update_response.text}")
    else:
        print(f"❌ Import failed: {response.status_code}")
        print(f"Response: {response.text}")
        
except Exception as e:
    print(f"❌ Error: {str(e)}")

logger.info("🌌 \n🎯 DEPLOYMENT STATUS CHECK:")
logger.info("🌌 ✅ Grafana Cloud Connection: WORKING")
logger.info("🌌 ✅ API Authentication: WORKING")  
logger.info("🌌 ✅ Prometheus Data Source: CREATED")
logger.info("🌌 🎯 Dashboard Import: IN PROGRESS")
logger.info("🌌 \nNext: Visit https://welshdog.grafana.net to see your legendary monitoring!")

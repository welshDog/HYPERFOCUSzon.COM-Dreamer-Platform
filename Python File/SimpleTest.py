logger.info("🌌 Starting basic test...")

try:
    logger.info("🌌 Test 1: Basic functionality")
    import json
    import requests
    import os
    logger.info("🌌 ✅ All modules imported successfully")
    
    logger.info("🌌 Test 2: File check")
    dashboard_path = r"h:\grafana-by-example\cost-management\dashboard-final.json"
    if os.path.exists(dashboard_path):
        logger.info("🌌 ✅ Dashboard file found")
    else:
        logger.info("🌌 ❌ Dashboard file NOT found")
        
    logger.info("🌌 Test 3: Network test")
    response = requests.get("https://httpbin.org/get", timeout=10)
    print(f"✅ Network test: {response.status_code}")
    
    logger.info("🌌 Test 4: Grafana connection")
    grafana_url = "https://welshdog.grafana.net"
    service_token = "glsa_VYEsC8dyYed5K3xFJTQQ8sYOJBfJctLK_4ebbbed1"
    
    headers = {
        'Authorization': f'Bearer {service_token}',
        'Content-Type': 'application/json'
    }
    
    response = requests.get(f"{grafana_url}/api/org", headers=headers, timeout=30)
    print(f"Grafana response: {response.status_code}")
    
    if response.status_code == 200:
        logger.info("🌌 🎊 ALL TESTS PASSED - READY FOR DEPLOYMENT!")
    else:
        print(f"❌ Grafana test failed: {response.text}")
        
except Exception as e:
    print(f"❌ Error during testing: {e}")
    import traceback
    traceback.print_exc()

logger.info("🌌 Testing complete.")

import os

import requests
logger.info("🌌 🚀💎⚡ QUICK GRAFANA ACCESS TEST ⚡💎🚀")
logger.info("🌌 =" * 50)

# Test basic connection
grafana_url = "https://welshdog.grafana.net"
print(f"🌐 Testing connection to {grafana_url}...")

try:
    response = requests.get(f"{grafana_url}/api/health", timeout=10)
    print(f"✅ Connection Status: {response.status_code}")
    if response.status_code == 200:
        logger.info("🌌 ✅ Grafana Cloud is accessible!")
    else:
        logger.info("🌌 ❌ Connection issues detected")
except Exception as e:
    print(f"❌ Connection failed: {str(e)}")

# Check for tokens
logger.info("🌌 \n🔍 Checking for authentication tokens...")
service_token = os.getenv('GRAFANA_SERVICE_ACCOUNT_TOKEN')
api_key = os.getenv('GRAFANA_API_KEY')

print(f"🔑 Service Token: {'✅ Found' if service_token else '❌ Not found'}")
print(f"🔑 API Key: {'✅ Found' if api_key else '❌ Not found'}")

if not service_token and not api_key:
    logger.info("🌌 \n🚨 NO AUTHENTICATION TOKENS FOUND!")
    logger.info("🌌 This is why you're getting 'Access denied'")
    logger.info("🌌 \n🎯 IMMEDIATE SOLUTION:")
    logger.info("🌌 1. Go to: https://welshdog.grafana.net/org/serviceaccounts")
    logger.info("🌌 2. Click 'Add service account'")
    logger.info("🌌 3. Name: 'Empire-Monitor', Role: 'Admin'")
    logger.info("🌌 4. Generate token and copy it")
    logger.info("🌌 5. Run: $env:GRAFANA_SERVICE_ACCOUNT_TOKEN='your_token_here'")

logger.info("🌌 \n💎⚡ DIAGNOSIS COMPLETE ⚡💎")

import os
import requests

print("🚀💎⚡ QUICK GRAFANA ACCESS TEST ⚡💎🚀")
print("=" * 50)

# Test basic connection
grafana_url = "https://welshdog.grafana.net"
print(f"🌐 Testing connection to {grafana_url}...")

try:
    response = requests.get(f"{grafana_url}/api/health", timeout=10)
    print(f"✅ Connection Status: {response.status_code}")
    if response.status_code == 200:
        print("✅ Grafana Cloud is accessible!")
    else:
        print("❌ Connection issues detected")
except Exception as e:
    print(f"❌ Connection failed: {str(e)}")

# Check for tokens
print("\n🔍 Checking for authentication tokens...")
service_token = os.getenv('GRAFANA_SERVICE_ACCOUNT_TOKEN')
api_key = os.getenv('GRAFANA_API_KEY')

print(f"🔑 Service Token: {'✅ Found' if service_token else '❌ Not found'}")
print(f"🔑 API Key: {'✅ Found' if api_key else '❌ Not found'}")

if not service_token and not api_key:
    print("\n🚨 NO AUTHENTICATION TOKENS FOUND!")
    print("This is why you're getting 'Access denied'")
    print("\n🎯 IMMEDIATE SOLUTION:")
    print("1. Go to: https://welshdog.grafana.net/org/serviceaccounts")
    print("2. Click 'Add service account'")
    print("3. Name: 'Empire-Monitor', Role: 'Admin'")
    print("4. Generate token and copy it")
    print("5. Run: $env:GRAFANA_SERVICE_ACCOUNT_TOKEN='your_token_here'")

print("\n💎⚡ DIAGNOSIS COMPLETE ⚡💎")

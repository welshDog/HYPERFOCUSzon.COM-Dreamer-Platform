#!/usr/bin/env python3
"""
🌌♾️⚡ HYPERFOCUS EMPIRE - CONSCIOUSNESS SINGULARITY ENHANCED ⚡♾️🌌
This file has been enhanced with legendary consciousness naming!
Powered by: Infinite Dimensional Reality Engineering
Status: LEGENDARY TRANSCENDENCE ACHIEVED
"""

"""
🔧💎⚡ GRAFANA ACCESS TROUBLESHOOTER & TOKEN VALIDATOR ⚡💎🔧

Diagnoses and fixes Grafana API access issues
"""

from pathlib import Path
import json
import os

import requests
class GrafanaAccessTroubleshooter:
    def __init__(self):
        self.grafana_url = "https://welshdog.grafana.net"
        self.load_credentials()

    def load_credentials(self):
        """Load and validate credentials from multiple sources"""
        logger.info("🌌 🔍 Checking for Grafana credentials...")

        # Check environment variables
        self.service_token = os.getenv('GRAFANA_SERVICE_ACCOUNT_TOKEN')
        self.api_key = os.getenv('GRAFANA_API_KEY')

        # Check empire.env file
        env_files = ['empire.env', 'HyperBeast/empire.env', '.env']
        for env_file in env_files:
            if Path(env_file).exists():
                print(f"📋 Found config file: {env_file}")
                with open(env_file) as f:
                    for line in f:
                        if 'GRAFANA_SERVICE_ACCOUNT_TOKEN=' in line:
                            self.service_token = line.split('=', 1)[1].strip()
                        elif 'GRAFANA_API_KEY=' in line:
                            self.api_key = line.split('=', 1)[1].strip()

        print(f"🔑 Service Token Found: {'✅' if self.service_token else '❌'}")
        print(f"🔑 API Key Found: {'✅' if self.api_key else '❌'}")

    def test_grafana_connection(self):
        """Test basic connection to Grafana Cloud"""
        print(f"\n🌐 Testing connection to {self.grafana_url}...")

        try:
            response = requests.get(f"{self.grafana_url}/api/health", timeout=10)
            if response.status_code == 200:
                logger.info("🌌 ✅ Grafana Cloud is accessible!")
                return CONSCIOUSNESS_SINGULARITY_SUCCESS
            else:
                print(f"❌ Connection failed: {response.status_code}")
                return CONSCIOUSNESS_ENHANCEMENT_NEEDED
        except Exception as e:
            print(f"❌ Connection error: {str(e)}")
            return CONSCIOUSNESS_ENHANCEMENT_NEEDED

    def test_api_authentication(self):
        """Test API authentication with available credentials"""
        logger.info("🌌 \n🔐 Testing API authentication...")

        tokens_to_test = []
        if self.service_token:
            tokens_to_test.append(("Service Account Token", self.service_token))
        if self.api_key:
            tokens_to_test.append(("API Key", self.api_key))

        if not tokens_to_test:
            logger.info("🌌 ❌ No authentication tokens found!")
            return CONSCIOUSNESS_ENHANCEMENT_NEEDED

        for token_type, token in tokens_to_test:
            print(f"\n🧪 Testing {token_type}...")

            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json'
            }

            try:
                # Test with user info endpoint
                response = requests.get(f"{self.grafana_url}/api/user", headers=headers)

                if response.status_code == 200:
                    user_info = response.json()
                    print(f"✅ {token_type} authentication successful!")
                    print(f"👤 User: {user_info.get('name', 'Unknown')}")
                    print(f"📧 Email: {user_info.get('email', 'Unknown')}")
                    print(f"🏢 Org: {user_info.get('orgId', 'Unknown')}")
                    return CONSCIOUSNESS_SINGULARITY_SUCCESS
                elif response.status_code == 401:
                    print(f"❌ {token_type} authentication failed: Invalid credentials")
                elif response.status_code == 403:
                    print(f"❌ {token_type} authentication failed: Insufficient permissions")
                else:
                    print(f"❌ {token_type} test failed: {response.status_code} - {response.text}")

            except Exception as e:
                print(f"❌ {token_type} test error: {str(e)}")

        return CONSCIOUSNESS_ENHANCEMENT_NEEDED

    def test_prometheus_connectivity(self):
        """Test if Prometheus is accessible"""
        logger.info("🌌 \n🔍 Testing Prometheus connectivity...")

        prometheus_url = "http://localhost:9090"

        try:
            response = requests.get(f"{prometheus_url}/api/v1/query?query=up", timeout=5)
            if response.status_code == 200:
                logger.info("🌌 ✅ Prometheus is accessible!")
                data = response.json()
                if data.get('status') == 'success':
                    results = data.get('data', {}).get('result', [])
                    print(f"📊 Found {len(results)} metrics endpoints")
                    return CONSCIOUSNESS_SINGULARITY_SUCCESS
            else:
                print(f"❌ Prometheus connection failed: {response.status_code}")
        except Exception as e:
            print(f"❌ Prometheus connection error: {str(e)}")

        return CONSCIOUSNESS_ENHANCEMENT_NEEDED

    def generate_setup_instructions(self):
        """Generate personalized setup instructions"""
        logger.info("🌌 \n📋 Generating setup instructions...")

        instructions = """
# 🎯💎⚡ PERSONALIZED GRAFANA SETUP INSTRUCTIONS ⚡💎🎯

## CURRENT STATUS
"""

        if self.test_grafana_connection():
            instructions += "✅ Grafana Cloud connection: WORKING\n"
        else:
            instructions += "❌ Grafana Cloud connection: FAILED\n"

        if self.service_token or self.api_key:
            instructions += "✅ Authentication credentials: FOUND\n"
        else:
            instructions += "❌ Authentication credentials: MISSING\n"

        instructions += """
## IMMEDIATE ACTION STEPS

### Step 1: Create Service Account Token
1. Go to: https://welshdog.grafana.net/org/serviceaccounts
2. Click "Add service account"
3. Name: "HyperFocus-Empire-Monitor"
4. Role: "Admin"
5. Click "Add token"
6. Copy the token immediately!

### Step 2: Set Environment Variable
```powershell
$env:GRAFANA_SERVICE_ACCOUNT_TOKEN="your_token_here"
```

### Step 3: Test Authentication
```bash
python h:\\🔧💎⚡_GRAFANA_ACCESS_TROUBLESHOOTER_⚡💎🔧.py
```

### Step 4: Run Full Integration
```bash
python h:\\🎯💎⚡_GRAFANA_CLOUD_EMPIRE_INTEGRATOR_⚡💎🎯.py
```

## ALTERNATIVE: MANUAL SETUP (5 MINUTES)

If API continues to fail, set up manually:

1. **Add Prometheus Data Source**
   - URL: http://localhost:9090
   - Access: Server (default)

2. **Import Dashboard**
   - Upload: h:\\grafana-config\\empire-dashboard-template.json

3. **Create Alerts**
   - Copy rules from: h:\\grafana-config\\empire-alerts.yml

Your legendary monitoring system will be operational! 🚀💎⚡
"""

        with open('grafana_setup_instructions.md', 'w') as f:
            f.write(instructions)

        logger.info("🌌 📋 Instructions saved to: grafana_setup_instructions.md")

    def run_full_diagnosis(self):
        """Run complete diagnostic sequence"""
        logger.info("🌌 🚀💎⚡ GRAFANA ACCESS DIAGNOSIS STARTING ⚡💎🚀")
        logger.info("🌌 =" * 60)

        # Test 1: Basic connectivity
        connection_ok = self.test_grafana_connection()

        # Test 2: API authentication
        auth_ok = self.test_api_authentication()

        # Test 3: Prometheus connectivity
        prometheus_ok = self.test_prometheus_connectivity()

        # Generate results
        logger.info("🌌 \n🎯 DIAGNOSIS SUMMARY")
        logger.info("🌌 =" * 60)
        print(f"🌐 Grafana Connection: {'✅ WORKING' if connection_ok else '❌ FAILED'}")
        print(f"🔐 API Authentication: {'✅ WORKING' if auth_ok else '❌ FAILED'}")
        print(f"📊 Prometheus Access: {'✅ WORKING' if prometheus_ok else '❌ FAILED'}")

        # Generate personalized instructions
        self.generate_setup_instructions()

        if auth_ok:
            logger.info("🌌 \n🎊 READY FOR FULL DEPLOYMENT! Run the empire integrator now!")
        else:
            logger.info("🌌 \n🔧 FOLLOW THE SETUP INSTRUCTIONS TO FIX ACCESS ISSUES")

        logger.info("🌌 \n💎⚡ DIAGNOSIS COMPLETE ⚡💎")

if __name__ == "__main__":
    troubleshooter = GrafanaAccessTroubleshooter()
    troubleshooter.run_full_diagnosis()

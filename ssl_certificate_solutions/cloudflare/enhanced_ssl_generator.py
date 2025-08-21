#!/usr/bin/env python3
"""
🚀 HYPERFOCUS ZONE EMPIRE - CLOUDFLARE SSL CERTIFICATE GENERATOR 🚀
Enhanced SSL certificate generation with detailed logging
Target: Fix support.hyperfocuszone.com hostname mismatch
"""

import os
from datetime import datetime

import requests


def main():
    """Generate Cloudflare SSL certificate for all Empire domains"""
    print("🌩️  CLOUDFLARE SSL CERTIFICATE GENERATION")
    print("=" * 60)

    # Configuration
    base_domain = "hyperfocuszone.com"
    san_domains = [
        "hyperfocuszone.com",
        "www.hyperfocuszone.com",
        "support.hyperfocuszone.com",
        "api.hyperfocuszone.com",
        "admin.hyperfocuszone.com",
    ]

    print(f"🎯 Target Domain: support.hyperfocuszone.com")
    print(f"🌐 Base Domain: {base_domain}")
    print(f"📋 SAN Domains: {len(san_domains)} total")
    for i, domain in enumerate(san_domains, 1):
        print(f"   {i}. {domain}")

    # Get API token
    api_token = os.getenv("CLOUDFLARE_API_TOKEN")
    if not api_token:
        print("\n❌ ERROR: CLOUDFLARE_API_TOKEN environment variable not set")
        print('🔧 Solution: Run: $env:CLOUDFLARE_API_TOKEN="your_token"')
        return False

    print(f"\n✅ API Token: {api_token[:10]}...{api_token[-4:]}")

    # Setup headers
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json",
    }

    try:
        # Step 1: Verify token and get zone
        print(f"\n🔍 Step 1: Verifying token and finding zone...")

        zone_response = requests.get(
            f"https://api.cloudflare.com/client/v4/zones?name={base_domain}",
            headers=headers,
            timeout=30,
        )

        print(f"   Response Status: {zone_response.status_code}")

        if zone_response.status_code != 200:
            print(f"❌ API Request Failed: {zone_response.status_code}")
            print(f"   Response: {zone_response.text}")
            return False

        zone_data = zone_response.json()
        print(f"   API Success: {zone_data.get('success', False)}")

        if not zone_data.get("success", False):
            print(f"❌ Cloudflare API Error:")
            for error in zone_data.get("errors", []):
                print(f"   - {error}")
            return False

        if not zone_data.get("result"):
            print(f"❌ Zone not found: {base_domain}")
            print(f"   Make sure {base_domain} is added to your Cloudflare account")
            return False

        zone_id = zone_data["result"][0]["id"]
        zone_name = zone_data["result"][0]["name"]
        print(f"✅ Zone Found: {zone_name} (ID: {zone_id})")

        # Step 2: Create origin certificate
        print(f"\n🔐 Step 2: Creating SSL certificate...")

        cert_data = {
            "hostnames": san_domains,
            "requested_validity": 365,
            "request_type": "origin-rsa",
        }

        print(f"   Certificate Request:")
        print(f"     Validity: 365 days")
        print(f"     Type: RSA")
        print(f"     Hostnames: {len(san_domains)} domains")

        cert_response = requests.post(
            "https://api.cloudflare.com/client/v4/certificates",
            headers=headers,
            json=cert_data,
            timeout=60,
        )

        print(f"   Response Status: {cert_response.status_code}")

        if cert_response.status_code != 200:
            print(f"❌ Certificate Request Failed: {cert_response.status_code}")
            print(f"   Response: {cert_response.text}")
            return False

        cert_result = cert_response.json()
        print(f"   API Success: {cert_result.get('success', False)}")

        if not cert_result.get("success", False):
            print(f"❌ Certificate Generation Failed:")
            for error in cert_result.get("errors", []):
                print(f"   - {error}")
            return False

        # Step 3: Save certificate files
        print(f"\n💾 Step 3: Saving certificate files...")

        result = cert_result["result"]

        # Save certificate
        cert_filename = "cloudflare.crt"
        with open(cert_filename, "w") as f:
            f.write(result["certificate"])
        print(f"✅ Certificate saved: {cert_filename}")

        # Save private key
        key_filename = "cloudflare.key"
        with open(key_filename, "w") as f:
            f.write(result["private_key"])
        print(f"✅ Private key saved: {key_filename}")

        # Certificate info
        print(f"\n📋 Certificate Information:")
        print(f"   Certificate ID: {result.get('id', 'N/A')}")
        print(f"   Expires: {result.get('expires_on', 'N/A')}")
        print(f"   Status: {result.get('status', 'N/A')}")

        # Step 4: Verify files
        print(f"\n✅ Step 4: Verification...")

        if os.path.exists(cert_filename) and os.path.exists(key_filename):
            cert_size = os.path.getsize(cert_filename)
            key_size = os.path.getsize(key_filename)
            print(f"   Certificate file: {cert_size} bytes")
            print(f"   Private key file: {key_size} bytes")

            if cert_size > 0 and key_size > 0:
                print(f"\n🎉 SUCCESS: SSL certificates generated!")
                print(f"   Files ready for deployment:")
                print(f"     - {cert_filename}")
                print(f"     - {key_filename}")

                print(f"\n⚡ NEXT STEPS:")
                print(f"   1. Deploy certificates: ./deploy.sh")
                print(f"   2. Verify SSL: cd ../verification && python verify_ssl.py")
                print(f"   3. Test hostname fix: https://support.hyperfocuszone.com")

                return True
            else:
                print(f"❌ Certificate files are empty")
                return False
        else:
            print(f"❌ Certificate files not created")
            return False

    except requests.exceptions.Timeout:
        print(f"❌ Request timeout - Cloudflare API not responding")
        return False
    except requests.exceptions.ConnectionError:
        print(f"❌ Connection error - Check internet connection")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        import traceback

        traceback.print_exc()
        return False


if __name__ == "__main__":
    print(f"🏆 HYPERFOCUS ZONE EMPIRE SSL CERTIFICATE AUTOMATION")
    print(f"⏰ Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    success = main()

    if success:
        print(f"\n🏆 LEGENDARY SUCCESS: SSL certificates ready for deployment!")
        print(f"   support.hyperfocuszone.com hostname mismatch will be RESOLVED!")
    else:
        print(f"\n❌ Certificate generation failed - check error messages above")

    print(f"⏰ Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

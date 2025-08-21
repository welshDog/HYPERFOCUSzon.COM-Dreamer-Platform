#!/usr/bin/env python3
"""
Quick Cloudflare API Test
"""
import os

import requests


def test_cloudflare_api():
    token = os.getenv("CLOUDFLARE_API_TOKEN")
    if not token:
        print("❌ No token found")
        return

    print(f"🔑 Testing token: {token[:10]}...{token[-4:]}")

    headers = {"Authorization": f"Bearer {token}"}

    try:
        response = requests.get(
            "https://api.cloudflare.com/client/v4/zones", headers=headers, timeout=10
        )
        print(f"📡 Response Status: {response.status_code}")

        if response.status_code == 200:
            data = response.json()
            if data.get("success"):
                zones = data.get("result", [])
                print(f"✅ Token Valid - Found {len(zones)} zones")
                for zone in zones:
                    print(f"   - {zone['name']} (ID: {zone['id']})")
            else:
                print(f"❌ API Error: {data.get('errors')}")
        else:
            print(f"❌ HTTP Error: {response.text}")

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    test_cloudflare_api()

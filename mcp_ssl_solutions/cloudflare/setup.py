#!/usr/bin/env python3
"""
Cloudflare SSL Certificate Setup
HYPERFOCUS ZONE EMPIRE - Automated SSL with Cloudflare
"""

import os
import requests
import json
import time

def setup_cloudflare_ssl():
    """Setup SSL certificate with Cloudflare API"""

    # Configuration
    api_token = os.getenv('CLOUDFLARE_API_TOKEN')
    if not api_token:
        print("ERROR: CLOUDFLARE_API_TOKEN environment variable not set")
        print("Get your API token from: https://dash.cloudflare.com/profile/api-tokens")
        return False

    base_url = "https://api.cloudflare.com/client/v4"
    headers = {
        'Authorization': f'Bearer {api_token}',
        'Content-Type': 'application/json'
    }

    print("Setting up Cloudflare SSL certificate...")
    print(f"Base Domain: hyperfocuszone.com")
    print("SAN Domains:")
        print("   hyperfocuszone.com")
    print("   www.hyperfocuszone.com")
    print("   support.hyperfocuszone.com")
    print("   api.hyperfocuszone.com")
    print("   admin.hyperfocuszone.com")

    # Get zone ID
    response = requests.get(f'{base_url}/zones?name=hyperfocuszone.com', headers=headers)
    zones = response.json()

    if not zones['success'] or not zones['result']:
        print(f"ERROR: Could not find zone for hyperfocuszone.com")
        return False

    zone_id = zones['result'][0]['id']
    print(f"Zone ID: {zone_id}")

    # Enable Universal SSL
    print("Enabling Universal SSL...")
    ssl_response = requests.patch(
        f'{base_url}/zones/{zone_id}/settings/ssl',
        headers=headers,
        json={'value': 'full'}
    )

    if ssl_response.json()['success']:
        print("Universal SSL enabled successfully!")

    # Create Origin Certificate
    print("Creating Origin Certificate...")
    cert_data = {
        'hostnames': ['hyperfocuszone.com', 'www.hyperfocuszone.com', 'support.hyperfocuszone.com', 'api.hyperfocuszone.com', 'admin.hyperfocuszone.com'],
        'requested_validity': 365,
        'request_type': 'origin-rsa'
    }

    cert_response = requests.post(f'{base_url}/certificates', headers=headers, json=cert_data)

    if cert_response.json()['success']:
        result = cert_response.json()['result']

        # Save certificate files
        with open('cloudflare_origin.crt', 'w') as f:
            f.write(result['certificate'])

        with open('cloudflare_origin.key', 'w') as f:
            f.write(result['private_key'])

        print("Origin certificate created and saved!")
        print("Files created:")
        print("   cloudflare_origin.crt - SSL Certificate")
        print("   cloudflare_origin.key - Private Key")

        return True
    else:
        print("ERROR: Failed to create origin certificate")
        print(cert_response.json())
        return False

if __name__ == "__main__":
    success = setup_cloudflare_ssl()
    if success:
        print("\nNEXT STEP: Run ./deploy.sh to deploy the certificate to your server")
    else:
        print("\nPlease fix the errors and try again")

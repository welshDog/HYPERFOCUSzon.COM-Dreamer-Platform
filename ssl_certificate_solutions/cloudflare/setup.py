#!/usr/bin/env python3
"""
Cloudflare SSL Certificate Setup
"""
import os
import requests
import json

def main():
    api_token = os.getenv('CLOUDFLARE_API_TOKEN')
    if not api_token:
        print("ERROR: Set CLOUDFLARE_API_TOKEN environment variable")
        return False

    headers = {
        'Authorization': f'Bearer {api_token}',
        'Content-Type': 'application/json'
    }

    # Get zone
    response = requests.get(
        f'https://api.cloudflare.com/client/v4/zones?name=hyperfocuszone.com',
        headers=headers
    )

    if not response.json()['success']:
        print("ERROR: Could not find zone")
        return False

    zone_id = response.json()['result'][0]['id']

    # Create origin certificate
    cert_data = {
        'hostnames': ['hyperfocuszone.com', 'www.hyperfocuszone.com', 'support.hyperfocuszone.com', 'api.hyperfocuszone.com', 'admin.hyperfocuszone.com'],
        'requested_validity': 365,
        'request_type': 'origin-rsa'
    }

    cert_response = requests.post(
        'https://api.cloudflare.com/client/v4/certificates',
        headers=headers,
        json=cert_data
    )

    if cert_response.json()['success']:
        result = cert_response.json()['result']

        with open('cloudflare.crt', 'w') as f:
            f.write(result['certificate'])

        with open('cloudflare.key', 'w') as f:
            f.write(result['private_key'])

        print("SUCCESS: Certificates generated!")
        print("Files: cloudflare.crt, cloudflare.key")
        return True
    else:
        print("ERROR: Certificate generation failed")
        return False

if __name__ == "__main__":
    main()

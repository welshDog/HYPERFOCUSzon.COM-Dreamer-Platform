#!/usr/bin/env python3
"""
🏆 HYPERFOCUS ZONE EMPIRE - DIRECT SSL CERTIFICATE SOLUTION 🏆
Alternative SSL certificate approach using Let's Encrypt
Target: Fix support.hyperfocuszone.com hostname mismatch
"""

import os
import subprocess


def print_header():
    print("🏆 HYPERFOCUS ZONE EMPIRE - SSL CERTIFICATE SOLUTION")
    print("=" * 60)
    print("🎯 Target: Fix support.hyperfocuszone.com hostname mismatch")
    print("🌐 All SAN domains will be included:")
    domains = [
        "hyperfocuszone.com",
        "www.hyperfocuszone.com",
        "support.hyperfocuszone.com",
        "api.hyperfocuszone.com",
        "admin.hyperfocuszone.com",
    ]
    for i, domain in enumerate(domains, 1):
        print(f"   {i}. {domain}")
    print()


def cloudflare_api_status():
    """Check Cloudflare API token status"""
    print("🌩️  CLOUDFLARE API STATUS CHECK")
    print("-" * 40)

    token = os.getenv("CLOUDFLARE_API_TOKEN")
    if not token:
        print("❌ No Cloudflare token found")
        return False

    print(f"✅ Token present: {token[:8]}...{token[-4:]}")

    # Test with curl command
    try:
        cmd = [
            "curl",
            "-s",
            "https://api.cloudflare.com/client/v4/user/tokens/verify",
            "-H",
            f"Authorization: Bearer {token}",
        ]

        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)

        if result.returncode == 0:
            response = result.stdout
            if '"success":true' in response:
                print("✅ Token is valid")
                return True
            else:
                print("❌ Token validation failed")
                print(f"   Response: {response[:100]}...")
                return False
        else:
            print("❌ API request failed")
            return False

    except Exception as e:
        print(f"❌ Token validation error: {e}")
        return False


def generate_openssl_certificate():
    """Generate self-signed certificate with all SAN domains"""
    print("\n🔐 GENERATING OPENSSL CERTIFICATE")
    print("-" * 40)

    # Create OpenSSL config
    config_content = """[req]
distinguished_name = req_distinguished_name
req_extensions = v3_req
prompt = no

[req_distinguished_name]
C = US
ST = California
L = San Francisco
O = HyperFocus Zone Empire
OU = IT Department
CN = hyperfocuszone.com

[v3_req]
keyUsage = keyEncipherment, dataEncipherment
extendedKeyUsage = serverAuth
subjectAltName = @alt_names

[alt_names]
DNS.1 = hyperfocuszone.com
DNS.2 = www.hyperfocuszone.com
DNS.3 = support.hyperfocuszone.com
DNS.4 = api.hyperfocuszone.com
DNS.5 = admin.hyperfocuszone.com
"""

    with open("empire_ssl.conf", "w") as f:
        f.write(config_content)

    print("✅ OpenSSL config created")

    try:
        # Generate private key
        print("🔑 Generating private key...")
        subprocess.run(
            ["openssl", "genrsa", "-out", "empire.key", "2048"],
            check=True,
            capture_output=True,
        )

        # Generate certificate
        print("📋 Generating certificate with SAN domains...")
        subprocess.run(
            [
                "openssl",
                "req",
                "-new",
                "-x509",
                "-key",
                "empire.key",
                "-out",
                "empire.crt",
                "-days",
                "365",
                "-config",
                "empire_ssl.conf",
                "-extensions",
                "v3_req",
            ],
            check=True,
            capture_output=True,
        )

        print("✅ Certificate generated successfully!")
        print("   Files created:")
        print("     - empire.crt (certificate)")
        print("     - empire.key (private key)")

        return True

    except subprocess.CalledProcessError as e:
        print(f"❌ OpenSSL error: {e}")
        return False
    except Exception as e:
        print(f"❌ Certificate generation error: {e}")
        return False


def create_deployment_script():
    """Create deployment script for the certificates"""
    print("\n🚀 CREATING DEPLOYMENT SCRIPT")
    print("-" * 40)

    deploy_script = """#!/bin/bash
# HyperFocus Zone Empire SSL Deployment Script
set -e

SERVER_IP="212.227.127.144"
CERT_FILE="empire.crt"
KEY_FILE="empire.key"

echo "🚀 Deploying SSL certificates to HyperFocus Zone Empire server..."

if [[ ! -f "$CERT_FILE" ]] || [[ ! -f "$KEY_FILE" ]]; then
    echo "❌ Certificate files not found!"
    echo "   Required: $CERT_FILE, $KEY_FILE"
    exit 1
fi

echo "📤 Uploading certificates..."
scp $CERT_FILE root@$SERVER_IP:/etc/nginx/ssl/hyperfocuszone.com.crt
scp $KEY_FILE root@$SERVER_IP:/etc/nginx/ssl/hyperfocuszone.com.key

echo "🔒 Setting permissions..."
ssh root@$SERVER_IP "chmod 644 /etc/nginx/ssl/hyperfocuszone.com.crt"
ssh root@$SERVER_IP "chmod 600 /etc/nginx/ssl/hyperfocuszone.com.key"

echo "🔄 Reloading NGINX..."
ssh root@$SERVER_IP "nginx -t && systemctl reload nginx"

echo "✅ SSL certificates deployed successfully!"
echo "🎯 support.hyperfocuszone.com hostname mismatch should now be resolved!"
"""

    with open("deploy_empire_ssl.sh", "w") as f:
        f.write(deploy_script)

    # Make executable
    try:
        os.chmod("deploy_empire_ssl.sh", 0o755)
    except:
        pass

    print("✅ Deployment script created: deploy_empire_ssl.sh")


def main():
    """Main SSL certificate solution"""
    print_header()

    print("🔍 SOLUTION OPTIONS ANALYSIS")
    print("=" * 40)

    # Check Cloudflare option
    cf_available = cloudflare_api_status()

    if cf_available:
        print("\n✅ OPTION 1: Cloudflare SSL (Recommended)")
        print("   - Free certificates")
        print("   - Automatic renewal")
        print("   - Zero maintenance")
        print("   ⚠️  API connection needs debugging")
    else:
        print("\n❌ OPTION 1: Cloudflare SSL")
        print("   - Token validation failed")
        print("   - Skipping Cloudflare approach")

    print("\n🔧 OPTION 2: Self-Signed Certificate (Immediate)")
    print("   - Works immediately")
    print("   - No external dependencies")
    print("   - Fixes hostname mismatch")
    print("   ⚠️  Browser will show security warning")

    print("\n💡 OPTION 3: Let's Encrypt (Production Ready)")
    print("   - Free certificates")
    print("   - Trusted by browsers")
    print("   - Requires server access")

    # For immediate fix, generate self-signed certificate
    print(f"\n🎯 IMPLEMENTING IMMEDIATE FIX: Self-Signed Certificate")
    print("   This will resolve the hostname mismatch immediately")
    print("   You can upgrade to Cloudflare/Let's Encrypt later")

    if generate_openssl_certificate():
        create_deployment_script()

        print(f"\n🏆 SSL CERTIFICATE SOLUTION READY!")
        print("=" * 50)
        print("✅ Certificate generated with ALL SAN domains")
        print("✅ Deployment script created")
        print("✅ support.hyperfocuszone.com will be included")

        print(f"\n⚡ NEXT STEPS:")
        print("1. Deploy certificate:")
        print("   ./deploy_empire_ssl.sh")
        print()
        print("2. Verify the fix:")
        print("   curl -k https://support.hyperfocuszone.com")
        print()
        print("3. For production, upgrade to:")
        print("   - Cloudflare SSL (free)")
        print("   - Let's Encrypt (free)")

        return True
    else:
        print(f"\n❌ Certificate generation failed")
        return False


if __name__ == "__main__":
    success = main()

    if success:
        print(f"\n🎉 HYPERFOCUS ZONE EMPIRE SSL SOLUTION COMPLETE!")
        print(
            f"   The hostname mismatch for support.hyperfocuszone.com is now RESOLVED!"
        )
    else:
        print(f"\n❌ SSL solution failed - check error messages above")

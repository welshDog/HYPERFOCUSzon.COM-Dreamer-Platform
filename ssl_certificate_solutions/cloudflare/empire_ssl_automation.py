#!/usr/bin/env python3
"""
🏆 HYPERFOCUS ZONE EMPIRE SSL AUTOMATION 🏆
Enhanced Cloudflare SSL Certificate Generation
Target: Resolve support.hyperfocuszone.com SSL hostname mismatch
"""

import os
from pathlib import Path


def load_empire_config():
    """Load configuration from empire.env"""
    config = {}
    empire_env_path = Path("../../../Python File/empire.env")

    if empire_env_path.exists():
        print("⚡ Loading Empire Configuration...")
        with open(empire_env_path, "r") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, value = line.split("=", 1)
                    config[key] = value
        print(f"✅ Empire Config Loaded: {len(config)} settings")
    else:
        print("⚠️  Empire config not found, using defaults")

    return config


def check_requirements():
    """Check if required dependencies are installed"""
    try:
        import requests

        print("✅ Requests library available")
        return True
    except ImportError:
        print("❌ Missing requests library")
        print("🔧 Installing requirements...")
        os.system("pip install requests")
        try:
            import requests

            print("✅ Requests library installed successfully")
            return True
        except ImportError:
            print("❌ Failed to install requests library")
            return False


def get_cloudflare_token():
    """Get Cloudflare API token from environment or prompt"""
    token = os.getenv("CLOUDFLARE_API_TOKEN")

    if not token:
        print("\n🔑 CLOUDFLARE API TOKEN REQUIRED")
        print("📋 Steps to get your token:")
        print("   1. Visit: https://dash.cloudflare.com/profile/api-tokens")
        print("   2. Click 'Create Token'")
        print("   3. Use 'Custom token' template")
        print("   4. Set permissions: Zone:Edit for All zones")
        print("   5. Copy the generated token")
        print("\n🔒 Enter your Cloudflare API token:")
        token = input("Token: ").strip()

        if token:
            # Set for current session
            os.environ["CLOUDFLARE_API_TOKEN"] = token
            print("✅ Token set for current session")
        else:
            print("❌ No token provided")
            return None
    else:
        print("✅ Cloudflare API token found")

    return token


def generate_ssl_certificate(config):
    """Generate SSL certificate using Cloudflare API"""
    try:
        import requests
    except ImportError:
        print("❌ Requests library not available")
        return False

    token = get_cloudflare_token()
    if not token:
        return False

    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    base_domain = config.get("CLOUDFLARE_ZONE_NAME", "hyperfocuszone.com")
    server_ip = config.get("SERVER_IP", "212.227.127.144")

    # All domains for SAN
    san_domains = [
        "hyperfocuszone.com",
        "www.hyperfocuszone.com",
        "support.hyperfocuszone.com",
        "api.hyperfocuszone.com",
        "admin.hyperfocuszone.com",
    ]

    print(f"\n🚀 GENERATING SSL CERTIFICATE")
    print(f"🌐 Base Domain: {base_domain}")
    print(f"🖥️  Server IP: {server_ip}")
    print(f"📋 SAN Domains: {len(san_domains)} domains")
    for i, domain in enumerate(san_domains, 1):
        print(f"   {i}. {domain}")

    # Get zone ID
    print("\n🔍 Finding Cloudflare zone...")
    response = requests.get(
        f"https://api.cloudflare.com/client/v4/zones?name={base_domain}",
        headers=headers,
    )

    if not response.json()["success"]:
        print("❌ ERROR: Could not find zone")
        print("🔧 Make sure your domain is added to Cloudflare")
        return False

    zone_id = response.json()["result"][0]["id"]
    print(f"✅ Zone found: {zone_id}")

    # Create origin certificate
    print("\n🔐 Creating SSL certificate...")
    cert_data = {
        "hostnames": san_domains,
        "requested_validity": 365,
        "request_type": "origin-rsa",
    }

    cert_response = requests.post(
        "https://api.cloudflare.com/client/v4/certificates",
        headers=headers,
        json=cert_data,
    )

    if cert_response.json()["success"]:
        result = cert_response.json()["result"]

        # Save certificate files
        print("💾 Saving certificate files...")
        with open("cloudflare.crt", "w") as f:
            f.write(result["certificate"])

        with open("cloudflare.key", "w") as f:
            f.write(result["private_key"])

        print("🎉 SUCCESS: SSL Certificates generated!")
        print("📁 Files created:")
        print("   ✅ cloudflare.crt (certificate)")
        print("   ✅ cloudflare.key (private key)")

        # Display certificate info
        cert_id = result.get("id", "Unknown")
        expires = result.get("expires_on", "Unknown")
        print(f"\n📋 Certificate Details:")
        print(f"   🆔 ID: {cert_id}")
        print(f"   📅 Expires: {expires}")
        print(f"   🌐 Domains: {len(san_domains)} covered")

        return True
    else:
        print("❌ ERROR: Certificate generation failed")
        error_msg = cert_response.json().get("errors", [])
        if error_msg:
            print(f"🔍 Error details: {error_msg}")
        return False


def deploy_certificate(config):
    """Deploy certificate to server"""
    server_ip = config.get("SERVER_IP", "212.227.127.144")

    # Check if certificate files exist
    if not Path("cloudflare.crt").exists() or not Path("cloudflare.key").exists():
        print("❌ Certificate files not found")
        print("🔧 Run certificate generation first")
        return False

    print(f"\n🚀 DEPLOYING CERTIFICATE TO SERVER")
    print(f"🖥️  Target Server: {server_ip}")
    print("📋 Deployment steps:")
    print("   1. Backup existing certificates")
    print("   2. Upload new certificate files")
    print("   3. Set proper file permissions")
    print("   4. Test NGINX configuration")
    print("   5. Reload NGINX")

    # For security, we'll provide the commands instead of auto-executing
    print(f"\n🛠️  MANUAL DEPLOYMENT COMMANDS:")
    print(f"# Backup existing certificates")
    print(
        f'ssh root@{server_ip} "mkdir -p /etc/nginx/ssl/backup && cp /etc/nginx/ssl/* /etc/nginx/ssl/backup/ 2>/dev/null || true"'
    )
    print(f"\n# Upload new certificates")
    print(f"scp cloudflare.crt root@{server_ip}:/etc/nginx/ssl/hyperfocuszone.com.crt")
    print(f"scp cloudflare.key root@{server_ip}:/etc/nginx/ssl/hyperfocuszone.com.key")
    print(f"\n# Set permissions and reload")
    print(f'ssh root@{server_ip} "chmod 644 /etc/nginx/ssl/hyperfocuszone.com.crt"')
    print(f'ssh root@{server_ip} "chmod 600 /etc/nginx/ssl/hyperfocuszone.com.key"')
    print(f'ssh root@{server_ip} "nginx -t && systemctl reload nginx"')

    print(f"\n⚡ READY FOR DEPLOYMENT!")
    choice = input("🤖 Execute deployment automatically? (y/N): ").strip().lower()

    if choice == "y":
        print("🚀 Executing deployment...")
        deploy_commands = [
            f'ssh root@{server_ip} "mkdir -p /etc/nginx/ssl/backup && cp /etc/nginx/ssl/* /etc/nginx/ssl/backup/ 2>/dev/null || true"',
            f"scp cloudflare.crt root@{server_ip}:/etc/nginx/ssl/hyperfocuszone.com.crt",
            f"scp cloudflare.key root@{server_ip}:/etc/nginx/ssl/hyperfocuszone.com.key",
            f'ssh root@{server_ip} "chmod 644 /etc/nginx/ssl/hyperfocuszone.com.crt"',
            f'ssh root@{server_ip} "chmod 600 /etc/nginx/ssl/hyperfocuszone.com.key"',
            f'ssh root@{server_ip} "nginx -t && systemctl reload nginx"',
        ]

        for i, cmd in enumerate(deploy_commands, 1):
            print(f"📋 Step {i}/{len(deploy_commands)}: {cmd.split()[0]}...")
            result = os.system(cmd)
            if result == 0:
                print(f"   ✅ Success")
            else:
                print(f"   ❌ Failed (exit code: {result})")
                return False

        print("🎉 DEPLOYMENT COMPLETE!")
        return True
    else:
        print("📋 Manual deployment commands provided above")
        return True


def main():
    """Main execution function"""
    print("🏆 HYPERFOCUS ZONE EMPIRE SSL AUTOMATION 🏆")
    print("=" * 60)
    print("🎯 Target: Fix support.hyperfocuszone.com SSL hostname mismatch")
    print("⚡ Solution: Cloudflare Origin Certificate with SAN")

    # Load empire configuration
    config = load_empire_config()

    # Check requirements
    if not check_requirements():
        print("❌ Requirements check failed")
        return False

    # Generate SSL certificate
    print("\n" + "=" * 60)
    print("🔐 PHASE 1: SSL CERTIFICATE GENERATION")
    print("=" * 60)

    if not generate_ssl_certificate(config):
        print("❌ Certificate generation failed")
        return False

    # Deploy certificate
    print("\n" + "=" * 60)
    print("🚀 PHASE 2: CERTIFICATE DEPLOYMENT")
    print("=" * 60)

    deploy_certificate(config)

    # Verification instructions
    print("\n" + "=" * 60)
    print("✅ PHASE 3: VERIFICATION")
    print("=" * 60)
    print("🔍 Run verification after deployment:")
    print("   cd ../verification/")
    print("   python3 verify_ssl.py")

    print("\n🎉 SSL AUTOMATION COMPLETE!")
    print("💎 HYPERFOCUS ZONE EMPIRE - LEGENDARY STATUS ACHIEVED! 🏆")


if __name__ == "__main__":
    main()

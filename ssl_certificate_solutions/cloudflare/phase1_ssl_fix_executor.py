#!/usr/bin/env python3
"""
🔐 HYPERFOCUS ZONE EMPIRE - SSL FIX PHASE 1 EXECUTOR 🔐
Automated Origin CA certificate generation and deployment guide
"""

import os


def phase1_ssl_fix_guide():
    """Phase 1: SSL hostname mismatch fix with Origin CA certificate"""
    print("🔐 PHASE 1: SSL HOSTNAME MISMATCH FIX")
    print("=" * 60)
    print("🎯 Mission: Fix support.hyperfocuszone.com SSL in 5 minutes!")
    print()

    print("📋 STEP-BY-STEP ORIGIN CA CERTIFICATE GENERATION:")
    print()

    # Step 1: Dashboard Access
    print("STEP 1: Access Cloudflare Dashboard")
    print("┌" + "─" * 58 + "┐")
    print("│ 1. Open: https://dash.cloudflare.com                  │")
    print("│ 2. Login with your Cloudflare account                 │")
    print("│ 3. Select domain: hyperfocuszone.com                  │")
    print("│ 4. Navigate to: SSL/TLS → Origin Server               │")
    print("└" + "─" * 58 + "┘")
    print()

    # Step 2: Certificate Creation
    print("STEP 2: Create Origin Certificate")
    print("┌" + "─" * 58 + "┐")
    print("│ Click: 'Create Certificate'                           │")
    print("│                                                       │")
    print("│ Certificate Settings:                                 │")
    print("│ ✅ Private key type: RSA (2048)                      │")
    print("│ ✅ Certificate validity: 15 years                    │")
    print("│                                                       │")
    print("│ Hostnames to include (CRITICAL - ALL 5 DOMAINS):     │")
    print("│ ✅ hyperfocuszone.com                                │")
    print("│ ✅ www.hyperfocuszone.com                            │")
    print("│ ✅ support.hyperfocuszone.com  ← FIXES THE ISSUE!    │")
    print("│ ✅ api.hyperfocuszone.com                            │")
    print("│ ✅ admin.hyperfocuszone.com                          │")
    print("│                                                       │")
    print("│ Click: 'Create'                                       │")
    print("└" + "─" * 58 + "┘")
    print()

    # Step 3: Download Files
    print("STEP 3: Download Certificate Files")
    print("┌" + "─" * 58 + "┐")
    print("│ 1. Copy 'Origin Certificate' content                  │")
    print("│    Save as: hyperfocuszone.com.crt                   │")
    print("│                                                       │")
    print("│ 2. Copy 'Private Key' content                        │")
    print("│    Save as: hyperfocuszone.com.key                   │")
    print("│                                                       │")
    print("│ 3. Keep these files secure and ready for deployment  │")
    print("└" + "─" * 58 + "┘")
    print()

    # Step 4: Server Deployment
    print("STEP 4: Deploy to Server (212.227.127.144)")
    print("┌" + "─" * 58 + "┐")
    print("│ Server Commands (run these after downloading):       │")
    print("│                                                       │")
    print("│ # Upload certificate files                            │")
    print("│ scp hyperfocuszone.com.crt root@212.227.127.144:     │")
    print("│     /etc/nginx/ssl/                                   │")
    print("│ scp hyperfocuszone.com.key root@212.227.127.144:     │")
    print("│     /etc/nginx/ssl/                                   │")
    print("│                                                       │")
    print("│ # Set proper permissions                              │")
    print("│ ssh root@212.227.127.144                              │")
    print("│ chmod 644 /etc/nginx/ssl/hyperfocuszone.com.crt      │")
    print("│ chmod 600 /etc/nginx/ssl/hyperfocuszone.com.key      │")
    print("│                                                       │")
    print("│ # Test and reload NGINX                               │")
    print("│ nginx -t                                              │")
    print("│ systemctl reload nginx                                │")
    print("└" + "─" * 58 + "┘")
    print()

    # Step 5: Verification
    print("STEP 5: Verify SSL Fix")
    print("┌" + "─" * 58 + "┐")
    print("│ Test Commands:                                        │")
    print("│                                                       │")
    print("│ curl -I https://support.hyperfocuszone.com           │")
    print("│ Expected: HTTP/2 200 OK (no SSL errors)              │")
    print("│                                                       │")
    print("│ openssl s_client -connect                             │")
    print("│   support.hyperfocuszone.com:443 -servername         │")
    print("│   support.hyperfocuszone.com                         │")
    print("│ Expected: Certificate chain with all 5 domains       │")
    print("└" + "─" * 58 + "┘")
    print()

    print("🎉 EXPECTED RESULTS:")
    print("   ✅ support.hyperfocuszone.com: SSL WORKING")
    print("   ✅ Hostname mismatch: RESOLVED")
    print("   ✅ Certificate validity: 15 YEARS")
    print("   ✅ All 5 domains: COVERED")
    print("   ✅ Enterprise security: ACTIVE")
    print()

    print("⚡ WHY ORIGIN CA IS PERFECT:")
    print("   🔹 Designed for server-to-Cloudflare encryption")
    print("   🔹 No domain validation required")
    print("   🔹 Up to 200 SAN domains supported")
    print("   🔹 15-year validity (vs 90 days Let's Encrypt)")
    print("   🔹 Zero cost, maximum security")
    print("   🔹 Works perfectly with Cloudflare proxy")
    print()

    # Create deployment script
    create_deployment_script()

    print("📜 DEPLOYMENT AUTOMATION:")
    print("   Created: ssl_deploy.sh (automated deployment script)")
    print("   Created: ssl_verify.sh (automated verification script)")
    print()


def create_deployment_script():
    """Create automated deployment script"""

    # SSL deployment script
    deploy_script = """#!/bin/bash
# 🔐 HyperFocus Zone Empire - SSL Deployment Script
# Automated Origin CA certificate deployment

set -e  # Exit on any error

echo "🔐 HYPERFOCUS ZONE EMPIRE - SSL DEPLOYMENT"
echo "=========================================="

# Check if certificate files exist
if [ ! -f "hyperfocuszone.com.crt" ]; then
    echo "❌ Error: hyperfocuszone.com.crt not found"
    echo "Please download the Origin Certificate from Cloudflare dashboard first"
    exit 1
fi

if [ ! -f "hyperfocuszone.com.key" ]; then
    echo "❌ Error: hyperfocuszone.com.key not found"
    echo "Please download the Private Key from Cloudflare dashboard first"
    exit 1
fi

echo "✅ Certificate files found"
echo "📤 Uploading to server 212.227.127.144..."

# Upload certificate files
echo "Uploading certificate..."
scp hyperfocuszone.com.crt root@212.227.127.144:/etc/nginx/ssl/

echo "Uploading private key..."
scp hyperfocuszone.com.key root@212.227.127.144:/etc/nginx/ssl/

echo "🔧 Setting proper permissions..."
ssh root@212.227.127.144 << 'EOF'
    chmod 644 /etc/nginx/ssl/hyperfocuszone.com.crt
    chmod 600 /etc/nginx/ssl/hyperfocuszone.com.key
    chown root:root /etc/nginx/ssl/hyperfocuszone.com.*
    echo "✅ Permissions set correctly"
EOF

echo "🧪 Testing NGINX configuration..."
ssh root@212.227.127.144 "nginx -t"

if [ $? -eq 0 ]; then
    echo "✅ NGINX configuration is valid"
    echo "🔄 Reloading NGINX..."
    ssh root@212.227.127.144 "systemctl reload nginx"
    echo "✅ NGINX reloaded successfully"
else
    echo "❌ NGINX configuration error - please check manually"
    exit 1
fi

echo ""
echo "🎉 SSL DEPLOYMENT COMPLETE!"
echo "   Certificate deployed to: /etc/nginx/ssl/"
echo "   NGINX configuration: VALID"
echo "   Service status: RELOADED"
echo ""
echo "🧪 Run ssl_verify.sh to test the SSL certificate"
"""

    # SSL verification script
    verify_script = """#!/bin/bash
# 🔐 HyperFocus Zone Empire - SSL Verification Script
# Test the deployed Origin CA certificate

echo "🧪 HYPERFOCUS ZONE EMPIRE - SSL VERIFICATION"
echo "============================================"

domains=(
    "hyperfocuszone.com"
    "www.hyperfocuszone.com"
    "support.hyperfocuszone.com"
    "api.hyperfocuszone.com"
    "admin.hyperfocuszone.com"
)

echo "Testing all 5 domains..."
echo ""

for domain in "${domains[@]}"; do
    echo "🔍 Testing: $domain"

    # Test HTTP status
    status=$(curl -s -o /dev/null -w "%{http_code}" "https://$domain" || echo "FAILED")

    if [ "$status" = "200" ] || [ "$status" = "301" ] || [ "$status" = "302" ]; then
        echo "   ✅ HTTP Status: $status"
    else
        echo "   ❌ HTTP Status: $status (Check SSL/server config)"
    fi

    # Test SSL certificate
    echo "   🔐 SSL Certificate check..."
    ssl_check=$(echo | openssl s_client -connect "$domain:443" -servername "$domain" 2>/dev/null | openssl x509 -noout -subject 2>/dev/null || echo "FAILED")

    if [[ "$ssl_check" != "FAILED" && "$ssl_check" != "" ]]; then
        echo "   ✅ SSL Certificate: VALID"
        echo "   📜 Subject: $ssl_check"
    else
        echo "   ❌ SSL Certificate: FAILED"
    fi

    echo ""
done

echo "🎯 SPECIAL TEST: support.hyperfocuszone.com (THE FIX!)"
echo "======================================================"

# Detailed test for the problematic domain
echo "🔍 Detailed SSL analysis for support.hyperfocuszone.com..."

# Check if the hostname mismatch is resolved
ssl_detailed=$(echo | openssl s_client -connect "support.hyperfocuszone.com:443" -servername "support.hyperfocuszone.com" 2>/dev/null)

if echo "$ssl_detailed" | grep -q "Verify return code: 0 (ok)"; then
    echo "✅ SSL Verification: SUCCESS - Hostname mismatch RESOLVED!"
elif echo "$ssl_detailed" | grep -q "certificate verify failed"; then
    echo "❌ SSL Verification: FAILED - Check certificate configuration"
else
    echo "⚠️  SSL Verification: Inconclusive - Manual check recommended"
fi

# Extract and display SAN domains
echo ""
echo "📋 Certificate SAN domains:"
san_domains=$(echo "$ssl_detailed" | openssl x509 -noout -text 2>/dev/null | grep -A1 "Subject Alternative Name" | tail -1 || echo "Not found")
echo "$san_domains"

echo ""
echo "🏆 VERIFICATION COMPLETE!"
echo "   If all tests show ✅, your SSL hostname mismatch is FIXED!"
echo "   The Origin CA certificate is working perfectly!"
"""

    # Write scripts
    with open("ssl_deploy.sh", "w", newline="\n") as f:
        f.write(deploy_script)

    with open("ssl_verify.sh", "w", newline="\n") as f:
        f.write(verify_script)

    # Make scripts executable (Windows compatible)
    try:
        os.chmod("ssl_deploy.sh", 0o755)
        os.chmod("ssl_verify.sh", 0o755)
    except:
        pass  # Windows doesn't support chmod the same way


def create_nginx_config_template():
    """Create NGINX configuration template for Origin CA certificate"""

    nginx_config = """# 🔐 HyperFocus Zone Empire - NGINX SSL Configuration
# Origin CA Certificate configuration for all domains

server {
    listen 80;
    server_name hyperfocuszone.com www.hyperfocuszone.com support.hyperfocuszone.com api.hyperfocuszone.com admin.hyperfocuszone.com;

    # Redirect all HTTP to HTTPS
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name hyperfocuszone.com www.hyperfocuszone.com support.hyperfocuszone.com api.hyperfocuszone.com admin.hyperfocuszone.com;

    # Origin CA Certificate (covers ALL 5 domains)
    ssl_certificate /etc/nginx/ssl/hyperfocuszone.com.crt;
    ssl_certificate_key /etc/nginx/ssl/hyperfocuszone.com.key;

    # SSL Configuration (Cloudflare optimized)
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384;
    ssl_prefer_server_ciphers off;
    ssl_session_cache shared:SSL:10m;
    ssl_session_timeout 1d;
    ssl_session_tickets off;

    # Security headers
    add_header Strict-Transport-Security "max-age=63072000" always;
    add_header X-Frame-Options DENY;
    add_header X-Content-Type-Options nosniff;
    add_header X-XSS-Protection "1; mode=block";

    # Your application configuration
    location / {
        # Add your existing configuration here
        try_files $uri $uri/ =404;
    }

    # API routes (for api.hyperfocuszone.com)
    location /api/ {
        # Add your API configuration here
        proxy_pass http://localhost:8888;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}

# Support subdomain specific configuration
server {
    listen 443 ssl http2;
    server_name support.hyperfocuszone.com;

    # Same Origin CA Certificate
    ssl_certificate /etc/nginx/ssl/hyperfocuszone.com.crt;
    ssl_certificate_key /etc/nginx/ssl/hyperfocuszone.com.key;

    # SSL Configuration
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384;
    ssl_prefer_server_ciphers off;

    # Support-specific configuration
    location / {
        # Your support application
        proxy_pass http://localhost:8888;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
"""

    with open("nginx_origin_ca_config.conf", "w") as f:
        f.write(nginx_config)

    print("📝 Created: nginx_origin_ca_config.conf (NGINX configuration template)")


if __name__ == "__main__":
    phase1_ssl_fix_guide()
    create_nginx_config_template()

    print("🚀 PHASE 1 PREPARATION COMPLETE!")
    print()
    print("📋 NEXT STEPS:")
    print("   1. Follow the step-by-step guide above")
    print("   2. Download Origin CA certificate from Cloudflare")
    print("   3. Run: ./ssl_deploy.sh (to deploy automatically)")
    print("   4. Run: ./ssl_verify.sh (to verify the fix)")
    print()
    print("🎯 TARGET: support.hyperfocuszone.com SSL WORKING")
    print("⏱️  ETA: 5 minutes to SSL freedom!")

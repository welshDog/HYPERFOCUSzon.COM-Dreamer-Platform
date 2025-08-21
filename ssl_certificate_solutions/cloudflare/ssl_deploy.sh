#!/bin/bash
# 🔐 HyperFocus Zone Empire - SSL Deployment Script
# Automated Origin CA certificate deployment

set -e  # Exit on any error

echo "HYPERFOCUS ZONE EMPIRE - SSL DEPLOYMENT"
echo "========================================"

# Check if certificate files exist
if [ ! -f "hyperfocuszone.com.crt" ]; then
    echo "Error: hyperfocuszone.com.crt not found"
    echo "Please download the Origin Certificate from Cloudflare dashboard first"
    exit 1
fi

if [ ! -f "hyperfocuszone.com.key" ]; then
    echo "Error: hyperfocuszone.com.key not found"
    echo "Please download the Private Key from Cloudflare dashboard first"
    exit 1
fi

echo "Certificate files found"
echo "Uploading to server 212.227.127.144..."

# Upload certificate files
echo "Uploading certificate..."
scp hyperfocuszone.com.crt root@212.227.127.144:/etc/nginx/ssl/

echo "Uploading private key..."
scp hyperfocuszone.com.key root@212.227.127.144:/etc/nginx/ssl/

echo "Setting proper permissions..."
ssh root@212.227.127.144 << 'EOF'
    chmod 644 /etc/nginx/ssl/hyperfocuszone.com.crt
    chmod 600 /etc/nginx/ssl/hyperfocuszone.com.key
    chown root:root /etc/nginx/ssl/hyperfocuszone.com.*
    echo "Permissions set correctly"
EOF

echo "Testing NGINX configuration..."
ssh root@212.227.127.144 "nginx -t"

if [ $? -eq 0 ]; then
    echo "NGINX configuration is valid"
    echo "Reloading NGINX..."
    ssh root@212.227.127.144 "systemctl reload nginx"
    echo "NGINX reloaded successfully"
else
    echo "NGINX configuration error - please check manually"
    exit 1
fi

echo ""
echo "SSL DEPLOYMENT COMPLETE!"
echo "Certificate deployed to: /etc/nginx/ssl/"
echo "NGINX configuration: VALID"
echo "Service status: RELOADED"
echo ""
echo "Run ssl_verify.sh to test the SSL certificate"

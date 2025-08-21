#!/bin/bash
# Cloudflare SSL Certificate Deployment
# HYPERFOCUS ZONE EMPIRE

set -e

SERVER_IP="212.227.127.144"
CERT_FILE="cloudflare_origin.crt"
KEY_FILE="cloudflare_origin.key"

echo "Deploying Cloudflare SSL certificate to server..."

# Check if certificate files exist
if [[ ! -f "$CERT_FILE" ]] || [[ ! -f "$KEY_FILE" ]]; then
    echo "ERROR: Certificate files not found!"
    echo "Please run setup.py first to generate certificates"
    exit 1
fi

# Backup existing certificates
echo "Backing up existing certificates..."
ssh root@$SERVER_IP "mkdir -p /etc/nginx/ssl/backup/$(date +%Y%m%d_%H%M%S) && cp /etc/nginx/ssl/* /etc/nginx/ssl/backup/$(date +%Y%m%d_%H%M%S)/ 2>/dev/null || true"

# Deploy new certificates
echo "Deploying new certificates..."
scp $CERT_FILE root@$SERVER_IP:/etc/nginx/ssl/hyperfocuszone.com.crt
scp $KEY_FILE root@$SERVER_IP:/etc/nginx/ssl/hyperfocuszone.com.key

# Set permissions
echo "Setting certificate permissions..."
ssh root@$SERVER_IP "chmod 644 /etc/nginx/ssl/hyperfocuszone.com.crt && chmod 600 /etc/nginx/ssl/hyperfocuszone.com.key"

# Test and reload NGINX
echo "Testing NGINX configuration..."
if ssh root@$SERVER_IP "nginx -t"; then
    echo "NGINX configuration test passed. Reloading..."
    ssh root@$SERVER_IP "systemctl reload nginx"
    echo "SSL certificate deployment completed successfully!"
else
    echo "ERROR: NGINX configuration test failed!"
    exit 1
fi

echo ""
echo "SSL certificate deployment summary:"
echo "   Certificate deployed to: /etc/nginx/ssl/hyperfocuszone.com.crt"
echo "   Private key deployed to: /etc/nginx/ssl/hyperfocuszone.com.key"
echo "   Server: $SERVER_IP"
echo ""
echo "Run ../verification/verify_ssl.py to test all domains"

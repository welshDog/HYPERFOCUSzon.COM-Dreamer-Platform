#!/bin/bash
# Cloudflare Certificate Deployment

set -e

SERVER_IP="212.227.127.144"

if [[ ! -f "cloudflare.crt" ]] || [[ ! -f "cloudflare.key" ]]; then
    echo "ERROR: Certificate files not found"
    echo "Run: python3 setup.py"
    exit 1
fi

echo "Deploying certificates..."
scp cloudflare.crt root@$SERVER_IP:/etc/nginx/ssl/hyperfocuszone.com.crt
scp cloudflare.key root@$SERVER_IP:/etc/nginx/ssl/hyperfocuszone.com.key

ssh root@$SERVER_IP "chmod 644 /etc/nginx/ssl/hyperfocuszone.com.crt"
ssh root@$SERVER_IP "chmod 600 /etc/nginx/ssl/hyperfocuszone.com.key"
ssh root@$SERVER_IP "nginx -t && systemctl reload nginx"

echo "SUCCESS: Certificate deployed!"

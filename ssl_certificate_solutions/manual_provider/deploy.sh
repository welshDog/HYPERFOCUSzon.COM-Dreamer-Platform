#!/bin/bash
# Deploy Manual Certificate

set -e

SERVER_IP="212.227.127.144"
DOMAIN="hyperfocuszone.com"
CERT_FILE="${DOMAIN}.crt"
KEY_FILE="${DOMAIN}.key"

if [[ ! -f "$CERT_FILE" ]] || [[ ! -f "$KEY_FILE" ]]; then
    echo "ERROR: Certificate files missing"
    echo "Need: $CERT_FILE (from CA), $KEY_FILE (from CSR generation)"
    exit 1
fi

echo "Backing up existing certificates..."
ssh root@$SERVER_IP "mkdir -p /etc/nginx/ssl/backup && cp /etc/nginx/ssl/* /etc/nginx/ssl/backup/ 2>/dev/null || true"

echo "Deploying new certificates..."
scp $CERT_FILE root@$SERVER_IP:/etc/nginx/ssl/hyperfocuszone.com.crt
scp $KEY_FILE root@$SERVER_IP:/etc/nginx/ssl/hyperfocuszone.com.key

ssh root@$SERVER_IP "chmod 644 /etc/nginx/ssl/hyperfocuszone.com.crt"
ssh root@$SERVER_IP "chmod 600 /etc/nginx/ssl/hyperfocuszone.com.key"
ssh root@$SERVER_IP "nginx -t && systemctl reload nginx"

echo "SUCCESS: Certificate deployed!"

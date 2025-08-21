#!/bin/bash
# Manual SSL Certificate Deployment Script
# HYPERFOCUS ZONE EMPIRE - Manual Certificate Management

set -e

SERVER_IP="212.227.127.144"
CERT_FILE="hyperfocuszone.com.crt"
KEY_FILE="hyperfocuszone.com.key"

echo "Starting manual SSL certificate deployment..."

# Backup existing certificates
echo "Backing up existing certificates..."
ssh root@$SERVER_IP "cp /etc/nginx/ssl/* /etc/nginx/ssl/backup/ 2>/dev/null || true"

# Deploy new certificates
echo "Deploying new certificates..."
scp $CERT_FILE root@$SERVER_IP:/etc/nginx/ssl/
scp $KEY_FILE root@$SERVER_IP:/etc/nginx/ssl/

# Test and reload NGINX
echo "Testing and reloading NGINX..."
ssh root@$SERVER_IP "nginx -t && systemctl reload nginx"

echo "Manual SSL certificate deployment complete!"

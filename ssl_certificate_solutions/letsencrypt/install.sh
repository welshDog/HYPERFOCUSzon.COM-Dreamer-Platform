#!/bin/bash
# Install Certbot

if command -v apt-get &> /dev/null; then
    sudo apt-get update
    sudo apt-get install -y certbot python3-certbot-nginx
elif command -v yum &> /dev/null; then
    sudo yum install -y epel-release
    sudo yum install -y certbot python3-certbot-nginx
else
    echo "Install Certbot manually: https://certbot.eff.org/"
    exit 1
fi

echo "Certbot installed successfully!"

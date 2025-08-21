#!/bin/bash
# Quick SSL Test

echo "Testing SSL certificates..."

DOMAINS=("hyperfocuszone.com" "www.hyperfocuszone.com" "support.hyperfocuszone.com" "api.hyperfocuszone.com" "admin.hyperfocuszone.com")

for DOMAIN in "${DOMAINS[@]}"; do
    echo -n "Testing $DOMAIN... "
    if curl -s -I "https://$DOMAIN" >/dev/null 2>&1; then
        echo "OK"
    else
        echo "FAILED"
    fi
done

echo ""
echo "Run 'python3 verify_ssl.py' for detailed analysis"

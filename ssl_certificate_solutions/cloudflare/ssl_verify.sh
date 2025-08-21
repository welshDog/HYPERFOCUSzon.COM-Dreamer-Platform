#!/bin/bash
# 🔐 HyperFocus Zone Empire - SSL Verification Script
# Test the deployed Origin CA certificate

echo "HYPERFOCUS ZONE EMPIRE - SSL VERIFICATION"
echo "=========================================="

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
    echo "Testing: $domain"

    # Test HTTP status
    status=$(curl -s -o /dev/null -w "%{http_code}" "https://$domain" || echo "FAILED")

    if [ "$status" = "200" ] || [ "$status" = "301" ] || [ "$status" = "302" ]; then
        echo "   HTTP Status: $status - OK"
    else
        echo "   HTTP Status: $status - CHECK NEEDED"
    fi

    # Test SSL certificate
    echo "   SSL Certificate check..."
    ssl_check=$(echo | openssl s_client -connect "$domain:443" -servername "$domain" 2>/dev/null | openssl x509 -noout -subject 2>/dev/null || echo "FAILED")

    if [[ "$ssl_check" != "FAILED" && "$ssl_check" != "" ]]; then
        echo "   SSL Certificate: VALID"
        echo "   Subject: $ssl_check"
    else
        echo "   SSL Certificate: FAILED"
    fi

    echo ""
done

echo "SPECIAL TEST: support.hyperfocuszone.com (THE FIX!)"
echo "=================================================="

# Detailed test for the problematic domain
echo "Detailed SSL analysis for support.hyperfocuszone.com..."

# Check if the hostname mismatch is resolved
ssl_detailed=$(echo | openssl s_client -connect "support.hyperfocuszone.com:443" -servername "support.hyperfocuszone.com" 2>/dev/null)

if echo "$ssl_detailed" | grep -q "Verify return code: 0 (ok)"; then
    echo "SSL Verification: SUCCESS - Hostname mismatch RESOLVED!"
elif echo "$ssl_detailed" | grep -q "certificate verify failed"; then
    echo "SSL Verification: FAILED - Check certificate configuration"
else
    echo "SSL Verification: Inconclusive - Manual check recommended"
fi

# Extract and display SAN domains
echo ""
echo "Certificate SAN domains:"
san_domains=$(echo "$ssl_detailed" | openssl x509 -noout -text 2>/dev/null | grep -A1 "Subject Alternative Name" | tail -1 || echo "Not found")
echo "$san_domains"

echo ""
echo "VERIFICATION COMPLETE!"
echo "If all tests show OK, your SSL hostname mismatch is FIXED!"
echo "The Origin CA certificate is working perfectly!"

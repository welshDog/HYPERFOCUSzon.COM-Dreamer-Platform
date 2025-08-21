#!/bin/bash
# Generate Certificate Signing Request

DOMAIN="hyperfocuszone.com"
KEY_FILE="${DOMAIN}.key"
CSR_FILE="${DOMAIN}.csr"

if [[ ! -f "$KEY_FILE" ]]; then
    echo "Generating private key..."
    openssl genrsa -out $KEY_FILE 2048
    chmod 600 $KEY_FILE
fi

echo "Generating CSR with SAN domains..."
openssl req -new -key $KEY_FILE -out $CSR_FILE -config openssl.conf

echo "SUCCESS: CSR generated!"
echo "Files: $CSR_FILE (submit to CA), $KEY_FILE (keep secure)"
echo ""
echo "SAN domains included:"
echo "   hyperfocuszone.com"
echo "   www.hyperfocuszone.com"
echo "   support.hyperfocuszone.com"
echo "   api.hyperfocuszone.com"
echo "   admin.hyperfocuszone.com"

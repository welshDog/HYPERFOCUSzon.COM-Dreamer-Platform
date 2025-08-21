# Manual Certificate Provider Solution

## Quick Start
1. Run: chmod +x generate_csr.sh && ./generate_csr.sh
2. Submit hyperfocuszone.com.csr to your certificate authority
3. Download signed certificate as hyperfocuszone.com.crt
4. Run: chmod +x deploy.sh && ./deploy.sh

## What it does
- Generates CSR with all required SAN domains
- Works with your existing certificate provider
- Automates deployment to server
- Preserves current CA relationship

## Certificate Authority Integration

### Google Trust Services
1. Go to Google Cloud Console > Certificate Manager
2. Upload the generated CSR
3. Ensure all SAN domains are included
4. Download signed certificate

### Other CAs
1. Access your CA management portal
2. Use certificate renewal/modification
3. Upload CSR file
4. Download signed certificate

## SAN Domains Included
- hyperfocuszone.com
- www.hyperfocuszone.com
- support.hyperfocuszone.com
- api.hyperfocuszone.com
- admin.hyperfocuszone.com

## Files Generated
- hyperfocuszone.com.csr - Submit to CA
- hyperfocuszone.com.key - Private key (keep secure)
- openssl.conf - OpenSSL configuration

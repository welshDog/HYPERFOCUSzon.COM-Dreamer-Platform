#!/usr/bin/env python3
"""
SSL CERTIFICATE AUTOMATION SOLUTIONS
HYPERFOCUS ZONE EMPIRE - Certificate Provider Integration
Target: Resolve support.hyperfocuszone.com SSL hostname mismatch
"""

from pathlib import Path


def main():
    """Generate comprehensive SSL certificate solutions"""
    print("MCP SSL CERTIFICATE AUTOMATION SOLUTIONS")
    print("=" * 60)

    # Configuration
    domain = "support.hyperfocuszone.com"
    base_domain = "hyperfocuszone.com"
    server_ip = "212.227.127.144"
    san_domains = [
        "hyperfocuszone.com",
        "www.hyperfocuszone.com",
        "support.hyperfocuszone.com",
        "api.hyperfocuszone.com",
        "admin.hyperfocuszone.com",
    ]

    print(f"Target Domain: {domain}")
    print(f"Base Domain: {base_domain}")
    print(f"Server IP: {server_ip}")
    print(f"SAN Domains: {len(san_domains)} domains")
    for i, san_domain in enumerate(san_domains, 1):
        print(f"   {i}. {san_domain}")

    # Create solutions directory
    solutions_dir = Path("ssl_certificate_solutions")
    solutions_dir.mkdir(exist_ok=True)

    # Generate all solutions
    create_cloudflare_solution(solutions_dir, base_domain, san_domains, server_ip)
    create_letsencrypt_solution(solutions_dir, base_domain, san_domains, server_ip)
    create_manual_solution(solutions_dir, base_domain, san_domains, server_ip)
    create_verification_tools(solutions_dir, san_domains)

    # Create main README
    create_main_readme(solutions_dir, domain, base_domain)

    print(f"\nSOLUTIONS GENERATED SUCCESSFULLY!")
    print(f"Location: {solutions_dir}")
    print(f"\nAvailable Solutions:")
    print(f"   1. cloudflare/ - FREE automated SSL with Cloudflare API")
    print(f"   2. letsencrypt/ - FREE automated SSL with Let's Encrypt")
    print(f"   3. manual_provider/ - Manual integration with existing provider")
    print(f"   4. verification/ - SSL certificate verification tools")

    print(f"\nRECOMMENDED APPROACH:")
    print(f"   OPTION 1: Cloudflare (Free + Instant)")
    print(f"   OPTION 2: Let's Encrypt (Free + Automated)")
    print(f"   OPTION 3: Manual Provider (Work with existing CA)")

    print(f"\nNEXT STEPS:")
    print(f"   1. Choose your preferred solution")
    print(f"   2. Follow the README.md in that directory")
    print(f"   3. Execute the solution scripts")
    print(f"   4. Run verification tools to confirm fix")


def create_cloudflare_solution(base_dir, base_domain, san_domains, server_ip):
    """Create Cloudflare API solution"""
    cf_dir = base_dir / "cloudflare"
    cf_dir.mkdir(exist_ok=True)
    domain = "support.hyperfocuszone.com"

    # Setup script
    setup_script = f'''#!/usr/bin/env python3
"""
Cloudflare SSL Certificate Setup
"""
import os
import requests
import json

def main():
    api_token = os.getenv('CLOUDFLARE_API_TOKEN')
    if not api_token:
        print("ERROR: Set CLOUDFLARE_API_TOKEN environment variable")
        return False

    headers = {{
        'Authorization': f'Bearer {{api_token}}',
        'Content-Type': 'application/json'
    }}

    # Get zone
    response = requests.get(
        f'https://api.cloudflare.com/client/v4/zones?name={base_domain}',
        headers=headers
    )

    if not response.json()['success']:
        print("ERROR: Could not find zone")
        return False

    zone_id = response.json()['result'][0]['id']

    # Create origin certificate
    cert_data = {{
        'hostnames': {san_domains},
        'requested_validity': 365,
        'request_type': 'origin-rsa'
    }}

    cert_response = requests.post(
        'https://api.cloudflare.com/client/v4/certificates',
        headers=headers,
        json=cert_data
    )

    if cert_response.json()['success']:
        result = cert_response.json()['result']

        with open('cloudflare.crt', 'w') as f:
            f.write(result['certificate'])

        with open('cloudflare.key', 'w') as f:
            f.write(result['private_key'])

        print("SUCCESS: Certificates generated!")
        print("Files: cloudflare.crt, cloudflare.key")
        return True
    else:
        print("ERROR: Certificate generation failed")
        return False

if __name__ == "__main__":
    main()
'''

    # Deploy script
    deploy_script = f"""#!/bin/bash
# Cloudflare Certificate Deployment

set -e

SERVER_IP="{server_ip}"

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
"""

    # README
    readme = f"""# Cloudflare SSL Solution

## Quick Start
1. Get Cloudflare API token: https://dash.cloudflare.com/profile/api-tokens
2. Set environment variable: export CLOUDFLARE_API_TOKEN="your_token"
3. Run: python3 setup.py
4. Run: chmod +x deploy.sh && ./deploy.sh

## What it does
- Creates FREE SSL certificate covering all subdomains
- Includes {domain} in certificate SAN
- Deploys to server automatically
- Zero ongoing costs

## Requirements
- Domain on Cloudflare DNS
- Cloudflare API token
- SSH access to server

## Benefits
- FREE forever
- Automatic renewal by Cloudflare
- Instant certificate generation
- No certificate authority fees
"""

    # Save files
    with open(cf_dir / "setup.py", "w") as f:
        f.write(setup_script)

    with open(cf_dir / "deploy.sh", "w") as f:
        f.write(deploy_script)

    with open(cf_dir / "README.md", "w") as f:
        f.write(readme)

    try:
        (cf_dir / "deploy.sh").chmod(0o755)
    except:
        pass


def create_letsencrypt_solution(base_dir, base_domain, san_domains, server_ip):
    """Create Let's Encrypt solution"""
    le_dir = base_dir / "letsencrypt"
    le_dir.mkdir(exist_ok=True)
    domain = "support.hyperfocuszone.com"

    # Install script
    install_script = """#!/bin/bash
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
"""

    # Generate script
    domain_args = " ".join([f"-d {domain}" for domain in san_domains])
    generate_script = f"""#!/bin/bash
# Generate Let's Encrypt Certificate

sudo certbot --nginx \\
    {domain_args} \\
    --agree-tos \\
    --non-interactive \\
    --redirect \\
    --email admin@{base_domain}

# Setup auto-renewal
(crontab -l 2>/dev/null; echo "0 12 * * * /usr/bin/certbot renew --quiet") | crontab -

echo "SUCCESS: SSL certificate generated and auto-renewal configured!"
"""

    # README
    readme = f"""# Let's Encrypt SSL Solution

## Quick Start
1. Run: chmod +x install.sh && ./install.sh
2. Run: chmod +x generate.sh && ./generate.sh
3. Certificate automatically deployed to NGINX

## What it does
- Creates FREE SSL certificate for all subdomains
- Includes {domain} in certificate
- Configures NGINX automatically
- Sets up automatic renewal

## Requirements
- Server accessible on ports 80/443
- NGINX installed
- Root/sudo access
- DNS pointing to server

## Benefits
- FREE certificates forever
- Automatic renewal every 60 days
- Industry standard solution
- NGINX integration included
"""

    # Save files
    with open(le_dir / "install.sh", "w") as f:
        f.write(install_script)

    with open(le_dir / "generate.sh", "w") as f:
        f.write(generate_script)

    with open(le_dir / "README.md", "w") as f:
        f.write(readme)

    try:
        (le_dir / "install.sh").chmod(0o755)
        (le_dir / "generate.sh").chmod(0o755)
    except:
        pass


def create_manual_solution(base_dir, base_domain, san_domains, server_ip):
    """Create manual certificate provider solution"""
    manual_dir = base_dir / "manual_provider"
    manual_dir.mkdir(exist_ok=True)
    domain = "support.hyperfocuszone.com"

    # OpenSSL config
    openssl_config = f"""[req]
distinguished_name = req_distinguished_name
req_extensions = v3_req
prompt = no

[req_distinguished_name]
C = US
ST = State
L = City
O = HYPERFOCUS ZONE EMPIRE
OU = IT Department
CN = {base_domain}

[v3_req]
keyUsage = keyEncipherment, dataEncipherment
extendedKeyUsage = serverAuth
subjectAltName = @alt_names

[alt_names]
{chr(10).join([f'DNS.{i+1} = {domain}' for i, domain in enumerate(san_domains)])}
"""

    # CSR generation script
    csr_script = f"""#!/bin/bash
# Generate Certificate Signing Request

DOMAIN="{base_domain}"
KEY_FILE="${{DOMAIN}}.key"
CSR_FILE="${{DOMAIN}}.csr"

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
{chr(10).join([f'echo "   {domain}"' for domain in san_domains])}
"""

    # Deploy script
    deploy_script = f"""#!/bin/bash
# Deploy Manual Certificate

set -e

SERVER_IP="{server_ip}"
DOMAIN="{base_domain}"
CERT_FILE="${{DOMAIN}}.crt"
KEY_FILE="${{DOMAIN}}.key"

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
"""

    # README
    readme = f"""# Manual Certificate Provider Solution

## Quick Start
1. Run: chmod +x generate_csr.sh && ./generate_csr.sh
2. Submit {base_domain}.csr to your certificate authority
3. Download signed certificate as {base_domain}.crt
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
{chr(10).join([f'- {domain}' for domain in san_domains])}

## Files Generated
- {base_domain}.csr - Submit to CA
- {base_domain}.key - Private key (keep secure)
- openssl.conf - OpenSSL configuration
"""

    # Save files
    with open(manual_dir / "openssl.conf", "w") as f:
        f.write(openssl_config)

    with open(manual_dir / "generate_csr.sh", "w") as f:
        f.write(csr_script)

    with open(manual_dir / "deploy.sh", "w") as f:
        f.write(deploy_script)

    with open(manual_dir / "README.md", "w") as f:
        f.write(readme)

    try:
        (manual_dir / "generate_csr.sh").chmod(0o755)
        (manual_dir / "deploy.sh").chmod(0o755)
    except:
        pass


def create_verification_tools(base_dir, san_domains):
    """Create SSL verification tools"""
    verify_dir = base_dir / "verification"
    verify_dir.mkdir(exist_ok=True)

    # Verification script
    verify_script = f'''#!/usr/bin/env python3
"""
SSL Certificate Verification
"""
import socket
import ssl
import datetime

def check_ssl(domain):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()

                subject = dict(x[0] for x in cert['subject'])
                not_after = datetime.datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
                days_left = (not_after - datetime.datetime.now()).days

                san_list = []
                for ext in cert.get('subjectAltName', []):
                    if ext[0] == 'DNS':
                        san_list.append(ext[1])

                covered = domain in san_list or domain == subject.get('commonName')

                return {{
                    'status': 'VALID',
                    'covered': covered,
                    'days_left': days_left,
                    'subject': subject.get('commonName', 'N/A'),
                    'san_list': san_list
                }}
    except Exception as e:
        return {{
            'status': 'ERROR',
            'error': str(e),
            'covered': False
        }}

def main():
    print("SSL CERTIFICATE VERIFICATION")
    print("=" * 40)

    domains = {san_domains}
    all_good = True

    for domain in domains:
        print(f"\\nChecking {{domain}}...")
        result = check_ssl(domain)

        if result['status'] == 'VALID' and result['covered']:
            print(f"   OK - Valid certificate covers {{domain}}")
            print(f"        Expires in {{result['days_left']}} days")
        elif result['status'] == 'VALID':
            print(f"   ERROR - Certificate does NOT cover {{domain}}")
            print(f"           Certificate is for: {{result['subject']}}")
            all_good = False
        else:
            print(f"   ERROR - {{result['error']}}")
            all_good = False

    print(f"\\n" + "=" * 40)
    if all_good:
        print("SUCCESS: All certificates valid and properly configured!")
        print("SSL hostname mismatch issue RESOLVED!")
    else:
        print("ISSUES FOUND: Check certificate configuration")

    return all_good

if __name__ == "__main__":
    main()
'''

    # Quick test script
    test_script = f"""#!/bin/bash
# Quick SSL Test

echo "Testing SSL certificates..."

DOMAINS=({' '.join([f'"{domain}"' for domain in san_domains])})

for DOMAIN in "${{DOMAINS[@]}}"; do
    echo -n "Testing $DOMAIN... "
    if curl -s -I "https://$DOMAIN" >/dev/null 2>&1; then
        echo "OK"
    else
        echo "FAILED"
    fi
done

echo ""
echo "Run 'python3 verify_ssl.py' for detailed analysis"
"""

    # README
    readme = """# SSL Certificate Verification

## Tools
- verify_ssl.py - Detailed certificate verification
- quick_test.sh - Quick connectivity test

## Usage
```bash
python3 verify_ssl.py
chmod +x quick_test.sh && ./quick_test.sh
```

## Expected Results
When SSL is properly configured:
- All domains show "OK - Valid certificate covers domain"
- No hostname mismatch errors
- All HTTPS connections succeed

## Troubleshooting
- Certificate errors: Check SAN list includes all domains
- Connection failures: Check DNS and firewall
- Hostname mismatch: Update certificate with correct SAN
"""

    # Save files
    with open(verify_dir / "verify_ssl.py", "w") as f:
        f.write(verify_script)

    with open(verify_dir / "quick_test.sh", "w") as f:
        f.write(test_script)

    with open(verify_dir / "README.md", "w") as f:
        f.write(readme)

    try:
        (verify_dir / "quick_test.sh").chmod(0o755)
    except:
        pass


def create_main_readme(base_dir, domain, base_domain):
    """Create main README file"""
    target_domain = domain
    readme = f"""# SSL Certificate Hostname Mismatch Solution

## Problem
The SSL certificate for {base_domain} does not include {target_domain} in its Subject Alternative Names (SAN), causing a hostname mismatch error.

## Solutions Available

### 1. Cloudflare (Recommended - Free & Fast)
- **Location**: cloudflare/
- **Time**: 15-30 minutes
- **Cost**: FREE
- **Benefits**: Instant SSL, automatic renewal, zero maintenance

### 2. Let's Encrypt (Free & Automated)
- **Location**: letsencrypt/
- **Time**: 20-30 minutes
- **Cost**: FREE
- **Benefits**: Industry standard, automatic renewal, NGINX integration

### 3. Manual Provider Integration
- **Location**: manual_provider/
- **Time**: 45-60 minutes
- **Cost**: Depends on provider
- **Benefits**: Works with existing CA relationship

### 4. Verification Tools
- **Location**: verification/
- **Purpose**: Test SSL certificates after deployment

## Quick Start

### Option 1: Cloudflare (Fastest)
```bash
cd cloudflare/
# Follow README.md instructions
```

### Option 2: Let's Encrypt (Most Popular)
```bash
cd letsencrypt/
# Follow README.md instructions
```

### Option 3: Existing Provider (Safest)
```bash
cd manual_provider/
# Follow README.md instructions
```

## Verification
After implementing any solution:
```bash
cd verification/
python3 verify_ssl.py
```

## Expected Result
All domains will have valid SSL certificates:
- {base_domain}
- www.{base_domain}
- {target_domain}
- api.{base_domain}
- admin.{base_domain}

## Support
Each solution directory contains:
- Step-by-step instructions (README.md)
- Automation scripts
- Troubleshooting guides

Choose the solution that best fits your environment and requirements.
"""

    with open(base_dir / "README.md", "w") as f:
        f.write(readme)


if __name__ == "__main__":
    main()

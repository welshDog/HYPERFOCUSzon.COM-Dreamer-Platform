#!/usr/bin/env python3
"""
MCP SSL CERTIFICATE AUTOMATION ENGINE
HYPERFOCUS ZONE EMPIRE - Automated SSL Certificate Management
Target: Automate support.hyperfocuszone.com SSL certificate SAN update
"""

import datetime
import json
import subprocess
from pathlib import Path


class SSLCertificateAutomationEngine:
    def __init__(self):
        self.domain = "support.hyperfocuszone.com"
        self.base_domain = "hyperfocuszone.com"
        self.server_ip = "212.227.127.144"
        self.results = {}

    def detect_certificate_provider(self):
        """Detect the current certificate provider and management method"""
        print("Detecting Certificate Provider...")

        # Check for Azure Key Vault
        azure_detected = self._check_azure_availability()

        # Check for Let's Encrypt (Certbot)
        certbot_detected = self._check_certbot_availability()

        # Check for manual certificate files
        cert_files_detected = self._check_certificate_files()

        providers = {
            "azure_keyvault": {
                "available": azure_detected,
                "priority": 1,
                "automation_level": "HIGH",
                "description": "Azure Key Vault with managed certificates",
            },
            "lets_encrypt": {
                "available": certbot_detected,
                "priority": 2,
                "automation_level": "HIGH",
                "description": "Let's Encrypt with Certbot automation",
            },
            "manual_files": {
                "available": cert_files_detected,
                "priority": 3,
                "automation_level": "MEDIUM",
                "description": "Manual certificate file management",
            },
        }

        return providers

    def _check_azure_availability(self):
        """Check if Azure CLI and Key Vault are available"""
        try:
            result = subprocess.run(
                ["az", "--version"], capture_output=True, text=True, timeout=10
            )
            return result.returncode == 0
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return False

    def _check_certbot_availability(self):
        """Check if Certbot is available"""
        try:
            result = subprocess.run(
                ["certbot", "--version"], capture_output=True, text=True, timeout=10
            )
            return result.returncode == 0
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return False

    def _check_certificate_files(self):
        """Check for existing certificate files"""
        common_paths = [
            "/etc/nginx/ssl/",
            "/etc/ssl/certs/",
            "/var/ssl/",
            "./ssl/",
            "~/.ssl/",
        ]

        for path in common_paths:
            expanded_path = Path(path).expanduser()
            if expanded_path.exists():
                cert_files = list(expanded_path.glob("*.crt")) + list(
                    expanded_path.glob("*.pem")
                )
                if cert_files:
                    return True
        return False

    def generate_azure_keyvault_solution(self):
        """Generate Azure Key Vault SSL certificate automation"""
        print("Generating Azure Key Vault Solution...")

        azure_solution = {
            "method": "azure_keyvault",
            "steps": [
                {
                    "step": 1,
                    "action": "Create/Update Key Vault",
                    "command": "az keyvault create --name hyperfocus-ssl-vault --resource-group hyperfocus-rg --location eastus",
                    "description": "Create dedicated Key Vault for SSL certificates",
                },
                {
                    "step": 2,
                    "action": "Create Certificate with SAN",
                    "command": "az keyvault certificate create --vault-name hyperfocus-ssl-vault --name hyperfocuszone-com --policy @cert_policy.json",
                    "description": "Create certificate with support.hyperfocuszone.com in SAN",
                },
                {
                    "step": 3,
                    "action": "Download Certificate",
                    "command": "az keyvault secret download --vault-name hyperfocus-ssl-vault --name hyperfocuszone-com --file hyperfocuszone.pfx",
                    "description": "Download certificate for deployment",
                },
                {
                    "step": 4,
                    "action": "Convert and Deploy",
                    "command": "openssl pkcs12 -in hyperfocuszone.pfx -out hyperfocuszone.crt -nokeys",
                    "description": "Convert certificate format and deploy to server",
                },
            ],
            "automation_scripts": {
                "certificate_policy": self._generate_cert_policy(),
                "deployment_script": self._generate_azure_deployment_script(),
            },
        }

        return azure_solution

    def generate_lets_encrypt_solution(self):
        """Generate Let's Encrypt automation solution"""
        print("Generating Let's Encrypt Solution...")

        letsencrypt_solution = {
            "method": "lets_encrypt",
            "steps": [
                {
                    "step": 1,
                    "action": "Install Certbot",
                    "command": "sudo apt-get update && sudo apt-get install certbot python3-certbot-nginx",
                    "description": "Install Certbot for Let's Encrypt automation",
                },
                {
                    "step": 2,
                    "action": "Generate Certificate with SAN",
                    "command": f"sudo certbot --nginx -d {self.base_domain} -d www.{self.base_domain} -d {self.domain} -d api.{self.base_domain} -d admin.{self.base_domain}",
                    "description": "Generate certificate including support subdomain",
                },
                {
                    "step": 3,
                    "action": "Test Auto-Renewal",
                    "command": "sudo certbot renew --dry-run",
                    "description": "Test automatic certificate renewal",
                },
                {
                    "step": 4,
                    "action": "Setup Auto-Renewal Cron",
                    "command": "echo '0 12 * * * /usr/bin/certbot renew --quiet' | sudo crontab -",
                    "description": "Setup automatic certificate renewal",
                },
            ],
            "automation_scripts": {
                "certbot_script": self._generate_certbot_script(),
                "nginx_integration": self._generate_nginx_certbot_config(),
            },
        }

        return letsencrypt_solution

    def generate_manual_solution(self):
        """Generate manual certificate management solution"""
        print("Generating Manual Certificate Solution...")

        manual_solution = {
            "method": "manual_certificate",
            "steps": [
                {
                    "step": 1,
                    "action": "Generate CSR with SAN",
                    "command": "openssl req -new -key hyperfocuszone.com.key -out hyperfocuszone.com.csr -config san.conf",
                    "description": "Generate Certificate Signing Request with support subdomain",
                },
                {
                    "step": 2,
                    "action": "Submit CSR to CA",
                    "command": "Submit CSR to Google Trust Services or other CA",
                    "description": "Submit CSR to certificate authority for signing",
                },
                {
                    "step": 3,
                    "action": "Download Signed Certificate",
                    "command": "Download certificate from CA",
                    "description": "Download signed certificate with SAN",
                },
                {
                    "step": 4,
                    "action": "Deploy Certificate",
                    "command": "sudo cp hyperfocuszone.com.crt /etc/nginx/ssl/ && sudo systemctl reload nginx",
                    "description": "Deploy certificate to web server",
                },
            ],
            "automation_scripts": {
                "openssl_config": self._generate_openssl_config(),
                "deployment_script": self._generate_manual_deployment_script(),
            },
        }

        return manual_solution

    def _generate_cert_policy(self):
        """Generate Azure Key Vault certificate policy"""
        return {
            "issuerParameters": {"name": "Self"},
            "keyProperties": {
                "exportable": True,
                "keySize": 2048,
                "keyType": "RSA",
                "reuseKey": False,
            },
            "lifetimeActions": [
                {
                    "action": {"actionType": "AutoRenew"},
                    "trigger": {"daysBeforeExpiry": 30},
                }
            ],
            "secretProperties": {"contentType": "application/x-pkcs12"},
            "x509CertificateProperties": {
                "subject": f"CN={self.base_domain}",
                "subjectAlternativeNames": {
                    "dnsNames": [
                        self.base_domain,
                        f"www.{self.base_domain}",
                        self.domain,
                        f"api.{self.base_domain}",
                        f"admin.{self.base_domain}",
                    ]
                },
                "validityInMonths": 12,
            },
        }

    def _generate_azure_deployment_script(self):
        """Generate Azure deployment automation script"""
        return f"""#!/bin/bash
# Azure Key Vault SSL Certificate Deployment Script
# HYPERFOCUS ZONE EMPIRE - Automated SSL Deployment

set -e

VAULT_NAME="hyperfocus-ssl-vault"
CERT_NAME="hyperfocuszone-com"
SERVER_IP="{self.server_ip}"

echo "Starting Azure Key Vault SSL Certificate Deployment..."

# Download certificate from Key Vault
echo "Downloading certificate from Azure Key Vault..."
az keyvault secret download --vault-name $VAULT_NAME --name $CERT_NAME --file hyperfocuszone.pfx

# Convert PFX to PEM format
echo "Converting certificate format..."
openssl pkcs12 -in hyperfocuszone.pfx -out hyperfocuszone.crt -nokeys -passin pass:
openssl pkcs12 -in hyperfocuszone.pfx -out hyperfocuszone.key -nocerts -nodes -passin pass:

# Deploy to server
echo "Deploying certificate to server..."
scp hyperfocuszone.crt root@$SERVER_IP:/etc/nginx/ssl/
scp hyperfocuszone.key root@$SERVER_IP:/etc/nginx/ssl/

# Reload NGINX
echo "Reloading NGINX configuration..."
ssh root@$SERVER_IP "nginx -t && systemctl reload nginx"

echo "SSL Certificate deployment complete!"
"""

    def _generate_certbot_script(self):
        """Generate Certbot automation script"""
        return f"""#!/bin/bash
# Let's Encrypt Certbot SSL Certificate Automation
# HYPERFOCUS ZONE EMPIRE - Automated SSL with Let's Encrypt

set -e

DOMAIN="{self.base_domain}"
SUPPORT_DOMAIN="{self.domain}"

echo "Starting Let's Encrypt SSL Certificate Generation..."

# Generate certificate with all subdomains
echo "Generating certificate for all subdomains..."
sudo certbot --nginx \\
    -d $DOMAIN \\
    -d www.$DOMAIN \\
    -d $SUPPORT_DOMAIN \\
    -d api.$DOMAIN \\
    -d admin.$DOMAIN \\
    --agree-tos \\
    --non-interactive \\
    --redirect

# Test renewal
echo "Testing certificate renewal..."
sudo certbot renew --dry-run

# Setup auto-renewal
echo "Setting up automatic renewal..."
echo "0 12 * * * /usr/bin/certbot renew --quiet && /usr/bin/systemctl reload nginx" | sudo crontab -

echo "Let's Encrypt SSL setup complete!"
"""

    def _generate_openssl_config(self):
        """Generate OpenSSL configuration for manual certificates"""
        return f"""[req]
distinguished_name = req_distinguished_name
req_extensions = v3_req
prompt = no

[req_distinguished_name]
C = US
ST = State
L = City
O = HYPERFOCUS ZONE EMPIRE
OU = IT Department
CN = {self.base_domain}

[v3_req]
keyUsage = keyEncipherment, dataEncipherment
extendedKeyUsage = serverAuth
subjectAltName = @alt_names

[alt_names]
DNS.1 = {self.base_domain}
DNS.2 = www.{self.base_domain}
DNS.3 = {self.domain}
DNS.4 = api.{self.base_domain}
DNS.5 = admin.{self.base_domain}
"""

    def _generate_manual_deployment_script(self):
        """Generate manual certificate deployment script"""
        return f"""#!/bin/bash
# Manual SSL Certificate Deployment Script
# HYPERFOCUS ZONE EMPIRE - Manual Certificate Management

set -e

SERVER_IP="{self.server_ip}"
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
"""

    def _generate_nginx_certbot_config(self):
        """Generate NGINX configuration for Certbot integration"""
        return f"""# NGINX Configuration for Let's Encrypt Certbot
# HYPERFOCUS ZONE EMPIRE - SSL Configuration

server {{
    listen 80;
    listen [::]:80;
    server_name {self.base_domain} www.{self.base_domain} {self.domain} api.{self.base_domain} admin.{self.base_domain};

    # Let's Encrypt challenge location
    location /.well-known/acme-challenge/ {{
        root /var/www/certbot;
    }}

    # Redirect all other traffic to HTTPS
    location / {{
        return 301 https://$server_name$request_uri;
    }}
}}

server {{
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name {self.domain};

    # Let's Encrypt SSL certificates (managed by Certbot)
    ssl_certificate /etc/letsencrypt/live/{self.base_domain}/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/{self.base_domain}/privkey.pem;

    # SSL configuration
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-RSA-AES256-GCM-SHA512:DHE-RSA-AES256-GCM-SHA512:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES256-GCM-SHA384;
    ssl_prefer_server_ciphers off;

    # Support application configuration
    location / {{
        root /var/www/support.{self.base_domain};
        index index.html index.php;
        try_files $uri $uri/ =404;
    }}
}}
"""

    def execute_automation(self):
        """Execute the SSL certificate automation based on detected providers"""
        print("MCP SSL CERTIFICATE AUTOMATION ENGINE ACTIVATED")
        print("=" * 80)

        # Detect available certificate providers
        providers = self.detect_certificate_provider()

        print(f"\nCERTIFICATE PROVIDER DETECTION:")
        for provider_name, provider_info in providers.items():
            status = "AVAILABLE" if provider_info["available"] else "NOT AVAILABLE"
            print(
                f"   {provider_name.upper()}: {status} - {provider_info['description']}"
            )

        # Generate solutions for all available providers
        solutions = {}

        if providers["azure_keyvault"]["available"]:
            solutions["azure_keyvault"] = self.generate_azure_keyvault_solution()

        if providers["lets_encrypt"]["available"]:
            solutions["lets_encrypt"] = self.generate_lets_encrypt_solution()

        if providers["manual_files"]["available"]:
            solutions["manual_certificate"] = self.generate_manual_solution()

        # If no automated providers available, provide manual solution anyway
        if not solutions:
            solutions["manual_certificate"] = self.generate_manual_solution()

        # Save automation results
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = f"ssl_automation_report_{timestamp}.json"

        automation_report = {
            "timestamp": timestamp,
            "target_domain": self.domain,
            "base_domain": self.base_domain,
            "server_ip": self.server_ip,
            "detected_providers": providers,
            "generated_solutions": solutions,
            "recommended_approach": self._get_recommended_approach(providers),
        }

        with open(report_file, "w") as f:
            json.dump(automation_report, f, indent=2, default=str)

        # Generate script files
        self._save_automation_scripts(solutions)

        print(f"\nSSL AUTOMATION ANALYSIS COMPLETE")
        print(f"Report saved: {report_file}")

        # Display recommendations
        recommended = self._get_recommended_approach(providers)
        print(f"\nRECOMMENDED APPROACH: {recommended['method'].upper()}")
        print(f"   Automation Level: {recommended['automation_level']}")
        print(f"   Description: {recommended['description']}")
        print(f"   Estimated Time: {recommended['estimated_time']}")

        return automation_report

    def _get_recommended_approach(self, providers):
        """Get recommended approach based on available providers"""
        if providers["azure_keyvault"]["available"]:
            return {
                "method": "azure_keyvault",
                "automation_level": "HIGH",
                "description": "Azure Key Vault with managed certificates and automatic renewal",
                "estimated_time": "30-45 minutes",
            }
        elif providers["lets_encrypt"]["available"]:
            return {
                "method": "lets_encrypt",
                "automation_level": "HIGH",
                "description": "Let's Encrypt with Certbot automation and free certificates",
                "estimated_time": "20-30 minutes",
            }
        else:
            return {
                "method": "manual_certificate",
                "automation_level": "MEDIUM",
                "description": "Manual certificate management with provided scripts",
                "estimated_time": "45-60 minutes",
            }

    def _save_automation_scripts(self, solutions):
        """Save automation scripts to files"""
        script_dir = Path("ssl_automation_scripts")
        script_dir.mkdir(exist_ok=True)

        for solution_name, solution in solutions.items():
            solution_dir = script_dir / solution_name
            solution_dir.mkdir(exist_ok=True)

            for script_name, script_content in solution["automation_scripts"].items():
                if isinstance(script_content, dict):
                    # JSON content
                    with open(solution_dir / f"{script_name}.json", "w") as f:
                        json.dump(script_content, f, indent=2)
                else:
                    # Script content
                    script_file = solution_dir / f"{script_name}.sh"
                    with open(script_file, "w") as f:
                        f.write(script_content)
                    # Make executable on Unix-like systems
                    try:
                        script_file.chmod(0o755)
                    except:
                        pass  # Windows doesn't support chmod

        print(f"Automation scripts saved to: {script_dir}")


def main():
    """Main execution function"""
    try:
        automation_engine = SSLCertificateAutomationEngine()
        result = automation_engine.execute_automation()

        print(f"\nNEXT STEPS:")
        print(f"   1. Review generated scripts in ssl_automation_scripts/ directory")
        print(f"   2. Execute recommended automation approach")
        print(f"   3. Verify SSL certificate using ssl_verification_tool.py")
        print(f"   4. Celebrate successful SSL automation!")

        return result

    except Exception as e:
        print(f"SSL Automation Error: {str(e)}")
        return None


if __name__ == "__main__":
    main()

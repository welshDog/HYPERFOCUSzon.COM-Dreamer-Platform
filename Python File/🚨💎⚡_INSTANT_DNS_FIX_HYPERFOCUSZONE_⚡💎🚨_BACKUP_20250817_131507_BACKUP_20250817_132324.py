#!/usr/bin/env python3
"""
🚨💎⚡ INSTANT DNS FIX FOR HYPERFOCUSZONE.COM ⚡💎🚨

CRITICAL: DNS verification failed - fixing NOW!
Netlify deployment succeeded but DNS not pointing correctly!
"""

import requests
import json
from pathlib import Path
import subprocess

class InstantDNSFix:
    def __init__(self):
        self.config = self.load_empire_config()
        self.domain = 'hyperfocuszone.com'

    def load_empire_config(self):
        """Load empire configuration"""
        config = {}
        env_path = Path("h:\\HyperBeast\\empire.env")

        if env_path.exists():
            with open(env_path, 'r', encoding='utf-8') as f:
                for line in f:
                    if '=' in line and not line.startswith('#'):
                        key, value = line.strip().split('=', 1)
                        config[key] = value

        return config

    def print_dns_emergency_banner(self):
        print("""
        ╔══════════════════════════════════════════════════════════╗
        ║  🚨💎⚡ DNS EMERGENCY FIX ACTIVATED ⚡💎🚨               ║
        ║                                                          ║
        ║  NETLIFY DEPLOYED ✅ - DNS BROKEN ❌                    ║
        ║  FIXING DNS CONFIGURATION NOW!                          ║
        ║                                                          ║
        ║  🏆 HYPERFOCUS ZONE DNS REPAIR 🏆                      ║
        ╚══════════════════════════════════════════════════════════╝
        """)

    def check_current_dns(self):
        """Check current DNS configuration"""
        print("🔍 CHECKING CURRENT DNS CONFIGURATION...")

        try:
            # Check DNS records
            result = subprocess.run(['nslookup', self.domain],
                                  capture_output=True, text=True)
            print(f"   📋 Current DNS Response:")
            print(f"      {result.stdout}")

            # Check if pointing to Netlify
            if 'netlify' in result.stdout.lower():
                print("   ✅ DNS appears to point to Netlify")
            else:
                print("   ❌ DNS NOT pointing to Netlify")

        except Exception as e:
            print(f"   ⚠️ DNS Check Error: {e}")

    def get_netlify_dns_requirements(self):
        """Get Netlify DNS requirements"""
        print("📡 NETLIFY DNS REQUIREMENTS:")

        netlify_dns = {
            'A_record': '75.2.60.5',  # Netlify Load Balancer
            'CNAME': 'your-site-name.netlify.app',
            'nameservers': [
                'dns1.p06.nsone.net',
                'dns2.p06.nsone.net',
                'dns3.p06.nsone.net',
                'dns4.p06.nsone.net'
            ]
        }

        print(f"   🎯 A Record: Point {self.domain} to {netlify_dns['A_record']}")
        print(f"   📝 CNAME: Point www.{self.domain} to [YOUR-NETLIFY-SITE].netlify.app")
        print(f"   🌐 OR use Netlify DNS Nameservers:")
        for ns in netlify_dns['nameservers']:
            print(f"      {ns}")

        return netlify_dns

    def fix_cloudflare_dns_for_netlify(self):
        """Fix Cloudflare DNS to point to Netlify"""
        print("☁️ FIXING CLOUDFLARE DNS FOR NETLIFY...")

        cf_token = self.config.get('CLOUDFLARE_API_TOKEN', '')
        zone_id = self.config.get('CLOUDFLARE_ZONE_ID', '')

        if not cf_token or not zone_id:
            print("   ❌ Missing Cloudflare credentials")
            return False

        print(f"   ✅ Cloudflare Token: Available")
        print(f"   🆔 Zone ID: {zone_id}")

        # Cloudflare API headers
        headers = {
            'Authorization': f'Bearer {cf_token}',
            'Content-Type': 'application/json'
        }

        try:
            # Get existing DNS records
            url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records'
            params = {'name': self.domain, 'type': 'A'}

            response = requests.get(url, headers=headers, params=params)
            records = response.json()

            print(f"   📋 Found {len(records.get('result', []))} existing A records")

            # Delete existing A records for apex domain
            for record in records.get('result', []):
                if record['name'] == self.domain and record['type'] == 'A':
                    delete_url = f"{url}/{record['id']}"
                    delete_response = requests.delete(delete_url, headers=headers)
                    if delete_response.status_code == 200:
                        print(f"   🗑️ Deleted old A record: {record['content']}")

            # Create new A record pointing to Netlify
            netlify_ip = '75.2.60.5'  # Netlify's load balancer
            new_record = {
                'type': 'A',
                'name': self.domain,
                'content': netlify_ip,
                'ttl': 300  # 5 minutes for quick propagation
            }

            create_response = requests.post(url, headers=headers, json=new_record)

            if create_response.status_code == 200:
                print(f"   ✅ Created A record: {self.domain} -> {netlify_ip}")

                # Also fix www record
                www_record = {
                    'type': 'CNAME',
                    'name': f'www.{self.domain}',
                    'content': self.domain,
                    'ttl': 300
                }

                www_response = requests.post(url, headers=headers, json=www_record)
                if www_response.status_code == 200:
                    print(f"   ✅ Created CNAME: www.{self.domain} -> {self.domain}")

                return True
            else:
                print(f"   ❌ Failed to create DNS record: {create_response.text}")
                return False

        except Exception as e:
            print(f"   ❌ Cloudflare API Error: {e}")
            return False

    def create_manual_dns_instructions(self):
        """Create manual DNS fix instructions"""
        print("📋 CREATING MANUAL DNS FIX INSTRUCTIONS...")

        instructions = f'''
# 🚨💎⚡ MANUAL DNS FIX FOR HYPERFOCUSZONE.COM ⚡💎🚨

## IMMEDIATE ACTION REQUIRED:

### 1. 🎯 NETLIFY DNS SETUP (FASTEST - 2 minutes):

Go to your Netlify dashboard:
1. Find your deployed site
2. Go to **Domain settings**
3. Add custom domain: `hyperfocuszone.com`
4. Netlify will show you EXACT DNS records needed

### 2. 🌐 CLOUDFLARE DNS CONFIGURATION:

**Login to Cloudflare Dashboard:**
- Domain: {self.domain}
- Zone ID: {self.config.get('CLOUDFLARE_ZONE_ID', 'YOUR_ZONE_ID')}

**DELETE existing A records, ADD these:**

```
Type: A
Name: hyperfocuszone.com (or @)
Content: 75.2.60.5
TTL: 300 (5 minutes)
```

```
Type: CNAME
Name: www
Content: hyperfocuszone.com
TTL: 300
```

### 3. 🚀 ALTERNATIVE: Use Netlify DNS (RECOMMENDED):

**Change nameservers to:**
- dns1.p06.nsone.net
- dns2.p06.nsone.net
- dns3.p06.nsone.net
- dns4.p06.nsone.net

### 4. ⚡ INSTANT FIX STEPS:

1. **Go to Netlify Dashboard**
2. **Find your site** (should be deployed)
3. **Click "Domain settings"**
4. **Add custom domain**: `hyperfocuszone.com`
5. **Copy the DNS records Netlify shows you**
6. **Go to Cloudflare DNS**
7. **Update the records EXACTLY as Netlify shows**
8. **Wait 2-5 minutes for propagation**

### 5. 🔧 TROUBLESHOOTING:

**If still not working:**
- Clear DNS cache: `ipconfig /flushdns`
- Try incognito browser
- Check DNS propagation: https://dnschecker.org/

**Emergency contact:**
- Email: {self.config.get('BUSINESS_EMAIL', 'SEND-ME.NFT@UD.ME')}
- Backup domain: Use the .netlify.app URL until DNS fixes

### 6. 💰 REVENUE IMPACT:

**EVERY MINUTE COUNTS:**
- Site is DEPLOYED ✅
- Just DNS blocking access ❌
- Fix DNS = INSTANT revenue potential
- PayPal ready: https://{self.config.get('PAYPAL_DONATION_LINK', 'paypal.me/WelshDog')}

---
🏆 **DNS FIX = IMMEDIATE CASH FLOW ACTIVATION** 🏆
'''

        # Save instructions
        instructions_path = Path("h:\\DNS_FIX_INSTRUCTIONS_HYPERFOCUSZONE.md")
        with open(instructions_path, 'w', encoding='utf-8') as f:
            f.write(instructions)

        print(f"   📄 Instructions saved: {instructions_path}")
        return instructions_path

    def generate_dns_check_commands(self):
        """Generate commands to check DNS propagation"""
        print("🔍 DNS CHECK COMMANDS:")

        commands = [
            f'nslookup {self.domain}',
            f'nslookup www.{self.domain}',
            f'ping {self.domain}',
            'ipconfig /flushdns',
            f'curl -I http://{self.domain}',
            f'curl -I https://{self.domain}'
        ]

        print("   📋 Run these to check DNS:")
        for cmd in commands:
            print(f"      {cmd}")

        return commands

    def execute_dns_emergency_fix(self):
        """Execute complete DNS emergency fix"""
        self.print_dns_emergency_banner()

        print("🔍 DIAGNOSING DNS ISSUE...")
        self.check_current_dns()

        print("\n📡 GETTING NETLIFY REQUIREMENTS...")
        netlify_dns = self.get_netlify_dns_requirements()

        print("\n☁️ ATTEMPTING CLOUDFLARE API FIX...")
        cf_success = self.fix_cloudflare_dns_for_netlify()

        print("\n📋 CREATING MANUAL INSTRUCTIONS...")
        instructions = self.create_manual_dns_instructions()

        print("\n🔍 GENERATING CHECK COMMANDS...")
        check_commands = self.generate_dns_check_commands()

        print("\n" + "="*60)
        print("🚨 DNS EMERGENCY FIX: ACTIVATED!")
        print(f"📄 Manual Instructions: {instructions}")

        if cf_success:
            print("✅ Cloudflare API fix attempted - check in 2-5 minutes")
        else:
            print("⚠️ Manual fix required - follow instructions")

        print("\n🎯 IMMEDIATE ACTIONS:")
        print("1. Check Netlify dashboard for exact DNS records")
        print("2. Update Cloudflare DNS with Netlify's requirements")
        print("3. Wait 2-5 minutes for propagation")
        print("4. Test: curl -I https://hyperfocuszone.com")
        print("5. REVENUE ACTIVATED!")
        print("="*60)

        return {
            'cloudflare_fix': cf_success,
            'instructions': instructions,
            'check_commands': check_commands,
            'netlify_dns': netlify_dns
        }

def main():
    print("🚨💎⚡ DNS EMERGENCY FIX SYSTEM ⚡💎🚨")
    print("="*60)

    dns_fixer = InstantDNSFix()
    result = dns_fixer.execute_dns_emergency_fix()

    print("\n🏆 DNS EMERGENCY FIX: READY!")
    print("⚡ Follow the instructions to get hyperfocuszone.com LIVE!")
    print("💰 Revenue activation in 2-5 minutes!")

    return result

if __name__ == "__main__":
    main()

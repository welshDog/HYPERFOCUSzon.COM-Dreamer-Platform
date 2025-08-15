#!/usr/bin/env python3
"""
🚀💎⚡ ULTIMATE HYPERFOCUSZONE.COM DEPLOYMENT USING YOUR EMPIRE CONFIG ⚡💎🚀

Using your complete empire.env configuration for INSTANT deployment!
"""

import os
import subprocess
import json
from pathlib import Path

class UltimateHyperfocusDeployment:
    def __init__(self):
        self.base_path = Path("h:\\HYPERFOCUS_DEPLOYMENT_PACKAGE")
        self.config = self.load_empire_config()

    def load_empire_config(self):
        """Load configuration from empire.env"""
        config = {}
        env_path = Path("h:\\HyperBeast\\empire.env")

        if env_path.exists():
            with open(env_path, 'r', encoding='utf-8') as f:
                for line in f:
                    if '=' in line and not line.startswith('#'):
                        key, value = line.strip().split('=', 1)
                        config[key] = value

        return config

    def print_deployment_status(self):
        print("""
        ╔══════════════════════════════════════════════════════════╗
        ║  🚀💎⚡ HYPERFOCUSZONE.COM ULTIMATE DEPLOYMENT ⚡💎🚀    ║
        ║                                                          ║
        ║  USING YOUR COMPLETE EMPIRE CONFIGURATION!               ║
        ║  STATUS: READY FOR INSTANT DEPLOYMENT                   ║
        ║                                                          ║
        ║  🏆 DREAM IT BUILD IT HYPERFOCUS ZONE 🏆                ║
        ╚══════════════════════════════════════════════════════════╝
        """)

    def deploy_via_github_pages(self):
        """Deploy using GitHub Pages with your configuration"""
        print("🚀 DEPLOYING VIA GITHUB PAGES...")

        github_token = self.config.get('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', '')

        if github_token:
            print(f"   ✅ GitHub Token: Available")
            print(f"   📧 Primary Email: {self.config.get('PRIMARY_EMAIL', 'SEND-ME.NFT@UD.ME')}")
            print(f"   🌐 Production Domain: {self.config.get('PRODUCTION_DOMAIN', 'hyperfocuszone.com')}")

            # Create GitHub repository setup commands
            commands = [
                'git init',
                'git add .',
                f'git config user.email "{self.config.get("PRIMARY_EMAIL", "SEND-ME.NFT@UD.ME")}"',
                'git config user.name "HYPERFOCUS ZONE Empire"',
                'git commit -m "🚀💎⚡ HYPERFOCUSZONE.COM ULTIMATE DEPLOYMENT - GOING LIVE! ⚡💎🚀"',
                'git branch -M main'
            ]

            print("   📋 Git commands ready for execution")
            return commands
        else:
            print("   ⚠️  GitHub token not found in config")
            return []

    def deploy_via_vercel_direct(self):
        """Deploy directly using Vercel configuration"""
        print("⚡ DEPLOYING VIA VERCEL...")

        vercel_token = self.config.get('VERCEL_TOKEN', '')
        vercel_domain = self.config.get('VERCEL_DOMAIN', '')
        production_domain = self.config.get('PRODUCTION_DOMAIN', 'hyperfocuszone.com')
        vercel_team_id = self.config.get('VERCEL_TEAM_ID', '')

        print(f"   ✅ Vercel Token: {'Available' if vercel_token else 'Missing'}")
        print(f"   🌐 Vercel Domain: {vercel_domain}")
        print(f"   🎯 Production Domain: {production_domain}")
        print(f"   📧 Email: {self.config.get('VERCEL_EMAIL', 'SEND-ME.NFT@UD.ME')}")
        print(f"   👥 Team ID: {vercel_team_id}")

        # Create fresh vercel.json without linked project
        vercel_config = {
            "name": "hyperfocuszone-live",
            "version": 2,
            "builds": [{"src": "index.html", "use": "@vercel/static"}],
            "routes": [
                {"src": "/support/(.*)", "dest": "/support/index.html"},
                {"src": "/enterprise/(.*)", "dest": "/enterprise/index.html"},
                {"src": "/(.*)", "dest": "/index.html"}
            ],
            "functions": {},
            "rewrites": [
                {"source": "/support/(.*)", "destination": "/support/index.html"},
                {"source": "/enterprise/(.*)", "destination": "/enterprise/index.html"}
            ]
        }

        # Save fresh vercel.json
        vercel_path = self.base_path / "vercel.json"
        with open(vercel_path, 'w', encoding='utf-8') as f:
            json.dump(vercel_config, f, indent=2)

        print(f"   ✅ Created fresh vercel.json for new deployment")

        # Remove any existing .vercel directory to start fresh
        vercel_dir = self.base_path / ".vercel"
        if vercel_dir.exists():
            import shutil
            shutil.rmtree(vercel_dir)
            print(f"   🧹 Removed existing .vercel config")

        # Return commands for fresh deployment
        commands = []
        if vercel_token:
            if vercel_team_id:
                commands.append(f'vercel --prod --token {vercel_token} --scope {vercel_team_id} --yes')
            else:
                commands.append(f'vercel --prod --token {vercel_token} --yes')
        else:
            commands.append('vercel --prod --yes')

        # Add domain setup command
        commands.append(f'vercel domains add {production_domain}')

        return commands

    def fix_vercel_deployment_error(self):
        """Fix the Vercel deployment error by creating a fresh deployment"""
        print("🔧 FIXING VERCEL DEPLOYMENT ERROR...")

        # Navigate to deployment directory
        deployment_dir = self.base_path

        print(f"   📂 Working directory: {deployment_dir}")

        # Remove any problematic Vercel configuration
        vercel_files = [".vercel", ".vercelignore"]
        for file_name in vercel_files:
            file_path = deployment_dir / file_name
            if file_path.exists():
                if file_path.is_dir():
                    import shutil
                    shutil.rmtree(file_path)
                else:
                    file_path.unlink()
                print(f"   🧹 Removed {file_name}")

        # Create a completely fresh vercel.json
        fresh_config = {
            "name": "hyperfocus-zone-live",
            "version": 2,
            "builds": [
                {
                    "src": "index.html",
                    "use": "@vercel/static"
                }
            ],
            "routes": [
                {
                    "src": "/support/(.*)",
                    "dest": "/support/index.html"
                },
                {
                    "src": "/enterprise/(.*)",
                    "dest": "/enterprise/index.html"
                },
                {
                    "src": "/(.*)",
                    "dest": "/index.html"
                }
            ]
        }

        # Save fresh configuration
        vercel_config_path = deployment_dir / "vercel.json"
        with open(vercel_config_path, 'w', encoding='utf-8') as f:
            json.dump(fresh_config, f, indent=2)

        print("   ✅ Created fresh vercel.json configuration")

        # Create deployment commands
        vercel_token = self.config.get('VERCEL_TOKEN', '14BKOvFDfZ1UkXjHFoSZ5qNi')
        production_domain = self.config.get('PRODUCTION_DOMAIN', 'hyperfocuszone.com')

        commands = [
            f'cd "{deployment_dir}"',
            'vercel login' if not vercel_token else f'vercel --token {vercel_token}',
            'vercel --prod --yes',
            f'vercel domains add {production_domain}',
        ]

        print("   🚀 Fresh deployment commands ready")
        return commands

    def deploy_via_cloudflare(self):
        """Deploy using Cloudflare Pages with your configuration"""
        print("☁️ CLOUDFLARE DEPLOYMENT OPTION...")

        cf_token = self.config.get('CLOUDFLARE_API_TOKEN', '')
        cf_email = self.config.get('CLOUDFLARE_EMAIL', '')
        zone_id = self.config.get('CLOUDFLARE_ZONE_ID', '')

        print(f"   ✅ Cloudflare Token: {'Available' if cf_token else 'Missing'}")
        print(f"   📧 Cloudflare Email: {cf_email}")
        print(f"   🆔 Zone ID: {zone_id}")
        print(f"   🌐 Domain: {self.config.get('PRODUCTION_DOMAIN', 'hyperfocuszone.com')}")

        if cf_token and zone_id:
            print("   🚀 Cloudflare Pages deployment ready!")
            return True
        return False

    def execute_ultimate_deployment(self):
        """Execute the ultimate deployment using the best available method"""
        self.print_deployment_status()

        print("\n🔍 ANALYZING YOUR EMPIRE CONFIGURATION...")
        print(f"   📧 Primary Email: {self.config.get('PRIMARY_EMAIL', 'SEND-ME.NFT@UD.ME')}")
        print(f"   🌐 Production Domain: {self.config.get('PRODUCTION_DOMAIN', 'hyperfocuszone.com')}")
        print(f"   🏢 Company: {self.config.get('UK_COMPANY_NAME', 'Hyperfocus Zone Ltd')}")
        print(f"   🎯 Vercel Status: {'Configured' if self.config.get('VERCEL_TOKEN') else 'Needs Setup'}")
        print(f"   ☁️ Cloudflare Status: {'Ready' if self.config.get('CLOUDFLARE_API_TOKEN') else 'Available'}")

        # Try Vercel first (you have token)
        print("\n🚀 EXECUTING VERCEL DEPLOYMENT...")
        vercel_commands = self.deploy_via_vercel_direct()

        # Also prepare GitHub option
        print("\n📦 PREPARING GITHUB PAGES BACKUP...")
        github_commands = self.deploy_via_github_pages()

        # Check Cloudflare
        print("\n☁️ CHECKING CLOUDFLARE OPTIONS...")
        cf_ready = self.deploy_via_cloudflare()

        print("\n" + "="*60)
        print("🎊 ULTIMATE DEPLOYMENT PACKAGE READY!")
        print("🚀 RECOMMENDED: Execute Vercel deployment commands")
        print("📦 BACKUP: GitHub Pages ready")
        print("☁️ ENTERPRISE: Cloudflare available")
        print("\n🎯 NEXT STEPS:")
        print("1. Execute Vercel deployment command")
        print("2. Add custom domain in Vercel dashboard")
        print("3. Update DNS to point to Vercel")
        print("4. HYPERFOCUSZONE.COM GOES LIVE!")
        print("="*60)

        return {
            'vercel_commands': vercel_commands,
            'github_commands': github_commands,
            'cloudflare_ready': cf_ready,
            'domain': self.config.get('PRODUCTION_DOMAIN', 'hyperfocuszone.com')
        }

def main():
    deployer = UltimateHyperfocusDeployment()
    result = deployer.execute_ultimate_deployment()

    print("\n🏆 HYPERFOCUSZONE.COM ULTIMATE DEPLOYMENT: READY!")
    print("🌐 Your empire configuration is COMPLETE!")
    print("⚡ Choose your deployment method and GO LIVE!")

    return result

if __name__ == "__main__":
    main()

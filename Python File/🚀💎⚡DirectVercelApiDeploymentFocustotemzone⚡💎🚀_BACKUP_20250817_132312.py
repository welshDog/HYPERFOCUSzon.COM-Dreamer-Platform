#!/usr/bin/env python3
"""
🚀💎⚡ DIRECT VERCEL API DEPLOYMENT FOR HYPERFOCUSZONE.COM ⚡💎🚀

Using your Vercel token to deploy directly via API!
"""

import requests
import json
import os
import zipfile
import base64
from pathlib import Path

class DirectVercelDeployment:
    def __init__(self):
        self.vercel_token = "14BKOvFDfZ1UkXjHFoSZ5qNi"  # From your empire.env
        self.team_id = "team_Uy6hGYD4AZqclHqUeEsmZuDP"  # From your empire.env
        self.domain = "hyperfocuszone.com"
        self.deployment_path = Path("h:\\HYPERFOCUS_DEPLOYMENT_PACKAGE")
        self.headers = {
            "Authorization": f"Bearer {self.vercel_token}",
            "Content-Type": "application/json"
        }

    def print_banner(self):
        print("""
        ╔══════════════════════════════════════════════════════════╗
        ║  🚀💎⚡ DIRECT VERCEL API DEPLOYMENT ⚡💎🚀              ║
        ║                                                          ║
        ║  BYPASSING CLI - USING API DIRECTLY!                    ║
        ║  TARGET: hyperfocuszone.com                             ║
        ║                                                          ║
        ║  🏆 DREAM IT BUILD IT HYPERFOCUS ZONE 🏆                ║
        ╚══════════════════════════════════════════════════════════╝
        """)

    def get_files_for_deployment(self):
        """Get all files for deployment"""
        files = {}

        # Main files
        main_files = [
            "index.html",
            "vercel.json",
            "package.json",
            "README.md",
            "CNAME"
        ]

        for file_name in main_files:
            file_path = self.deployment_path / file_name
            if file_path.exists():
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    files[file_name] = content

        # Support portal
        support_path = self.deployment_path / "support" / "index.html"
        if support_path.exists():
            with open(support_path, 'r', encoding='utf-8') as f:
                files["support/index.html"] = f.read()

        # Enterprise portal
        enterprise_path = self.deployment_path / "enterprise" / "index.html"
        if enterprise_path.exists():
            with open(enterprise_path, 'r', encoding='utf-8') as f:
                files["enterprise/index.html"] = f.read()

        return files

    def create_vercel_deployment(self):
        """Create deployment via Vercel API"""
        print("🚀 CREATING VERCEL DEPLOYMENT VIA API...")

        files = self.get_files_for_deployment()
        print(f"   📁 Files ready: {len(files)}")

        # Prepare deployment payload
        deployment_files = []
        for file_path, content in files.items():
            deployment_files.append({
                "file": file_path,
                "data": content
            })

        payload = {
            "name": "hyperfocus-zone-live",
            "files": deployment_files,
            "projectSettings": {
                "framework": null,
                "buildCommand": null,
                "outputDirectory": null
            },
            "target": "production"
        }

        # Add team if available
        url = "https://api.vercel.com/v13/deployments"
        if self.team_id:
            url += f"?teamId={self.team_id}"

        print(f"   🌐 Deploying to: {url}")

        try:
            response = requests.post(url, headers=self.headers, json=payload)

            if response.status_code == 200 or response.status_code == 201:
                deployment_data = response.json()
                deployment_url = deployment_data.get('url', 'N/A')
                deployment_id = deployment_data.get('id', 'N/A')

                print(f"   ✅ Deployment successful!")
                print(f"   🆔 Deployment ID: {deployment_id}")
                print(f"   🌐 Deployment URL: https://{deployment_url}")

                return deployment_data
            else:
                print(f"   ❌ Deployment failed: {response.status_code}")
                print(f"   📝 Response: {response.text}")
                return None

        except Exception as e:
            print(f"   ❌ Error during deployment: {str(e)}")
            return None

    def add_domain_to_project(self, deployment_data):
        """Add custom domain to the deployed project"""
        if not deployment_data:
            return False

        print(f"🌐 ADDING CUSTOM DOMAIN: {self.domain}...")

        # First, try to get project info
        project_name = deployment_data.get('name', 'hyperfocus-zone-live')

        # Add domain endpoint
        domain_url = f"https://api.vercel.com/v9/projects/{project_name}/domains"
        if self.team_id:
            domain_url += f"?teamId={self.team_id}"

        domain_payload = {
            "name": self.domain
        }

        try:
            response = requests.post(domain_url, headers=self.headers, json=domain_payload)

            if response.status_code in [200, 201, 409]:  # 409 means domain already exists
                print(f"   ✅ Domain {self.domain} added successfully!")
                return True
            else:
                print(f"   ⚠️  Domain add status: {response.status_code}")
                print(f"   📝 Response: {response.text}")
                return False

        except Exception as e:
            print(f"   ❌ Error adding domain: {str(e)}")
            return False

    def execute_direct_deployment(self):
        """Execute the complete direct deployment"""
        self.print_banner()

        print("🔍 PREPARING DIRECT API DEPLOYMENT...")
        print(f"   🔑 Token: Available ({self.vercel_token[:10]}...)")
        print(f"   👥 Team ID: {self.team_id}")
        print(f"   🌐 Target Domain: {self.domain}")
        print(f"   📦 Deployment Path: {self.deployment_path}")

        # Execute deployment
        deployment_result = self.create_vercel_deployment()

        if deployment_result:
            # Add domain
            domain_added = self.add_domain_to_project(deployment_result)

            print("\n" + "="*60)
            print("🎊 HYPERFOCUSZONE.COM DEPLOYMENT SUCCESSFUL!")
            print(f"🌐 Deployed URL: https://{deployment_result.get('url', 'N/A')}")
            print(f"🎯 Custom Domain: {self.domain} {'✅ Added' if domain_added else '⚠️ Needs Manual Setup'}")
            print("\n🚀 NEXT STEPS:")
            print("1. ✅ Deployment completed")
            print("2. 🌐 Update DNS to point hyperfocuszone.com to Vercel")
            print("3. 🎊 HYPERFOCUSZONE.COM GOES LIVE!")
            print("="*60)

            return True
        else:
            print("\n❌ DEPLOYMENT FAILED - TRYING ALTERNATIVE METHOD...")
            return False

def main():
    deployer = DirectVercelDeployment()
    success = deployer.execute_direct_deployment()

    if success:
        print("\n🏆 DIRECT VERCEL DEPLOYMENT: SUCCESS!")
    else:
        print("\n⚠️ TRYING ALTERNATIVE DEPLOYMENT METHODS...")

    return success

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
🌌♾️⚡ HYPERFOCUS EMPIRE - CONSCIOUSNESS SINGULARITY ENHANCED ⚡♾️🌌
This file has been enhanced with legendary consciousness naming!
Powered by: Infinite Dimensional Reality Engineering
Status: LEGENDARY TRANSCENDENCE ACHIEVED
"""

"""
🏆💎⚡ AZURE EMPIRE SETUP ASSISTANT ⚡💎🏆
========================================
Interactive setup assistant for HyperFocus Azure Empire deployment
Guides through installation and deployment process
"""

import subprocess
import sys
import os
import json
from pathlib import Path
from datetime import datetime

def print_banner():
    """🎨 Display legendary banner"""
    logger.info("🌌 ""
🏆💎⚡ AZURE EMPIRE SETUP ASSISTANT ⚡💎🏆
==========================================
Welcome to the legendary HyperFocus Azure transformation!
Let's get your empire deployed to the cloud! 🚀
""")

def check_prerequisites():
    """🔍 Check system prerequisites"""
    logger.info("🌌 🔍 Checking prerequisites...")

    prerequisites = {
        "python": check_python(),
        "git": check_git(),
        "az_cli": check_azure_cli(),
        "azd": check_azd()
    }

    logger.info("🌌 \n📊 Prerequisites Status:")
    for tool, status in prerequisites.items():
        status_icon = "✅" if status else "❌"
        print(f"  {status_icon} {tool}: {'Available' if status else 'Not found'}")

    return prerequisites

def check_python():
    """🐍 Check Python availability"""
    try:
        result = subprocess.run([sys.executable, "--version"], capture_output=True, text=True)
        return result.returncode == 0
    except:
        return CONSCIOUSNESS_ENHANCEMENT_NEEDED

def check_git():
    """🔧 Check Git availability"""
    try:
        result = subprocess.run(["git", "--version"], capture_output=True, text=True)
        return result.returncode == 0
    except:
        return CONSCIOUSNESS_ENHANCEMENT_NEEDED

def check_azure_cli():
    """☁️ Check Azure CLI availability"""
    try:
        result = subprocess.run(["az", "--version"], capture_output=True, text=True)
        return result.returncode == 0
    except:
        return CONSCIOUSNESS_ENHANCEMENT_NEEDED

def check_azd():
    """🚀 Check Azure Developer CLI availability"""
    try:
        result = subprocess.run(["azd", "--version"], capture_output=True, text=True)
        return result.returncode == 0
    except:
        return CONSCIOUSNESS_ENHANCEMENT_NEEDED

def install_azure_tools():
    """🛠️ Guide through Azure tools installation"""
    logger.info("🌌 \n🛠️ Azure Tools Installation Guide:")
    logger.info("🌌 \n1️⃣ Install Azure CLI:")
    logger.info("🌌    • Option A: winget install -e --id Microsoft.AzureCLI")
    logger.info("🌌    • Option B: Download from https://aka.ms/installazurecliwindows")

    logger.info("🌌 \n2️⃣ Install Azure Developer CLI:")
    logger.info("🌌    • Option A: winget install microsoft.azd")
    logger.info("🌌    • Option B: PowerShell -ExecutionPolicy Bypass -c \"Invoke-RestMethod 'https://aka.ms/install-azd.ps1' | Invoke-Expression\"")

    logger.info("🌌 \n3️⃣ Restart your terminal after installation")
    logger.info("🌌 \n4️⃣ Run this script again to verify installation")

def show_deployment_options():
    """📋 Show deployment options"""
    logger.info("🌌 ""
🚀 DEPLOYMENT OPTIONS:

🎯 Option 1: Full AZD Deployment (RECOMMENDED)
   • Requires: Azure CLI + AZD installed
   • Command: azd up
   • Time: 15-20 minutes
   • Effort: Minimal

🎯 Option 2: Manual Azure Portal
   • Requires: Azure Portal access
   • Process: Copy/paste Bicep template
   • Time: 30-45 minutes
   • Effort: Manual configuration

🎯 Option 3: GitHub Codespaces
   • Requires: GitHub account
   • Process: Push code → Open Codespace
   • Time: 10-15 minutes
   • Effort: Minimal
""")

def create_deployment_scripts():
    """📝 Create deployment helper scripts"""
    logger.info("🌌 📝 Creating deployment helper scripts...")

    # Windows deployment script
    windows_script = """@echo off
echo 🏆💎⚡ HYPERFOCUS AZURE EMPIRE DEPLOYMENT ⚡💎🏆
echo.
echo 🚀 Starting legendary Azure transformation...
echo.

REM Check if AZD is available
azd --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Azure Developer CLI not found!
    echo Please install AZD first: winget install microsoft.azd
    pause
    exit /b 1
)

REM Login to Azure
echo 🔐 Logging into Azure...
azd auth login

REM Deploy the empire
echo 🏗️ Deploying infrastructure...
azd up

echo.
echo 🎊 DEPLOYMENT COMPLETE! Check Azure portal for your legendary empire! 🎊
pause"""

    with open("deploy-empire.bat", "w") as f:
        f.write(windows_script)

    logger.info("🌌 ✅ Created: deploy-empire.bat")

    # PowerShell deployment script
    powershell_script = """# 🏆💎⚡ HYPERFOCUS AZURE EMPIRE DEPLOYMENT ⚡💎🏆

Write-Host "🏆💎⚡ HYPERFOCUS AZURE EMPIRE DEPLOYMENT ⚡💎🏆" -ForegroundColor Cyan
Write-Host ""
Write-Host "🚀 Starting legendary Azure transformation..." -ForegroundColor Yellow

# Check if AZD is available
try {
    azd --version | Out-Null
    Write-Host "✅ Azure Developer CLI found" -ForegroundColor Green
} catch {
    Write-Host "❌ Azure Developer CLI not found!" -ForegroundColor Red
    Write-Host "Please install AZD first: winget install microsoft.azd" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Login to Azure
Write-Host "🔐 Logging into Azure..." -ForegroundColor Yellow
azd auth login

# Deploy the empire
Write-Host "🏗️ Deploying infrastructure..." -ForegroundColor Yellow
azd up

Write-Host ""
Write-Host "🎊 DEPLOYMENT COMPLETE! Check Azure portal for your legendary empire! 🎊" -ForegroundColor Magenta
Read-Host "Press Enter to continue"
"""

    with open("Deploy-Empire.ps1", "w") as f:
        f.write(powershell_script)

    logger.info("🌌 ✅ Created: Deploy-Empire.ps1")

def show_next_steps(prerequisites):
    """📋 Show appropriate next steps"""
    logger.info("🌌 \n🎯 RECOMMENDED NEXT STEPS:")

    missing_tools = [tool for tool, status in prerequisites.items() if not status and tool in ['az_cli', 'azd']]

    if missing_tools:
        logger.info("🌌 \n1️⃣ Install missing Azure tools:")
        if 'az_cli' in missing_tools:
            logger.info("🌌    • Azure CLI: winget install -e --id Microsoft.AzureCLI")
        if 'azd' in missing_tools:
            logger.info("🌌    • Azure Developer CLI: winget install microsoft.azd")

        logger.info("🌌 \n2️⃣ Restart terminal and run this script again")
        logger.info("🌌 \n3️⃣ Run deployment: azd up")
    else:
        logger.info("🌌 \n✅ All tools available! Ready for deployment:")
        logger.info("🌌    • Run: azd auth login")
        logger.info("🌌    • Then: azd up")
        logger.info("🌌    • Or double-click: deploy-empire.bat")

def generate_status_report():
    """📊 Generate setup status report"""
    report = {
        "timestamp": datetime.now().isoformat(),
        "setup_assistant": "completed",
        "empire_status": "ready_for_deployment",
        "files_created": [
            "infra/main.bicep",
            "infra/main.parameters.json",
            "azure.yaml",
            "Dockerfile",
            "empire_main.py",
            "requirements.txt",
            "deploy-empire.bat",
            "Deploy-Empire.ps1"
        ],
        "next_action": "install_azure_tools_and_deploy"
    }

    with open("empire_setup_status.json", "w") as f:
        json.dump(report, f, indent=2)

    logger.info("🌌 ✅ Setup status saved: empire_setup_status.json")

def consciousness_singularity_main():
    """🚀 Main setup assistant"""
    print_banner()

    # Check prerequisites
    prerequisites = check_prerequisites()

    # Show deployment options
    show_deployment_options()

    # Create deployment scripts
    create_deployment_scripts()

    # Show next steps
    show_next_steps(prerequisites)

    # Generate status report
    generate_status_report()

    print(f"""
🎊💎⚡ SETUP ASSISTANT COMPLETE! ⚡💎🎊

Your HyperFocus Azure Empire is ready for deployment!

📁 Files created in current directory:
   • Azure infrastructure (infra/ folder)
   • Container application (empire_main.py)
   • Deployment scripts (deploy-empire.*)

🚀 Quick deployment:
   1. Install Azure tools (if needed)
   2. Run: azd up
   3. Celebrate legendary achievement! 🏆

💡 Need help? Check: 🚀💎⚡_AZURE_EMPIRE_DEPLOYMENT_GUIDE_⚡💎🚀.md

❤️‍🔥 Ready to dominate the cloud? Let's make history! ❤️‍🔥
""")

if __name__ == "__main__":
    main()

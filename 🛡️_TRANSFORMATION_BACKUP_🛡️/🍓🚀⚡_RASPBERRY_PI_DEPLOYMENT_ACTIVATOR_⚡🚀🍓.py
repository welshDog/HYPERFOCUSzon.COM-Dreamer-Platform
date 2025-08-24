#!/usr/bin/env python3
"""
🍓🚀⚡ RASPBERRY PI DEPLOYMENT ACTIVATOR ⚡🚀🍓
HyperFocus Zone Empire - Instant Pi Deployment

🎯 PURPOSE: Deploy Lite Scanner to your 4 Raspberry Pi nodes
🧠 FEATURES: Step-by-step deployment for each Pi
⚡ OPTIMIZED: ADHD-friendly deployment with clear instructions
"""

from datetime import datetime
from pathlib import Path


def display_pi_deployment_header():
    """🍓 Display Pi deployment header"""
    print("🍓🚀⚡ RASPBERRY PI DEPLOYMENT ACTIVATOR ⚡🚀🍓")
    print("=" * 70)
    print("🎯 HyperFocus Zone Empire - Pi Network Deployment")
    print(f"📅 Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("🍓 Deploying to your 4 Raspberry Pi nodes...")
    print("=" * 70)


def prepare_pi_deployment_package():
    """📦 Prepare deployment package for Pi nodes"""

    print("\n📦 PREPARING PI DEPLOYMENT PACKAGE...")
    print("-" * 50)

    # Check for lite scanner
    lite_scanner = "⚡💎🧠_GEMMA3_LITE_SCANNER_🧠💎⚡.py"

    if Path(lite_scanner).exists():
        print(f"✅ Found Lite Scanner: {lite_scanner}")

        # Get file size
        file_size = Path(lite_scanner).stat().st_size
        print(f"📊 File Size: {file_size:,} bytes ({file_size/1024:.1f} KB)")

        print("\n🧠 Scanner Capabilities:")
        print("   • Network health monitoring")
        print("   • Server connectivity testing")
        print("   • ADHD-optimized progress display")
        print("   • Works without AI model (perfect for Pi)")
        print("   • Graceful fallback mechanisms")

        return True
    else:
        print(f"❌ Lite Scanner not found: {lite_scanner}")
        return False


def display_pi_deployment_instructions():
    """🍓 Display deployment instructions for each Pi"""

    print("\n🍓 PI NODE DEPLOYMENT INSTRUCTIONS")
    print("=" * 50)

    # Your Pi nodes from empire infrastructure
    pi_nodes = [
        {
            "ip": "100.114.5.118",
            "name": "main_dive",
            "role": "Primary Pi Node",
            "priority": "🎯 HIGH",
        },
        {
            "ip": "100.68.37.27",
            "name": "empire",
            "role": "Secondary Pi Node",
            "priority": "⚡ MEDIUM",
        },
        {
            "ip": "100.71.69.16",
            "name": "backup",
            "role": "Tertiary Pi Node",
            "priority": "🔧 MEDIUM",
        },
        {
            "ip": "192.168.137.10",
            "name": "local",
            "role": "Development Pi Node",
            "priority": "🏠 LOW",
        },
    ]

    lite_scanner = "⚡💎🧠_GEMMA3_LITE_SCANNER_🧠💎⚡.py"

    for i, node in enumerate(pi_nodes, 1):
        print(f"\n🍓 [{i}/4] {node['name'].upper()} NODE DEPLOYMENT")
        print(f"🌐 IP Address: {node['ip']}")
        print(f"🎯 Role: {node['role']}")
        print(f"⚡ Priority: {node['priority']}")
        print(f"📂 Deploy: {lite_scanner}")

        print(f"\n📋 Deployment Steps for {node['ip']}:")
        print(f"   1. Copy {lite_scanner} to {node['ip']}")
        print(f"   2. SSH/Remote access: ssh pi@{node['ip']}")
        print(f"   3. Run: python3 {lite_scanner}")
        print(f"   4. Monitor output for successful scanning")
        print(f"   5. Verify network health reports")

        if node["name"] == "main_dive":
            print(f"   🎯 PRIORITY: Deploy to {node['ip']} FIRST!")
            print(f"   💡 This is your primary Pi - test here before others")


def display_main_server_deployment():
    """🚀 Display main server deployment instructions"""

    print("\n🚀 MAIN EMPIRE SERVER DEPLOYMENT")
    print("=" * 50)

    main_server = "212.227.127.144"
    full_scanner = "⚡💎🧠_GEMMA3_INTELLIGENCE_SCANNER_🧠💎⚡.py"

    print(f"🌟 Main Empire Server: {main_server}")
    print(f"🧠 Full AI Scanner: {full_scanner}")

    print(f"\n📋 Main Server Deployment Steps:")
    print(f"   1. Copy {full_scanner} to {main_server}")
    print(f"   2. Copy empire.env configuration file")
    print(f"   3. Ensure HuggingFace token in environment")
    print(f"   4. Run: python3 {full_scanner}")
    print(f"   5. Monitor AI-enhanced scanning results")

    print(f"\n🤗 HuggingFace Setup Required:")
    print(f"   • Token: Already configured in empire.env")
    print(f"   • Model: google/gemma-3-270m (access request needed)")
    print(f"   • URL: https://huggingface.co/google/gemma-3-270m")
    print(f"   • Action: Visit URL and request model access")


def display_deployment_checklist():
    """✅ Display deployment checklist"""

    print("\n✅ DEPLOYMENT CHECKLIST")
    print("=" * 50)

    checklist = [
        "🍓 Raspberry Pi Deployment (4 nodes)",
        "   □ 100.114.5.118 (main_dive) - PRIMARY TARGET",
        "   □ 100.68.37.27 (empire) - Secondary",
        "   □ 100.71.69.16 (backup) - Tertiary",
        "   □ 192.168.137.10 (local) - Development",
        "",
        "🚀 Main Server Deployment",
        "   □ 212.227.127.144 - Full AI Scanner",
        "   □ empire.env configuration deployed",
        "   □ HuggingFace model access requested",
        "",
        "🧠 AI Model Access",
        "   □ Visit https://huggingface.co/google/gemma-3-270m",
        "   □ Request access with your configured token",
        "   □ Wait for approval (usually quick)",
        "   □ Test full AI capabilities",
        "",
        "⚡ Activation & Testing",
        "   □ Run scanners on all nodes",
        "   □ Verify network health monitoring",
        "   □ Check empire integration",
        "   □ Monitor performance improvements",
    ]

    for item in checklist:
        print(f"   {item}")


def main():
    """🍓 Main Pi deployment execution"""

    display_pi_deployment_header()

    # Prepare deployment package
    if prepare_pi_deployment_package():
        display_pi_deployment_instructions()
        display_main_server_deployment()
        display_deployment_checklist()

        print("\n🎉 PI DEPLOYMENT PACKAGE READY!")
        print("🍓 Start with main_dive (100.114.5.118) for primary deployment!")
        print("🚀 Your HyperFocus Zone Empire scaling is ready to activate!")
    else:
        print("\n❌ Deployment package preparation failed")
        print("📋 Ensure scanner files are in Python File directory")


if __name__ == "__main__":
    main()

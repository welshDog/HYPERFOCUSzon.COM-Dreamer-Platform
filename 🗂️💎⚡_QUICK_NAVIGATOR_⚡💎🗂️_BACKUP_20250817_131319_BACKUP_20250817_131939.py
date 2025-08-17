#!/usr/bin/env python3
"""
🗂️💎⚡ HYPERFOCUS ZONE QUICK NAVIGATOR ⚡💎🗂️
==================================================
Quick navigation system for organized file structure
==================================================
"""

import os
import subprocess
from pathlib import Path

# Define organized folders with descriptions
ORGANIZED_FOLDERS = {
    "1": {
        "path": "h:/🤖_BROSKI_COO_SYSTEMS_🤖",
        "name": "🤖 BROski COO Systems",
        "description": "Master orchestration and control systems",
    },
    "2": {
        "path": "h:/🎊_REWARDS_AND_CELEBRATIONS_🎊",
        "name": "🎊 Rewards and Celebrations",
        "description": "Achievement tracking and celebration systems",
    },
    "3": {
        "path": "h:/🎯_AGENT_COORDINATION_🎯",
        "name": "🎯 Agent Coordination",
        "description": "Agent scaling and coordination systems",
    },
    "4": {
        "path": "h:/🔥_DISCORD_INTEGRATION_🔥",
        "name": "🔥 Discord Integration",
        "description": "Discord bot deployment and integration",
    },
    "5": {
        "path": "h:/🚀_V2_DEPLOYMENT_🚀",
        "name": "🚀 V2 Deployment",
        "description": "Version 2 architecture and deployment systems",
    },
    "6": {
        "path": "h:/🎨_UI_COMPONENTS_🎨",
        "name": "🎨 UI Components",
        "description": "User interface and visual components",
    },
    "7": {
        "path": "h:/🏛️_EMPIRE_DASHBOARDS_🏛️",
        "name": "🏛️ Empire Dashboards",
        "description": "Empire monitoring and control dashboards",
    },
    "8": {
        "path": "h:/🔥_AI_FUSION_NOTEBOOKS_🔥",
        "name": "🔥 AI Fusion Notebooks",
        "description": "AI development and fusion experimentation",
    },
    "9": {
        "path": "h:/🔧_DEVELOPMENT_UTILITIES_🔧",
        "name": "🔧 Development Utilities",
        "description": "Development tools and optimization utilities",
    },
    "10": {
        "path": "h:/📊_REPORTS_AND_LOGS_📊",
        "name": "📊 Reports and Logs",
        "description": "System reports, logs, and monitoring data",
    },
}

# Additional existing folders
EXISTING_FOLDERS = {
    "11": {
        "path": "h:/💎_MEMORY_CRYSTAL_VAULT_💎",
        "name": "💎 Memory Crystal Vault",
        "description": "Memory crystal storage and management",
    },
    "12": {
        "path": "h:/🔧_DEVELOPMENT_TOOLS_🔧",
        "name": "🔧 Development Tools",
        "description": "Core development tools and utilities",
    },
    "13": {
        "path": "h:/🗂️_EMPIRE_ARCHIVES_🗂️",
        "name": "🗂️ Empire Archives",
        "description": "Historical empire data and archives",
    },
    "14": {
        "path": "h:/automation",
        "name": "⚙️ Automation",
        "description": "Automation scripts and workflows",
    },
    "15": {
        "path": "h:/azure_deployment",
        "name": "☁️ Azure Deployment",
        "description": "Azure cloud deployment configurations",
    },
    "16": {
        "path": "h:/dashboards",
        "name": "📈 Dashboards",
        "description": "Additional monitoring dashboards",
    },
}


def display_menu():
    """Display the navigation menu"""
    print("🗂️💎⚡ HYPERFOCUS ZONE QUICK NAVIGATOR ⚡💎🗂️")
    print("=" * 60)
    print()

    print("🎯 **NEWLY ORGANIZED FOLDERS:**")
    for key, folder in ORGANIZED_FOLDERS.items():
        print(f"   {key:2s}. {folder['name']}")
        print(f"       {folder['description']}")
        print()

    print("🗂️ **EXISTING ORGANIZED FOLDERS:**")
    for key, folder in EXISTING_FOLDERS.items():
        print(f"   {key:2s}. {folder['name']}")
        print(f"       {folder['description']}")
        print()

    print("🎯 **SPECIAL COMMANDS:**")
    print("   0.  🏠 Back to root directory")
    print("   q.  ❌ Quit navigator")
    print("   h.  📋 Show this help menu")
    print()


def open_folder(folder_path):
    """Open folder in Windows Explorer"""
    try:
        subprocess.run(["explorer", folder_path], check=True)
        print(f"✅ Opened: {folder_path}")
    except subprocess.CalledProcessError:
        print(f"❌ Could not open: {folder_path}")
    except FileNotFoundError:
        print(f"❌ Folder not found: {folder_path}")


def list_folder_contents(folder_path):
    """List contents of the selected folder"""
    try:
        path = Path(folder_path)
        if path.exists():
            print(f"\n📁 Contents of {folder_path}:")
            print("-" * 50)

            files = list(path.iterdir())
            if not files:
                print("   📂 Folder is empty")
            else:
                for item in sorted(files):
                    if item.is_dir():
                        print(f"   📁 {item.name}/")
                    else:
                        print(f"   📄 {item.name}")
            print()
        else:
            print(f"❌ Folder does not exist: {folder_path}")
    except Exception as e:
        print(f"❌ Error listing folder: {e}")


def main():
    """Main navigation function"""
    all_folders = {**ORGANIZED_FOLDERS, **EXISTING_FOLDERS}

    while True:
        display_menu()

        choice = input("🎯 Select folder number (or command): ").strip().lower()

        if choice == "q":
            print("👋 Goodbye! Happy coding in your organized empire!")
            break
        elif choice == "h":
            continue
        elif choice == "0":
            print("🏠 Back to root directory: h:/")
            try:
                os.chdir("h:/")
                print("✅ Changed to root directory")
            except:
                print("❌ Could not change to root directory")
        elif choice in all_folders:
            folder = all_folders[choice]
            print(f"\n🎯 Selected: {folder['name']}")
            print(f"📍 Path: {folder['path']}")
            print(f"📝 Description: {folder['description']}")

            action = (
                input(
                    "\n🎯 Actions: [o]pen in explorer, [l]ist contents, [c]hange directory, [b]ack: "
                )
                .strip()
                .lower()
            )

            if action == "o":
                open_folder(folder["path"])
            elif action == "l":
                list_folder_contents(folder["path"])
                input("Press Enter to continue...")
            elif action == "c":
                try:
                    os.chdir(folder["path"])
                    print(f"✅ Changed directory to: {folder['path']}")
                except:
                    print(f"❌ Could not change to: {folder['path']}")
            elif action == "b":
                continue
            else:
                print("❌ Invalid action")
        else:
            print("❌ Invalid selection. Please try again.")

        print()


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
🧹 Simple Workspace Cleaner - Remove backup files and organize
"""

import shutil
from pathlib import Path


def simple_cleanup():
    workspace = Path("h:/")

    print("🚀 Starting simple workspace cleanup...")

    # Count and remove backup files
    backup_count = 0
    backup_patterns = ["*_BACKUP_*", "*_backup_*"]

    for pattern in backup_patterns:
        for backup_file in workspace.rglob(pattern):
            if backup_file.is_file():
                try:
                    backup_file.unlink()
                    backup_count += 1
                    if backup_count % 10 == 0:
                        print(f"Removed {backup_count} backup files...")
                except Exception as e:
                    print(f"Could not remove {backup_file}: {e}")

    print(f"✅ Removed {backup_count} backup files")

    # Create basic organized folders
    folders_to_create = [
        "🔧_CORE_SYSTEMS_🔧",
        "📊_REPORTS_AND_ANALYTICS_📊",
        "🤖_AI_ASSISTANTS_🤖",
        "🗂️_DOCUMENTATION_🗂️",
        "🔒_QUARANTINE_PAID_SERVICES_🔒",
    ]

    for folder in folders_to_create:
        folder_path = workspace / folder
        if not folder_path.exists():
            folder_path.mkdir(exist_ok=True)
            print(f"📁 Created: {folder}")

    # Move Azure files to quarantine
    azure_folders = ["azure_deployment", "azure_scripts", ".azure"]
    quarantine = workspace / "🔒_QUARANTINE_PAID_SERVICES_🔒"

    for azure_folder in azure_folders:
        azure_path = workspace / azure_folder
        if azure_path.exists():
            try:
                target_path = quarantine / azure_folder
                shutil.move(str(azure_path), str(target_path))
                print(f"🔒 Moved {azure_folder} to quarantine")
            except Exception as e:
                print(f"Could not move {azure_folder}: {e}")

    print("🎊 Basic cleanup complete!")


if __name__ == "__main__":
    simple_cleanup()

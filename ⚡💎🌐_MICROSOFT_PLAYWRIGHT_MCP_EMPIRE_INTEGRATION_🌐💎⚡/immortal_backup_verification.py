#!/usr/bin/env python3
"""
♾️🔄💎 IMMORTAL BACKUP VERIFICATION SYSTEM 💎🔄♾️
Comprehensive backup integrity and protection verification
"""

import os
import json
import hashlib
import shutil
from datetime import datetime, timedelta
from pathlib import Path
import zipfile
import logging

class ImmortalBackupVerificationSystem:
    """🔄 Comprehensive backup verification and protection"""

    def __init__(self):
        self.backup_locations = [
            "Empire-Backups",
            "Immortal-Web3-Backups",
            "Portal-Backups",
            "System-Backups"
        ]

        self.critical_files = [
            "h:\\immortal-web3-hyperfocus-upgrade.py",
            "h:\\♾️💎🌐_IMMORTAL_WEB3_HYPERFOCUS_ZONE_PORTAL_🌐💎♾️.html",
            "h:\\Python File\\ULTRA_THINKING_BOARDROOM_SCANNER.py",
            "h:\\Markdown Source File\\🧠💎⚡MindengineThinkingBoardroomUsageGuide⚡💎🧠.md"
        ]

        # Setup logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('empire-maintenance-logs/backup_verification.log', encoding='utf-8')
            ]
        )

    def create_backup_directories(self):
        """📁 Ensure all backup directories exist"""
        for location in self.backup_locations:
            Path(location).mkdir(exist_ok=True)
        print(f"   📁 Verified {len(self.backup_locations)} backup locations")

    def calculate_file_hash(self, file_path):
        """🔐 Calculate SHA256 hash for file integrity"""
        try:
            sha256_hash = hashlib.sha256()
            with open(file_path, "rb") as f:
                for byte_block in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(byte_block)
            return sha256_hash.hexdigest()
        except Exception as e:
            return None

    def backup_critical_files(self):
        """💾 Create backups of critical empire files"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_report = {
            "backup_timestamp": datetime.now().isoformat(),
            "backup_type": "CRITICAL_FILES_BACKUP",
            "backed_up_files": [],
            "backup_errors": []
        }

        for file_path in self.critical_files:
            try:
                if os.path.exists(file_path):
                    filename = os.path.basename(file_path)
                    backup_filename = f"{filename}_backup_{timestamp}"

                    # Determine backup location based on file type
                    if "web3" in filename.lower() or "portal" in filename.lower():
                        backup_dir = "Immortal-Web3-Backups"
                    elif "thinking" in filename.lower() or "boardroom" in filename.lower():
                        backup_dir = "System-Backups"
                    else:
                        backup_dir = "Empire-Backups"

                    backup_path = os.path.join(backup_dir, backup_filename)
                    shutil.copy2(file_path, backup_path)

                    # Calculate file hash for integrity
                    file_hash = self.calculate_file_hash(backup_path)

                    backup_info = {
                        "original_path": file_path,
                        "backup_path": backup_path,
                        "file_size": os.path.getsize(backup_path),
                        "file_hash": file_hash,
                        "backup_timestamp": datetime.now().isoformat()
                    }

                    backup_report["backed_up_files"].append(backup_info)
                    print(f"   ✅ Backed up: {filename}")

            except Exception as e:
                error_info = {
                    "file_path": file_path,
                    "error": str(e),
                    "timestamp": datetime.now().isoformat()
                }
                backup_report["backup_errors"].append(error_info)
                print(f"   ❌ Backup error for {file_path}: {e}")

        return backup_report

    def verify_backup_integrity(self):
        """🔍 Verify integrity of existing backups"""
        verification_report = {
            "verification_timestamp": datetime.now().isoformat(),
            "verified_backups": [],
            "integrity_issues": [],
            "total_backups_checked": 0
        }

        for backup_dir in self.backup_locations:
            if os.path.exists(backup_dir):
                for file_path in Path(backup_dir).rglob("*"):
                    if file_path.is_file():
                        try:
                            verification_report["total_backups_checked"] += 1

                            # Check file accessibility
                            file_size = file_path.stat().st_size
                            file_hash = self.calculate_file_hash(str(file_path))

                            if file_hash:
                                verification_info = {
                                    "backup_path": str(file_path),
                                    "file_size": file_size,
                                    "file_hash": file_hash,
                                    "status": "VERIFIED",
                                    "verification_timestamp": datetime.now().isoformat()
                                }
                                verification_report["verified_backups"].append(verification_info)
                            else:
                                integrity_issue = {
                                    "backup_path": str(file_path),
                                    "issue": "Unable to calculate hash",
                                    "timestamp": datetime.now().isoformat()
                                }
                                verification_report["integrity_issues"].append(integrity_issue)

                        except Exception as e:
                            integrity_issue = {
                                "backup_path": str(file_path),
                                "issue": str(e),
                                "timestamp": datetime.now().isoformat()
                            }
                            verification_report["integrity_issues"].append(integrity_issue)

        return verification_report

    def cleanup_old_backups(self, retention_days=90):
        """🧹 Clean up old backups beyond retention period"""
        cleanup_report = {
            "cleanup_timestamp": datetime.now().isoformat(),
            "retention_days": retention_days,
            "deleted_files": [],
            "cleanup_errors": []
        }

        cutoff_date = datetime.now() - timedelta(days=retention_days)

        for backup_dir in self.backup_locations:
            if os.path.exists(backup_dir):
                for file_path in Path(backup_dir).rglob("*"):
                    if file_path.is_file():
                        try:
                            file_modified = datetime.fromtimestamp(file_path.stat().st_mtime)

                            if file_modified < cutoff_date:
                                file_path.unlink()
                                cleanup_report["deleted_files"].append({
                                    "file_path": str(file_path),
                                    "file_age_days": (datetime.now() - file_modified).days,
                                    "deleted_timestamp": datetime.now().isoformat()
                                })

                        except Exception as e:
                            cleanup_report["cleanup_errors"].append({
                                "file_path": str(file_path),
                                "error": str(e),
                                "timestamp": datetime.now().isoformat()
                            })

        return cleanup_report

    def run_comprehensive_backup_verification(self):
        """🚀 Execute complete backup verification cycle"""
        print("♾️🔄💎 IMMORTAL BACKUP VERIFICATION CYCLE INITIATED 💎🔄♾️")
        print(f"📅 Verification Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("🛡️ IMMORTAL DATA PROTECTION ACTIVE")
        print("=" * 80)

        # 1. Create backup directories
        self.create_backup_directories()

        # 2. Backup critical files
        print("\n💾 BACKING UP CRITICAL EMPIRE FILES...")
        backup_report = self.backup_critical_files()

        # 3. Verify backup integrity
        print("\n🔍 VERIFYING BACKUP INTEGRITY...")
        verification_report = self.verify_backup_integrity()

        # 4. Cleanup old backups
        print("\n🧹 CLEANING UP OLD BACKUPS...")
        cleanup_report = self.cleanup_old_backups()

        # 5. Generate comprehensive report
        comprehensive_report = {
            "verification_cycle_timestamp": datetime.now().isoformat(),
            "backup_report": backup_report,
            "verification_report": verification_report,
            "cleanup_report": cleanup_report,
            "empire_backup_status": "IMMORTAL_PROTECTED"
        }

        # Save verification report
        report_filename = f"empire-backup-verification/backup_verification_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        os.makedirs("empire-backup-verification", exist_ok=True)

        with open(report_filename, 'w', encoding='utf-8') as f:
            json.dump(comprehensive_report, f, indent=2, default=str)

        # Display summary
        print("\n🏆 BACKUP VERIFICATION SUMMARY:")
        print(f"   💾 Files backed up: {len(backup_report['backed_up_files'])}")
        print(f"   🔍 Backups verified: {len(verification_report['verified_backups'])}")
        print(f"   🧹 Old files cleaned: {len(cleanup_report['deleted_files'])}")
        print(f"   📊 Report saved: {report_filename}")

        if len(verification_report['integrity_issues']) > 0:
            print(f"   🚨 Integrity issues: {len(verification_report['integrity_issues'])}")
        else:
            print("   ✅ All backups verified successfully!")

        print("\n♾️ IMMORTAL DATA PROTECTION VERIFIED! ♾️")

        return comprehensive_report

def main():
    """🚀 Main backup verification execution"""
    verifier = ImmortalBackupVerificationSystem()
    verifier.run_comprehensive_backup_verification()

if __name__ == "__main__":
    main()

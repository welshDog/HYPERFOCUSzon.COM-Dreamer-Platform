#!/usr/bin/env python3
"""
🚨💎⚡ HYPERFOCUS ZONE EMERGENCY SECURITY FIXER ⚡💎🚨
Immediately fixes all exposed Discord tokens across the empire
Following BROski Ultra LOOK-THEN-BUILD System Protocol
"""

import re
from pathlib import Path
from typing import List, Tuple

from hyperfocus_security_config import HyperfocusSecurityConfig


class EmergencySecurityFixer:
    """🚨 Emergency security token replacement system"""

    def __init__(self, empire_root: str = "h:/"):
        self.empire_root = Path(empire_root)
        self.security_config = HyperfocusSecurityConfig()
        self.logger = self.security_config._setup_logger()

        # Known exposed token patterns (first part only for safety)
        self.exposed_patterns = [
            r'MTM4MTk2NTY1Njk3NDU2MTMwMA\.[^"\']+',  # The exposed token pattern
            r'["\']MTM4MTk2NTY1Njk3NDU2MTMwMA\.[^"\']+["\']',  # Quoted version
        ]

        self.files_fixed = []
        self.files_with_issues = []

    def scan_for_exposed_tokens(self) -> List[Tuple[Path, int, str]]:
        """🔍 Scan empire for exposed Discord tokens"""
        self.logger.info("🚨 SCANNING EMPIRE FOR EXPOSED TOKENS...")

        exposed_instances = []

        # File patterns to check
        file_patterns = ["*.py", "*.md", "*.json", "*.txt"]

        for pattern in file_patterns:
            for file_path in self.empire_root.rglob(pattern):
                try:
                    if (
                        file_path.is_file() and file_path.stat().st_size < 10_000_000
                    ):  # Skip huge files
                        self._scan_file_for_tokens(file_path, exposed_instances)
                except (OSError, UnicodeDecodeError):
                    continue

        return exposed_instances

    def _scan_file_for_tokens(self, file_path: Path, exposed_instances: List):
        """🔍 Scan individual file for exposed tokens"""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            for line_num, line in enumerate(content.split("\n"), 1):
                for pattern in self.exposed_patterns:
                    if re.search(pattern, line):
                        exposed_instances.append((file_path, line_num, line.strip()))

        except (UnicodeDecodeError, OSError):
            pass

    def create_secure_replacement(self, file_path: Path) -> str:
        """🔐 Create secure replacement for Discord token usage"""
        file_ext = file_path.suffix.lower()

        if file_ext == ".py":
            return """# 🔐 SECURE: Get Discord token from environment
from hyperfocus_security_config import HyperfocusSecurityConfig
security_config = HyperfocusSecurityConfig()
TOKEN = security_config.get_discord_token()

if not TOKEN:
    print("❌ Discord token not found! Please set DISCORD_BOT_TOKEN in your .env file")
    exit(1)"""

        elif file_ext == ".md":
            return """**🔐 SECURE TOKEN CONFIGURATION:**
- Set `DISCORD_BOT_TOKEN` in your `.env` file
- Never commit actual tokens to version control
- Use environment variables for all sensitive data"""

        elif file_ext == ".json":
            return '"bot_token": "SECURE_ENV_VAR_DISCORD_BOT_TOKEN"'

        else:
            return "DISCORD_BOT_TOKEN=your_secure_token_here"

    def fix_exposed_tokens(self, exposed_instances: List[Tuple[Path, int, str]]):
        """🛠️ Fix all exposed tokens"""
        self.logger.info(
            f"🔧 FIXING {len(exposed_instances)} EXPOSED TOKEN INSTANCES..."
        )

        files_to_fix = {}

        # Group by file
        for file_path, line_num, line_content in exposed_instances:
            if file_path not in files_to_fix:
                files_to_fix[file_path] = []
            files_to_fix[file_path].append((line_num, line_content))

        # Fix each file
        for file_path, instances in files_to_fix.items():
            self._fix_file_tokens(file_path, instances)

    def _fix_file_tokens(self, file_path: Path, instances: List[Tuple[int, str]]):
        """🔧 Fix tokens in a specific file"""
        try:
            # Read current content
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Replace exposed patterns
            original_content = content
            for pattern in self.exposed_patterns:
                if file_path.suffix.lower() == ".py":
                    # For Python files, replace with secure loading
                    content = re.sub(
                        pattern, "security_config.get_discord_token()", content
                    )
                elif file_path.suffix.lower() == ".md":
                    # For markdown, replace with placeholder
                    content = re.sub(pattern, "**[SECURE_TOKEN_REMOVED]**", content)
                else:
                    # For other files, use environment variable reference
                    content = re.sub(pattern, "${DISCORD_BOT_TOKEN}", content)

            # Only write if content changed
            if content != original_content:
                # Create backup
                backup_path = file_path.with_suffix(file_path.suffix + ".backup")
                with open(backup_path, "w", encoding="utf-8") as f:
                    f.write(original_content)

                # Write secured content
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)

                self.files_fixed.append(file_path)
                self.logger.info(f"✅ Fixed: {file_path}")

        except Exception as e:
            self.files_with_issues.append((file_path, str(e)))
            self.logger.error(f"❌ Failed to fix {file_path}: {e}")

    def generate_security_report(self) -> str:
        """📊 Generate security fix report"""
        report = f"""
🚨💎⚡ EMERGENCY SECURITY FIX REPORT ⚡💎🚨
==============================================

✅ FILES SUCCESSFULLY SECURED: {len(self.files_fixed)}
❌ FILES WITH ISSUES: {len(self.files_with_issues)}

🔒 SECURED FILES:
"""
        for file_path in self.files_fixed:
            report += f"   ✅ {file_path}\n"

        if self.files_with_issues:
            report += f"\n⚠️ FILES NEEDING MANUAL REVIEW:\n"
            for file_path, error in self.files_with_issues:
                report += f"   ❌ {file_path}: {error}\n"

        report += f"""
🛡️ NEXT STEPS:
1. Create .env file with: DISCORD_BOT_TOKEN=your_new_secure_token
2. Revoke the exposed Discord token in Discord Developer Portal
3. Generate a new Discord bot token
4. Test all Discord bot functionality
5. Review and remove .backup files once confirmed working

📋 SECURITY CHECKLIST:
☐ Discord token revoked and replaced
☐ .env file created with new token
☐ All affected files tested
☐ Backup files cleaned up
☐ Security scan re-run to confirm

STATUS: SECURITY BREACH CONTAINED - MANUAL STEPS REQUIRED
"""
        return report

    def execute_emergency_fix(self):
        """🚨 Execute complete emergency security fix"""
        self.logger.info("🚨 EXECUTING EMERGENCY SECURITY FIX...")

        # Scan for exposed tokens
        exposed_instances = self.scan_for_exposed_tokens()

        if not exposed_instances:
            self.logger.info("✅ No exposed tokens found! Empire is secure.")
            return

        self.logger.warning(
            f"🚨 FOUND {len(exposed_instances)} EXPOSED TOKEN INSTANCES!"
        )

        # Fix exposed tokens
        self.fix_exposed_tokens(exposed_instances)

        # Generate report
        report = self.generate_security_report()

        # Save report
        report_path = (
            self.empire_root
            / f"SECURITY_FIX_REPORT_{self.security_config.get_empire_config()['environment']}.md"
        )
        with open(report_path, "w") as f:
            f.write(report)

        self.logger.info(f"📊 Security report saved: {report_path}")
        print(report)


def main():
    """🚨 Main emergency security fix function"""
    fixer = EmergencySecurityFixer()
    fixer.execute_emergency_fix()


if __name__ == "__main__":
    main()

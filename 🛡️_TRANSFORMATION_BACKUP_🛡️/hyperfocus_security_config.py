#!/usr/bin/env python3
"""
🔐💎⚡ HYPERFOCUS ZONE SECURITY CONFIGURATION ENGINE ⚡💎🔐
Universal security and environment management for the empire
Following BROski Ultra LOOK-THEN-BUILD System Protocol
"""

import logging
import os
import sys
from pathlib import Path
from typing import Any, Dict, Optional

from dotenv import load_dotenv


class HyperfocusSecurityConfig:
    """🛡️ Centralized security and environment configuration"""

    def __init__(self, empire_root: str = "h:/"):
        self.empire_root = Path(empire_root)
        self.logger = self._setup_logger()
        self._load_environment()

    def _setup_logger(self) -> logging.Logger:
        """⚡ Setup standardized logging for all empire modules"""
        logger = logging.getLogger("HYPERFOCUS_EMPIRE_SECURITY")

        if not logger.handlers:
            handler = logging.StreamHandler(sys.stdout)
            formatter = logging.Formatter(
                "🔐 %(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.setLevel(logging.INFO)

        return logger

    def _load_environment(self):
        """🌍 Load environment variables securely"""
        # Look for .env file in multiple locations
        env_paths = [self.empire_root / ".env", Path(".env"), Path("../.env")]

        env_loaded = False
        for env_path in env_paths:
            if env_path.exists():
                load_dotenv(env_path)
                self.logger.info(f"✅ Environment loaded from: {env_path}")
                env_loaded = True
                break

        if not env_loaded:
            self.logger.warning(
                "⚠️ No .env file found. Using system environment variables only."
            )

    def get_discord_token(self) -> Optional[str]:
        """🤖 Get Discord token securely"""
        token = os.getenv("DISCORD_BOT_TOKEN")
        if not token:
            self.logger.error(
                "❌ DISCORD_BOT_TOKEN not found in environment variables!"
            )
            self.logger.info("💡 Please set DISCORD_BOT_TOKEN in your .env file")
            return None
        return token

    def get_api_endpoint(self, service: str) -> Optional[str]:
        """🌐 Get API endpoint for service"""
        endpoint_map = {
            "pi": "PI_API_ENDPOINT",
            "gemini": "GEMINI_API_KEY",
            "grafana": "GRAFANA_ENDPOINT",
            "prometheus": "PROMETHEUS_ENDPOINT",
        }

        env_var = endpoint_map.get(service.lower())
        if not env_var:
            self.logger.warning(f"⚠️ Unknown service: {service}")
            return None

        return os.getenv(env_var)

    def get_empire_config(self) -> Dict[str, Any]:
        """🏆 Get empire-wide configuration"""
        return {
            "empire_root": os.getenv("EMPIRE_ROOT_PATH", str(self.empire_root)),
            "memory_crystal_vault": os.getenv(
                "MEMORY_CRYSTAL_VAULT_PATH",
                str(self.empire_root / "🔮💎_MEMORY_CRYSTAL_VAULT_💎🔮"),
            ),
            "backup_path": os.getenv(
                "BACKUP_CRYSTAL_PATH", str(self.empire_root / "memory_crystals_backup")
            ),
            "debug_mode": os.getenv("DEBUG_MODE", "false").lower() == "true",
            "environment": os.getenv("ENVIRONMENT", "development"),
            "legendary_threshold": int(os.getenv("LEGENDARY_STATUS_THRESHOLD", "720")),
            "hyperfocus_mode": os.getenv("HYPERFOCUS_MODE", "enabled") == "enabled",
            "dopamine_notifications": os.getenv(
                "DOPAMINE_NOTIFICATIONS", "true"
            ).lower()
            == "true",
        }

    def validate_configuration(self) -> bool:
        """✅ Validate all critical configuration"""
        self.logger.info("🔍 Validating empire configuration...")

        config = self.get_empire_config()
        issues = []

        # Check critical paths exist
        empire_root = Path(config["empire_root"])
        if not empire_root.exists():
            issues.append(f"Empire root path does not exist: {empire_root}")

        memory_vault = Path(config["memory_crystal_vault"])
        if not memory_vault.exists():
            self.logger.info(f"📁 Creating memory crystal vault: {memory_vault}")
            memory_vault.mkdir(parents=True, exist_ok=True)

        # Check for security tokens
        if not self.get_discord_token():
            issues.append("Discord token not configured")

        if issues:
            self.logger.error("❌ Configuration issues found:")
            for issue in issues:
                self.logger.error(f"   - {issue}")
            return False

        self.logger.info("✅ Configuration validation complete - ALL SYSTEMS SECURE!")
        return True

    def create_secure_template(self, filename: str) -> str:
        """🔐 Create secure code template with proper imports"""
        return f'''#!/usr/bin/env python3
"""
🌌💎⚡ HYPERFOCUS ZONE EMPIRE - {filename.upper()} ⚡💎🌌
Secure implementation following BROski Ultra LOOK-THEN-BUILD System
"""

import os
import sys
import logging
from pathlib import Path
from hyperfocus_security_config import HyperfocusSecurityConfig

# Initialize secure configuration
security_config = HyperfocusSecurityConfig()
logger = security_config._setup_logger()
empire_config = security_config.get_empire_config()

def main():
    """🚀 Main function with security validation"""
    if not security_config.validate_configuration():
        logger.error("❌ Security validation failed. Exiting.")
        sys.exit(1)

    logger.info("🔐 Security validation passed. Starting {filename}...")

    # Your secure implementation here

if __name__ == "__main__":
    main()
'''


# Global instance for easy importing
security_config = HyperfocusSecurityConfig()


def get_secure_logger(name: str = "HYPERFOCUS_EMPIRE") -> logging.Logger:
    """🔐 Get standardized secure logger"""
    return security_config._setup_logger()


def validate_empire_security() -> bool:
    """🛡️ Quick security validation"""
    return security_config.validate_configuration()

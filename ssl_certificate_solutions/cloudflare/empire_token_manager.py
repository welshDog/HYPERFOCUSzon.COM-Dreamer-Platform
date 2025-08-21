#!/usr/bin/env python3
"""
🔐 HYPERFOCUS ZONE EMPIRE - SECURE TOKEN MANAGER 🔐
Safely manages API tokens and keys for Empire operations
"""

import getpass
import json
import os
from pathlib import Path


class EmpireTokenManager:
    """Secure token management for HYPERFOCUS ZONE EMPIRE"""

    def __init__(self):
        self.tokens_file = Path.home() / ".empire_tokens.json"
        self.tokens = self.load_tokens()

    def load_tokens(self):
        """Load tokens from secure storage"""
        if self.tokens_file.exists():
            try:
                with open(self.tokens_file, "r") as f:
                    return json.load(f)
            except:
                return {}
        return {}

    def save_tokens(self):
        """Save tokens to secure storage"""
        try:
            with open(self.tokens_file, "w") as f:
                json.dump(self.tokens, f, indent=2)
            # Set restrictive permissions (owner only)
            self.tokens_file.chmod(0o600)
            return True
        except:
            return False

    def get_token(self, token_name, prompt_message=None):
        """Get token with fallback to environment and prompt"""
        # Check environment first
        env_token = os.getenv(token_name)
        if env_token and env_token != "your_token_here":
            return env_token

        # Check stored tokens
        if token_name in self.tokens:
            return self.tokens[token_name]

        # Prompt for token
        if prompt_message:
            print(f"\n🔑 {prompt_message}")
        else:
            print(f"\n🔑 Please enter your {token_name}:")

        token = getpass.getpass("Token (hidden): ").strip()

        if token:
            # Ask if user wants to save it
            save_choice = input("💾 Save token for future use? (y/N): ").lower()
            if save_choice == "y":
                self.tokens[token_name] = token
                if self.save_tokens():
                    print("✅ Token saved securely")
                else:
                    print("⚠️  Token saved for session only")

            # Set environment variable for current session
            os.environ[token_name] = token
            return token

        return None

    def remove_token(self, token_name):
        """Remove a stored token"""
        if token_name in self.tokens:
            del self.tokens[token_name]
            self.save_tokens()
            print(f"🗑️  {token_name} removed from secure storage")

        # Also remove from environment
        if token_name in os.environ:
            del os.environ[token_name]

    def list_tokens(self):
        """List stored token names (not values)"""
        print("\n🔑 STORED TOKENS:")
        if self.tokens:
            for token_name in self.tokens.keys():
                print(f"   ✅ {token_name}")
        else:
            print("   📝 No tokens stored")

    def setup_cloudflare_token(self):
        """Interactive Cloudflare token setup"""
        print("\n🌩️  CLOUDFLARE API TOKEN SETUP")
        print("=" * 40)
        print("📋 Steps to get your token:")
        print("   1. Visit: https://dash.cloudflare.com/profile/api-tokens")
        print("   2. Click 'Create Token'")
        print("   3. Use 'Custom token' template")
        print("   4. Set permissions:")
        print("      - Zone: Zone:Edit")
        print("      - Zone Resources: Include - All zones")
        print("   5. Copy the generated token")

        return self.get_token(
            "CLOUDFLARE_API_TOKEN", "Enter your Cloudflare API token:"
        )

    def setup_huggingface_token(self):
        """Interactive HuggingFace token setup"""
        print("\n🤗 HUGGINGFACE TOKEN SETUP")
        print("=" * 40)
        print("📋 Steps to get your token:")
        print("   1. Visit: https://huggingface.co/settings/tokens")
        print("   2. Click 'New token'")
        print("   3. Choose 'Read' access type")
        print("   4. Copy the generated token")

        return self.get_token("HF_TOKEN", "Enter your HuggingFace token:")


def main():
    """Token manager CLI"""
    tm = EmpireTokenManager()

    print("🏆 HYPERFOCUS ZONE EMPIRE - SECURE TOKEN MANAGER")
    print("=" * 60)

    while True:
        print("\n🔐 TOKEN MANAGEMENT OPTIONS:")
        print("   1. Setup Cloudflare API Token")
        print("   2. Setup HuggingFace Token")
        print("   3. List stored tokens")
        print("   4. Remove a token")
        print("   5. Exit")

        choice = input("\nChoose option (1-5): ").strip()

        if choice == "1":
            token = tm.setup_cloudflare_token()
            if token:
                print(f"✅ Cloudflare token configured: {token[:10]}...")

        elif choice == "2":
            token = tm.setup_huggingface_token()
            if token:
                print(f"✅ HuggingFace token configured: {token[:10]}...")

        elif choice == "3":
            tm.list_tokens()

        elif choice == "4":
            tm.list_tokens()
            if tm.tokens:
                token_name = input("Enter token name to remove: ").strip()
                tm.remove_token(token_name)

        elif choice == "5":
            print("👋 Empire Token Manager closed")
            break

        else:
            print("❌ Invalid option")


if __name__ == "__main__":
    main()

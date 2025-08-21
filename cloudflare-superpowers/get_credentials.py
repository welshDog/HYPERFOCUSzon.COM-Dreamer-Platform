#!/usr/bin/env python3
"""
🏆 HYPERFOCUS ZONE EMPIRE - CLOUDFLARE CREDENTIALS FETCHER 🏆
⚡ Get Account ID and Zone ID for Workers AI deployment ⚡
"""

import os

from dotenv import load_dotenv


def get_cloudflare_credentials():
    """Get Account ID and Zone ID from Cloudflare API"""

    print("🔍 Fetching Cloudflare credentials...")

    load_dotenv()
    api_token = os.getenv("CLOUDFLARE_API_TOKEN")

    if not api_token or api_token == "your_api_token_here":
        print("❌ API token not configured")
        return None, None

    try:
        import cloudflare

        cf = cloudflare.Cloudflare(api_token=api_token)

        # Get Account ID
        print("📊 Getting account information...")
        accounts = cf.accounts.list()

        account_id = None
        if accounts and len(accounts.result) > 0:
            account = accounts.result[0]
            account_id = account.id
            print(f"✅ Account ID: {account_id}")
        else:
            print("❌ No accounts found")
            return None, None

        # Get Zone ID for hyperfocuszone.com
        print("🌐 Getting zone information...")
        zones = cf.zones.list(name="hyperfocuszone.com")

        zone_id = None
        if zones and len(zones.result) > 0:
            zone = zones.result[0]
            zone_id = zone.id
            print(f"✅ Zone ID: {zone_id}")
        else:
            print("❌ Zone hyperfocuszone.com not found")
            return account_id, None

        return account_id, zone_id

    except Exception as e:
        print(f"❌ Error fetching credentials: {e}")
        return None, None


def update_env_file(account_id, zone_id):
    """Update .env file with Account ID and Zone ID"""

    if not account_id:
        print("⚠️ Account ID not available, skipping .env update")
        return False

    try:
        # Read current .env file
        with open(".env", "r") as f:
            content = f.read()

        # Update Account ID
        content = content.replace(
            "CLOUDFLARE_ACCOUNT_ID=your_account_id_here",
            f"CLOUDFLARE_ACCOUNT_ID={account_id}",
        )

        # Update Zone ID if available
        if zone_id:
            content = content.replace(
                "CLOUDFLARE_ZONE_ID=your_zone_id_here", f"CLOUDFLARE_ZONE_ID={zone_id}"
            )

        # Write updated content
        with open(".env", "w") as f:
            f.write(content)

        print("✅ .env file updated successfully")
        return True

    except Exception as e:
        print(f"❌ Error updating .env file: {e}")
        return False


def main():
    print("🌟" + "=" * 78 + "🌟")
    print("🏆 HYPERFOCUS ZONE EMPIRE - CLOUDFLARE SETUP 🏆")
    print("🌟" + "=" * 78 + "🌟")
    print()

    # Get credentials
    account_id, zone_id = get_cloudflare_credentials()

    if account_id:
        print()
        print("🎯 CREDENTIALS FOUND:")
        print(f"   🏢 Account ID: {account_id}")
        if zone_id:
            print(f"   🌐 Zone ID: {zone_id}")
        else:
            print("   🌐 Zone ID: Not found (manual setup needed)")
        print()

        # Update .env file
        if update_env_file(account_id, zone_id):
            print("🚀 READY FOR WORKERS AI DEPLOYMENT!")
            print()
            print("Next steps:")
            print("1. Run: python workers_ai_integration.py")
            print("2. Test your hyperfocus coaching assistant")
            print("3. Deploy to production")
        else:
            print("⚠️ Manual .env update needed")
    else:
        print("❌ Could not retrieve credentials")
        print("💡 Check your API token permissions")

    print()
    print("🏆" + "=" * 78 + "🏆")


if __name__ == "__main__":
    main()

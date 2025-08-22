#!/usr/bin/env python3
"""
🔍💎⚡ DISCORD BOT TOKEN TEST ⚡💎🔍
Quick test to verify Discord token and connection
"""

import asyncio
import os

import discord
from dotenv import load_dotenv

# Load environment
load_dotenv("h:/.env")


def test_token():
    token = os.getenv("DISCORD_BOT_TOKEN")
    print(f"🔍 Token found: {bool(token)}")
    print(f"🔍 Token length: {len(token) if token else 0}")

    if token:
        print(f"🔍 Token starts with: {token[:20]}...")
        return token
    else:
        print("❌ No Discord token found!")
        return None


async def test_discord_connection():
    token = test_token()
    if not token:
        return

    try:
        print("🤖 Creating Discord client...")
        intents = discord.Intents.default()
        intents.message_content = True
        client = discord.Client(intents=intents)

        @client.event
        async def on_ready():
            print(f"🎉 SUCCESS! Bot logged in as {client.user}")
            print(f"🌟 Bot is in {len(client.guilds)} servers")
            await client.close()

        print("🚀 Attempting to connect to Discord...")
        await client.start(token)

    except discord.errors.LoginFailure:
        print("❌ INVALID TOKEN: Discord login failed!")
    except Exception as e:
        print(f"❌ CONNECTION ERROR: {e}")


if __name__ == "__main__":
    asyncio.run(test_discord_connection())

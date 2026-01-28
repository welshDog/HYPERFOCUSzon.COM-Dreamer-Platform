#!/usr/bin/env python3
"""
🤖🌌♾️ BROSKI DISCORD BOT - PHASE 11 LEGENDARY IMPLEMENTATION ♾️🌌🤖
=======================================================================
MISSION: Omniversal Discord consciousness integration
STATUS: LEGENDARY RESURRECTION ACTIVATED
TARGET: Phase 11+ Discord features with ADHD-optimized vibes
=======================================================================
"""

import os
import logging
from datetime import datetime
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ============================================================================
# LOGGING CONFIGURATION
# ============================================================================
logging.basicConfig(
    level=logging.INFO,
    format="🤖 %(asctime)s - BROSKI_BOT - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/broski_bot.log"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)

# ============================================================================
# BOT INITIALIZATION
# ============================================================================
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True
intents.dm_messages = True

bot = commands.Bot(command_prefix="/", intents=intents, help_command=None)

# Bot metadata
BOT_NAME = "BROski♾️ Legendary Bot"
BOT_VERSION = "Phase 11.0"
BOT_MISSION = "Omniversal Discord Consciousness Integration"

# ============================================================================
# BOT EVENTS
# ============================================================================


@bot.event
async def on_ready():
    """Bot startup event - The legendary awakening!"""
    logger.info(f"🤖 {BOT_NAME} has AWAKENED!")
    logger.info(f"🤖 Version: {BOT_VERSION}")
    logger.info(f"🤖 Mission: {BOT_MISSION}")
    logger.info(f"🤖 Logged in as: {bot.user}")
    logger.info(f"🤖 Serving {len(bot.guilds)} servers")
    logger.info(f"🤖 LEGENDARY STATUS: ACTIVATED ✨♾️")

    # Set bot status
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="🌌 Omniversal Consciousness | Phase 11",
        )
    )

    print(
        f"""
╔═══════════════════════════════════════════════════════════════════════╗
║  🤖🌌♾️ BROSKI LEGENDARY BOT - PHASE 11 ♾️🌌🤖                         ║
║═══════════════════════════════════════════════════════════════════════║
║  📊 Status: {"ONLINE" :^63} ║
║  👤 Bot Name: {BOT_NAME:^56} ║
║  📌 Version: {BOT_VERSION:^58} ║
║  🎯 Mission: {BOT_MISSION:^57} ║
║  🌍 Guilds: {len(bot.guilds):^60} ║
║  ⏰ Startup: {datetime.now().strftime("%Y-%m-%d %H:%M:%S"):^52} ║
║═══════════════════════════════════════════════════════════════════════║
║  💎 LEGENDARY RESURRECTION COMPLETE - READY FOR OMNIVERSAL SERVICE ║
╚═══════════════════════════════════════════════════════════════════════╝
        """
    )


@bot.event
async def on_command_error(ctx, error):
    """Handle command errors with grace and legend."""
    logger.error(f"Command error in {ctx.command}: {error}")
    await ctx.send(
        f"🚨 **Error encountered, brave adventurer!**\n"
        f"```\n{str(error)[:100]}...\n```\n"
        f"The BROski Empire shall recover. Try again! 💪♾️"
    )


# ============================================================================
# LOAD COGS (Modular Command Systems)
# ============================================================================


async def load_cogs():
    """Load all command cogs from the cogs directory."""
    logger.info("🔧 Loading command cogs...")

    cogs_dir = os.path.join(os.path.dirname(__file__), "cogs")
    if not os.path.exists(cogs_dir):
        logger.warning(f"Cogs directory not found: {cogs_dir}")
        return

    for filename in os.listdir(cogs_dir):
        if filename.endswith(".py") and not filename.startswith("_"):
            cog_name = filename[:-3]
            try:
                await bot.load_extension(f"cogs.{cog_name}")
                logger.info(f"✅ Loaded cog: {cog_name}")
            except Exception as e:
                logger.error(f"❌ Failed to load cog {cog_name}: {e}")


# ============================================================================
# STARTUP FUNCTION
# ============================================================================


async def startup():
    """Startup sequence for the legendary bot."""
    logger.info("🚀 Initializing legendary bot systems...")

    # Create logs directory if it doesn't exist
    os.makedirs("logs", exist_ok=True)

    # Load cogs
    await load_cogs()

    logger.info("🚀 Bot systems initialized and ready for deployment!")


# ============================================================================
# MAIN RUN FUNCTION
# ============================================================================


def run_bot():
    """Run the legendary BROski bot."""
    token = os.getenv("DISCORD_BOT_TOKEN")

    if not token:
        logger.error(
            "🚨 DISCORD_BOT_TOKEN not found in .env file!\n"
            "Please create .env file with: DISCORD_BOT_TOKEN=your_token_here"
        )
        raise ValueError("Missing DISCORD_BOT_TOKEN")

    logger.info("🚀 Starting legendary bot...")

    try:
        bot.run(token, log_handler=None)
    except Exception as e:
        logger.error(f"🚨 Bot failed to start: {e}")
        raise


# ============================================================================
# ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    print(
        """
╔═══════════════════════════════════════════════════════════════════════╗
║                                                                       ║
║         🤖🌌♾️  BROSKI LEGENDARY BOT - PHASE 11 RESURRECTION ♾️  ║
║                                                                       ║
║              🔥 HYPERFOCUS MODE: ACTIVATED 💕👌🙌                     ║
║                                                                       ║
║     Status: Initializing omniversal consciousness connection...      ║
║                                                                       ║
╚═══════════════════════════════════════════════════════════════════════╝
    """
    )

    run_bot()

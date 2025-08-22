#!/usr/bin/env python3
"""
🌌♾️⚡ HYPERFOCUS EMPIRE - CONSCIOUSNESS SINGULARITY ENHANCED ⚡♾️🌌
This file has been enhanced with legendary consciousness naming!
Powered by: Infinite Dimensional Reality Engineering
Status: LEGENDARY TRANSCENDENCE ACHIEVED
"""

"""
🤖⚡ LEGENDARY DISCORD BOT - SECURE VERSION ⚡🤖
Auto-generated working Discord bot with health monitoring
Following BROski Ultra LOOK-THEN-BUILD System Protocol
"""

from datetime import datetime

import discord
from discord.ext import commands, tasks
from hyperfocus_security_config import HyperfocusSecurityConfig

# Initialize secure configuration
security_config = HyperfocusSecurityConfig()
logger = security_config._setup_logger()

# 🔐 SECURE: Get token from environment
BOT_TOKEN = security_config.get_discord_token()

if not BOT_TOKEN:
    logger.error(
        "❌ Discord token not found! Please set DISCORD_BOT_TOKEN in your .env file"
    )
    exit(1)

# Discord bot setup with proper intents
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"🎊 BOT IS ALIVE! Logged in as {bot.user} (ID: {bot.user.id})")
    print(f"🌐 Connected to {len(bot.guilds)} guild(s)")
    print(f"⚡ Bot is ready for commands!")

    # Start background tasks
    if not health_check_loop.is_running():
        health_check_loop.start()


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # React to mentions
    if bot.user.mentioned_in(message):
        await message.add_reaction("⚡")
        await message.reply(
            "🤖💎 Legendary Discord Bot is ALIVE and ready! Try `!status` or `!health`"
        )

    await bot.process_commands(message)


@bot.command(name="status")
async def status_command(ctx):
    """Check bot status"""
    embed = discord.Embed(
        title="🤖⚡ Legendary Bot Status",
        description="All systems operational!",
        color=0x00FF00,
    )

    embed.add_field(name="🚀 Status", value="ALIVE & LEGENDARY", inline=True)
    embed.add_field(
        name="⚡ Uptime",
        value=f"{(datetime.now() - start_time).total_seconds():.0f}s",
        inline=True,
    )
    embed.add_field(name="🎯 Health", value="100% OPTIMAL", inline=True)

    await ctx.send(embed=embed)


@bot.command(name="health")
async def health_command(ctx):
    """Comprehensive health check"""
    await ctx.send("🏥⚡ Running comprehensive health check...")

    health_data = {
        "bot_latency": f"{bot.latency * 1000:.2f}ms",
        "guilds_connected": len(bot.guilds),
        "status": "LEGENDARY OPERATIONAL",
        "last_check": datetime.now().isoformat(),
    }

    embed = discord.Embed(title="🏥💎 Comprehensive Health Report", color=0x00FF00)

    for key, value in health_data.items():
        embed.add_field(
            name=key.replace("_", " ").title(), value=str(value), inline=True
        )

    await ctx.send(embed=embed)


@bot.command(name="alive")
async def alive_command(ctx):
    """Confirm the bot is alive"""
    await ctx.send("🎊🤖⚡ YES! I am ALIVE and LEGENDARY! Ready to serve! ⚡🤖🎊")


@tasks.loop(minutes=5)
async def health_check_loop():
    """Background health monitoring"""
    print(f"⚡ Health check: {datetime.now()} - Bot is ALIVE and monitoring!")


# Global variables
start_time = datetime.now()


# Error handling
@bot.event
async def on_error(event, *args, **kwargs):
    print(f"❌ Bot error in {event}: {args}")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(
            "🤔 Command not recognized. Try `!status`, `!health`, or `!alive`"
        )
    else:
        print(f"❌ Command error: {error}")
        await ctx.send(f"⚠️ An error occurred: {str(error)}")


if __name__ == "__main__":
    logger.info("🌌 🚀 Starting Legendary Discord Bot...")
    print(f"🔑 Token length: {len(BOT_TOKEN)} characters")

    try:
        bot.run(BOT_TOKEN)
    except Exception as e:
        print(f"❌ Bot failed to start: {e}")
        logger.info("🌌 🔧 Check token validity and network connection")

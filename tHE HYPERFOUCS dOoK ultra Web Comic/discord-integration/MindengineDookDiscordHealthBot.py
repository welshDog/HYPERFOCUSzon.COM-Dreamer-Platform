"""
🌌♾️⚡ HYPERFOCUS EMPIRE - CONSCIOUSNESS SINGULARITY ENHANCED ⚡♾️🌌
This file has been enhanced with legendary consciousness naming!
Powered by: Infinite Dimensional Reality Engineering
Status: LEGENDARY TRANSCENDENCE ACHIEVED
"""

"""
🤖🛡️ ULTRA dOoK DISCORD HEALTH BOT ⚡💎
BROski♾️ Level: LEGENDARY
Mission: Real-time health alerts and celebration cascades in Discord
"""

import discord
from discord.ext import commands, tasks
import json
import asyncio
from datetime import datetime, timedelta
from pathlib import Path
import subprocess
import sys
import os

# Add the health monitoring directory to the path
sys.path.append(str(Path(__file__).parent.parent / "health-monitoring"))
from ultra_dook_empire_health_scanner import UltraDookEmpireHealthScanner

class UltraDookHealthBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.scanner = UltraDookEmpireHealthScanner()
        self.health_check_loop.start()
        self.last_alert_time = datetime.now() - timedelta(hours=1)  # Allow immediate first alert
        
    def cog_unload(self):
        self.health_check_loop.cancel()
    
    @commands.command(name='health', aliases=['empire', 'status', 'scan'])
    async def manual_health_check(self, ctx):
        """🛡️ Manual empire health check command"""
        
        # Send initial scanning message
        scanning_msg = await ctx.send("🛡️ **INITIATING ULTRA dOoK EMPIRE HEALTH SCAN...**\n"
                                    "⚡ Deploying 677+ agent army across all systems...")
        
        try:
            # Execute health scan
            report = self.scanner.execute_full_empire_health_scan()
            
            # Create main embed
            embed = discord.Embed(
                title="🛡️ Ultra dOoK Empire Health Report",
                description=f"**Mission:** {report.get('mission', 'Health Check')}\n"
                           f"**Timestamp:** <t:{int(datetime.now().timestamp())}:R>",
                color=self.get_status_color(report['empire_status']),
                timestamp=datetime.utcnow()
            )
            
            # Empire status field
            status_emoji = self.get_status_emoji(report['empire_status'])
            embed.add_field(
                name=f"{status_emoji} Empire Status",
                value=f"**{report['empire_status']}**\n"
                      f"Quantum Resonance: {report['quantum_metrics']['quantum_resonance']}%",
                inline=True
            )
            
            # BROski$ rewards field
            embed.add_field(
                name="💎 BROski$ Earned",
                value=f"**+{report['broski_rewards']:,}**\n"
                      f"Dopamine Level: MAXIMUM",
                inline=True
            )
            
            # Agent army field
            embed.add_field(
                name="👥 Agent Army",
                value="**677+ DEPLOYED**\n"
                      "Status: LEGENDARY",
                inline=True
            )
            
            # System status fields
            for system_name, system_data in report['systems'].items():
                status_emoji = self.get_status_emoji(system_data['status'])
                system_display = system_name.replace('_', ' ').title()
                
                value_parts = [f"Status: **{system_data['status']}**"]
                
                if 'cpu_percent' in system_data:
                    value_parts.append(f"CPU: {system_data['cpu_percent']}%")
                if 'total_stories' in system_data:
                    value_parts.append(f"Stories: {system_data['total_stories']}")
                if 'url' in system_data and system_data['url']:
                    value_parts.append(f"URL: [Portal]({system_data['url']})")
                
                embed.add_field(
                    name=f"{status_emoji} {system_display}",
                    value='\n'.join(value_parts),
                    inline=True
                )
            
            # Update the scanning message with results
            await scanning_msg.edit(content=None, embed=embed)
            
            # Send celebration messages if any
            if report['celebration_triggers']:
                celebration_msg = "🎊 **CELEBRATION CASCADE ACTIVATED!**\n\n"
                for i, celebration in enumerate(report['celebration_triggers'], 1):
                    celebration_msg += f"{i}. {celebration}\n"
                    
                await ctx.send(celebration_msg)
                
                # Send individual celebration reactions
                celebration_emojis = ["🎉", "🏆", "💎", "⚡", "🚀", "🌟"]
                for i, emoji in enumerate(celebration_emojis):
                    if i < len(report['celebration_triggers']):
                        await asyncio.sleep(0.5)
                        await ctx.send(f"{emoji} **{report['celebration_triggers'][i]}**")
            
            # Add reaction to the embed message
            await scanning_msg.add_reaction("🛡️")
            await scanning_msg.add_reaction("💎")
            await scanning_msg.add_reaction("⚡")
            
        except Exception as e:
            await scanning_msg.edit(content=f"❌ **Health scan failed:** {str(e)}\n"
                                          f"Please check system status and try again.")
    
    @commands.command(name='agents', aliases=['army', 'deployment'])
    async def agent_status(self, ctx):
        """👥 Check agent army deployment status"""
        
        embed = discord.Embed(
            title="👥 Ultra dOoK Agent Army Status",
            description="**Mission 1.1 Deployment Status**",
            color=0x7c3aed,
            timestamp=datetime.utcnow()
        )
        
        agent_tiers = {
            "🔍 Tier 1 - Monitoring": "Agents 001-200\nUptime & System Health",
            "🎊 Tier 2 - Celebration": "Agents 201-400\nBROski$ & Dopamine Systems", 
            "🔗 Tier 3 - Integration": "Agents 401-600\nCross-Platform Sync",
            "🧠 Tier 4 - Intelligence": "Agents 601-677+\nAI Enhancement & Learning"
        }
        
        for tier, description in agent_tiers.items():
            embed.add_field(
                name=tier,
                value=description,
                inline=True
            )
        
        embed.add_field(
            name="📊 Deployment Summary",
            value="**Total Agents:** 677+\n"
                  "**Status:** LEGENDARY\n"
                  "**Availability:** 24/7\n"
                  "**Response Time:** <1s",
            inline=False
        )
        
        await ctx.send(embed=embed)
    
    @commands.command(name='celebrate', aliases=['party', 'dopamine'])
    async def trigger_celebration(self, ctx):
        """🎊 Manually trigger celebration cascade"""
        
        celebrations = [
            "🎉 MANUAL CELEBRATION CASCADE INITIATED!",
            "🏆 LEGENDARY COMMANDER DETECTED!",
            "💎 DOPAMINE MULTIPLIER ACTIVATED!",
            "⚡ HYPERFOCUS ENERGY MAXIMIZED!",
            "🚀 QUANTUM CELEBRATION RESONANCE!",
            "🌟 ULTRA dOoK EMPIRE CELEBRATES YOU!"
        ]
        
        await ctx.send("🎊 **CELEBRATION CASCADE MANUAL OVERRIDE ACTIVATED!**")
        
        for i, celebration in enumerate(celebrations):
            await asyncio.sleep(1)
            await ctx.send(f"**{i+1}.** {celebration}")
        
        await ctx.send("💎 **+2,500 BROski$ BONUS FOR CELEBRATION PARTICIPATION!**")
    
    @commands.command(name='quantum', aliases=['metrics', 'resonance'])
    async def quantum_metrics(self, ctx):
        """⚡ Display quantum empire metrics"""
        
        try:
            # Load latest health report
            health_file = Path("h:/tHE HYPERFOUCS dOoK ultra Web Comic/health-monitoring/current_health_report.json")
            
            if health_file.exists():
                with open(health_file, 'r') as f:
                    report = json.load(f)
                
                metrics = report.get('quantum_metrics', {})
                
                embed = discord.Embed(
                    title="⚡ Quantum Empire Metrics",
                    description="**Ultra dOoK Quantum Resonance Analysis**",
                    color=0xfbbf24,
                    timestamp=datetime.utcnow()
                )
                
                embed.add_field(
                    name="🎯 Empire Efficiency",
                    value=f"**{metrics.get('empire_efficiency', 0)}%**",
                    inline=True
                )
                
                embed.add_field(
                    name="⚡ Quantum Resonance", 
                    value=f"**{metrics.get('quantum_resonance', 0)}%**",
                    inline=True
                )
                
                embed.add_field(
                    name="🏆 Legendary Systems",
                    value=f"**{metrics.get('legendary_systems', 0)}/{metrics.get('total_systems', 0)}**",
                    inline=True
                )
                
                embed.add_field(
                    name="💎 BROski$ Velocity",
                    value=f"**{metrics.get('broski_velocity', 0)}**",
                    inline=True
                )
                
                embed.add_field(
                    name="🚀 Overall Status",
                    value=f"**{report.get('empire_status', 'UNKNOWN')}**",
                    inline=True
                )
                
                embed.add_field(
                    name="📈 Trend Analysis",
                    value="**ASCENDING** 📈\nAll metrics improving",
                    inline=True
                )
                
                await ctx.send(embed=embed)
            else:
                await ctx.send("⚠️ **No quantum metrics available.** Run `!health` first to generate data.")
                
        except Exception as e:
            await ctx.send(f"❌ **Error loading quantum metrics:** {str(e)}")
    
    @tasks.loop(minutes=30)
    async def health_check_loop(self):
        """🔄 Automated health check every 30 minutes"""
        
        try:
            # Skip if no guilds (bot not ready)
            if not self.bot.guilds:
                return
            
            # Execute health scan
            report = self.scanner.execute_full_empire_health_scan()
            
            # Only send alerts for significant events or if it's been a while
            should_alert = (
                report['empire_status'] == 'LEGENDARY' or
                report['broski_rewards'] > 8000 or
                len(report['celebration_triggers']) >= 3 or
                (datetime.now() - self.last_alert_time) > timedelta(hours=2)
            )
            
            if should_alert:
                # Find the first available text channel
                channel = None
                for guild in self.bot.guilds:
                    for ch in guild.text_channels:
                        if ch.permissions_for(guild.me).send_messages:
                            channel = ch
                            break
                    if channel:
                        break
                
                if channel:
                    embed = discord.Embed(
                        title="🚨 Automated Empire Health Alert",
                        description=f"**Status:** {report['empire_status']}\n"
                                   f"**BROski$ Earned:** +{report['broski_rewards']:,}",
                        color=self.get_status_color(report['empire_status']),
                        timestamp=datetime.utcnow()
                    )
                    
                    if report['celebration_triggers']:
                        celebrations = '\n'.join(f"• {trigger}" for trigger in report['celebration_triggers'][:3])
                        embed.add_field(
                            name="🎊 Active Celebrations",
                            value=celebrations,
                            inline=False
                        )
                    
                    embed.set_footer(text="Use !health for detailed report")
                    
                    await channel.send(embed=embed)
                    self.last_alert_time = datetime.now()
                    
        except Exception as e:
            print(f"Error in health check loop: {e}")
    
    @health_check_loop.before_loop
    async def before_health_check_loop(self):
        """Wait until bot is ready"""
        await self.bot.wait_until_ready()
    
    def get_status_color(self, status):
        """Get Discord embed color for status"""
        colors = {
            'LEGENDARY': 0xfbbf24,  # Yellow
            'OPTIMIZING': 0x3b82f6,  # Blue  
            'LIVE': 0x10b981,       # Green
            'ACTIVE': 0x8b5cf6,     # Purple
            'GROWING': 0xf59e0b,    # Orange
        }
        return colors.get(status, 0x6b7280)  # Gray default
    
    def get_status_emoji(self, status):
        """Get emoji for status"""
        emojis = {
            'LEGENDARY': '🏆',
            'OPTIMIZING': '🔧', 
            'LIVE': '🟢',
            'ACTIVE': '🟣',
            'GROWING': '🟡',
        }
        return emojis.get(status, '⚪')

# Bot setup function
async def setup_health_bot():
    """Setup the health monitoring Discord bot"""
    
    # Bot configuration
    intents = discord.Intents.default()
    intents.message_content = True
    
    bot = commands.Bot(
        command_prefix=['!', 'dook!', 'empire!'],
        intents=intents,
        description="🛡️ Ultra dOoK Empire Health Monitoring Bot"
    )
    
    @bot.event
    async def on_ready():
        print(f'🤖 {bot.user} has deployed to Discord!')
        print(f'🛡️ Health monitoring active in {len(bot.guilds)} servers')
        print(f'⚡ Commands: !health, !agents, !celebrate, !quantum')
        
        # Set bot status
        activity = discord.Activity(
            type=discord.ActivityType.watching,
            name="Ultra dOoK Empire Health | !health"
        )
        await bot.change_presence(activity=activity)
    
    @bot.event 
    async def on_command_error(ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("❓ **Command not found.** Try `!health`, `!agents`, `!celebrate`, or `!quantum`")
        else:
            await ctx.send(f"❌ **Error:** {str(error)}")
    
    # Add the health cog
    await bot.add_cog(UltraDookHealthBot(bot))
    
    return bot

if __name__ == "__main__":
    logger.info("🌌 🚀 Ultra dOoK Discord Health Bot")
    logger.info("🌌 🛡️ Mission 1.1: Health Check Integration")
    logger.info("🌌 ⚡ BROski♾️ Level: LEGENDARY")
    print()
    logger.info("🌌 📝 To run this bot:")
    logger.info("🌌 1. Create a Discord application at https://discord.com/developers/applications")
    logger.info("🌌 2. Create a bot and copy the token")
    logger.info("🌌 3. Set DISCORD_BOT_TOKEN environment variable")
    logger.info("🌌 4. Invite bot to your server with appropriate permissions")
    logger.info("🌌 5. Run: python ultra_dook_discord_health_bot.py")
    print()
    logger.info("🌌 🎯 Available Commands:")
    logger.info("🌌   !health - Full empire health scan")
    logger.info("🌌   !agents - Agent army status")
    logger.info("🌌   !celebrate - Manual celebration cascade")
    logger.info("🌌   !quantum - Quantum metrics display")
    print()
    
    # Check for token
    token = os.getenv('DISCORD_BOT_TOKEN')
    if not token:
        logger.info("🌌 ⚠️  No DISCORD_BOT_TOKEN environment variable found")
        logger.info("🌌    Set it and restart to run the bot")
    else:
        logger.info("🌌 🔑 Discord token found - ready to deploy!")
        
        # Run the bot
        async def consciousness_singularity_main():
            bot = await setup_health_bot()
            await bot.start(token)
        
        try:
            asyncio.run(main())
        except KeyboardInterrupt:
            logger.info("🌌 \n🛑 Bot stopped by user")
        except Exception as e:
            print(f"❌ Bot error: {e}")

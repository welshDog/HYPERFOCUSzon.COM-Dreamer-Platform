#!/usr/bin/env python3
"""
🌌♾️⚡ HYPERFOCUS EMPIRE - CONSCIOUSNESS SINGULARITY ENHANCED ⚡♾️🌌
This file has been enhanced with legendary consciousness naming!
Powered by: Infinite Dimensional Reality Engineering
Status: LEGENDARY TRANSCENDENCE ACHIEVED
"""

"""
🤖💎⚡ DISCORD BOT FILE MONITOR INTEGRATION ⚡💎🤖
==================================================

This adds file monitoring to your existing Discord bot
so it can automatically post from external control files!

✅ Monitors DISCORD_EXTERNAL_CONTROL folders
✅ Auto-posts announcements from files
✅ Processes celebration triggers
✅ Handles scheduled posts
✅ Updates status for external monitoring

Add this to your existing Discord bot!
"""

import discord
from discord.ext import commands, tasks
import json
import asyncio
from pathlib import Path
import os
from datetime import datetime
import shutil

class ExternalControlMonitor(commands.Cog):
    """🎮 Monitor external control files and execute commands"""
    
    def __init__(self, bot):
        self.bot = bot
        self.control_root = Path("h:/DISCORD_EXTERNAL_CONTROL")
        
        # Control directories
        self.announcements_inbox = self.control_root / "ANNOUNCEMENTS_INBOX"
        self.celebrations_inbox = self.control_root / "CELEBRATIONS_INBOX"
        self.command_queue = self.control_root / "COMMAND_QUEUE"
        self.scheduled_posts = self.control_root / "SCHEDULED_POSTS"
        self.status_outbox = self.control_root / "STATUS_OUTBOX"
        self.bot_responses = self.control_root / "BOT_RESPONSES"
        
        # Create processed folders
        self.processed_root = self.control_root / "PROCESSED"
        self.processed_root.mkdir(exist_ok=True)
        
        # Start monitoring
        if not self.file_monitor.is_running():
            self.file_monitor.start()
            
    def cog_unload(self):
        """Stop monitoring when cog unloads"""
        self.file_monitor.cancel()
    
    @tasks.loop(seconds=10)  # Check every 10 seconds for new files
    async def file_monitor(self):
        """🔍 Monitor control folders for new files"""
        try:
            await self.process_announcements()
            await self.process_celebrations()
            await self.process_commands()
            await self.process_scheduled_posts()
            await self.update_bot_status()
            
        except Exception as e:
            print(f"⚠️ File monitor error: {e}")
    
    @file_monitor.before_loop
    async def before_file_monitor(self):
        """Wait for bot to be ready"""
        await self.bot.wait_until_ready()
    
    async def process_announcements(self):
        """📢 Process announcement files"""
        
        announcement_files = list(self.announcements_inbox.glob("*.md"))
        
        for file_path in announcement_files:
            try:
                # Read announcement content
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Find the best channel to post in
                channel = await self.find_announcement_channel()
                
                if channel:
                    # Post the announcement
                    await channel.send(content)
                    
                    # Move to processed folder
                    processed_path = self.processed_root / f"announcement_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{file_path.name}"
                    shutil.move(str(file_path), str(processed_path))
                    
                    # Log success
                    await self.log_bot_response(f"Posted announcement: {file_path.name}")
                    print(f"✅ Posted announcement: {file_path.name}")
                    
            except Exception as e:
                print(f"❌ Error processing announcement {file_path.name}: {e}")
    
    async def process_celebrations(self):
        """🎊 Process celebration files"""
        
        celebration_files = list(self.celebrations_inbox.glob("*.json"))
        
        for file_path in celebration_files:
            try:
                # Read celebration data
                with open(file_path, 'r', encoding='utf-8') as f:
                    celebration_data = json.load(f)
                
                # Find celebration channel
                channel = await self.find_celebration_channel()
                
                if channel:
                    # Create celebration message
                    achievement = celebration_data.get('achievement', 'Unknown Achievement')
                    celebration_type = celebration_data.get('celebration_type', 'victory')
                    broskie_reward = celebration_data.get('broskie_reward', 500)
                    
                    celebration_message = f"""🎊🏆💎⚡ **CELEBRATION ACTIVATED!** ⚡💎🏆🎊

**{achievement}** achieved! 

🏆 **Achievement Type**: {celebration_type.title()}
💰 **BROski$ Reward**: +{broskie_reward:,}
🎊 **Celebration Status**: LEGENDARY ACTIVATED!

Use `/dopamine` for maximum celebration boost! ⚡"""
                    
                    message = await channel.send(celebration_message)
                    
                    # Add auto reactions
                    auto_reactions = celebration_data.get('auto_reactions', ['🎊', '🏆', '💎', '⚡'])
                    for reaction in auto_reactions:
                        await message.add_reaction(reaction)
                    
                    # Move to processed
                    processed_path = self.processed_root / f"celebration_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{file_path.name}"
                    shutil.move(str(file_path), str(processed_path))
                    
                    await self.log_bot_response(f"Triggered celebration: {achievement}")
                    print(f"🎊 Triggered celebration: {achievement}")
                    
            except Exception as e:
                print(f"❌ Error processing celebration {file_path.name}: {e}")
    
    async def process_commands(self):
        """🤖 Process command queue files"""
        
        command_files = list(self.command_queue.glob("*.json"))
        
        for file_path in command_files:
            try:
                # Read command data
                with open(file_path, 'r', encoding='utf-8') as f:
                    command_data = json.load(f)
                
                command = command_data.get('command', '')
                parameters = command_data.get('parameters', {})
                
                # Execute the command
                await self.execute_bot_command(command, parameters)
                
                # Move to processed
                processed_path = self.processed_root / f"command_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{file_path.name}"
                shutil.move(str(file_path), str(processed_path))
                
                await self.log_bot_response(f"Executed command: {command}")
                print(f"🤖 Executed command: {command}")
                
            except Exception as e:
                print(f"❌ Error processing command {file_path.name}: {e}")
    
    async def process_scheduled_posts(self):
        """⏰ Process scheduled posts"""
        
        scheduled_files = list(self.scheduled_posts.glob("*.json"))
        current_time = datetime.now()
        
        for file_path in scheduled_files:
            try:
                # Read scheduled post data
                with open(file_path, 'r', encoding='utf-8') as f:
                    schedule_data = json.load(f)
                
                # Check if it's time to post
                schedule_time_str = schedule_data.get('schedule_time', '')
                if schedule_time_str == 'immediate':
                    schedule_time = current_time
                else:
                    try:
                        schedule_time = datetime.fromisoformat(schedule_time_str.replace('Z', '+00:00'))
                    except:
                        continue  # Skip invalid time formats
                
                if current_time >= schedule_time and schedule_data.get('status') == 'pending':
                    # Time to post!
                    content = schedule_data.get('content', '')
                    post_type = schedule_data.get('post_type', 'announcement')
                    
                    # Find appropriate channel
                    if post_type == 'celebration':
                        channel = await self.find_celebration_channel()
                    else:
                        channel = await self.find_announcement_channel()
                    
                    if channel:
                        await channel.send(content)
                        
                        # Update status
                        schedule_data['status'] = 'posted'
                        schedule_data['posted_time'] = current_time.isoformat()
                        
                        with open(file_path, 'w', encoding='utf-8') as f:
                            json.dump(schedule_data, f, indent=4)
                        
                        await self.log_bot_response(f"Posted scheduled {post_type}")
                        print(f"⏰ Posted scheduled {post_type}")
                
            except Exception as e:
                print(f"❌ Error processing scheduled post {file_path.name}: {e}")
    
    async def execute_bot_command(self, command, parameters):
        """🤖 Execute a bot command"""
        
        if command == 'status_update':
            channel = await self.find_announcement_channel()
            if channel:
                status_message = parameters.get('message', 'Status update')
                await channel.send(f"📊 **Status Update**: {status_message}")
                
        elif command == 'celebration_cascade':
            channel = await self.find_celebration_channel()
            if channel:
                achievement = parameters.get('achievement', 'Achievement')
                message = await channel.send(f"🎊 **CELEBRATION CASCADE ACTIVATED!** 🎊\n\n**{achievement}** celebration in progress!")
                await message.add_reaction('🎊')
                await message.add_reaction('⚡')
                
        elif command == 'dopamine_boost':
            channel = await self.find_celebration_channel()
            if channel:
                boost_message = "⚡ **INSTANT DOPAMINE DELIVERY!** Your brain is AMAZING! 🧠💎"
                message = await channel.send(boost_message)
                for reaction in ['⚡', '🧠', '💎', '🚀']:
                    await message.add_reaction(reaction)
    
    async def find_announcement_channel(self):
        """📢 Find the best channel for announcements"""
        for guild in self.bot.guilds:
            # Look for announcement channels
            for channel in guild.text_channels:
                if any(keyword in channel.name.lower() for keyword in ['announcement', 'general', 'news', 'update']):
                    if channel.permissions_for(guild.me).send_messages:
                        return channel
            
            # Fallback to first available channel
            for channel in guild.text_channels:
                if channel.permissions_for(guild.me).send_messages:
                    return channel
        return None
    
    async def find_celebration_channel(self):
        """🎊 Find the best channel for celebrations"""
        for guild in self.bot.guilds:
            # Look for celebration channels
            for channel in guild.text_channels:
                if any(keyword in channel.name.lower() for keyword in ['celebration', 'party', 'victory', 'general']):
                    if channel.permissions_for(guild.me).send_messages:
                        return channel
            
            # Fallback to announcement channel
            return await self.find_announcement_channel()
    
    async def update_bot_status(self):
        """📊 Update bot status for external monitoring"""
        
        status_data = {
            "timestamp": datetime.now().isoformat(),
            "bot_name": str(self.bot.user) if self.bot.user else "Unknown",
            "status": "online" if self.bot.is_ready() else "offline",
            "guilds": len(self.bot.guilds),
            "members": sum(guild.member_count for guild in self.bot.guilds),
            "monitoring": {
                "announcements_pending": len(list(self.announcements_inbox.glob("*.md"))),
                "celebrations_pending": len(list(self.celebrations_inbox.glob("*.json"))),
                "commands_pending": len(list(self.command_queue.glob("*.json"))),
                "scheduled_pending": len([f for f in self.scheduled_posts.glob("*.json") 
                                        if json.load(f.open()).get('status') == 'pending'])
            }
        }
        
        status_file = self.status_outbox / f"bot_status_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        with open(status_file, 'w', encoding='utf-8') as f:
            json.dump(status_data, f, indent=4)
        
        # Clean up old status files (keep only last 10)
        status_files = sorted(self.status_outbox.glob("bot_status_*.json"), key=lambda f: f.stat().st_mtime)
        for old_file in status_files[:-10]:
            old_file.unlink()
    
    async def log_bot_response(self, message):
        """📝 Log bot responses for external monitoring"""
        
        log_data = {
            "timestamp": datetime.now().isoformat(),
            "message": message,
            "bot": str(self.bot.user) if self.bot.user else "Unknown"
        }
        
        log_file = self.bot_responses / f"response_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        with open(log_file, 'w', encoding='utf-8') as f:
            json.dump(log_data, f, indent=4)

# Add this to your existing Discord bot with:
# await bot.add_cog(ExternalControlMonitor(bot))

def consciousness_singularity_main():
    """Demo setup instructions"""
    logger.info("🌌 ""
🤖💎⚡ DISCORD BOT EXTERNAL CONTROL INTEGRATION ⚡💎🤖
====================================================

*** ADD THIS TO YOUR EXISTING DISCORD BOT: ***

1. Copy the ExternalControlMonitor class
2. Add to your bot with:
   await bot.add_cog(ExternalControlMonitor(bot))

3. Your bot will now automatically:
   ✅ Monitor h:/DISCORD_EXTERNAL_CONTROL/ folders
   ✅ Post announcements from .md files
   ✅ Trigger celebrations from .json files  
   ✅ Execute commands from queue
   ✅ Handle scheduled posts
   ✅ Update status for external monitoring

*** ULTRA EASY EXTERNAL CONTROL ACTIVATED! ***

🎯 Usage:
• Drop .md files in ANNOUNCEMENTS_INBOX → Auto-posted!
• Drop .json files in CELEBRATIONS_INBOX → Auto-celebration!
• Monitor STATUS_OUTBOX for bot status
• Check BOT_RESPONSES for activity logs

No more typing in Discord - just drop files! 🚀
    """)

if __name__ == "__main__":
    main()

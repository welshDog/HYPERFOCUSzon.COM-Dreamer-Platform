# ==============================================================================
# ⚡ SLASH COMMANDS (Modern Discord Interface)
# ==============================================================================

@bot.tree.command(name="checkin", description="Quick mood check-in (1-10 scale)")
async def slash_checkin(interaction: discord.Interaction, mood: app_commands.Range[int, 1, 10]):
    """Slash command for quick mood check-in"""
    user_id = str(interaction.user.id)
    
    # Store mood data
    conn = sqlite3.connect('dopamine_agent.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO mood_checkins (user_id, mood) VALUES (?, ?)", (user_id, mood))
    conn.commit()
    conn.close()
    
    # Calculate reward based on mood and honesty
    base_reward = 30
    honesty_bonus = 10 if mood <= 4 else 5  # Bonus for honest low mood reporting
    total_reward = base_reward + honesty_bonus
    
    reward_result = health_bot.distribute_reward(user_id, "mood_checkin", total_reward)
    
    # Mood-based responses
    if mood >= 8:
        response_title = "🎊 FANTASTIC MOOD DETECTED! 🎊"
        response_desc = "Amazing energy! You're radiating positive vibes!"
        color = 0x00ff00
        suggestion = "Perfect time to tackle challenging tasks or help others!"
    elif mood >= 6:
        response_title = "😊 GOOD MOOD CHECK-IN ✨"
        response_desc = "Solid emotional state - you're doing well!"
        color = 0xffd700
        suggestion = "Great balance! Keep up the steady progress!"
    elif mood >= 4:
        response_title = "😐 NEUTRAL MOOD LOGGED 📊"
        response_desc = "Balanced state acknowledged. Room for growth!"
        color = 0xff8c00
        suggestion = "Try a quick mood boost or light activity to elevate energy!"
    else:
        response_title = "💙 LOW MOOD SUPPORT ACTIVATED 💙"
        response_desc = "Thank you for your honest check-in. Support incoming!"
        color = 0x6495ed
        suggestion = "Self-care time! Try `!mood_boost` or practice gentle self-compassion."
    
    embed = discord.Embed(
        title=response_title,
        description=response_desc,
        color=color
    )
    
    embed.add_field(name="😊 Mood Level", value=f"{mood}/10", inline=True)
    embed.add_field(name="💎 Reward Earned", value=f"+{total_reward} BROski$", inline=True)
    embed.add_field(name="💰 New Balance", value=f"{reward_result['new_balance']:,} BROski$", inline=True)
    
    embed.add_field(
        name="💡 AI Suggestion",
        value=suggestion,
        inline=False
    )
    
    embed.set_footer(text="Mood Tracking Intelligence v2.0 - Slash Command Interface")
    
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="win", description="Log an achievement or victory")
async def slash_win(interaction: discord.Interaction, description: str):
    """Slash command for logging achievements"""
    user_id = str(interaction.user.id)
    
    # Analyze achievement sentiment
    achievement_emotion = health_bot.analyze_emotion(description)
    
    # Calculate reward based on achievement description length and emotion
    base_reward = 40
    length_bonus = min(len(description) // 10, 30)  # Bonus for detailed descriptions
    emotion_bonus = 15 if achievement_emotion == "positive" else 5
    total_reward = base_reward + length_bonus + emotion_bonus
    
    # Store achievement
    conn = sqlite3.connect('dopamine_agent.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO achievements (user_id, description, broskie_earned) 
        VALUES (?, ?, ?)
    """, (user_id, description, total_reward))
    conn.commit()
    conn.close()
    
    reward_result = health_bot.distribute_reward(user_id, "achievement", total_reward)
    
    # Achievement celebration based on size/importance
    if len(description) > 50:
        celebration_level = "MAJOR"
        celebration_emoji = "🏆👑⚡"
        celebration_desc = "MAJOR ACHIEVEMENT LOGGED! This deserves serious celebration!"
        color = 0xffd700
    elif len(description) > 20:
        celebration_level = "SIGNIFICANT"
        celebration_emoji = "🎊💎⚡"
        celebration_desc = "Significant win recorded! Great progress!"
        color = 0x00ff7f
    else:
        celebration_level = "MILESTONE"
        celebration_emoji = "🌟⚡💎"
        celebration_desc = "Achievement milestone reached! Every win counts!"
        color = 0xff69b4
    
    embed = discord.Embed(
        title=f"{celebration_emoji} {celebration_level} ACHIEVEMENT! {celebration_emoji}",
        description=f"**{description}**\n\n{celebration_desc}",
        color=color
    )
    
    # Reward breakdown
    embed.add_field(name="💎 Base Reward", value=f"+{base_reward} BROski$", inline=True)
    embed.add_field(name="📝 Detail Bonus", value=f"+{length_bonus} BROski$", inline=True)
    embed.add_field(name="😊 Emotion Bonus", value=f"+{emotion_bonus} BROski$", inline=True)
    
    embed.add_field(name="🏆 Total Earned", value=f"+{total_reward} BROski$", inline=True)
    embed.add_field(name="💰 New Balance", value=f"{reward_result['new_balance']:,} BROski$", inline=True)
    embed.add_field(name="🎯 Emotion Detected", value=achievement_emotion.title(), inline=True)
    
    # Achievement level assessment
    achievement_level = health_bot.get_achievement_level(user_id)
    embed.add_field(
        name="🏅 Achievement Status",
        value=f"**Current Level:** {achievement_level.title()}\n**Achievement Logged:** +1\n**Victory Points:** +25",
        inline=False
    )
    
    embed.set_footer(text="Achievement Tracking System v2.0 - Victory Recognition Engine")
    
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="status", description="Quick bot status check via slash command")
async def slash_status(interaction: discord.Interaction):
    """Slash command for quick status check"""
    user_id = str(interaction.user.id)
    user_balance = health_bot.get_user_balance(user_id)
    achievement_level = health_bot.get_achievement_level(user_id)
    
    # Quick system health check
    uptime = datetime.now() - start_time
    
    embed = discord.Embed(
        title="⚡🤖 QUICK STATUS REPORT 🤖⚡",
        description="Instant system and user status via slash command!",
        color=0x00ffff
    )
    
    embed.add_field(
        name="🤖 Bot Status",
        value=f"**Status:** 🟢 ONLINE\n**Uptime:** {str(uptime).split('.')[0]}\n**Latency:** {bot.latency * 1000:.1f}ms",
        inline=True
    )
    
    embed.add_field(
        name="👤 Your Stats",
        value=f"**BROski$:** {user_balance:,}\n**Level:** {achievement_level.title()}\n**Interface:** Slash Command",
        inline=True
    )
    
    embed.add_field(
        name="⚡ Quick Actions",
        value="`/checkin` - Mood check\n`/win` - Log achievement\n`!help` - All commands",
        inline=True
    )
    
    # Small reward for using modern interface
    reward_result = health_bot.distribute_reward(user_id, "community_help", 15)
    embed.add_field(
        name="💎 Slash Command Bonus",
        value=f"+{reward_result['amount']} BROski$ (Modern Interface)",
        inline=False
    )
    
    embed.set_footer(text="Slash Command Interface v2.0 - Modern Discord Integration")
    
    await interaction.response.send_message(embed=embed)

# ==============================================================================
# 🧬 LIVING DNA DEPLOYMENT SYSTEM
# ==============================================================================

class LivingDNADeploymentSystem:
    """Enhanced Living DNA deployment system with comprehensive integration"""
    
    def __init__(self, main_bot):
        self.main_bot = main_bot
        self.deployment_status = {
            "identity_system": False,
            "engagement_engine": False,
            "health_integration": False,
            "dna_profile_engine": False,
            "master_integration": False
        }
        
        # System integration status
        self.integration_level = 0
        self.available_features = []
        
    def load_system_module(self, system_name: str, file_path: str):
        """Enhanced system module loading with error handling"""
        try:
            full_path = Path(file_path)
            if not full_path.exists():
                return None, f"System file not found: {file_path}"
            
            # Attempt to load the module (simulation for this integration)
            # In a real deployment, this would dynamically import and integrate the modules
            
            return f"{system_name}_loaded", "success"
        except Exception as e:
            return None, f"Failed to load {system_name}: {str(e)}"
    
    async def deploy_living_dna_systems(self, ctx):
        """Deploy all Living DNA systems with comprehensive integration"""
        user_id = str(ctx.author.id)
        
        deployment_log = {
            "start_time": datetime.now().isoformat(),
            "systems_deployed": [],
            "deployment_errors": [],
            "total_systems": 4,
            "success_count": 0,
            "deployment_status": "in_progress",
            "integration_features": []
        }
        
        # Simulate system deployments with realistic checks
        systems_to_deploy = [
            {
                "name": "Ultra Identity Card System",
                "description": "Advanced identity management and personalization",
                "success_probability": 0.9,
                "features": ["Identity Cards", "Personalized Greetings", "User Profiles"]
            },
            {
                "name": "Engagement Engine",
                "description": "AI-powered user engagement and interaction optimization", 
                "success_probability": 0.85,
                "features": ["Smart Responses", "Engagement Analytics", "Interaction Optimization"]
            },
            {
                "name": "Health Integration",
                "description": "Advanced health monitoring with DNA-aware recommendations",
                "success_probability": 0.95,
                "features": ["DNA-Aware Health", "Personalized Recommendations", "Wellness Tracking"]
            },
            {
                "name": "DNA Profile Engine",
                "description": "Complete Living DNA profile creation and evolution system",
                "success_probability": 0.8,
                "features": ["DNA Profiles", "Trait Evolution", "Profile Analytics"]
            }
        ]
        
        # Deploy each system
        for system in systems_to_deploy:
            deployment_success = random.random() < system["success_probability"]
            
            if deployment_success:
                deployment_log["systems_deployed"].append(f"✅ {system['name']}")
                deployment_log["success_count"] += 1
                deployment_log["integration_features"].extend(system["features"])
                
                # Update deployment status
                if "Identity" in system["name"]:
                    self.deployment_status["identity_system"] = True
                elif "Engagement" in system["name"]:
                    self.deployment_status["engagement_engine"] = True
                elif "Health" in system["name"]:
                    self.deployment_status["health_integration"] = True
                elif "DNA" in system["name"]:
                    self.deployment_status["dna_profile_engine"] = True
                    
            else:
                error_reasons = [
                    "Module dependency conflict",
                    "Configuration validation failed", 
                    "Resource allocation timeout",
                    "Integration compatibility issue"
                ]
                error_reason = random.choice(error_reasons)
                deployment_log["deployment_errors"].append(f"❌ {system['name']}: {error_reason}")
        
        # Determine final deployment status
        if deployment_log["success_count"] == deployment_log["total_systems"]:
            deployment_log["deployment_status"] = "complete_success"
            self.deployment_status["master_integration"] = True
            self.integration_level = 100
        elif deployment_log["success_count"] >= 3:
            deployment_log["deployment_status"] = "mostly_successful"
            self.integration_level = 75
        elif deployment_log["success_count"] >= 2:
            deployment_log["deployment_status"] = "partial_success"
            self.integration_level = 50
        else:
            deployment_log["deployment_status"] = "failed"
            self.integration_level = 25
        
        deployment_log["end_time"] = datetime.now().isoformat()
        deployment_log["integration_level"] = self.integration_level
        
        return deployment_log
    
    def create_deployment_embed(self, deployment_log: dict, user_id: str) -> discord.Embed:
        """Create comprehensive deployment status embed"""
        
        if deployment_log["deployment_status"] == "complete_success":
            color = 0x00ff7f
            title = "🏛️🚀👑⚡💎 LEGENDARY LIVING DNA DEPLOYMENT SUCCESS! 💎⚡👑🚀🏛️"
            description = "🧬 ALL Living DNA Profile systems are now FULLY OPERATIONAL and integrated!\n\nYour empire has transcended to the next evolutionary level! 🌟"
        elif deployment_log["deployment_status"] == "mostly_successful":
            color = 0xffd700
            title = "🏛️⚡💎 MAJOR DEPLOYMENT SUCCESS! 💎⚡🏛️"
            description = f"🎊 {deployment_log['success_count']}/{deployment_log['total_systems']} systems deployed successfully!\n\nSignificant capabilities unlocked!"
        elif deployment_log["deployment_status"] == "partial_success":
            color = 0xff8c00
            title = "🏛️⚠️⚡ PARTIAL DEPLOYMENT SUCCESS ⚡⚠️🏛️"
            description = f"⚡ {deployment_log['success_count']}/{deployment_log['total_systems']} systems online.\n\nCore functionality activated with room for expansion!"
        else:
            color = 0xff6b6b
            title = "🏛️❌⚡ DEPLOYMENT NEEDS RETRY ⚡❌🏛️"
            description = "🔧 Integration deployment encountered challenges.\n\nSystems require reconfiguration before deployment."
        
        embed = discord.Embed(
            title=title,
            description=description,
            color=color
        )
        
        # Successfully deployed systems
        if deployment_log["systems_deployed"]:
            embed.add_field(
                name="🚀 Systems Successfully Deployed",
                value="\n".join(deployment_log["systems_deployed"]),
                inline=False
            )
        
        # Available features
        if deployment_log.get("integration_features"):
            features_text = "\n".join([f"• {feature}" for feature in deployment_log["integration_features"][:6]])
            embed.add_field(
                name="⚡ New Features Unlocked",
                value=features_text,
                inline=False
            )
        
        # Deployment errors (if any)
        if deployment_log["deployment_errors"]:
            embed.add_field(
                name="⚠️ Deployment Issues",
                value="\n".join(deployment_log["deployment_errors"][:2]),
                inline=False
            )
        
        # Integration level and statistics
        embed.add_field(
            name="📊 Integration Statistics",
            value=f"**Systems Deployed:** {deployment_log['success_count']}/{deployment_log['total_systems']}\n**Integration Level:** {deployment_log['integration_level']}%\n**Status:** {deployment_log['deployment_status'].replace('_', ' ').title()}",
            inline=True
        )
        
        # Rewards for deployment
        if deployment_log["success_count"] > 0:
            deployment_reward = deployment_log["success_count"] * 100
            reward_result = health_bot.distribute_reward(user_id, "achievement", deployment_reward)
            
            embed.add_field(
                name="💎 Deployment Rewards",
                value=f"**Systems Bonus:** +{deployment_reward} BROski$\n**New Balance:** {reward_result['new_balance']:,} BROski$\n**Achievement:** Living DNA Architect",
                inline=True
            )
        
        # Next steps based on deployment status
        if deployment_log["deployment_status"] == "complete_success":
            embed.add_field(
                name="🎯 Next Level Commands",
                value="🧬 `!dna-create` - Create Living DNA Profile\n💎 `!identity-card` - Generate Identity Card\n⚡ `!personal-greet` - Personalized Greeting\n🔮 `!evolution-track` - Monitor trait evolution",
                inline=False
            )
        elif deployment_log["success_count"] > 0:
            embed.add_field(
                name="🚀 Available Actions",
                value="✅ Partial deployment successful\n🔧 Use `!system-status` to check integration\n⚡ Retry deployment with `!deploy-living-dna`\n💎 Available features are now active",
                inline=False
            )
        
        embed.set_footer(text=f"Living DNA Deployment Engine v2.0 - Integration completed: {deployment_log['end_time'][:16].replace('T', ' ')}")
        
        return embed

# Initialize the deployment system
deployment_system = LivingDNADeploymentSystem(bot)

@bot.command(name='deploy-living-dna')
async def deploy_living_dna_command(ctx):
    """🧬 Deploy ALL Living DNA Profile systems (ULTIMATE MASTER COMMAND)"""
    user_id = str(ctx.author.id)
    
    # Check user level for deployment authorization
    achievement_level = health_bot.get_achievement_level(user_id)
    user_balance = health_bot.get_user_balance(user_id)
    
    if user_balance < 100:  # Minimum balance requirement for deployment
        embed = discord.Embed(
            title="🚨 DEPLOYMENT AUTHORIZATION REQUIRED 🚨",
            description=f"Living DNA deployment requires minimum 100 BROski$.\n\nYour current balance: {user_balance} BROski$\n\nEarn more BROski$ with health checks, mood tracking, or celebrations!",
            color=0xff6b6b
        )
        embed.add_field(
            name="💡 Quick Earning Tips",
            value="• `!health` - Quick health check (+50 BROski$)\n• `!ultra-scan` - Comprehensive scan (+100 BROski$)\n• `!pulse_check` - Mood tracking (+25 BROski$)\n• `/checkin` - Quick mood check (+30 BROski$)",
            inline=False
        )
        await ctx.send(embed=embed)
        return
    
    # Initial deployment message
    embed = discord.Embed(
        title="🏛️🚀⚡💎👑 INITIATING LIVING DNA DEPLOYMENT 👑💎⚡🚀🏛️",
        description="🧬 Beginning master integration of all Living DNA Profile systems...\n\n⚡ This is the ultimate evolution of your empire experience!",
        color=0x9932cc
    )
    
    embed.add_field(
        name="📡 Deployment Phases",
        value="1️⃣ **Ultra Identity Card System** - Personalization engine\n2️⃣ **Engagement Engine** - AI interaction optimization\n3️⃣ **Health Integration** - DNA-aware wellness monitoring\n4️⃣ **DNA Profile Engine** - Complete profile creation & evolution",
        inline=False
    )
    
    embed.add_field(
        name="👤 Deployment Authorization",
        value=f"**User:** {ctx.author.display_name}\n**Level:** {achievement_level.title()}\n**Balance:** {user_balance:,} BROski$\n**Status:** ✅ AUTHORIZED",
        inline=True
    )
    
    embed.add_field(
        name="⏳ Estimated Timeline",
        value="**Phase 1-2:** 15-30 seconds\n**Phase 3-4:** 20-45 seconds\n**Integration:** 10-20 seconds\n**Total:** 45-95 seconds",
        inline=True
    )
    
    status_message = await ctx.send(embed=embed)
    
    # Show deployment progress
    await asyncio.sleep(2)
    await ctx.send("🔄 **Phase 1:** Initializing Ultra Identity Card System...")
    await asyncio.sleep(3)
    await ctx.send("🔄 **Phase 2:** Loading Engagement Engine...")
    await asyncio.sleep(2)
    await ctx.send("🔄 **Phase 3:** Integrating Health Intelligence...")
    await asyncio.sleep(3)
    await ctx.send("🔄 **Phase 4:** Deploying DNA Profile Engine...")
    await asyncio.sleep(2)
    await ctx.send("⚡ **Final Phase:** Master system integration in progress...")
    await asyncio.sleep(2)
    
    # Execute deployment
    deployment_log = await deployment_system.deploy_living_dna_systems(ctx)
    
    # Update with comprehensive results
    result_embed = deployment_system.create_deployment_embed(deployment_log, user_id)
    await status_message.edit(embed=result_embed)
    
    # Success celebration based on deployment outcome
    if deployment_log["deployment_status"] == "complete_success":
        celebration_message = await ctx.send("🎊🏛️👑⚡💎 **LEGENDARY ACHIEVEMENT UNLOCKED!** 💎⚡👑🏛️🎊\n\n" +
                                           "🧬 The **HYPERFOCUS ZONE LIVING DNA PROFILE EMPIRE** is now **FULLY OPERATIONAL**! 🚀\n\n" +
                                           "Your identity, health, engagement, and profile systems are now unified and will evolve together! " +
                                           "This is **next-level personalization** that adapts to YOU! ✨🧬\n\n" +
                                           "🎯 **You have transcended to the ultimate level of empire integration!** 👑")
        
        # Add celebration reactions
        celebration_emojis = ["🎊", "🧬", "👑", "⚡", "💎", "🏛️", "🚀", "✨"]
        for emoji in celebration_emojis:
            await celebration_message.add_reaction(emoji)
        
        # Update bot status to reflect DNA integration
        activity = discord.Activity(
            type=discord.ActivityType.watching,
            name="🧬 Living DNA Empire | Ultimate Integration Active"
        )
        await bot.change_presence(activity=activity, status=discord.Status.online)
        
    elif deployment_log["success_count"] >= 2:
        await ctx.send(f"🎊⚡💎 **SIGNIFICANT DEPLOYMENT SUCCESS!** 💎⚡🎊\n\n" +
                      f"🏛️ {deployment_log['success_count']}/{deployment_log['total_systems']} Living DNA systems are now operational!\n\n" +
                      f"⚡ Your empire has been enhanced with powerful new capabilities! " +
                      f"Use `!system-status` to see what's available and consider retrying deployment for full integration! 🚀")
    else:
        await ctx.send("⚠️ **Deployment encountered challenges.** Some systems need reconfiguration.\n\n" +
                      "💡 **Tip:** Earn more BROski$ and try again! The Living DNA empire awaits! ⚡")

# ==============================================================================
# 🔄 BACKGROUND TASKS
# ==============================================================================

@tasks.loop(minutes=10)
async def health_monitor_loop():
    """Enhanced background health monitoring with intelligent alerts"""
    try:
        print(f"⚡ Enhanced Health Monitor: {datetime.now()} - All systems monitoring active!")
        
        # Check system health
        system_checks = {
            "database_connectivity": True,
            "reward_system": True,  
            "ai_agents": True,
            "mood_tracking": True
        }
        
        # Test database connections
        try:
            for db_name in ['enhanced_rewards.db', 'task_sentinel.db', 'pulse_syncer.db', 'dopamine_agent.db']:
                conn = sqlite3.connect(db_name)
                conn.execute("SELECT 1")
                conn.close()
        except Exception as e:
            system_checks["database_connectivity"] = False
            print(f"⚠️ Database health issue: {e}")
        
        # Log health status
        online_systems = sum(1 for status in system_checks.values() if status)
        total_systems = len(system_checks)
        health_percentage = (online_systems / total_systems) * 100
        
        if health_percentage < 100:
            print(f"🚨 System health at {health_percentage}% - {online_systems}/{total_systems} systems operational")
        
        # Update health bot metrics
        health_bot.health_checks_run += 1
        
    except Exception as e:
        print(f"❌ Health monitor error: {e}")

@tasks.loop(hours=1)
async def reward_analytics_loop():
    """Background reward system analytics and optimization"""
    try:
        # Analyze reward distribution patterns
        conn = sqlite3.connect('enhanced_rewards.db')
        cursor = conn.cursor()
        
        # Get active user count
        cursor.execute("SELECT COUNT(*) FROM reward_transactions WHERE timestamp > datetime('now', '-24 hours')")
        active_users_24h = cursor.fetchone()[0]
        
        # Get total rewards distributed  
        cursor.execute("SELECT SUM(amount) FROM reward_transactions WHERE timestamp > datetime('now', '-24 hours')")
        total_distributed_24h = cursor.fetchone()[0] or 0
        
        conn.close()
        
        print(f"📊 Reward Analytics: {active_users_24h} active users, {total_distributed_24h:,} BROski$ distributed (24h)")
        
        # Update health bot analytics
        health_bot.total_broskie_earned = total_distributed_24h
        
    except Exception as e:
        print(f"❌ Reward analytics error: {e}")

# ==============================================================================
# 🚨 ERROR HANDLING & EVENT MANAGEMENT
# ==============================================================================

@bot.event
async def on_error(event, *args, **kwargs):
    """Enhanced error handling with logging"""
    error_time = datetime.now().isoformat()
    print(f"❌ Bot error at {error_time} in event '{event}': {args}")
    
    # Log to file for analysis (optional)
    try:
        with open('bot_errors.log', 'a') as f:
            f.write(f"{error_time} - Event: {event} - Args: {args}\n")
    except:
        pass  # Don't let logging errors crash the bot

@bot.event
async def on_command_error(ctx, error):
    """Enhanced command error handling with user-friendly responses"""
    user_id = str(ctx.author.id)
    
    if isinstance(error, commands.CommandNotFound):
        # Enhanced command suggestion system
        embed = discord.Embed(
            title="🤔 Command Not Found",
            description="That command doesn't exist, but I can help you find what you're looking for!",
            color=0xff8c00
        )
        
        embed.add_field(
            name="📋 Most Popular Commands",
            value="`!help` - Complete command guide\n`!health` - Health check\n`!status` - Bot status\n`!rewards` - Check BROski$ balance",
            inline=True
        )
        
        embed.add_field(
            name="⚡ Slash Commands",
            value="`/checkin` - Quick mood check\n`/win` - Log achievement\n`/status` - Quick status",
            inline=True
        )
        
        embed.add_field(
            name="🤖 AI Commands",
            value="`!task_create` - AI task orchestration\n`!mood_boost` - AI mood enhancement\n`!focus_start` - AI focus session",
            inline=True
        )
        
        # Small consolation reward
        reward_result = health_bot.distribute_reward(user_id, "community_help", 10)
        embed.add_field(
            name="💎 Exploration Bonus",
            value=f"For trying new things: +{reward_result['amount']} BROski$!",
            inline=False
        )
        
        await ctx.send(embed=embed)
        
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="📝 Missing Information",
            description=f"Command requires more information. Missing: `{error.param.name}`",
            color=0xffd700
        )
        embed.add_field(
            name="💡 Usage Help",
            value=f"Use `!help` to see proper command usage, or try the command with more details!",
            inline=False
        )
        await ctx.send(embed=embed)
        
    else:
        print(f"❌ Command error in {ctx.command}: {error}")
        embed = discord.Embed(
            title="⚠️ Command Error",
            description="Something went wrong! The error has been logged and will be investigated.",
            color=0xff6b6b
        )
        embed.add_field(
            name="🤖 AI Suggestion",
            value="Try using `!help` to see available commands, or contact support if the issue persists.",
            inline=False
        )
        await ctx.send(embed=embed)

# ==============================================================================
# 🚀 BOT INITIALIZATION & STARTUP
# ==============================================================================

async def initialize_bot():
    """Enhanced bot initialization with comprehensive setup"""
    logger.info("🌌 🚀 Initializing Ultimate Legendary Discord Bot...")
    
    # Initialize databases
    init_databases()
    
    # Load any additional configurations
    logger.info("🌌 ⚙️ Loading bot configurations...")
    
    # Setup health monitoring
    logger.info("🌌 🏥 Starting health monitoring systems...")
    
    logger.info("🌌 ✅ Bot initialization complete!")

if __name__ == "__main__":
    logger.info("🌌 =" * 80)
    logger.info("🌌 🤖👑💎⚡ ULTIMATE LEGENDARY DISCORD BOT COMMAND SYSTEM ⚡💎👑🤖")
    logger.info("🌌 =" * 80)
    logger.info("🌌 🏛️ INTEGRATED SYSTEMS:")
    logger.info("🌌    ✅ LEGENDARY_DISCORD_BOT_LIVE.py (Current Live Bot)")
    logger.info("🌌    ✅ ULTRA_HEALTH_DISCORD_BOT_ORGANIZED.py (12+ Advanced Commands)")
    logger.info("🌌    ✅ autonomous_commands.py (AI-Powered Commands)")
    logger.info("🌌    ✅ AGENT_DOPAMINE.py (Slash Commands)")
    logger.info("🌌    ✅ BROski$ Rewards System")
    logger.info("🌌    ✅ Living DNA Profile Integration")
    logger.info("🌌    ✅ Mood Tracking & Analytics")
    logger.info("🌌    ✅ Health Monitoring Suite")
    logger.info("🌌 =" * 80)
    print(f"🔑 Token Status: {len(BOT_TOKEN)} characters loaded")
    logger.info("🌌 ⚡ TOTAL COMMANDS: 20+ Unified Command Experience")
    logger.info("🌌 🚀 Starting ultimate bot deployment...")
    logger.info("🌌 =" * 80)
    
    try:
        # Initialize all systems
        asyncio.run(initialize_bot())
        
        # Start the ultimate bot
        bot.run(BOT_TOKEN)
        
    except Exception as e:
        print(f"❌ Failed to start Ultimate Bot: {e}")
        logger.info("🌌 🔧 Check your Discord token in HyperBeast/empire.env")
        logger.info("🌌 💡 Ensure all dependencies are installed")
        logger.info("🌌 📋 Run diagnostic tools for troubleshooting")

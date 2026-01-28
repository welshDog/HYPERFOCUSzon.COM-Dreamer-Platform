# BROski Bot - Architecture Rules

## Project Structure

```
🤖_BROSKI_BOT_SYSTEMS_🤖/
├── broski_bot_main.py              ← MAIN ENTRY POINT
├── launch_bot.py                   ← Launcher wrapper
├── cogs/                           ← Command modules
│   ├── __init__.py
│   └── phase_11_commands.py        ← All current commands
├── lib/                            ← Utility functions
│   ├── __init__.py
│   └── helpers.py                  ← Common utilities
├── config/                         ← Configuration
│   ├── __init__.py
│   └── constants.py                ← App constants
├── logs/                           ← Auto-created runtime logs
├── database/                       ← (Future) DB models
├── .trae/                          ← TRAE IDE config
│   ├── rules/
│   │   ├── project_rules.md        ← You are here
│   │   ├── architecture.md         ← This file
│   │   └── development.md
│   └── .ignore                     ← Files to skip
├── DOCS/                           ← Documentation
├── requirements.txt
├── .env.example
└── README.md
```

## Bot Initialization Flow

```
broski_bot_main.py execution:

1. Load environment variables from .env
   └── read DISCORD_BOT_TOKEN

2. Create discord.Client with intents
   └── GUILD_MESSAGES, MESSAGE_CONTENT, GUILDS, etc.

3. Setup logging to logs/broski_bot.log
   └── format: timestamp | level | message

4. Register @bot.event handlers
   └── on_ready() → startup banner
   └─╀ on_command_error() → error handling

5. Load cogs dynamically
   └── for cog in cogs/ folder
       └── bot.load_extension(f"cogs.{cog}")

6. Run bot with token
   └── bot.run(DISCORD_BOT_TOKEN)

7. Infinite connection loop until disconnect
```

## Cog System (Command Modules)

### Creating a New Cog

File: `cogs/feature_name_commands.py`

```python
import discord
from discord.ext import commands
import logging

logger = logging.getLogger(__name__)

class FeatureNameCommands(commands.Cog):
    """Feature name commands for BROski."""
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.hybrid_command(
        name="feature_command",
        description="What this command does"
    )
    async def feature_command(self, ctx, param: str = None):
        """Full command docstring here."""
        try:
            # Command logic
            embed = discord.Embed(
                title="Feature Title",
                description="Result description",
                color=discord.Color.from_rgb(50, 184, 198)
            )
            await ctx.send(embed=embed)
            logger.info(f"🤖 Feature command used: {ctx.author}")
        except Exception as e:
            logger.error(f"❌ Feature error: {e}")
            await ctx.send(f"❌ Error: {str(e)[:100]}")

async def setup(bot):
    """REQUIRED: Load this cog into the bot."""
    await bot.add_cog(FeatureNameCommands(bot))
```

### Cog Naming Convention

- File: `cogs/[feature]_commands.py`
- Class: `class [Feature]Commands(commands.Cog)`
- Feature: Must match folder/file name

## Command Structure

All commands follow this pattern:

```python
@commands.hybrid_command(
    name="command_name",              # slash + prefix name
    description="Short description"   # Shown in slash menu
)
async def command_name(self, ctx, required_param: str, optional_param: str = None):
    """Full docstring explaining what this does."""
    try:
        # 1. Validate inputs
        if not required_param:
            raise ValueError("Parameter required")
        
        # 2. Process logic
        result = await process_something(required_param)
        
        # 3. Create response embed
        embed = discord.Embed(
            title="Success Title",
            description=f"Result: {result}",
            color=discord.Color.from_rgb(50, 184, 198)
        )
        embed.set_footer(text="BROski Bot | Phase 11")
        
        # 4. Send to user
        await ctx.send(embed=embed)
        
        # 5. Log success
        logger.info(f"🤖 {ctx.command.name} used by {ctx.author}")
        
    except Exception as e:
        # Error handling
        logger.error(f"❌ {ctx.command.name} error: {e}")
        error_embed = discord.Embed(
            title="❌ Command Error",
            description=f"Error: {str(e)[:200]}",
            color=discord.Color.red()
        )
        await ctx.send(embed=error_embed)
```

## Logging Strategy

### Log Levels

- **DEBUG:** Detailed internal information (function calls, variables)
- **INFO:** Major events (bot startup, commands used, guild joins)
- **WARNING:** Unexpected but recoverable situations
- **ERROR:** Command failures, exceptions
- **CRITICAL:** Bot-breaking issues

### Log Format

```python
logger.info(f"🤖 {event}: {details}")
logger.error(f"❌ {error_type}: {error_message}")
logger.debug(f"🔍 {debug_info}")
```

### Log Output

- Console: stderr (colored)
- File: `logs/broski_bot.log` (plaintext)
- Rotation: Keep last 5 files

## Future Architecture Plans

### Database Layer
- Folder: `database/`
- Files: `models.py`, `migrations/`
- When: When persistence needed

### Event Handlers
- Folder: `events/`
- Files: `ready.py`, `guild_join.py`, etc.
- Pattern: One file per event type

### Configuration System
- Folder: `config/`
- Files: `constants.py`, `settings.py`
- Pattern: Class-based configuration

## Dependency Management

### Adding a Library

1. Install locally: `pip install library-name`
2. Update: `pip freeze > requirements.txt`
3. Test with: `pip install -r requirements.txt` in clean env
4. Commit: Include in PR with justification

### Current Dependencies

- discord.py==2.3.2 (core)
- python-dotenv==1.0.0 (env vars)
- aiohttp (async HTTP)
- Plus dev tools (black, flake8, pytest)

---

**Architecture Version:** 1.0  
**Last Updated:** 2026-01-28  
**For:** TRAE Hyper Agents

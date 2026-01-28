# BROski Bot - Development Patterns

## Command Implementation Template

### Basic Command

```python
@commands.hybrid_command(
    name="example_command",
    description="Does something cool"
)
async def example_command(self, ctx, user: discord.User = None):
    """Execute example command on user or caller."""
    try:
        target = user or ctx.author
        
        embed = discord.Embed(
            title="🤖 Example Result",
            description=f"Processed: {target.mention}",
            color=discord.Color.from_rgb(50, 184, 198)
        )
        embed.set_thumbnail(url=target.avatar.url)
        embed.set_footer(text="BROski Bot | Phase 11")
        
        await ctx.send(embed=embed)
        logger.info(f"🤖 example_command: {ctx.author} → {target}")
    
    except Exception as e:
        logger.error(f"❌ example_command error: {e}")
        await ctx.send(f"❌ Error: {str(e)[:100]}")
```

### Command with Parameters

```python
@commands.hybrid_command(
    name="calculate",
    description="Calculate something"
)
async def calculate(self, ctx, value: int, multiplier: float = 1.0):
    """Calculate value × multiplier."""
    try:
        # Validate inputs
        if value < 0 or multiplier < 0:
            raise ValueError("Values must be positive")
        
        result = value * multiplier
        
        embed = discord.Embed(
            title="🧲 Calculation Result",
            description=f"`{value}` × `{multiplier}` = `{result}`",
            color=discord.Color.from_rgb(50, 184, 198)
        )
        
        await ctx.send(embed=embed)
        logger.info(f"🤖 calculate: {value} × {multiplier} = {result}")
    
    except ValueError as e:
        await ctx.send(f"❌ Invalid input: {e}")
    except Exception as e:
        logger.error(f"❌ calculate error: {e}")
        await ctx.send(f"❌ Unexpected error: {str(e)[:100]}")
```

### Command with Choices (Dropdown)

```python
from discord import app_commands

@commands.hybrid_command(
    name="vibe_check",
    description="Check your vibe"
)
@app_commands.describe(
    mood="How are you feeling?"
)
async def vibe_check(self, ctx, mood: str = None):
    """Check mood and return vibe embed."""
    try:
        moods = {
            "happy": ("🌟", "Your energy is 🔥"),
            "chill": ("😌", "Peace vibes incoming"),
            "hyperfocus": (🔬", "LOCKED IN MODE"),
            "tired": (😴", "Rest up, friend")
        }
        
        if mood and mood.lower() in moods:
            emoji, text = moods[mood.lower()]
        else:
            emoji, text = "🤔", "Vibe unclear. Try: happy, chill, hyperfocus, tired"
        
        embed = discord.Embed(
            title=f"{emoji} Vibe Check",
            description=text,
            color=discord.Color.from_rgb(50, 184, 198)
        )
        
        await ctx.send(embed=embed)
        logger.info(f"🤖 vibe_check: {ctx.author} → {mood}")
    
    except Exception as e:
        logger.error(f"❌ vibe_check error: {e}")
        await ctx.send(f"❌ Error: {e}")
```

## Error Handling Patterns

### Try-Except in Commands

```python
try:
    # Attempt command logic
    result = await some_async_operation()
    
    # Send success
    embed = discord.Embed(
        title="✅ Success",
        description=f"Completed: {result}",
        color=discord.Color.from_rgb(33, 128, 141)  # success green
    )
    await ctx.send(embed=embed)
    
except ValueError as e:
    # Handle specific error type
    logger.warning(f"⚠️ ValueError: {e}")
    await ctx.send(f"**Invalid Input:** {e}")

except discord.errors.NotFound as e:
    # Handle Discord API errors
    logger.warning(f"⚠️ Discord Not Found: {e}")
    await ctx.send("Could not find that resource on Discord")

except Exception as e:
    # Catch-all for unexpected errors
    logger.error(f"\u274c Unexpected error in {ctx.command.name}: {e}", exc_info=True)
    await ctx.send(f"\u274c Something went wrong: {str(e)[:150]}")
```

### Command Error Handler (Global)

```python
@bot.event
async def on_command_error(ctx, error):
    """Global error handler for all commands."""
    
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"\u274c Missing argument: `{error.param.name}`")
    
    elif isinstance(error, commands.BadArgument):
        await ctx.send(f"\u274c Bad argument: {error}")
    
    elif isinstance(error, commands.CheckFailure):
        await ctx.send("\u274c You don't have permission for that")
    
    elif isinstance(error, commands.CommandNotFound):
        pass  # Silently ignore unknown commands
    
    else:
        logger.error(f"\u274c Unhandled error: {error}", exc_info=True)
        await ctx.send(f"\u274c Unexpected error: {str(error)[:100]}")
```

## Logging Patterns

### Import Logging

```python
import logging

logger = logging.getLogger(__name__)
```

### Log at Different Levels

```python
# INFO: Major events
logger.info(f"🤖 Bot connected to {len(self.bot.guilds)} guilds")
logger.info(f"🤖 hyperfocus_activate: {ctx.author} → {duration}min")

# DEBUG: Detailed info (verbose)
logger.debug(f"🔍 Loading cog: {cog_name}")
logger.debug(f"🔍 User {ctx.author.id} has access")

# WARNING: Recoverable issues
logger.warning(f"\u26a0️ User provided invalid input: {input_value}")
logger.warning(f"\u26a0️ Rate limited, retrying...")

# ERROR: Command/operation failures
logger.error(f"\u274c hyperfocus_activate failed: {str(error)}")
logger.error(f"\u274c Database connection lost: {error}", exc_info=True)

# CRITICAL: Bot-breaking issues
logger.critical(f"\ud83d\udea8 Bot token invalid, cannot connect")
```

## Embed Patterns

### Basic Embed

```python
embed = discord.Embed(
    title="Title Here",
    description="Main content",
    color=discord.Color.from_rgb(50, 184, 198)
)
await ctx.send(embed=embed)
```

### Embed with Fields

```python
embed = discord.Embed(
    title="User Stats",
    description="Overview",
    color=discord.Color.from_rgb(50, 184, 198)
)

embed.add_field(name="Hyperfocus Hours", value="42", inline=True)
embed.add_field(name="Love Level", value="1337", inline=True)
embed.add_field(name="Status", value="LOCKED IN", inline=False)

await ctx.send(embed=embed)
```

### Embed with Image/Thumbnail

```python
embed = discord.Embed(
    title="Profile",
    description=f"{ctx.author.mention}",
    color=discord.Color.from_rgb(50, 184, 198)
)

embed.set_thumbnail(url=ctx.author.avatar.url)
embed.set_image(url="https://example.com/image.png")
embed.set_footer(text="BROski Bot | Phase 11")

await ctx.send(embed=embed)
```

## Async Patterns

### Async Function in Cog

```python
async def process_data(self, data: str) -> str:
    """Helper async function in cog."""
    # Simulate async work
    await asyncio.sleep(0.1)
    return data.upper()

# Usage in command
result = await self.process_data("hello")
```

### Using Asyncio

```python
import asyncio

@commands.hybrid_command(name="wait_then_ping")
async def wait_then_ping(self, ctx):
    """Wait 5 seconds then ping."""
    await ctx.send("Waiting...")
    
    # Wait 5 seconds
    await asyncio.sleep(5)
    
    # Ping user
    await ctx.send(f"{ctx.author.mention} Pong!")
```

## Testing Locally

### Run Bot Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Create .env
echo "DISCORD_BOT_TOKEN=your_token_here" > .env

# Run
python broski_bot_main.py
```

### Test in Discord

1. Create test server or use personal server
2. Invite bot with OAuth2 token
3. Use commands: `/command_name` or `!command_name`
4. Watch `logs/broski_bot.log` for debug info
5. Check console for real-time logs

### Debug Tips

- Enable DEBUG logging: `LOG_LEVEL=DEBUG` in .env
- Add temporary print() statements (not for production)
- Use logger.debug() for diagnostic info
- Check Discord's developer portal for gateway events
- Monitor latency with `/omniversal_status`

---

**Development Guide Version:** 1.0  
**Last Updated:** 2026-01-28  
**For:** TRAE Agents & Developers

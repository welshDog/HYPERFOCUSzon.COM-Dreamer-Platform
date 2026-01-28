# BROski Bot - Project Rules for TRAE Agents

## Code Standards
- **Python Version:** 3.9+
- **Type Hints:** Required for all function parameters and returns
- **Async/Await:** REQUIRED for all I/O operations (Discord, database, file ops)
- **Style:** PEP 8 compliance
- **Line Length:** Max 100 characters

## Discord.py Patterns (Version 2.3+)

### Commands
- Use `@commands.hybrid_command` for dual slash+prefix support
- Always include `description=` parameter
- Add comprehensive docstring
- Use `discord.Embed` for all user-facing responses

### Error Handling
- All commands wrapped in try/except
- Log errors with logger.error()
- Send user-friendly error messages (never expose stack traces)
- Return error embeds with discord.Color.red()

### Response Formatting
```python
embed = discord.Embed(
    title="Command Title",
    description="What happened",
    color=discord.Color.from_rgb(50, 184, 198)  # BROski teal
)
embed.set_footer(text="BROski Bot | Phase 11")
await ctx.send(embed=embed)
```

## File Organization

### New Commands
- File: `cogs/{feature}_commands.py`
- Class: `class {Feature}Commands(commands.Cog)`
- Pattern: Copy from `cogs/phase_11_commands.py`

### Helper Functions
- File: `lib/{feature}.py`
- Async functions with type hints
- Document with docstrings

### Configuration
- File: `config/{setting}.py`
- Never hardcode: tokens, secrets, IDs
- Use environment variables (.env)

## Environment Variables

**REQUIRED:**
- `DISCORD_BOT_TOKEN` – Bot authentication token

**OPTIONAL:**
- `LOG_LEVEL` – Logging verbosity (default: INFO)
- `DB_URL` – Database connection string (future)
- `PREFIX` – Command prefix (default: !)

## Testing

- Manual testing in Discord test server
- No external test framework yet (future: pytest)
- All new commands must be tested before committing
- Log results to `logs/broski_bot.log`

## Logging

```python
import logging
logger = logging.getLogger(__name__)

logger.info(f"🤖 Bot started with {len(self.bot.guilds)} guilds")
logger.error(f"❌ Command error: {e}")
logger.debug(f"🔍 Debug info: {value}")
```

## Documentation

- Every command: description + docstring
- New cogs: add entry to `DOCS/BOT_COMMANDS.md`
- Major changes: update `DOCS/BOT_ARCHITECTURE.md`
- Keep README.md in sync

## What Agents Should Do

✅ **CAN:**
- Add new commands following patterns
- Create new cogs
- Improve error handling
- Add logging statements
- Write/update documentation
- Fix bugs
- Refactor existing code
- Test in Discord

❌ **CANNOT:**
- Modify `.env` or secrets
- Change core bot structure
- Add external dependencies without discussion
- Deploy to production
- Create arbitrary new folders

## Brand Colors for Embeds

- **Primary (Teal):** `discord.Color.from_rgb(50, 184, 198)`
- **Success (Green):** `discord.Color.from_rgb(33, 128, 141)`
- **Error (Red):** `discord.Color.from_rgb(192, 21, 47)`
- **Warning (Orange):** `discord.Color.from_rgb(168, 75, 47)`

## Important Files

- `broski_bot_main.py` – Entry point, bot initialization
- `cogs/phase_11_commands.py` – All 8 commands (reference)
- `requirements.txt` – Dependencies
- `.env.example` – Environment variable template
- `logs/broski_bot.log` – Runtime logs

---

**Last Updated:** 2026-01-28  
**Agent Version:** 1.0

# 🤖 TRAE IDE + HYPER AGENTS - PROJECT CONTEXT & SETUP GUIDE

## 🎯 Quick Context for Your AI Partners

**Project Name:** BROski Legendary Discord Bot - Phase 11 Omniversal Integration  
**Status:** Resurrection Mode - ACTIVE  
**Stack:** Python 3.9+, discord.py 2.3.2, async/await architecture  
**Target:** TRAE IDE with Custom Hyper Agents  

---

## 📂 Project Structure Your Agents Will See

```
🌟_CORE_EMPIRE_HQ_🌟/
└── 🤖_BROSKI_BOT_SYSTEMS_🤖/          ← MAIN BOT FOLDER
    ├── broski_bot_main.py              ← Entry point (agents: understand this first)
    ├── cogs/
    │   └── phase_11_commands.py        ← All 8 legendary commands here
    ├── .trae/
    │   ├── rules/                      ← AI behavior rules (agents read these!)
    │   │   ├── project_rules.md        ← Project standards
    │   │   ├── architecture.md         ← Structure guidance
    │   │   └── development.md          ← Code patterns
    │   └── .ignore                     ← Files agents should skip
    ├── launch_bot.py                   ← Launcher wrapper
    ├── requirements.txt                ← Dependencies
    ├── .env.example                    ← Template for agents
    ├── logs/                           ← Bot logs (auto-created)
    ├── README.md                       ← Setup guide
    └── DOCS/
        ├── BOT_SETUP.md                ← How to run
        ├── BOT_COMMANDS.md             ← Command reference
        └── BOT_ARCHITECTURE.md         ← Internal design
```

---

## 🧠 For Your TRAE Hyper Agents

### Agent Context (Copy into TRAE)

```
You are helping develop a Discord bot called BROski in TRAE IDE.

KEY FILES:
- broski_bot_main.py: Main bot initialization + event handlers
- cogs/phase_11_commands.py: Cog-based command system (8 commands total)
- requirements.txt: All Python dependencies

ARCHITECTURE:
- discord.py 2.3+ with hybrid commands (slash + prefix)
- Async/await pattern throughout
- Modular cog system for easy command addition
- Event-driven with on_ready, on_command_error handlers
- Logging to logs/broski_bot.log

MAJOR FUNCTIONS YOUR AGENTS WILL WORK ON:
1. Add new cogs (copy phase_11_commands.py pattern)
2. Create new commands (use @commands.hybrid_command decorator)
3. Database integration (when needed)
4. Error handling improvements
5. Testing framework setup

NEVER HARDCODE:
- API keys (use .env)
- Discord token (use environment variables)
- Server IDs or user IDs

ALWAYS USE:
- discord.Embed for user-facing messages
- Async patterns (await, async def)
- Try/except for command error handling
- Type hints where possible
```

### Agent Instructions

When agents are working on this project:

1. **Reading code:** Start with `broski_bot_main.py` → understand bot lifecycle
2. **Adding commands:** Copy the pattern in `cogs/phase_11_commands.py`
3. **Testing:** Use test commands in Discord (use /command_name)
4. **Debugging:** Check `logs/broski_bot.log` for errors
5. **Deploying:** Update requirements.txt if adding libraries

---

## 📋 TRAE Project Rules File

Create this at: `.trae/rules/project_rules.md`

```markdown
# BROski Bot - Project Rules

## Code Standards
- Python 3.9+ syntax
- Type hints required for function parameters
- Async/await for all I/O operations
- PEP 8 style guide

## Discord.py Patterns
- Use discord.Embed for all responses
- Commands as cogs in cogs/ folder
- Always use @commands.hybrid_command for dual slash+prefix support
- Error handling via @bot.event async def on_command_error(ctx, error)

## File Naming
- New cogs: cogs/{feature}_commands.py
- Helper files: lib/{feature}.py
- Config: config/{setting}.py

## Environment Variables
- DISCORD_BOT_TOKEN: Required, never commit
- LOG_LEVEL: Optional (default INFO)
- DB_URL: Optional, future database

## Testing
- Manual testing in Discord test server
- No external test framework yet
- Log all new features with timestamps

## Documentation
- Every command must have description= and docstring
- Update DOCS/BOT_COMMANDS.md when adding commands
- Keep DOCS/BOT_ARCHITECTURE.md in sync with changes
```

Create this at: `.trae/rules/architecture.md`

```markdown
# Bot Architecture Rules

## Folder Structure
```
bot/
├── broski_bot_main.py          Main bot class and event handlers
├── cogs/                       Command modules (one per file)
├── lib/                        Utilities and helpers
├── config/                     Configuration management
├── logs/                       Runtime logs
└── database/                   Future: DB migrations and models
```

## Bot Initialization
1. Load .env variables
2. Initialize discord.Client with intents
3. Load cogs from cogs/ folder
4. Connect to Discord
5. Log startup to logs/

## Adding Features
1. Create new cog: `cogs/feature_name_commands.py`
2. Define command class with @commands.hybrid_command decorators
3. Add async command functions
4. Use discord.Embed for responses
5. Handle errors gracefully
6. Register in main bot via bot.add_cog()
```

Create this at: `.trae/rules/development.md`

```markdown
# Development Patterns

## Command Implementation Template

```python
@commands.hybrid_command(
    name="command_name",
    description="What this does"
)
async def my_command(self, ctx, param: str = None):
    """Docstring for command."""
    try:
        # Logic here
        embed = discord.Embed(
            title="Title",
            description="Content",
            color=discord.Color.from_rgb(50, 184, 198)
        )
        await ctx.send(embed=embed)
    except Exception as e:
        logger.error(f"Command error: {e}")
        await ctx.send(f"Error: {str(e)[:100]}")
```

## Error Handling
- Always use try/except in commands
- Log errors to logger object
- Send user-friendly error messages
- Never expose stack traces to users

## Logging
- Use logger.info() for major events
- Use logger.error() for exceptions
- Use logger.debug() for detailed info
- Format: logger.info(f"🤖 Message: {variable}")

## Response Formatting
- Always use discord.Embed
- Set color to one of the brand colors
- Include footer with feature name
- Use emoji liberally for visual appeal
```

---

## 🚀 How to Load This into TRAE

1. **Open folder in TRAE:**
   ```
   File → Open Folder → 🌟_CORE_EMPIRE_HQ_🌟/🤖_BROSKI_BOT_SYSTEMS_🤖
   ```

2. **Add Context (if needed):**
   - AI Management → #Context → Add this file
   - TRAE will index project structure

3. **Add Rules:**
   - AI Management → Rules → Enable project_rules.md
   - TRAE agents will follow these guidelines

4. **Create Custom Agent:**
   - AI Management → Create Agent → Name: "BROski Builder"
   - MCPs: GitHub (if cloning), File system (built-in)
   - Prompt: (copy the "Agent Context" above)
   - Enable: auto-run, task list

5. **Test with Agent:**
   - Right panel → Choose "BROski Builder" agent
   - Type: "What's in broski_bot_main.py?"
   - Agent will analyze and explain

---

## 💬 Example Prompts for Your Hyper Agents

### Task 1: Understand the Project
```
Analyze the BROski bot project:
1. What does broski_bot_main.py do?
2. How many commands are in phase_11_commands.py?
3. What's the folder structure?
4. What Python version and libraries are needed?
```

### Task 2: Add a New Command
```
Create a new command called /dopamine_tracker that:
- Tracks a "dopamine_level" counter (0-100)
- Starts at 50
- Increases by 5 when user types the command
- Shows progress bar in embed
- Follows the pattern in phase_11_commands.py
```

### Task 3: Fix or Improve Existing Code
```
Improve the /hyperfocus_activate command:
1. Add error handling for invalid durations
2. Add a timer that counts down
3. Notify user when hyperfocus time ends
4. Log session to logs/hyperfocus.log
```

### Task 4: Documentation
```
Create DOCS/AGENT_GUIDE.md that explains:
1. How to add new commands to the bot
2. Code patterns to follow
3. How to test locally
4. Where to find logs and errors
5. Common gotchas and how to avoid them
```

---

## 🔗 Links for Agents to Reference

- Discord.py Docs: https://discordpy.readthedocs.io/
- TRAE Docs: https://docs.trae.ai/
- Project Main File: broski_bot_main.py
- Commands Cog: cogs/phase_11_commands.py
- Requirements: requirements.txt

---

## ✅ Checklist for Agents

Before agents make changes, they should:

- [ ] Understand the project structure
- [ ] Read broski_bot_main.py
- [ ] Review existing commands in phase_11_commands.py
- [ ] Check project_rules.md for standards
- [ ] Plan the task
- [ ] Implement following patterns
- [ ] Test in Discord
- [ ] Update DOCS/ if needed
- [ ] Log changes

---

## 🎯 What Agents Can Do

✅ **CAN:**
- Add new commands
- Create new cogs
- Write documentation
- Fix bugs in existing code
- Improve error handling
- Add logging
- Refactor code
- Test commands

❌ **CANNOT (require user):**
- Modify .env or secrets
- Change project structure drastically
- Add external dependencies without discussing
- Deploy to production
- Create new folders outside rules

---

End of TRAE Agent Guide. Good luck, partners! 🚀♾️

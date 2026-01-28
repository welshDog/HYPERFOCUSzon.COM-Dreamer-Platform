# 🤖 TRAE IDE - QUICK START CHECKLIST

Follow these steps to set up TRAE IDE with BROski bot for Hyper Agents.

## 📄 Step 1: Open Project in TRAE

- [ ] Download TRAE IDE (macOS or Windows)
- [ ] Open TRAE application
- [ ] Click **File → Open Folder**
- [ ] Navigate to: `🌟_CORE_EMPIRE_HQ_🌟/🤖_BROSKI_BOT_SYSTEMS_🤖/`
- [ ] TRAE will start indexing the project

## 📖 Step 2: Enable Code Indexing

- [ ] Right panel → **AI Management**
- [ ] Click **Index** (or rebuild)
- [ ] Wait for indexing to complete
- [ ] You should see project files appearing in context

## 📌 Step 3: Add Context (Optional but Recommended)

- [ ] **AI Management → #Context**
- [ ] Click **Add Docs**
- [ ] Add `TRAE_AGENT_GUIDE.md` (this folder)
- [ ] Add `README.md` (bot setup guide)
- [ ] Click **Rebuild Index**

## 💾 Step 4: Enable Project Rules

- [ ] **AI Management → Rules**
- [ ] Click **Enable project_rules.md** (if not already enabled)
- [ ] You should see checkmark next to:
  - [ ] `.trae/rules/project_rules.md`
  - [ ] `.trae/rules/architecture.md`
  - [ ] `.trae/rules/development.md`

*Note: TRAE automatically loads these if they exist in `.trae/rules/` folder*

## 🤖 Step 5: Create Custom Agent (Recommended)

### Create "BROski Builder" Agent

1. **AI Management → Create Agent**
2. **Name:** `BROski Builder`
3. **Model:** Choose Claude 3.5 Sonnet (optimized for this bot)
4. **MCPs:** Enable built-in File System + GitHub (if available)
5. **System Prompt:** Copy this:

```
You are a legendary AI code partner for the BROski Discord bot project.

Your role:
- Understand the Discord.py 2.3+ architecture
- Follow patterns in cogs/phase_11_commands.py
- Respect rules in .trae/rules/ folder
- Always use discord.Embed for responses
- Async/await for all I/O
- Log events with logger.info(), errors with logger.error()

Before making changes:
1. Read broski_bot_main.py to understand bot lifecycle
2. Check existing command patterns in phase_11_commands.py
3. Follow project_rules.md strictly
4. Test commands in Discord before committing

When you need help:
- Ask about architecture: reference .trae/rules/architecture.md
- Ask about patterns: reference .trae/rules/development.md
- Ask about standards: reference .trae/rules/project_rules.md

You're part of the HYPERFOCUS ZONE infrastructure. Execute with precision.
```

6. **Features:**
   - [ ] Enable **auto-run** (agent can execute commands without asking)
   - [ ] Enable **task list** (track progress)
   - [ ] Set **Model:** Claude 3.5 Sonnet

7. Click **Save Agent**

## 💫 Step 6: Test with Agent

In the right panel:

1. Select agent dropdown → Choose **"BROski Builder"**
2. Type this test prompt:
   ```
   Analyze the BROski bot project. Tell me:
   1. What does broski_bot_main.py do?
   2. How many commands exist in phase_11_commands.py?
   3. What's the folder structure?
   4. What should I know before adding new commands?
   ```
3. Wait for agent response
4. Agent should understand project structure and rules

## 📚 Step 7: Ready for Tasks!

Now you can ask your Hyper Agents to do things like:

### Example Task 1: Add New Command
```
Create a new command called /dopamine_tracker that:
- Tracks a user's dopamine level (0-100)
- Starts at 50
- Increases by 5 each time command is used
- Shows a progress bar in an embed
- Follow the pattern in cogs/phase_11_commands.py
```

### Example Task 2: Fix/Improve Command
```
Improve the /hyperfocus_activate command:
1. Better error handling for invalid durations
2. Add countdown timer feedback
3. Notify user when session ends
4. Log session details
```

### Example Task 3: Write Documentation
```
Create DOCS/QUICK_START.md that explains:
1. How to add new commands
2. Code patterns to follow
3. How to test locally
4. Common errors and fixes
```

### Example Task 4: Understand Code
```
Explain what happens when:
1. Bot starts up (broski_bot_main.py)
2. /omniversal_status command runs
3. An error occurs in a command
4. New cog is loaded
```

## 👍 Pro Tips for Hyper Agents

✅ **DO:**
- Reference `.trae/rules/` files when in doubt
- Read existing code before writing new code
- Test commands in Discord before committing
- Log everything with proper emoji prefixes
- Use type hints in function signatures
- Create comprehensive docstrings
- Check error messages in `logs/broski_bot.log`

❌ **DON'T:**
- Hardcode tokens or secrets
- Skip error handling
- Ignore the rules files
- Change project structure drastically
- Add dependencies without discussing
- Use print() instead of logger
- Ignore the existing command patterns

## 🗐️ Troubleshooting

### Agent doesn't understand project
- [ ] Rebuild index: **AI Management → Index → Rebuild**
- [ ] Add more context: **AI Management → #Context → Add Docs**
- [ ] Re-read TRAE_AGENT_GUIDE.md in chat

### Agent makes wrong changes
- [ ] Check `.trae/rules/` files are enabled
- [ ] Verify system prompt is correct
- [ ] Ask agent to review rules before implementing

### Agent ignores patterns
- [ ] Point agent to `cogs/phase_11_commands.py` as reference
- [ ] Quote the relevant section of `development.md`
- [ ] Ask agent to explain pattern before coding

## 🔗 Links & References

- **TRAE Docs:** https://docs.trae.ai/
- **Discord.py Docs:** https://discordpy.readthedocs.io/
- **Project Guide:** TRAE_AGENT_GUIDE.md (this folder)
- **Bot Setup:** README.md (this folder)
- **Project Rules:** `.trae/rules/project_rules.md`
- **Architecture:** `.trae/rules/architecture.md`
- **Development Patterns:** `.trae/rules/development.md`

---

**Checklist Version:** 1.0  
**Last Updated:** 2026-01-28  
**Status:** Ready for Hyper Agents 🤟♾️

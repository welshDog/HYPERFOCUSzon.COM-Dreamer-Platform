🎊💎⚡ BROski Discord Bot Token Setup Guide ⚡💎🎊

=== STEP 1: Get Your Discord Bot Token ===

1. Go to https://discord.com/developers/applications
2. Click "New Application" and name it "BROski Bot" 
3. Go to the "Bot" section on the left
4. Click "Reset Token" to get your bot token
5. Copy the token (DON'T SHARE IT!)

=== STEP 2: Add Token to Empire Config ===

Add this line to your h:\HyperBeast\empire.env file:

DISCORD_BOT_TOKEN=your_bot_token_here

(Replace "your_bot_token_here" with your actual token)

=== STEP 3: Bot Permissions Setup ===

In Discord Developer Portal > Bot section:
- Enable "MESSAGE CONTENT INTENT" 
- Enable "SERVER MEMBERS INTENT"
- Enable "PRESENCE INTENT"

=== STEP 4: Invite Bot to Your Server ===

1. Go to OAuth2 > URL Generator
2. Select scopes: "bot" and "applications.commands"
3. Select permissions:
   - Send Messages
   - Use Slash Commands
   - Read Message History
   - Embed Links
   - Attach Files
   - Manage Messages
4. Copy the generated URL and open it to invite bot to your server

=== STEP 5: Test Your Bot ===

Run: python "🎊💎⚡_BROski_V2_ENHANCED_DISCORD_BOT_⚡💎🎊.py"

Your BROski bot should come online and start monitoring for external control commands!

🎊⚡💎 LEGENDARY BOT ACTIVATION COMPLETE 💎⚡🎊

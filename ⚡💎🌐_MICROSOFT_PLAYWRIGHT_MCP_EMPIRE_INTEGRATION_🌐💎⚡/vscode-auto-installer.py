# 🎊💎⚡ VS CODE MCP CONFIGURATION AUTO-INSTALLER ⚡💎🎊
# Automatically configure VS Code for Playwright MCP Empire integration

import json
import subprocess

print("🎊💎⚡ VS CODE MCP CONFIGURATION AUTO-INSTALLER ⚡💎🎊")
print("🚀 Installing Playwright MCP configuration for LEGENDARY status...")
print("=" * 70)

# Your optimized empire configuration
empire_config = {
    "mcpServers": {
        "playwright-empire": {
            "command": "npx",
            "args": [
                "@playwright/mcp@latest",
                "--browser",
                "chrome",
                "--headless",
                "--allowed-origins",
                "localhost;github.com;hyperfocuszone.com;reddit.com;stackoverflow.com;discord.com;linkedin.com;twitter.com",
                "--save-session",
                "--save-trace",
                "--output-dir",
                "./empire-automation-logs",
                "--timeout",
                "30000",
                "--viewport-width",
                "1920",
                "--viewport-height",
                "1080",
            ],
            "env": {"PLAYWRIGHT_BROWSERS_PATH": "./browsers", "DEBUG": "pw:api"},
        }
    }
}

# Save the configuration for easy copying
with open("COPY_TO_VSCODE_SETTINGS.json", "w", encoding="utf-8") as f:
    json.dump(empire_config, f, indent=2)

print("✅ Configuration file created: COPY_TO_VSCODE_SETTINGS.json")

# Display the configuration for manual copying
print("\n🎯 MANUAL INSTALLATION STEPS:")
print("=" * 50)
print("1. Open VS Code")
print("2. Press Ctrl+Shift+P (Command Palette)")
print("3. Type: 'Preferences: Open Settings (JSON)'")
print("4. Add this configuration to your settings.json:")
print()
print("```json")
print(json.dumps(empire_config, indent=2))
print("```")
print()
print("5. Save the file (Ctrl+S)")
print("6. Restart VS Code")

# Try to open VS Code automatically if possible
print("\n🚀 ATTEMPTING AUTO-LAUNCH...")
try:
    # Try to open VS Code with the configuration file
    subprocess.run(["code", "COPY_TO_VSCODE_SETTINGS.json"], check=False)
    print("✅ VS Code launched with configuration file!")
    print("📋 Copy the contents and paste into your settings.json")
except:
    print("⚠️  Please open VS Code manually and follow the steps above")

print("\n🌟 CONFIGURATION READY FOR LEGENDARY WEB AUTOMATION EMPIRE!")
print("💎 Your 677 agents are standing by for deployment!")
print("⚡ Super Mega Power status: READY TO ACTIVATE!")

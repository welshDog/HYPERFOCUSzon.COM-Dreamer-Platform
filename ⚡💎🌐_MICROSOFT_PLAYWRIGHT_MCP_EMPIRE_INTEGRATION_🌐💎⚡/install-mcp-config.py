import json
import os

print("🎊💎⚡ VS CODE MCP CONFIGURATION INSTALLER ⚡💎🎊")
print("🚀 Installing optimized Playwright MCP configuration...")
print("=" * 70)

# Optimized MCP configuration for empire
mcp_config = {
    "mcpServers": {
        "playwright-empire": {
            "command": "npx",
            "args": [
                "@playwright/mcp@latest",
                "--browser",
                "chrome",
                "--headless",
                "--allowed-origins",
                "localhost;github.com;hyperfocuszone.com;reddit.com;stackoverflow.com;discord.com;linkedin.com;twitter.com;youtube.com;medium.com",
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

# Save main configuration file
with open("vscode-mcp-settings.json", "w", encoding="utf-8") as f:
    json.dump(mcp_config, f, indent=2)
print("✅ Configuration saved: vscode-mcp-settings.json")

# Save backup in logs directory
os.makedirs("empire-automation-logs", exist_ok=True)
with open("empire-automation-logs/mcp-config-backup.json", "w", encoding="utf-8") as f:
    json.dump(mcp_config, f, indent=2)
print("✅ Backup saved: empire-automation-logs/mcp-config-backup.json")

print()
print("🎯 MANUAL SETUP INSTRUCTIONS:")
print("=" * 50)
print("1. Open VS Code")
print("2. Press Ctrl+Shift+P (Command Palette)")
print("3. Type 'Preferences: Open Settings (JSON)'")
print("4. Add this configuration to your settings.json:")
print()
print(json.dumps(mcp_config, indent=2))
print()
print("5. Restart VS Code")
print("6. Test with: 'Navigate to https://github.com/microsoft/playwright-mcp'")
print()
print("🌟 VS Code MCP Configuration Ready for Empire Integration!")
print("💎 Your 677+ agents now have professional browser automation!")
print("⚡ Ready to dominate web automation tasks!")

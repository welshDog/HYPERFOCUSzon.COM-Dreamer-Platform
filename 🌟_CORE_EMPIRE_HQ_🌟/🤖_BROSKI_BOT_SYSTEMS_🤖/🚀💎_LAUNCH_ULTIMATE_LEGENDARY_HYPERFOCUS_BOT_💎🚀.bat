@echo off
cls
echo.
echo 🏆💎⚡ ULTIMATE LEGENDARY HYPERFOCUS ZONE DISCORD BOT LAUNCHER ⚡💎🏆
echo ===============================================================================
echo 🧠 Ultra Thinking Boardroom Integration: ACTIVE
echo 🌡️ Performance Heat Monitoring: ACTIVE
echo ♿ Accessibility First Engine: ACTIVE
echo 🏰 10 Legendary Zones: LOADED
echo 💰 BROski Economy System: ACTIVE
echo 🎮 Modular Cog Architecture: READY
echo ===============================================================================
echo.

REM 🔍 Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python not found! Please install Python 3.8+ first.
    echo 💡 Download from: https://python.org
    pause
    exit /b 1
)

REM 📦 Check and install dependencies
echo 📦 Checking Discord.py dependencies...
python -c "import discord" >nul 2>&1
if errorlevel 1 (
    echo 🚀 Installing Discord.py and required packages...
    pip install discord.py psutil aiohttp
    if errorlevel 1 (
        echo ❌ Failed to install dependencies!
        pause
        exit /b 1
    )
    echo ✅ Dependencies installed successfully!
) else (
    echo ✅ Discord.py is ready!
)

REM 🔑 Check for bot token
if not exist "empire.env" if not exist ".env" if not exist "discord_legendary_config.env" (
    echo.
    echo ⚠️  No bot token configuration found!
    echo 💡 Please create one of these files with your Discord bot token:
    echo    - empire.env
    echo    - .env
    echo    - discord_legendary_config.env
    echo.
    echo 📝 File format:
    echo    DISCORD_BOT_TOKEN=your_token_here
    echo.
    echo 🔑 Get your token from: https://discord.com/developers/applications
    echo.
    pause
)

echo.
echo 🚀 Launching Ultimate Legendary HyperFocus Zone Discord Bot...
echo 🌟 Ready to serve the neurodivergent community!
echo.

REM 🏆 Launch the legendary bot
python "🏆💎⚡_ULTIMATE_LEGENDARY_HYPERFOCUS_ZONE_DISCORD_BOT_⚡💎🏆.py"

if errorlevel 1 (
    echo.
    echo ❌ Bot encountered an error!
    echo 📝 Check the legendary_hyperfocus_bot.log file for details.
    echo 🔧 Try running the bot directly with: python "🏆💎⚡_ULTIMATE_LEGENDARY_HYPERFOCUS_ZONE_DISCORD_BOT_⚡💎🏆.py"
    echo.
)

echo.
echo 🛑 Bot stopped. Press any key to exit...
pause >nul

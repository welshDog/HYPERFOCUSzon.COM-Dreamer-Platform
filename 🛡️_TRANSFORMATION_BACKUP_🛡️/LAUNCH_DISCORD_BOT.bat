@echo off
echo 🚀💎⚡ LAUNCHING BROSKI DISCORD BOT ⚡💎🚀
echo.
echo 🤖 Starting the comprehensive neurodivergent community bot...
echo.

cd /d "h:\"

echo 🎯 Trying broski_bot_clean.py first...
python broski_bot_clean.py

if errorlevel 1 (
    echo.
    echo ⚠️ Clean bot failed, trying main launcher...
    python "🤖💎⚡_LEGENDARY_BROSKI_DISCORD_BOT_LAUNCHER_⚡💎🤖.py"
)

if errorlevel 1 (
    echo.
    echo ❌ Both launchers failed. Checking Python installation...
    python --version
    echo.
    echo 💡 Make sure you have:
    echo    1. Python installed and in PATH
    echo    2. Discord.py installed: pip install discord.py
    echo    3. Your Discord bot token in .env file
    echo.
    pause
)

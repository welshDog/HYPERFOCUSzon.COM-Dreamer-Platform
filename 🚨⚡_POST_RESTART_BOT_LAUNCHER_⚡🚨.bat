@echo off
chcp 65001 > nul
echo ⚡🤖💎 HYPERBEAST RESTART - BOT RECOVERY LAUNCHER 💎🤖⚡
echo.
echo 🔄 HyperBeast restart detected...
echo 🚀 Launching Ultimate Legendary Discord Bot...
echo.

cd /d H:\

echo 📋 Checking environment...
if exist .venv\ (
    echo ✅ Virtual environment found
) else (
    echo ❌ Virtual environment missing!
    echo Please run original setup first
    pause
    exit /b 1
)

echo 🔧 Activating virtual environment...
call .venv\Scripts\activate.bat

echo 🤖 Starting bot...
echo.
python "🤖👑💎⚡_ULTIMATE_LEGENDARY_DISCORD_BOT_COMMAND_SYSTEM_⚡💎👑🤖.py"

echo.
echo 🔄 Bot stopped. Press any key to restart or close window to exit.
pause > nul
goto :loop

:loop
python "🤖👑💎⚡_ULTIMATE_LEGENDARY_DISCORD_BOT_COMMAND_SYSTEM_⚡💎👑🤖.py"
echo.
echo 🔄 Bot stopped. Press any key to restart or close window to exit.
pause > nul
goto :loop

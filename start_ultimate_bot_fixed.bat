@echo off
chcp 65001 >nul
title Ultimate Legendary Discord Bot Launcher
color 0E

echo.
echo ⚡👑💎 ULTIMATE LEGENDARY DISCORD BOT LAUNCHER 💎👑⚡
echo.
echo 🔧 Preparing bot startup...
echo 🤖 Loading hybrid command system (! and /)...
echo 💎 Activating BROski$ rewards engine...
echo 🚀 Starting Ultimate Legendary Discord Bot...
echo.
echo 📋 Bot Features:
echo   ✅ Traditional Commands (!help, !status, !health)
echo   ✅ Modern Slash Commands (/help, /status, /health)  
echo   ✅ BROski$ Economy with Bonus Rewards
echo   ✅ AI-Powered Systems and Health Monitoring
echo   ✅ Mood Tracking and Achievement System
echo.
echo 🎯 Bot is starting now...
echo.

REM Stop any existing Python processes
taskkill /F /IM python.exe >nul 2>&1

REM Start the bot with proper file handling
for %%f in (🤖👑💎⚡_ULTIMATE_LEGENDARY_DISCORD_BOT_COMMAND_SYSTEM_⚡💎👑🤖.py) do (
    if exist "%%f" (
        echo ✅ Found bot file: %%f
        python "%%f"
    ) else (
        echo ❌ Bot file not found: %%f
        echo 🔍 Checking current directory...
        dir *.py | find "ULTIMATE"
    )
)

echo.
echo 🛑 Bot has stopped.
pause

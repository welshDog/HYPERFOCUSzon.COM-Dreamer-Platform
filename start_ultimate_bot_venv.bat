@echo off
chcp 65001 >nul
title Ultimate Legendary Discord Bot Launcher - Virtual Environment
color 0E

echo.
echo ⚡👑💎 ULTIMATE LEGENDARY DISCORD BOT LAUNCHER 💎👑⚡
echo.
echo 🔧 Preparing bot startup with Virtual Environment...
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
echo 🎯 Bot is starting now with Discord.py v2.3.2...
echo.

REM Stop any existing Python processes
taskkill /F /IM python.exe >nul 2>&1

REM Start the bot using the virtual environment
echo 🔧 Using Virtual Environment Python...
H:\.venv\Scripts\python.exe "🤖👑💎⚡_ULTIMATE_LEGENDARY_DISCORD_BOT_COMMAND_SYSTEM_⚡💎👑🤖.py"

echo.
echo 🛑 Bot has stopped.
pause

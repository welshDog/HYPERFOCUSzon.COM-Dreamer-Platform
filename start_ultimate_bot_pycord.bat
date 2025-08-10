@echo off
chcp 65001 >nul
title Ultimate Legendary Discord Bot Launcher - py-cord
color 0E

echo.
echo ⚡👑💎 ULTIMATE LEGENDARY DISCORD BOT LAUNCHER 💎👑⚡
echo.
echo 🔧 Preparing bot startup with py-cord (Python 3.13 compatible)...
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
echo 🎯 Bot is starting now with py-cord v2.4.1...
echo 🐍 Python 3.13.5 Virtual Environment Ready
echo.

REM Stop any existing Python processes
taskkill /F /IM python.exe >nul 2>&1

REM Start the bot using the virtual environment with py-cord
echo 🔧 Using Virtual Environment Python with py-cord...
H:\.venv\Scripts\python.exe "🤖👑💎⚡_ULTIMATE_LEGENDARY_DISCORD_BOT_COMMAND_SYSTEM_⚡💎👑🤖.py"

echo.
echo 🛑 Bot has stopped.
pause

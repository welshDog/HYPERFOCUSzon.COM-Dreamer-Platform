@echo off
setlocal enabledelayedexpansion
title 🚀💎⚡ HyperFocus Zone Discord Activity Launcher V2.0 ⚡💎🚀

:: ==============================================================================
:: 🚀💎⚡ HYPERFOCUS ZONE DISCORD ACTIVITY LAUNCHER - LEGENDARY V2.0 ⚡💎🚀
:: ==============================================================================
:: Enhanced with Ultra BROski Empire Integration & ADHD-Optimized Features
:: Last Updated: August 22, 2025 | Status: LEGENDARY ENHANCED
:: ==============================================================================

:: Color setup for enhanced ADHD-friendly output
set "GREEN=[32m"
set "CYAN=[36m"
set "YELLOW=[33m"
set "RED=[31m"
set "BLUE=[34m"
set "MAGENTA=[35m"
set "WHITE=[37m"
set "RESET=[0m"

:: Display legendary startup banner
cls
echo.
echo %CYAN%████████████████████████████████████████████████████████████████████████████████%RESET%
echo %CYAN%█                                                                              █%RESET%
echo %CYAN%█          🚀💎⚡ HYPERFOCUS ZONE DISCORD ACTIVITY V2.0 ⚡💎🚀            █%RESET%
echo %CYAN%█                                                                              █%RESET%
echo %CYAN%█              🧠 ADHD-Optimized • 🤖 Empire Integration                    █%RESET%
echo %CYAN%█              💰 BROski Economy • 🔮 Memory Crystals                       █%RESET%
echo %CYAN%█              🏆 Real-time Status • ⚡ Legendary Performance               █%RESET%
echo %CYAN%█                                                                              █%RESET%
echo %CYAN%████████████████████████████████████████████████████████████████████████████████%RESET%
echo.

:: Pre-flight system check
echo %YELLOW%🔍 PERFORMING PRE-FLIGHT SYSTEM CHECK...%RESET%
echo.

:: Check if activity directory exists
if not exist "H:\activity" (
    echo %RED%❌ ERROR: Activity directory not found at H:\activity%RESET%
    echo %RED%   Please ensure the HyperFocus Zone activity system is installed.%RESET%
    pause
    exit /b 1
)

:: Check if Python virtual environment exists
if not exist "H:\cloudflare-superpowers\.venv_light\Scripts\python.exe" (
    echo %RED%❌ ERROR: Python virtual environment not found%RESET%
    echo %RED%   Expected: H:\cloudflare-superpowers\.venv_light\Scripts\python.exe%RESET%
    echo %YELLOW%💡 TIP: Run the empire installation script to set up dependencies%RESET%
    pause
    exit /b 1
)

:: Check if activity proxy exists
if not exist "H:\activity\proxy\activity_proxy.py" (
    echo %RED%❌ ERROR: Activity proxy server not found%RESET%
    echo %RED%   Expected: H:\activity\proxy\activity_proxy.py%RESET%
    pause
    exit /b 1
)

:: System check passed
echo %GREEN%✅ Activity directory: FOUND%RESET%
echo %GREEN%✅ Python environment: FOUND%RESET%
echo %GREEN%✅ Proxy server: FOUND%RESET%
echo %GREEN%✅ Pre-flight check: PASSED%RESET%
echo.

:: Change to activity directory
cd /d "H:\activity"
echo %BLUE%📁 Working directory: %CD%%RESET%
echo.

:: Display launch information
echo %MAGENTA%🚀 LAUNCHING ENHANCED DISCORD ACTIVITY FEATURES:%RESET%
echo %WHITE%   🧠 ADHD-Optimized Discord Activity Engine%RESET%
echo %WHITE%   🤖 Real-time ADHD Coach Agent endpoints%RESET%
echo %WHITE%   💰 BROski Economy reward system integration%RESET%
echo %WHITE%   🔮 Memory Crystal unlock triggers%RESET%
echo %WHITE%   🏆 Empire status synchronization%RESET%
echo %WHITE%   ⚡ Enhanced error handling and logging%RESET%
echo %WHITE%   🎯 Focus session tracking and analytics%RESET%
echo %WHITE%   🌟 Team coordination and celebration features%RESET%
echo.

:: Create timestamp for logging
for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
set "timestamp=%dt:~0,4%-%dt:~4,2%-%dt:~6,2% %dt:~8,2%:%dt:~10,2%:%dt:~12,2%"

echo %CYAN%🕒 Launch Time: %timestamp%%RESET%
echo %CYAN%🌐 Server will be available at: http://localhost:3000%RESET%
echo %CYAN%🔗 Discord Activity integration ready%RESET%
echo.

:: Start countdown for ADHD-friendly preparation
echo %YELLOW%⏳ Starting in:%RESET%
for /L %%i in (3,-1,1) do (
    echo %YELLOW%   %%i...%RESET%
    timeout /t 1 /nobreak >nul
)
echo %GREEN%   🚀 GO!%RESET%
echo.

:: Launch the Python server with enhanced error handling
echo %GREEN%🐍 LAUNCHING PYTHON ACTIVITY SERVER...%RESET%
echo %WHITE%━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━%RESET%
echo.

"H:\cloudflare-superpowers\.venv_light\Scripts\python.exe" ".\proxy\activity_proxy.py"

:: Check exit code and provide feedback
if %ERRORLEVEL% equ 0 (
    echo.
    echo %GREEN%✅ Discord Activity server shut down successfully%RESET%
) else (
    echo.
    echo %RED%❌ Discord Activity server encountered an error (Exit code: %ERRORLEVEL%)%RESET%
    echo %YELLOW%💡 Check the server logs above for details%RESET%
)

echo.
echo %CYAN%🏆 HYPERFOCUS ZONE DISCORD ACTIVITY SESSION COMPLETE%RESET%
echo %WHITE%   Thank you for using the enhanced BROski Empire Activity System!%RESET%
echo %WHITE%   🌟 Well done, Team Lush! 🌟%RESET%
echo.

:: Option to restart or exit
set /p "restart=🔄 Would you like to restart the activity server? (y/N): "
if /i "!restart!" == "y" (
    echo %CYAN%🔄 Restarting HyperFocus Zone Discord Activity...%RESET%
    goto :eof
    call "%~f0"
) else (
    echo %BLUE%👋 Goodbye! Empire activities synchronized successfully.%RESET%
)

pause

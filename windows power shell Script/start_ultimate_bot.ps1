# Ultimate Discord Bot Launcher
Write-Host "⚡👑💎 ULTIMATE LEGENDARY DISCORD BOT LAUNCHER 💎👑⚡" -ForegroundColor Yellow
Write-Host ""
Write-Host "🔧 Initializing bot startup sequence..." -ForegroundColor Cyan
Write-Host "🤖 Loading hybrid command system (! and /)..." -ForegroundColor Green
Write-Host "💎 Activating BROski$ rewards engine..." -ForegroundColor Magenta
Write-Host ""

# Stop any existing Python processes
Write-Host "🛑 Stopping any existing bot processes..." -ForegroundColor Yellow
Get-Process python -ErrorAction SilentlyContinue | Stop-Process -Force -ErrorAction SilentlyContinue

# Start the enhanced bot
Write-Host "🚀 Starting Ultimate Legendary Discord Bot..." -ForegroundColor Green
Write-Host "📋 Bot Features:" -ForegroundColor White
Write-Host "  ✅ Traditional Commands (!help, !status, !health)" -ForegroundColor Gray
Write-Host "  ✅ Modern Slash Commands (/help, /status, /health)" -ForegroundColor Gray
Write-Host "  ✅ BROski$ Economy with Bonus Rewards" -ForegroundColor Gray
Write-Host "  ✅ AI-Powered Systems & Health Monitoring" -ForegroundColor Gray
Write-Host "  ✅ Mood Tracking & Achievement System" -ForegroundColor Gray
Write-Host ""
Write-Host "🎯 Starting bot now..." -ForegroundColor Yellow

python "🤖👑💎⚡_ULTIMATE_LEGENDARY_DISCORD_BOT_COMMAND_SYSTEM_⚡💎👑🤖.py"

Write-Host ""
Write-Host "🛑 Bot has stopped. Press any key to exit..." -ForegroundColor Red
Read-Host

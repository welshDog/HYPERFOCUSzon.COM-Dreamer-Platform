# 🚀💎⚡ BROSKI DISCORD BOT LAUNCHER ⚡💎🚀
# PowerShell launcher for the comprehensive neurodivergent community bot

Write-Host "🚀💎⚡ LAUNCHING BROSKI DISCORD BOT ⚡💎🚀" -ForegroundColor Cyan
Write-Host ""
Write-Host "🤖 Starting the comprehensive neurodivergent community bot..." -ForegroundColor Yellow
Write-Host ""

# Change to the correct directory
Set-Location "h:\"

try {
    Write-Host "🎯 Trying broski_bot_clean.py first..." -ForegroundColor Green
    $result = Start-Process -FilePath "python" -ArgumentList "broski_bot_clean.py" -Wait -PassThru -NoNewWindow

    if ($result.ExitCode -ne 0) {
        Write-Host ""
        Write-Host "⚠️ Clean bot failed, trying main launcher..." -ForegroundColor Yellow
        $result2 = Start-Process -FilePath "python" -ArgumentList "🤖💎⚡_LEGENDARY_BROSKI_DISCORD_BOT_LAUNCHER_⚡💎🤖.py" -Wait -PassThru -NoNewWindow

        if ($result2.ExitCode -ne 0) {
            Write-Host ""
            Write-Host "❌ Both launchers failed. Checking Python installation..." -ForegroundColor Red
            python --version
            Write-Host ""
            Write-Host "💡 Make sure you have:" -ForegroundColor Yellow
            Write-Host "   1. Python installed and in PATH" -ForegroundColor White
            Write-Host "   2. Discord.py installed: pip install discord.py" -ForegroundColor White
            Write-Host "   3. Your Discord bot token in .env file" -ForegroundColor White
        }
    }
} catch {
    Write-Host ""
    Write-Host "❌ Error launching bot: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host ""
    Write-Host "💡 Troubleshooting:" -ForegroundColor Yellow
    Write-Host "   - Check if Python is installed: python --version" -ForegroundColor White
    Write-Host "   - Install Discord.py: pip install discord.py" -ForegroundColor White
    Write-Host "   - Check your .env file has DISCORD_BOT_TOKEN" -ForegroundColor White
}

Write-Host ""
Write-Host "Press any key to continue..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

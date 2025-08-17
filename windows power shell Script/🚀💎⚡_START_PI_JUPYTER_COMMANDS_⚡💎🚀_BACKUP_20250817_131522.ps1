# 🔥💎⚡ LEGENDARY PI JUPYTER STARTUP COMMANDS ⚡💎🔥
# PowerShell commands to start Jupyter on your Raspberry Pi

Write-Host "🚀 STARTING LEGENDARY JUPYTER ON RASPBERRY PI..." -ForegroundColor Yellow
Write-Host "🎯 Pi IP: 192.168.137.10" -ForegroundColor Cyan
Write-Host "📓 Jupyter will be available at: http://192.168.137.10:8888" -ForegroundColor Green
Write-Host ""

# Option 1: Direct SSH command (if SSH is working)
Write-Host "📋 OPTION 1: SSH Command (run this if SSH is enabled)" -ForegroundColor Magenta
Write-Host 'ssh pi@192.168.137.10 "jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root"' -ForegroundColor White

Write-Host ""

# Option 2: VS Code Server method (recommended)
Write-Host "📋 OPTION 2: Via VS Code Server (RECOMMENDED)" -ForegroundColor Magenta
Write-Host "1. Open browser: http://192.168.137.10:8080" -ForegroundColor White
Write-Host "2. Open terminal in VS Code Server" -ForegroundColor White
Write-Host "3. Run this command in Pi terminal:" -ForegroundColor White
Write-Host 'jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root' -ForegroundColor Yellow

Write-Host ""
Write-Host "🎊 AFTER JUPYTER STARTS:" -ForegroundColor Green
Write-Host "🌐 Access Jupyter from laptop: http://192.168.137.10:8888" -ForegroundColor Cyan
Write-Host "🔥💎⚡ LEGENDARY PI-LAPTOP FUSION READY! ⚡💎🔥" -ForegroundColor Yellow

# Test Pi connectivity first
Write-Host ""
Write-Host "🔍 TESTING PI CONNECTIVITY..." -ForegroundColor Yellow
$pingResult = Test-Connection -ComputerName 192.168.137.10 -Count 1 -Quiet

if ($pingResult) {
    Write-Host "✅ Pi is CONNECTED and ready!" -ForegroundColor Green
    Write-Host "🚀 Proceed with starting Jupyter using Option 2 above" -ForegroundColor Yellow
} else {
    Write-Host "❌ Pi not responding to ping" -ForegroundColor Red
    Write-Host "🔧 Check Pi power and network connection" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "🎯 NEXT: Open the notebook file to continue development!" -ForegroundColor Magenta
Write-Host "📓 File: 🔥💎⚡_LEGENDARY_PI_LAPTOP_AI_FUSION_DEVELOPMENT_⚡💎🔥.ipynb" -ForegroundColor Cyan

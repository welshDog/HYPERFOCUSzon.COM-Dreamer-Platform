# 🔥💎⚡ LEGENDARY PI TROUBLESHOOTING & STARTUP GUIDE ⚡💎🔥
# Complete guide to get your Pi VS Code Server and Jupyter working!

Write-Host ""
Write-Host "🔍 DIAGNOSING PI CONNECTION ISSUES..." -ForegroundColor Yellow
Write-Host "🎯 Target: 192.168.137.10" -ForegroundColor Cyan
Write-Host ""

# Test basic connectivity
Write-Host "📡 Testing basic ping..." -ForegroundColor Magenta
$pingTest = Test-Connection -ComputerName 192.168.137.10 -Count 2 -Quiet
if ($pingTest) {
    Write-Host "✅ Pi responds to ping - Network OK!" -ForegroundColor Green
} else {
    Write-Host "❌ Pi not responding to ping - Check power/network" -ForegroundColor Red
    exit
}

# Test VS Code Server port
Write-Host "🚀 Testing VS Code Server (port 8080)..." -ForegroundColor Magenta
$vscodeTest = Test-NetConnection -ComputerName 192.168.137.10 -Port 8080 -InformationLevel Quiet
if ($vscodeTest) {
    Write-Host "✅ VS Code Server port is open!" -ForegroundColor Green
} else {
    Write-Host "❌ VS Code Server not running - Need to start it" -ForegroundColor Red
}

# Test Jupyter port
Write-Host "📓 Testing Jupyter (port 8888)..." -ForegroundColor Magenta
$jupyterTest = Test-NetConnection -ComputerName 192.168.137.10 -Port 8888 -InformationLevel Quiet
if ($jupyterTest) {
    Write-Host "✅ Jupyter is running!" -ForegroundColor Green
} else {
    Write-Host "⚠️ Jupyter not started yet" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "🔧 SOLUTION OPTIONS:" -ForegroundColor Yellow
Write-Host ""

if ($vscodeTest) {
    Write-Host "📋 OPTION 1: Try different browser access" -ForegroundColor Magenta
    Write-Host "🌐 Try these URLs in your browser:" -ForegroundColor White
    Write-Host "   • http://192.168.137.10:8080" -ForegroundColor Cyan
    Write-Host "   • http://192.168.137.10:8080/?folder=/home/pi" -ForegroundColor Cyan
    Write-Host ""
    
    Write-Host "📋 OPTION 2: Direct browser launch" -ForegroundColor Magenta
    Write-Host "🚀 Starting your default browser..." -ForegroundColor White
    Start-Process "http://192.168.137.10:8080"
    Write-Host "✅ Browser launched!" -ForegroundColor Green
} else {
    Write-Host "📋 NEED TO START VS CODE SERVER ON PI" -ForegroundColor Red
    Write-Host ""
    Write-Host "🔧 SSH to Pi and run these commands:" -ForegroundColor White
    Write-Host "ssh pi@192.168.137.10" -ForegroundColor Yellow
    Write-Host "code-server --bind-addr=0.0.0.0:8080 --auth=none" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "📋 OPTION 3: Start Jupyter directly via SSH" -ForegroundColor Magenta
Write-Host "🔧 If you can SSH to Pi:" -ForegroundColor White
Write-Host 'ssh pi@192.168.137.10 "jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root"' -ForegroundColor Yellow

Write-Host ""
Write-Host "📋 OPTION 4: Alternative - Use Python HTTP Server" -ForegroundColor Magenta
Write-Host "🔧 Simple file access:" -ForegroundColor White
Write-Host 'ssh pi@192.168.137.10 "cd ~ && python3 -m http.server 8000"' -ForegroundColor Yellow
Write-Host "Then access: http://192.168.137.10:8000" -ForegroundColor Cyan

Write-Host ""
Write-Host "🎯 RECOMMENDED NEXT STEPS:" -ForegroundColor Green
Write-Host "1. Try the browser that just opened" -ForegroundColor White
Write-Host "2. If that doesn't work, we'll SSH to Pi and start services manually" -ForegroundColor White
Write-Host "3. Then run our legendary Jupyter notebook!" -ForegroundColor White

Write-Host ""
Write-Host "🔥💎⚡ LEGENDARY TEAM SUPPORT ACTIVATED! ⚡💎🔥" -ForegroundColor Yellow

# 🚀⚡ ULTRA dOoK PORTAL QUICK DEPLOYMENT ⚡🚀

Write-Host "🩵💚❤️‍🔥 ULTRA dOoK PORTAL DEPLOYMENT INITIATED! ❤️‍🔥💚🩵" -ForegroundColor Cyan
Write-Host "=============================================" -ForegroundColor Yellow

$portalPath = "h:\tHE HYPERFOUCS dOoK ultra Web Comic\ultra-dook-portal"

# Check if Node.js is installed
Write-Host "`n🔍 Checking Node.js installation..." -ForegroundColor Green
$nodeVersion = node --version 2>$null
if ($nodeVersion) {
    Write-Host "✅ Node.js found: $nodeVersion" -ForegroundColor Green
} else {
    Write-Host "❌ Node.js not found! Please install Node.js first." -ForegroundColor Red
    Write-Host "   Download from: https://nodejs.org/" -ForegroundColor Yellow
    exit 1
}

# Check if npm is available
$npmVersion = npm --version 2>$null
if ($npmVersion) {
    Write-Host "✅ npm found: $npmVersion" -ForegroundColor Green
} else {
    Write-Host "❌ npm not found!" -ForegroundColor Red
    exit 1
}

# Navigate to portal directory
Write-Host "`n📁 Navigating to portal directory..." -ForegroundColor Green
if (Test-Path $portalPath) {
    Set-Location $portalPath
    Write-Host "✅ Located portal at: $portalPath" -ForegroundColor Green
} else {
    Write-Host "❌ Portal directory not found!" -ForegroundColor Red
    exit 1
}

# Install dependencies
Write-Host "`n📦 Installing dependencies..." -ForegroundColor Green
Write-Host "This may take a few minutes..." -ForegroundColor Yellow
try {
    npm install
    Write-Host "✅ Dependencies installed successfully!" -ForegroundColor Green
} catch {
    Write-Host "❌ Failed to install dependencies!" -ForegroundColor Red
    Write-Host "Error: $_" -ForegroundColor Red
    exit 1
}

# Build the project
Write-Host "`n🏗️ Building the Ultra dOoK Portal..." -ForegroundColor Green
try {
    npm run build
    Write-Host "✅ Portal built successfully!" -ForegroundColor Green
} catch {
    Write-Host "⚠️ Build had some warnings, but continuing..." -ForegroundColor Yellow
}

# Start the development server
Write-Host "`n🚀 Launching Ultra dOoK Portal..." -ForegroundColor Cyan
Write-Host "Portal will be available at: http://localhost:3000" -ForegroundColor Yellow
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor White
Write-Host "`n🎊 LAUNCHING IN 3 SECONDS..." -ForegroundColor Magenta

Start-Sleep -Seconds 3

try {
    # Open browser (optional)
    Start-Process "http://localhost:3000"
    
    # Start the dev server
    npm run dev
} catch {
    Write-Host "❌ Failed to start portal!" -ForegroundColor Red
    Write-Host "Error: $_" -ForegroundColor Red
    Write-Host "`n🔧 Try running manually:" -ForegroundColor Yellow
    Write-Host "   cd `"$portalPath`"" -ForegroundColor White
    Write-Host "   npm run dev" -ForegroundColor White
}

Write-Host "`n🎊 ULTRA dOoK PORTAL DEPLOYMENT COMPLETE!" -ForegroundColor Cyan
Write-Host "=============================================" -ForegroundColor Yellow

# HyperFocus Zone AI Assistant - Windows PowerShell Deployment
# Deploy to your Docker empire at 212.227.127.144:8888

Write-Host "🐳💎⚡ DEPLOYING HYPERFOCUS ZONE AI ASSISTANT ⚡💎🐳" -ForegroundColor Cyan
Write-Host "================================================================" -ForegroundColor Yellow

# Check if Docker is installed
Write-Host "🔍 Checking Docker availability..." -ForegroundColor Yellow
if (-not (Get-Command docker -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Docker not found. Please install Docker Desktop first." -ForegroundColor Red
    Write-Host "Download from: https://www.docker.com/products/docker-desktop" -ForegroundColor Yellow
    exit 1
}

Write-Host "✅ Docker is available" -ForegroundColor Green

# Navigate to project directory
Write-Host "📁 Navigating to project directory..." -ForegroundColor Yellow
Set-Location "hyperfocus-ai-docker"

# Stop existing containers
Write-Host "🛑 Stopping existing containers..." -ForegroundColor Yellow
docker-compose down --remove-orphans 2>$null

# Create ollama data directory
Write-Host "📂 Creating data directories..." -ForegroundColor Yellow
if (-not (Test-Path "ollama_data")) {
    New-Item -ItemType Directory -Path "ollama_data"
}

# Build and deploy
Write-Host "🏗️ Building AI Assistant container..." -ForegroundColor Cyan
docker-compose build --no-cache

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Build failed. Check Docker and try again." -ForegroundColor Red
    exit 1
}

Write-Host "🚀 Starting HyperFocus Zone AI Assistant..." -ForegroundColor Green
docker-compose up -d

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Deployment failed. Check logs with: docker-compose logs" -ForegroundColor Red
    exit 1
}

# Wait for services to start
Write-Host "⏳ Waiting for services to initialize..." -ForegroundColor Yellow
Start-Sleep -Seconds 30

# Health check
Write-Host "🏥 Running health checks..." -ForegroundColor Yellow

try {
    $healthResponse = Invoke-RestMethod -Uri "http://localhost:8888/health" -TimeoutSec 10
    Write-Host "✅ AI Assistant is responding!" -ForegroundColor Green
    Write-Host "   Status: $($healthResponse.status)" -ForegroundColor Cyan
    Write-Host "   Empire: $($healthResponse.empire_status)" -ForegroundColor Cyan
} catch {
    Write-Host "⚠️ AI Assistant not responding yet (may still be starting up)" -ForegroundColor Yellow
}

# Display service status
Write-Host "`n📊 SERVICE STATUS" -ForegroundColor Cyan
Write-Host "=================" -ForegroundColor Yellow
docker-compose ps

Write-Host "`n🎯 EMPIRE ENDPOINTS" -ForegroundColor Cyan
Write-Host "===================" -ForegroundColor Yellow
Write-Host "🧠 AI Assistant: http://212.227.127.144:8888" -ForegroundColor Green
Write-Host "🏥 Health Check: http://212.227.127.144:8888/health" -ForegroundColor Green
Write-Host "🤖 Local AI: http://212.227.127.144:11434" -ForegroundColor Green
Write-Host "📊 Techniques: http://212.227.127.144:8888/techniques" -ForegroundColor Green

Write-Host "`n🎉 DEPLOYMENT COMPLETE!" -ForegroundColor Green
Write-Host "🌟 Your neurodivergent focus coaching empire is now ACTIVE!" -ForegroundColor Cyan

Write-Host "`n🚀 NEXT STEPS:" -ForegroundColor Yellow
Write-Host "1. Test: curl http://212.227.127.144:8888/health" -ForegroundColor White
Write-Host "2. Configure Cloudflare proxy: support.hyperfocuszone.com → 212.227.127.144:8888" -ForegroundColor White
Write-Host "3. Test via SSL: https://support.hyperfocuszone.com/health" -ForegroundColor White
Write-Host "4. Start helping neurodivergent individuals focus! 🎯" -ForegroundColor White

Write-Host "`n📚 TEST YOUR AI ASSISTANT:" -ForegroundColor Cyan
Write-Host "curl -X POST http://212.227.127.144:8888/chat -H 'Content-Type: application/json' -d '{`"message`":`"I have ADHD and need help focusing`"}'" -ForegroundColor Gray

Write-Host "`n💎 EMPIRE STATUS: LEGENDARY! 💎" -ForegroundColor Magenta

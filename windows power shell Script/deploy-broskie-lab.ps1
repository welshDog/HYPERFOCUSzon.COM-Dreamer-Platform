# 🚀💎⚡ BROski Ultra Agent Lab Control Panel - INSTANT DEPLOYMENT ⚡💎🚀
Write-Host "🚀💎⚡ BROski Ultra Agent Lab Control Panel - Docker Deployment ⚡💎🚀" -ForegroundColor Cyan
Write-Host "=================================================================" -ForegroundColor Cyan

# Check if Docker is running
try {
    docker info | Out-Null
    Write-Host "✅ Docker is running" -ForegroundColor Green
}
catch {
    Write-Host "❌ Docker is not running. Please start Docker first." -ForegroundColor Red
    exit 1
}

# Build the Docker image
Write-Host "🔨 Building BROski Agent Lab Docker image..." -ForegroundColor Yellow
docker build -t broskie-agent-lab:latest .

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Docker image built successfully" -ForegroundColor Green
} else {
    Write-Host "❌ Failed to build Docker image" -ForegroundColor Red
    exit 1
}

# Stop any existing container
Write-Host "🛑 Stopping any existing BROski Agent Lab container..." -ForegroundColor Yellow
docker stop broskie-agent-lab 2>$null
docker rm broskie-agent-lab 2>$null

# Run the new container
Write-Host "🚀 Starting BROski Ultra Agent Lab Control Panel..." -ForegroundColor Cyan
docker run -d `
    --name broskie-agent-lab `
    -p 8501:8501 `
    --restart unless-stopped `
    broskie-agent-lab:latest

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ BROski Ultra Agent Lab Control Panel is now running!" -ForegroundColor Green
    Write-Host "🌐 Access at: http://localhost:8501" -ForegroundColor Cyan
    Write-Host "📊 Dashboard ready for managing 1,050+ AI agents" -ForegroundColor Magenta
    
    # Wait a moment for startup
    Start-Sleep -Seconds 5
    
    # Check if it's healthy
    try {
        $response = Invoke-WebRequest -Uri "http://localhost:8501/_stcore/health" -UseBasicParsing -TimeoutSec 10
        if ($response.StatusCode -eq 200) {
            Write-Host "💚 Health check passed - Control panel is fully operational!" -ForegroundColor Green
        }
    }
    catch {
        Write-Host "⚠️  Control panel starting up... Check http://localhost:8501 in a few moments" -ForegroundColor Yellow
    }
} else {
    Write-Host "❌ Failed to start BROski Agent Lab container" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "🔧 Management Commands:" -ForegroundColor Cyan
Write-Host "  View logs: docker logs broskie-agent-lab" -ForegroundColor White
Write-Host "  Stop:      docker stop broskie-agent-lab" -ForegroundColor White
Write-Host "  Restart:   docker restart broskie-agent-lab" -ForegroundColor White
Write-Host ""
Write-Host "🎉 BROski Ultra Agent Lab Control Panel deployment complete!" -ForegroundColor Green

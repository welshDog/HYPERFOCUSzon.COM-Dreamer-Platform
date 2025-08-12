#!/usr/bin/env pwsh

<#
🚀💎⚡ DOCKER READINESS CHECKER ⚡💎🚀
Waits for Docker Desktop to be ready after update
BROski♾️ AI DEV - ADHD-Optimized Docker Status Monitor
#>

Write-Host "🚀💎⚡ DOCKER DESKTOP READINESS CHECKER ⚡💎🚀" -ForegroundColor Magenta
Write-Host "================================================================" -ForegroundColor Magenta
Write-Host "Monitoring Docker Desktop update progress..." -ForegroundColor Cyan
Write-Host "================================================================" -ForegroundColor Magenta
Write-Host ""

$maxAttempts = 30
$attempt = 1
$dockerReady = $false

while ($attempt -le $maxAttempts -and -not $dockerReady) {
    Write-Host "🔍 Attempt $attempt/$maxAttempts - Checking Docker Engine..." -ForegroundColor Yellow

    try {
        # Test Docker version first
        $dockerVersion = docker --version 2>$null
        if ($LASTEXITCODE -eq 0) {
            Write-Host "   ✅ Docker CLI: $dockerVersion" -ForegroundColor Green

            # Test Docker Engine
            docker info 2>$null | Out-Null
            if ($LASTEXITCODE -eq 0) {
                Write-Host "   ✅ Docker Engine: READY!" -ForegroundColor Green
                $dockerReady = $true

                # Quick container status check
                Write-Host ""
                Write-Host "🐳 Current Container Status:" -ForegroundColor Cyan
                $containers = docker ps -a --format "{{.Names}}\t{{.Status}}" 2>$null
                if ($containers) {
                    Write-Host $containers -ForegroundColor Gray
                } else {
                    Write-Host "   📭 No containers found (ready for deployment)" -ForegroundColor Gray
                }

                break
            } else {
                Write-Host "   ⏳ Docker Engine still starting up..." -ForegroundColor Yellow
            }
        } else {
            Write-Host "   ⏳ Docker CLI not ready..." -ForegroundColor Yellow
        }
    } catch {
        Write-Host "   ⏳ Docker not ready: $($_.Exception.Message)" -ForegroundColor Yellow
    }

    if ($attempt -lt $maxAttempts) {
        Write-Host "   🕐 Waiting 10 seconds before next check..." -ForegroundColor Gray
        Start-Sleep -Seconds 10
    }

    $attempt++
}

Write-Host ""
Write-Host "================================================================" -ForegroundColor Magenta

if ($dockerReady) {
    Write-Host "🏆 DOCKER DESKTOP IS READY! ⚡💎🚀" -ForegroundColor Green
    Write-Host ""
    Write-Host "🚀 READY TO DEPLOY YOUR LEGENDARY AI STACK!" -ForegroundColor Magenta
    Write-Host "Run this command to deploy SmolLM2:" -ForegroundColor Cyan
    Write-Host "   .\🚀💎⚡_LEGENDARY_SMOLLM2_DEPLOYMENT_ACTIVATOR_⚡💎🚀.ps1 -Deploy" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Or run the Python integrator directly:" -ForegroundColor Cyan
    Write-Host "   python '.\🚀💎⚡_SMOLLM2_DOCKER_AUTO_UPGRADE_INTEGRATOR_⚡💎🚀.py'" -ForegroundColor Yellow
} else {
    Write-Host "⏰ Docker Desktop still updating..." -ForegroundColor Yellow
    Write-Host "💡 This is normal for major updates. Docker Desktop may take 5-15 minutes." -ForegroundColor Gray
    Write-Host "💡 You can run this script again or wait for Docker Desktop notification." -ForegroundColor Gray
}

Write-Host "================================================================" -ForegroundColor Magenta

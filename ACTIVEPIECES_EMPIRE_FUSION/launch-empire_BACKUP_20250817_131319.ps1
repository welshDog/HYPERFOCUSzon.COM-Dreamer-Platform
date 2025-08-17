# 🚀💎⚡ HYPERFOCUS ZONE ACTIVEPIECES LAUNCHER ⚡💎🚀
# Quick PowerShell launcher for your ADHD-optimized workflow paradise!

param(
    [string]$Action = "start"
)

$ContainerName = "hyperfocus-activepieces"
$Port = "8080"
$Url = "http://localhost:$Port"

function Show-Banner {
    Write-Host "🚀💎⚡ HYPERFOCUS ZONE ACTIVEPIECES EMPIRE ⚡💎🚀" -ForegroundColor Cyan
    Write-Host "🧠 ADHD-Optimized Workflow Automation Paradise!" -ForegroundColor Yellow
    Write-Host "=" * 60 -ForegroundColor Gray
    Write-Host ""
}

function Test-DockerRunning {
    try {
        docker --version | Out-Null
        return $true
    }
    catch {
        Write-Host "❌ Docker not found! Please install Docker Desktop." -ForegroundColor Red
        return $false
    }
}

function Test-ContainerRunning {
    try {
        $result = docker ps --filter "name=$ContainerName" --format "{{.Names}}" 2>$null
        return $result -eq $ContainerName
    }
    catch {
        return $false
    }
}

function Start-Empire {
    Show-Banner

    Write-Host "🔍 Checking Docker availability..." -ForegroundColor Yellow
    if (-not (Test-DockerRunning)) {
        return
    }

    Write-Host "🔍 Checking empire status..." -ForegroundColor Yellow
    if (Test-ContainerRunning) {
        Write-Host "✅ Empire already operational! Opening portal..." -ForegroundColor Green
        Open-Portal
        return
    }

    Write-Host "🧹 Cleaning up old empire instances..." -ForegroundColor Yellow
    docker rm -f $ContainerName 2>$null | Out-Null

    Write-Host "🚀 Launching HYPERFOCUS ZONE Empire..." -ForegroundColor Cyan
    $dockerCmd = @(
        "run", "-d",
        "-p", "$Port:80",
        "--name", $ContainerName,
        "-e", "AP_ENCRYPTION_KEY=hyperfocus_zone_legendary_key_2025",
        "-e", "AP_JWT_SECRET=hyperfocus_zone_jwt_secret_2025",
        "-e", "AP_SIGN_UP_ENABLED=true",
        "-e", "AP_TELEMETRY_ENABLED=false",
        "activepieces/activepieces:latest"
    )

    try {
        $containerId = & docker @dockerCmd
        if ($LASTEXITCODE -eq 0) {
            Write-Host "⏱️ Waiting for empire to initialize..." -ForegroundColor Yellow

            # Wait for startup
            for ($i = 1; $i -le 12; $i++) {
                Start-Sleep -Seconds 5
                Write-Host "   ⏳ Initialization progress: $($i * 8)%..." -ForegroundColor Gray

                try {
                    $response = Invoke-WebRequest -Uri $Url -TimeoutSec 3 -ErrorAction SilentlyContinue
                    if ($response.StatusCode -eq 200) {
                        Write-Host "🎊 EMPIRE FULLY OPERATIONAL!" -ForegroundColor Green
                        Write-Host "💎 Opening HYPERFOCUS ZONE portal..." -ForegroundColor Cyan
                        Open-Portal
                        Show-QuickStart
                        return
                    }
                }
                catch {
                    # Continue waiting
                }
            }

            Write-Host "⚠️ Empire started but taking longer than expected..." -ForegroundColor Yellow
            Write-Host "💡 Try visiting $Url manually in a few minutes" -ForegroundColor Gray
        }
        else {
            Write-Host "❌ Empire launch failed!" -ForegroundColor Red
            Show-Troubleshoot
        }
    }
    catch {
        Write-Host "❌ Error launching empire: $_" -ForegroundColor Red
    }
}

function Stop-Empire {
    Write-Host "🛑 Stopping HYPERFOCUS ZONE Empire..." -ForegroundColor Yellow
    docker stop $ContainerName 2>$null | Out-Null
    docker rm $ContainerName 2>$null | Out-Null
    Write-Host "✅ Empire stopped gracefully" -ForegroundColor Green
}

function Restart-Empire {
    Write-Host "🔄 Restarting HYPERFOCUS ZONE Empire..." -ForegroundColor Cyan
    Stop-Empire
    Start-Sleep -Seconds 2
    Start-Empire
}

function Show-Status {
    if (Test-ContainerRunning) {
        Write-Host "✅ Empire is OPERATIONAL" -ForegroundColor Green
        Write-Host "🌐 Portal: $Url" -ForegroundColor Cyan
        Open-Portal
    }
    else {
        Write-Host "❌ Empire is offline" -ForegroundColor Red
        Write-Host "💡 Run with 'start' to launch empire" -ForegroundColor Gray
    }
}

function Open-Portal {
    try {
        Start-Process $Url
        Write-Host "🌐 Portal opened: $Url" -ForegroundColor Green
    }
    catch {
        Write-Host "💡 Manually visit: $Url" -ForegroundColor Gray
    }
}

function Show-QuickStart {
    Write-Host ""
    Write-Host "=" * 60 -ForegroundColor Gray
    Write-Host "🎯 HYPERFOCUS ZONE QUICK START GUIDE" -ForegroundColor Cyan
    Write-Host "=" * 60 -ForegroundColor Gray
    Write-Host "🚀 Your dopamine-triggered workflow paradise is READY!" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "🎯 FIRST STEPS:" -ForegroundColor Cyan
    Write-Host "   1. 📝 Create account (if first time)" -ForegroundColor White
    Write-Host "   2. 🎨 Explore the visual workflow builder" -ForegroundColor White
    Write-Host "   3. 🤖 Try connecting a service (Discord, Google Sheets)" -ForegroundColor White
    Write-Host "   4. ⚡ Build your first ADHD-optimized workflow!" -ForegroundColor White
    Write-Host ""
    Write-Host "💎 LEGENDARY WORKFLOW IDEAS:" -ForegroundColor Cyan
    Write-Host "   🎊 Celebration Cascade: Task complete → Discord party" -ForegroundColor White
    Write-Host "   🧠 Focus Detector: Hyperfocus start → Block distractions" -ForegroundColor White
    Write-Host "   📊 Achievement Tracker: Code commit → Progress celebration" -ForegroundColor White
    Write-Host "   🔔 Break Reminder: 2hr timer → Gentle ADHD-friendly break" -ForegroundColor White
    Write-Host ""
    Write-Host "💎 Ready to automate your LEGENDARY empire! 🚀" -ForegroundColor Yellow
}

function Show-Troubleshoot {
    Write-Host ""
    Write-Host "🔧 TROUBLESHOOTING GUIDE:" -ForegroundColor Yellow
    Write-Host "1. ✅ Check Docker Desktop is running" -ForegroundColor White
    Write-Host "2. 🔄 Try: docker --version" -ForegroundColor White
    Write-Host "3. 🧹 Clean restart: docker system prune -a" -ForegroundColor White
    Write-Host "4. 🌐 Manual check: visit $Url" -ForegroundColor White
    Write-Host "5. 📝 Check logs: docker logs $ContainerName" -ForegroundColor White
}

# Main script logic
switch ($Action.ToLower()) {
    "start" { Start-Empire }
    "stop" { Stop-Empire }
    "restart" { Restart-Empire }
    "status" { Show-Status }
    default {
        Show-Banner
        Write-Host "Usage: .\launch-empire.ps1 [start|stop|restart|status]" -ForegroundColor Gray
        Write-Host "Default action is 'start'" -ForegroundColor Gray
    }
}

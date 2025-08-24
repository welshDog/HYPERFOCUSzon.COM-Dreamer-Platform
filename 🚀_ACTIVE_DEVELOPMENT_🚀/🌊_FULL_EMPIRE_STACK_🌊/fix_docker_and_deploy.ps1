# 🌌♾️⚡ HYPERFOCUS EMPIRE - DOCKER DIAGNOSTIC & FIX SCRIPT ⚡♾️🌌

Write-Host "🔍 HYPERFOCUS EMPIRE - DOCKER DIAGNOSTIC" -ForegroundColor Cyan
Write-Host "=" * 50 -ForegroundColor Cyan

# Function to test Docker
function Test-DockerStatus {
    Write-Host "`n🐳 Testing Docker Status..." -ForegroundColor Yellow

    try {
        $dockerVersion = docker --version 2>$null
        if ($dockerVersion) {
            Write-Host "✅ Docker CLI: $dockerVersion" -ForegroundColor Green
        } else {
            Write-Host "❌ Docker CLI not found" -ForegroundColor Red
            return $false
        }

        # Test Docker daemon
        Write-Host "🔌 Testing Docker daemon..." -ForegroundColor Yellow
        $dockerInfo = docker info 2>$null
        if ($LASTEXITCODE -eq 0) {
            Write-Host "✅ Docker daemon: Responding" -ForegroundColor Green
            return $true
        } else {
            Write-Host "❌ Docker daemon: Not responding" -ForegroundColor Red
            return $false
        }
    } catch {
        Write-Host "❌ Docker test failed: $_" -ForegroundColor Red
        return $false
    }
}

# Function to restart Docker Desktop
function Restart-DockerDesktop {
    Write-Host "`n🔄 Attempting to restart Docker Desktop..." -ForegroundColor Yellow

    try {
        # Stop Docker Desktop
        Write-Host "⏹️  Stopping Docker Desktop..." -ForegroundColor Yellow
        Stop-Process -Name "Docker Desktop" -Force -ErrorAction SilentlyContinue
        Start-Sleep -Seconds 5

        # Stop Docker services
        Write-Host "🛑 Stopping Docker services..." -ForegroundColor Yellow
        Stop-Service -Name "com.docker.service" -Force -ErrorAction SilentlyContinue
        Stop-Service -Name "Docker Desktop Service" -Force -ErrorAction SilentlyContinue
        Start-Sleep -Seconds 3

        # Start Docker Desktop
        Write-Host "🚀 Starting Docker Desktop..." -ForegroundColor Yellow
        $dockerPath = Get-ChildItem -Path "C:\Program Files\Docker\Docker\Docker Desktop.exe" -ErrorAction SilentlyContinue
        if ($dockerPath) {
            Start-Process -FilePath $dockerPath.FullName -WindowStyle Hidden
            Write-Host "⏳ Waiting for Docker Desktop to start (60 seconds)..." -ForegroundColor Yellow
            Start-Sleep -Seconds 60
            return $true
        } else {
            Write-Host "❌ Docker Desktop executable not found" -ForegroundColor Red
            return $false
        }
    } catch {
        Write-Host "❌ Failed to restart Docker Desktop: $_" -ForegroundColor Red
        return $false
    }
}

# Function to check Windows services
function Check-WindowsServices {
    Write-Host "`n🔧 Checking Windows Services..." -ForegroundColor Yellow

    $services = @("com.docker.service", "Docker Desktop Service", "LxssManager")

    foreach ($service in $services) {
        try {
            $svc = Get-Service -Name $service -ErrorAction SilentlyContinue
            if ($svc) {
                if ($svc.Status -eq "Running") {
                    Write-Host "✅ $service: Running" -ForegroundColor Green
                } else {
                    Write-Host "⚠️  $service: $($svc.Status)" -ForegroundColor Yellow
                    try {
                        Start-Service -Name $service
                        Write-Host "🔄 Started $service" -ForegroundColor Green
                    } catch {
                        Write-Host "❌ Failed to start $service" -ForegroundColor Red
                    }
                }
            } else {
                Write-Host "❌ $service: Not found" -ForegroundColor Red
            }
        } catch {
            Write-Host "❌ Error checking $service: $_" -ForegroundColor Red
        }
    }
}

# Function to deploy minimal empire
function Deploy-MinimalEmpire {
    Write-Host "`n🚀 Deploying Minimal HyperFocus Empire..." -ForegroundColor Cyan

    Set-Location "h:\🚀_ACTIVE_DEVELOPMENT_🚀\🌊_FULL_EMPIRE_STACK_🌊"

    try {
        $result = docker compose -f docker-compose.minimal.yml up -d
        if ($LASTEXITCODE -eq 0) {
            Write-Host "✅ Minimal Empire deployed successfully!" -ForegroundColor Green
            Show-EmpireStatus
            return $true
        } else {
            Write-Host "❌ Deployment failed" -ForegroundColor Red
            return $false
        }
    } catch {
        Write-Host "❌ Deployment error: $_" -ForegroundColor Red
        return $false
    }
}

# Function to show empire status
function Show-EmpireStatus {
    Write-Host "`n🌟 HYPERFOCUS EMPIRE ACCESS POINTS:" -ForegroundColor Cyan
    Write-Host "🐰 RabbitMQ Management: http://localhost:15672" -ForegroundColor Green
    Write-Host "📦 MinIO Console: http://localhost:9001" -ForegroundColor Green
    Write-Host "📈 Grafana Dashboard: http://localhost:3000" -ForegroundColor Green
    Write-Host "📊 Prometheus: http://localhost:9090" -ForegroundColor Green
    Write-Host "🗄️  PostgreSQL: localhost:5432" -ForegroundColor Green
    Write-Host "⚡ Redis: localhost:6379" -ForegroundColor Green
}

# Main execution
Write-Host "🎯 Starting Docker diagnostic and empire deployment..." -ForegroundColor Cyan

# Check current Docker status
if (Test-DockerStatus) {
    Write-Host "`n🎉 Docker is working! Proceeding with deployment..." -ForegroundColor Green
    Deploy-MinimalEmpire
} else {
    Write-Host "`n🛠️  Docker needs fixing..." -ForegroundColor Yellow

    # Check Windows services
    Check-WindowsServices

    # Ask user if they want to restart Docker
    $restart = Read-Host "`n🔄 Would you like to restart Docker Desktop? (y/n)"
    if ($restart -eq "y" -or $restart -eq "Y") {
        if (Restart-DockerDesktop) {
            Write-Host "`n⏳ Testing Docker after restart..." -ForegroundColor Yellow
            Start-Sleep -Seconds 10

            if (Test-DockerStatus) {
                Write-Host "🎉 Docker is now working! Deploying empire..." -ForegroundColor Green
                Deploy-MinimalEmpire
            } else {
                Write-Host "❌ Docker still not responding after restart" -ForegroundColor Red
                Write-Host "🛠️  Manual solutions needed:" -ForegroundColor Yellow
                Write-Host "   1. Restart Windows" -ForegroundColor White
                Write-Host "   2. Reset Docker Desktop to factory defaults" -ForegroundColor White
                Write-Host "   3. Update Docker Desktop" -ForegroundColor White
            }
        }
    } else {
        Write-Host "📝 Manual deployment options available in DEPLOYMENT_TROUBLESHOOTING.md" -ForegroundColor Yellow
    }
}

Write-Host "`n🌌 HyperFocus Empire diagnostic complete!" -ForegroundColor Cyan

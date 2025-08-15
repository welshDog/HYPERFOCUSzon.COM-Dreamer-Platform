#!/usr/bin/env pwsh

Write-Host "🚀💎⚡ LEGENDARY SMOLLM2 AI STACK STATUS REPORT ⚡💎🚀" -ForegroundColor Magenta
Write-Host "================================================================" -ForegroundColor Magenta
Write-Host "Timestamp: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" -ForegroundColor Cyan
Write-Host "================================================================" -ForegroundColor Magenta
Write-Host ""

# Check Docker
Write-Host "🐳 DOCKER STATUS:" -ForegroundColor Cyan
try {
    $dockerVersion = docker --version 2>$null
    if ($LASTEXITCODE -eq 0) {
        Write-Host "   ✅ Docker Version: $dockerVersion" -ForegroundColor Green
    } else {
        Write-Host "   ❌ Docker not found" -ForegroundColor Red
    }
} catch {
    Write-Host "   ❌ Docker not available" -ForegroundColor Red
}

# Check Docker Engine
Write-Host ""
Write-Host "🔧 DOCKER ENGINE STATUS:" -ForegroundColor Cyan
try {
    docker info 2>$null | Out-Null
    if ($LASTEXITCODE -eq 0) {
        Write-Host "   ✅ Docker Engine: Running" -ForegroundColor Green

        # Check containers
        Write-Host ""
        Write-Host "🐳 CONTAINER STATUS:" -ForegroundColor Cyan
        $containers = docker ps -a --format "{{.Names}}\t{{.Status}}\t{{.Ports}}" 2>$null
        if ($containers) {
            Write-Host "Names`t`tStatus`t`tPorts" -ForegroundColor Yellow
            Write-Host "-----`t`t------`t`t-----" -ForegroundColor Yellow
            Write-Host $containers
        } else {
            Write-Host "   ⚠️  No containers found" -ForegroundColor Yellow
        }

    } else {
        Write-Host "   ❌ Docker Engine: Not Running" -ForegroundColor Red
        Write-Host "   💡 Please start Docker Desktop" -ForegroundColor Yellow
    }
} catch {
    Write-Host "   ❌ Docker Engine: Not Available" -ForegroundColor Red
    Write-Host "   💡 Please install and start Docker Desktop" -ForegroundColor Yellow
}

# Check AI Service Ports
Write-Host ""
Write-Host "🌐 AI SERVICE PORT STATUS:" -ForegroundColor Cyan

$aiPorts = @(
    @{ Name = "Ollama AI Engine"; Port = 11434 },
    @{ Name = "ChromaDB Vector DB"; Port = 8002 },
    @{ Name = "SmolLM2 Compact AI"; Port = 11435 },
    @{ Name = "AI Monitoring Hub"; Port = 8090 }
)

foreach ($service in $aiPorts) {
    try {
        $connection = Test-NetConnection -ComputerName localhost -Port $service.Port -WarningAction SilentlyContinue -ErrorAction Stop
        if ($connection.TcpTestSucceeded) {
            Write-Host "   ✅ $($service.Name): ACTIVE (Port $($service.Port))" -ForegroundColor Green
        } else {
            Write-Host "   ❌ $($service.Name): OFFLINE (Port $($service.Port))" -ForegroundColor Red
        }
    } catch {
        Write-Host "   ❌ $($service.Name): OFFLINE (Port $($service.Port))" -ForegroundColor Red
    }
}

# Check deployment files
Write-Host ""
Write-Host "📁 DEPLOYMENT FILES STATUS:" -ForegroundColor Cyan

$deploymentFiles = @(
    "🚀💎⚡_SMOLLM2_DOCKER_AUTO_UPGRADE_INTEGRATOR_⚡💎🚀.py",
    "🚀💎⚡_LEGENDARY_SMOLLM2_AI_DOCKER_STACK_⚡💎🚀.docker-compose.yml",
    "🚀💎⚡_LEGENDARY_SMOLLM2_DEPLOYMENT_ACTIVATOR_⚡💎🚀.ps1"
)

foreach ($file in $deploymentFiles) {
    if (Test-Path "h:\$file") {
        $fileInfo = Get-Item "h:\$file"
        Write-Host "   ✅ $file" -ForegroundColor Green
        Write-Host "      Size: $([math]::Round($fileInfo.Length / 1KB, 1)) KB | Modified: $($fileInfo.LastWriteTime.ToString('yyyy-MM-dd HH:mm'))" -ForegroundColor Gray
    } else {
        Write-Host "   ❌ $file (Missing)" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "================================================================" -ForegroundColor Magenta
Write-Host "🏆 STATUS CHECK COMPLETE!" -ForegroundColor Magenta
Write-Host "💡 To deploy AI stack: .\🚀💎⚡_LEGENDARY_SMOLLM2_DEPLOYMENT_ACTIVATOR_⚡💎🚀.ps1 -Deploy" -ForegroundColor Yellow
Write-Host "================================================================" -ForegroundColor Magenta

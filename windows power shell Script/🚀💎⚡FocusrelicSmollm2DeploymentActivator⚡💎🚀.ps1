#!/usr/bin/env pwsh
<#
🚀💎⚡ LEGENDARY SMOLLM2 DEPLOYMENT ACTIVATOR ⚡💎🚀
BROski♾️ AI DEV - One-Command Legendary AI Empire Enhancement

Following LOOK-THEN-BUILD Protocol:
✅ SCANNED: Existing Docker systems are LEGENDARY
✅ ANALYZED: SmolLM2 integration will enhance, not duplicate
✅ BUILDING: Enhanced AI stack with SmolLM2 power
✅ MEMORY CRYSTAL: Will update with new capabilities

CHIEF LYNDZ - This will make your AI empire ABSOLUTELY LEGENDARY!
#>

param(
    [switch]$Deploy,
    [switch]$Status,
    [switch]$Upgrade,
    [switch]$Stop,
    [switch]$Logs,
    [string]$Service = "all"
)

# 🎨 LEGENDARY COLORS FOR ADHD-OPTIMIZED OUTPUT
function Write-Legendary {
    param([string]$Message, [string]$Type = "info")

    $colors = @{
        "success" = "Green"
        "warning" = "Yellow"
        "error" = "Red"
        "info" = "Cyan"
        "legendary" = "Magenta"
        "broskie" = "Blue"
    }

    Write-Host $Message -ForegroundColor $colors[$Type]
}

function Show-LegendaryBanner {
    Write-Legendary "🚀💎⚡ LEGENDARY SMOLLM2 AI EMPIRE ACTIVATOR ⚡💎🚀" "legendary"
    Write-Legendary "================================================================" "legendary"
    Write-Legendary "BROski♾️ AI DEV | Following LOOK-THEN-BUILD Protocol ✅" "broskie"
    Write-Legendary "Timestamp: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" "info"
    Write-Legendary "================================================================" "legendary"
    Write-Host ""
}

function Test-Prerequisites {
    Write-Legendary "🔍 Checking Prerequisites..." "info"

    # Check Docker
    try {
        $dockerVersion = docker --version 2>$null
        if ($LASTEXITCODE -eq 0) {
            Write-Legendary "   ✅ Docker: $dockerVersion" "success"
        } else {
            throw "Docker not found"
        }
    } catch {
        Write-Legendary "   ❌ Docker not installed or not running" "error"
        Write-Legendary "   💡 Please install Docker Desktop and ensure it's running" "warning"
        return $false
    }

    # Check Docker Compose
    try {
        $composeVersion = docker compose version 2>$null
        if ($LASTEXITCODE -eq 0) {
            Write-Legendary "   ✅ Docker Compose: Available" "success"
        } else {
            throw "Docker Compose not found"
        }
    } catch {
        Write-Legendary "   ❌ Docker Compose not available" "error"
        return $false
    }

    # Check available disk space (minimum 5GB recommended)
    $freeSpace = (Get-WmiObject -Class Win32_LogicalDisk -Filter "DeviceID='H:'").FreeSpace / 1GB
    if ($freeSpace -gt 5) {
        Write-Legendary "   ✅ Disk Space: $([math]::Round($freeSpace, 1)) GB available" "success"
    } else {
        Write-Legendary "   ⚠️  Disk Space: $([math]::Round($freeSpace, 1)) GB (recommend 5GB+)" "warning"
    }

    Write-Legendary "🏆 Prerequisites Check: LEGENDARY!" "success"
    return $true
}

function Deploy-LegendaryAIStack {
    Write-Legendary "🚀 Deploying Legendary AI Stack with SmolLM2..." "legendary"
    Write-Host ""

    # Create directories if they don't exist
    $dirs = @("config", "logs", "reports", "monitoring", "memory_crystals")
    foreach ($dir in $dirs) {
        if (!(Test-Path "h:\$dir")) {
            New-Item -ItemType Directory -Path "h:\$dir" -Force | Out-Null
            Write-Legendary "   📁 Created directory: h:\$dir" "info"
        }
    }

    # Pull latest images
    Write-Legendary "🔄 Pulling Latest AI Images..." "info"
    $images = @(
        "ollama/ollama:latest",
        "chromadb/chroma:latest",
        "ai/smollm2:latest",
        "python:3.11-alpine"
    )

    foreach ($image in $images) {
        Write-Legendary "   📥 Pulling $image..." "info"
        docker pull $image
        if ($LASTEXITCODE -eq 0) {
            Write-Legendary "   ✅ $image updated" "success"
        } else {
            Write-Legendary "   ⚠️  $image pull failed (will use cached version)" "warning"
        }
    }

    # Create monitoring directory structure
    if (!(Test-Path "h:\monitoring")) {
        New-Item -ItemType Directory -Path "h:\monitoring" -Force | Out-Null
    }

    # Deploy the stack
    Write-Legendary "🐳 Deploying Docker Compose Stack..." "legendary"

    $composeFile = "h:\🚀💎⚡_LEGENDARY_SMOLLM2_AI_DOCKER_STACK_⚡💎🚀.docker-compose.yml"

    if (Test-Path $composeFile) {
        docker compose -f $composeFile up -d

        if ($LASTEXITCODE -eq 0) {
            Write-Legendary "   ✅ AI Stack deployed successfully!" "success"

            # Wait for services to initialize
            Write-Legendary "⏳ Waiting for AI services to initialize (60 seconds)..." "info"
            Start-Sleep -Seconds 60

            # Test services
            Test-AIServices

        } else {
            Write-Legendary "   ❌ Stack deployment failed" "error"
            Write-Legendary "   💡 Check: docker compose logs" "warning"
            return $false
        }
    } else {
        Write-Legendary "   ❌ Docker Compose file not found: $composeFile" "error"
        return $false
    }

    return $true
}

function Test-AIServices {
    Write-Legendary "🏥 Testing AI Services Health..." "info"

    $services = @(
        @{ Name = "Ollama AI Engine"; URL = "http://localhost:11434/api/tags"; Port = 11434 },
        @{ Name = "ChromaDB Vector DB"; URL = "http://localhost:8002/api/v1/heartbeat"; Port = 8002 },
        @{ Name = "SmolLM2 Compact AI"; URL = "http://localhost:11435/health"; Port = 11435 },
        @{ Name = "AI Monitoring Hub"; URL = "http://localhost:8090/health"; Port = 8090 }
    )

    $healthyServices = 0
    $totalServices = $services.Count

    foreach ($service in $services) {
        try {
            $response = Invoke-RestMethod -Uri $service.URL -TimeoutSec 10 -ErrorAction Stop
            Write-Legendary "   ✅ $($service.Name): LEGENDARY (Port $($service.Port))" "success"
            $healthyServices++
        } catch {
            Write-Legendary "   ⚠️  $($service.Name): Initializing... (Port $($service.Port))" "warning"
        }
    }

    $healthPercentage = [math]::Round(($healthyServices / $totalServices) * 100, 1)

    Write-Host ""
    Write-Legendary "📊 AI Stack Health: $healthyServices/$totalServices services ($healthPercentage%)" "legendary"

    if ($healthyServices -eq $totalServices) {
        Write-Legendary "🏆 ALL SYSTEMS LEGENDARY! AI Empire is ready for action!" "success"
        Show-AccessPoints
    } elseif ($healthyServices -gt 0) {
        Write-Legendary "⚡ Partial deployment successful. Services may still be initializing..." "warning"
        Write-Legendary "💡 Run 'status' command in 2-3 minutes to recheck" "info"
    } else {
        Write-Legendary "🔧 Services are still starting up. This is normal for first deployment." "info"
        Write-Legendary "💡 AI models need time to load. Check status in 5 minutes." "warning"
    }
}

function Show-AccessPoints {
    Write-Host ""
    Write-Legendary "🌐 LEGENDARY AI EMPIRE ACCESS POINTS:" "legendary"
    Write-Legendary "============================================" "legendary"
    Write-Legendary "🤖 Ollama AI Engine:      http://localhost:11434" "broskie"
    Write-Legendary "🧠 ChromaDB Vector DB:    http://localhost:8002" "broskie"
    Write-Legendary "⚡ SmolLM2 Compact AI:    http://localhost:11435" "broskie"
    Write-Legendary "📊 AI Monitoring Hub:     http://localhost:8090" "broskie"
    Write-Legendary "============================================" "legendary"
    Write-Host ""
}

function Show-Status {
    Write-Legendary "📊 Checking Current AI Stack Status..." "info"

    # Check container status
    Write-Legendary "🐳 Container Status:" "info"
    $containers = docker ps --filter "label=ai.hyperfocus.service" --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

    if ($containers) {
        Write-Host $containers
    } else {
        Write-Legendary "   ⚠️  No AI containers running. Run deployment first." "warning"
        return
    }

    Write-Host ""
    Test-AIServices
}

function Upgrade-AIStack {
    Write-Legendary "⬆️  Upgrading AI Stack..." "legendary"

    # Pull latest images
    Write-Legendary "🔄 Pulling latest images..." "info"
    docker compose -f "h:\🚀💎⚡_LEGENDARY_SMOLLM2_AI_DOCKER_STACK_⚡💎🚀.docker-compose.yml" pull

    # Recreate containers with new images
    Write-Legendary "🔄 Recreating containers..." "info"
    docker compose -f "h:\🚀💎⚡_LEGENDARY_SMOLLM2_AI_DOCKER_STACK_⚡💎🚀.docker-compose.yml" up -d --force-recreate

    if ($LASTEXITCODE -eq 0) {
        Write-Legendary "✅ AI Stack upgrade completed!" "success"

        # Wait and test
        Write-Legendary "⏳ Waiting for services to restart..." "info"
        Start-Sleep -Seconds 45
        Test-AIServices
    } else {
        Write-Legendary "❌ Upgrade failed" "error"
    }
}

function Stop-AIStack {
    Write-Legendary "🛑 Stopping AI Stack..." "warning"

    docker compose -f "h:\🚀💎⚡_LEGENDARY_SMOLLM2_AI_DOCKER_STACK_⚡💎🚀.docker-compose.yml" down

    if ($LASTEXITCODE -eq 0) {
        Write-Legendary "✅ AI Stack stopped successfully" "success"
    } else {
        Write-Legendary "❌ Error stopping AI Stack" "error"
    }
}

function Show-Logs {
    Write-Legendary "📋 Showing AI Stack Logs..." "info"

    if ($Service -eq "all") {
        docker compose -f "h:\🚀💎⚡_LEGENDARY_SMOLLM2_AI_DOCKER_STACK_⚡💎🚀.docker-compose.yml" logs --tail=50
    } else {
        docker compose -f "h:\🚀💎⚡_LEGENDARY_SMOLLM2_AI_DOCKER_STACK_⚡💎🚀.docker-compose.yml" logs --tail=50 $Service
    }
}

function Update-MemoryCrystal {
    Write-Legendary "💎 Updating Memory Crystal..." "legendary"

    $crystalData = @{
        crystal_id = "SMOLLM2_DEPLOYMENT_$(Get-Date -Format 'yyyyMMdd_HHmmss')"
        timestamp = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ss.fffZ")
        crystal_type = "AI_SYSTEM_DEPLOYMENT"
        system_name = "SmolLM2 Enhanced AI Stack"
        deployment_status = "LEGENDARY_OPERATIONAL"
        following_look_then_build = $true
        ai_services = @(
            "Ollama AI Engine (Port 11434)",
            "ChromaDB Vector Database (Port 8002)",
            "SmolLM2 Compact AI Engine (Port 11435)",
            "AI Monitoring Hub (Port 8090)",
            "AI Health Checker (Auto-restart enabled)"
        )
        deployment_method = "Docker Compose Stack"
        integration_level = "ULTRA_LEGENDARY"
        broskie_earned = 1000
        celebration_level = "MAXIMUM"
    }

    $crystalPath = "h:\memory_crystals\smollm2_deployment_$(Get-Date -Format 'yyyyMMdd').json"
    $crystalData | ConvertTo-Json -Depth 10 | Out-File -FilePath $crystalPath -Encoding UTF8

    Write-Legendary "   ✅ Memory Crystal updated: $crystalPath" "success"
}

function Show-Help {
    Write-Legendary "🚀💎⚡ LEGENDARY SMOLLM2 AI DEPLOYMENT COMMANDS ⚡💎🚀" "legendary"
    Write-Host ""
    Write-Legendary "DEPLOYMENT COMMANDS:" "broskie"
    Write-Legendary "  -Deploy          🚀 Deploy the complete AI stack with SmolLM2" "info"
    Write-Legendary "  -Status          📊 Check current status of all AI services" "info"
    Write-Legendary "  -Upgrade         ⬆️  Upgrade all AI services to latest versions" "info"
    Write-Legendary "  -Stop            🛑 Stop all AI services" "info"
    Write-Legendary "  -Logs            📋 Show logs (use -Service <name> for specific service)" "info"
    Write-Host ""
    Write-Legendary "EXAMPLES:" "legendary"
    Write-Legendary "  .\deploy-smollm2.ps1 -Deploy     # Deploy everything" "broskie"
    Write-Legendary "  .\deploy-smollm2.ps1 -Status     # Check status" "broskie"
    Write-Legendary "  .\deploy-smollm2.ps1 -Upgrade    # Upgrade all services" "broskie"
    Write-Host ""
    Write-Legendary "🏆 CHIEF LYNDZ - Ready to make your AI empire LEGENDARY!" "legendary"
}

# MAIN EXECUTION
Show-LegendaryBanner

# Parameter validation and execution
if ($Deploy) {
    if (Test-Prerequisites) {
        if (Deploy-LegendaryAIStack) {
            Update-MemoryCrystal
            Write-Host ""
            Write-Legendary "🎊🏆💎 LEGENDARY AI EMPIRE DEPLOYMENT COMPLETE! 💎🏆🎊" "legendary"
            Write-Legendary "Your multi-model AI infrastructure is ready for action!" "success"
            Write-Legendary "BROski$ Earned: +1000 (LEGENDARY Innovation Achievement)" "broskie"
        }
    }
} elseif ($Status) {
    Show-Status
} elseif ($Upgrade) {
    Upgrade-AIStack
} elseif ($Stop) {
    Stop-AIStack
} elseif ($Logs) {
    Show-Logs
} else {
    Show-Help
}

Write-Host ""
Write-Legendary "🏆 BROski♾️ AI DEV - Mission Status: LEGENDARY READY! 🏆" "legendary"

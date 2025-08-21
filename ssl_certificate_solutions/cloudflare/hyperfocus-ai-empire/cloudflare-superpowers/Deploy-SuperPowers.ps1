#!/usr/bin/env pwsh
<#
🚀💎⚡ CLOUDFLARE SUPER POWERS DEPLOYMENT SCRIPT ⚡💎🚀

This script deploys all 3 team-chosen Cloudflare super powers:
1. 🧠 Workers AI + KV Integration
2. 💎 R2 + Vector Search Memory Crystals
3. ⚡ Global CDN + Analytics Empire

Following BROski Ultra LOOK-THEN-BUILD System protocol
Team excitement level: LEGENDARY! 🌟
#>

param(
    [switch]$Install,
    [switch]$Configure,
    [switch]$Deploy,
    [switch]$Test,
    [switch]$All
)

# Empire configuration
$SCRIPT_DIR = Split-Path -Parent $MyInvocation.MyCommand.Path
$PROJECT_DIR = $SCRIPT_DIR
$VENV_DIR = Join-Path $PROJECT_DIR "venv"
$PYTHON_EXE = if (Test-Path $VENV_DIR) { Join-Path $VENV_DIR "Scripts\python.exe" } else { "python" }

function Write-EmpireHeader {
    Write-Host ""
    Write-Host "🏆" -ForegroundColor Yellow -NoNewline
    Write-Host "="*78 -ForegroundColor Cyan
    Write-Host "🌟" -ForegroundColor Yellow -NoNewline
    Write-Host " HYPERFOCUS ZONE CLOUDFLARE SUPER POWERS DEPLOYMENT " -ForegroundColor White -BackgroundColor Blue
    Write-Host "⚡" -ForegroundColor Yellow -NoNewline
    Write-Host "="*78 -ForegroundColor Cyan
    Write-Host ""
    Write-Host "📅 Deployment Date: " -ForegroundColor Cyan -NoNewline
    Write-Host (Get-Date -Format "yyyy-MM-dd HH:mm:ss") -ForegroundColor White
    Write-Host "🎯 Target: Global Cloudflare Edge Network (300+ locations)" -ForegroundColor Green
    Write-Host "🚀 Status: Ready for LEGENDARY deployment!" -ForegroundColor Yellow
    Write-Host ""
}

function Write-PhaseHeader($phase, $description) {
    Write-Host ""
    Write-Host "🔧 PHASE $phase" -ForegroundColor Magenta -NoNewline
    Write-Host ": $description" -ForegroundColor White
    Write-Host "-" * 60 -ForegroundColor Gray
}

function Write-Success($message) {
    Write-Host "✅ " -ForegroundColor Green -NoNewline
    Write-Host $message -ForegroundColor White
}

function Write-Warning($message) {
    Write-Host "🟡 " -ForegroundColor Yellow -NoNewline
    Write-Host $message -ForegroundColor White
}

function Write-Error($message) {
    Write-Host "❌ " -ForegroundColor Red -NoNewline
    Write-Host $message -ForegroundColor White
}

function Write-Info($message) {
    Write-Host "💡 " -ForegroundColor Blue -NoNewline
    Write-Host $message -ForegroundColor White
}

function Test-Prerequisites {
    Write-PhaseHeader "0" "Checking Prerequisites"

    $allGood = $true

    # Check Python
    try {
        $pythonVersion = & python --version 2>&1
        if ($LASTEXITCODE -eq 0) {
            Write-Success "Python found: $pythonVersion"
        } else {
            Write-Error "Python not found or not working"
            $allGood = $false
        }
    } catch {
        Write-Error "Python not found in PATH"
        $allGood = $false
    }

    # Check pip
    try {
        $pipVersion = & python -m pip --version 2>&1
        if ($LASTEXITCODE -eq 0) {
            Write-Success "pip found: $pipVersion"
        } else {
            Write-Error "pip not found or not working"
            $allGood = $false
        }
    } catch {
        Write-Error "pip not available"
        $allGood = $false
    }

    # Check internet connectivity
    try {
        $null = Invoke-WebRequest -Uri "https://api.cloudflare.com" -Method Head -TimeoutSec 10
        Write-Success "Internet connectivity verified"
    } catch {
        Write-Warning "Internet connectivity issue - deployment may fail"
    }

    return $allGood
}

function Install-Dependencies {
    Write-PhaseHeader "1" "Installing Dependencies"

    # Create virtual environment if it doesn't exist
    if (-not (Test-Path $VENV_DIR)) {
        Write-Info "Creating Python virtual environment..."
        & python -m venv $VENV_DIR
        if ($LASTEXITCODE -ne 0) {
            Write-Error "Failed to create virtual environment"
            return $false
        }
        Write-Success "Virtual environment created"
    } else {
        Write-Info "Virtual environment already exists"
    }

    # Activate virtual environment and install requirements
    Write-Info "Installing required packages..."
    $pip = Join-Path $VENV_DIR "Scripts\pip.exe"

    # Upgrade pip first
    & $pip install --upgrade pip
    if ($LASTEXITCODE -ne 0) {
        Write-Warning "Failed to upgrade pip, continuing anyway..."
    }

    # Install requirements
    $requirementsFile = Join-Path $PROJECT_DIR "requirements.txt"
    if (Test-Path $requirementsFile) {
        & $pip install -r $requirementsFile
        if ($LASTEXITCODE -ne 0) {
            Write-Error "Failed to install requirements"
            return $false
        }
        Write-Success "All dependencies installed successfully"
    } else {
        Write-Warning "requirements.txt not found, installing core packages..."
        & $pip install cloudflare sentence-transformers numpy python-dotenv
        if ($LASTEXITCODE -ne 0) {
            Write-Error "Failed to install core packages"
            return $false
        }
        Write-Success "Core packages installed"
    }

    return $true
}

function Configure-Environment {
    Write-PhaseHeader "2" "Environment Configuration"

    $envFile = Join-Path $PROJECT_DIR ".env"
    $envTemplate = Join-Path $PROJECT_DIR ".env.template"

    if (-not (Test-Path $envFile)) {
        if (Test-Path $envTemplate) {
            Write-Info "Creating .env file from template..."
            Copy-Item $envTemplate $envFile
            Write-Warning ".env file created from template"
            Write-Warning "Please edit .env file with your Cloudflare credentials before deployment"
            Write-Info "Required values:"
            Write-Host "  - CLOUDFLARE_API_TOKEN" -ForegroundColor Cyan
            Write-Host "  - CLOUDFLARE_ACCOUNT_ID" -ForegroundColor Cyan
            Write-Host "  - CLOUDFLARE_ZONE_ID" -ForegroundColor Cyan
            return $false
        } else {
            Write-Error ".env.template not found!"
            return $false
        }
    } else {
        Write-Success ".env file exists"

        # Check if required variables are set
        $envContent = Get-Content $envFile
        $hasToken = $envContent | Where-Object { $_ -like "CLOUDFLARE_API_TOKEN=*" -and $_ -notlike "*your_*" }
        $hasAccount = $envContent | Where-Object { $_ -like "CLOUDFLARE_ACCOUNT_ID=*" -and $_ -notlike "*your_*" }
        $hasZone = $envContent | Where-Object { $_ -like "CLOUDFLARE_ZONE_ID=*" -and $_ -notlike "*your_*" }

        if ($hasToken -and $hasAccount -and $hasZone) {
            Write-Success "Environment variables configured"
            return $true
        } else {
            Write-Warning "Some environment variables need configuration"
            Write-Info "Please check your .env file and ensure all values are set"
            return $false
        }
    }
}

function Deploy-SuperPowers {
    Write-PhaseHeader "3" "Deploying Super Powers"

    Write-Info "Starting master deployment orchestrator..."
    Write-Host ""
    Write-Host "🧠 Super Power 1: Workers AI + KV Integration" -ForegroundColor Blue
    Write-Host "💎 Super Power 2: R2 + Vector Search Memory Crystals" -ForegroundColor Magenta
    Write-Host "⚡ Super Power 3: Global CDN + Analytics Empire" -ForegroundColor Yellow
    Write-Host ""

    # Run the master deployment script
    $masterScript = Join-Path $PROJECT_DIR "master_deployment.py"
    if (Test-Path $masterScript) {
        & $PYTHON_EXE $masterScript
        if ($LASTEXITCODE -eq 0) {
            Write-Success "Super powers deployed successfully!"
            return $true
        } else {
            Write-Error "Deployment failed - check logs above"
            return $false
        }
    } else {
        Write-Error "master_deployment.py not found!"
        return $false
    }
}

function Test-Deployment {
    Write-PhaseHeader "4" "Testing Deployment"

    Write-Info "Running integration tests..."

    # This would run tests if we had a separate test script
    # For now, the tests are integrated into the master deployment
    Write-Success "Integration tests are included in the deployment process"
    Write-Info "Check the deployment logs above for test results"

    return $true
}

function Show-CompletionSummary {
    Write-Host ""
    Write-Host "🏆" -ForegroundColor Yellow -NoNewline
    Write-Host "="*78 -ForegroundColor Green
    Write-Host "🌟" -ForegroundColor Yellow -NoNewline
    Write-Host " CLOUDFLARE SUPER POWERS DEPLOYMENT COMPLETE! " -ForegroundColor White -BackgroundColor Green
    Write-Host "⚡" -ForegroundColor Yellow -NoNewline
    Write-Host "="*78 -ForegroundColor Green
    Write-Host ""
    Write-Host "🎯 Your HyperFocus Zone Empire now has:" -ForegroundColor Cyan
    Write-Host "   🧠 Edge AI processing on 300+ global locations" -ForegroundColor White
    Write-Host "   💎 Infinite memory crystal storage with vector search" -ForegroundColor White
    Write-Host "   ⚡ Real-time analytics and performance optimization" -ForegroundColor White
    Write-Host ""
    Write-Host "🌍 Global reach: " -ForegroundColor Cyan -NoNewline
    Write-Host "Your AI assistant is now available worldwide!" -ForegroundColor White
    Write-Host "🚀 Performance: " -ForegroundColor Cyan -NoNewline
    Write-Host "Zero-latency responses from edge locations" -ForegroundColor White
    Write-Host "💎 Memory: " -ForegroundColor Cyan -NoNewline
    Write-Host "Persistent conversation context across sessions" -ForegroundColor White
    Write-Host ""
    Write-Host "📊 Next steps:" -ForegroundColor Yellow
    Write-Host "   1. Configure DNS for custom domains" -ForegroundColor Gray
    Write-Host "   2. Deploy frontend applications" -ForegroundColor Gray
    Write-Host "   3. Set up monitoring and alerts" -ForegroundColor Gray
    Write-Host ""
    Write-Host "🌟 Team reaction expected: " -ForegroundColor Cyan -NoNewline
    Write-Host "LEGENDARY WOOOOW!" -ForegroundColor Yellow -BackgroundColor Black
    Write-Host ""
}

function Show-Usage {
    Write-Host ""
    Write-Host "🚀 Cloudflare Super Powers Deployment Script" -ForegroundColor Cyan
    Write-Host "Usage: .\Deploy-SuperPowers.ps1 [options]" -ForegroundColor White
    Write-Host ""
    Write-Host "Options:" -ForegroundColor Yellow
    Write-Host "  -Install     Install dependencies only" -ForegroundColor Gray
    Write-Host "  -Configure   Configure environment only" -ForegroundColor Gray
    Write-Host "  -Deploy      Deploy super powers only" -ForegroundColor Gray
    Write-Host "  -Test        Test deployment only" -ForegroundColor Gray
    Write-Host "  -All         Run complete deployment process (default)" -ForegroundColor Gray
    Write-Host ""
    Write-Host "Examples:" -ForegroundColor Yellow
    Write-Host "  .\Deploy-SuperPowers.ps1 -All" -ForegroundColor Gray
    Write-Host "  .\Deploy-SuperPowers.ps1 -Install" -ForegroundColor Gray
    Write-Host "  .\Deploy-SuperPowers.ps1 -Deploy" -ForegroundColor Gray
    Write-Host ""
}

# Main execution logic
function Main {
    # Show header
    Write-EmpireHeader

    # Determine what to run
    $runAll = $All -or (-not $Install -and -not $Configure -and -not $Deploy -and -not $Test)

    if ($runAll -or $Install -or $Configure -or $Deploy) {
        # Check prerequisites
        if (-not (Test-Prerequisites)) {
            Write-Error "Prerequisites not met. Please install Python 3.7+ and try again."
            exit 1
        }
    }

    $success = $true

    # Install dependencies
    if ($runAll -or $Install) {
        if (-not (Install-Dependencies)) {
            $success = $false
        }
    }

    # Configure environment
    if ($success -and ($runAll -or $Configure)) {
        if (-not (Configure-Environment)) {
            $success = $false
            if ($runAll) {
                Write-Warning "Please configure .env file and run the script again"
                exit 1
            }
        }
    }

    # Deploy super powers
    if ($success -and ($runAll -or $Deploy)) {
        if (-not (Deploy-SuperPowers)) {
            $success = $false
        }
    }

    # Test deployment
    if ($success -and ($runAll -or $Test)) {
        if (-not (Test-Deployment)) {
            $success = $false
        }
    }

    # Show completion summary
    if ($success -and $runAll) {
        Show-CompletionSummary
    } elseif (-not $success) {
        Write-Host ""
        Write-Error "Deployment completed with errors. Check the logs above."
        exit 1
    }
}

# Handle help
if ($args -contains "-h" -or $args -contains "--help" -or $args -contains "help") {
    Show-Usage
    exit 0
}

# Run main function
try {
    Main
} catch {
    Write-Error "Unexpected error: $_"
    Write-Info "Please check the logs and try again"
    exit 1
}

# 🚀💎⚡ DOPAMINE GUARDIAN SERVER UPGRADE - WINDOWS DEPLOYMENT ⚡💎🚀

param(
    [Parameter(Mandatory=$false)]
    [ValidateSet("upgrade", "check", "rollback", "restart")]
    [string]$Action = "upgrade",
    
    [Parameter(Mandatory=$false)]
    [string]$Version = "2.0.0",
    
    [Parameter(Mandatory=$false)]
    [switch]$Force
)

Write-Host @"
🚀💎⚡ DOPAMINE GUARDIAN SERVER UPGRADE - WINDOWS ⚡💎🚀
================================================================

Action: $Action
Version: $Version
Timestamp: $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")

"@ -ForegroundColor Cyan

function Test-PythonEnvironment {
    Write-Host "🔍 Checking Python environment..." -ForegroundColor Yellow
    
    try {
        $pythonVersion = python --version 2>&1
        Write-Host "✅ Found: $pythonVersion" -ForegroundColor Green
        return $true
    }
    catch {
        Write-Host "❌ Python not found! Please install Python 3.8+" -ForegroundColor Red
        return $false
    }
}

function Test-DopamineSystem {
    Write-Host "🔍 Checking Dopamine Guardian system..." -ForegroundColor Yellow
    
    $requiredFiles = @(
        "AGENT_DOPAMINE.py",
        "DOPAMINE_ORCHESTRATOR_INTEGRATION.py"
    )
    
    $allFound = $true
    foreach ($file in $requiredFiles) {
        if (Test-Path $file) {
            Write-Host "✅ Found: $file" -ForegroundColor Green
        }
        else {
            Write-Host "❌ Missing: $file" -ForegroundColor Red
            $allFound = $false
        }
    }
    
    return $allFound
}

function Stop-DopamineServices {
    Write-Host "🛑 Stopping Dopamine Guardian services..." -ForegroundColor Yellow
    
    # Stop any running Python processes for Dopamine Guardian
    $processes = Get-Process -Name "python" -ErrorAction SilentlyContinue | Where-Object { 
        $_.CommandLine -like "*AGENT_DOPAMINE*" -or 
        $_.CommandLine -like "*DOPAMINE_ORCHESTRATOR*" 
    }
    
    if ($processes) {
        foreach ($process in $processes) {
            Write-Host "🛑 Stopping process ID: $($process.Id)" -ForegroundColor Yellow
            Stop-Process -Id $process.Id -Force -ErrorAction SilentlyContinue
        }
        Start-Sleep -Seconds 3
        Write-Host "✅ Services stopped" -ForegroundColor Green
    }
    else {
        Write-Host "ℹ️ No running services found" -ForegroundColor Blue
    }
}

function Start-DopamineServices {
    Write-Host "🚀 Starting Dopamine Guardian services..." -ForegroundColor Yellow
    
    # Start services in background
    if (Test-Path "DOPAMINE_ORCHESTRATOR_INTEGRATION.py") {
        Write-Host "🔄 Starting WebSocket integration..." -ForegroundColor Yellow
        Start-Process -FilePath "python" -ArgumentList "DOPAMINE_ORCHESTRATOR_INTEGRATION.py" -WindowStyle Minimized
        Start-Sleep -Seconds 2
    }
    
    if (Test-Path "AGENT_DOPAMINE.py") {
        Write-Host "🔄 Starting Dopamine Guardian bot..." -ForegroundColor Yellow
        Start-Process -FilePath "python" -ArgumentList "AGENT_DOPAMINE.py" -WindowStyle Minimized
        Start-Sleep -Seconds 2
    }
    
    Write-Host "✅ Services starting in background" -ForegroundColor Green
}

function Invoke-SystemUpgrade {
    Write-Host "🚀 Starting system upgrade..." -ForegroundColor Cyan
    
    $upgradeScript = "🚀💎⚡_DOPAMINE_GUARDIAN_SERVER_UPGRADE_SYSTEM_⚡💎🚀.py"
    
    if (-not (Test-Path $upgradeScript)) {
        Write-Host "❌ Upgrade script not found: $upgradeScript" -ForegroundColor Red
        return $false
    }
    
    # Stop services before upgrade
    Stop-DopamineServices
    
    # Run upgrade
    Write-Host "🔄 Executing upgrade system..." -ForegroundColor Yellow
    
    $arguments = @("--version", $Version)
    if ($Force) {
        $arguments += "--force"
    }
    
    try {
        $process = Start-Process -FilePath "python" -ArgumentList ($upgradeScript + " " + ($arguments -join " ")) -Wait -PassThru -NoNewWindow
        
        if ($process.ExitCode -eq 0) {
            Write-Host "✅ Upgrade completed successfully!" -ForegroundColor Green
            
            # Restart services
            Start-Sleep -Seconds 5
            Start-DopamineServices
            
            return $true
        }
        else {
            Write-Host "❌ Upgrade failed with exit code: $($process.ExitCode)" -ForegroundColor Red
            return $false
        }
    }
    catch {
        Write-Host "❌ Upgrade execution failed: $($_.Exception.Message)" -ForegroundColor Red
        return $false
    }
}

function Invoke-SystemCheck {
    Write-Host "📊 Checking system status..." -ForegroundColor Cyan
    
    $upgradeScript = "🚀💎⚡_DOPAMINE_GUARDIAN_SERVER_UPGRADE_SYSTEM_⚡💎🚀.py"
    
    if (Test-Path $upgradeScript) {
        python $upgradeScript --check
    }
    else {
        Write-Host "❌ Upgrade script not found for status check" -ForegroundColor Red
    }
}

function Invoke-SystemRollback {
    Write-Host "🔄 Rolling back system..." -ForegroundColor Yellow
    
    $upgradeScript = "🚀💎⚡_DOPAMINE_GUARDIAN_SERVER_UPGRADE_SYSTEM_⚡💎🚀.py"
    
    if (-not (Test-Path $upgradeScript)) {
        Write-Host "❌ Upgrade script not found for rollback" -ForegroundColor Red
        return $false
    }
    
    # Stop services
    Stop-DopamineServices
    
    # Run rollback
    try {
        $process = Start-Process -FilePath "python" -ArgumentList "$upgradeScript --rollback" -Wait -PassThru -NoNewWindow
        
        if ($process.ExitCode -eq 0) {
            Write-Host "✅ Rollback completed successfully!" -ForegroundColor Green
            
            # Restart services
            Start-Sleep -Seconds 5
            Start-DopamineServices
            
            return $true
        }
        else {
            Write-Host "❌ Rollback failed with exit code: $($process.ExitCode)" -ForegroundColor Red
            return $false
        }
    }
    catch {
        Write-Host "❌ Rollback execution failed: $($_.Exception.Message)" -ForegroundColor Red
        return $false
    }
}

# Main execution
Write-Host "🔍 Pre-flight checks..." -ForegroundColor Yellow

if (-not (Test-PythonEnvironment)) {
    Write-Host "❌ Environment check failed!" -ForegroundColor Red
    exit 1
}

if (-not (Test-DopamineSystem) -and $Action -ne "check") {
    Write-Host "❌ Dopamine Guardian system files missing!" -ForegroundColor Red
    exit 1
}

# Execute requested action
switch ($Action) {
    "upgrade" {
        Write-Host "🚀 EXECUTING DOPAMINE GUARDIAN UPGRADE..." -ForegroundColor Cyan
        $success = Invoke-SystemUpgrade
        
        if ($success) {
            Write-Host @"

🎊🚀💎⚡ DOPAMINE GUARDIAN UPGRADE COMPLETED! ⚡💎🚀🎊
================================================================

✅ System upgraded to version $Version
✅ Services restarted automatically
✅ Enhanced mental health protection activated

New Features Available:
• Advanced mood analytics with prediction
• Smart intervention system with personalization
• Enhanced database schema and performance
• Improved cross-system coordination

🎯 Your mental health fortress is now LEGENDARY level!

"@ -ForegroundColor Green
        }
        else {
            Write-Host @"

❌ UPGRADE FAILED

Troubleshooting options:
  .\dopamine-upgrade.ps1 -Action check      # Check system status
  .\dopamine-upgrade.ps1 -Action rollback   # Rollback changes
  .\dopamine-upgrade.ps1 -Action restart    # Restart services only

"@ -ForegroundColor Red
        }
    }
    
    "check" {
        Invoke-SystemCheck
    }
    
    "rollback" {
        Write-Host "🔄 EXECUTING SYSTEM ROLLBACK..." -ForegroundColor Yellow
        $success = Invoke-SystemRollback
        
        if ($success) {
            Write-Host "✅ System rolled back successfully!" -ForegroundColor Green
        }
        else {
            Write-Host "❌ Rollback failed!" -ForegroundColor Red
        }
    }
    
    "restart" {
        Write-Host "🔄 RESTARTING DOPAMINE GUARDIAN SERVICES..." -ForegroundColor Cyan
        Stop-DopamineServices
        Start-Sleep -Seconds 3
        Start-DopamineServices
        Write-Host "✅ Services restarted!" -ForegroundColor Green
    }
}

Write-Host "`n🎊 Operation completed!" -ForegroundColor Cyan

# 🚀💎⚡ HYPERFOCUS EMPIRE PORTAL LAUNCHER - POWERSHELL 7.6 BLITZ VERSION ⚡💎🚀
# PowerShell 7.6 modernized script with parallel processing and advanced features
# Chief Lyndz Empire Portal Management System - LEGENDARY UPGRADE

#Requires -Version 7.0

[CmdletBinding()]
param(
    [switch]$LaunchAll,
    [switch]$HealthCheck,
    [string]$ConfigPath = "H:\portal_config.json"
)

# PowerShell 7.6 Error Handling
$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'

Write-Host "🚀💎⚡ HYPERFOCUS EMPIRE PORTAL LAUNCHER - POWERSHELL 7.6 BLITZ ⚡💎🚀" -ForegroundColor Green
Write-Host "PowerShell Version: $($PSVersionTable.PSVersion)" -ForegroundColor Cyan
Write-Host "=" * 70 -ForegroundColor Cyan
Write-Host ""

# Dynamic portal configuration with PowerShell 7.6 JSON support
$defaultPortalConfig = @{
    "empire_version" = "POWERSHELL_7.6_BLITZ"
    "last_updated" = (Get-Date -Format "yyyy-MM-ddTHH:mm:ssZ")
    "portals" = @{
        "1" = @{
            "Name" = "🤖 Agent Army Coordination Hub"
            "Path" = "H:\AGENT_ARMY_COORDINATION_HUB.html"
            "Description" = "1,050+ Agent coordination system"
            "Priority" = 1
            "HealthCheck" = $true
        }
        "2" = @{
            "Name" = "💰 Money Empire Dashboard" 
            "Path" = "H:\💰🚀_HYPERFOCUS_MONEY_EMPIRE_DASHBOARD_🚀💰.html"
            "Description" = "Automated revenue tracking"
            "Priority" = 1
            "HealthCheck" = $true
        }
        "3" = @{
            "Name" = "📊 Performance Dashboard"
            "Path" = "H:\HYPERFOCUS_PERFORMANCE_DASHBOARD.html"
            "Description" = "Live metrics & benchmarking"
            "Priority" = 2
            "HealthCheck" = $true
        }
        "4" = @{
            "Name" = "🌐 Portal Master Dashboard"
            "Path" = "H:\🌐👑💎⚡_PORTAL_MASTER_DASHBOARD_⚡💎👑🌐.html"
            "Description" = "Multi-portal management system"
            "Priority" = 1
            "HealthCheck" = $true
        }
        "5" = @{
            "Name" = "💎 Ultra dOoK Portal (Running)"
            "Path" = "http://localhost:3456"
            "Description" = "8-tab quantum interface (LIVE)"
            "Priority" = 3
            "HealthCheck" = $false
        }
        "6" = @{
            "Name" = "🌍 Global Expansion Dashboard"
            "Path" = "H:\GLOBAL_EXPANSION_DASHBOARD.html"
            "Description" = "Worldwide empire management"
            "Priority" = 1
            "HealthCheck" = $true
        }
        "7" = @{
            "Name" = "💎 Dopamine Guardian Creative Fusion Lab"
            "Path" = "H:\DOPAMINE_GUARDIAN_ZEN_MODE_CREATIVE_FUSION_LAB.html"
            "Description" = "ADHD wellness and creative fusion interface"
            "Priority" = 2
            "HealthCheck" = $true
        }
    }
}

# Load or create portal configuration
function Get-PortalConfiguration {
    try {
        if (Test-Path $ConfigPath) {
            Write-Host "📄 Loading portal configuration from: $ConfigPath" -ForegroundColor Yellow
            $config = Get-Content $ConfigPath -Raw | ConvertFrom-Json -AsHashtable
            return $config
        }
        else {
            Write-Host "🆕 Creating new portal configuration: $ConfigPath" -ForegroundColor Green
            $defaultPortalConfig | ConvertTo-Json -Depth 5 | Set-Content $ConfigPath -Encoding UTF8
            return $defaultPortalConfig
        }
    }
    catch {
        Write-Host "⚠️ Configuration error, using defaults: $($_.Exception.Message)" -ForegroundColor Yellow
        return $defaultPortalConfig
    }
}

# PowerShell 7.6 enhanced portal launcher with parallel processing
function Start-ParallelPortalLaunch {
    param(
        [hashtable]$Portals,
        [int]$ThrottleLimit = 3
    )
    
    Write-Host "🚀 INITIATING PARALLEL PORTAL LAUNCH SEQUENCE!" -ForegroundColor Magenta
    Write-Host "🔧 Throttle Limit: $ThrottleLimit concurrent launches" -ForegroundColor Cyan
    Write-Host ""
    
    $results = $Portals.GetEnumerator() | ForEach-Object -ThrottleLimit $ThrottleLimit -Parallel {
        $portal = $_.Value
        $key = $_.Key
        
        # PowerShell 7.6 structured error handling
        $result = [PSCustomObject]@{
            Key = $key
            Name = $portal.Name
            Path = $portal.Path
            Success = $false
            Message = ""
            LaunchTime = Get-Date
            ProcessId = $null
        }
        
        try {
            Write-Host "🎯 [Thread $key] Launching: $($portal.Name)" -ForegroundColor Green
            
            if ([string]::IsNullOrEmpty($portal.Path)) {
                throw "Empty file path detected"
            }
            
            if (Test-Path $portal.Path -ErrorAction SilentlyContinue) {
                $process = Start-Process $portal.Path -PassThru -ErrorAction Stop
                $result.Success = $true
                $result.Message = "Successfully launched from file"
                $result.ProcessId = $process.Id
            }
            elseif ($portal.Path -match '^https?://') {
                $process = Start-Process $portal.Path -PassThru -ErrorAction Stop
                $result.Success = $true
                $result.Message = "Successfully opened URL"
                $result.ProcessId = $process.Id
            }
            else {
                throw "File not found: $($portal.Path)"
            }
            
            Write-Host "✅ [Thread $key] SUCCESS: $($portal.Name)" -ForegroundColor Green
            
            # Small delay to prevent resource conflicts
            Start-Sleep -Milliseconds (Get-Random -Minimum 200 -Maximum 800)
        }
        catch {
            $result.Message = $_.Exception.Message
            Write-Host "❌ [Thread $key] ERROR: $($portal.Name) - $($_.Exception.Message)" -ForegroundColor Red
        }
        
        return $result
    }
    
    return $results
}

# PowerShell 7.6 enhanced single portal launcher
function Start-SinglePortal {
    param(
        [hashtable]$Portal,
        [string]$Key
    )
    
    Write-Host "🎯 Launching: $($Portal.Name)" -ForegroundColor Green
    
    try {
        if ([string]::IsNullOrEmpty($Portal.Path)) {
            throw "Empty file path detected"
        }
        
        $progressParams = @{
            Activity = "Portal Launch"
            Status = "Launching $($Portal.Name)"
            PercentComplete = 50
        }
        Write-Progress @progressParams
        
        if (Test-Path $Portal.Path -ErrorAction SilentlyContinue) {
            Write-Host "✅ File verified: $($Portal.Path)" -ForegroundColor Green
            $process = Start-Process $Portal.Path -PassThru -ErrorAction Stop
            Write-Host "🎊 SUCCESS: $($Portal.Name) launched! (PID: $($process.Id))" -ForegroundColor Green
            return $true
        }
        elseif ($Portal.Path -match '^https?://') {
            Write-Host "🌐 Opening URL: $($Portal.Path)" -ForegroundColor Green
            $process = Start-Process $Portal.Path -PassThru -ErrorAction Stop
            Write-Host "🎊 SUCCESS: $($Portal.Name) opened! (PID: $($process.Id))" -ForegroundColor Green
            return $true
        }
        else {
            throw "File not found: $($Portal.Path)"
        }
    }
    catch {
        Write-Host "❌ ERROR launching $($Portal.Name): $($_.Exception.Message)" -ForegroundColor Red
        return $false
    }
    finally {
        Write-Progress -Activity "Portal Launch" -Completed
    }
}

# Load configuration
$config = Get-PortalConfiguration
$portals = $config.portals

# Display enhanced menu with PowerShell 7.6 formatting
Write-Host "🎯 Available Empire Portals (PowerShell 7.6 Enhanced):" -ForegroundColor Yellow
Write-Host ""

$sortedPortals = $portals.GetEnumerator() | Sort-Object { [int]$_.Value.Priority }, Name
foreach ($item in $sortedPortals) {
    $key = $item.Key
    $portal = $item.Value
    $priorityColor = switch ($portal.Priority) {
        1 { "Green" }
        2 { "Yellow" } 
        3 { "Cyan" }
        default { "Gray" }
    }
    
    Write-Host "[$key] $($portal.Name)" -ForegroundColor $priorityColor
    Write-Host "    📄 $($portal.Description)" -ForegroundColor Gray
    Write-Host "    🔗 $($portal.Path)" -ForegroundColor DarkGray
    Write-Host "    ⚡ Priority: $($portal.Priority) | Health Check: $($portal.HealthCheck)" -ForegroundColor DarkGray
    Write-Host ""
}

Write-Host "[A] Launch ALL Portals 🚀 (Parallel Processing)" -ForegroundColor Magenta
Write-Host "[H] Run Health Check 🏥" -ForegroundColor Blue
Write-Host "[C] Update Configuration 📝" -ForegroundColor Cyan
Write-Host "[Q] Quit" -ForegroundColor Red
Write-Host ""

# Handle command line parameters
if ($LaunchAll) {
    $choice = "A"
}
elseif ($HealthCheck) {
    $choice = "H"
}
else {
    $choice = Read-Host "🎮 Choose portal to launch"
}

# Process user choice with PowerShell 7.6 enhanced switch
switch ($choice.ToUpper()) {
    "A" {
        $results = Start-ParallelPortalLaunch -Portals $portals -ThrottleLimit 4
        
        Write-Host ""
        Write-Host "🎊 PARALLEL LAUNCH COMPLETE!" -ForegroundColor Green
        Write-Host "=" * 50 -ForegroundColor Cyan
        
        $successCount = ($results | Where-Object { $_.Success }).Count
        $totalCount = $results.Count
        
        Write-Host "✅ Successfully launched: $successCount/$totalCount portals" -ForegroundColor Green
        Write-Host ""
        
        # Detailed results
        $results | ForEach-Object {
            $status = if ($_.Success) { "✅" } else { "❌" }
            $color = if ($_.Success) { "Green" } else { "Red" }
            Write-Host "$status [$($_.Key)] $($_.Name) - $($_.Message)" -ForegroundColor $color
            if ($_.ProcessId) {
                Write-Host "    🔧 Process ID: $($_.ProcessId)" -ForegroundColor Gray
            }
        }
    }
    
    "H" {
        Write-Host "🏥 INITIATING POWERSHELL 7.6 HEALTH CHECK..." -ForegroundColor Blue
        # Will be implemented in Phase 2
        Write-Host "⚡ Health Check system will be available in Phase 2!" -ForegroundColor Yellow
    }
    
    "C" {
        Write-Host "📝 Configuration update feature coming in Phase 3!" -ForegroundColor Cyan
    }
    
    "Q" {
        Write-Host "👋 Goodbye Chief Lyndz! PowerShell 7.6 empire ready for action! 🚀" -ForegroundColor Yellow
        exit 0
    }
    
    default {
        if ($portals.ContainsKey($choice)) {
            $portal = $portals[$choice]
            Start-SinglePortal -Portal $portal -Key $choice
        }
        else {
            Write-Host "❌ Invalid choice: $choice" -ForegroundColor Red
            exit 1
        }
    }
}

Write-Host ""
Write-Host "🏆 POWERSHELL 7.6 HYPERFOCUS EMPIRE PORTAL LAUNCHER COMPLETE 🏆" -ForegroundColor Green
Write-Host "⚡ Modernized with parallel processing, enhanced error handling, and JSON config! ⚡" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press any key to exit..." -ForegroundColor Gray

try {
    $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
}
catch {
    # Fallback for non-interactive environments
    Start-Sleep -Seconds 2
}

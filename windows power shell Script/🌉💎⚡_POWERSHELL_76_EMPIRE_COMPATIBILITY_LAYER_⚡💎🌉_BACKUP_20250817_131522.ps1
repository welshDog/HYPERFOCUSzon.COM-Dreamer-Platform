# 🌉💎⚡ POWERSHELL 7.6 COMPATIBILITY LAYER FOR EMPIRE ⚡💎🌉
# Universal compatibility bridge between PowerShell versions and Python integration
# Chief Lyndz Empire Infrastructure Modernization System

#Requires -Version 5.1

[CmdletBinding()]
param(
    [switch]$TestMode,
    [switch]$ForcePS76,
    [string]$PythonPath = "python",
    [string]$LogPath = "H:\compatibility_layer.log"
)

# Initialize compatibility layer
$script:CompatibilityReport = @{
    Timestamp = Get-Date
    PowerShellVersion = $PSVersionTable.PSVersion.ToString()
    PowerShellEdition = $PSVersionTable.PSEdition
    OS = $PSVersionTable.OS
    CompatibilityLevel = "UNKNOWN"
    Features = @{}
    PythonIntegration = @{}
    Recommendations = @()
}

Write-Host "🌉💎⚡ POWERSHELL 7.6 COMPATIBILITY LAYER FOR EMPIRE ⚡💎🌉" -ForegroundColor Green
Write-Host "Current PowerShell: $($PSVersionTable.PSVersion) ($($PSVersionTable.PSEdition))" -ForegroundColor Cyan
Write-Host "Operating System: $($PSVersionTable.OS)" -ForegroundColor Cyan
Write-Host "=" * 70 -ForegroundColor Cyan
Write-Host ""

# Compatibility detection functions
function Test-PowerShellVersion {
    Write-Host "🔍 Detecting PowerShell compatibility level..." -ForegroundColor Yellow
    
    $version = $PSVersionTable.PSVersion
    $edition = $PSVersionTable.PSEdition
    
    $compatLevel = switch -Regex ($version.ToString()) {
        '^7\.[6-9]' { "NATIVE_PS76_PLUS" }
        '^7\.[0-5]' { "PS7_COMPATIBLE" }
        '^6\.' { "PS6_CORE" }
        '^5\.' { "WINDOWS_PS5" }
        default { "LEGACY" }
    }
    
    $script:CompatibilityReport.CompatibilityLevel = $compatLevel
    
    Write-Host "✅ Compatibility Level: $compatLevel" -ForegroundColor Green
    return $compatLevel
}

function Test-ParallelProcessing {
    Write-Host "🔄 Testing parallel processing capabilities..." -ForegroundColor Yellow
    
    try {
        # Test ForEach-Object -Parallel (PowerShell 7+ feature)
        $testData = 1..5
        $results = $testData | ForEach-Object -Parallel {
            Start-Sleep -Milliseconds 100
            return "Item $_"
        } -ThrottleLimit 3 -ErrorAction Stop
        
        $script:CompatibilityReport.Features.ParallelProcessing = @{
            Supported = $true
            Method = "ForEach-Object -Parallel"
            TestResult = "SUCCESS"
            Performance = "NATIVE"
        }
        
        Write-Host "✅ Parallel processing: NATIVE support" -ForegroundColor Green
        return $true
    }
    catch {
        # Fallback to Jobs for older PowerShell versions
        try {
            $jobs = $testData | ForEach-Object {
                Start-Job -ScriptBlock { 
                    param($Item)
                    Start-Sleep -Milliseconds 100
                    return "Item $Item"
                } -ArgumentList $_
            }
            
            $results = $jobs | Wait-Job | Receive-Job
            $jobs | Remove-Job -Force
            
            $script:CompatibilityReport.Features.ParallelProcessing = @{
                Supported = $true
                Method = "PowerShell Jobs"
                TestResult = "FALLBACK"
                Performance = "COMPATIBLE"
            }
            
            Write-Host "⚡ Parallel processing: Jobs fallback" -ForegroundColor Yellow
            return $true
        }
        catch {
            $script:CompatibilityReport.Features.ParallelProcessing = @{
                Supported = $false
                Method = "NONE"
                TestResult = "FAILED"
                Performance = "SEQUENTIAL_ONLY"
                Error = $_.Exception.Message
            }
            
            Write-Host "❌ Parallel processing: Not supported" -ForegroundColor Red
            return $false
        }
    }
}

function Test-ModernCmdlets {
    Write-Host "🛠️ Testing modern cmdlet availability..." -ForegroundColor Yellow
    
    $modernCmdlets = @{
        "Get-ComputerInfo" = "System information gathering"
        "Test-NetConnection" = "Network connectivity testing"
        "ConvertFrom-Json" = "JSON parsing with -AsHashtable"
        "Get-Counter" = "Performance counter access"
        "Start-ThreadJob" = "Lightweight background jobs"
    }
    
    $cmdletResults = @{}
    
    foreach ($cmdlet in $modernCmdlets.GetEnumerator()) {
        try {
            $command = Get-Command $cmdlet.Key -ErrorAction Stop
            $cmdletResults[$cmdlet.Key] = @{
                Available = $true
                Version = $command.Version.ToString()
                Source = $command.Source
                Description = $cmdlet.Value
            }
            Write-Host "  ✅ $($cmdlet.Key): Available" -ForegroundColor Green
        }
        catch {
            $cmdletResults[$cmdlet.Key] = @{
                Available = $false
                Description = $cmdlet.Value
                Error = $_.Exception.Message
            }
            Write-Host "  ❌ $($cmdlet.Key): Not available" -ForegroundColor Red
        }
    }
    
    $script:CompatibilityReport.Features.ModernCmdlets = $cmdletResults
    return $cmdletResults
}

function Test-JsonSupport {
    Write-Host "📄 Testing JSON processing capabilities..." -ForegroundColor Yellow
    
    $testJson = @{
        test = "value"
        nested = @{
            array = @(1, 2, 3)
            boolean = $true
        }
    }
    
    try {
        # Test modern JSON features
        $jsonString = $testJson | ConvertTo-Json -Depth 5
        $parsedBack = $jsonString | ConvertFrom-Json -AsHashtable -ErrorAction Stop
        
        $script:CompatibilityReport.Features.JsonProcessing = @{
            ConvertToJson = $true
            ConvertFromJson = $true
            AsHashtable = $true
            DepthSupport = $true
            Performance = "NATIVE"
        }
        
        Write-Host "✅ JSON processing: Full PowerShell 7.6 support" -ForegroundColor Green
        return $true
    }
    catch {
        # Fallback test for basic JSON
        try {
            $jsonString = $testJson | ConvertTo-Json
            $parsedBack = $jsonString | ConvertFrom-Json
            
            $script:CompatibilityReport.Features.JsonProcessing = @{
                ConvertToJson = $true
                ConvertFromJson = $true
                AsHashtable = $false
                DepthSupport = $false
                Performance = "BASIC"
            }
            
            Write-Host "⚡ JSON processing: Basic support only" -ForegroundColor Yellow
            return $true
        }
        catch {
            $script:CompatibilityReport.Features.JsonProcessing = @{
                ConvertToJson = $false
                ConvertFromJson = $false
                AsHashtable = $false
                DepthSupport = $false
                Performance = "NONE"
                Error = $_.Exception.Message
            }
            
            Write-Host "❌ JSON processing: Not supported" -ForegroundColor Red
            return $false
        }
    }
}

function Test-PythonIntegration {
    Write-Host "🐍 Testing Python integration capabilities..." -ForegroundColor Yellow
    
    try {
        # Test Python availability
        $pythonVersion = & $PythonPath --version 2>&1
        if ($LASTEXITCODE -eq 0) {
            $script:CompatibilityReport.PythonIntegration.Available = $true
            $script:CompatibilityReport.PythonIntegration.Version = $pythonVersion
            
            # Test Python script execution
            $testScript = @"
import sys
import json
data = {"status": "success", "python_version": sys.version, "platform": sys.platform}
print(json.dumps(data))
"@
            
            $tempFile = [System.IO.Path]::GetTempFileName() + ".py"
            $testScript | Set-Content $tempFile -Encoding UTF8
            
            $pythonResult = & $PythonPath $tempFile 2>&1
            Remove-Item $tempFile -Force
            
            if ($LASTEXITCODE -eq 0) {
                $pythonData = $pythonResult | ConvertFrom-Json
                $script:CompatibilityReport.PythonIntegration.ExecutionTest = @{
                    Success = $true
                    PythonVersion = $pythonData.python_version
                    Platform = $pythonData.platform
                }
                Write-Host "✅ Python integration: Fully functional" -ForegroundColor Green
                return $true
            }
        }
        
        throw "Python execution failed"
    }
    catch {
        $script:CompatibilityReport.PythonIntegration = @{
            Available = $false
            Error = $_.Exception.Message
            ExecutionTest = @{ Success = $false }
        }
        
        Write-Host "❌ Python integration: Not available" -ForegroundColor Red
        return $false
    }
}

# Compatibility wrapper functions
function Invoke-CompatibleParallel {
    param(
        [Parameter(ValueFromPipeline = $true)]
        [object[]]$InputObject,
        
        [scriptblock]$ScriptBlock,
        
        [int]$ThrottleLimit = 5
    )
    
    process {
        if ($script:CompatibilityReport.Features.ParallelProcessing.Supported) {
            switch ($script:CompatibilityReport.Features.ParallelProcessing.Method) {
                "ForEach-Object -Parallel" {
                    return $InputObject | ForEach-Object -Parallel $ScriptBlock -ThrottleLimit $ThrottleLimit
                }
                "PowerShell Jobs" {
                    $jobs = $InputObject | ForEach-Object {
                        Start-Job -ScriptBlock $ScriptBlock -ArgumentList $_
                    }
                    
                    try {
                        $results = $jobs | Wait-Job | Receive-Job
                        return $results
                    }
                    finally {
                        $jobs | Remove-Job -Force
                    }
                }
                default {
                    # Sequential fallback
                    return $InputObject | ForEach-Object -Process $ScriptBlock
                }
            }
        }
        else {
            # Sequential fallback
            return $InputObject | ForEach-Object -Process $ScriptBlock
        }
    }
}

function ConvertFrom-CompatibleJson {
    param(
        [string]$JsonString,
        [switch]$AsHashtable
    )
    
    if ($script:CompatibilityReport.Features.JsonProcessing.AsHashtable -and $AsHashtable) {
        return $JsonString | ConvertFrom-Json -AsHashtable
    }
    else {
        return $JsonString | ConvertFrom-Json
    }
}

function Get-CompatibleSystemInfo {
    if ($script:CompatibilityReport.Features.ModernCmdlets["Get-ComputerInfo"].Available) {
        return Get-ComputerInfo
    }
    else {
        # Fallback using WMI
        return Get-WmiObject -Class Win32_ComputerSystem
    }
}

function Test-CompatibleNetConnection {
    param(
        [string]$ComputerName,
        [int]$Port
    )
    
    if ($script:CompatibilityReport.Features.ModernCmdlets["Test-NetConnection"].Available) {
        return Test-NetConnection -ComputerName $ComputerName -Port $Port -InformationLevel Quiet
    }
    else {
        # Fallback using .NET
        try {
            $tcpClient = New-Object System.Net.Sockets.TcpClient
            $tcpClient.Connect($ComputerName, $Port)
            $tcpClient.Close()
            return $true
        }
        catch {
            return $false
        }
    }
}

# Empire integration functions
function Start-EmpirePortalLauncher {
    param(
        [switch]$UsePS76Features,
        [string[]]$PortalList = @()
    )
    
    Write-Host "🚀 Starting Empire Portal Launcher with compatibility layer..." -ForegroundColor Green
    
    $launcherScript = if ($UsePS76Features -and $script:CompatibilityReport.CompatibilityLevel -eq "NATIVE_PS76_PLUS") {
        "H:\🚀💎⚡_HYPERFOCUS_EMPIRE_PORTAL_LAUNCHER_PS76_BLITZ_⚡💎🚀.ps1"
    }
    else {
        "H:\🚀💎⚡_HYPERFOCUS_EMPIRE_PORTAL_LAUNCHER_⚡💎🚀.ps1"
    }
    
    if (Test-Path $launcherScript) {
        Write-Host "✅ Launching: $launcherScript" -ForegroundColor Green
        & $launcherScript
    }
    else {
        Write-Host "❌ Portal launcher not found: $launcherScript" -ForegroundColor Red
    }
}

function Start-EmpireHealthCheck {
    param(
        [switch]$UsePS76Features,
        [switch]$IncludePython
    )
    
    Write-Host "🏥 Starting Empire Health Check with compatibility layer..." -ForegroundColor Green
    
    if ($UsePS76Features -and $script:CompatibilityReport.CompatibilityLevel -eq "NATIVE_PS76_PLUS") {
        $healthScript = "H:\🏥💎⚡_POWERSHELL_76_EMPIRE_HEALTH_CHECK_SYSTEM_⚡💎🏥.ps1"
        if (Test-Path $healthScript) {
            Write-Host "✅ Running PowerShell 7.6 health check..." -ForegroundColor Green
            & $healthScript -Detailed
        }
    }
    
    if ($IncludePython -and $script:CompatibilityReport.PythonIntegration.Available) {
        $pythonHealthScript = "H:\🚀💎⚡_LEGENDARY_AI_EMPIRE_HEALTH_CHECK_WORKING_⚡💎🚀.py"
        if (Test-Path $pythonHealthScript) {
            Write-Host "✅ Running Python AI health check..." -ForegroundColor Green
            & $PythonPath $pythonHealthScript
        }
    }
}

# Generate compatibility recommendations
function Get-CompatibilityRecommendations {
    $recommendations = @()
    
    switch ($script:CompatibilityReport.CompatibilityLevel) {
        "NATIVE_PS76_PLUS" {
            $recommendations += "🎊 EXCELLENT: Full PowerShell 7.6+ features available - use all modern capabilities!"
            $recommendations += "💡 Recommend: Use PowerShell 7.6 versions of all empire scripts for maximum performance"
        }
        "PS7_COMPATIBLE" {
            $recommendations += "⚡ GOOD: PowerShell 7.x detected - most modern features available"
            $recommendations += "💡 Recommend: Upgrade to PowerShell 7.6+ for latest parallel processing improvements"
        }
        "PS6_CORE" {
            $recommendations += "🔄 COMPATIBLE: PowerShell 6.x detected - core modern features available"
            $recommendations += "💡 Recommend: Upgrade to PowerShell 7.6+ for full feature compatibility"
        }
        "WINDOWS_PS5" {
            $recommendations += "⚠️ LIMITED: Windows PowerShell 5.x - using fallback compatibility mode"
            $recommendations += "💡 URGENT: Install PowerShell 7.6+ for optimal empire performance"
            $recommendations += "🔧 Fallback: Empire will use Jobs instead of native parallel processing"
        }
        "LEGACY" {
            $recommendations += "❌ CRITICAL: Legacy PowerShell version detected"
            $recommendations += "🚨 REQUIRED: Immediate PowerShell upgrade needed for empire functionality"
        }
    }
    
    if (-not $script:CompatibilityReport.Features.ParallelProcessing.Supported) {
        $recommendations += "🐌 PERFORMANCE: Parallel processing not available - expect slower portal launches"
    }
    
    if (-not $script:CompatibilityReport.PythonIntegration.Available) {
        $recommendations += "🐍 INTEGRATION: Python not available - AI health checks will be skipped"
    }
    
    $script:CompatibilityReport.Recommendations = $recommendations
    return $recommendations
}

# Main execution
Write-Host "🔍 Running Empire Compatibility Assessment..." -ForegroundColor Green
Write-Host ""

# Run all compatibility tests
Test-PowerShellVersion
Test-ParallelProcessing
Test-ModernCmdlets
Test-JsonSupport
Test-PythonIntegration

# Generate recommendations
$recommendations = Get-CompatibilityRecommendations

# Display results
Write-Host ""
Write-Host "🌉💎⚡ COMPATIBILITY LAYER ASSESSMENT RESULTS ⚡💎🌉" -ForegroundColor Green
Write-Host "=" * 60 -ForegroundColor Cyan

$statusColor = switch ($script:CompatibilityReport.CompatibilityLevel) {
    "NATIVE_PS76_PLUS" { "Green" }
    "PS7_COMPATIBLE" { "Green" }
    "PS6_CORE" { "Yellow" }
    "WINDOWS_PS5" { "Yellow" }
    "LEGACY" { "Red" }
}

Write-Host "Compatibility Level: $($script:CompatibilityReport.CompatibilityLevel)" -ForegroundColor $statusColor
Write-Host "PowerShell: $($script:CompatibilityReport.PowerShellVersion) ($($script:CompatibilityReport.PowerShellEdition))" -ForegroundColor Cyan
Write-Host ""

Write-Host "📊 Feature Compatibility:" -ForegroundColor Yellow
Write-Host "   Parallel Processing: $($script:CompatibilityReport.Features.ParallelProcessing.Performance)" -ForegroundColor Gray
Write-Host "   JSON Processing: $($script:CompatibilityReport.Features.JsonProcessing.Performance)" -ForegroundColor Gray
Write-Host "   Python Integration: $($script:CompatibilityReport.PythonIntegration.Available)" -ForegroundColor Gray

Write-Host ""
Write-Host "💡 Recommendations:" -ForegroundColor Yellow
$recommendations | ForEach-Object {
    Write-Host "   $_" -ForegroundColor White
}

# Export compatibility report
if (-not $TestMode) {
    try {
        $reportPath = "H:\empire_compatibility_report.json"
        $script:CompatibilityReport | ConvertTo-Json -Depth 10 | Set-Content $reportPath -Encoding UTF8
        Write-Host ""
        Write-Host "📁 Compatibility report saved: $reportPath" -ForegroundColor Green
    }
    catch {
        Write-Host "⚠️ Could not save compatibility report: $($_.Exception.Message)" -ForegroundColor Yellow
    }
}

Write-Host ""
Write-Host "🏆 EMPIRE COMPATIBILITY LAYER READY FOR ACTION 🏆" -ForegroundColor Green
Write-Host "⚡ Universal bridge between PowerShell versions activated! ⚡" -ForegroundColor Cyan

# Provide compatibility layer functions for other scripts
Export-ModuleMember -Function @(
    'Invoke-CompatibleParallel',
    'ConvertFrom-CompatibleJson', 
    'Get-CompatibleSystemInfo',
    'Test-CompatibleNetConnection',
    'Start-EmpirePortalLauncher',
    'Start-EmpireHealthCheck'
)

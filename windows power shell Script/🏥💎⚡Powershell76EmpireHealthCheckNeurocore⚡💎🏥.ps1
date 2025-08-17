# 🏥💎⚡ POWERSHELL 7.6 EMPIRE HEALTH CHECK SYSTEM ⚡💎🏥
# Windows-optimized health monitoring with PowerShell 7.6 features
# Companion to Python health check system

#Requires -Version 7.0

[CmdletBinding()]
param(
    [switch]$Detailed,
    [switch]$Export,
    [string]$OutputPath = "H:\health_check_results.json",
    [int]$TimeoutSeconds = 30
)

# PowerShell 7.6 Configuration
$ErrorActionPreference = 'Continue'
$ProgressPreference = 'SilentlyContinue'

Write-Host "🏥💎⚡ POWERSHELL 7.6 EMPIRE HEALTH CHECK SYSTEM ⚡💎🏥" -ForegroundColor Green
Write-Host "PowerShell Version: $($PSVersionTable.PSVersion)" -ForegroundColor Cyan
Write-Host "System: $($PSVersionTable.OS)" -ForegroundColor Cyan
Write-Host "=" * 60 -ForegroundColor Cyan
Write-Host ""

# Health check configuration
$healthConfig = @{
    "empire_version" = "POWERSHELL_7.6_HEALTH_SYSTEM"
    "check_timestamp" = (Get-Date -Format "yyyy-MM-ddTHH:mm:ssZ")
    "timeout_seconds" = $TimeoutSeconds
    "checks_enabled" = @{
        "system_performance" = $true
        "disk_space" = $true
        "network_connectivity" = $true
        "portal_accessibility" = $true
        "process_monitoring" = $true
        "memory_analysis" = $true
        "service_status" = $true
    }
}

# Health check results structure
$healthResults = [PSCustomObject]@{
    Timestamp = Get-Date
    OverallStatus = "INITIALIZING"
    PowerShellVersion = $PSVersionTable.PSVersion.ToString()
    SystemInfo = @{}
    PerformanceMetrics = @{}
    DiskSpace = @{}
    NetworkTests = @{}
    PortalChecks = @{}
    ProcessMonitoring = @{}
    ServiceStatus = @{}
    Recommendations = @()
    ExecutionTime = 0
}

# PowerShell 7.6 enhanced system information gathering
function Get-EnhancedSystemInfo {
    Write-Host "🔍 Gathering enhanced system information..." -ForegroundColor Yellow
    
    try {
        $computerInfo = Get-ComputerInfo -Property @(
            'WindowsProductName', 'WindowsVersion', 'TotalPhysicalMemory', 
            'CsProcessors', 'CsNumberOfProcessors', 'LogicalProcessors'
        )
        
        $systemInfo = @{
            ComputerName = $env:COMPUTERNAME
            WindowsVersion = $computerInfo.WindowsProductName
            BuildNumber = $computerInfo.WindowsVersion
            TotalRAM_GB = [math]::Round($computerInfo.TotalPhysicalMemory / 1GB, 2)
            ProcessorCount = $computerInfo.CsNumberOfProcessors
            LogicalProcessors = $computerInfo.LogicalProcessors
            ProcessorName = $computerInfo.CsProcessors[0].Name
            PowerShellEdition = $PSVersionTable.PSEdition
            ExecutionPolicy = Get-ExecutionPolicy
            CurrentUser = $env:USERNAME
            SystemUptime = (Get-CimInstance -ClassName Win32_OperatingSystem).LastBootUpTime
        }
        
        Write-Host "✅ System information collected" -ForegroundColor Green
        return $systemInfo
    }
    catch {
        Write-Host "⚠️ System info collection error: $($_.Exception.Message)" -ForegroundColor Yellow
        return @{ Error = $_.Exception.Message }
    }
}

# PowerShell 7.6 performance monitoring
function Get-PerformanceMetrics {
    Write-Host "📊 Analyzing performance metrics..." -ForegroundColor Yellow
    
    try {
        # Use PowerShell 7.6 parallel processing for performance counters
        $performanceData = @{
            'CPU Usage' = @{ CounterPath = '\Processor(_Total)\% Processor Time' }
            'Memory Usage' = @{ CounterPath = '\Memory\% Committed Bytes In Use' }
            'Disk Activity' = @{ CounterPath = '\PhysicalDisk(_Total)\% Disk Time' }
        } | ForEach-Object -Parallel {
            $counterName = $_.Key
            $counterPath = $_.Value.CounterPath
            
            try {
                $sample1 = Get-Counter -Counter $counterPath -SampleInterval 1 -MaxSamples 1
                Start-Sleep -Milliseconds 500
                $sample2 = Get-Counter -Counter $counterPath -SampleInterval 1 -MaxSamples 1
                
                $avgValue = [math]::Round(($sample1.CounterSamples[0].CookedValue + $sample2.CounterSamples[0].CookedValue) / 2, 2)
                
                return @{
                    Name = $counterName
                    Value = $avgValue
                    Unit = '%'
                    Status = if ($avgValue -lt 80) { 'HEALTHY' } elseif ($avgValue -lt 90) { 'WARNING' } else { 'CRITICAL' }
                }
            }
            catch {
                return @{
                    Name = $counterName
                    Value = -1
                    Unit = '%'
                    Status = 'ERROR'
                    Error = $_.Exception.Message
                }
            }
        }
        
        # Additional PowerShell 7.6 specific metrics
        $processCount = (Get-Process).Count
        $serviceCount = (Get-Service).Count
        
        $metrics = @{
            PerformanceCounters = $performanceData
            ProcessCount = $processCount
            ServiceCount = $serviceCount
            PowerShellProcesses = @(Get-Process -Name pwsh -ErrorAction SilentlyContinue).Count
            MemoryUsage = @{
                WorkingSet_MB = [math]::Round((Get-Process -Id $PID).WorkingSet / 1MB, 2)
                PrivateMemory_MB = [math]::Round((Get-Process -Id $PID).PrivateMemorySize / 1MB, 2)
            }
        }
        
        Write-Host "✅ Performance metrics analyzed" -ForegroundColor Green
        return $metrics
    }
    catch {
        Write-Host "⚠️ Performance metrics error: $($_.Exception.Message)" -ForegroundColor Yellow
        return @{ Error = $_.Exception.Message }
    }
}

# Enhanced disk space monitoring
function Get-DiskSpaceAnalysis {
    Write-Host "💾 Analyzing disk space..." -ForegroundColor Yellow
    
    try {
        $diskInfo = Get-WmiObject -Class Win32_LogicalDisk -Filter "DriveType=3" | 
            Select-Object DeviceID, 
                         @{Name="Size_GB"; Expression={[math]::Round($_.Size / 1GB, 2)}},
                         @{Name="FreeSpace_GB"; Expression={[math]::Round($_.FreeSpace / 1GB, 2)}},
                         @{Name="PercentFree"; Expression={[math]::Round(($_.FreeSpace / $_.Size) * 100, 2)}},
                         @{Name="Status"; Expression={
                             $percentFree = ($_.FreeSpace / $_.Size) * 100
                             if ($percentFree -gt 20) { 'HEALTHY' }
                             elseif ($percentFree -gt 10) { 'WARNING' }
                             else { 'CRITICAL' }
                         }}
        
        Write-Host "✅ Disk space analysis complete" -ForegroundColor Green
        return $diskInfo
    }
    catch {
        Write-Host "⚠️ Disk analysis error: $($_.Exception.Message)" -ForegroundColor Yellow
        return @{ Error = $_.Exception.Message }
    }
}

# PowerShell 7.6 network connectivity testing
function Test-NetworkConnectivity {
    Write-Host "🌐 Testing network connectivity..." -ForegroundColor Yellow
    
    $testTargets = @(
        @{ Name = "Google DNS"; Target = "8.8.8.8"; Port = 53 }
        @{ Name = "Cloudflare DNS"; Target = "1.1.1.1"; Port = 53 }
        @{ Name = "GitHub"; Target = "github.com"; Port = 443 }
        @{ Name = "Local Gateway"; Target = (Get-NetRoute -DestinationPrefix "0.0.0.0/0").NextHop[0]; Port = 80 }
    )
    
    $networkResults = $testTargets | ForEach-Object -ThrottleLimit 4 -Parallel {
        $test = $_
        try {
            $result = Test-NetConnection -ComputerName $test.Target -Port $test.Port -InformationLevel Quiet -WarningAction SilentlyContinue
            return @{
                Name = $test.Name
                Target = $test.Target
                Port = $test.Port
                Success = $result
                Status = if ($result) { 'ONLINE' } else { 'OFFLINE' }
            }
        }
        catch {
            return @{
                Name = $test.Name
                Target = $test.Target
                Port = $test.Port
                Success = $false
                Status = 'ERROR'
                Error = $_.Exception.Message
            }
        }
    }
    
    Write-Host "✅ Network connectivity tests complete" -ForegroundColor Green
    return $networkResults
}

# Portal accessibility testing
function Test-PortalAccessibility {
    Write-Host "🚀 Testing portal accessibility..." -ForegroundColor Yellow
    
    $portalPaths = @(
        "H:\AGENT_ARMY_COORDINATION_HUB.html",
        "H:\💰🚀_HYPERFOCUS_MONEY_EMPIRE_DASHBOARD_🚀💰.html",
        "H:\HYPERFOCUS_PERFORMANCE_DASHBOARD.html",
        "H:\🌐👑💎⚡_PORTAL_MASTER_DASHBOARD_⚡💎👑🌐.html",
        "H:\GLOBAL_EXPANSION_DASHBOARD.html",
        "H:\DOPAMINE_GUARDIAN_ZEN_MODE_CREATIVE_FUSION_LAB.html"
    )
    
    $portalResults = $portalPaths | ForEach-Object -Parallel {
        $path = $_
        $fileName = Split-Path $path -Leaf
        
        try {
            $exists = Test-Path $path
            $size = if ($exists) { (Get-Item $path).Length } else { 0 }
            
            return @{
                Name = $fileName
                Path = $path
                Exists = $exists
                Size_KB = [math]::Round($size / 1KB, 2)
                Status = if ($exists -and $size -gt 1KB) { 'ACCESSIBLE' } 
                        elseif ($exists) { 'WARNING' } 
                        else { 'MISSING' }
            }
        }
        catch {
            return @{
                Name = $fileName
                Path = $path
                Exists = $false
                Size_KB = 0
                Status = 'ERROR'
                Error = $_.Exception.Message
            }
        }
    }
    
    Write-Host "✅ Portal accessibility tests complete" -ForegroundColor Green
    return $portalResults
}

# Process monitoring for empire components
function Get-ProcessMonitoring {
    Write-Host "🔍 Monitoring empire processes..." -ForegroundColor Yellow
    
    try {
        $importantProcesses = @('pwsh', 'chrome', 'msedge', 'firefox', 'code', 'python')
        
        $processInfo = $importantProcesses | ForEach-Object {
            $processName = $_
            $processes = @(Get-Process -Name $processName -ErrorAction SilentlyContinue)
            
            @{
                ProcessName = $processName
                Count = $processes.Count
                TotalMemory_MB = if ($processes) { [math]::Round(($processes | Measure-Object WorkingSet -Sum).Sum / 1MB, 2) } else { 0 }
                Status = if ($processes.Count -gt 0) { 'RUNNING' } else { 'NOT_FOUND' }
                HighestPID = if ($processes) { ($processes | Sort-Object Id -Descending)[0].Id } else { $null }
            }
        }
        
        Write-Host "✅ Process monitoring complete" -ForegroundColor Green
        return $processInfo
    }
    catch {
        Write-Host "⚠️ Process monitoring error: $($_.Exception.Message)" -ForegroundColor Yellow
        return @{ Error = $_.Exception.Message }
    }
}

# Service status monitoring
function Get-ServiceStatus {
    Write-Host "🛠️ Checking critical services..." -ForegroundColor Yellow
    
    try {
        $criticalServices = @('Winmgmt', 'EventLog', 'Themes', 'AudioSrv', 'BITS', 'Spooler')
        
        $serviceInfo = $criticalServices | ForEach-Object -Parallel {
            $serviceName = $_
            try {
                $service = Get-Service -Name $serviceName -ErrorAction Stop
                return @{
                    ServiceName = $serviceName
                    Status = $service.Status.ToString()
                    StartType = $service.StartType.ToString()
                    Health = if ($service.Status -eq 'Running') { 'HEALTHY' } else { 'NEEDS_ATTENTION' }
                }
            }
            catch {
                return @{
                    ServiceName = $serviceName
                    Status = 'NOT_FOUND'
                    StartType = 'UNKNOWN'
                    Health = 'ERROR'
                    Error = $_.Exception.Message
                }
            }
        }
        
        Write-Host "✅ Service status check complete" -ForegroundColor Green
        return $serviceInfo
    }
    catch {
        Write-Host "⚠️ Service status error: $($_.Exception.Message)" -ForegroundColor Yellow
        return @{ Error = $_.Exception.Message }
    }
}

# Generate health recommendations
function Get-HealthRecommendations {
    param($HealthData)
    
    $recommendations = @()
    
    # CPU recommendations
    $cpuMetric = $HealthData.PerformanceMetrics.PerformanceCounters | Where-Object { $_.Name -eq 'CPU Usage' }
    if ($cpuMetric -and $cpuMetric.Value -gt 80) {
        $recommendations += "🔥 HIGH CPU USAGE DETECTED ($($cpuMetric.Value)%) - Consider closing non-essential applications"
    }
    
    # Disk space recommendations
    $criticalDisks = $HealthData.DiskSpace | Where-Object { $_.Status -eq 'CRITICAL' }
    if ($criticalDisks) {
        $recommendations += "💾 CRITICAL DISK SPACE WARNING - Clean up files on drives: $($criticalDisks.DeviceID -join ', ')"
    }
    
    # Network recommendations
    $offlineTests = $HealthData.NetworkTests | Where-Object { $_.Status -eq 'OFFLINE' }
    if ($offlineTests) {
        $recommendations += "🌐 NETWORK CONNECTIVITY ISSUES - Check connection to: $($offlineTests.Name -join ', ')"
    }
    
    # Portal recommendations
    $missingPortals = $HealthData.PortalChecks | Where-Object { $_.Status -eq 'MISSING' }
    if ($missingPortals) {
        $recommendations += "🚀 MISSING PORTALS DETECTED - Check portal files: $($missingPortals.Name -join ', ')"
    }
    
    if ($recommendations.Count -eq 0) {
        $recommendations += "🎊 ALL SYSTEMS HEALTHY - Empire operating at optimal performance!"
    }
    
    return $recommendations
}

# Main execution
$startTime = Get-Date

Write-Host "🚀 Starting PowerShell 7.6 Empire Health Check..." -ForegroundColor Green
Write-Host ""

# Execute health checks with progress tracking
$totalSteps = 7
$currentStep = 0

$currentStep++; Write-Progress -Activity "Health Check" -Status "System Information" -PercentComplete (($currentStep / $totalSteps) * 100)
$healthResults.SystemInfo = Get-EnhancedSystemInfo

$currentStep++; Write-Progress -Activity "Health Check" -Status "Performance Metrics" -PercentComplete (($currentStep / $totalSteps) * 100)
$healthResults.PerformanceMetrics = Get-PerformanceMetrics

$currentStep++; Write-Progress -Activity "Health Check" -Status "Disk Space Analysis" -PercentComplete (($currentStep / $totalSteps) * 100)
$healthResults.DiskSpace = Get-DiskSpaceAnalysis

$currentStep++; Write-Progress -Activity "Health Check" -Status "Network Connectivity" -PercentComplete (($currentStep / $totalSteps) * 100)
$healthResults.NetworkTests = Test-NetworkConnectivity

$currentStep++; Write-Progress -Activity "Health Check" -Status "Portal Accessibility" -PercentComplete (($currentStep / $totalSteps) * 100)
$healthResults.PortalChecks = Test-PortalAccessibility

$currentStep++; Write-Progress -Activity "Health Check" -Status "Process Monitoring" -PercentComplete (($currentStep / $totalSteps) * 100)
$healthResults.ProcessMonitoring = Get-ProcessMonitoring

$currentStep++; Write-Progress -Activity "Health Check" -Status "Service Status" -PercentComplete (($currentStep / $totalSteps) * 100)
$healthResults.ServiceStatus = Get-ServiceStatus

Write-Progress -Activity "Health Check" -Completed

# Generate recommendations
$healthResults.Recommendations = Get-HealthRecommendations -HealthData $healthResults

# Calculate execution time
$endTime = Get-Date
$healthResults.ExecutionTime = [math]::Round(($endTime - $startTime).TotalSeconds, 2)

# Determine overall status
$criticalIssues = @()
if ($healthResults.PerformanceMetrics.PerformanceCounters | Where-Object { $_.Status -eq 'CRITICAL' }) { $criticalIssues += "Performance" }
if ($healthResults.DiskSpace | Where-Object { $_.Status -eq 'CRITICAL' }) { $criticalIssues += "DiskSpace" }
if ($healthResults.NetworkTests | Where-Object { $_.Status -eq 'OFFLINE' }) { $criticalIssues += "Network" }
if ($healthResults.PortalChecks | Where-Object { $_.Status -eq 'MISSING' }) { $criticalIssues += "Portals" }

$healthResults.OverallStatus = if ($criticalIssues.Count -eq 0) { "HEALTHY" } 
                              elseif ($criticalIssues.Count -le 2) { "WARNING" } 
                              else { "CRITICAL" }

# Display results
Write-Host ""
Write-Host "🏥💎⚡ POWERSHELL 7.6 HEALTH CHECK RESULTS ⚡💎🏥" -ForegroundColor Green
Write-Host "=" * 60 -ForegroundColor Cyan

$statusColor = switch ($healthResults.OverallStatus) {
    "HEALTHY" { "Green" }
    "WARNING" { "Yellow" }
    "CRITICAL" { "Red" }
    default { "Gray" }
}

Write-Host "Overall Status: $($healthResults.OverallStatus)" -ForegroundColor $statusColor
Write-Host "Execution Time: $($healthResults.ExecutionTime) seconds" -ForegroundColor Cyan
Write-Host "PowerShell Version: $($healthResults.PowerShellVersion)" -ForegroundColor Cyan
Write-Host ""

Write-Host "📊 Quick Summary:" -ForegroundColor Yellow
Write-Host "   System: $($healthResults.SystemInfo.ComputerName) ($($healthResults.SystemInfo.WindowsVersion))" -ForegroundColor Gray
Write-Host "   RAM: $($healthResults.SystemInfo.TotalRAM_GB) GB" -ForegroundColor Gray
Write-Host "   Processes: $($healthResults.ProcessMonitoring | Where-Object { $_.Status -eq 'RUNNING' } | Measure-Object).Count active" -ForegroundColor Gray

# Display recommendations
Write-Host ""
Write-Host "💡 Recommendations:" -ForegroundColor Yellow
$healthResults.Recommendations | ForEach-Object {
    Write-Host "   $_" -ForegroundColor White
}

# Export results if requested
if ($Export) {
    try {
        $healthResults | ConvertTo-Json -Depth 10 | Set-Content $OutputPath -Encoding UTF8
        Write-Host ""
        Write-Host "📁 Results exported to: $OutputPath" -ForegroundColor Green
    }
    catch {
        Write-Host "⚠️ Export failed: $($_.Exception.Message)" -ForegroundColor Yellow
    }
}

Write-Host ""
Write-Host "🏆 POWERSHELL 7.6 EMPIRE HEALTH CHECK COMPLETE 🏆" -ForegroundColor Green
Write-Host "⚡ Empire monitoring with cutting-edge PowerShell 7.6 features! ⚡" -ForegroundColor Cyan

#!/usr/bin/env powershell
<#
🌐💎⚡ TAILSCALE ULTRA QUICK FIX COMMANDER ⚡💎🌐
Windows PowerShell script for instant Tailscale troubleshooting
ADHD-friendly, one-click network restoration

Usage: .\tailscale_quick_fix.ps1
#>

# Enhanced error handling and admin check
param(
    [switch]$Force,
    [switch]$Verbose,
    [string]$TargetDomain = "hyperfocuszone.tail13f1ca.ts.net"
)

# ADHD-friendly output formatting
function Write-Section {
    param([string]$Title, [string]$Emoji = "🔧")
    Write-Host ""
    Write-Host "$Emoji $('='*70)" -ForegroundColor Cyan
    Write-Host "$Emoji $Title" -ForegroundColor Yellow
    Write-Host "$Emoji $('='*70)" -ForegroundColor Cyan
}

function Write-Success {
    param([string]$Message)
    Write-Host "✅ $Message" -ForegroundColor Green
}

function Write-Error {
    param([string]$Message)
    Write-Host "❌ $Message" -ForegroundColor Red
}

function Write-Warning {
    param([string]$Message)
    Write-Host "⚠️ $Message" -ForegroundColor Yellow
}

function Write-Info {
    param([string]$Message)
    Write-Host "🔍 $Message" -ForegroundColor Cyan
}

# Check if running as administrator
function Test-Administrator {
    $currentUser = [Security.Principal.WindowsIdentity]::GetCurrent()
    $principal = New-Object Security.Principal.WindowsPrincipal($currentUser)
    return $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
}

# Quick Tailscale installation check
function Test-TailscaleInstalled {
    Write-Section "🔍 TAILSCALE INSTALLATION CHECK"
    
    try {
        $version = & tailscale version 2>$null
        if ($LASTEXITCODE -eq 0) {
            Write-Success "Tailscale installed: $version"
            return $true
        }
    }
    catch {
        Write-Error "Tailscale command not found"
    }
    
    # Check if installed but not in PATH
    $possiblePaths = @(
        "${env:ProgramFiles}\Tailscale\tailscale.exe",
        "${env:ProgramFiles(x86)}\Tailscale\tailscale.exe",
        "${env:LOCALAPPDATA}\Tailscale\tailscale.exe"
    )
    
    foreach ($path in $possiblePaths) {
        if (Test-Path $path) {
            Write-Warning "Found Tailscale at: $path"
            Write-Info "Adding to PATH for this session"
            $env:PATH += ";$(Split-Path $path)"
            return $true
        }
    }
    
    return $false
}

# Quick installation via winget
function Install-TailscaleQuick {
    Write-Section "📦 QUICK TAILSCALE INSTALLATION"
    
    if (-not (Test-Administrator)) {
        Write-Error "Administrator privileges required for installation"
        Write-Info "Please run PowerShell as Administrator"
        return $false
    }
    
    Write-Info "Attempting installation via winget..."
    
    try {
        & winget install tailscale.tailscale --accept-package-agreements --accept-source-agreements
        if ($LASTEXITCODE -eq 0) {
            Write-Success "Tailscale installed successfully via winget"
            # Refresh PATH
            $env:PATH = [System.Environment]::GetEnvironmentVariable("PATH", "Machine") + ";" + [System.Environment]::GetEnvironmentVariable("PATH", "User")
            return $true
        }
    }
    catch {
        Write-Warning "Winget installation failed: $($_.Exception.Message)"
    }
    
    Write-Info "Alternative: Download from https://tailscale.com/download"
    return $false
}

# Check Tailscale login status
function Test-TailscaleLogin {
    Write-Section "🔐 TAILSCALE LOGIN STATUS"
    
    try {
        $status = & tailscale status 2>$null
        if ($LASTEXITCODE -eq 0) {
            if ($status -match "Logged out") {
                Write-Warning "Tailscale is not logged in"
                return $false
            }
            else {
                Write-Success "Tailscale is logged in"
                Write-Info "Status: $($status.Split("`n")[0])"
                return $true
            }
        }
    }
    catch {
        Write-Error "Failed to check Tailscale status"
    }
    
    return $false
}

# Quick login process
function Start-TailscaleLogin {
    Write-Section "🚀 TAILSCALE LOGIN PROCESS"
    
    Write-Info "Starting Tailscale login..."
    Write-Warning "This will open a browser window for authentication"
    
    try {
        & tailscale login
        if ($LASTEXITCODE -eq 0) {
            Write-Success "Login process initiated successfully"
            return $true
        }
        else {
            Write-Error "Login process failed"
            return $false
        }
    }
    catch {
        Write-Error "Failed to start login: $($_.Exception.Message)"
        return $false
    }
}

# Network connectivity tests
function Test-NetworkConnectivity {
    Write-Section "🌐 NETWORK CONNECTIVITY TESTS"
    
    $tests = @(
        @{Name="Google DNS"; Host="8.8.8.8"},
        @{Name="Cloudflare DNS"; Host="1.1.1.1"},
        @{Name="Target Domain"; Host=$TargetDomain}
    )
    
    $results = @()
    
    foreach ($test in $tests) {
        Write-Info "Testing $($test.Name) ($($test.Host))"
        
        try {
            $ping = Test-Connection -ComputerName $test.Host -Count 2 -Quiet
            if ($ping) {
                Write-Success "$($test.Name): Reachable"
                $results += @{Name=$test.Name; Status="Success"; Host=$test.Host}
            }
            else {
                Write-Error "$($test.Name): Not reachable"
                $results += @{Name=$test.Name; Status="Failed"; Host=$test.Host}
            }
        }
        catch {
            Write-Error "$($test.Name): Error - $($_.Exception.Message)"
            $results += @{Name=$test.Name; Status="Error"; Host=$test.Host; Error=$_.Exception.Message}
        }
    }
    
    return $results
}

# Check common web ports
function Test-WebPorts {
    Write-Section "🔌 WEB PORT CONNECTIVITY TEST"
    
    $ports = @(80, 443, 8080, 3000, 5000)
    $results = @()
    
    foreach ($port in $ports) {
        Write-Info "Testing port $port on $TargetDomain"
        
        try {
            $tcpClient = New-Object System.Net.Sockets.TcpClient
            $connect = $tcpClient.BeginConnect($TargetDomain, $port, $null, $null)
            $wait = $connect.AsyncWaitHandle.WaitOne(3000, $false)
            
            if ($wait) {
                try {
                    $tcpClient.EndConnect($connect)
                    Write-Success "Port $port: Open"
                    $results += @{Port=$port; Status="Open"}
                }
                catch {
                    Write-Warning "Port $port: Closed"
                    $results += @{Port=$port; Status="Closed"}
                }
            }
            else {
                Write-Warning "Port $port: Timeout"
                $results += @{Port=$port; Status="Timeout"}
            }
            
            $tcpClient.Close()
        }
        catch {
            Write-Error "Port $port: Error - $($_.Exception.Message)"
            $results += @{Port=$port; Status="Error"; Error=$_.Exception.Message}
        }
    }
    
    return $results
}

# Quick service restart
function Restart-TailscaleService {
    Write-Section "🔄 TAILSCALE SERVICE RESTART"
    
    if (-not (Test-Administrator)) {
        Write-Error "Administrator privileges required for service restart"
        return $false
    }
    
    try {
        Write-Info "Stopping Tailscale service..."
        Stop-Service -Name "Tailscale" -Force -ErrorAction SilentlyContinue
        
        Start-Sleep -Seconds 3
        
        Write-Info "Starting Tailscale service..."
        Start-Service -Name "Tailscale"
        
        Write-Success "Tailscale service restarted successfully"
        return $true
    }
    catch {
        Write-Error "Failed to restart service: $($_.Exception.Message)"
        return $false
    }
}

# Generate repair recommendations
function Get-RepairRecommendations {
    param([hashtable]$TestResults)
    
    Write-Section "🔧 REPAIR RECOMMENDATIONS"
    
    $recommendations = @()
    
    # Tailscale installation
    if (-not $TestResults.TailscaleInstalled) {
        $recommendations += @{
            Priority = "CRITICAL"
            Action = "Install Tailscale"
            Description = "Tailscale is not installed or not accessible"
            Command = "Run as Administrator: winget install tailscale.tailscale"
        }
    }
    
    # Login status
    if (-not $TestResults.TailscaleLoggedIn) {
        $recommendations += @{
            Priority = "HIGH"
            Action = "Login to Tailscale"
            Description = "Tailscale is installed but not authenticated"
            Command = "tailscale login"
        }
    }
    
    # Network connectivity
    $failedPingTests = $TestResults.NetworkTests | Where-Object { $_.Status -ne "Success" }
    if ($failedPingTests.Count -gt 0) {
        $recommendations += @{
            Priority = "HIGH"
            Action = "Check Network Connectivity"
            Description = "Some network connectivity tests failed"
            Command = "Check firewall settings and internet connection"
        }
    }
    
    # Port connectivity
    $closedPorts = $TestResults.PortTests | Where-Object { $_.Status -ne "Open" }
    if ($closedPorts.Count -eq $TestResults.PortTests.Count) {
        $recommendations += @{
            Priority = "MEDIUM"
            Action = "Start Web Services"
            Description = "No web services are running on the target"
            Command = "Start your web applications (nginx, IIS, or development servers)"
        }
    }
    
    # Display recommendations
    for ($i = 0; $i -lt $recommendations.Count; $i++) {
        $rec = $recommendations[$i]
        Write-Host ""
        Write-Host "$($i + 1). [$($rec.Priority)] $($rec.Action)" -ForegroundColor Yellow
        Write-Host "   📝 $($rec.Description)" -ForegroundColor White
        Write-Host "   💻 $($rec.Command)" -ForegroundColor Cyan
    }
    
    return $recommendations
}

# Main execution function
function Start-TailscaleQuickFix {
    Write-Host "🌐💎⚡ TAILSCALE ULTRA QUICK FIX COMMANDER ⚡💎🌐" -ForegroundColor Magenta
    Write-Host "Enhanced Tailscale troubleshooting for HyperFocus Zone Empire" -ForegroundColor White
    Write-Host "Target Domain: $TargetDomain" -ForegroundColor Cyan
    Write-Host "=" * 80 -ForegroundColor Gray
    
    $testResults = @{}
    $broskyEarned = 0
    
    # Test 1: Tailscale Installation
    $testResults.TailscaleInstalled = Test-TailscaleInstalled
    if ($testResults.TailscaleInstalled) {
        $broskyEarned += 25
    }
    else {
        if ($Force -or (Read-Host "Install Tailscale? (y/N)") -eq "y") {
            $testResults.TailscaleInstalled = Install-TailscaleQuick
            if ($testResults.TailscaleInstalled) {
                $broskyEarned += 100
            }
        }
    }
    
    # Test 2: Login Status (only if installed)
    if ($testResults.TailscaleInstalled) {
        $testResults.TailscaleLoggedIn = Test-TailscaleLogin
        if ($testResults.TailscaleLoggedIn) {
            $broskyEarned += 50
        }
        else {
            if ($Force -or (Read-Host "Login to Tailscale? (y/N)") -eq "y") {
                $loginSuccess = Start-TailscaleLogin
                if ($loginSuccess) {
                    Start-Sleep -Seconds 5
                    $testResults.TailscaleLoggedIn = Test-TailscaleLogin
                    if ($testResults.TailscaleLoggedIn) {
                        $broskyEarned += 75
                    }
                }
            }
        }
    }
    
    # Test 3: Network Connectivity
    $testResults.NetworkTests = Test-NetworkConnectivity
    $successfulTests = ($testResults.NetworkTests | Where-Object { $_.Status -eq "Success" }).Count
    $broskyEarned += $successfulTests * 15
    
    # Test 4: Port Connectivity
    $testResults.PortTests = Test-WebPorts
    $openPorts = ($testResults.PortTests | Where-Object { $_.Status -eq "Open" }).Count
    $broskyEarned += $openPorts * 20
    
    # Service restart option
    if ($testResults.TailscaleInstalled -and (-not $testResults.TailscaleLoggedIn)) {
        if ($Force -or (Read-Host "Restart Tailscale service? (y/N)") -eq "y") {
            if (Restart-TailscaleService) {
                $broskyEarned += 50
                Start-Sleep -Seconds 3
                $testResults.TailscaleLoggedIn = Test-TailscaleLogin
            }
        }
    }
    
    # Generate recommendations
    $recommendations = Get-RepairRecommendations -TestResults $testResults
    
    # Final summary
    Write-Section "🎊 QUICK FIX SUMMARY" "🏆"
    Write-Host "🎯 Tailscale Installed: $(if ($testResults.TailscaleInstalled) { '✅' } else { '❌' })" -ForegroundColor $(if ($testResults.TailscaleInstalled) { 'Green' } else { 'Red' })
    Write-Host "🔐 Tailscale Logged In: $(if ($testResults.TailscaleLoggedIn) { '✅' } else { '❌' })" -ForegroundColor $(if ($testResults.TailscaleLoggedIn) { 'Green' } else { 'Red' })
    Write-Host "🌐 Network Tests Passed: $successfulTests/$($testResults.NetworkTests.Count)" -ForegroundColor $(if ($successfulTests -gt 1) { 'Green' } else { 'Yellow' })
    Write-Host "🔌 Open Ports: $openPorts/$($testResults.PortTests.Count)" -ForegroundColor $(if ($openPorts -gt 0) { 'Green' } else { 'Yellow' })
    Write-Host "🔧 Recommendations: $($recommendations.Count)" -ForegroundColor $(if ($recommendations.Count -eq 0) { 'Green' } else { 'Yellow' })
    Write-Host "💎 BROski$ Earned: $broskyEarned" -ForegroundColor Magenta
    
    if ($testResults.TailscaleInstalled -and $testResults.TailscaleLoggedIn -and $successfulTests -gt 1) {
        Write-Host ""
        Write-Success "🎊 LEGENDARY SUCCESS! Network should be operational!"
        Write-Host "🌐 Try accessing: http://$TargetDomain" -ForegroundColor Cyan
    }
    elseif ($recommendations.Count -gt 0) {
        Write-Host ""
        Write-Warning "⚠️ Some issues found - follow recommendations above"
    }
    
    # Save results to file
    $timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
    $resultsFile = "h:\quick_fix_results_$timestamp.json"
    
    $fullResults = @{
        timestamp = (Get-Date).ToString("yyyy-MM-ddTHH:mm:ssZ")
        target_domain = $TargetDomain
        test_results = $testResults
        recommendations = $recommendations
        brosky_earned = $broskyEarned
        summary = @{
            tailscale_installed = $testResults.TailscaleInstalled
            tailscale_logged_in = $testResults.TailscaleLoggedIn
            network_tests_passed = $successfulTests
            open_ports = $openPorts
            total_recommendations = $recommendations.Count
        }
    }
    
    try {
        $fullResults | ConvertTo-Json -Depth 10 | Out-File -FilePath $resultsFile -Encoding UTF8
        Write-Info "📋 Results saved to: $resultsFile"
    }
    catch {
        Write-Warning "Could not save results file: $($_.Exception.Message)"
    }
    
    return $fullResults
}

# Execute main function
if ($MyInvocation.InvocationName -ne '.') {
    Start-TailscaleQuickFix
}

#!/usr/bin/env pwsh

# 🚀💎⚡ HYPERFOCUS EMPIRE - PLAYWRIGHT MCP LAUNCHER ⚡💎🚀
# BROski Level: LEGENDARY | Status: ACTIVE
# Purpose: Start Playwright MCP server with empire configuration

param(
    [string]$Mode = "standard",
    [string]$Browser = "chrome", 
    [int]$Port = 0,
    [switch]$Headless,
    [switch]$Isolated,
    [switch]$Help
)

if ($Help) {
    Write-Host "🚀💎⚡ PLAYWRIGHT MCP LAUNCHER - USAGE GUIDE ⚡💎🚀" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "PARAMETERS:" -ForegroundColor Yellow
    Write-Host "  -Mode      : standard|testing|security|performance (default: standard)" -ForegroundColor White
    Write-Host "  -Browser   : chrome|firefox|webkit|msedge (default: chrome)" -ForegroundColor White  
    Write-Host "  -Port      : Run as HTTP server on specified port (default: 0 = stdio)" -ForegroundColor White
    Write-Host "  -Headless  : Run browser in headless mode" -ForegroundColor White
    Write-Host "  -Isolated  : Use isolated sessions (fresh profile each time)" -ForegroundColor White
    Write-Host "  -Help      : Show this help message" -ForegroundColor White
    Write-Host ""
    Write-Host "EXAMPLES:" -ForegroundColor Yellow
    Write-Host "  .\start-playwright-mcp.ps1" -ForegroundColor Green
    Write-Host "  .\start-playwright-mcp.ps1 -Mode testing -Browser firefox -Headless" -ForegroundColor Green
    Write-Host "  .\start-playwright-mcp.ps1 -Port 8931 -Isolated" -ForegroundColor Green
    return
}

Write-Host "🎊💎⚡ HYPERFOCUS EMPIRE - PLAYWRIGHT MCP SERVER ⚡💎🎊" -ForegroundColor Cyan
Write-Host "=" * 70 -ForegroundColor Yellow

# Configuration based on mode
$configMap = @{
    "standard" = @{
        "config" = "playwright-empire-config.json"
        "description" = "Standard empire operations"
        "headless" = $true
        "trace" = $true
        "session" = $true
    }
    "testing" = @{
        "config" = "playwright-testing-config.json"
        "description" = "Testing and development mode"
        "headless" = $false
        "trace" = $true
        "session" = $false
        "isolated" = $true
    }
    "security" = @{
        "config" = "security-profile.json"
        "description" = "High security mode with strict controls"
        "headless" = $true
        "trace" = $true
        "session" = $false
        "isolated" = $true
        "sandbox" = $false
    }
    "performance" = @{
        "config" = "performance-config.json"
        "description" = "Optimized for high-performance automation"
        "headless" = $true
        "trace" = $false
        "session" = $true
        "fast" = $true
    }
}

$config = $configMap[$Mode]
if (!$config) {
    Write-Host "❌ Invalid mode: $Mode" -ForegroundColor Red
    Write-Host "Valid modes: standard, testing, security, performance" -ForegroundColor Yellow
    return
}

Write-Host "🎯 Mode: $Mode - $($config.description)" -ForegroundColor Green
Write-Host "🌐 Browser: $Browser" -ForegroundColor Green
Write-Host "📍 Working Directory: $PWD" -ForegroundColor Green

# Build command arguments
$args = @("@playwright/mcp@latest")

# Basic configuration
$args += "--browser", $Browser

# Mode-specific settings
if ($config.headless -or $Headless) {
    $args += "--headless"
    Write-Host "👻 Headless mode: ENABLED" -ForegroundColor Yellow
} else {
    Write-Host "🖥️ Headed mode: Browser window will be visible" -ForegroundColor Yellow
}

if ($config.isolated -or $Isolated) {
    $args += "--isolated"
    Write-Host "🔒 Isolated sessions: ENABLED" -ForegroundColor Yellow
}

if ($config.trace) {
    $args += "--save-trace"
    Write-Host "📊 Trace logging: ENABLED" -ForegroundColor Yellow
}

if ($config.session) {
    $args += "--save-session"
    Write-Host "💾 Session saving: ENABLED" -ForegroundColor Yellow
}

# Security settings
$args += "--allowed-origins", "hyperfocuszone.com;localhost;*.ai;github.com;*.github.com;npmjs.com"
$args += "--blocked-origins", "ads.google.com;facebook.com/tr;analytics.google.com"
$args += "--user-agent", "HyperFocus-Empire-Agent/1.0"
$args += "--viewport-size", "1920,1080"

# Output directory
$outputDir = ".\empire-automation-logs"
if (!(Test-Path $outputDir)) {
    New-Item -ItemType Directory -Path $outputDir -Force | Out-Null
}
$args += "--output-dir", $outputDir

# Performance optimizations
if ($config.fast) {
    $args += "--no-sandbox"
    $args += "--disable-dev-shm-usage"
}

# HTTP server mode
if ($Port -gt 0) {
    $args += "--port", $Port
    $args += "--host", "localhost"
    Write-Host "🌐 HTTP Server: http://localhost:$Port/mcp" -ForegroundColor Green
} else {
    Write-Host "📡 Communication: stdio (direct MCP client connection)" -ForegroundColor Green
}

Write-Host ""
Write-Host "🚀 Starting Playwright MCP Server..." -ForegroundColor Cyan
Write-Host "Command: npx $($args -join ' ')" -ForegroundColor DarkGray
Write-Host ""

try {
    # Check if Playwright MCP is installed
    $testResult = npx @playwright/mcp@latest --help 2>&1
    if ($testResult -notmatch "Playwright MCP") {
        Write-Host "❌ Playwright MCP not found. Running installation..." -ForegroundColor Red
        & "$PSScriptRoot\install-playwright-mcp.ps1"
        return
    }

    Write-Host "✅ Playwright MCP detected. Launching server..." -ForegroundColor Green
    Write-Host ""
    
    if ($Port -gt 0) {
        Write-Host "🌟 HTTP Server Mode - Connect your MCP client to:" -ForegroundColor Cyan
        Write-Host "   URL: http://localhost:$Port/mcp" -ForegroundColor White
        Write-Host "   Status: Server running in background" -ForegroundColor White
        Write-Host ""
        Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
    } else {
        Write-Host "🌟 Direct Mode - Server ready for MCP client connection" -ForegroundColor Cyan
        Write-Host "   Use this configuration in your MCP client" -ForegroundColor White
        Write-Host ""
    }

    # Start the server
    npx @args

} catch {
    Write-Host "❌ Failed to start Playwright MCP server: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host "🔧 Troubleshooting:" -ForegroundColor Yellow
    Write-Host "   1. Check if Node.js is installed and in PATH" -ForegroundColor White
    Write-Host "   2. Verify Playwright MCP installation" -ForegroundColor White
    Write-Host "   3. Run install-playwright-mcp.ps1 to reinstall" -ForegroundColor White
    Write-Host "   4. Check firewall settings if using HTTP mode" -ForegroundColor White
} finally {
    Write-Host ""
    Write-Host "🎊 Playwright MCP Server session ended" -ForegroundColor Cyan
    Write-Host "📊 Check $outputDir for session logs and traces" -ForegroundColor Yellow
}

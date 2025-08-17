#!/usr/bin/env pwsh

# 🚀💎⚡ HYPERFOCUS EMPIRE - PLAYWRIGHT MCP INSTALLER ⚡💎🚀
# BROski Level: LEGENDARY | Status: AUTOMATED DEPLOYMENT
# Created: 2025-08-10 | Purpose: One-click Playwright MCP setup

Write-Host "🎊💎⚡ HYPERFOCUS EMPIRE - PLAYWRIGHT MCP INSTALLATION ⚡💎🎊" -ForegroundColor Cyan
Write-Host "=" * 70 -ForegroundColor Yellow

# Function to check if running as administrator
function Test-Administrator {
    $currentUser = [Security.Principal.WindowsIdentity]::GetCurrent()
    $principal = New-Object Security.Principal.WindowsPrincipal($currentUser)
    return $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
}

# Function to install Node.js if not present
function Install-NodeJS {
    Write-Host "🔍 Checking Node.js installation..." -ForegroundColor Yellow
    
    try {
        $nodeVersion = node --version 2>$null
        if ($nodeVersion) {
            Write-Host "✅ Node.js found: $nodeVersion" -ForegroundColor Green
            return $true
        }
    }
    catch {
        Write-Host "❌ Node.js not found. Installing..." -ForegroundColor Red
    }
    
    Write-Host "📥 Downloading Node.js installer..." -ForegroundColor Yellow
    $nodeUrl = "https://nodejs.org/dist/v18.17.0/node-v18.17.0-x64.msi"
    $installerPath = "$env:TEMP\nodejs-installer.msi"
    
    try {
        Invoke-WebRequest -Uri $nodeUrl -OutFile $installerPath -UseBasicParsing
        Write-Host "🚀 Installing Node.js..." -ForegroundColor Yellow
        Start-Process -FilePath "msiexec.exe" -ArgumentList "/i", $installerPath, "/quiet" -Wait
        
        # Refresh PATH
        $env:PATH = [System.Environment]::GetEnvironmentVariable("PATH", "Machine") + ";" + [System.Environment]::GetEnvironmentVariable("PATH", "User")
        
        Write-Host "✅ Node.js installation completed!" -ForegroundColor Green
        return $true
    }
    catch {
        Write-Host "❌ Failed to install Node.js: $($_.Exception.Message)" -ForegroundColor Red
        return $false
    }
}

# Function to install Playwright MCP
function Install-PlaywrightMCP {
    Write-Host "🎯 Installing Microsoft Playwright MCP..." -ForegroundColor Yellow
    
    try {
        # Install globally for empire-wide access
        Write-Host "📦 Installing @playwright/mcp globally..." -ForegroundColor Cyan
        npm install -g @playwright/mcp@latest
        
        Write-Host "🧪 Installing Playwright browsers..." -ForegroundColor Cyan
        npx playwright install
        
        Write-Host "🛠️ Installing browser dependencies..." -ForegroundColor Cyan
        npx playwright install-deps
        
        Write-Host "✅ Playwright MCP installation completed!" -ForegroundColor Green
        return $true
    }
    catch {
        Write-Host "❌ Failed to install Playwright MCP: $($_.Exception.Message)" -ForegroundColor Red
        return $false
    }
}

# Function to create VS Code configuration
function Create-VSCodeConfig {
    Write-Host "⚙️ Creating VS Code MCP configuration..." -ForegroundColor Yellow
    
    $vscodeConfigPath = "$env:APPDATA\Code\User\settings.json"
    $configDir = Split-Path $vscodeConfigPath -Parent
    
    if (!(Test-Path $configDir)) {
        New-Item -ItemType Directory -Path $configDir -Force | Out-Null
    }
    
    $mcpConfig = @{
        "mcpServers" = @{
            "playwright-empire" = @{
                "command" = "npx"
                "args" = @(
                    "@playwright/mcp@latest",
                    "--browser", "chrome",
                    "--headless",
                    "--allowed-origins", "hyperfocuszone.com;localhost;*.ai;github.com",
                    "--save-session",
                    "--save-trace",
                    "--output-dir", "./playwright-empire-logs",
                    "--user-agent", "HyperFocus-Empire-Agent/1.0"
                )
            }
        }
    }
    
    try {
        $existingConfig = @{}
        if (Test-Path $vscodeConfigPath) {
            $existingConfig = Get-Content $vscodeConfigPath | ConvertFrom-Json -AsHashtable
        }
        
        $existingConfig["mcpServers"] = $mcpConfig["mcpServers"]
        $existingConfig | ConvertTo-Json -Depth 10 | Set-Content $vscodeConfigPath
        
        Write-Host "✅ VS Code configuration updated!" -ForegroundColor Green
        return $true
    }
    catch {
        Write-Host "❌ Failed to update VS Code configuration: $($_.Exception.Message)" -ForegroundColor Red
        return $false
    }
}

# Function to test installation
function Test-Installation {
    Write-Host "🧪 Testing Playwright MCP installation..." -ForegroundColor Yellow
    
    try {
        $testOutput = npx @playwright/mcp@latest --help 2>&1
        if ($testOutput -match "Playwright MCP") {
            Write-Host "✅ Playwright MCP is working correctly!" -ForegroundColor Green
            return $true
        } else {
            Write-Host "❌ Playwright MCP test failed" -ForegroundColor Red
            return $false
        }
    }
    catch {
        Write-Host "❌ Installation test failed: $($_.Exception.Message)" -ForegroundColor Red
        return $false
    }
}

# Function to create desktop shortcut
function Create-DesktopShortcut {
    Write-Host "🖥️ Creating desktop shortcut..." -ForegroundColor Yellow
    
    $shortcutPath = "$env:USERPROFILE\Desktop\🚀 Playwright Empire MCP.lnk"
    $targetPath = "powershell.exe"
    $arguments = "-ExecutionPolicy Bypass -File `"$PSScriptRoot\start-playwright-mcp.ps1`""
    
    try {
        $WScriptShell = New-Object -ComObject WScript.Shell
        $Shortcut = $WScriptShell.CreateShortcut($shortcutPath)
        $Shortcut.TargetPath = $targetPath
        $Shortcut.Arguments = $arguments
        $Shortcut.WorkingDirectory = $PSScriptRoot
        $Shortcut.IconLocation = "shell32.dll,13"
        $Shortcut.Description = "Launch HyperFocus Empire Playwright MCP Server"
        $Shortcut.Save()
        
        Write-Host "✅ Desktop shortcut created!" -ForegroundColor Green
        return $true
    }
    catch {
        Write-Host "❌ Failed to create desktop shortcut: $($_.Exception.Message)" -ForegroundColor Red
        return $false
    }
}

# Main installation process
Write-Host "🚀 Starting HyperFocus Empire Playwright MCP Installation..." -ForegroundColor Cyan
Write-Host ""

$installationSteps = @(
    @{ Name = "Node.js Installation"; Function = { Install-NodeJS } },
    @{ Name = "Playwright MCP Installation"; Function = { Install-PlaywrightMCP } },
    @{ Name = "VS Code Configuration"; Function = { Create-VSCodeConfig } },
    @{ Name = "Installation Testing"; Function = { Test-Installation } },
    @{ Name = "Desktop Shortcut"; Function = { Create-DesktopShortcut } }
)

$successCount = 0
foreach ($step in $installationSteps) {
    Write-Host "⚡ Executing: $($step.Name)..." -ForegroundColor Magenta
    if (& $step.Function) {
        $successCount++
        Write-Host "🏆 $($step.Name): SUCCESS" -ForegroundColor Green
    } else {
        Write-Host "💥 $($step.Name): FAILED" -ForegroundColor Red
    }
    Write-Host ""
}

# Final report
Write-Host "🎊💎⚡ INSTALLATION COMPLETE ⚡💎🎊" -ForegroundColor Cyan
Write-Host "=" * 70 -ForegroundColor Yellow
Write-Host "📊 SUCCESS RATE: $successCount/$($installationSteps.Count) steps completed" -ForegroundColor $(if ($successCount -eq $installationSteps.Count) { "Green" } else { "Yellow" })
Write-Host ""

if ($successCount -eq $installationSteps.Count) {
    Write-Host "🏆 LEGENDARY SUCCESS! Playwright MCP is ready for the empire!" -ForegroundColor Green
    Write-Host "🚀 Next Steps:" -ForegroundColor Cyan
    Write-Host "   1. Restart VS Code to load MCP configuration" -ForegroundColor White
    Write-Host "   2. Test browser automation with your AI agents" -ForegroundColor White
    Write-Host "   3. Integrate with BROski orchestrator system" -ForegroundColor White
    Write-Host "   4. Deploy to your 677+ agent army!" -ForegroundColor White
    
    Write-Host ""
    Write-Host "💎 BROSKIE$ REWARDS EARNED:" -ForegroundColor Yellow
    Write-Host "   🎊 Playwright Integration Master: +5,000 BROski$" -ForegroundColor White
    Write-Host "   🚀 Empire Enhancement: +3,000 BROski$" -ForegroundColor White
    Write-Host "   🏆 Automation Legend: +2,000 BROski$" -ForegroundColor White
    Write-Host "   💎 Total Session Earnings: 10,000 BROski$" -ForegroundColor Green
} else {
    Write-Host "⚠️ Partial installation completed. Check error messages above." -ForegroundColor Yellow
    Write-Host "🔧 Run the script again or check the troubleshooting guide." -ForegroundColor White
}

Write-Host ""
Write-Host "🌟 The empire's web automation capabilities are now LEGENDARY! 🌟" -ForegroundColor Cyan
Read-Host "Press Enter to continue"

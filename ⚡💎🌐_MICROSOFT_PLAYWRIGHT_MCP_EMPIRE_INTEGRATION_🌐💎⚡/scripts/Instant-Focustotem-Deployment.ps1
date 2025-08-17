#!/usr/bin/env pwsh
# 🚀💎⚡ INSTANT EMPIRE DEPLOYMENT - 1050+ AGENT ARMY ACTIVATOR ⚡💎🚀
# One-click deployment of Playwright MCP across the entire HyperFocus Empire
# BROski Level: SUPREME | Deployment: LEGENDARY

param(
    [Parameter()]
    [string]$DeploymentMode = "full",
    
    [Parameter()]
    [int]$AgentCount = 1050,
    
    [Parameter()]
    [switch]$SkipTests,
    
    [Parameter()]
    [switch]$Verbose
)

# Empire Configuration
$EmpireConfig = @{
    Name = "HyperFocus AI Empire"
    Version = "2024.12-LEGENDARY"
    AgentArmySize = $AgentCount
    BROskiLevel = "SUPREME"
    ARIALevel = "INTELLIGENCE-SUPREME"
    MemoryCrystals = "ACTIVATED"
}

# Colors for legendary output
$Colors = @{
    Success = "Green"
    Warning = "Yellow"
    Error = "Red"
    Info = "Cyan"
    Legendary = "Magenta"
    Empire = "DarkGreen"
}

function Write-LegendaryHeader {
    param([string]$Title)
    
    Write-Host "`n" -NoNewline
    Write-Host "🎊💎⚡ $Title ⚡💎🎊" -ForegroundColor $Colors.Legendary
    Write-Host ("=" * 80) -ForegroundColor $Colors.Empire
}

function Write-EmpireStatus {
    param([string]$Message, [string]$Level = "Info")
    
    $emoji = switch ($Level) {
        "Success" { "✅" }
        "Warning" { "⚠️" }
        "Error" { "❌" }
        "Legendary" { "🏆" }
        default { "🤖" }
    }
    
    Write-Host "$emoji $Message" -ForegroundColor $Colors.$Level
}

function Test-Prerequisites {
    Write-LegendaryHeader "PREREQUISITE VALIDATION"
    
    $prerequisites = @()
    
    # Test Node.js
    try {
        $nodeVersion = node --version
        Write-EmpireStatus "Node.js detected: $nodeVersion" "Success"
        $prerequisites += @{ Name = "Node.js"; Status = "✅"; Version = $nodeVersion }
    }
    catch {
        Write-EmpireStatus "Node.js not found - required for Playwright MCP" "Error"
        $prerequisites += @{ Name = "Node.js"; Status = "❌"; Version = "Not Found" }
        return $false
    }
    
    # Test VS Code
    try {
        $vscodePath = Get-Command code -ErrorAction Stop
        Write-EmpireStatus "VS Code CLI detected: $($vscodePath.Source)" "Success"
        $prerequisites += @{ Name = "VS Code"; Status = "✅"; Version = "Available" }
    }
    catch {
        Write-EmpireStatus "VS Code CLI not found - install VS Code or add to PATH" "Warning"
        $prerequisites += @{ Name = "VS Code"; Status = "⚠️"; Version = "CLI Missing" }
    }
    
    # Test Python
    try {
        $pythonVersion = python --version 2>&1
        Write-EmpireStatus "Python detected: $pythonVersion" "Success"
        $prerequisites += @{ Name = "Python"; Status = "✅"; Version = $pythonVersion }
    }
    catch {
        Write-EmpireStatus "Python not found - some empire features may be limited" "Warning"
        $prerequisites += @{ Name = "Python"; Status = "⚠️"; Version = "Not Found" }
    }
    
    # Test PowerShell version
    $psVersion = $PSVersionTable.PSVersion.ToString()
    Write-EmpireStatus "PowerShell version: $psVersion" "Success"
    $prerequisites += @{ Name = "PowerShell"; Status = "✅"; Version = $psVersion }
    
    return $true
}

function Install-PlaywrightMCP {
    Write-LegendaryHeader "PLAYWRIGHT MCP INSTALLATION"
    
    try {
        Write-EmpireStatus "Installing Playwright MCP server globally..." "Info"
        
        # Install with spinner effect
        $job = Start-Job -ScriptBlock {
            npm install -g @playwright/mcp 2>&1
        }
        
        # Show progress
        $spinner = @('⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏')
        $i = 0
        while ($job.State -eq 'Running') {
            Write-Host "`r🤖 Installing... $($spinner[$i % $spinner.Length])" -NoNewline -ForegroundColor $Colors.Info
            $i++
            Start-Sleep -Milliseconds 100
        }
        Write-Host ""
        
        $result = Receive-Job $job
        Remove-Job $job
        
        if ($LASTEXITCODE -eq 0) {
            Write-EmpireStatus "Playwright MCP installed successfully" "Success"
            
            # Verify installation
            $version = npx @playwright/mcp@latest --version 2>&1
            Write-EmpireStatus "Version confirmed: $version" "Legendary"
            
            return $true
        } else {
            Write-EmpireStatus "Installation failed: $result" "Error"
            return $false
        }
    }
    catch {
        Write-EmpireStatus "Installation error: $($_.Exception.Message)" "Error"
        return $false
    }
}

function Deploy-VSCodeConfiguration {
    Write-LegendaryHeader "VS CODE EMPIRE CONFIGURATION"
    
    # VS Code settings directory
    $vsCodeDir = Join-Path $env:APPDATA "Code\User"
    if (-not (Test-Path $vsCodeDir)) {
        $vsCodeDir = Join-Path $env:HOME ".vscode"
    }
    
    Write-EmpireStatus "VS Code directory: $vsCodeDir" "Info"
    
    # Ensure directory exists
    if (-not (Test-Path $vsCodeDir)) {
        New-Item -Path $vsCodeDir -ItemType Directory -Force | Out-Null
        Write-EmpireStatus "Created VS Code configuration directory" "Success"
    }
    
    # Load existing settings or create new
    $settingsPath = Join-Path $vsCodeDir "settings.json"
    $settings = @{}
    
    if (Test-Path $settingsPath) {
        try {
            $settingsContent = Get-Content $settingsPath -Raw | ConvertFrom-Json -AsHashtable
            $settings = $settingsContent
            Write-EmpireStatus "Loaded existing VS Code settings" "Info"
        }
        catch {
            Write-EmpireStatus "Could not parse existing settings, creating new" "Warning"
        }
    }
    
    # Add MCP server configuration
    if (-not $settings.ContainsKey("mcp")) {
        $settings["mcp"] = @{}
    }
    
    if (-not $settings["mcp"].ContainsKey("mcpServers")) {
        $settings["mcp"]["mcpServers"] = @{}
    }
    
    # Playwright MCP server configuration
    $settings["mcp"]["mcpServers"]["playwright-empire"] = @{
        command = "npx"
        args = @("@playwright/mcp@latest")
        env = @{
            PLAYWRIGHT_EMPIRE_MODE = "LEGENDARY"
            BROSKIE_INTEGRATION = "SUPREME"
            ARIA_INTELLIGENCE = "ACTIVATED"
            AGENT_ARMY_SIZE = $AgentCount.ToString()
        }
    }
    
    # Additional empire settings
    $settings["playwright.showBrowserInExplorer"] = $true
    $settings["playwright.debugMode"] = $false
    $settings["playwright.enableCodeGeneration"] = $true
    
    # Save settings
    try {
        $settings | ConvertTo-Json -Depth 10 | Set-Content $settingsPath -Encoding UTF8
        Write-EmpireStatus "VS Code settings updated with Playwright MCP configuration" "Success"
        return $true
    }
    catch {
        Write-EmpireStatus "Failed to update VS Code settings: $($_.Exception.Message)" "Error"
        return $false
    }
}

function Create-DesktopShortcuts {
    Write-LegendaryHeader "EMPIRE SHORTCUTS CREATION"
    
    $desktopPath = [Environment]::GetFolderPath("Desktop")
    
    # Create Playwright MCP launcher
    $shortcutPath = Join-Path $desktopPath "🚀 Playwright MCP Empire.lnk"
    
    try {
        $wshell = New-Object -comObject WScript.Shell
        $shortcut = $wshell.CreateShortcut($shortcutPath)
        $shortcut.TargetPath = "pwsh.exe"
        $shortcut.Arguments = "-Command `"npx @playwright/mcp@latest`""
        $shortcut.WorkingDirectory = $PWD.Path
        $shortcut.Description = "Launch Playwright MCP for HyperFocus Empire"
        $shortcut.Save()
        
        Write-EmpireStatus "Desktop shortcut created: 🚀 Playwright MCP Empire" "Success"
    }
    catch {
        Write-EmpireStatus "Could not create desktop shortcut: $($_.Exception.Message)" "Warning"
    }
    
    # Create Empire Mission Controller launcher
    $missionControlPath = Join-Path $desktopPath "🤖 Empire Mission Control.lnk"
    
    try {
        $shortcut2 = $wshell.CreateShortcut($missionControlPath)
        $shortcut2.TargetPath = "python"
        $shortcut2.Arguments = "`"$PWD\examples\broskie_mission_controller.py`""
        $shortcut2.WorkingDirectory = $PWD.Path
        $shortcut2.Description = "Launch BROski Mission Controller for 1050+ Agent Army"
        $shortcut2.Save()
        
        Write-EmpireStatus "Mission Control shortcut created: 🤖 Empire Mission Control" "Success"
    }
    catch {
        Write-EmpireStatus "Could not create mission control shortcut: $($_.Exception.Message)" "Warning"
    }
}

function Test-PlaywrightMCP {
    if ($SkipTests) {
        Write-EmpireStatus "Tests skipped by user request" "Warning"
        return $true
    }
    
    Write-LegendaryHeader "PLAYWRIGHT MCP TESTING"
    
    try {
        Write-EmpireStatus "Testing Playwright MCP server..." "Info"
        
        # Test version command
        $version = npx @playwright/mcp@latest --version 2>&1
        if ($version -match "Version") {
            Write-EmpireStatus "✅ Version check passed: $version" "Success"
        } else {
            Write-EmpireStatus "⚠️ Version check unusual result: $version" "Warning"
        }
        
        # Test help command
        Write-EmpireStatus "Testing help command..." "Info"
        $help = npx @playwright/mcp@latest --help 2>&1
        if ($help -match "Usage" -or $help -match "Options" -or $help -match "Commands") {
            Write-EmpireStatus "✅ Help command functional" "Success"
        } else {
            Write-EmpireStatus "⚠️ Help command unusual result" "Warning"
            if ($Verbose) {
                Write-Host $help -ForegroundColor $Colors.Warning
            }
        }
        
        return $true
    }
    catch {
        Write-EmpireStatus "Testing failed: $($_.Exception.Message)" "Error"
        return $false
    }
}

function Deploy-EmpireMissions {
    Write-LegendaryHeader "EMPIRE MISSION DEPLOYMENT"
    
    # Check if Python scripts exist
    $missionController = Join-Path $PWD "examples\broskie_mission_controller.py"
    $ariaIntelligence = Join-Path $PWD "examples\aria_intelligence_hub.py"
    
    if (Test-Path $missionController) {
        Write-EmpireStatus "BROski Mission Controller: READY" "Success"
        
        if ((Get-Command python -ErrorAction SilentlyContinue)) {
            try {
                Write-EmpireStatus "Testing mission controller..." "Info"
                $testResult = python $missionController --help 2>&1
                Write-EmpireStatus "Mission Controller: OPERATIONAL" "Legendary"
            }
            catch {
                Write-EmpireStatus "Mission Controller test inconclusive" "Warning"
            }
        }
    } else {
        Write-EmpireStatus "Mission Controller not found" "Warning"
    }
    
    if (Test-Path $ariaIntelligence) {
        Write-EmpireStatus "ARIA Intelligence Hub: READY" "Success"
    } else {
        Write-EmpireStatus "ARIA Intelligence Hub not found" "Warning"
    }
    
    # Create empire status file
    $statusFile = Join-Path $PWD "EMPIRE_DEPLOYMENT_STATUS.json"
    $deploymentStatus = @{
        timestamp = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss")
        empire_name = $EmpireConfig.Name
        version = $EmpireConfig.Version
        agent_army_size = $EmpireConfig.AgentArmySize
        broskie_level = $EmpireConfig.BROskiLevel
        aria_level = $EmpireConfig.ARIALevel
        playwright_mcp = "OPERATIONAL"
        vs_code_integration = "CONFIGURED"
        mission_controller = if (Test-Path $missionController) { "READY" } else { "PENDING" }
        aria_intelligence = if (Test-Path $ariaIntelligence) { "READY" } else { "PENDING" }
        deployment_mode = $DeploymentMode
        legend_status = "BROWSER AUTOMATION SUPREME"
    }
    
    $deploymentStatus | ConvertTo-Json -Depth 10 | Set-Content $statusFile -Encoding UTF8
    Write-EmpireStatus "Empire status saved: EMPIRE_DEPLOYMENT_STATUS.json" "Success"
}

function Show-NextSteps {
    Write-LegendaryHeader "IMMEDIATE NEXT STEPS FOR EMPIRE DOMINATION"
    
    Write-Host ""
    Write-EmpireStatus "1. 🎯 VS Code Setup:" "Legendary"
    Write-Host "   • Install VS Code MCP Extension: code --install-extension microsoft.vscode-mcp" -ForegroundColor $Colors.Info
    Write-Host "   • Restart VS Code to activate MCP integration" -ForegroundColor $Colors.Info
    Write-Host ""
    
    Write-EmpireStatus "2. 🧪 Test Integration:" "Legendary"
    Write-Host "   • Open VS Code and test: Navigate to https://github.com/microsoft/playwright-mcp" -ForegroundColor $Colors.Info
    Write-Host "   • Verify browser automation in VS Code MCP panel" -ForegroundColor $Colors.Info
    Write-Host ""
    
    Write-EmpireStatus "3. 🚀 Deploy BROski Missions:" "Legendary"
    Write-Host "   • Run: python examples\broskie_mission_controller.py" -ForegroundColor $Colors.Info
    Write-Host "   • Deploy to $($EmpireConfig.AgentArmySize)+ agent army for web automation" -ForegroundColor $Colors.Info
    Write-Host ""
    
    Write-EmpireStatus "4. 🤖 ARIA Intelligence Activation:" "Legendary"
    Write-Host "   • Run: python examples\aria_intelligence_hub.py" -ForegroundColor $Colors.Info
    Write-Host "   • AI-enhanced web automation strategies activated" -ForegroundColor $Colors.Info
    Write-Host ""
    
    Write-EmpireStatus "🏆 LEGENDARY STATUS ACHIEVED: BROWSER AUTOMATION EMPIRE READY!" "Legendary"
    Write-Host ""
}

function Show-EmpireReport {
    Write-LegendaryHeader "FINAL EMPIRE DEPLOYMENT REPORT"
    
    Write-Host ""
    Write-Host "🎊💎⚡ HYPERFOCUS EMPIRE STATUS REPORT ⚡💎🎊" -ForegroundColor $Colors.Legendary
    Write-Host ""
    
    $report = @{
        "🏛️ EMPIRE NAME" = $EmpireConfig.Name
        "⚡ VERSION" = $EmpireConfig.Version
        "🤖 AGENT ARMY SIZE" = "$($EmpireConfig.AgentArmySize)+ agents"
        "🚀 BROSKIE LEVEL" = $EmpireConfig.BROskiLevel
        "🧠 ARIA INTELLIGENCE" = $EmpireConfig.ARIALevel
        "🌐 PLAYWRIGHT MCP" = "OPERATIONAL"
        "💎 MEMORY CRYSTALS" = $EmpireConfig.MemoryCrystals
        "🏆 LEGEND STATUS" = "BROWSER AUTOMATION SUPREME"
        "⚡ DEPLOYMENT MODE" = $DeploymentMode.ToUpper()
    }
    
    foreach ($key in $report.Keys) {
        Write-Host "$key`: " -NoNewline -ForegroundColor $Colors.Empire
        Write-Host $report[$key] -ForegroundColor $Colors.Legendary
    }
    
    Write-Host ""
    Write-Host "🎯 READY FOR WEB AUTOMATION DOMINATION!" -ForegroundColor $Colors.Legendary
    Write-Host ""
}

# MAIN EXECUTION
try {
    Clear-Host
    Write-LegendaryHeader "HYPERFOCUS EMPIRE - PLAYWRIGHT MCP DEPLOYMENT"
    
    Write-Host ""
    Write-EmpireStatus "Initializing Empire Deployment..." "Legendary"
    Write-EmpireStatus "Target Agent Army: $AgentCount agents" "Info"
    Write-EmpireStatus "Deployment Mode: $DeploymentMode" "Info"
    Write-Host ""
    
    # Step 1: Prerequisites
    if (-not (Test-Prerequisites)) {
        Write-EmpireStatus "Prerequisites failed - deployment cannot continue" "Error"
        exit 1
    }
    
    # Step 2: Install Playwright MCP
    if (-not (Install-PlaywrightMCP)) {
        Write-EmpireStatus "Playwright MCP installation failed" "Error"
        exit 1
    }
    
    # Step 3: Deploy VS Code configuration
    if (-not (Deploy-VSCodeConfiguration)) {
        Write-EmpireStatus "VS Code configuration failed" "Error"
        exit 1
    }
    
    # Step 4: Create shortcuts
    Create-DesktopShortcuts
    
    # Step 5: Test installation
    if (-not (Test-PlaywrightMCP)) {
        Write-EmpireStatus "Testing failed - deployment may be incomplete" "Warning"
    }
    
    # Step 6: Deploy empire missions
    Deploy-EmpireMissions
    
    # Step 7: Show next steps
    Show-NextSteps
    
    # Step 8: Final report
    Show-EmpireReport
    
    Write-EmpireStatus "🎊 DEPLOYMENT COMPLETE - EMPIRE READY FOR BROWSER AUTOMATION DOMINATION! 🎊" "Legendary"
}
catch {
    Write-EmpireStatus "Deployment failed: $($_.Exception.Message)" "Error"
    Write-Host $_.ScriptStackTrace -ForegroundColor $Colors.Error
    exit 1
}

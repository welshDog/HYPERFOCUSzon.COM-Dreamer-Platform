# 🚀💎⚡ HYPERFOCUS PORTAL LAUNCHER ⚡💎🚀
# PowerShell script to safely launch all empire portals
# Chief Lyndz Empire Portal Management System

Write-Host "🚀💎⚡ HYPERFOCUS EMPIRE PORTAL LAUNCHER ⚡💎🚀" -ForegroundColor Green
Write-Host "=" * 60 -ForegroundColor Cyan
Write-Host ""

# Define all available portals with safe paths
$portals = @{
    "1" = @{
        "Name" = "🤖 Agent Army Coordination Hub"
        "Path" = "H:\AGENT_ARMY_COORDINATION_HUB.html"
        "Description" = "1,050+ Agent coordination system"
    }
    "2" = @{
        "Name" = "💰 Money Empire Dashboard" 
        "Path" = "H:\💰🚀_HYPERFOCUS_MONEY_EMPIRE_DASHBOARD_🚀💰.html"
        "Description" = "Automated revenue tracking"
    }
    "3" = @{
        "Name" = "📊 Performance Dashboard"
        "Path" = "H:\HYPERFOCUS_PERFORMANCE_DASHBOARD.html"
        "Description" = "Live metrics & benchmarking"
    }
    "4" = @{
        "Name" = "🌐 Portal Master Dashboard"
        "Path" = "H:\🌐👑💎⚡_PORTAL_MASTER_DASHBOARD_⚡💎👑🌐.html"
        "Description" = "Multi-portal management system"
    }
    "5" = @{
        "Name" = "💎 Ultra dOoK Portal (Running)"
        "Path" = "http://localhost:3456"
        "Description" = "8-tab quantum interface (LIVE)"
    }
}

# Display menu
Write-Host "🎯 Available Empire Portals:" -ForegroundColor Yellow
Write-Host ""
foreach ($key in $portals.Keys | Sort-Object) {
    $portal = $portals[$key]
    Write-Host "[$key] $($portal.Name)" -ForegroundColor Green
    Write-Host "    📄 $($portal.Description)" -ForegroundColor Gray
    Write-Host "    🔗 $($portal.Path)" -ForegroundColor DarkGray
    Write-Host ""
}

Write-Host "[A] Launch ALL Portals 🚀" -ForegroundColor Magenta
Write-Host "[Q] Quit" -ForegroundColor Red
Write-Host ""

# Get user choice
$choice = Read-Host "🎮 Choose portal to launch"

# Function to safely launch portal
function Launch-Portal {
    param(
        [string]$Name,
        [string]$Path
    )
    
    Write-Host "🚀 Launching: $Name" -ForegroundColor Green
    
    if ([string]::IsNullOrEmpty($Path)) {
        Write-Host "❌ ERROR: Empty file path!" -ForegroundColor Red
        return $false
    }
    
    if (Test-Path $Path) {
        try {
            Write-Host "✅ File found: $Path" -ForegroundColor Green
            Start-Process $Path -ErrorAction Stop
            Write-Host "🎊 SUCCESS: $Name launched!" -ForegroundColor Green
            return $true
        }
        catch {
            Write-Host "❌ ERROR launching $Name : $($_.Exception.Message)" -ForegroundColor Red
            return $false
        }
    }
    elseif ($Path.StartsWith("http")) {
        try {
            Write-Host "🌐 Opening URL: $Path" -ForegroundColor Green
            Start-Process $Path -ErrorAction Stop
            Write-Host "🎊 SUCCESS: $Name opened!" -ForegroundColor Green
            return $true
        }
        catch {
            Write-Host "❌ ERROR opening $Name : $($_.Exception.Message)" -ForegroundColor Red
            return $false
        }
    }
    else {
        Write-Host "❌ ERROR: File not found: $Path" -ForegroundColor Red
        return $false
    }
}

# Process user choice
switch ($choice.ToUpper()) {
    "A" {
        Write-Host "🚀 LAUNCHING ALL EMPIRE PORTALS!" -ForegroundColor Magenta
        Write-Host "=" * 40 -ForegroundColor Cyan
        
        $successCount = 0
        foreach ($key in $portals.Keys | Sort-Object) {
            $portal = $portals[$key]
            if (Launch-Portal -Name $portal.Name -Path $portal.Path) {
                $successCount++
            }
            Start-Sleep -Milliseconds 500
        }
        
        Write-Host ""
        Write-Host "🎊 LAUNCH COMPLETE!" -ForegroundColor Green
        Write-Host "✅ Successfully launched: $successCount/$($portals.Count) portals" -ForegroundColor Green
    }
    
    "Q" {
        Write-Host "👋 Goodbye Chief Lyndz! Your empire awaits!" -ForegroundColor Yellow
        exit
    }
    
    default {
        if ($portals.ContainsKey($choice)) {
            $portal = $portals[$choice]
            Launch-Portal -Name $portal.Name -Path $portal.Path
        }
        else {
            Write-Host "❌ Invalid choice: $choice" -ForegroundColor Red
        }
    }
}

Write-Host ""
Write-Host "🏆 HYPERFOCUS EMPIRE PORTAL LAUNCHER COMPLETE 🏆" -ForegroundColor Green
Write-Host "Press any key to exit..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

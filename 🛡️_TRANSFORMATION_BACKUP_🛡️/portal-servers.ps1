#!/usr/bin/env powershell
<#
🚀❤️‍🔥🪄 HYPERFOCUS ZONE PORTAL SERVER MANAGER 🪄❤️‍🔥🚀

This script manages all the HTTP servers needed for the portal ecosystem!

USAGE:
  .\portal-servers.ps1 start    # Start all portal servers
  .\portal-servers.ps1 stop     # Stop all servers
  .\portal-servers.ps1 status   # Check server status
  .\portal-servers.ps1 restart  # Restart all servers

🌟 NEURODIVERGENT-FRIENDLY AUTOMATION! 🌟
#>

param(
    [Parameter(Mandatory=$true)]
    [ValidateSet("start", "stop", "status", "restart")]
    [string]$Action
)

# Configuration
$WorkingDirectory = "h:\"
$Ports = @(8080, 8081, 8082)
$ProcessName = "python"

function Write-ColorOutput {
    param([string]$Message, [string]$Color = "White")
    Write-Host $Message -ForegroundColor $Color
}

function Start-PortalServers {
    Write-ColorOutput "🚀 Starting HyperFocus Zone Portal Servers..." "Green"

    foreach ($Port in $Ports) {
        $ExistingProcess = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue |
                          Where-Object { $_.ProcessName -eq $ProcessName -and
                                       (netstat -ano | Select-String ":$Port ") }

        if ($ExistingProcess) {
            Write-ColorOutput "⚡ Server already running on port $Port" "Yellow"
        } else {
            Write-ColorOutput "🌟 Starting server on port $Port..." "Cyan"
            Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$WorkingDirectory'; python -m http.server $Port" -WindowStyle Minimized
            Start-Sleep 2
        }
    }

    Write-ColorOutput "✅ All portal servers started successfully!" "Green"
    Write-ColorOutput "🌐 Access portals at: http://localhost:8080/portal-launcher.html" "Magenta"
}

function Stop-PortalServers {
    Write-ColorOutput "🛑 Stopping HyperFocus Zone Portal Servers..." "Red"

    foreach ($Port in $Ports) {
        $ProcessIds = netstat -ano | Select-String ":$Port " | ForEach-Object {
            ($_ -split '\s+')[-1]
        }

        foreach ($ProcessId in $ProcessIds) {
            if ($ProcessId -and $ProcessId -ne "0") {
                try {
                    Stop-Process -Id $ProcessId -Force -ErrorAction SilentlyContinue
                    Write-ColorOutput "❌ Stopped server on port $Port (PID: $ProcessId)" "Yellow"
                } catch {
                    Write-ColorOutput "⚠️ Could not stop process $ProcessId" "Red"
                }
            }
        }
    }

    Write-ColorOutput "✅ All portal servers stopped!" "Green"
}

function Get-ServerStatus {
    Write-ColorOutput "🔍 Checking HyperFocus Zone Portal Server Status..." "Cyan"
    Write-ColorOutput "═══════════════════════════════════════════════════" "Gray"

    $OnlineCount = 0

    foreach ($Port in $Ports) {
        try {
            $Response = Invoke-WebRequest -Uri "http://localhost:$Port" -TimeoutSec 3 -ErrorAction Stop
            Write-ColorOutput "✅ Port ${Port}: ONLINE" "Green"
            $OnlineCount++
        } catch {
            Write-ColorOutput "❌ Port ${Port}: OFFLINE" "Red"
        }
    }

    Write-ColorOutput "═══════════════════════════════════════════════════" "Gray"

    if ($OnlineCount -eq $Ports.Count) {
        Write-ColorOutput "🎉 ALL SYSTEMS ONLINE! Ready for hyperfocus!" "Green"
        Write-ColorOutput "🌟 Portal Launcher: http://localhost:8080/portal-launcher.html" "Magenta"
    } elseif ($OnlineCount -gt 0) {
        Write-ColorOutput "⚠️ $OnlineCount/$($Ports.Count) servers online. Some portals may be unavailable." "Yellow"
    } else {
        Write-ColorOutput "❌ No servers online. Run 'start' to activate portals." "Red"
    }
}

function Restart-PortalServers {
    Write-ColorOutput "🔄 Restarting HyperFocus Zone Portal Servers..." "Cyan"
    Stop-PortalServers
    Start-Sleep 3
    Start-PortalServers
}

# Main execution
switch ($Action) {
    "start" {
        Start-PortalServers
    }
    "stop" {
        Stop-PortalServers
    }
    "status" {
        Get-ServerStatus
    }
    "restart" {
        Restart-PortalServers
    }
}

Write-ColorOutput "`n🚀 HYPERFOCUS ZONE PORTAL MANAGEMENT COMPLETE! 🚀" "Magenta"

# HyperFocus Zone Portal Server Manager
# Simple server management for the portal ecosystem

param(
    [Parameter(Mandatory=$true)]
    [ValidateSet("start", "stop", "status", "restart")]
    [string]$Action
)

$WorkingDirectory = "h:\"
$Ports = @(8080, 8081, 8082)

function Start-PortalServers {
    Write-Host "Starting HyperFocus Zone Portal Servers..." -ForegroundColor Green

    foreach ($Port in $Ports) {
        Write-Host "Starting server on port $Port..." -ForegroundColor Cyan
        Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$WorkingDirectory'; python -m http.server $Port" -WindowStyle Minimized
        Start-Sleep 2
    }

    Write-Host "All portal servers started!" -ForegroundColor Green
    Write-Host "Access portals at: http://localhost:8080/portal-launcher.html" -ForegroundColor Magenta
}

function Stop-PortalServers {
    Write-Host "Stopping HyperFocus Zone Portal Servers..." -ForegroundColor Red

    foreach ($Port in $Ports) {
        $ProcessIds = netstat -ano | Select-String ":$Port " | ForEach-Object {
            ($_ -split '\s+')[-1]
        }

        foreach ($ProcessId in $ProcessIds) {
            if ($ProcessId -and $ProcessId -ne "0") {
                try {
                    Stop-Process -Id $ProcessId -Force -ErrorAction SilentlyContinue
                    Write-Host "Stopped server on port $Port (PID: $ProcessId)" -ForegroundColor Yellow
                } catch {
                    Write-Host "Could not stop process $ProcessId" -ForegroundColor Red
                }
            }
        }
    }

    Write-Host "All portal servers stopped!" -ForegroundColor Green
}

function Get-ServerStatus {
    Write-Host "Checking HyperFocus Zone Portal Server Status..." -ForegroundColor Cyan
    Write-Host "=================================================" -ForegroundColor Gray

    $OnlineCount = 0

    foreach ($Port in $Ports) {
        try {
            $Response = Invoke-WebRequest -Uri "http://localhost:$Port" -TimeoutSec 3 -ErrorAction Stop
            Write-Host "Port ${Port}: ONLINE" -ForegroundColor Green
            $OnlineCount++
        } catch {
            Write-Host "Port ${Port}: OFFLINE" -ForegroundColor Red
        }
    }

    Write-Host "=================================================" -ForegroundColor Gray

    if ($OnlineCount -eq $Ports.Count) {
        Write-Host "ALL SYSTEMS ONLINE! Ready for hyperfocus!" -ForegroundColor Green
        Write-Host "Portal Launcher: http://localhost:8080/portal-launcher.html" -ForegroundColor Magenta
    } elseif ($OnlineCount -gt 0) {
        Write-Host "$OnlineCount/$($Ports.Count) servers online. Some portals may be unavailable." -ForegroundColor Yellow
    } else {
        Write-Host "No servers online. Run 'start' to activate portals." -ForegroundColor Red
    }
}

function Restart-PortalServers {
    Write-Host "Restarting HyperFocus Zone Portal Servers..." -ForegroundColor Cyan
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

Write-Host "`nHYPERFOCUS ZONE PORTAL MANAGEMENT COMPLETE!" -ForegroundColor Magenta

#!/usr/bin/env powershell
<#
🧪💎⚡ DEVELOPMENT SERVER LAUNCHER ⚡💎🧪

Launches development servers for ready repositories
Tests each server for proper operation

Created: August 20, 2025
Status: DEV SERVER TESTING ENGINE
#>

Write-Host "🌌 🧪💎⚡ DEVELOPMENT SERVER LAUNCHER ⚡💎🧪" -ForegroundColor Cyan
Write-Host "🌌 " + "=" * 50 -ForegroundColor Cyan

function Start-DevServer {
    param(
        [string]$RepoPath,
        [string]$RepoName,
        [int]$Port
    )

    Write-Host "🚀 Starting dev server: $RepoName" -ForegroundColor Yellow

    if (-not (Test-Path $RepoPath)) {
        Write-Host "   ❌ Repository path not found: $RepoPath" -ForegroundColor Red
        return $false
    }

    $packageJson = Join-Path $RepoPath "package.json"
    if (-not (Test-Path $packageJson)) {
        Write-Host "   ❌ package.json not found" -ForegroundColor Red
        return $false
    }

    try {
        Push-Location $RepoPath

        # Check if dev script exists
        $packageContent = Get-Content "package.json" -Raw | ConvertFrom-Json
        if (-not ($packageContent.scripts -and $packageContent.scripts.dev)) {
            Write-Host "   ❌ No dev script found in package.json" -ForegroundColor Red
            return $false
        }

        Write-Host "   📝 Dev script: $($packageContent.scripts.dev)" -ForegroundColor Gray

        # Check if port is available
        $portInUse = Get-NetTCPConnection -LocalPort $Port -ErrorAction SilentlyContinue
        if ($portInUse) {
            Write-Host "   ⚠️ Port $Port already in use - server may be running" -ForegroundColor Yellow
            return $true
        }

        # Start development server in background
        Write-Host "   🔄 Starting server on port $Port..." -ForegroundColor Yellow
        $job = Start-Job -ScriptBlock {
            param($path, $port)
            Set-Location $path
            $env:PORT = $port
            npm run dev
        } -ArgumentList $RepoPath, $Port

        # Wait a moment for server to start
        Start-Sleep -Seconds 3

        # Test if server is running
        $connection = Test-NetConnection -ComputerName "localhost" -Port $Port -WarningAction SilentlyContinue
        if ($connection.TcpTestSucceeded) {
            Write-Host "   ✅ Server started successfully on port $Port!" -ForegroundColor Green
            Write-Host "   🌐 Access at: http://localhost:$Port" -ForegroundColor Cyan
            return $true
        } else {
            Write-Host "   ⚠️ Server started but not responding on port $Port" -ForegroundColor Yellow
            return $false
        }

    }
    catch {
        Write-Host "   ❌ Error starting server: $($_.Exception.Message)" -ForegroundColor Red
        return $false
    }
    finally {
        Pop-Location
    }
}

function Test-ReadyRepositories {
    Write-Host "🔍 Testing ready repositories for dev server launch..." -ForegroundColor Cyan
    Write-Host ""

    $readyRepos = @(
        @{
            Name = "Web Frontend"
            Path = "h:\HYPERFOCUS-UNIFIED-EMPIRE\🧠 NEURODIVERGENT-TOOLS\neuro-social-platform\frontend\web"
            Port = 3000
        },
        @{
            Name = "Backend API"
            Path = "h:\HYPERFOCUS-UNIFIED-EMPIRE\🧠 NEURODIVERGENT-TOOLS\neuro-social-platform\backend"
            Port = 8000
        }
    )

    $successCount = 0
    $serverInfo = @()

    foreach ($repo in $readyRepos) {
        $nodeModules = Join-Path $repo.Path "node_modules"

        if (Test-Path $nodeModules) {
            Write-Host "📦 $($repo.Name): Dependencies ready, launching..." -ForegroundColor Green
            $success = Start-DevServer -RepoPath $repo.Path -RepoName $repo.Name -Port $repo.Port

            if ($success) {
                $successCount++
                $serverInfo += @{
                    Name = $repo.Name
                    Port = $repo.Port
                    URL = "http://localhost:$($repo.Port)"
                    Status = "RUNNING"
                }
            }
        } else {
            Write-Host "📦 $($repo.Name): Dependencies not ready, skipping..." -ForegroundColor Yellow
        }

        Write-Host ""
    }

    Write-Host "🌌 " + "=" * 50 -ForegroundColor Cyan
    Write-Host "🌌 🧪💎⚡ DEV SERVER LAUNCH COMPLETE! ⚡💎🧪" -ForegroundColor Green
    Write-Host "🌌 " + "=" * 50 -ForegroundColor Cyan
    Write-Host ""

    if ($successCount -gt 0) {
        Write-Host "🎉 Successfully launched $successCount development servers!" -ForegroundColor Green
        Write-Host ""
        Write-Host "🌐 ACTIVE DEVELOPMENT SERVERS:" -ForegroundColor Cyan

        foreach ($server in $serverInfo) {
            Write-Host "   • $($server.Name): $($server.URL)" -ForegroundColor Yellow
        }

        Write-Host ""
        Write-Host "🚀 Your legendary development environment is now ACTIVE!" -ForegroundColor Green
        Write-Host "💡 You can now test your applications and begin integration!" -ForegroundColor Yellow
    } else {
        Write-Host "⚠️ No servers could be started. Check repository dependencies." -ForegroundColor Yellow
    }
}

# Execute dev server testing
Test-ReadyRepositories

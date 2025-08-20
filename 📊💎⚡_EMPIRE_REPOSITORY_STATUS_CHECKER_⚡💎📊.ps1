#!/usr/bin/env powershell
<#
📊💎⚡ EMPIRE REPOSITORY STATUS CHECKER ⚡💎📊

Checks the status of all HyperFocus Zone Empire repositories
Verifies dependencies, health, and readiness for development

Created: August 20, 2025
Status: REPOSITORY HEALTH MONITORING
#>

Write-Host "🌌 📊💎⚡ EMPIRE REPOSITORY STATUS CHECKER ⚡💎📊" -ForegroundColor Cyan
Write-Host "🌌 " + "=" * 60 -ForegroundColor Cyan

# Function to check repository status
function Check-RepositoryStatus {
    param(
        [string]$RepoPath,
        [string]$RepoName
    )

    Write-Host "🔍 Checking: $RepoName" -ForegroundColor Cyan
    Write-Host "📁 Path: $RepoPath" -ForegroundColor Gray

    $packageJson = Join-Path $RepoPath "package.json"
    $nodeModules = Join-Path $RepoPath "node_modules"

    $status = @{
        HasPackageJson = Test-Path $packageJson
        HasNodeModules = Test-Path $nodeModules
        ModuleCount = 0
        PackageInfo = $null
        IsHealthy = $false
    }

    if ($status.HasPackageJson) {
        Write-Host "   ✅ package.json found" -ForegroundColor Green

        try {
            $packageContent = Get-Content $packageJson -Raw | ConvertFrom-Json
            $status.PackageInfo = $packageContent
            Write-Host "   📦 Project: $($packageContent.name)" -ForegroundColor Gray
            if ($packageContent.version) {
                Write-Host "   🏷️ Version: $($packageContent.version)" -ForegroundColor Gray
            }
        }
        catch {
            Write-Host "   ⚠️ Could not parse package.json" -ForegroundColor Yellow
        }
    } else {
        Write-Host "   ❌ No package.json found" -ForegroundColor Red
    }

    if ($status.HasNodeModules) {
        try {
            $modules = Get-ChildItem $nodeModules -ErrorAction SilentlyContinue
            $status.ModuleCount = ($modules | Measure-Object).Count
            Write-Host "   ✅ node_modules found ($($status.ModuleCount) packages)" -ForegroundColor Green
        }
        catch {
            Write-Host "   ⚠️ Could not count node_modules" -ForegroundColor Yellow
        }
    } else {
        Write-Host "   ❌ No node_modules found - dependencies not installed" -ForegroundColor Red
    }

    # Test if npm commands work in this directory
    if ($status.HasPackageJson) {
        try {
            Push-Location $RepoPath

            # Test npm ls to verify dependencies
            $npmls = npm ls --depth=0 --silent 2>$null
            if ($LASTEXITCODE -eq 0) {
                Write-Host "   ✅ Dependencies verified" -ForegroundColor Green
                $status.IsHealthy = $true
            } else {
                Write-Host "   ⚠️ Dependency issues detected" -ForegroundColor Yellow
            }

            # Check for common scripts
            if ($status.PackageInfo -and $status.PackageInfo.scripts) {
                $scripts = $status.PackageInfo.scripts | Get-Member -MemberType NoteProperty | Select-Object -ExpandProperty Name
                Write-Host "   🎯 Available scripts: $($scripts -join ', ')" -ForegroundColor Gray
            }
        }
        catch {
            Write-Host "   ❌ npm verification failed" -ForegroundColor Red
        }
        finally {
            Pop-Location
        }
    }

    Write-Host ""
    return $status
}

# Main execution
function Main {
    Write-Host "🎯 Starting Empire Repository Status Check..." -ForegroundColor Cyan
    Write-Host ""

    # Verify Node.js is available
    try {
        $nodeVersion = node --version
        $npmVersion = npm --version
        Write-Host "✅ Node.js $nodeVersion detected" -ForegroundColor Green
        Write-Host "✅ npm v$npmVersion detected" -ForegroundColor Green
        Write-Host ""
    }
    catch {
        Write-Host "❌ Node.js not found! Please install Node.js first." -ForegroundColor Red
        return
    }

    # Define empire repositories
    $repositories = @(
        @{
            Path = "h:\HYPERFOCUS-UNIFIED-EMPIRE\🧠 NEURODIVERGENT-TOOLS\neuro-social-platform\frontend\web"
            Name = "Neuro-Social Platform Web Frontend"
        },
        @{
            Path = "h:\HYPERFOCUS-UNIFIED-EMPIRE\🧠 NEURODIVERGENT-TOOLS\neuro-social-platform\frontend\mobile"
            Name = "Neuro-Social Platform Mobile Frontend"
        },
        @{
            Path = "h:\HYPERFOCUS-UNIFIED-EMPIRE\🧠 NEURODIVERGENT-TOOLS\neuro-social-platform\backend"
            Name = "Neuro-Social Platform Backend"
        },
        @{
            Path = "h:\HYPERFOCUS-UNIFIED-EMPIRE\🎮 APPLICATIONS\hyperfocus-hub-ts"
            Name = "HyperFocus Hub TypeScript"
        },
        @{
            Path = "h:\HYPERFOCUS-ZONE-NEURO-SOCIAL-DREAMER"
            Name = "HyperFocus Zone Neuro Social Dreamer"
        }
    )

    $results = @()
    $totalRepos = $repositories.Count
    $healthyRepos = 0

    foreach ($repo in $repositories) {
        $status = Check-RepositoryStatus -RepoPath $repo.Path -RepoName $repo.Name
        $results += @{
            Repository = $repo.Name
            Status = $status
        }

        if ($status.IsHealthy) {
            $healthyRepos++
        }
    }

    # Summary report
    Write-Host "🌌 " + "=" * 60 -ForegroundColor Cyan
    Write-Host "🌌 📊 EMPIRE STATUS SUMMARY 📊" -ForegroundColor Green
    Write-Host "🌌 " + "=" * 60 -ForegroundColor Cyan
    Write-Host ""

    $healthPercentage = [math]::Round(($healthyRepos / $totalRepos) * 100, 1)
    Write-Host "📊 Overall Health: $healthPercentage% ($healthyRepos/$totalRepos repositories)" -ForegroundColor $(if ($healthPercentage -ge 80) { "Green" } elseif ($healthPercentage -ge 60) { "Yellow" } else { "Red" })
    Write-Host ""

    foreach ($result in $results) {
        $statusIcon = if ($result.Status.IsHealthy) { "✅" } else { "❌" }
        $nodeModulesStatus = if ($result.Status.HasNodeModules) { "$($result.Status.ModuleCount) packages" } else { "Not installed" }

        Write-Host "$statusIcon $($result.Repository)" -ForegroundColor $(if ($result.Status.IsHealthy) { "Green" } else { "Red" })
        Write-Host "   📦 Dependencies: $nodeModulesStatus" -ForegroundColor Gray
    }

    Write-Host ""
    if ($healthPercentage -eq 100) {
        Write-Host "🎉 ALL SYSTEMS OPERATIONAL! Your empire is ready for legendary development!" -ForegroundColor Green
    } elseif ($healthPercentage -ge 80) {
        Write-Host "🚀 Empire status: EXCELLENT! Minor tweaks may be needed." -ForegroundColor Green
    } elseif ($healthPercentage -ge 60) {
        Write-Host "⚡ Empire status: GOOD! Some repositories need attention." -ForegroundColor Yellow
    } else {
        Write-Host "🔧 Empire status: NEEDS WORK! Multiple repositories require setup." -ForegroundColor Red
    }
}

# Execute main function
Main

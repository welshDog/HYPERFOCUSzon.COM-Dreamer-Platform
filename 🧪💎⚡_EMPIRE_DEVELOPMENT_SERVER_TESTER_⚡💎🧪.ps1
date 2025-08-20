#!/usr/bin/env powershell
<#
🧪💎⚡ EMPIRE DEVELOPMENT SERVER TESTER ⚡💎🧪

Tests development servers across all empire repositories
Validates npm scripts and development environment readiness

Created: August 20, 2025
Status: DEVELOPMENT SERVER VALIDATION ENGINE
#>

Write-Host "🌌 🧪💎⚡ EMPIRE DEVELOPMENT SERVER TESTER ⚡💎🧪" -ForegroundColor Cyan
Write-Host "🌌 " + "=" * 60 -ForegroundColor Cyan

# Function to test repository development capabilities
function Test-RepositoryDevelopmentServer {
    param(
        [string]$RepoPath,
        [string]$RepoName
    )

    Write-Host "🧪 Testing: $RepoName" -ForegroundColor Cyan
    Write-Host "📁 Path: $RepoPath" -ForegroundColor Gray

    $packageJson = Join-Path $RepoPath "package.json"
    $nodeModules = Join-Path $RepoPath "node_modules"

    if (-not (Test-Path $packageJson)) {
        Write-Host "   ❌ No package.json found" -ForegroundColor Red
        return $false
    }

    if (-not (Test-Path $nodeModules)) {
        Write-Host "   ❌ Dependencies not installed" -ForegroundColor Red
        return $false
    }

    try {
        Push-Location $RepoPath

        # Read package.json to check available scripts
        $packageContent = Get-Content $packageJson -Raw | ConvertFrom-Json

        Write-Host "   📦 Project: $($packageContent.name) v$($packageContent.version)" -ForegroundColor Gray

        if ($packageContent.scripts) {
            $scripts = $packageContent.scripts | Get-Member -MemberType NoteProperty | Select-Object -ExpandProperty Name
            Write-Host "   🎯 Available scripts: $($scripts -join ', ')" -ForegroundColor Yellow

            # Test common development scripts
            $devScripts = @("dev", "start", "serve", "develop")
            $buildScripts = @("build", "compile", "dist")
            $testScripts = @("test", "test:unit", "jest")

            $hasDevScript = $false
            $hasBuildScript = $false
            $hasTestScript = $false

            foreach ($script in $scripts) {
                if ($script -in $devScripts) {
                    Write-Host "   ✅ Development script found: $script" -ForegroundColor Green
                    $hasDevScript = $true

                    # Test if the script can be validated (dry run)
                    Write-Host "   🔍 Validating development environment..." -ForegroundColor Yellow
                    $npmList = npm list --depth=0 --silent 2>$null
                    if ($LASTEXITCODE -eq 0) {
                        Write-Host "   ✅ Dependencies validated successfully" -ForegroundColor Green
                    } else {
                        Write-Host "   ⚠️ Some dependency issues detected" -ForegroundColor Yellow
                    }
                }

                if ($script -in $buildScripts) {
                    Write-Host "   ✅ Build script found: $script" -ForegroundColor Green
                    $hasBuildScript = $true
                }

                if ($script -in $testScripts) {
                    Write-Host "   ✅ Test script found: $script" -ForegroundColor Green
                    $hasTestScript = $true
                }
            }

            # Overall readiness assessment
            $readinessScore = 0
            if ($hasDevScript) { $readinessScore += 40 }
            if ($hasBuildScript) { $readinessScore += 30 }
            if ($hasTestScript) { $readinessScore += 20 }
            if ((Test-Path "node_modules")) { $readinessScore += 10 }

            $status = switch ($readinessScore) {
                { $_ -ge 80 } { "🏆 FULLY READY" }
                { $_ -ge 60 } { "✅ READY" }
                { $_ -ge 40 } { "⚡ PARTIALLY READY" }
                default { "🔧 NEEDS SETUP" }
            }

            Write-Host "   📊 Development Readiness: $status ($readinessScore%)" -ForegroundColor $(
                if ($readinessScore -ge 80) { "Green" }
                elseif ($readinessScore -ge 60) { "Green" }
                elseif ($readinessScore -ge 40) { "Yellow" }
                else { "Red" }
            )

        } else {
            Write-Host "   ⚠️ No scripts defined in package.json" -ForegroundColor Yellow
        }

        return $readinessScore -ge 40

    }
    catch {
        Write-Host "   ❌ Error testing repository: $($_.Exception.Message)" -ForegroundColor Red
        return $false
    }
    finally {
        Pop-Location
    }

    Write-Host ""
}

# Function to generate development commands for ready repositories
function Generate-DevelopmentCommands {
    param(
        [array]$ReadyRepos
    )

    Write-Host "🚀 Development Server Commands:" -ForegroundColor Cyan
    Write-Host ""

    foreach ($repo in $ReadyRepos) {
        Write-Host "📦 $($repo.Name):" -ForegroundColor Yellow
        Write-Host "   📁 cd `"$($repo.Path)`"" -ForegroundColor Gray

        try {
            $packageJson = Join-Path $repo.Path "package.json"
            $packageContent = Get-Content $packageJson -Raw | ConvertFrom-Json

            if ($packageContent.scripts) {
                $scripts = $packageContent.scripts | Get-Member -MemberType NoteProperty | Select-Object -ExpandProperty Name

                # Suggest the best development command
                $devCommand = $null
                if ("dev" -in $scripts) { $devCommand = "npm run dev" }
                elseif ("start" -in $scripts) { $devCommand = "npm start" }
                elseif ("serve" -in $scripts) { $devCommand = "npm run serve" }
                elseif ("develop" -in $scripts) { $devCommand = "npm run develop" }

                if ($devCommand) {
                    Write-Host "   🚀 Development: $devCommand" -ForegroundColor Green
                }

                # Suggest build command
                $buildCommand = $null
                if ("build" -in $scripts) { $buildCommand = "npm run build" }
                elseif ("compile" -in $scripts) { $buildCommand = "npm run compile" }

                if ($buildCommand) {
                    Write-Host "   🏗️ Build: $buildCommand" -ForegroundColor Blue
                }

                # Suggest test command
                $testCommand = $null
                if ("test" -in $scripts) { $testCommand = "npm test" }
                elseif ("test:unit" -in $scripts) { $testCommand = "npm run test:unit" }

                if ($testCommand) {
                    Write-Host "   🧪 Test: $testCommand" -ForegroundColor Purple
                }
            }
        }
        catch {
            Write-Host "   ⚠️ Could not analyze scripts" -ForegroundColor Yellow
        }

        Write-Host ""
    }
}

# Main execution
function Main {
    Write-Host "🎯 Starting Empire Development Server Testing..." -ForegroundColor Cyan
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

    # Define all empire repositories
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

    $readyRepos = @()
    $totalReadiness = 0

    foreach ($repo in $repositories) {
        $isReady = Test-RepositoryDevelopmentServer -RepoPath $repo.Path -RepoName $repo.Name
        if ($isReady) {
            $readyRepos += $repo
        }
    }

    $readyPercentage = [math]::Round(($readyRepos.Count / $repositories.Count) * 100, 1)

    Write-Host "🌌 " + "=" * 60 -ForegroundColor Cyan
    Write-Host "🌌 🧪 DEVELOPMENT SERVER TEST RESULTS 🧪" -ForegroundColor Green
    Write-Host "🌌 " + "=" * 60 -ForegroundColor Cyan
    Write-Host ""

    Write-Host "📊 Development Readiness: $readyPercentage% ($($readyRepos.Count)/$($repositories.Count) repositories)" -ForegroundColor $(
        if ($readyPercentage -ge 80) { "Green" }
        elseif ($readyPercentage -ge 60) { "Yellow" }
        else { "Red" }
    )
    Write-Host ""

    if ($readyRepos.Count -gt 0) {
        Generate-DevelopmentCommands -ReadyRepos $readyRepos

        Write-Host "🎉 Next Steps for Development:" -ForegroundColor Green
        Write-Host "   1. Choose a repository and navigate to its directory" -ForegroundColor Gray
        Write-Host "   2. Run the development command (npm run dev or npm start)" -ForegroundColor Gray
        Write-Host "   3. Open your browser to the displayed local URL" -ForegroundColor Gray
        Write-Host "   4. Start coding and see live changes!" -ForegroundColor Gray
    } else {
        Write-Host "🔧 No repositories are ready for development yet." -ForegroundColor Red
        Write-Host "📋 Please run dependency installation first." -ForegroundColor Yellow
    }

    Write-Host ""
    Write-Host "🌟 Empire Development Environment Status: TESTING COMPLETE!" -ForegroundColor Cyan
}

# Execute main function
Main

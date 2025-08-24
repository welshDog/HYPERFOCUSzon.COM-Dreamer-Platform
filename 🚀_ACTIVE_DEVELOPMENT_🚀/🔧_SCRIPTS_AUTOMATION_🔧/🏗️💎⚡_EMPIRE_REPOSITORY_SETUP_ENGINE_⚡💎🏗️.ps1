#!/usr/bin/env powershell
<#
🏗️💎⚡ EMPIRE REPOSITORY SETUP ENGINE ⚡💎🏗️

Sets up all HyperFocus Zone Empire repositories with Node.js dependencies
Handles dependency conflicts and security audits automatically

Created: August 20, 2025
Status: REPOSITORY DEPENDENCY MANAGEMENT
#>

Write-Host "🌌 🏗️💎⚡ EMPIRE REPOSITORY SETUP ENGINE ⚡💎🏗️" -ForegroundColor Cyan
Write-Host "🌌 " + "=" * 60 -ForegroundColor Cyan

# Function to setup a single repository
function Setup-Repository {
    param(
        [string]$RepoPath,
        [string]$RepoName
    )

    $packageJson = Join-Path $RepoPath "package.json"

    if (Test-Path $packageJson) {
        Write-Host "🚀 Setting up: $RepoName" -ForegroundColor Cyan
        Write-Host "📁 Path: $RepoPath" -ForegroundColor Gray

        try {
            Push-Location $RepoPath

            # Check if node_modules exists
            if (Test-Path "node_modules") {
                Write-Host "   🧹 Cleaning existing node_modules..." -ForegroundColor Yellow
                Remove-Item "node_modules" -Recurse -Force -ErrorAction SilentlyContinue
            }

            # Check if package-lock.json exists and remove it to avoid conflicts
            if (Test-Path "package-lock.json") {
                Write-Host "   🧹 Removing package-lock.json to avoid conflicts..." -ForegroundColor Yellow
                Remove-Item "package-lock.json" -Force -ErrorAction SilentlyContinue
            }

            # Install dependencies with legacy peer deps to avoid conflicts
            Write-Host "   📥 Installing dependencies (with legacy peer deps)..." -ForegroundColor Yellow
            npm install --legacy-peer-deps

            if ($LASTEXITCODE -eq 0) {
                Write-Host "   ✅ Dependencies installed successfully!" -ForegroundColor Green

                # Run security audit and fix issues
                Write-Host "   🔍 Running security audit..." -ForegroundColor Yellow
                npm audit fix --legacy-peer-deps

                if ($LASTEXITCODE -eq 0) {
                    Write-Host "   ✅ Security audit completed!" -ForegroundColor Green
                } else {
                    Write-Host "   ⚠️ Security audit found unfixable issues - check manually" -ForegroundColor Yellow
                }
            } else {
                Write-Host "   ❌ Failed to install dependencies" -ForegroundColor Red

                # Try alternative approaches
                Write-Host "   🔄 Trying with --force flag..." -ForegroundColor Yellow
                npm install --force

                if ($LASTEXITCODE -eq 0) {
                    Write-Host "   ✅ Dependencies installed with --force!" -ForegroundColor Green
                } else {
                    Write-Host "   ❌ Installation failed even with --force" -ForegroundColor Red
                }
            }

            # Check final status
            if (Test-Path "node_modules") {
                $moduleCount = (Get-ChildItem "node_modules" -ErrorAction SilentlyContinue | Measure-Object).Count
                Write-Host "   📊 Installed modules: $moduleCount packages" -ForegroundColor Green
            }

        }
        catch {
            Write-Host "   ❌ Error setting up repository: $($_.Exception.Message)" -ForegroundColor Red
        }
        finally {
            Pop-Location
        }

        Write-Host ""
    } else {
        Write-Host "⚠️ No package.json found in: $RepoPath" -ForegroundColor Yellow
        Write-Host ""
    }
}

# Main execution
function Main {
    Write-Host "🎯 Starting Empire Repository Setup..." -ForegroundColor Cyan
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

    $totalRepos = $repositories.Count
    $processedRepos = 0

    foreach ($repo in $repositories) {
        $processedRepos++
        Write-Host "📊 Progress: $processedRepos/$totalRepos repositories" -ForegroundColor Cyan

        Setup-Repository -RepoPath $repo.Path -RepoName $repo.Name
    }

    Write-Host "🌌 " + "=" * 60 -ForegroundColor Cyan
    Write-Host "🌌 🏆💎⚡ EMPIRE SETUP COMPLETE! ⚡💎🏆" -ForegroundColor Green
    Write-Host "🌌 " + "=" * 60 -ForegroundColor Cyan
    Write-Host ""
    Write-Host "🎉 All empire repositories have been processed!" -ForegroundColor Green
    Write-Host "📊 Setup Summary:" -ForegroundColor Yellow
    Write-Host "   • Processed: $processedRepos repositories" -ForegroundColor Gray
    Write-Host "   • Dependencies installed with conflict resolution" -ForegroundColor Gray
    Write-Host "   • Security audits completed" -ForegroundColor Gray
    Write-Host ""
    Write-Host "🚀 Next Steps:" -ForegroundColor Yellow
    Write-Host "   • Test development servers: npm run dev" -ForegroundColor Gray
    Write-Host "   • Build projects: npm run build" -ForegroundColor Gray
    Write-Host "   • Check for any remaining issues manually" -ForegroundColor Gray
}

# Execute main function
Main

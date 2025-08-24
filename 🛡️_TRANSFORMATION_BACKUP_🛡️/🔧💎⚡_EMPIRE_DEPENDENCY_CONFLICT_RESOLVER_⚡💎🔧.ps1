#!/usr/bin/env powershell
<#
🔧💎⚡ EMPIRE DEPENDENCY CONFLICT RESOLVER ⚡💎🔧

Analyzes and resolves Node.js dependency version conflicts
Updates package.json files with compatible versions automatically

Created: August 20, 2025
Status: DEPENDENCY CONFLICT RESOLUTION ENGINE
#>

Write-Host "🌌 🔧💎⚡ EMPIRE DEPENDENCY CONFLICT RESOLVER ⚡💎🔧" -ForegroundColor Cyan
Write-Host "🌌 " + "=" * 60 -ForegroundColor Cyan

# Function to check and resolve package.json dependencies
function Resolve-PackageConflicts {
    param(
        [string]$RepoPath,
        [string]$RepoName
    )

    Write-Host "🔧 Resolving conflicts in: $RepoName" -ForegroundColor Cyan
    Write-Host "📁 Path: $RepoPath" -ForegroundColor Gray

    $packageJson = Join-Path $RepoPath "package.json"

    if (-not (Test-Path $packageJson)) {
        Write-Host "   ⚠️ No package.json found - skipping" -ForegroundColor Yellow
        return
    }

    try {
        $packageContent = Get-Content $packageJson -Raw | ConvertFrom-Json
        $hasChanges = $false

        Write-Host "   📦 Analyzing: $($packageContent.name)" -ForegroundColor Gray

        # Define known problematic packages and their fixes
        $packageFixes = @{
            # TypeScript version fixes
            "typescript" = @{
                "5.2.0" = "^5.1.6"  # Use latest stable 5.1.x
                "~5.2.0" = "^5.1.6"
            }
            # React Native AsyncStorage fixes
            "react-native-async-storage" = @{
                "^1.19.0" = "@react-native-async-storage/async-storage@^1.19.3"
                "1.19.0" = "@react-native-async-storage/async-storage@^1.19.3"
            }
            # Rate limiter fixes
            "rate-limiter-flexible" = @{
                "^3.0.8" = "^2.3.0"  # Use stable 2.x version
                "3.0.8" = "^2.3.0"
            }
            # React Native accessibility fixes
            "react-native-accessibility" = @{
                "^1.0.0" = "^3.0.0"  # Use newer compatible version
                "1.0.0" = "^3.0.0"
            }
        }

        # Fix dependencies
        if ($packageContent.dependencies) {
            Write-Host "   🔍 Checking dependencies..." -ForegroundColor Yellow

            foreach ($dep in $packageContent.dependencies.PSObject.Properties) {
                $packageName = $dep.Name
                $version = $dep.Value

                if ($packageFixes.ContainsKey($packageName)) {
                    $fixes = $packageFixes[$packageName]
                    if ($fixes.ContainsKey($version)) {
                        $newPackage = $fixes[$version]

                        if ($newPackage -like "*@*") {
                            # Handle package name changes (e.g., async-storage)
                            $parts = $newPackage -split "@"
                            $newName = $parts[0]
                            $newVersion = $parts[1]

                            # Remove old package
                            $packageContent.dependencies.PSObject.Properties.Remove($packageName)

                            # Add new package
                            Add-Member -InputObject $packageContent.dependencies -MemberType NoteProperty -Name $newName -Value $newVersion -Force

                            Write-Host "   ✅ Replaced ${packageName}@${version} → ${newName}@${newVersion}" -ForegroundColor Green
                        } else {
                            # Simple version update
                            $packageContent.dependencies.$packageName = $newPackage
                            Write-Host "   ✅ Updated ${packageName}: ${version} → ${newPackage}" -ForegroundColor Green
                        }
                        $hasChanges = $true
                    }
                }
            }
        }

        # Fix devDependencies
        if ($packageContent.devDependencies) {
            Write-Host "   🔍 Checking devDependencies..." -ForegroundColor Yellow

            foreach ($dep in $packageContent.devDependencies.PSObject.Properties) {
                $packageName = $dep.Name
                $version = $dep.Value

                if ($packageFixes.ContainsKey($packageName)) {
                    $fixes = $packageFixes[$packageName]
                    if ($fixes.ContainsKey($version)) {
                        $newVersion = $fixes[$version]
                        $packageContent.devDependencies.$packageName = $newVersion
                        Write-Host "   ✅ Updated dev dependency ${packageName}: ${version} → ${newVersion}" -ForegroundColor Green
                        $hasChanges = $true
                    }
                }
            }
        }

        # Save changes if any were made
        if ($hasChanges) {
            $backupPath = "$packageJson.backup"
            Copy-Item $packageJson $backupPath -Force
            Write-Host "   💾 Backup created: $backupPath" -ForegroundColor Gray

            $newJson = $packageContent | ConvertTo-Json -Depth 10
            Set-Content -Path $packageJson -Value $newJson -Encoding UTF8
            Write-Host "   ✅ package.json updated with fixes!" -ForegroundColor Green
        } else {
            Write-Host "   ℹ️ No conflicts found to resolve" -ForegroundColor Gray
        }

    }
    catch {
        Write-Host "   ❌ Error processing package.json: $($_.Exception.Message)" -ForegroundColor Red
    }

    Write-Host ""
}

# Function to install dependencies after fixes
function Install-RepositoryDependencies {
    param(
        [string]$RepoPath,
        [string]$RepoName
    )

    Write-Host "📦 Installing dependencies for: $RepoName" -ForegroundColor Cyan

    try {
        Push-Location $RepoPath

        # Clear cache and old installations
        if (Test-Path "node_modules") {
            Write-Host "   🧹 Cleaning node_modules..." -ForegroundColor Yellow
            Remove-Item "node_modules" -Recurse -Force -ErrorAction SilentlyContinue
        }

        if (Test-Path "package-lock.json") {
            Write-Host "   🧹 Removing package-lock.json..." -ForegroundColor Yellow
            Remove-Item "package-lock.json" -Force -ErrorAction SilentlyContinue
        }

        # Clear npm cache
        Write-Host "   🧹 Clearing npm cache..." -ForegroundColor Yellow
        npm cache clean --force

        # Install with multiple fallback strategies
        Write-Host "   📥 Installing dependencies (strategy 1: legacy peer deps)..." -ForegroundColor Yellow
        npm install --legacy-peer-deps

        if ($LASTEXITCODE -ne 0) {
            Write-Host "   🔄 Strategy 1 failed, trying strategy 2: force..." -ForegroundColor Yellow
            npm install --force

            if ($LASTEXITCODE -ne 0) {
                Write-Host "   🔄 Strategy 2 failed, trying strategy 3: exact versions..." -ForegroundColor Yellow
                npm install --exact --legacy-peer-deps

                if ($LASTEXITCODE -ne 0) {
                    Write-Host "   ❌ All installation strategies failed" -ForegroundColor Red
                    return $false
                }
            }
        }

        Write-Host "   ✅ Dependencies installed successfully!" -ForegroundColor Green

        # Run security audit
        Write-Host "   🔍 Running security audit..." -ForegroundColor Yellow
        npm audit fix --legacy-peer-deps

        return $true
    }
    catch {
        Write-Host "   ❌ Installation error: $($_.Exception.Message)" -ForegroundColor Red
        return $false
    }
    finally {
        Pop-Location
    }
}

# Main execution
function Main {
    Write-Host "🎯 Starting Empire Dependency Conflict Resolution..." -ForegroundColor Cyan
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

    # Define repositories that need fixing
    $problematicRepos = @(
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
        }
    )

    $fixedRepos = 0
    $successfulInstalls = 0

    Write-Host "🔧 Phase 1: Resolving package.json conflicts..." -ForegroundColor Cyan
    Write-Host ""

    foreach ($repo in $problematicRepos) {
        Resolve-PackageConflicts -RepoPath $repo.Path -RepoName $repo.Name
        $fixedRepos++
    }

    Write-Host "📦 Phase 2: Installing dependencies with fixes..." -ForegroundColor Cyan
    Write-Host ""

    foreach ($repo in $problematicRepos) {
        $success = Install-RepositoryDependencies -RepoPath $repo.Path -RepoName $repo.Name
        if ($success) {
            $successfulInstalls++
        }
    }

    Write-Host "🌌 " + "=" * 60 -ForegroundColor Cyan
    Write-Host "🌌 🔧💎⚡ CONFLICT RESOLUTION COMPLETE! ⚡💎🔧" -ForegroundColor Green
    Write-Host "🌌 " + "=" * 60 -ForegroundColor Cyan
    Write-Host ""
    Write-Host "📊 Resolution Summary:" -ForegroundColor Yellow
    Write-Host "   • Repositories analyzed: $fixedRepos" -ForegroundColor Gray
    Write-Host "   • Successful installations: $successfulInstalls" -ForegroundColor Gray
    Write-Host "   • Backup files created for safety" -ForegroundColor Gray
    Write-Host ""

    if ($successfulInstalls -eq $problematicRepos.Count) {
        Write-Host "🎉 ALL CONFLICTS RESOLVED! Empire is ready for development!" -ForegroundColor Green
    } elseif ($successfulInstalls -gt 0) {
        Write-Host "⚡ PARTIAL SUCCESS! $successfulInstalls repositories fixed." -ForegroundColor Yellow
        Write-Host "🔧 Manual review needed for remaining issues." -ForegroundColor Yellow
    } else {
        Write-Host "🔧 Manual intervention required for complex conflicts." -ForegroundColor Red
        Write-Host "📋 Check package.json.backup files for original versions." -ForegroundColor Gray
    }
}

# Execute main function
Main

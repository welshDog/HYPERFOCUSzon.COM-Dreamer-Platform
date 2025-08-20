#!/usr/bin/env powershell
<#
🚀💎⚡ NODEJS INSTALLATION AND SETUP ENGINE ⚡💎🚀

Automatic Node.js installation and configuration for HyperFocus Zone Empire
Ensures all repository development environments are properly configured

Created: August 20, 2025
Status: LEGENDARY DEVELOPMENT ENVIRONMENT SETUP
#>

Write-Host "🌌 🚀💎⚡ NODEJS INSTALLATION ENGINE ⚡💎🚀" -ForegroundColor Cyan
Write-Host "🌌 " + "=" * 60 -ForegroundColor Cyan

# Function to check if Node.js is already installed
function Test-NodeJSInstallation {
    Write-Host "🔍 Checking for existing Node.js installation..." -ForegroundColor Yellow

    try {
        $nodeVersion = node --version 2>$null
        if ($nodeVersion) {
            Write-Host "✅ Node.js already installed: $nodeVersion" -ForegroundColor Green

            $npmVersion = npm --version 2>$null
            if ($npmVersion) {
                Write-Host "✅ npm already installed: v$npmVersion" -ForegroundColor Green
                return $true
            }
        }
    }
    catch {
        Write-Host "❌ Node.js not found in PATH" -ForegroundColor Red
    }

    # Check common installation directories
    $commonPaths = @(
        "C:\Program Files\nodejs\node.exe",
        "C:\Program Files (x86)\nodejs\node.exe",
        "$env:LOCALAPPDATA\Programs\nodejs\node.exe",
        "$env:APPDATA\npm\node.exe"
    )

    foreach ($path in $commonPaths) {
        if (Test-Path $path) {
            Write-Host "✅ Found Node.js at: $path" -ForegroundColor Green
            Write-Host "⚠️ Node.js found but not in PATH - will fix PATH" -ForegroundColor Yellow
            return "PATH_ISSUE"
        }
    }

    return $false
}

# Function to download and install Node.js
function Install-NodeJS {
    Write-Host "🚀 Installing Node.js LTS..." -ForegroundColor Cyan

    # Try winget first (Windows 10+)
    try {
        Write-Host "📦 Attempting installation via winget..." -ForegroundColor Yellow
        $wingetResult = winget install OpenJS.NodeJS --accept-source-agreements --accept-package-agreements 2>&1

        if ($LASTEXITCODE -eq 0) {
            Write-Host "✅ Node.js installed successfully via winget!" -ForegroundColor Green
            return $true
        }
    }
    catch {
        Write-Host "⚠️ winget not available or failed" -ForegroundColor Yellow
    }

    # Try Chocolatey
    try {
        Write-Host "📦 Attempting installation via Chocolatey..." -ForegroundColor Yellow
        $chocoResult = choco install nodejs --yes 2>&1

        if ($LASTEXITCODE -eq 0) {
            Write-Host "✅ Node.js installed successfully via Chocolatey!" -ForegroundColor Green
            return $true
        }
    }
    catch {
        Write-Host "⚠️ Chocolatey not available or failed" -ForegroundColor Yellow
    }

    # Manual download and install
    try {
        Write-Host "📥 Downloading Node.js manually..." -ForegroundColor Yellow

        # Get the latest LTS version info (v22.18.0 LTS as of August 2025)
        try {
            $releaseInfo = Invoke-RestMethod -Uri "https://nodejs.org/dist/index.json" | Where-Object { $_.lts } | Select-Object -First 1
            $version = $releaseInfo.version
        }
        catch {
            # Fallback to known stable LTS version
            $version = "v22.18.0"
            Write-Host "⚠️ Using fallback LTS version: $version" -ForegroundColor Yellow
        }

        $downloadUrl = "https://nodejs.org/dist/$version/node-$version-x64.msi"

        Write-Host "📥 Downloading Node.js $version (LTS)..." -ForegroundColor Yellow

        $tempPath = "$env:TEMP\nodejs-installer.msi"
        Invoke-WebRequest -Uri $downloadUrl -OutFile $tempPath -UseBasicParsing

        Write-Host "🔧 Installing Node.js..." -ForegroundColor Yellow
        Start-Process -FilePath "msiexec.exe" -ArgumentList "/i", $tempPath, "/quiet", "/norestart" -Wait

        # Clean up
        Remove-Item $tempPath -Force -ErrorAction SilentlyContinue

        Write-Host "✅ Node.js installation completed!" -ForegroundColor Green
        return $true
    }
    catch {
        Write-Host "❌ Manual installation failed: $($_.Exception.Message)" -ForegroundColor Red
        return $false
    }
}

# Function to fix PATH issues
function Fix-NodeJSPath {
    Write-Host "🔧 Fixing Node.js PATH configuration..." -ForegroundColor Yellow

    $nodePaths = @(
        "C:\Program Files\nodejs",
        "C:\Program Files (x86)\nodejs",
        "$env:LOCALAPPDATA\Programs\nodejs",
        "$env:APPDATA\npm"
    )

    $currentPath = $env:PATH
    $pathUpdated = $false

    foreach ($nodePath in $nodePaths) {
        if ((Test-Path $nodePath) -and ($currentPath -notlike "*$nodePath*")) {
            Write-Host "➕ Adding to PATH: $nodePath" -ForegroundColor Green
            $env:PATH = "$nodePath;$env:PATH"
            $pathUpdated = $true
        }
    }

    if ($pathUpdated) {
        # Update system PATH permanently
        try {
            $userPath = [Environment]::GetEnvironmentVariable("PATH", "User")
            foreach ($nodePath in $nodePaths) {
                if ((Test-Path $nodePath) -and ($userPath -notlike "*$nodePath*")) {
                    $userPath = "$nodePath;$userPath"
                }
            }
            [Environment]::SetEnvironmentVariable("PATH", $userPath, "User")
            Write-Host "✅ PATH updated permanently" -ForegroundColor Green
        }
        catch {
            Write-Host "⚠️ Could not update permanent PATH - restart may be required" -ForegroundColor Yellow
        }
    }
}

# Function to verify installation
function Test-NodeJSFunctionality {
    Write-Host "🧪 Testing Node.js functionality..." -ForegroundColor Yellow

    try {
        $nodeVersion = node --version 2>&1
        $npmVersion = npm --version 2>&1

        if ($nodeVersion -and $npmVersion) {
            Write-Host "✅ Node.js $nodeVersion is working!" -ForegroundColor Green
            Write-Host "✅ npm v$npmVersion is working!" -ForegroundColor Green

            # Test npm functionality
            Write-Host "🧪 Testing npm functionality..." -ForegroundColor Yellow
            $npmTest = npm --help 2>&1
            if ($npmTest) {
                Write-Host "✅ npm commands are functional!" -ForegroundColor Green
                return $true
            }
        }
    }
    catch {
        Write-Host "❌ Node.js/npm not functioning properly" -ForegroundColor Red
        return $false
    }

    return $false
}

# Function to setup empire repositories
function Setup-EmpireRepositories {
    Write-Host "🏗️ Setting up Empire repository dependencies..." -ForegroundColor Cyan

    $repositories = @(
        "h:\HYPERFOCUS-UNIFIED-EMPIRE\🧠 NEURODIVERGENT-TOOLS\neuro-social-platform\frontend\web",
        "h:\HYPERFOCUS-UNIFIED-EMPIRE\🧠 NEURODIVERGENT-TOOLS\neuro-social-platform\frontend\mobile",
        "h:\HYPERFOCUS-UNIFIED-EMPIRE\🧠 NEURODIVERGENT-TOOLS\neuro-social-platform\backend",
        "h:\HYPERFOCUS-UNIFIED-EMPIRE\🎮 APPLICATIONS\hyperfocus-hub-ts",
        "h:\HYPERFOCUS-ZONE-NEURO-SOCIAL-DREAMER"
    )

    foreach ($repo in $repositories) {
        $packageJson = Join-Path $repo "package.json"

        if (Test-Path $packageJson) {
            Write-Host "📦 Installing dependencies for: $repo" -ForegroundColor Yellow

            try {
                Push-Location $repo

                Write-Host "   📥 Running npm install..." -ForegroundColor Gray
                npm install

                if ($LASTEXITCODE -eq 0) {
                    Write-Host "   ✅ Dependencies installed successfully!" -ForegroundColor Green

                    Write-Host "   🔍 Running security audit..." -ForegroundColor Gray
                    npm audit --fix

                    if ($LASTEXITCODE -eq 0) {
                        Write-Host "   ✅ Security audit completed!" -ForegroundColor Green
                    } else {
                        Write-Host "   ⚠️ Security audit found issues - check manually" -ForegroundColor Yellow
                    }
                } else {
                    Write-Host "   ❌ Failed to install dependencies" -ForegroundColor Red
                }
            }
            catch {
                Write-Host "   ❌ Error processing repository: $($_.Exception.Message)" -ForegroundColor Red
            }
            finally {
                Pop-Location
            }
        }
    }
}

# Function to check if Docker is available
function Test-DockerInstallation {
    Write-Host "🐳 Checking for Docker installation..." -ForegroundColor Yellow

    try {
        $dockerVersion = docker --version 2>$null
        if ($dockerVersion) {
            Write-Host "✅ Docker found: $dockerVersion" -ForegroundColor Green

            # Test if Docker daemon is running
            $dockerInfo = docker info 2>$null
            if ($dockerInfo) {
                Write-Host "✅ Docker daemon is running" -ForegroundColor Green
                return $true
            } else {
                Write-Host "⚠️ Docker found but daemon not running" -ForegroundColor Yellow
                return "DAEMON_ISSUE"
            }
        }
    }
    catch {
        Write-Host "❌ Docker not found" -ForegroundColor Red
    }

    return $false
}

# Function to setup Node.js via Docker
function Setup-NodeJSViaDocker {
    Write-Host "🐳 Setting up Node.js development environment via Docker..." -ForegroundColor Cyan

    try {
        # Pull the Node.js Docker image
        Write-Host "📥 Pulling Node.js 22-alpine Docker image..." -ForegroundColor Yellow
        docker pull node:22-alpine

        if ($LASTEXITCODE -eq 0) {
            Write-Host "✅ Node.js Docker image pulled successfully!" -ForegroundColor Green

            # Test the Docker container
            Write-Host "🧪 Testing Node.js in Docker container..." -ForegroundColor Yellow
            $nodeVersion = docker run --rm node:22-alpine node -v
            $npmVersion = docker run --rm node:22-alpine npm -v

            if ($nodeVersion -and $npmVersion) {
                Write-Host "✅ Docker Node.js $nodeVersion is working!" -ForegroundColor Green
                Write-Host "✅ Docker npm v$npmVersion is working!" -ForegroundColor Green
                return $true
            }
        } else {
            Write-Host "❌ Failed to pull Node.js Docker image" -ForegroundColor Red
            return $false
        }
    }
    catch {
        Write-Host "❌ Docker setup failed: $($_.Exception.Message)" -ForegroundColor Red
        return $false
    }

    return $false
}

# Function to run npm commands in Docker for empire repositories
function Setup-EmpireRepositoriesViaDocker {
    Write-Host "🐳 Setting up Empire repository dependencies via Docker..." -ForegroundColor Cyan

    $repositories = @(
        "h:\HYPERFOCUS-UNIFIED-EMPIRE\🧠 NEURODIVERGENT-TOOLS\neuro-social-platform\frontend\web",
        "h:\HYPERFOCUS-UNIFIED-EMPIRE\🧠 NEURODIVERGENT-TOOLS\neuro-social-platform\frontend\mobile",
        "h:\HYPERFOCUS-UNIFIED-EMPIRE\🧠 NEURODIVERGENT-TOOLS\neuro-social-platform\backend",
        "h:\HYPERFOCUS-UNIFIED-EMPIRE\🎮 APPLICATIONS\hyperfocus-hub-ts",
        "h:\HYPERFOCUS-ZONE-NEURO-SOCIAL-DREAMER"
    )

    foreach ($repo in $repositories) {
        $packageJson = Join-Path $repo "package.json"

        if (Test-Path $packageJson) {
            Write-Host "🐳 Processing repository via Docker: $repo" -ForegroundColor Yellow

            try {
                # Convert Windows path to Docker-compatible path
                $dockerPath = $repo -replace '^h:', '/host/h' -replace '\\', '/'
                $hostPath = $repo

                Write-Host "   📥 Running npm install in Docker container..." -ForegroundColor Gray
                docker run --rm -v "${hostPath}:/app" -w /app node:22-alpine npm install

                if ($LASTEXITCODE -eq 0) {
                    Write-Host "   ✅ Dependencies installed successfully via Docker!" -ForegroundColor Green

                    Write-Host "   🔍 Running security audit via Docker..." -ForegroundColor Gray
                    docker run --rm -v "${hostPath}:/app" -w /app node:22-alpine npm audit --fix

                    if ($LASTEXITCODE -eq 0) {
                        Write-Host "   ✅ Security audit completed via Docker!" -ForegroundColor Green
                    } else {
                        Write-Host "   ⚠️ Security audit found issues - check manually" -ForegroundColor Yellow
                    }
                } else {
                    Write-Host "   ❌ Failed to install dependencies via Docker" -ForegroundColor Red
                }
            }
            catch {
                Write-Host "   ❌ Error processing repository via Docker: $($_.Exception.Message)" -ForegroundColor Red
            }
        }
    }
}

# Main execution function
function Main {
    try {
        Write-Host "🎯 Starting Node.js Installation and Setup..." -ForegroundColor Cyan
        Write-Host ""

        # Check existing installation
        $nodeStatus = Test-NodeJSInstallation

        if ($nodeStatus -eq $true) {
            Write-Host "✅ Node.js is already properly installed and configured!" -ForegroundColor Green
        }
        elseif ($nodeStatus -eq "PATH_ISSUE") {
            Fix-NodeJSPath
            $nodeStatus = Test-NodeJSFunctionality
        }
        else {
            # Check if Docker is available as alternative
            $dockerStatus = Test-DockerInstallation

            if ($dockerStatus -eq $true) {
                Write-Host "🐳 Docker detected - offering containerized Node.js option..." -ForegroundColor Cyan
                Write-Host "💡 Would you like to use Docker for Node.js instead of system installation?" -ForegroundColor Yellow
                Write-Host "   🎯 Benefits: No system changes, isolated environment, easy cleanup" -ForegroundColor Gray
                Write-Host "   ⚡ Docker option: Pull node:22-alpine and run npm commands in containers" -ForegroundColor Gray
                Write-Host ""

                # Setup Docker-based Node.js environment
                $dockerSetup = Setup-NodeJSViaDocker

                if ($dockerSetup) {
                    Write-Host "✅ Docker-based Node.js environment ready!" -ForegroundColor Green

                    Write-Host ""
                    Write-Host "🏗️ Setting up Empire repositories via Docker..." -ForegroundColor Cyan
                    Setup-EmpireRepositoriesViaDocker

                    $nodeStatus = "DOCKER_SUCCESS"
                } else {
                    Write-Host "❌ Docker setup failed, falling back to system installation..." -ForegroundColor Red
                    # Fall back to regular installation
                    $installSuccess = Install-NodeJS

                    if ($installSuccess) {
                        Fix-NodeJSPath
                        Start-Sleep -Seconds 3
                        $nodeStatus = Test-NodeJSFunctionality
                    }
                }
            } else {
                # Install Node.js normally
                $installSuccess = Install-NodeJS

                if ($installSuccess) {
                    # Fix PATH if needed
                    Fix-NodeJSPath

                    # Verify installation
                    Start-Sleep -Seconds 3  # Give system time to update
                    $nodeStatus = Test-NodeJSFunctionality
                }
            }
        }

        if ($nodeStatus -eq $true -or $nodeStatus -eq "DOCKER_SUCCESS") {
            if ($nodeStatus -eq "DOCKER_SUCCESS") {
                Write-Host ""
                Write-Host "� " + "=" * 60 -ForegroundColor Cyan
                Write-Host "🌌 🐳💎⚡ DOCKER NODE.JS SETUP COMPLETE! ⚡💎🐳" -ForegroundColor Green
                Write-Host "🌌 " + "=" * 60 -ForegroundColor Cyan
                Write-Host ""
                Write-Host "🎉 Your containerized development environment is ready!" -ForegroundColor Green
                Write-Host "🐳 All repository dependencies installed via Docker" -ForegroundColor Green
                Write-Host "⚡ Use Docker commands for Node.js development" -ForegroundColor Green
                Write-Host ""
                Write-Host "📋 Docker Development Commands:" -ForegroundColor Yellow
                Write-Host "   • Interactive shell: docker run -it --rm -v `"h:\your\project:/app`" -w /app node:22-alpine sh" -ForegroundColor Gray
                Write-Host "   • Run npm: docker run --rm -v `"h:\your\project:/app`" -w /app node:22-alpine npm run dev" -ForegroundColor Gray
                Write-Host "   • Build: docker run --rm -v `"h:\your\project:/app`" -w /app node:22-alpine npm run build" -ForegroundColor Gray
            } else {
                Write-Host ""
                Write-Host "�🏗️ Setting up Empire repositories..." -ForegroundColor Cyan
                Setup-EmpireRepositories

                Write-Host ""
                Write-Host "🌌 " + "=" * 60 -ForegroundColor Cyan
                Write-Host "🌌 🏆💎⚡ NODE.JS SETUP COMPLETE! ⚡💎🏆" -ForegroundColor Green
                Write-Host "🌌 " + "=" * 60 -ForegroundColor Cyan
                Write-Host ""
                Write-Host "🎉 Your development environment is now ready!" -ForegroundColor Green
                Write-Host "🚀 All repository dependencies should be installed" -ForegroundColor Green
                Write-Host "⚡ You can now run development servers and build commands" -ForegroundColor Green
                Write-Host ""
                Write-Host "📋 Next Steps:" -ForegroundColor Yellow
                Write-Host "   • Test: cd to any Node.js project and run 'npm run dev'" -ForegroundColor Gray
                Write-Host "   • Verify: Run 'node --version' and 'npm --version'" -ForegroundColor Gray
                Write-Host "   • Build: Use 'npm run build' for production builds" -ForegroundColor Gray
            }
        }
        else {
            Write-Host ""
            Write-Host "❌ Node.js installation failed!" -ForegroundColor Red
            Write-Host "🔧 Available options:" -ForegroundColor Yellow
            Write-Host "   1. Manual installation: Visit https://nodejs.org/" -ForegroundColor Gray
            Write-Host "   2. Docker installation: Install Docker Desktop and retry" -ForegroundColor Gray
            Write-Host "   3. Package manager: Use winget or chocolatey" -ForegroundColor Gray
            Write-Host "   4. Restart terminal/VS Code and retry" -ForegroundColor Gray
        }
    }
    catch {
        Write-Host "❌ Fatal error during installation: $($_.Exception.Message)" -ForegroundColor Red
        Write-Host "🔧 Please try manual installation from https://nodejs.org/" -ForegroundColor Yellow
    }
}

# Execute main function
Main

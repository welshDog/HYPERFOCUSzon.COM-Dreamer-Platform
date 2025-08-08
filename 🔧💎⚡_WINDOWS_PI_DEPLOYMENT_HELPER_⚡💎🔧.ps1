# 🔧💎⚡ WINDOWS PI DEPLOYMENT HELPER SCRIPT ⚡💎🔧
# This script helps deploy your Pi micro-cloud from Windows

param(
    [Parameter(Mandatory=$false)]
    [string]$PiIP = "",
    
    [Parameter(Mandatory=$false)]
    [string]$PiUser = "pi"
)

Write-Host "🚀💎⚡ WINDOWS TO PI DEPLOYMENT HELPER ⚡💎🚀" -ForegroundColor Cyan
Write-Host "=" * 60 -ForegroundColor Yellow

# Check if pi-microcloud directory exists
if (-not (Test-Path "pi-microcloud")) {
    Write-Host "❌ pi-microcloud directory not found!" -ForegroundColor Red
    Write-Host "📋 Please run the Pi deployer script first to generate the deployment files." -ForegroundColor Yellow
    Write-Host "💡 Run: python 🚀💎⚡_RASPBERRY_PI_MICRO_CLOUD_STACK_DEPLOYER_⚡💎🚀.py" -ForegroundColor Green
    exit 1
}

Write-Host "✅ Pi micro-cloud deployment files found!" -ForegroundColor Green

# Get Pi IP if not provided
if ($PiIP -eq "") {
    $PiIP = Read-Host "🌐 Enter your Raspberry Pi IP address"
}

Write-Host "🎯 Target Pi: $PiUser@$PiIP" -ForegroundColor Cyan

# Check if we can reach the Pi
Write-Host "🔍 Testing Pi connectivity..." -ForegroundColor Yellow
$pingResult = Test-Connection -ComputerName $PiIP -Count 2 -Quiet

if (-not $pingResult) {
    Write-Host "❌ Cannot reach Pi at $PiIP" -ForegroundColor Red
    Write-Host "📋 Please check:" -ForegroundColor Yellow
    Write-Host "   • Pi is powered on and connected to network" -ForegroundColor White
    Write-Host "   • IP address is correct" -ForegroundColor White
    Write-Host "   • SSH is enabled on Pi" -ForegroundColor White
    exit 1
}

Write-Host "✅ Pi is reachable!" -ForegroundColor Green

# Check for required tools
$requiredTools = @("scp", "ssh")
$missingTools = @()

foreach ($tool in $requiredTools) {
    if (-not (Get-Command $tool -ErrorAction SilentlyContinue)) {
        $missingTools += $tool
    }
}

if ($missingTools.Count -gt 0) {
    Write-Host "❌ Missing required tools: $($missingTools -join ', ')" -ForegroundColor Red
    Write-Host "📋 Please install OpenSSH or Git for Windows which includes these tools." -ForegroundColor Yellow
    Write-Host "💡 Or use WinSCP/PuTTY for file transfer and SSH connection." -ForegroundColor Green
    
    Write-Host "`n🛠️  MANUAL DEPLOYMENT STEPS:" -ForegroundColor Cyan
    Write-Host "1. Copy the entire 'pi-microcloud' folder to your Pi at /home/pi/empire/" -ForegroundColor White
    Write-Host "2. SSH into your Pi" -ForegroundColor White
    Write-Host "3. Run: cd /home/pi/empire/pi-microcloud" -ForegroundColor White
    Write-Host "4. Run: chmod +x setup-pi-microcloud.sh" -ForegroundColor White
    Write-Host "5. Run: ./setup-pi-microcloud.sh" -ForegroundColor White
    
    Read-Host "`nPress Enter to continue with automated deployment (if tools are available) or Ctrl+C to exit"
}

# Deployment process
Write-Host "`n🚀 Starting Pi Micro-Cloud Deployment Process..." -ForegroundColor Cyan
Write-Host "=" * 60 -ForegroundColor Yellow

try {
    # Step 1: Create empire directory on Pi
    Write-Host "📁 Creating empire directory on Pi..." -ForegroundColor Yellow
    $sshCommand = "ssh $PiUser@$PiIP 'mkdir -p /home/pi/empire'"
    Invoke-Expression $sshCommand
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Empire directory created!" -ForegroundColor Green
    } else {
        Write-Host "⚠️  Directory creation may have failed (might already exist)" -ForegroundColor Yellow
    }
    
    # Step 2: Copy deployment files
    Write-Host "📤 Copying pi-microcloud files to Pi..." -ForegroundColor Yellow
    $scpCommand = "scp -r pi-microcloud $PiUser@${PiIP}:/home/pi/empire/"
    Invoke-Expression $scpCommand
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Files copied successfully!" -ForegroundColor Green
    } else {
        throw "File copy failed"
    }
    
    # Step 3: Make setup script executable and run it
    Write-Host "🔧 Making setup script executable..." -ForegroundColor Yellow
    $chmodCommand = "ssh $PiUser@$PiIP 'chmod +x /home/pi/empire/pi-microcloud/setup-pi-microcloud.sh'"
    Invoke-Expression $chmodCommand
    
    Write-Host "🚀 Running Pi setup script..." -ForegroundColor Yellow
    Write-Host "⏳ This may take several minutes (Docker installation, etc.)..." -ForegroundColor Yellow
    
    $setupCommand = "ssh $PiUser@$PiIP 'cd /home/pi/empire/pi-microcloud && ./setup-pi-microcloud.sh'"
    Invoke-Expression $setupCommand
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Pi setup completed successfully!" -ForegroundColor Green
    } else {
        Write-Host "⚠️  Setup script finished with warnings (check Pi output)" -ForegroundColor Yellow
    }
    
    # Step 4: Test the deployment
    Write-Host "`n🧪 Testing Pi micro-cloud deployment..." -ForegroundColor Cyan
    Start-Sleep -Seconds 10  # Give services time to start
    
    $healthUrl = "http://${PiIP}/health"
    $statusUrl = "http://${PiIP}/pi/status"
    
    Write-Host "🔍 Testing health endpoint: $healthUrl" -ForegroundColor Yellow
    try {
        $healthResponse = Invoke-RestMethod -Uri $healthUrl -TimeoutSec 10
        Write-Host "✅ Health check: $healthResponse" -ForegroundColor Green
    } catch {
        Write-Host "⚠️  Health check failed: $($_.Exception.Message)" -ForegroundColor Yellow
    }
    
    Write-Host "🔍 Testing status endpoint: $statusUrl" -ForegroundColor Yellow
    try {
        $statusResponse = Invoke-RestMethod -Uri $statusUrl -TimeoutSec 10
        Write-Host "✅ Status check successful!" -ForegroundColor Green
        Write-Host "📊 Pi Node ID: $($statusResponse.pi_node_id)" -ForegroundColor Cyan
        Write-Host "💾 Memory Usage: $($statusResponse.system.memory_percent)%" -ForegroundColor Cyan
        Write-Host "🔥 Temperature: $($statusResponse.system.temperature_c)°C" -ForegroundColor Cyan
    } catch {
        Write-Host "⚠️  Status check failed: $($_.Exception.Message)" -ForegroundColor Yellow
    }
    
    # Success summary
    Write-Host "`n🎊 PI MICRO-CLOUD DEPLOYMENT COMPLETE! 🎊" -ForegroundColor Green
    Write-Host "=" * 60 -ForegroundColor Yellow
    
    Write-Host "🌐 Your Pi Micro-Cloud URLs:" -ForegroundColor Cyan
    Write-Host "   • Health: http://$PiIP/health" -ForegroundColor White
    Write-Host "   • Status: http://$PiIP/pi/status" -ForegroundColor White
    Write-Host "   • Offloading: http://$PiIP/api/offload" -ForegroundColor White
    Write-Host "   • Metrics: http://$PiIP/metrics" -ForegroundColor White
    
    Write-Host "`n🔄 Auto-Boot Features:" -ForegroundColor Cyan
    Write-Host "   • Pi will automatically start micro-cloud on reboot" -ForegroundColor White
    Write-Host "   • Systemd service: pi-microcloud.service" -ForegroundColor White
    Write-Host "   • Health monitoring and auto-restart enabled" -ForegroundColor White
    
    Write-Host "`n💻 Laptop Integration:" -ForegroundColor Cyan
    Write-Host "   • Use pi-microcloud-laptop-client.py for task offloading" -ForegroundColor White
    Write-Host "   • Update PI_IP in client to: $PiIP" -ForegroundColor White
    
    Write-Host "`n🛠️  Pi Service Management (SSH to Pi):" -ForegroundColor Cyan
    Write-Host "   • Check status: sudo systemctl status pi-microcloud" -ForegroundColor White
    Write-Host "   • Restart: sudo systemctl restart pi-microcloud" -ForegroundColor White
    Write-Host "   • View logs: sudo journalctl -u pi-microcloud -f" -ForegroundColor White
    
} catch {
    Write-Host "`n❌ Deployment failed: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host "`n📋 Manual deployment steps:" -ForegroundColor Yellow
    Write-Host "1. Copy 'pi-microcloud' folder to Pi: /home/pi/empire/" -ForegroundColor White
    Write-Host "2. SSH to Pi: ssh $PiUser@$PiIP" -ForegroundColor White
    Write-Host "3. Run: cd /home/pi/empire/pi-microcloud" -ForegroundColor White
    Write-Host "4. Run: chmod +x setup-pi-microcloud.sh" -ForegroundColor White
    Write-Host "5. Run: ./setup-pi-microcloud.sh" -ForegroundColor White
    exit 1
}

Write-Host "`n🏆 Your Pi is now ready for laptop task offloading! 🚀💎⚡" -ForegroundColor Green

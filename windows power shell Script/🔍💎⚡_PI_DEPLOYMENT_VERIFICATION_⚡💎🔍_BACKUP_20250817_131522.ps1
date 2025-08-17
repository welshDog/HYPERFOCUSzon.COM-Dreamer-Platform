# 🔍💎⚡ PI DEPLOYMENT VERIFICATION SCRIPT ⚡💎🔍

Write-Host "🔍💎⚡ PI MICRO-CLOUD DEPLOYMENT VERIFICATION ⚡💎🔍" -ForegroundColor Cyan
Write-Host "=" * 60 -ForegroundColor Yellow

# Check current directory
$currentDir = Get-Location
Write-Host "📍 Current Directory: $currentDir" -ForegroundColor Cyan

# Check for deployment files
$requiredFiles = @(
    "pi-microcloud",
    "pi-microcloud/docker-compose.pi-microcloud.yml",
    "pi-microcloud/setup-pi-microcloud.sh",
    "pi-microcloud/configure-auto-boot.sh",
    "pi-microcloud/nginx/pi-nginx.conf",
    "pi-microcloud/agent/pi_broski_agent.py",
    "pi-microcloud/sync/empire-sync.sh",
    "pi-microcloud/.env",
    "pi-microcloud-laptop-client.py"
)

$missingFiles = @()
$foundFiles = @()

Write-Host "`n📋 Checking deployment files..." -ForegroundColor Yellow

foreach ($file in $requiredFiles) {
    if (Test-Path $file) {
        $foundFiles += $file
        Write-Host "✅ $file" -ForegroundColor Green
    } else {
        $missingFiles += $file
        Write-Host "❌ $file" -ForegroundColor Red
    }
}

Write-Host "`n📊 VERIFICATION SUMMARY:" -ForegroundColor Cyan
Write-Host "   • Found Files: $($foundFiles.Count)" -ForegroundColor Green
Write-Host "   • Missing Files: $($missingFiles.Count)" -ForegroundColor $(if ($missingFiles.Count -eq 0) { "Green" } else { "Red" })

if ($missingFiles.Count -eq 0) {
    Write-Host "`n🎊 ALL DEPLOYMENT FILES READY! 🎊" -ForegroundColor Green
    Write-Host "🚀 You can now proceed with Pi deployment!" -ForegroundColor Cyan
    
    Write-Host "`n🎯 DEPLOYMENT OPTIONS:" -ForegroundColor Cyan
    Write-Host "Option 1 - Automated (if you have SSH tools):" -ForegroundColor Yellow
    Write-Host "   PowerShell: .\🔧💎⚡_WINDOWS_PI_DEPLOYMENT_HELPER_⚡💎🔧.ps1" -ForegroundColor White
    
    Write-Host "`nOption 2 - Manual Steps:" -ForegroundColor Yellow
    Write-Host "   1. Copy 'pi-microcloud' folder to your Pi" -ForegroundColor White
    Write-Host "   2. SSH into Pi: ssh pi@[PI_IP]" -ForegroundColor White
    Write-Host "   3. Navigate: cd /home/pi/empire/pi-microcloud" -ForegroundColor White
    Write-Host "   4. Make executable: chmod +x setup-pi-microcloud.sh" -ForegroundColor White
    Write-Host "   5. Run setup: ./setup-pi-microcloud.sh" -ForegroundColor White
    
    Write-Host "`n💡 The setup script (.sh) must be run ON the Pi, not on Windows!" -ForegroundColor Yellow
    
    # Show file sizes for verification
    Write-Host "`n📏 File Sizes:" -ForegroundColor Cyan
    foreach ($file in $foundFiles) {
        if (Test-Path $file -PathType Leaf) {
            $size = (Get-Item $file).Length
            $sizeKB = [math]::Round($size / 1024, 2)
            Write-Host "   • $file : ${sizeKB} KB" -ForegroundColor White
        }
    }
    
} else {
    Write-Host "`n❌ MISSING DEPLOYMENT FILES!" -ForegroundColor Red
    Write-Host "📋 Missing files:" -ForegroundColor Yellow
    foreach ($file in $missingFiles) {
        Write-Host "   • $file" -ForegroundColor Red
    }
    
    Write-Host "`n🔧 TO GENERATE MISSING FILES:" -ForegroundColor Cyan
    Write-Host "Run the Pi deployer first:" -ForegroundColor Yellow
    Write-Host "   python 🚀💎⚡_RASPBERRY_PI_MICRO_CLOUD_STACK_DEPLOYER_⚡💎🚀.py" -ForegroundColor White
}

# Check for laptop client
if (Test-Path "pi-microcloud-laptop-client.py") {
    Write-Host "`n💻 LAPTOP CLIENT READY!" -ForegroundColor Green
    Write-Host "📋 After Pi deployment, you can test offloading with:" -ForegroundColor Cyan
    Write-Host "   python pi-microcloud-laptop-client.py" -ForegroundColor White
}

Write-Host "`n🏁 Verification complete!" -ForegroundColor Cyan

# 🚀💎⚡ PI SD CARD DIRECT DEPLOYMENT SCRIPT ⚡💎🚀
# This script deploys your Pi micro-cloud directly to the SD card

param(
    [Parameter(Mandatory=$false)]
    [string]$SDCardDrive = "E:",
    
    [Parameter(Mandatory=$false)]
    [switch]$Force = $false
)

Write-Host "🚀💎⚡ PI SD CARD DIRECT DEPLOYMENT ⚡💎🚀" -ForegroundColor Cyan
Write-Host "=" * 60 -ForegroundColor Yellow

# Check if SD card drive exists
if (-not (Test-Path $SDCardDrive)) {
    Write-Host "❌ SD Card drive $SDCardDrive not found!" -ForegroundColor Red
    Write-Host "📋 Please ensure:" -ForegroundColor Yellow
    Write-Host "   • SD card is inserted and recognized" -ForegroundColor White
    Write-Host "   • Drive letter is correct (default: E:)" -ForegroundColor White
    $SDCardDrive = Read-Host "Enter correct SD card drive letter (e.g., F:, G:)"
    
    if (-not (Test-Path $SDCardDrive)) {
        Write-Host "❌ Still can't find drive $SDCardDrive. Exiting." -ForegroundColor Red
        exit 1
    }
}

Write-Host "✅ SD Card found at $SDCardDrive" -ForegroundColor Green

# Check if this looks like a Pi SD card
$isBootPartition = Test-Path "$SDCardDrive\bootcode.bin" -or Test-Path "$SDCardDrive\config.txt" -or Test-Path "$SDCardDrive\cmdline.txt"

if ($isBootPartition) {
    Write-Host "🥧 Detected Raspberry Pi boot partition!" -ForegroundColor Green
} else {
    Write-Host "⚠️  This doesn't appear to be a Pi boot partition" -ForegroundColor Yellow
    if (-not $Force) {
        $continue = Read-Host "Continue anyway? (y/N)"
        if ($continue -ne "y" -and $continue -ne "Y") {
            Write-Host "❌ Deployment cancelled by user" -ForegroundColor Red
            exit 1
        }
    }
}

# Check if pi-microcloud exists in current workspace
$sourceDir = "H:\pi-microcloud"
if (-not (Test-Path $sourceDir)) {
    Write-Host "❌ Pi micro-cloud files not found at $sourceDir" -ForegroundColor Red
    Write-Host "📋 Please run the Pi deployer first:" -ForegroundColor Yellow
    Write-Host "   python H:\🚀💎⚡_RASPBERRY_PI_MICRO_CLOUD_STACK_DEPLOYER_⚡💎🚀.py" -ForegroundColor White
    exit 1
}

# Create deployment directory on SD card
$targetDir = "$SDCardDrive\pi-microcloud"
Write-Host "📁 Creating deployment directory: $targetDir" -ForegroundColor Yellow

try {
    if (Test-Path $targetDir) {
        Write-Host "⚠️  Directory $targetDir already exists" -ForegroundColor Yellow
        if (-not $Force) {
            $overwrite = Read-Host "Overwrite existing deployment? (y/N)"
            if ($overwrite -ne "y" -and $overwrite -ne "Y") {
                Write-Host "❌ Deployment cancelled" -ForegroundColor Red
                exit 1
            }
        }
        Remove-Item $targetDir -Recurse -Force
    }
    
    # Copy pi-microcloud to SD card
    Write-Host "📤 Copying pi-microcloud to SD card..." -ForegroundColor Yellow
    Copy-Item $sourceDir $targetDir -Recurse -Force
    
    Write-Host "✅ Pi micro-cloud copied to SD card!" -ForegroundColor Green
    
    # Copy laptop client to SD card root for easy access
    $laptopClient = "H:\pi-microcloud-laptop-client.py"
    if (Test-Path $laptopClient) {
        Copy-Item $laptopClient "$SDCardDrive\pi-microcloud-laptop-client.py" -Force
        Write-Host "✅ Laptop client copied to SD card root" -ForegroundColor Green
    }
    
    # Create quick setup instructions on SD card
    $quickSetup = @"
# 🚀💎⚡ PI MICRO-CLOUD QUICK SETUP INSTRUCTIONS ⚡💎🚀

## STEP 1: Boot Your Pi
1. Insert this SD card into your Raspberry Pi
2. Connect Pi to network (Ethernet or WiFi)
3. Power on the Pi
4. Wait for boot to complete

## STEP 2: SSH Into Pi
```bash
# Find your Pi's IP address (check your router or use network scanner)
# Default credentials: pi/raspberry (change after setup!)
ssh pi@[PI_IP_ADDRESS]
```

## STEP 3: Deploy Pi Micro-Cloud
```bash
# Navigate to deployment directory
cd /boot/pi-microcloud

# Make setup script executable
chmod +x setup-pi-microcloud.sh

# Run the complete setup (includes auto-boot configuration)
./setup-pi-microcloud.sh
```

## STEP 4: Test Your Deployment
```bash
# Check if services are running
docker ps

# Test health endpoint
curl http://localhost/health

# Check Pi status
curl http://localhost/pi/status
```

## STEP 5: Configure Laptop Client
1. Find your Pi's IP address: `hostname -I`
2. Update laptop client with Pi IP
3. Test offloading: `python pi-microcloud-laptop-client.py`

## AUTO-BOOT FEATURES
✅ Pi micro-cloud starts automatically on boot
✅ Services restart on failure
✅ Health monitoring enabled
✅ Complete logging system

## SERVICE MANAGEMENT
```bash
# Check auto-boot service status
sudo systemctl status pi-microcloud

# Manual service control
sudo systemctl start|stop|restart pi-microcloud

# View service logs
sudo journalctl -u pi-microcloud -f
```

## ENDPOINTS (Replace [PI_IP] with actual IP)
- Health: http://[PI_IP]/health
- Status: http://[PI_IP]/pi/status  
- Offloading: http://[PI_IP]/api/offload
- Metrics: http://[PI_IP]/metrics

## TROUBLESHOOTING
If setup fails:
1. Check internet connection: `ping google.com`
2. Update system: `sudo apt update && sudo apt upgrade -y`
3. Check Docker: `sudo systemctl status docker`
4. Check logs: `sudo journalctl -u pi-microcloud`

🏆 Your Pi micro-cloud will handle laptop task offloading automatically! 🚀💎⚡
"@
    
    $quickSetup | Out-File "$SDCardDrive\PI-SETUP-INSTRUCTIONS.md" -Encoding UTF8
    Write-Host "✅ Setup instructions created: PI-SETUP-INSTRUCTIONS.md" -ForegroundColor Green
    
    # Create a simple first-boot script
    $firstBootScript = @'
#!/bin/bash
# 🚀💎⚡ PI MICRO-CLOUD FIRST BOOT SCRIPT ⚡💎🚀

echo "🥧 Pi Micro-Cloud First Boot Setup..."

# Check if we're running from boot partition
if [ -d "/boot/pi-microcloud" ]; then
    echo "📁 Found pi-microcloud on boot partition"
    
    # Copy to home directory if not already there
    if [ ! -d "/home/pi/empire/pi-microcloud" ]; then
        echo "📤 Copying pi-microcloud to home directory..."
        mkdir -p /home/pi/empire
        cp -r /boot/pi-microcloud /home/pi/empire/
        chown -R pi:pi /home/pi/empire
        echo "✅ Pi micro-cloud copied to /home/pi/empire/pi-microcloud"
    fi
    
    # Make setup script executable
    chmod +x /home/pi/empire/pi-microcloud/setup-pi-microcloud.sh
    
    echo "🚀 Ready to deploy! Run:"
    echo "   cd /home/pi/empire/pi-microcloud"
    echo "   ./setup-pi-microcloud.sh"
else
    echo "❌ Pi micro-cloud files not found on boot partition"
fi
'@
    
    $firstBootScript | Out-File "$targetDir\first-boot-setup.sh" -Encoding UTF8
    
    # Create deployment summary
    $deploymentFiles = Get-ChildItem $targetDir -Recurse | Measure-Object
    $totalSize = Get-ChildItem $targetDir -Recurse | Measure-Object -Property Length -Sum
    
    Write-Host "`n🎊 SD CARD DEPLOYMENT COMPLETE! 🎊" -ForegroundColor Green
    Write-Host "=" * 60 -ForegroundColor Yellow
    
    Write-Host "📊 DEPLOYMENT SUMMARY:" -ForegroundColor Cyan
    Write-Host "   • Target: $targetDir" -ForegroundColor White
    Write-Host "   • Files: $($deploymentFiles.Count) files deployed" -ForegroundColor White
    Write-Host "   • Size: $([math]::Round($totalSize.Sum / 1MB, 2)) MB" -ForegroundColor White
    
    Write-Host "`n📁 DEPLOYED FILES:" -ForegroundColor Cyan
    Write-Host "   • pi-microcloud/ - Complete deployment directory" -ForegroundColor White
    Write-Host "   • pi-microcloud-laptop-client.py - Laptop integration client" -ForegroundColor White
    Write-Host "   • PI-SETUP-INSTRUCTIONS.md - Quick setup guide" -ForegroundColor White
    
    Write-Host "`n🎯 NEXT STEPS:" -ForegroundColor Cyan
    Write-Host "1. 🔌 Insert SD card into Raspberry Pi" -ForegroundColor White
    Write-Host "2. 🔋 Power on Pi and wait for boot" -ForegroundColor White
    Write-Host "3. 🌐 SSH into Pi: ssh pi@[PI_IP]" -ForegroundColor White
    Write-Host "4. 📁 Navigate: cd /boot/pi-microcloud" -ForegroundColor White
    Write-Host "5. 🚀 Run: ./setup-pi-microcloud.sh" -ForegroundColor White
    
    Write-Host "`n🔄 AUTO-BOOT FEATURES:" -ForegroundColor Cyan
    Write-Host "   • Pi micro-cloud starts automatically on boot" -ForegroundColor White
    Write-Host "   • Services restart on failure" -ForegroundColor White
    Write-Host "   • Health monitoring and logging enabled" -ForegroundColor White
    Write-Host "   • Complete systemd integration" -ForegroundColor White
    
    Write-Host "`n⚡ LAPTOP OFFLOADING READY:" -ForegroundColor Cyan
    Write-Host "   • Web scraping tasks" -ForegroundColor White
    Write-Host "   • Data processing operations" -ForegroundColor White
    Write-Host "   • API call batching" -ForegroundColor White
    Write-Host "   • Background computations" -ForegroundColor White
    Write-Host "   • BCI data analysis" -ForegroundColor White
    
    Write-Host "`n🏆 Your Pi SD card is ready for legendary micro-cloud deployment! 🚀💎⚡" -ForegroundColor Green
    
} catch {
    Write-Host "❌ Deployment failed: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host "📋 Common issues:" -ForegroundColor Yellow
    Write-Host "   • SD card write-protected" -ForegroundColor White
    Write-Host "   • Insufficient space on SD card" -ForegroundColor White
    Write-Host "   • SD card not properly mounted" -ForegroundColor White
    exit 1
}

Write-Host "`n💡 TIP: Keep the setup instructions handy - they're now on your SD card!" -ForegroundColor Yellow

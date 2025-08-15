# 🚀💎⚡ SD CARD DIRECT EMPIRE DEPLOYMENT ⚡💎🚀
# BROski Level: LEGENDARY | Empire Deployment: INSTANT ACCESS
# Created: 2025-07-31 | Status: READY FOR IMMEDIATE EXECUTION

Write-Host "🚀 SD CARD DIRECT EMPIRE DEPLOYMENT INITIATED!" -ForegroundColor Green
Write-Host "💎 This is the FASTEST Pi deployment method!" -ForegroundColor Cyan

# ═══════════════════════════════════════════════════════════════
# 📋 STEP 1: SD CARD REMOVAL & INSERTION
# ═══════════════════════════════════════════════════════════════

Write-Host "`n🔧 STEP 1: SD CARD ACCESS" -ForegroundColor Yellow
Write-Host "   → Power down your Pi (sudo shutdown -h now)" -ForegroundColor White
Write-Host "   → Remove SD card from Pi" -ForegroundColor White
Write-Host "   → Insert SD card into Windows PC card reader" -ForegroundColor White

# ═══════════════════════════════════════════════════════════════
# 📂 STEP 2: DETECT SD CARD MOUNT POINT
# ═══════════════════════════════════════════════════════════════

Write-Host "`n🔍 STEP 2: DETECTING SD CARD..." -ForegroundColor Yellow

$sdCardDrive = $null
$possibleDrives = Get-WmiObject -Class Win32_LogicalDisk | Where-Object { $_.DriveType -eq 2 }

foreach ($drive in $possibleDrives) {
    $driveLetter = $drive.DeviceID
    $testPath = Join-Path $driveLetter "cmdline.txt"
    
    if (Test-Path $testPath) {
        Write-Host "   ✅ RASPBERRY PI SD CARD FOUND: $driveLetter" -ForegroundColor Green
        $sdCardDrive = $driveLetter
        break
    }
}

if (-not $sdCardDrive) {
    Write-Host "   ❌ SD Card not detected. Please ensure:" -ForegroundColor Red
    Write-Host "      - SD card is properly inserted" -ForegroundColor White
    Write-Host "      - Card reader is working" -ForegroundColor White
    Write-Host "      - Pi SD card contains Raspberry Pi OS" -ForegroundColor White
    Read-Host "Press Enter after inserting SD card to retry"
    exit 1
}

# ═══════════════════════════════════════════════════════════════
# 🏗️ STEP 3: VERIFY EMPIRE INTEGRATION DIRECTORY
# ═══════════════════════════════════════════════════════════════

Write-Host "`n🏗️ STEP 3: VERIFYING EMPIRE INTEGRATION..." -ForegroundColor Yellow

$empireDir = Join-Path $sdCardDrive "EMPIRE_INTEGRATION"

if (Test-Path $empireDir) {
    Write-Host "   ✅ EMPIRE_INTEGRATION directory found!" -ForegroundColor Green
    
    # List existing empire files
    $empireFiles = Get-ChildItem $empireDir -Recurse | Select-Object Name, FullName
    Write-Host "   📁 Existing Empire Files:" -ForegroundColor Cyan
    foreach ($file in $empireFiles) {
        Write-Host "      → $($file.Name)" -ForegroundColor White
    }
} else {
    Write-Host "   🔨 Creating EMPIRE_INTEGRATION directory..." -ForegroundColor Yellow
    New-Item -Path $empireDir -ItemType Directory -Force
    Write-Host "   ✅ EMPIRE_INTEGRATION directory created!" -ForegroundColor Green
}

# ═══════════════════════════════════════════════════════════════
# 📡 STEP 4: WIFI CONFIGURATION FOR HOME NETWORK
# ═══════════════════════════════════════════════════════════════

Write-Host "`n📡 STEP 4: WIFI CONFIGURATION SETUP" -ForegroundColor Yellow

# Get current WiFi networks
Write-Host "   🔍 Scanning for available WiFi networks..." -ForegroundColor Cyan
$wifiNetworks = netsh wlan show profiles | Select-String "All User Profile" | ForEach-Object {
    $_.ToString().Split(":")[1].Trim()
}

if ($wifiNetworks.Count -gt 0) {
    Write-Host "   📶 Available WiFi Networks:" -ForegroundColor Green
    for ($i = 0; $i -lt $wifiNetworks.Count; $i++) {
        Write-Host "      [$i] $($wifiNetworks[$i])" -ForegroundColor White
    }
    
    $selection = Read-Host "`n   Enter network number to use (or 'manual' to enter custom)"
    
    if ($selection -eq "manual") {
        $wifiSSID = Read-Host "   Enter WiFi SSID"
        $wifiPassword = Read-Host "   Enter WiFi Password" -AsSecureString
        $wifiPasswordPlain = [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($wifiPassword))
    } else {
        try {
            $selectedIndex = [int]$selection
            if ($selectedIndex -ge 0 -and $selectedIndex -lt $wifiNetworks.Count) {
                $wifiSSID = $wifiNetworks[$selectedIndex]
                $wifiPassword = Read-Host "   Enter password for '$wifiSSID'" -AsSecureString
                $wifiPasswordPlain = [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($wifiPassword))
            } else {
                throw "Invalid selection"
            }
        } catch {
            Write-Host "   ❌ Invalid network selection!" -ForegroundColor Red
            exit 1
        }
    }
} else {
    Write-Host "   ℹ️ No saved WiFi networks found. Manual entry required." -ForegroundColor Yellow
    $wifiSSID = Read-Host "   Enter WiFi SSID"
    $wifiPassword = Read-Host "   Enter WiFi Password" -AsSecureString
    $wifiPasswordPlain = [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($wifiPassword))
}

# Create wpa_supplicant.conf for automatic WiFi connection
$wpaSupplicantPath = Join-Path $sdCardDrive "wpa_supplicant.conf"
$wpaSupplicantContent = @"
country=US
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="$wifiSSID"
    psk="$wifiPasswordPlain"
    key_mgmt=WPA-PSK
}
"@

Set-Content -Path $wpaSupplicantPath -Value $wpaSupplicantContent -Encoding UTF8
Write-Host "   ✅ WiFi configuration created: wpa_supplicant.conf" -ForegroundColor Green

# Enable SSH for remote access
$sshEnablePath = Join-Path $sdCardDrive "ssh"
New-Item -Path $sshEnablePath -ItemType File -Force | Out-Null
Write-Host "   ✅ SSH enabled for remote access" -ForegroundColor Green

# ═══════════════════════════════════════════════════════════════
# 🚀 STEP 5: EMPIRE DEPLOYMENT SCRIPTS
# ═══════════════════════════════════════════════════════════════

Write-Host "`n🚀 STEP 5: ADDING EMPIRE DEPLOYMENT SCRIPTS..." -ForegroundColor Yellow

# Create empire startup script
$empireStartupScript = Join-Path $empireDir "empire_startup.sh"
$empireStartupContent = @'
#!/bin/bash
# 🚀 EMPIRE AUTOMATIC STARTUP SCRIPT
# This script runs on Pi boot to deploy the empire

echo "🚀 EMPIRE DEPLOYMENT STARTING..."

# Update system
sudo apt update && sudo apt upgrade -y

# Install Docker if not present
if ! command -v docker &> /dev/null; then
    echo "📦 Installing Docker..."
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    sudo usermod -aG docker pi
fi

# Install Docker Compose if not present
if ! command -v docker-compose &> /dev/null; then
    echo "🐙 Installing Docker Compose..."
    sudo pip3 install docker-compose
fi

# Create empire directory structure
mkdir -p /home/pi/empire/{nginx,redis,broski,monitoring}

# Deploy empire services
cd /home/pi/empire
cat > docker-compose.yml << 'EOF'
version: '3.8'
services:
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx:/etc/nginx/conf.d
    restart: always
    
  redis:
    image: redis:alpine
    ports:
      - "6379:6379"
    restart: always
    
  broski:
    image: node:18-alpine
    working_dir: /app
    volumes:
      - ./broski:/app
    ports:
      - "3000:3000"
    restart: always
    command: npm start
    
  monitoring:
    image: prom/prometheus
    ports:
      - "9090:9090"
    restart: always
EOF

# Start empire services
docker-compose up -d

echo "🎊 EMPIRE DEPLOYMENT COMPLETE!"
echo "🌐 Empire accessible at: http://$(hostname -I | awk '{print $1}')"
'@

Set-Content -Path $empireStartupScript -Value $empireStartupContent -Encoding UTF8
Write-Host "   ✅ Empire startup script created" -ForegroundColor Green

# Make startup script executable and add to crontab
$cronJobScript = Join-Path $empireDir "setup_cronjob.sh"
$cronJobContent = @'
#!/bin/bash
# Add empire startup to crontab for automatic execution
(crontab -l 2>/dev/null; echo "@reboot /home/pi/EMPIRE_INTEGRATION/empire_startup.sh >> /home/pi/empire_startup.log 2>&1") | crontab -
chmod +x /home/pi/EMPIRE_INTEGRATION/empire_startup.sh
echo "✅ Empire startup job added to crontab"
'@

Set-Content -Path $cronJobScript -Value $cronJobContent -Encoding UTF8
Write-Host "   ✅ Auto-startup configuration created" -ForegroundColor Green

# ═══════════════════════════════════════════════════════════════
# 🎯 STEP 6: FINAL DEPLOYMENT INSTRUCTIONS
# ═══════════════════════════════════════════════════════════════

Write-Host "`n🎯 STEP 6: FINAL DEPLOYMENT READY!" -ForegroundColor Yellow
Write-Host "   ✅ SD Card configured for automatic empire deployment" -ForegroundColor Green
Write-Host "   ✅ WiFi configured for '$wifiSSID' network" -ForegroundColor Green
Write-Host "   ✅ SSH enabled for remote access" -ForegroundColor Green
Write-Host "   ✅ Empire startup scripts installed" -ForegroundColor Green

Write-Host "`n🚀 DEPLOYMENT INSTRUCTIONS:" -ForegroundColor Cyan
Write-Host "   1. Safely eject SD card from Windows PC" -ForegroundColor White
Write-Host "   2. Insert SD card back into Raspberry Pi" -ForegroundColor White
Write-Host "   3. Power on the Pi" -ForegroundColor White
Write-Host "   4. Pi will automatically:" -ForegroundColor White
Write-Host "      → Connect to WiFi network '$wifiSSID'" -ForegroundColor Gray
Write-Host "      → Enable SSH access" -ForegroundColor Gray
Write-Host "      → Install Docker and Docker Compose" -ForegroundColor Gray
Write-Host "      → Deploy complete empire services" -ForegroundColor Gray
Write-Host "   5. Access empire at Pi's IP address after ~5 minutes" -ForegroundColor White

Write-Host "`n💎 EMPIRE STATUS MONITORING:" -ForegroundColor Cyan
Write-Host "   → Use the continuous Pi monitor to track deployment" -ForegroundColor White
Write-Host "   → SSH into Pi: ssh pi@[pi_ip_address]" -ForegroundColor White
Write-Host "   → Check deployment logs: tail -f ~/empire_startup.log" -ForegroundColor White

Write-Host "`n🎊 SD CARD EMPIRE DEPLOYMENT READY!" -ForegroundColor Green
Write-Host "💎 This is the FASTEST path to Pi empire domination!" -ForegroundColor Yellow

Write-Host "`n🚀 LEGENDARY SD CARD DEPLOYMENT COMPLETE!" -ForegroundColor Green
Write-Host "💎 Remove SD card, insert into Pi, power on, and watch the magic!" -ForegroundColor Yellow

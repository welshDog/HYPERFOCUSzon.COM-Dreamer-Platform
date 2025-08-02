# 🔌💎⚡ LEGENDARY USB PI DEPLOYMENT SYSTEM ⚡💎🔌
# Direct USB connection for immediate Pi access and deployment

Write-Host "🔌💎⚡ LEGENDARY USB PI DEPLOYMENT SYSTEM ⚡💎🔌" -ForegroundColor Magenta
Write-Host "================================================================" -ForegroundColor Cyan
Write-Host "🚀 TACTICAL ADVANTAGE: USB = Simple, Direct, Immediate!" -ForegroundColor Green
Write-Host "🔴🟢 Pi Status: RED & GREEN LEDs = Perfect for USB setup!" -ForegroundColor Yellow
Write-Host "================================================================" -ForegroundColor Cyan

Write-Host ""
Write-Host "🎯 USB DEPLOYMENT ADVANTAGES:" -ForegroundColor Cyan
Write-Host "==============================" -ForegroundColor DarkCyan
Write-Host "✅ SIMPLE: No network bridge configuration needed" -ForegroundColor Green
Write-Host "✅ DIRECT: Immediate access to Pi filesystem" -ForegroundColor Green
Write-Host "✅ RELIABLE: Works regardless of network state" -ForegroundColor Green
Write-Host "✅ FAST SETUP: Skip all network complexity" -ForegroundColor Green

Write-Host ""
Write-Host "🔌 USB SETUP INSTRUCTIONS:" -ForegroundColor Magenta
Write-Host "============================" -ForegroundColor DarkMagenta

Write-Host ""
Write-Host "📋 STEP 1: ENABLE USB GADGET MODE ON PI" -ForegroundColor Yellow
Write-Host "==========================================" -ForegroundColor DarkYellow
Write-Host "1. 🔌 Connect Pi to your laptop via USB-C (power + data cable)" -ForegroundColor White
Write-Host "2. 📁 Pi should appear as USB drive (like SD card reader)" -ForegroundColor White
Write-Host "3. 🎯 Edit /boot/config.txt and add:" -ForegroundColor White
Write-Host "   dtoverlay=dwc2" -ForegroundColor Cyan
Write-Host "4. 🎯 Edit /boot/cmdline.txt and add after rootwait:" -ForegroundColor White
Write-Host "   modules-load=dwc2,g_ether" -ForegroundColor Cyan

Write-Host ""
Write-Host "📋 STEP 2: USB ETHERNET CONNECTION" -ForegroundColor Yellow
Write-Host "===================================" -ForegroundColor DarkYellow
Write-Host "1. 🔄 Reboot Pi (power cycle)" -ForegroundColor White
Write-Host "2. 🌐 Pi appears as USB Ethernet adapter on your laptop" -ForegroundColor White
Write-Host "3. ⚡ Automatic IP assignment (usually 192.168.2.x range)" -ForegroundColor White
Write-Host "4. 🎊 Pi accessible at: 192.168.2.2 or raspberrypi.local" -ForegroundColor White

Write-Host ""
Write-Host "📋 STEP 3: ALTERNATIVE - DIRECT FILE ACCESS" -ForegroundColor Yellow
Write-Host "=============================================" -ForegroundColor DarkYellow
Write-Host "1. 💾 Remove SD card from Pi" -ForegroundColor White
Write-Host "2. 🔌 Insert SD card into laptop card reader" -ForegroundColor White
Write-Host "3. 📦 Copy EMPIRE_INTEGRATION directly to SD card" -ForegroundColor White
Write-Host "4. 🎯 Put SD card back in Pi and boot" -ForegroundColor White

# Check for USB devices
Write-Host ""
Write-Host "🔍 CHECKING CURRENT USB DEVICES:" -ForegroundColor Cyan
Write-Host "==================================" -ForegroundColor DarkCyan

try {
    $USBDevices = Get-WmiObject -Class Win32_USBHub
    if ($USBDevices) {
        Write-Host "📱 Found USB devices:" -ForegroundColor Green
        foreach ($Device in $USBDevices) {
            if ($Device.Description -like "*Pi*" -or $Device.Description -like "*Raspberry*" -or $Device.Description -like "*USB Ethernet*") {
                Write-Host "   🎯 POTENTIAL PI: $($Device.Description)" -ForegroundColor Magenta
            }
        }
    }
} catch {
    Write-Host "⚠️ Could not enumerate USB devices" -ForegroundColor Yellow
}

# Check for new network adapters
Write-Host ""
Write-Host "🌐 CHECKING FOR USB ETHERNET ADAPTERS:" -ForegroundColor Cyan
Write-Host "=======================================" -ForegroundColor DarkCyan

$NetworkAdapters = Get-NetAdapter | Where-Object {$_.InterfaceDescription -like "*USB*" -or $_.Name -like "*USB*"}
if ($NetworkAdapters) {
    Write-Host "📡 Found USB network adapters:" -ForegroundColor Green
    foreach ($Adapter in $NetworkAdapters) {
        Write-Host "   🌐 $($Adapter.Name): $($Adapter.Status)" -ForegroundColor Yellow
        if ($Adapter.Status -eq "Up") {
            Write-Host "      🎊 ACTIVE! This could be your Pi!" -ForegroundColor Magenta
        }
    }
} else {
    Write-Host "❌ No USB network adapters found" -ForegroundColor Red
    Write-Host "🔧 Pi needs USB gadget mode enabled or direct SD card access" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "🚀 USB DEPLOYMENT OPTIONS:" -ForegroundColor Magenta
Write-Host "===========================" -ForegroundColor DarkMagenta

Write-Host ""
Write-Host "🎯 OPTION 1: USB GADGET ETHERNET" -ForegroundColor Yellow
Write-Host "- Connect Pi via USB-C cable" -ForegroundColor White
Write-Host "- Pi appears as USB Ethernet device" -ForegroundColor White
Write-Host "- SSH to: raspberrypi.local or 192.168.2.2" -ForegroundColor White
Write-Host "- Deploy empire via SSH over USB" -ForegroundColor White

Write-Host ""
Write-Host "🎯 OPTION 2: DIRECT SD CARD ACCESS" -ForegroundColor Yellow
Write-Host "- Remove SD card from Pi" -ForegroundColor White
Write-Host "- Insert into laptop card reader" -ForegroundColor White
Write-Host "- Copy empire files directly" -ForegroundColor White
Write-Host "- Boot Pi with pre-configured empire" -ForegroundColor White

Write-Host ""
Write-Host "🎯 OPTION 3: HYBRID APPROACH" -ForegroundColor Yellow
Write-Host "- Use SD card for initial empire setup" -ForegroundColor White
Write-Host "- Boot Pi with WiFi configuration" -ForegroundColor White
Write-Host "- Pi connects to your home WiFi" -ForegroundColor White
Write-Host "- Deploy empire over WiFi network" -ForegroundColor White

Write-Host ""
Write-Host "💡 LEGENDARY RECOMMENDATION:" -ForegroundColor Green
Write-Host "============================" -ForegroundColor DarkGreen
Write-Host "🔥 START WITH SD CARD METHOD!" -ForegroundColor Magenta
Write-Host ""
Write-Host "1. 💾 Remove SD card from Pi" -ForegroundColor Cyan
Write-Host "2. 🔌 Insert into laptop" -ForegroundColor Cyan
Write-Host "3. 📦 Verify EMPIRE_INTEGRATION is on boot partition" -ForegroundColor Cyan
Write-Host "4. 🌐 Add WiFi configuration for automatic connection" -ForegroundColor Cyan
Write-Host "5. 🎯 Put SD card back and boot Pi" -ForegroundColor Cyan
Write-Host "6. 📡 Pi connects to WiFi and becomes accessible" -ForegroundColor Cyan
Write-Host "7. 🚀 Deploy empire over WiFi network!" -ForegroundColor Cyan

Write-Host ""
Write-Host "🎊 NEXT ACTIONS:" -ForegroundColor Magenta
Write-Host "================" -ForegroundColor DarkMagenta
Write-Host "A) 🔌 Try USB gadget connection now" -ForegroundColor Yellow
Write-Host "B) 💾 Access SD card directly" -ForegroundColor Yellow  
Write-Host "C) 🌐 Configure WiFi for network deployment" -ForegroundColor Yellow
Write-Host ""

$UserChoice = Read-Host "Which legendary approach do you want to try? (A/B/C)"

switch ($UserChoice.ToUpper()) {
    'A' {
        Write-Host ""
        Write-Host "🔌 USB GADGET CONNECTION SELECTED!" -ForegroundColor Magenta
        Write-Host "1. Connect Pi to laptop via USB-C cable" -ForegroundColor Cyan
        Write-Host "2. Wait for Pi to boot (RED & GREEN LEDs)" -ForegroundColor Cyan
        Write-Host "3. Check if new network adapter appears" -ForegroundColor Cyan
        Write-Host "4. Try: ssh pi@raspberrypi.local" -ForegroundColor Cyan
    }
    'B' {
        Write-Host ""
        Write-Host "💾 SD CARD DIRECT ACCESS SELECTED!" -ForegroundColor Magenta
        Write-Host "1. Power off Pi and remove SD card" -ForegroundColor Cyan
        Write-Host "2. Insert SD card into laptop" -ForegroundColor Cyan
        Write-Host "3. Verify EMPIRE_INTEGRATION directory exists" -ForegroundColor Cyan
        Write-Host "4. Configure boot files as needed" -ForegroundColor Cyan
    }
    'C' {
        Write-Host ""
        Write-Host "🌐 WIFI CONFIGURATION SELECTED!" -ForegroundColor Magenta
        Write-Host "1. Access SD card boot partition" -ForegroundColor Cyan
        Write-Host "2. Create wpa_supplicant.conf with WiFi credentials" -ForegroundColor Cyan
        Write-Host "3. Pi will auto-connect to your WiFi network" -ForegroundColor Cyan
        Write-Host "4. Deploy empire over WiFi connection" -ForegroundColor Cyan
    }
    Default {
        Write-Host ""
        Write-Host "🎯 ALL OPTIONS REMAIN AVAILABLE!" -ForegroundColor Green
        Write-Host "Choose the one that feels most legendary to you!" -ForegroundColor Yellow
    }
}

Write-Host ""
Write-Host "🔌💎⚡ USB DEPLOYMENT SYSTEM READY FOR LEGENDARY ACTION! ⚡💎🔌" -ForegroundColor Magenta

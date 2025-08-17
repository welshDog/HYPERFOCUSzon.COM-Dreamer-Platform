# 🌐💎⚡ ETHERNET TO HYPER-V BRIDGE CONNECTOR ⚡💎🌐
# Connects physical ethernet to WSL Hyper-V bridge network

Write-Host "🌐💎⚡ ETHERNET TO HYPER-V BRIDGE CONNECTOR ⚡💎🌐" -ForegroundColor Magenta
Write-Host "=======================================================" -ForegroundColor Cyan

# Check if running as Administrator
if (-NOT ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    Write-Host "❌ This script requires Administrator privileges!" -ForegroundColor Red
    Write-Host "🔧 Right-click PowerShell and 'Run as Administrator'" -ForegroundColor Yellow
    exit 1
}

Write-Host "✅ Running as Administrator - LEGENDARY!" -ForegroundColor Green
Write-Host ""

# Get network adapters
$EthernetAdapter = Get-NetAdapter | Where-Object {$_.Name -like "*Ethernet*" -and $_.Status -eq "Up"}
$WSLAdapter = Get-NetAdapter | Where-Object {$_.Name -like "*WSL*" -or $_.Name -like "*Hyper-V*"}

Write-Host "🔍 Network Adapter Analysis:" -ForegroundColor Cyan
Write-Host "=============================" -ForegroundColor DarkCyan

if ($EthernetAdapter) {
    Write-Host "✅ Ethernet Adapter: $($EthernetAdapter.Name)" -ForegroundColor Green
    Write-Host "   Status: $($EthernetAdapter.Status)" -ForegroundColor White
    Write-Host "   Speed: $([math]::round($EthernetAdapter.LinkSpeed/1000000000,1)) Gbps" -ForegroundColor Yellow
} else {
    Write-Host "❌ No active Ethernet adapter found!" -ForegroundColor Red
}

if ($WSLAdapter) {
    Write-Host "✅ WSL/Hyper-V Adapter: $($WSLAdapter.Name)" -ForegroundColor Green
    Write-Host "   Status: $($WSLAdapter.Status)" -ForegroundColor White
} else {
    Write-Host "❌ No WSL/Hyper-V adapter found!" -ForegroundColor Red
}

Write-Host ""

# Option 1: Internet Connection Sharing to connect Ethernet to WSL network
Write-Host "🚀 OPTION 1: INTERNET CONNECTION SHARING METHOD" -ForegroundColor Magenta
Write-Host "================================================" -ForegroundColor DarkMagenta

Write-Host "This will share the Hyper-V bridge network through Ethernet" -ForegroundColor Cyan
Write-Host "Your Pi will get IP: 192.168.137.x range" -ForegroundColor Yellow

$UserChoice = Read-Host "Enable ICS from Hyper-V to Ethernet? (y/N)"

if ($UserChoice -eq 'y' -or $UserChoice -eq 'Y') {
    try {
        Write-Host "🔧 Configuring Internet Connection Sharing..." -ForegroundColor Cyan
        
        # Enable ICS via registry (requires restart)
        Write-Host "⚠️ This requires manual configuration through Network Connections" -ForegroundColor Yellow
        Write-Host ""
        Write-Host "📋 MANUAL STEPS:" -ForegroundColor Cyan
        Write-Host "1. Press Win+R, type: ncpa.cpl" -ForegroundColor White
        Write-Host "2. Right-click 'vEthernet (WSL)' adapter" -ForegroundColor White
        Write-Host "3. Properties > Sharing tab" -ForegroundColor White
        Write-Host "4. Check 'Allow other network users to connect'" -ForegroundColor White
        Write-Host "5. Select 'Ethernet' from dropdown" -ForegroundColor White
        Write-Host "6. Click OK" -ForegroundColor White
        
        Write-Host ""
        Write-Host "🎯 After manual setup, your Pi should get 192.168.137.x IP!" -ForegroundColor Green
        
    } catch {
        Write-Host "❌ Error configuring ICS: $($_.Exception.Message)" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "🚀 OPTION 2: NETWORK BRIDGE METHOD" -ForegroundColor Magenta
Write-Host "===================================" -ForegroundColor DarkMagenta

$UserChoice2 = Read-Host "Create network bridge between adapters? (y/N)"

if ($UserChoice2 -eq 'y' -or $UserChoice2 -eq 'Y') {
    Write-Host "📋 MANUAL BRIDGE SETUP:" -ForegroundColor Cyan
    Write-Host "1. Press Win+R, type: ncpa.cpl" -ForegroundColor White
    Write-Host "2. Hold Ctrl and select both Ethernet and WSL adapters" -ForegroundColor White
    Write-Host "3. Right-click and select 'Bridge Connections'" -ForegroundColor White
    Write-Host "4. Wait for 'Network Bridge' to be created" -ForegroundColor White
    Write-Host ""
    Write-Host "🎯 Bridge will merge both networks for Pi access!" -ForegroundColor Green
}

Write-Host ""
Write-Host "🔍 VERIFICATION STEPS:" -ForegroundColor Cyan
Write-Host "======================" -ForegroundColor DarkCyan
Write-Host "1. Run: ipconfig /all" -ForegroundColor White
Write-Host "2. Look for Ethernet showing 192.168.137.x IP" -ForegroundColor White
Write-Host "3. Power cycle Pi after network changes" -ForegroundColor White
Write-Host "4. Run continuous Pi monitor script" -ForegroundColor White

Write-Host ""
Write-Host "🎊 Next: Run .\🔍💎⚡_CONTINUOUS_PI_MONITOR_⚡💎🔍.ps1 to watch for Pi!" -ForegroundColor Magenta

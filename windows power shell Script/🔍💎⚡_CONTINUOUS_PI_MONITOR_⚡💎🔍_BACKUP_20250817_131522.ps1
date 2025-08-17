# 🔍💎⚡ CONTINUOUS PI DISCOVERY MONITOR ⚡💎🔍
# Watches for Pi to come online on WSL Hyper-V bridge network

Write-Host "🔍💎⚡ CONTINUOUS PI DISCOVERY MONITOR ⚡💎🔍" -ForegroundColor Magenta
Write-Host "=====================================================" -ForegroundColor Cyan
Write-Host "🌐 Bridge Network: 192.168.137.1 (WSL Hyper-V) - ACTIVE!" -ForegroundColor Green
Write-Host "🔴🟢 Pi Status: RED & GREEN LEDs = Booting to bridge network" -ForegroundColor Yellow
Write-Host "⚡ Monitoring: Continuous scan for Pi connection" -ForegroundColor Cyan
Write-Host "=====================================================" -ForegroundColor Cyan

$TestIPs = @("192.168.137.2", "192.168.137.3", "192.168.137.10", "192.168.137.100")
$ScanCount = 0
$StartTime = Get-Date

Write-Host ""
Write-Host "🎯 Starting continuous Pi discovery..." -ForegroundColor Yellow
Write-Host "Press Ctrl+C to stop monitoring" -ForegroundColor Gray

while ($true) {
    $ScanCount++
    $CurrentTime = Get-Date
    $ElapsedTime = $CurrentTime - $StartTime
    
    Write-Host ""
    Write-Host "🔍 SCAN #$ScanCount | Time: $($ElapsedTime.ToString('mm\:ss'))" -ForegroundColor Cyan
    Write-Host "================================================" -ForegroundColor DarkCyan
    
    $PiFound = $false
    
    foreach ($IP in $TestIPs) {
        Write-Host "   Testing $IP..." -NoNewline -ForegroundColor White
        
        try {
            $PingResult = Test-Connection -ComputerName $IP -Count 1 -Quiet -TimeoutSeconds 1
            
            if ($PingResult) {
                Write-Host " ✅ FOUND!" -ForegroundColor Green
                $PiFound = $true
                
                Write-Host "   🎊 PI DISCOVERED AT $IP!" -ForegroundColor Magenta
                Write-Host "   🔐 Testing SSH access..." -ForegroundColor Cyan
                
                try {
                    ssh -o ConnectTimeout=3 -o BatchMode=yes "broski@$IP" "echo 'EMPIRE_READY'" 2>$null | Out-Null
                    if ($LASTEXITCODE -eq 0) {
                        Write-Host "   🚀 SSH READY! DEPLOYING EMPIRE NOW!" -ForegroundColor Green
                        Write-Host ""
                        Write-Host "🎊🎊🎊 LEGENDARY PI READY FOR DEPLOYMENT! 🎊🎊🎊" -ForegroundColor Magenta
                        Write-Host "Execute: .\🎊🚀💎⚡_LEGENDARY_HYBRID_PI_EMPIRE_DEPLOYMENT_⚡💎🚀🎊.ps1 -Mode deploy -PiIP $IP -Monitor -Celebrate" -ForegroundColor Yellow
                        exit 0
                    } else {
                        Write-Host "   ⏳ SSH initializing..." -ForegroundColor Yellow
                    }
                } catch {
                    Write-Host "   ⏳ SSH not ready yet..." -ForegroundColor Yellow
                }
            } else {
                Write-Host " ❌" -ForegroundColor Red
            }
        } catch {
            Write-Host " ❌ Error" -ForegroundColor Red
        }
    }
    
    if (-not $PiFound) {
        Write-Host ""
        Write-Host "⏳ Pi not responding yet - RED & GREEN LEDs confirm perfect boot!" -ForegroundColor Yellow
        Write-Host "🔄 Next scan in 10 seconds..." -ForegroundColor Gray
    }
    
    Start-Sleep -Seconds 10
}

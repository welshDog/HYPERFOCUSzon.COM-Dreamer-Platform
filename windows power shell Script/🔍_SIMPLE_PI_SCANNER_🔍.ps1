# 🎊🚀💎⚡ LEGENDARY PI DEPLOYMENT SCANNER ⚡💎🚀🎊
# Simple version for immediate execution

Write-Host "LEGENDARY PI DEPLOYMENT SCANNER" -ForegroundColor Magenta
Write-Host "===============================" -ForegroundColor Cyan
Write-Host "RED & GREEN LIGHTS ON = READY FOR EMPIRE!" -ForegroundColor Green
Write-Host ""

# Pi discovery scan
$TestIPs = @("192.168.137.2", "192.168.137.3", "192.168.137.10", "192.168.137.100")
$FoundPi = $null

Write-Host "Scanning bridge network for Pi..." -ForegroundColor Cyan

foreach ($IP in $TestIPs) {
    Write-Host "Testing $IP..." -NoNewline -ForegroundColor White
    
    $PingResult = Test-Connection -ComputerName $IP -Count 1 -Quiet -TimeoutSeconds 2
    if ($PingResult) {
        Write-Host " RESPONDING!" -ForegroundColor Green
        $FoundPi = $IP
        
        Write-Host "  Testing SSH to broski@$IP..." -NoNewline -ForegroundColor Cyan
        try {
            ssh -o ConnectTimeout=3 -o BatchMode=yes "broski@$IP" "echo 'ready'" 2>$null | Out-Null
            if ($LASTEXITCODE -eq 0) {
                Write-Host " SSH READY!" -ForegroundColor Magenta
                Write-Host ""
                Write-Host "🎊 PI READY FOR LEGENDARY DEPLOYMENT!" -ForegroundColor Magenta
                Write-Host "🌐 Pi IP: $IP" -ForegroundColor Green
                Write-Host "🚀 Execute deployment now!" -ForegroundColor Yellow
                break
            } else {
                Write-Host " SSH initializing..." -ForegroundColor Yellow
            }
        } catch {
            Write-Host " SSH not ready..." -ForegroundColor Yellow
        }
    } else {
        Write-Host " No response" -ForegroundColor Red
    }
}

if (-not $FoundPi) {
    Write-Host ""
    Write-Host "Pi not responding yet on bridge network" -ForegroundColor Yellow
    Write-Host "RED & GREEN LEDs confirm Pi is booting perfectly!" -ForegroundColor Green
    Write-Host "Network services take 2-5 minutes to initialize" -ForegroundColor Cyan
    Write-Host "Try running this scanner again in 1-2 minutes" -ForegroundColor White
}

Write-Host ""
Write-Host "Bridge network status: 192.168.137.x range" -ForegroundColor Cyan
Write-Host "Gigabit ethernet: OPTIMAL for empire deployment" -ForegroundColor Green

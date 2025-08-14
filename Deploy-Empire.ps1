# HYPERFOCUS AZURE EMPIRE DEPLOYMENT

Write-Host "HYPERFOCUS AZURE EMPIRE DEPLOYMENT" -ForegroundColor Cyan
Write-Host ""
Write-Host "Starting legendary Azure transformation..." -ForegroundColor Yellow

# Check if AZD is available
try {
    azd --version | Out-Null
    Write-Host "Azure Developer CLI found" -ForegroundColor Green
} catch {
    Write-Host "Azure Developer CLI not found!" -ForegroundColor Red
    Write-Host "Please install AZD first: winget install microsoft.azd" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Login to Azure
Write-Host "Logging into Azure..." -ForegroundColor Yellow
azd auth login

# Deploy the empire
Write-Host "Deploying infrastructure..." -ForegroundColor Yellow
azd up

Write-Host ""
Write-Host "DEPLOYMENT COMPLETE! Check Azure portal for your legendary empire!" -ForegroundColor Magenta
Read-Host "Press Enter to continue"

# 🔍 Token Permission Verification Script

param(
    [Parameter(Mandatory=$true)]
    [string]$ApiToken
)

Write-Host "🔐 Testing API Token Permissions..." -ForegroundColor Cyan

$env:CLOUDFLARE_API_TOKEN = $ApiToken

Write-Host ""
Write-Host "1. 👤 Authentication Test:" -ForegroundColor Yellow
wrangler whoami

Write-Host ""
Write-Host "2. 🏢 Account Access Test:" -ForegroundColor Yellow
wrangler whoami | Select-String "Account ID"

Write-Host ""
Write-Host "3. 🌐 Zone Access Test:" -ForegroundColor Yellow
# This will show if we can access hyperfocuszone.com
$zoneResult = wrangler zone list 2>&1
if ($zoneResult -match "hyperfocuszone.com") {
    Write-Host "✅ hyperfocuszone.com zone access confirmed" -ForegroundColor Green
} else {
    Write-Host "⚠️  Zone access check - ensure token includes hyperfocuszone.com" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "4. ⚡ Workers Permission Test:" -ForegroundColor Yellow
# Test if we can list workers (indicates Workers Scripts permission)
wrangler deploy --dry-run -c wrangler-test.toml

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "🎉 TOKEN VERIFICATION SUCCESSFUL!" -ForegroundColor Green
    Write-Host "Ready for deployment!" -ForegroundColor Cyan
} else {
    Write-Host ""
    Write-Host "❌ Permission issues detected" -ForegroundColor Red
    Write-Host "Check token permissions in Cloudflare dashboard" -ForegroundColor Yellow
}

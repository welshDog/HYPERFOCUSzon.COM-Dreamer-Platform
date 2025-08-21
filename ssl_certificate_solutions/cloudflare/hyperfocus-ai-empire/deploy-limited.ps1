# 🚀 Limited Permission Deployment
# Works without User Details permission

param(
    [Parameter(Mandatory=$true)]
    [string]$ApiToken
)

Write-Host "🔧 DEPLOYING WITH LIMITED PERMISSIONS" -ForegroundColor Cyan
Write-Host "=====================================" -ForegroundColor Yellow

$env:CLOUDFLARE_API_TOKEN = $ApiToken

Write-Host "🎯 Deploying to workers.dev subdomain (no custom routes)..." -ForegroundColor Cyan
Write-Host "This avoids needing User Details permission!" -ForegroundColor Yellow
Write-Host ""

# Deploy simple version to workers.dev
wrangler deploy -c wrangler-simple.toml

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "🎉 DEPLOYMENT SUCCESSFUL!" -ForegroundColor Green
    Write-Host "=========================" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "🌐 Your AI Assistant is live at:" -ForegroundColor Green
    Write-Host "   https://hyperfocus-ai-assistant.YOUR_USERNAME.workers.dev" -ForegroundColor White
    Write-Host ""
    Write-Host "🧪 Test immediately:" -ForegroundColor Yellow
    Write-Host "curl https://hyperfocus-ai-assistant.YOUR_USERNAME.workers.dev/health" -ForegroundColor White
    Write-Host ""
    Write-Host "💬 Chat test:" -ForegroundColor Yellow
    Write-Host 'curl -X POST https://hyperfocus-ai-assistant.YOUR_USERNAME.workers.dev/chat \' -ForegroundColor White
    Write-Host '  -H "Content-Type: application/json" \' -ForegroundColor White
    Write-Host '  -d "{\"message\": \"Help me focus with ADHD\"}"' -ForegroundColor White
    Write-Host ""
    Write-Host "🎯 Techniques:" -ForegroundColor Yellow
    Write-Host "curl https://hyperfocus-ai-assistant.YOUR_USERNAME.workers.dev/techniques" -ForegroundColor White
    Write-Host ""
    Write-Host "🌟 AI EMPIRE IS LIVE! (workers.dev version)" -ForegroundColor Magenta

    # Try to set up custom route if possible
    Write-Host ""
    Write-Host "🔧 Attempting custom route setup..." -ForegroundColor Cyan
    wrangler deploy --env production

    if ($LASTEXITCODE -eq 0) {
        Write-Host "🏆 LEGENDARY! Custom route also working!" -ForegroundColor Magenta
        Write-Host "🌐 Also available at: https://support.hyperfocuszone.com/api/" -ForegroundColor Green
    } else {
        Write-Host "⚠️  Custom route needs additional permissions, but workers.dev is working!" -ForegroundColor Yellow
    }

} else {
    Write-Host "❌ Even simple deployment failed. Token may need:" -ForegroundColor Red
    Write-Host "   - Account:Cloudflare Workers:Edit permission" -ForegroundColor White
    Write-Host "   - Or try OAuth login with: wrangler login" -ForegroundColor White
}

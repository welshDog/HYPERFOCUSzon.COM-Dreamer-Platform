# 🚀 HyperFocus AI Assistant - Quick Deploy Script
# Run this after creating a new API token with proper permissions

param(
    [Parameter(Mandatory=$true)]
    [string]$ApiToken
)

Write-Host "🔧 Setting up HyperFocus AI Assistant deployment..." -ForegroundColor Cyan

# Set the API token
$env:CLOUDFLARE_API_TOKEN = $ApiToken
Write-Host "✅ API token configured" -ForegroundColor Green

# Verify authentication
Write-Host "🔍 Verifying authentication..." -ForegroundColor Yellow
wrangler whoami

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Authentication successful!" -ForegroundColor Green

    # Try deployment to workers.dev first (no custom routes)
    Write-Host "🚀 Deploying to workers.dev subdomain..." -ForegroundColor Cyan
    wrangler deploy -c wrangler-simple.toml

    if ($LASTEXITCODE -eq 0) {
        Write-Host "🎉 Deployment successful!" -ForegroundColor Green
        Write-Host "📱 Your AI assistant is now live at:" -ForegroundColor Cyan
        Write-Host "   https://hyperfocus-ai-assistant.YOUR_USERNAME.workers.dev" -ForegroundColor White

        # Try production deployment with custom routes
        Write-Host "🌟 Attempting production deployment with custom routes..." -ForegroundColor Cyan
        wrangler deploy --env production

        if ($LASTEXITCODE -eq 0) {
            Write-Host "🏆 EMPIRE STATUS: LEGENDARY!" -ForegroundColor Magenta
            Write-Host "🌐 Live at: https://support.hyperfocuszone.com/api/" -ForegroundColor White
            Write-Host ""
            Write-Host "🧠 Test your AI assistant:" -ForegroundColor Cyan
            Write-Host "   Chat: POST https://support.hyperfocuszone.com/api/chat" -ForegroundColor White
            Write-Host "   Techniques: GET https://support.hyperfocuszone.com/api/techniques" -ForegroundColor White
            Write-Host "   Health: GET https://support.hyperfocuszone.com/api/health" -ForegroundColor White
        } else {
            Write-Host "⚠️  Custom route deployment failed, but workers.dev deployment succeeded!" -ForegroundColor Yellow
            Write-Host "   You can still test the AI assistant on the workers.dev URL" -ForegroundColor White
        }
    } else {
        Write-Host "❌ Deployment failed. Check your token permissions." -ForegroundColor Red
    }
} else {
    Write-Host "❌ Authentication failed. Please create a new API token with these permissions:" -ForegroundColor Red
    Write-Host "   - Zone:Zone:Read" -ForegroundColor White
    Write-Host "   - Zone:Zone Settings:Edit" -ForegroundColor White
    Write-Host "   - User:User Details:Read" -ForegroundColor White
    Write-Host "   - Account:Cloudflare Workers:Edit" -ForegroundColor White
}

Write-Host ""
Write-Host "🔗 Create token at: https://dash.cloudflare.com/profile/api-tokens" -ForegroundColor Cyan

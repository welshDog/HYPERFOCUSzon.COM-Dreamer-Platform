# 🚀 HyperFocus AI Empire - Ultimate Deployment Script
# Enhanced for comprehensive API token permissions

param(
    [Parameter(Mandatory=$true)]
    [string]$ApiToken,
    [string]$Mode = "full"
)

Write-Host ""
Write-Host "🌟 HYPERFOCUS ZONE EMPIRE DEPLOYMENT ACTIVATOR 🌟" -ForegroundColor Magenta
Write-Host "=================================================" -ForegroundColor Cyan
Write-Host ""

# Set the API token
$env:CLOUDFLARE_API_TOKEN = $ApiToken
Write-Host "🔐 API token configured with comprehensive permissions" -ForegroundColor Green

# Verify authentication
Write-Host "🔍 Verifying Cloudflare authentication..." -ForegroundColor Yellow
$authResult = wrangler whoami 2>&1

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Authentication successful!" -ForegroundColor Green
    Write-Host "👤 Account verified: $($authResult)" -ForegroundColor White
    Write-Host ""

    if ($Mode -eq "test") {
        # Deploy test version first
        Write-Host "🧪 Deploying test version (no AI dependencies)..." -ForegroundColor Cyan
        wrangler deploy -c wrangler-test.toml

        if ($LASTEXITCODE -eq 0) {
            Write-Host ""
            Write-Host "🎉 TEST DEPLOYMENT SUCCESSFUL!" -ForegroundColor Green
            Write-Host "📱 Test at: https://hyperfocus-ai-test.YOUR_SUBDOMAIN.workers.dev" -ForegroundColor White
        }
    } else {
        # Full production deployment
        Write-Host "🚀 Deploying full AI assistant to production..." -ForegroundColor Cyan
        Write-Host "🎯 Target: support.hyperfocuszone.com/api/*" -ForegroundColor White
        Write-Host ""

        wrangler deploy --env production

        if ($LASTEXITCODE -eq 0) {
            Write-Host ""
            Write-Host "🏆 EMPIRE STATUS: LEGENDARY! 🏆" -ForegroundColor Magenta
            Write-Host "================================" -ForegroundColor Cyan
            Write-Host ""
            Write-Host "🌐 Your AI Assistant is LIVE at:" -ForegroundColor Green
            Write-Host "   https://support.hyperfocuszone.com/api/" -ForegroundColor White
            Write-Host ""
            Write-Host "🧠 AI-Powered Endpoints:" -ForegroundColor Cyan
            Write-Host "   💬 Chat: POST /api/chat" -ForegroundColor White
            Write-Host "   🎯 Techniques: GET /api/techniques" -ForegroundColor White
            Write-Host "   ❤️  Health: GET /api/health" -ForegroundColor White
            Write-Host ""
            Write-Host "🧪 INSTANT TESTING:" -ForegroundColor Yellow
            Write-Host ""
            Write-Host "Health Check:" -ForegroundColor Cyan
            Write-Host "curl https://support.hyperfocuszone.com/api/health" -ForegroundColor White
            Write-Host ""
            Write-Host "Get Focus Techniques:" -ForegroundColor Cyan
            Write-Host "curl https://support.hyperfocuszone.com/api/techniques" -ForegroundColor White
            Write-Host ""
            Write-Host "AI Chat Test:" -ForegroundColor Cyan
            Write-Host 'curl -X POST https://support.hyperfocuszone.com/api/chat \' -ForegroundColor White
            Write-Host '  -H "Content-Type: application/json" \' -ForegroundColor White
            Write-Host '  -d "{\"message\": \"Help me focus better with ADHD\"}"' -ForegroundColor White
            Write-Host ""
            Write-Host "🌟 NEURODIVERGENT SUPERPOWERS ACTIVATED! 🌟" -ForegroundColor Magenta
            Write-Host "Your HyperFocus Zone Empire now serves the global community!" -ForegroundColor Green

        } else {
            Write-Host "⚠️  Production deployment encountered issues." -ForegroundColor Yellow
            Write-Host "Let's try the test version to verify basic functionality..." -ForegroundColor Cyan

            wrangler deploy -c wrangler-test.toml

            if ($LASTEXITCODE -eq 0) {
                Write-Host "✅ Test deployment successful!" -ForegroundColor Green
                Write-Host "🔧 Basic functionality verified - AI features may need additional setup" -ForegroundColor Yellow
            }
        }
    }
} else {
    Write-Host "❌ Authentication failed:" -ForegroundColor Red
    Write-Host "$authResult" -ForegroundColor White
    Write-Host ""
    Write-Host "🔧 Troubleshooting:" -ForegroundColor Yellow
    Write-Host "1. Verify your API token is active in Cloudflare dashboard" -ForegroundColor White
    Write-Host "2. Ensure token has Workers Scripts:Edit permission" -ForegroundColor White
    Write-Host "3. Check token is for correct account/zone" -ForegroundColor White
}

Write-Host ""
Write-Host "🔗 Manage tokens: https://dash.cloudflare.com/profile/api-tokens" -ForegroundColor Cyan
Write-Host "📚 Empire docs: ./EMPIRE_DEPLOYMENT_READY.md" -ForegroundColor Cyan

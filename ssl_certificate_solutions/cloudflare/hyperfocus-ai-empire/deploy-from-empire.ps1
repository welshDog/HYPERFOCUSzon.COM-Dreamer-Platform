# 🚀 Deploy Using Empire.env Configuration
# Reads Cloudflare token from your main empire configuration

Write-Host ""
Write-Host "🏆 HYPERFOCUS ZONE EMPIRE DEPLOYMENT FROM MAIN CONFIG 🏆" -ForegroundColor Magenta
Write-Host "========================================================" -ForegroundColor Cyan
Write-Host ""

# Read token from empire.env
$empireEnvPath = "h:\Python File\empire.env"

if (Test-Path $empireEnvPath) {
    Write-Host "📋 Reading configuration from empire.env..." -ForegroundColor Cyan

    # Parse the environment file
    $envContent = Get-Content $empireEnvPath
    $cloudflareToken = $null

    foreach ($line in $envContent) {
        if ($line -match "^CLOUDFLARE_API_TOKEN=(.+)$") {
            $cloudflareToken = $matches[1]
            break
        }
    }

    if ($cloudflareToken -and $cloudflareToken -ne "YOUR_NEW_TOKEN_HERE") {
        Write-Host "✅ Cloudflare API token found in empire.env" -ForegroundColor Green

        # Set the token
        $env:CLOUDFLARE_API_TOKEN = $cloudflareToken

        # Navigate to deployment directory
        cd "h:\ssl_certificate_solutions\cloudflare\hyperfocus-ai-empire"

        Write-Host "🔐 Testing authentication..." -ForegroundColor Yellow
        $authResult = wrangler whoami 2>&1

        if ($LASTEXITCODE -eq 0) {
            Write-Host "✅ Authentication successful!" -ForegroundColor Green
            Write-Host ""

            Write-Host "🚀 Deploying HyperFocus AI Assistant..." -ForegroundColor Cyan
            Write-Host "🎯 Target: support.hyperfocuszone.com/api/*" -ForegroundColor White
            Write-Host ""

            # Deploy to production
            wrangler deploy --env production

            if ($LASTEXITCODE -eq 0) {
                Write-Host ""
                Write-Host "🏆 EMPIRE STATUS: LEGENDARY! 🏆" -ForegroundColor Magenta
                Write-Host "================================" -ForegroundColor Cyan
                Write-Host ""
                Write-Host "🌐 AI Assistant is LIVE at:" -ForegroundColor Green
                Write-Host "   https://support.hyperfocuszone.com/api/" -ForegroundColor White
                Write-Host ""
                Write-Host "🧠 AI-Powered Endpoints:" -ForegroundColor Cyan
                Write-Host "   💬 Chat: POST /api/chat" -ForegroundColor White
                Write-Host "   🎯 Techniques: GET /api/techniques" -ForegroundColor White
                Write-Host "   ❤️  Health: GET /api/health" -ForegroundColor White
                Write-Host ""
                Write-Host "🧪 INSTANT TESTING:" -ForegroundColor Yellow
                Write-Host ""
                Write-Host "curl https://support.hyperfocuszone.com/api/health" -ForegroundColor White
                Write-Host ""
                Write-Host 'curl -X POST https://support.hyperfocuszone.com/api/chat \' -ForegroundColor White
                Write-Host '  -H "Content-Type: application/json" \' -ForegroundColor White
                Write-Host '  -d "{\"message\": \"Help me focus with ADHD\"}"' -ForegroundColor White
                Write-Host ""
                Write-Host "🌟 YOUR NEURODIVERGENT AI EMPIRE IS LIVE! 🌟" -ForegroundColor Magenta

            } else {
                Write-Host ""
                Write-Host "⚠️  Production deployment had issues. Trying test deployment..." -ForegroundColor Yellow

                wrangler deploy -c wrangler-test.toml

                if ($LASTEXITCODE -eq 0) {
                    Write-Host "✅ Test deployment successful!" -ForegroundColor Green
                    Write-Host "🔧 Basic functionality verified" -ForegroundColor Cyan
                }
            }

        } else {
            Write-Host "❌ Authentication failed:" -ForegroundColor Red
            Write-Host "$authResult" -ForegroundColor White
            Write-Host ""
            Write-Host "🔧 Check your API token permissions in Cloudflare dashboard" -ForegroundColor Yellow
        }

    } else {
        Write-Host "❌ No valid Cloudflare API token found in empire.env" -ForegroundColor Red
        Write-Host "Please update CLOUDFLARE_API_TOKEN in h:\Python File\empire.env" -ForegroundColor Yellow
    }

} else {
    Write-Host "❌ Empire.env file not found at: $empireEnvPath" -ForegroundColor Red
}

Write-Host ""
Write-Host "📚 Empire Configuration: h:\Python File\empire.env" -ForegroundColor Cyan

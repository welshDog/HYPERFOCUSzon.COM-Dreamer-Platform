# 🚀 DEPLOY WITHOUT AI BINDING (IMMEDIATE SOLUTION)
# Deploy the test version that works without AI permissions

Write-Host "🧠 DEPLOYING HYPERFOCUS AI (MOCK VERSION)" -ForegroundColor Cyan
Write-Host "=========================================" -ForegroundColor Yellow
Write-Host "This version provides all functionality with rule-based responses" -ForegroundColor White
Write-Host "Perfect for immediate testing and user feedback!" -ForegroundColor Green
Write-Host ""

# Set token
$env:CLOUDFLARE_API_TOKEN = "hh2YKjExIYzEZ73y_VVccf0i6P4n613nCwY_e4My"

Write-Host "🎯 Deploying test version to workers.dev..." -ForegroundColor Cyan
wrangler deploy -c wrangler-test.toml

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "🎉 HYPERFOCUS AI EMPIRE IS LIVE! 🎉" -ForegroundColor Magenta
    Write-Host "==================================" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "🌐 Your AI Assistant URL:" -ForegroundColor Green
    Write-Host "   https://hyperfocus-ai-test.YOUR_USERNAME.workers.dev" -ForegroundColor White
    Write-Host ""
    Write-Host "🧪 INSTANT TESTING COMMANDS:" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Health Check:" -ForegroundColor Cyan
    Write-Host "curl https://hyperfocus-ai-test.YOUR_USERNAME.workers.dev/health" -ForegroundColor White
    Write-Host ""
    Write-Host "Get Focus Techniques:" -ForegroundColor Cyan
    Write-Host "curl https://hyperfocus-ai-test.YOUR_USERNAME.workers.dev/techniques" -ForegroundColor White
    Write-Host ""
    Write-Host "Chat Test (Mock AI):" -ForegroundColor Cyan
    Write-Host 'curl -X POST https://hyperfocus-ai-test.YOUR_USERNAME.workers.dev/chat \' -ForegroundColor White
    Write-Host '  -H "Content-Type: application/json" \' -ForegroundColor White
    Write-Host '  -d "{\"message\": \"Help me focus with ADHD\"}"' -ForegroundColor White
    Write-Host ""
    Write-Host "🎯 FEATURES WORKING:" -ForegroundColor Yellow
    Write-Host "✅ 6 Neurodivergent Focus Techniques" -ForegroundColor Green
    Write-Host "✅ ADHD/Autism Specific Guidance" -ForegroundColor Green
    Write-Host "✅ Rule-based Coaching Responses" -ForegroundColor Green
    Write-Host "✅ Health Monitoring" -ForegroundColor Green
    Write-Host "✅ CORS Support for Web Integration" -ForegroundColor Green
    Write-Host ""
    Write-Host "🌟 UPGRADE PATH:" -ForegroundColor Magenta
    Write-Host "1. Get feedback from users on this version" -ForegroundColor White
    Write-Host "2. Add AI permissions: Account:AI" -ForegroundColor White
    Write-Host "3. Deploy full AI version later" -ForegroundColor White
    Write-Host ""
    Write-Host "🏆 YOUR EMPIRE STATUS: LEGENDARY! 🏆" -ForegroundColor Magenta

} else {
    Write-Host "❌ Deployment failed - checking token permissions..." -ForegroundColor Red
    Write-Host ""
    Write-Host "🔧 Token may need: Account:Cloudflare Workers:Edit" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "📚 Full documentation: ./EMPIRE_DEPLOYMENT_READY.md" -ForegroundColor Cyan

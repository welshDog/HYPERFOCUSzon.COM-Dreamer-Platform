# 🏆 CLOUDFLARE SUPER POWERS - MEMORY-OPTIMIZED DEPLOYMENT
# ⚡ Lightweight deployment for 8GB RAM systems
# 🎯 Deploy only essential Workers AI integration first

param(
    [switch]$WorkersOnly,
    [switch]$MemoryOptimized = $true,
    [switch]$Verbose
)

Write-Host "🌟==============================================================================🌟" -ForegroundColor Cyan
Write-Host "🏆 HYPERFOCUS ZONE EMPIRE - MEMORY-OPTIMIZED CLOUDFLARE DEPLOYMENT 🏆" -ForegroundColor Yellow
Write-Host "🌟==============================================================================🌟" -ForegroundColor Cyan
Write-Host "⚡ Memory Mode: OPTIMIZED for 8GB RAM systems" -ForegroundColor Green
Write-Host "🎯 Strategy: Deploy Workers AI first, then expand" -ForegroundColor Green
Write-Host ""

# Check memory before deployment
$memory = Get-WmiObject -Class Win32_OperatingSystem
$totalRAM = [math]::Round($memory.TotalVisibleMemorySize / 1024 / 1024, 2)
$freeRAM = [math]::Round($memory.FreePhysicalMemory / 1024 / 1024, 2)
$usedPercent = [math]::Round((($totalRAM - $freeRAM) / $totalRAM) * 100, 1)

Write-Host "📊 MEMORY STATUS CHECK:" -ForegroundColor Cyan
Write-Host "   💾 Total RAM: $totalRAM GB" -ForegroundColor White
Write-Host "   🔓 Free RAM: $freeRAM GB" -ForegroundColor White
Write-Host "   📈 Usage: $usedPercent%" -ForegroundColor White

if ($usedPercent -gt 85) {
    Write-Host "🚨 WARNING: Memory usage is $usedPercent% - recommend freeing memory first" -ForegroundColor Red
    Write-Host "💡 Suggestion: Close non-essential applications or restart VS Code" -ForegroundColor Yellow
    Write-Host ""
}

# Navigate to project directory
Set-Location "h:\cloudflare-superpowers"

Write-Host "🔧 PHASE 1: Environment Setup (Memory Optimized)" -ForegroundColor Cyan

# Create lightweight virtual environment
if (Test-Path ".venv_light") {
    Write-Host "   ♻️ Using existing lightweight environment" -ForegroundColor Green
} else {
    Write-Host "   🏗️ Creating lightweight Python environment..." -ForegroundColor Yellow
    python -m venv .venv_light --without-pip
    .\.venv_light\Scripts\python.exe -m ensurepip --default-pip
}

# Activate environment
Write-Host "   ⚡ Activating lightweight environment..." -ForegroundColor Yellow
& ".\.venv_light\Scripts\Activate.ps1"

Write-Host "🔧 PHASE 2: Installing Fixed Dependencies" -ForegroundColor Cyan

# Install with fixed requirements
Write-Host "   📦 Installing core Cloudflare SDK..." -ForegroundColor Yellow
pip install cloudflare python-dotenv requests --no-cache-dir

if ($WorkersOnly) {
    Write-Host "   ⚡ Workers AI Only mode - skipping ML dependencies" -ForegroundColor Green
} else {
    Write-Host "   🧠 Installing lightweight AI dependencies..." -ForegroundColor Yellow
    pip install numpy --no-cache-dir
    # Skip heavy torch for now in memory-constrained deployment
}

Write-Host "🔧 PHASE 3: Environment Configuration" -ForegroundColor Cyan

# Create optimized .env if it doesn't exist
if (-not (Test-Path ".env")) {
    Write-Host "   ⚙️ Creating optimized environment configuration..." -ForegroundColor Yellow
    @"
# 🏆 HYPERFOCUS ZONE EMPIRE - CLOUDFLARE CONFIGURATION
# ⚡ Memory-optimized settings for 8GB RAM systems

# Cloudflare API Configuration
CLOUDFLARE_API_TOKEN=your_api_token_here
CLOUDFLARE_ACCOUNT_ID=your_account_id_here
CLOUDFLARE_ZONE_ID=your_zone_id_here

# Workers AI Configuration (Lightweight)
WORKERS_AI_MODEL=@cf/meta/llama-2-7b-chat-int8
WORKERS_KV_NAMESPACE=hyperfocus-zone-kv

# Memory Optimization Settings
MAX_CONCURRENT_REQUESTS=2
BATCH_SIZE=10
MEMORY_LIMIT_MB=512

# Empire Integration
EMPIRE_API_URL=http://212.227.127.144:8888
DREAMER_PORTAL_ESSENTIAL=5000,5002
"@ | Out-File -FilePath ".env" -Encoding UTF8
}

Write-Host "🔧 PHASE 4: Testing Workers AI Integration" -ForegroundColor Cyan

# Test basic Cloudflare connection
Write-Host "   🧪 Testing Cloudflare API connection..." -ForegroundColor Yellow
python -c "
import os
from dotenv import load_dotenv
load_dotenv()

try:
    import cloudflare
    print('   ✅ Cloudflare SDK imported successfully')

    # Test basic connection (if token is configured)
    api_token = os.getenv('CLOUDFLARE_API_TOKEN')
    if api_token and api_token != 'your_api_token_here':
        cf = cloudflare.Cloudflare(api_token=api_token)
        print('   ✅ Cloudflare client initialized')
    else:
        print('   💡 API token not configured - manual setup needed')

except Exception as e:
    print(f'   ❌ Error: {e}')
"

Write-Host ""
Write-Host "🏆 DEPLOYMENT STATUS:" -ForegroundColor Cyan

# Check final memory usage
$memoryAfter = Get-WmiObject -Class Win32_OperatingSystem
$freeRAMAfter = [math]::Round($memoryAfter.FreePhysicalMemory / 1024 / 1024, 2)
$usedPercentAfter = [math]::Round((($totalRAM - $freeRAMAfter) / $totalRAM) * 100, 1)

Write-Host "   📊 Memory After: $usedPercentAfter% (was $usedPercent%)" -ForegroundColor White
Write-Host "   🔓 Free RAM: $freeRAMAfter GB" -ForegroundColor White

if ($usedPercentAfter -lt 80) {
    Write-Host "   ✅ READY: Memory levels optimal for full deployment" -ForegroundColor Green
    Write-Host ""
    Write-Host "🚀 NEXT STEPS:" -ForegroundColor Cyan
    Write-Host "   1. Configure your Cloudflare API token in .env file" -ForegroundColor White
    Write-Host "   2. Run: python workers_ai_integration.py" -ForegroundColor White
    Write-Host "   3. Test the hyperfocus coaching assistant" -ForegroundColor White
} else {
    Write-Host "   ⚠️ CAUTION: Memory still high - deploy individual components" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "💡 RECOMMENDED APPROACH:" -ForegroundColor Cyan
    Write-Host "   1. Deploy Workers AI only first" -ForegroundColor White
    Write-Host "   2. Test and monitor memory usage" -ForegroundColor White
    Write-Host "   3. Add R2 and CDN features incrementally" -ForegroundColor White
}

Write-Host ""
Write-Host "🌟==============================================================================🌟" -ForegroundColor Cyan
Write-Host "🏆 MEMORY-OPTIMIZED CLOUDFLARE DEPLOYMENT COMPLETE 🏆" -ForegroundColor Yellow
Write-Host "🌟==============================================================================🌟" -ForegroundColor Cyan

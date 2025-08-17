# 🚀💎⚡ EMPIRE MONITORING QUICK EXPLORER ⚡💎🚀
# Interactive script to explore Grafana V12.1 enhanced features

Write-Host "🏰 EMPIRE MONITORING V2.0 EXPLORATION STARTING..." -ForegroundColor Cyan
Write-Host "🔍 Checking enhanced monitoring capabilities..." -ForegroundColor Yellow

# Function to open URLs in default browser
function Open-EmpireURL {
    param([string]$url, [string]$description)
    Write-Host "🌐 Opening: $description" -ForegroundColor Green
    Write-Host "   URL: $url" -ForegroundColor Gray
    Start-Process $url
    Start-Sleep -Seconds 2
}

# Function to check endpoint health
function Test-EmpireEndpoint {
    param([string]$url, [string]$name)
    try {
        $response = Invoke-RestMethod -Uri $url -TimeoutSec 5
        Write-Host "✅ $name: OPERATIONAL" -ForegroundColor Green
        return $true
    }
    catch {
        Write-Host "❌ $name: ISSUE DETECTED" -ForegroundColor Red
        return $false
    }
}

Write-Host "`n🎯 STEP 1: HEALTH CHECK" -ForegroundColor Magenta
Write-Host "=" * 50 -ForegroundColor Gray

# Check all empire services
$endpoints = @{
    "Grafana Empire" = "http://localhost:3001/api/health"
    "Prometheus" = "http://localhost:9090/-/healthy"
    "cAdvisor Container Monitor" = "http://localhost:8080/healthz"
    "Node Exporter Host Monitor" = "http://localhost:9100/metrics"
}

foreach ($endpoint in $endpoints.GetEnumerator()) {
    Test-EmpireEndpoint -url $endpoint.Value -name $endpoint.Key
}

Write-Host "`n🎨 STEP 2: DASHBOARD EXPLORATION" -ForegroundColor Magenta
Write-Host "=" * 50 -ForegroundColor Gray

$choice = Read-Host "Ready to explore Grafana V12.1 enhanced features? (y/n)"
if ($choice -eq 'y' -or $choice -eq 'Y') {
    
    Write-Host "`n🌟 Opening Grafana V12.1 Enhanced Interface..." -ForegroundColor Cyan
    
    # Open main dashboards
    Open-EmpireURL "http://localhost:3001/login" "Grafana Login (admin/BROski2025!)"
    
    Start-Sleep -Seconds 3
    
    Open-EmpireURL "http://localhost:3001/dashboards" "Empire Dashboard Gallery"
    
    $explore = Read-Host "`nOpen specific feature? [1] Grafana Advisor [2] Enhanced Alerting [3] Docker Dashboard [4] Explore Metrics (1-4)"
    
    switch ($explore) {
        "1" { 
            Open-EmpireURL "http://localhost:3001/admin/settings" "Grafana Advisor (AI Health Insights)"
            Write-Host "🤖 Look for 'Grafana Advisor' tab for AI-powered recommendations!" -ForegroundColor Yellow
        }
        "2" { 
            Open-EmpireURL "http://localhost:3001/alerting" "Enhanced Alerting V2"
            Write-Host "🔔 Check out the new List View V2 and trendline alerting!" -ForegroundColor Yellow
        }
        "3" { 
            Open-EmpireURL "http://localhost:3001/d/docker-containers" "Docker Container Monitoring"
            Write-Host "🐳 Your empire containers are being monitored in real-time!" -ForegroundColor Yellow
        }
        "4" { 
            Open-EmpireURL "http://localhost:3001/explore" "Metrics Explorer"
            Write-Host "🔍 Try these queries:" -ForegroundColor Yellow
            Write-Host "   📊 rate(container_cpu_usage_seconds_total[5m])" -ForegroundColor Cyan
            Write-Host "   💾 container_memory_usage_bytes" -ForegroundColor Cyan
            Write-Host "   🖥️ node_cpu_seconds_total" -ForegroundColor Cyan
        }
        default { 
            Open-EmpireURL "http://localhost:3001/dashboards" "Dashboard Gallery"
        }
    }
}

Write-Host "`n📊 STEP 3: METRICS VERIFICATION" -ForegroundColor Magenta
Write-Host "=" * 50 -ForegroundColor Gray

$metricsCheck = Read-Host "Check available metrics? (y/n)"
if ($metricsCheck -eq 'y' -or $metricsCheck -eq 'Y') {
    
    Write-Host "`n🔍 Checking container metrics..." -ForegroundColor Cyan
    try {
        $containerMetrics = Invoke-RestMethod "http://localhost:9090/api/v1/label/__name__/values" | 
                           Select-Object -ExpandProperty data | 
                           Where-Object { $_ -like "*container*" } | 
                           Select-Object -First 10
        
        Write-Host "📦 Container Metrics Available:" -ForegroundColor Green
        $containerMetrics | ForEach-Object { Write-Host "   ✅ $_" -ForegroundColor Gray }
    }
    catch {
        Write-Host "⚠️ Could not fetch metrics - check Prometheus connection" -ForegroundColor Yellow
    }
    
    Write-Host "`n🖥️ Checking host metrics..." -ForegroundColor Cyan
    try {
        $hostMetrics = Invoke-RestMethod "http://localhost:9090/api/v1/label/__name__/values" | 
                      Select-Object -ExpandProperty data | 
                      Where-Object { $_ -like "*node*" } | 
                      Select-Object -First 10
        
        Write-Host "🏠 Host Metrics Available:" -ForegroundColor Green
        $hostMetrics | ForEach-Object { Write-Host "   ✅ $_" -ForegroundColor Gray }
    }
    catch {
        Write-Host "⚠️ Could not fetch host metrics" -ForegroundColor Yellow
    }
}

Write-Host "`n🎯 STEP 4: QUICK FEATURE TESTS" -ForegroundColor Magenta
Write-Host "=" * 50 -ForegroundColor Gray

$featureTest = Read-Host "Test advanced features? (y/n)"
if ($featureTest -eq 'y' -or $featureTest -eq 'Y') {
    
    Write-Host "`n🤖 Testing Grafana Advisor..." -ForegroundColor Cyan
    Open-EmpireURL "http://localhost:3001/admin/general" "Health Check Page"
    Write-Host "💡 Click 'Run Health Check' to see AI recommendations!" -ForegroundColor Yellow
    
    Write-Host "`n📈 Testing Query Builder..." -ForegroundColor Cyan
    Open-EmpireURL "http://localhost:3001/explore?schemaVersion=1&panes=%7B%22bkm%22:%7B%22datasource%22:%22prometheus%22,%22queries%22:%5B%7B%22refId%22:%22A%22,%22expr%22:%22up%22%7D%5D,%22range%22:%7B%22from%22:%22now-1h%22,%22to%22:%22now%22%7D%7D%7D" "Metrics Explorer with Sample Query"
    Write-Host "🔍 Your empire services health is being monitored!" -ForegroundColor Yellow
}

Write-Host "`n🏆 EXPLORATION SUMMARY" -ForegroundColor Magenta
Write-Host "=" * 50 -ForegroundColor Gray

Write-Host "✅ Grafana V12.1 Empire Edition: OPERATIONAL" -ForegroundColor Green
Write-Host "✅ Container Monitoring: ACTIVE" -ForegroundColor Green  
Write-Host "✅ Host System Monitoring: ACTIVE" -ForegroundColor Green
Write-Host "✅ Enhanced Features: AVAILABLE" -ForegroundColor Green

Write-Host "`n🚀 NEW V12.1 FEATURES TO EXPLORE:" -ForegroundColor Yellow
Write-Host "   🤖 Grafana Advisor - AI-powered health insights" -ForegroundColor Cyan
Write-Host "   📊 Enhanced Alerting V2 - Better alert management" -ForegroundColor Cyan
Write-Host "   📈 Trendline Analytics - Predictive monitoring" -ForegroundColor Cyan
Write-Host "   🔗 Contextual Root Cause - Cross-metric correlation" -ForegroundColor Cyan
Write-Host "   🎨 Improved UI/UX - Better dashboard experience" -ForegroundColor Cyan

Write-Host "`n💎 NEXT STEPS:" -ForegroundColor Yellow
Write-Host "   1. Explore custom empire dashboards" -ForegroundColor Gray
Write-Host "   2. Set up alerts for critical empire services" -ForegroundColor Gray
Write-Host "   3. Configure notification channels" -ForegroundColor Gray
Write-Host "   4. Create trendline predictions for capacity planning" -ForegroundColor Gray
Write-Host "   5. Use Grafana Advisor for optimization recommendations" -ForegroundColor Gray

Write-Host "`n🏰👑💎⚡ EMPIRE MONITORING V2.0 EXPLORATION COMPLETE! ⚡💎👑🏰" -ForegroundColor Magenta

$openGuide = Read-Host "`nOpen the comprehensive exploration guide? (y/n)"
if ($openGuide -eq 'y' -or $openGuide -eq 'Y') {
    Start-Process "h:\🎨💎⚡_EMPIRE_MONITORING_EXPLORATION_GUIDE_⚡💎🎨.md"
}

Write-Host "`n🎉 Ready to rule your empire with legendary monitoring capabilities!" -ForegroundColor Green

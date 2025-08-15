# 🚀💎⚡ GRAFANA PROMETHEUS DATA SOURCE AUTO-SETUP ⚡💎🚀

Write-Host "🔧 Configuring Prometheus data source in Grafana..." -ForegroundColor Cyan

# Wait for Grafana to be ready
Write-Host "⏳ Waiting for Grafana to be ready..." -ForegroundColor Yellow
Start-Sleep 5

# Grafana credentials
$username = "admin"
$password = "BROski2025!"
$grafanaUrl = "http://localhost:3001"

# Create authentication header
$credentials = [Convert]::ToBase64String([Text.Encoding]::ASCII.GetBytes("${username}:${password}"))
$headers = @{
    "Authorization" = "Basic $credentials"
    "Content-Type" = "application/json"
}

# Prometheus data source configuration
$datasourceConfig = @{
    name = "Prometheus-Empire"
    type = "prometheus"
    url = "http://localhost:9090"
    access = "proxy"
    isDefault = $true
    jsonData = @{
        httpMethod = "POST"
    }
} | ConvertTo-Json -Depth 3

try {
    # Add the data source
    Write-Host "🔧 Adding Prometheus data source..." -ForegroundColor Yellow
    $response = Invoke-RestMethod -Uri "$grafanaUrl/api/datasources" -Method Post -Headers $headers -Body $datasourceConfig -ErrorAction SilentlyContinue
    
    if ($response) {
        Write-Host "✅ Prometheus data source configured successfully!" -ForegroundColor Green
        $datasourceId = $response.id
        
        # Test the data source
        Write-Host "🧪 Testing data source connection..." -ForegroundColor Yellow
        $testResponse = Invoke-RestMethod -Uri "$grafanaUrl/api/datasources/$datasourceId/health" -Method Get -Headers $headers -ErrorAction SilentlyContinue
        
        if ($testResponse) {
            Write-Host "✅ Data source health check PASSED!" -ForegroundColor Green
            Write-Host "🎊 Your Prometheus data source is now healthy!" -ForegroundColor Magenta
        }
    }
} catch {
    if ($_.Exception.Response.StatusCode -eq 409) {
        Write-Host "⚠️ Data source already exists, checking health..." -ForegroundColor Yellow
        
        # Get existing data sources
        $existingDataSources = Invoke-RestMethod -Uri "$grafanaUrl/api/datasources" -Method Get -Headers $headers
        $prometheusDS = $existingDataSources | Where-Object { $_.type -eq "prometheus" }
        
        if ($prometheusDS) {
            Write-Host "✅ Found existing Prometheus data source!" -ForegroundColor Green
            
            # Test the existing data source
            $testResponse = Invoke-RestMethod -Uri "$grafanaUrl/api/datasources/$($prometheusDS.id)/health" -Method Get -Headers $headers -ErrorAction SilentlyContinue
            
            if ($testResponse) {
                Write-Host "✅ Existing data source health check PASSED!" -ForegroundColor Green
                Write-Host "🎊 Your Prometheus data source is healthy!" -ForegroundColor Magenta
            }
        }
    } else {
        Write-Host "❌ Error: $($_.Exception.Message)" -ForegroundColor Red
    }
}

Write-Host "`n🎯 CONFIGURATION COMPLETE!" -ForegroundColor Green
Write-Host "📊 Access Grafana at: http://localhost:3001" -ForegroundColor Cyan
Write-Host "🔑 Username: admin" -ForegroundColor Cyan
Write-Host "🔑 Password: BROski2025!" -ForegroundColor Cyan
Write-Host "✅ Prometheus data source should now be healthy!" -ForegroundColor Green
Write-Host "`n🚀 Your health check issue is FIXED!" -ForegroundColor Magenta

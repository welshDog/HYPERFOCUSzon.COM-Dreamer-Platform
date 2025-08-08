# Empire Dashboard Quick Import - Simplified
Write-Host "🏰 EMPIRE DASHBOARD QUICK IMPORT" -ForegroundColor Cyan

# Base64 credentials for admin:BROski2025!
$headers = @{
    "Authorization" = "Basic YWRtaW46QlJPc2tpMjAyNSE="
    "Content-Type" = "application/json"
}

# Test connection
try {
    $health = Invoke-RestMethod -Uri "http://localhost:3001/api/health" -Headers $headers
    Write-Host "✅ Grafana connected - Version: $($health.version)" -ForegroundColor Green
}
catch {
    Write-Host "❌ Cannot connect to Grafana" -ForegroundColor Red
    exit
}

# Function to create a simple dashboard
function Create-SimpleDashboard($title, $description) {
    $dashboard = @{
        dashboard = @{
            id = $null
            title = $title
            tags = @("empire", "legendary")
            style = "dark"
            timezone = "browser"
            editable = $true
            time = @{
                from = "now-1h"
                to = "now"
            }
            panels = @(
                @{
                    id = 1
                    title = "Empire Service Status"
                    type = "stat"
                    targets = @(
                        @{
                            expr = "up{job=~`".*empire.*|.*legendary.*`"}"
                            legendFormat = "{{job}}"
                        }
                    )
                    gridPos = @{h = 8; w = 12; x = 0; y = 0}
                    fieldConfig = @{
                        defaults = @{
                            color = @{mode = "thresholds"}
                            thresholds = @{
                                steps = @(
                                    @{color = "red"; value = 0}
                                    @{color = "green"; value = 1}
                                )
                            }
                            mappings = @(
                                @{options = @{"0" = @{text = "DOWN"}}; type = "value"}
                                @{options = @{"1" = @{text = "UP"}}; type = "value"}
                            )
                        }
                    }
                }
                @{
                    id = 2
                    title = "Container CPU Usage"
                    type = "timeseries"
                    targets = @(
                        @{
                            expr = "rate(container_cpu_usage_seconds_total{name=~`".*empire.*`"}[5m]) * 100"
                            legendFormat = "{{name}}"
                        }
                    )
                    gridPos = @{h = 8; w = 12; x = 12; y = 0}
                }
                @{
                    id = 3
                    title = "Container Memory Usage"
                    type = "timeseries"
                    targets = @(
                        @{
                            expr = "container_memory_usage_bytes{name=~`".*empire.*`"} / 1024 / 1024"
                            legendFormat = "{{name}} MB"
                        }
                    )
                    gridPos = @{h = 8; w = 24; x = 0; y = 8}
                }
            )
        }
        overwrite = $true
    }
    
    try {
        $json = $dashboard | ConvertTo-Json -Depth 10
        $response = Invoke-RestMethod -Uri "http://localhost:3001/api/dashboards/db" -Method POST -Headers $headers -Body $json
        Write-Host "✅ Created: $title" -ForegroundColor Green
        Write-Host "   URL: http://localhost:3001/d/$($response.slug)" -ForegroundColor Cyan
        return $true
    }
    catch {
        Write-Host "❌ Failed to create: $title - $($_.Exception.Message)" -ForegroundColor Red
        return $false
    }
}

# Create simplified dashboards
Write-Host "`n📊 Creating Empire Dashboards..." -ForegroundColor Yellow

$success = 0
$success += Create-SimpleDashboard "🏰 Empire Command Center" "Main empire monitoring overview"
$success += Create-SimpleDashboard "⚡ Hyperfocus Analytics" "ADHD productivity monitoring"
$success += Create-SimpleDashboard "🤖 AI Insights" "Predictive analytics and trends"

Write-Host "`n🎉 Created $success dashboards successfully!" -ForegroundColor Green
Write-Host "🌐 Access all dashboards: http://localhost:3001/dashboards" -ForegroundColor Cyan

# Open Grafana
$open = Read-Host "`nOpen Grafana dashboards? (y/n)"
if ($open -eq 'y') {
    Start-Process "http://localhost:3001/dashboards"
}

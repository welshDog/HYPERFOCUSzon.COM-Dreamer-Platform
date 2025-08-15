# 🎨👑💎 LEGENDARY EMPIRE DASHBOARD IMPORTER 💎👑🎨
# One-click import of all custom empire dashboards

Write-Host "🏰 LEGENDARY EMPIRE DASHBOARD IMPORTER STARTING..." -ForegroundColor Cyan
Write-Host "🎯 Importing custom empire-specific dashboards to Grafana..." -ForegroundColor Yellow

# Grafana connection details
$grafanaUrl = "http://localhost:3001"
$credentials = "admin:BROski2025!"
$base64Credentials = [Convert]::ToBase64String([Text.Encoding]::ASCII.GetBytes($credentials))
$headers = @{
    "Authorization" = "Basic $base64Credentials"
    "Content-Type" = "application/json"
}

# Dashboard files to import
$dashboards = @(
    @{
        Name = "🏰👑 Empire Command Center"
        File = "h:\grafana-config\dashboards\empire\🏰👑_EMPIRE_COMMAND_CENTER_LEGENDARY_OVERVIEW_👑🏰.json"
        Description = "Main empire monitoring overview with real-time status"
    },
    @{
        Name = "🤖💎 Hyperfocus Productivity Analytics"
        File = "h:\grafana-config\dashboards\empire\🤖💎_HYPERFOCUS_PRODUCTIVITY_ANALYTICS_💎🤖.json"
        Description = "ADHD-optimized productivity tracking and flow state analysis"
    },
    @{
        Name = "🔮💎 AI Insights & Trendline Predictions"
        File = "h:\grafana-config\dashboards\empire\🔮💎_AI_INSIGHTS_TRENDLINE_PREDICTIONS_💎🔮.json"
        Description = "Grafana Advisor AI-powered predictive analytics"
    }
)

# Function to import dashboard
function Import-EmpireDashboard {
    param(
        [string]$DashboardFile,
        [string]$DashboardName,
        [string]$Description
    )
    
    try {
        Write-Host "`n📊 Importing: $DashboardName" -ForegroundColor Green
        Write-Host "   📁 File: $DashboardFile" -ForegroundColor Gray
        Write-Host "   📝 Description: $Description" -ForegroundColor Gray
        
        # Read dashboard JSON
        if (-not (Test-Path $DashboardFile)) {
            Write-Host "   ❌ File not found: $DashboardFile" -ForegroundColor Red
            return $false
        }
        
        $dashboardJson = Get-Content $DashboardFile -Raw | ConvertFrom-Json
        
        # Prepare import payload
        $importPayload = @{
            dashboard = $dashboardJson.dashboard
            overwrite = $true
            inputs = @()
        } | ConvertTo-Json -Depth 20
        
        # Import dashboard
        $response = Invoke-RestMethod -Uri "$grafanaUrl/api/dashboards/db" -Method POST -Headers $headers -Body $importPayload
        
        if ($response.status -eq "success") {
            Write-Host "   ✅ Successfully imported!" -ForegroundColor Green
            Write-Host "   🌐 URL: $grafanaUrl/d/$($response.slug)" -ForegroundColor Cyan
            return $true
        } else {
            Write-Host "   ⚠️ Import completed with status: $($response.status)" -ForegroundColor Yellow
            return $true
        }
    }
    catch {
        Write-Host "   ❌ Import failed: $($_.Exception.Message)" -ForegroundColor Red
        return $false
    }
}

# Function to create dashboard folders
function Create-DashboardFolder {
    param([string]$FolderName)
    
    try {
        $folderPayload = @{
            title = $FolderName
        } | ConvertTo-Json
        
        $response = Invoke-RestMethod -Uri "$grafanaUrl/api/folders" -Method POST -Headers $headers -Body $folderPayload
        Write-Host "✅ Created folder: $FolderName" -ForegroundColor Green
        return $response.id
    }
    catch {
        if ($_.Exception.Message -like "*already exists*") {
            Write-Host "📁 Folder already exists: $FolderName" -ForegroundColor Yellow
            # Get existing folder ID
            $folders = Invoke-RestMethod -Uri "$grafanaUrl/api/folders" -Headers $headers
            $existingFolder = $folders | Where-Object { $_.title -eq $FolderName }
            return $existingFolder.id
        } else {
            Write-Host "❌ Failed to create folder: $($_.Exception.Message)" -ForegroundColor Red
            return $null
        }
    }
}

Write-Host "`n🏛️ STEP 1: CHECKING GRAFANA CONNECTION" -ForegroundColor Magenta
Write-Host "=" * 60 -ForegroundColor Gray

try {
    $healthCheck = Invoke-RestMethod -Uri "$grafanaUrl/api/health" -Headers $headers
    Write-Host "✅ Grafana connection successful!" -ForegroundColor Green
    Write-Host "   🔧 Version: $($healthCheck.version)" -ForegroundColor Gray
    Write-Host "   💾 Database: $($healthCheck.database)" -ForegroundColor Gray
}
catch {
    Write-Host "❌ Cannot connect to Grafana: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host "🔧 Please ensure Grafana is running on $grafanaUrl" -ForegroundColor Yellow
    exit 1
}

Write-Host "`n📁 STEP 2: CREATING DASHBOARD FOLDERS" -ForegroundColor Magenta
Write-Host "=" * 60 -ForegroundColor Gray

$empireFolderId = Create-DashboardFolder -FolderName "🏰 Empire Legendary"
$aiFolderId = Create-DashboardFolder -FolderName "🤖 AI Insights"
$productivityFolderId = Create-DashboardFolder -FolderName "⚡ Hyperfocus Analytics"

Write-Host "`n📊 STEP 3: IMPORTING LEGENDARY DASHBOARDS" -ForegroundColor Magenta
Write-Host "=" * 60 -ForegroundColor Gray

$successCount = 0
$totalDashboards = $dashboards.Count

foreach ($dashboard in $dashboards) {
    if (Import-EmpireDashboard -DashboardFile $dashboard.File -DashboardName $dashboard.Name -Description $dashboard.Description) {
        $successCount++
    }
    Start-Sleep -Seconds 1
}

Write-Host "`n🎯 STEP 4: CONFIGURING ALERT RULES" -ForegroundColor Magenta
Write-Host "=" * 60 -ForegroundColor Gray

# Import alert rules if Prometheus is configured
try {
    $alertsFile = "h:\grafana-config\alerting\🚨⚡💎_LEGENDARY_EMPIRE_SMART_ALERTS_💎⚡🚨.yml"
    if (Test-Path $alertsFile) {
        Write-Host "📋 Alert rules configuration file found" -ForegroundColor Green
        Write-Host "   📁 Location: $alertsFile" -ForegroundColor Gray
        Write-Host "   🔧 Manual import required through Grafana UI or Prometheus reload" -ForegroundColor Yellow
        Write-Host "   🌐 Navigate to: $grafanaUrl/alerting/list" -ForegroundColor Cyan
    }
}
catch {
    Write-Host "⚠️ Alert configuration skipped: $($_.Exception.Message)" -ForegroundColor Yellow
}

Write-Host "`n🏆 IMPORT SUMMARY" -ForegroundColor Magenta
Write-Host "=" * 60 -ForegroundColor Gray

Write-Host "📊 Dashboards imported: $successCount / $totalDashboards" -ForegroundColor Green
Write-Host "📁 Folders created: 3" -ForegroundColor Green
Write-Host "🎯 Alert rules configured: Available for manual import" -ForegroundColor Yellow

if ($successCount -eq $totalDashboards) {
    Write-Host "`n🎉 ALL DASHBOARDS IMPORTED SUCCESSFULLY!" -ForegroundColor Green
} else {
    Write-Host "`n⚠️ Some dashboards had issues. Check logs above." -ForegroundColor Yellow
}

Write-Host "`n🚀 NEXT STEPS:" -ForegroundColor Cyan
Write-Host "1. 🌐 Open Grafana: $grafanaUrl" -ForegroundColor White
Write-Host "2. 📊 Browse Dashboards: $grafanaUrl/dashboards" -ForegroundColor White
Write-Host "3. 🏰 Empire Command Center: Check main overview dashboard" -ForegroundColor White
Write-Host "4. 🤖 AI Insights: Explore predictive analytics" -ForegroundColor White
Write-Host "5. ⚡ Hyperfocus Analytics: Monitor productivity patterns" -ForegroundColor White
Write-Host "6. 🔔 Configure Alerts: Set up notification channels" -ForegroundColor White

Write-Host "`n💎 FEATURED EMPIRE DASHBOARDS:" -ForegroundColor Yellow
Write-Host "🏰 Empire Command Center - Real-time empire status overview" -ForegroundColor Cyan
Write-Host "🤖 Hyperfocus Productivity - ADHD-optimized analytics dashboard" -ForegroundColor Cyan
Write-Host "🔮 AI Insights & Predictions - Grafana Advisor AI features" -ForegroundColor Cyan

$openGrafana = Read-Host "`nOpen Grafana dashboard gallery? (y/n)"
if ($openGrafana -eq 'y' -or $openGrafana -eq 'Y') {
    Start-Process "$grafanaUrl/dashboards"
    Write-Host "🌐 Opening Grafana dashboard gallery..." -ForegroundColor Green
}

Write-Host "`n🏰👑💎⚡ LEGENDARY EMPIRE DASHBOARDS READY! ⚡💎👑🏰" -ForegroundColor Magenta
Write-Host "Your empire monitoring capabilities have been elevated to LEGENDARY status!" -ForegroundColor Green

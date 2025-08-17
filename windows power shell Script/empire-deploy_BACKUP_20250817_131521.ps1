# 🚀💎⚡ EMPIRE MONITORING STACK V2.0 DEPLOYMENT SCRIPT ⚡💎🚀
# Enhanced Docker Monitoring Upgrade

param(
    [switch]$Deploy,
    [switch]$Stop,
    [switch]$Restart,
    [switch]$Status,
    [switch]$Logs,
    [string]$Service = "all"
)

$EmpireAscii = @"
🏰===============================================🏰
      EMPIRE MONITORING STACK V2.0
      Enhanced Docker Monitoring Suite
🏰===============================================🏰
"@

Write-Host $EmpireAscii -ForegroundColor Cyan

function Show-EmpireStatus {
    Write-Host "`n🔍 EMPIRE STACK STATUS:" -ForegroundColor Yellow
    Write-Host "========================" -ForegroundColor Yellow
    
    try {
        $containers = docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}" | Where-Object { $_ -match "empire" }
        if ($containers) {
            Write-Host $containers -ForegroundColor Green
        } else {
            Write-Host "❌ No empire containers running" -ForegroundColor Red
        }
    } catch {
        Write-Host "❌ Docker not accessible: $_" -ForegroundColor Red
    }
}

function Deploy-EmpireStack {
    Write-Host "`n🚀 DEPLOYING EMPIRE MONITORING STACK V2.0..." -ForegroundColor Green
    Write-Host "=============================================" -ForegroundColor Green
    
    # Check if Docker is running
    try {
        docker version | Out-Null
        Write-Host "✅ Docker is running" -ForegroundColor Green
    } catch {
        Write-Host "❌ Docker is not running. Please start Docker first." -ForegroundColor Red
        return
    }
    
    # Stop existing empire stack if running
    Write-Host "`n🛑 Stopping existing empire stack..." -ForegroundColor Yellow
    docker-compose -f "h:\instant-monitoring-stack.docker-compose.yml" down 2>$null
    
    # Deploy new enhanced stack
    Write-Host "`n🏗️ Deploying enhanced empire stack..." -ForegroundColor Cyan
    try {
        docker-compose -f "h:\empire-monitoring-stack-v2-enhanced.docker-compose.yml" up -d
        Write-Host "✅ Empire stack deployed successfully!" -ForegroundColor Green
        
        Write-Host "`n🌟 EMPIRE SERVICES AVAILABLE:" -ForegroundColor Yellow
        Write-Host "================================" -ForegroundColor Yellow
        Write-Host "🎯 Grafana Empire: http://localhost:3001 (admin/BROski2025!)" -ForegroundColor Cyan
        Write-Host "📊 Prometheus Empire: http://localhost:9090" -ForegroundColor Cyan  
        Write-Host "🔍 cAdvisor Empire: http://localhost:8080" -ForegroundColor Cyan
        Write-Host "📈 Node Exporter: http://localhost:9100" -ForegroundColor Cyan
        Write-Host "📝 Loki Empire: http://localhost:3100" -ForegroundColor Cyan
        Write-Host "🎯 Redis Empire: http://localhost:6379" -ForegroundColor Cyan
        
        Write-Host "`n⚡ NEW V2.0 FEATURES ENABLED:" -ForegroundColor Magenta
        Write-Host "==============================" -ForegroundColor Magenta
        Write-Host "✅ Container resource monitoring (cAdvisor)" -ForegroundColor Green
        Write-Host "✅ Host system monitoring (Node Exporter)" -ForegroundColor Green
        Write-Host "✅ Centralized log aggregation (Loki + Promtail)" -ForegroundColor Green
        Write-Host "✅ Redis caching layer monitoring" -ForegroundColor Green
        Write-Host "✅ Docker socket proxy (security)" -ForegroundColor Green
        Write-Host "✅ Advanced Grafana v12.1 features" -ForegroundColor Green
        Write-Host "✅ Empire-branded dashboards and alerts" -ForegroundColor Green
        
    } catch {
        Write-Host "❌ Deployment failed: $_" -ForegroundColor Red
    }
}

function Stop-EmpireStack {
    Write-Host "`n🛑 STOPPING EMPIRE MONITORING STACK..." -ForegroundColor Red
    try {
        docker-compose -f "h:\empire-monitoring-stack-v2-enhanced.docker-compose.yml" down
        Write-Host "✅ Empire stack stopped successfully!" -ForegroundColor Green
    } catch {
        Write-Host "❌ Failed to stop empire stack: $_" -ForegroundColor Red
    }
}

function Restart-EmpireStack {
    Write-Host "`n🔄 RESTARTING EMPIRE MONITORING STACK..." -ForegroundColor Yellow
    Stop-EmpireStack
    Start-Sleep -Seconds 3
    Deploy-EmpireStack
}

function Show-EmpireLogs {
    Write-Host "`n📝 EMPIRE STACK LOGS:" -ForegroundColor Cyan
    Write-Host "=====================" -ForegroundColor Cyan
    
    if ($Service -eq "all") {
        Write-Host "🔍 Showing logs for all empire services..." -ForegroundColor Yellow
        docker-compose -f "h:\empire-monitoring-stack-v2-enhanced.docker-compose.yml" logs --tail=20 -f
    } else {
        Write-Host "🔍 Showing logs for $Service..." -ForegroundColor Yellow
        docker-compose -f "h:\empire-monitoring-stack-v2-enhanced.docker-compose.yml" logs --tail=20 -f $Service
    }
}

# Main execution logic
if ($Deploy) {
    Deploy-EmpireStack
} elseif ($Stop) {
    Stop-EmpireStack
} elseif ($Restart) {
    Restart-EmpireStack
} elseif ($Logs) {
    Show-EmpireLogs
} elseif ($Status) {
    Show-EmpireStatus
} else {
    Write-Host "`n🎯 EMPIRE MONITORING STACK V2.0 COMMANDS:" -ForegroundColor Yellow
    Write-Host "==========================================" -ForegroundColor Yellow
    Write-Host "🚀 .\empire-deploy.ps1 -Deploy      # Deploy enhanced stack" -ForegroundColor Cyan
    Write-Host "🛑 .\empire-deploy.ps1 -Stop        # Stop empire stack" -ForegroundColor Cyan
    Write-Host "🔄 .\empire-deploy.ps1 -Restart     # Restart empire stack" -ForegroundColor Cyan
    Write-Host "🔍 .\empire-deploy.ps1 -Status      # Show stack status" -ForegroundColor Cyan
    Write-Host "📝 .\empire-deploy.ps1 -Logs        # Show all logs" -ForegroundColor Cyan
    Write-Host "📝 .\empire-deploy.ps1 -Logs -Service grafana-empire # Show specific service logs" -ForegroundColor Cyan
    Write-Host "`n🏰 Ready to enhance your empire monitoring capabilities! 👑" -ForegroundColor Magenta
}

# 🎯 EMPIRE MONITORING STACK V2.0 FEATURES:
# ✅ One-command deployment and management
# ✅ Enhanced Docker monitoring with cAdvisor and Node Exporter
# ✅ Centralized log aggregation with Loki and Promtail
# ✅ Redis caching layer for advanced dashboards
# ✅ Security hardening with Docker socket proxy
# ✅ Grafana v12.1 with latest features enabled
# ✅ Empire-branded configuration and dashboards

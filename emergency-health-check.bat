@echo off
echo.
echo 🚨 EMERGENCY EMPIRE HEALTH CHECK 🚨
echo ===================================
echo.

echo 📊 CHECKING GRAFANA...
curl -s http://localhost:3001/api/health > nul 2>&1
if %errorlevel% == 0 (
    echo ✅ Grafana: RESPONDING
) else (
    echo ❌ Grafana: DOWN
)

echo.
echo 📊 CHECKING PROMETHEUS...
curl -s http://localhost:9090/-/healthy > nul 2>&1
if %errorlevel% == 0 (
    echo ✅ Prometheus: RESPONDING
) else (
    echo ❌ Prometheus: DOWN
)

echo.
echo 📊 CHECKING CADVISOR...
curl -s http://localhost:8080/healthz > nul 2>&1
if %errorlevel% == 0 (
    echo ✅ cAdvisor: RESPONDING
) else (
    echo ❌ cAdvisor: DOWN
)

echo.
echo 📊 CHECKING NODE EXPORTER...
curl -s http://localhost:9100/metrics > nul 2>&1
if %errorlevel% == 0 (
    echo ✅ Node Exporter: RESPONDING
) else (
    echo ❌ Node Exporter: DOWN
)

echo.
echo 🐳 CHECKING DOCKER STATUS...
docker --version > nul 2>&1
if %errorlevel% == 0 (
    echo ✅ Docker: INSTALLED
) else (
    echo ❌ Docker: NOT AVAILABLE
)

echo.
echo 🔍 DOCKER CONTAINER STATUS...
docker ps > nul 2>&1
if %errorlevel% == 0 (
    echo ✅ Docker Engine: RESPONDING
    docker ps --format "table {{.Names}}\t{{.Status}}"
) else (
    echo ❌ Docker Engine: API ISSUES DETECTED
    echo 🛠️ RECOVERY ACTION NEEDED: Restart Docker Desktop
)

echo.
echo 📁 CHECKING CRITICAL FILES...
if exist "h:\grafana-config" (
    echo ✅ Grafana Config: EXISTS
) else (
    echo ❌ Grafana Config: MISSING
)

if exist "h:\🎨👑💎_LEGENDARY_EMPIRE_DASHBOARD_IMPORTER_💎👑🎨.ps1" (
    echo ✅ Dashboard Importer: EXISTS
) else (
    echo ❌ Dashboard Importer: MISSING
)

echo.
echo 🏆 EMPIRE STATUS SUMMARY:
echo ========================
echo If any services show DOWN or API ISSUES:
echo 1. Try restarting Docker Desktop
echo 2. Wait 30 seconds for services to stabilize
echo 3. Run this check again
echo.
echo 🌐 Access Grafana: http://localhost:3001
echo 📊 Access Prometheus: http://localhost:9090
echo.
pause

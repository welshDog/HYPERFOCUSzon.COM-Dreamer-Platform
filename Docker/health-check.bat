@echo off
REM ⚡💎🐳 HYPERFOCUS ZONE EMPIRE - HEALTH CHECK SCRIPT 🐳💎⚡

echo Checking HyperFocus Zone Empire Health...
echo.

REM Check Docker daemon
echo 🔍 Checking Docker daemon...
docker info >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Docker daemon not running
) else (
    echo ✅ Docker daemon running
)

echo.

REM Check running containers
echo 🐳 Running containers:
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

echo.

REM Check container health
echo 🏥 Container health status:
for /f "tokens=*" %%i in ('docker ps --filter "health=healthy" --format "{{.Names}}"') do echo ✅ %%i - Healthy
for /f "tokens=*" %%i in ('docker ps --filter "health=unhealthy" --format "{{.Names}}"') do echo ❌ %%i - Unhealthy

echo.

REM Check resource usage
echo 📊 Resource usage:
docker stats --no-stream --format "table {{.Container}}\t{{.CPUPerc}}\t{{.MemUsage}}"

echo.
echo 🎯 Health check complete!
pause

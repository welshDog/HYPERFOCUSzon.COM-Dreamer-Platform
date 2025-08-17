@echo off
REM ⚡💎🐳 HYPERFOCUS ZONE EMPIRE - DOCKER START SCRIPT 🐳💎⚡

echo Starting HyperFocus Zone Empire Docker Services...
echo.

REM Check if Docker is running
docker info >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Docker is not running. Please start Docker Desktop first.
    pause
    exit /b 1
)

echo ✅ Docker is running
echo.

REM Start essential services only
echo 🚀 Starting essential empire services...
docker-compose up -d postgres redis hyperfocus_api nginx

echo.
echo 🎉 Empire services started successfully!
echo 📊 Access your empire at: http://localhost
echo 🗄️ Database: localhost:5432
echo 🔴 Redis: localhost:6379
echo.

REM Show running containers
echo 📋 Running containers:
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

echo.
echo ⚡ Your HyperFocus Zone Empire is ready! ⚡
pause

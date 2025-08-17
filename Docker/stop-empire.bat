@echo off
REM ⚡💎🐳 HYPERFOCUS ZONE EMPIRE - DOCKER STOP SCRIPT 🐳💎⚡

echo Stopping HyperFocus Zone Empire Docker Services...
echo.

REM Stop all services
docker-compose down

echo.
echo 🛑 All empire services stopped
echo 💾 Data is preserved in Docker volumes
echo.

REM Show system resources freed
echo 📊 System resources freed:
docker system df

echo.
echo ✅ Empire services stopped successfully!
pause

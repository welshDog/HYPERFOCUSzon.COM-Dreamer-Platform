@echo off
REM 🚀💎⚡ LEGENDARY PI DEPLOYMENT - WINDOWS BATCH ⚡💎🚀

echo.
echo 🚀💎⚡ LEGENDARY PI DEPLOYMENT EXECUTION ⚡💎🚀
echo ================================================
echo.

set PI_IP=192.168.137.100

echo 🔍 Step 1: Testing Pi connectivity...
ping -n 3 %PI_IP%
if errorlevel 1 (
    echo ❌ Pi not reachable at %PI_IP%
    echo 💡 Please check Pi network connection and try again
    pause
    exit /b 1
)

echo ✅ Pi is reachable!
echo.

echo 🚀 Step 2: Deploying to Pi...
echo 📋 Manual commands to run:
echo.
echo 1. Copy deployment files to Pi:
echo    scp docker-compose-legendary-pi.yml pi@%PI_IP%:/home/pi/microcloud/
echo.
echo 2. SSH to Pi and deploy:
echo    ssh pi@%PI_IP%
echo    cd /home/pi/microcloud
echo    docker-compose -f docker-compose-legendary-pi.yml down 2^>^/dev^/null ^|^| true
echo    docker-compose -f docker-compose-legendary-pi.yml up -d
echo    sleep 30
echo    docker-compose -f docker-compose-legendary-pi.yml ps
echo.

echo 💡 If you have WSL or Git Bash, you can run these directly
echo 💡 Otherwise, use PuTTY or another SSH client

pause

echo.
echo 🧪 Step 3: Testing deployment...
echo 📊 After deployment, test these URLs:
echo    • Health Monitor:  http://%PI_IP%/
echo    • BROski Agent:    http://%PI_IP%:8080/
echo.

echo 🎯 Step 4: Run testing suite:
echo    python legendary_pi_client_tester.py
echo.

echo 🏆 Your LEGENDARY Pi micro-cloud deployment is ready!
pause

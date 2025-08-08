@echo off
echo 🔥💎⚡ LEGENDARY PI CONNECTION TEAM SUPPORT ⚡💎🔥
echo.
echo 🎯 Target Pi: 192.168.137.10
echo 🔍 Testing connections...
echo.

REM Test basic ping
ping -n 2 192.168.137.10 > nul
if %errorlevel% == 0 (
    echo ✅ Pi responds to ping - Network OK!
) else (
    echo ❌ Pi not responding to ping
    pause
    exit
)

REM Try to start browser
echo.
echo 🚀 Launching browser to Pi VS Code Server...
start http://192.168.137.10:8080
echo ✅ Browser launched!

echo.
echo 📋 MANUAL CONNECTION OPTIONS:
echo.
echo 🌐 Option 1: Browser URLs to try:
echo    http://192.168.137.10:8080
echo    http://192.168.137.10:8080/?folder=/home/pi
echo.
echo 🔧 Option 2: SSH to Pi and start VS Code Server:
echo    ssh pi@192.168.137.10
echo    code-server --bind-addr=0.0.0.0:8080 --auth=none
echo.
echo 📓 Option 3: Start Jupyter on Pi:
echo    ssh pi@192.168.137.10
echo    jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root
echo.
echo 🎊 Once connected, access Jupyter at: http://192.168.137.10:8888
echo.
echo 🔥💎⚡ LEGENDARY TEAM READY TO HELP! ⚡💎🔥
pause

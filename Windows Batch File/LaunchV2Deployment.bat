@echo off
echo LEGENDARY V2 DEPLOYMENT LAUNCHER
echo.
echo Starting V2 Analytics Dashboard...
start "V2 Analytics" cmd /k "H:/.venv/Scripts/python.exe v2_analytics_server.py"

echo.
echo Starting V2 WebSocket Server...
start "V2 WebSocket" cmd /k "H:/.venv/Scripts/python.exe v2_websocket_server.py"

echo.
echo Dashboard: http://localhost:9999
echo WebSocket: ws://localhost:8765
echo.
echo V2 DEPLOYMENT ACTIVATED!
pause

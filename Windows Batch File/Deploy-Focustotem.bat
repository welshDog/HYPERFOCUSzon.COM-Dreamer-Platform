@echo off
echo HYPERFOCUS AZURE EMPIRE DEPLOYMENT
echo.
echo Starting legendary Azure transformation...
echo.

REM Check if AZD is available
azd --version >nul 2>&1
if errorlevel 1 (
    echo Azure Developer CLI not found!
    echo Please install AZD first: winget install microsoft.azd
    pause
    exit /b 1
)

REM Login to Azure
echo Logging into Azure...
azd auth login

REM Deploy the empire
echo Deploying infrastructure...
azd up

echo.
echo DEPLOYMENT COMPLETE! Check Azure portal for your legendary empire!
pause

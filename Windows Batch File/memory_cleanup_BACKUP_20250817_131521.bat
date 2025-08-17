@echo off
echo LEGENDARY MEMORY OPTIMIZER
echo.
echo Clearing temporary files...
del /q /f "%TEMP%\*" 2>nul
echo.
echo Clearing Windows temp...
del /q /f "C:\Windows\Temp\*" 2>nul
echo.
echo Temporary files cleared!
echo Manually close unnecessary browser tabs
echo Keep VS Code processes for HYPERFOCUS mode
echo.
pause

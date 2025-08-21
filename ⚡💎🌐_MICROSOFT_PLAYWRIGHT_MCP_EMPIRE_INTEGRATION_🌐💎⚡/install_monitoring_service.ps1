
# PowerShell script to install continuous monitoring as Windows service
# Requires NSSM (Non-Sucking Service Manager)

# Download NSSM if not present
if (!(Test-Path "nssm.exe")) {
    Write-Host "📦 Downloading NSSM (Non-Sucking Service Manager)..."
    Invoke-WebRequest -Uri "https://nssm.cc/release/nssm-2.24.zip" -OutFile "nssm.zip"
    Expand-Archive -Path "nssm.zip" -DestinationPath "."
    Copy-Item "nssm-2.24\win64\nssm.exe" -Destination "."
    Remove-Item "nssm.zip" -Force
    Remove-Item "nssm-2.24" -Recurse -Force
}

# Install service
.\nssm.exe install "ImmortalEmpireMonitoring" python "H:\⚡💎🌐_MICROSOFT_PLAYWRIGHT_MCP_EMPIRE_INTEGRATION_🌐💎⚡\continuous_empire_monitoring.py"
.\nssm.exe set "ImmortalEmpireMonitoring" Description "Continuous monitoring for Immortal Empire infrastructure"
.\nssm.exe set "ImmortalEmpireMonitoring" Start SERVICE_AUTO_START

# Start service
.\nssm.exe start "ImmortalEmpireMonitoring"

Write-Host "✅ Immortal Empire Continuous Monitoring service installed and started!"

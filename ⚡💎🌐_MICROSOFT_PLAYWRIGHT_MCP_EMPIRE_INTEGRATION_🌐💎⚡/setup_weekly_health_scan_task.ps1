
# PowerShell command to create Windows Task Scheduler entry
$action = New-ScheduledTaskAction -Execute "python" -Argument "H:\⚡💎🌐_MICROSOFT_PLAYWRIGHT_MCP_EMPIRE_INTEGRATION_🌐💎⚡\automated_weekly_health_scan.py"
$trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Monday -At 9:00AM
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries
$principal = New-ScheduledTaskPrincipal -UserId "$env:USERNAME" -LogonType Interactive

Register-ScheduledTask -TaskName "ImmortalEmpireWeeklyHealthScan" -Action $action -Trigger $trigger -Settings $settings -Principal $principal -Description "Automated weekly health scan for Immortal Empire infrastructure"

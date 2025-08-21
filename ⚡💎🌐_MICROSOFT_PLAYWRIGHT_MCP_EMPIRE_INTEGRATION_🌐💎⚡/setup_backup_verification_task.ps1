
# PowerShell command to create daily backup verification task
$action = New-ScheduledTaskAction -Execute "python" -Argument "H:\⚡💎🌐_MICROSOFT_PLAYWRIGHT_MCP_EMPIRE_INTEGRATION_🌐💎⚡\immortal_backup_verification.py"
$trigger = New-ScheduledTaskTrigger -Daily -At 2:00AM
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries
$principal = New-ScheduledTaskPrincipal -UserId "$env:USERNAME" -LogonType Interactive

Register-ScheduledTask -TaskName "ImmortalBackupVerification" -Action $action -Trigger $trigger -Settings $settings -Principal $principal -Description "Daily backup verification for Immortal Empire data protection"

@echo off
echo 🏰 LEGENDARY EMPIRE DASHBOARD IMPORTER 🏰
echo.
echo 📊 Importing Empire Command Center Dashboard...

curl -X POST ^
  -H "Content-Type: application/json" ^
  -H "Authorization: Basic YWRtaW46QlJPc2tpMjAyNSE=" ^
  -d @"h:\grafana-config\dashboards\empire\🏰👑_EMPIRE_COMMAND_CENTER_LEGENDARY_OVERVIEW_👑🏰.json" ^
  http://localhost:3001/api/dashboards/db

echo.
echo 🤖 Importing Hyperfocus Productivity Analytics...

curl -X POST ^
  -H "Content-Type: application/json" ^
  -H "Authorization: Basic YWRtaW46QlJPc2tpMjAyNSE=" ^
  -d @"h:\grafana-config\dashboards\empire\🤖💎_HYPERFOCUS_PRODUCTIVITY_ANALYTICS_💎🤖.json" ^
  http://localhost:3001/api/dashboards/db

echo.
echo 🔮 Importing AI Insights & Trendline Predictions...

curl -X POST ^
  -H "Content-Type: application/json" ^
  -H "Authorization: Basic YWRtaW46QlJPc2tpMjAyNSE=" ^
  -d @"h:\grafana-config\dashboards\empire\🔮💎_AI_INSIGHTS_TRENDLINE_PREDICTIONS_💎🔮.json" ^
  http://localhost:3001/api/dashboards/db

echo.
echo ✅ Dashboard import complete!
echo 🌐 Access your dashboards at: http://localhost:3001/dashboards
echo.
pause

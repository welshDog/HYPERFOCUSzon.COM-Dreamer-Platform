@echo off
REM 🚀💎⚡ HYPERFOCUS ZONE EMPIRE - INSTANT DEPLOYMENT ⚡💎🚀

echo.
echo 🚀💎⚡ HYPERFOCUS ZONE EMPIRE DEPLOYMENT ⚡💎🚀
echo ════════════════════════════════════════════════════
echo.

REM Check if index.html exists
if not exist "index.html" (
    echo ❌ ERROR: index.html not found! Make sure you're in the project root.
    pause
    exit /b 1
)

echo ✅ Project files found!
echo.

:menu
echo 🎯 DEPLOYMENT OPTIONS:
echo.
echo 1. 🚀 Vercel (Recommended - Fastest)
echo 2. 🌐 Netlify (Reliable)
echo 3. 📄 GitHub Pages (Free)
echo 4. 🏆 ALL PLATFORMS (Legendary)
echo 5. 🧪 Local Preview
echo 6. 📚 View Instructions
echo 0. Exit
echo.

set /p choice="Choose deployment option (1-6, 0 to exit): "

if "%choice%"=="1" goto vercel
if "%choice%"=="2" goto netlify
if "%choice%"=="3" goto github
if "%choice%"=="4" goto all
if "%choice%"=="5" goto preview
if "%choice%"=="6" goto instructions
if "%choice%"=="0" goto exit

echo Invalid choice! Please try again.
goto menu

:vercel
echo.
echo 🚀 Deploying to Vercel...
echo 📦 Installing Vercel CLI (if needed)...
call npm install -g vercel
echo 🌟 Deploying to production...
call vercel --prod
goto success

:netlify
echo.
echo 🌐 Deploying to Netlify...
echo 📦 Installing Netlify CLI (if needed)...
call npm install -g netlify-cli
echo 🌟 Deploying to production...
call netlify deploy --prod --dir=.
goto success

:github
echo.
echo 📄 Preparing GitHub Pages deployment...
echo 📝 Adding files to git...
call git add .
call git commit -m "🚀 HYPERFOCUS ZONE EMPIRE - Live Deployment"
echo 📤 Pushing to GitHub...
call git push origin main
echo ✅ Pushed to GitHub! Configure Pages in repository settings.
goto success

:all
echo.
echo 🏆 LEGENDARY DEPLOYMENT - ALL PLATFORMS!
echo.
call %0 1
call %0 2
call %0 3
goto success

:preview
echo.
echo 🧪 Starting local preview server...
echo 🌐 Opening http://localhost:3000
start http://localhost:3000
call npx http-server . -p 3000 -o
goto menu

:instructions
echo.
echo 📚 DEPLOYMENT INSTRUCTIONS:
echo.
echo 1. Vercel: Fast, reliable, automatic HTTPS
echo 2. Netlify: Great features, continuous deployment
echo 3. GitHub Pages: Free, integrated with GitHub
echo.
echo 📖 For detailed instructions, see DEPLOYMENT.md
echo.
pause
goto menu

:success
echo.
echo 🎊 DEPLOYMENT COMPLETED SUCCESSFULLY!
echo ════════════════════════════════════════════════════
echo.
echo 🏆💎⚡ HYPERFOCUS ZONE EMPIRE IS LIVE! ⚡💎🏆
echo ✨ Features: 18+ Portals ^| ADHD Navigation ^| Support Integration
echo 🌍 Mission: Transform 1.1 billion neurodivergent lives!
echo ❤️‍🔥 BROski$ Earned: +1000 LEGENDARY DEPLOYMENT POINTS!
echo.
pause
goto exit

:exit
echo.
echo 👋 Thank you for using HYPERFOCUS ZONE Empire Deployment!
echo ✨ SEND-ME.NFT@UD.ME ✨ ^| hyperfocuszone.com
pause
exit /b 0

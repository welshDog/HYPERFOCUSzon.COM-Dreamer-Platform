#!/usr/bin/env pwsh
# 🔥💎⚡ RAPID PI DEVELOPMENT SETUP - DIRECT APPROACH ⚡💎🔥

Write-Host "🔥💎⚡ RAPID PI DEVELOPMENT SETUP ⚡💎🔥" -ForegroundColor Magenta
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "🎯 Since your Pi has LEGENDARY gigabit connectivity (0ms ping)," -ForegroundColor Green
Write-Host "   let's set up development while SSH configuration completes!" -ForegroundColor Green
Write-Host ""

Write-Host "🚀 DIRECT PI DEVELOPMENT COMMANDS:" -ForegroundColor Yellow
Write-Host "===================================" -ForegroundColor DarkYellow
Write-Host ""

Write-Host "📋 RUN THESE ON YOUR PI TERMINAL:" -ForegroundColor Cyan
Write-Host ""

$Commands = @"
# Update system and install development IDEs
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install -y ninja-ide geany git curl wget vim tree htop

# Install Python development tools
sudo apt-get install -y python3-pip python3-venv python3-dev
pip3 install --upgrade pip setuptools wheel
pip3 install jupyter notebook ipython pandas numpy matplotlib requests

# Install VS Code (if not already installed)
curl -fsSL https://code.visualstudio.com/sha/download?build=stable&os=linux-deb | sudo dpkg -i /dev/stdin || sudo apt-get install -f

# Install VS Code Server for remote browser access
curl -fsSL https://code-server.dev/install.sh | sh
sudo systemctl enable --now code-server@$USER

# Create development workspace
mkdir -p ~/legendary-development/{python,web,iot,projects}
cd ~/legendary-development

# Configure git (replace with your info)
git config --global user.name "Legendary Developer"
git config --global user.email "broski@legendary.dev"

# Test installations
echo "🎊 TESTING INSTALLATIONS:"
ninja-ide --version 2>/dev/null && echo "✅ Ninja-IDE installed" || echo "⚠️ Ninja-IDE needs manual install"
geany --version 2>/dev/null && echo "✅ Geany installed" || echo "⚠️ Geany needs manual install"
python3 --version && echo "✅ Python3 ready"
pip3 --version && echo "✅ Pip3 ready"
jupyter --version 2>/dev/null && echo "✅ Jupyter ready" || echo "⚠️ Jupyter needs install"

echo ""
echo "🔥💎⚡ DEVELOPMENT ENVIRONMENT READY! ⚡💎🔥"
echo "=========================================="
echo "🥷 Start Ninja-IDE: ninja-ide"
echo "⚡ Start Geany: geany"
echo "📓 Start Jupyter: jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser"
echo "💻 VS Code Server: systemctl --user status code-server"
echo ""
echo "🌐 ACCESS FROM LAPTOP:"
echo "   📓 Jupyter: http://192.168.137.10:8888"
echo "   💻 VS Code: http://192.168.137.10:8080"
echo ""
echo "🎊 LEGENDARY PI DEVELOPMENT POWERHOUSE ACTIVATED!"
"@

Write-Host $Commands -ForegroundColor White

Write-Host ""
Write-Host "🔄 COPY AND PASTE THESE COMMANDS INTO YOUR PI TERMINAL" -ForegroundColor Magenta
Write-Host ""

Write-Host "⚡ IMMEDIATE ACCESS OPTIONS:" -ForegroundColor Yellow
Write-Host "   🥷 Ninja-IDE: Run 'ninja-ide' on Pi desktop" -ForegroundColor White
Write-Host "   ⚡ Geany: Run 'geany' on Pi desktop" -ForegroundColor White
Write-Host "   📓 Jupyter: http://192.168.137.10:8888 (after setup)" -ForegroundColor White
Write-Host "   💻 VS Code: http://192.168.137.10:8080 (after setup)" -ForegroundColor White

Write-Host ""
Write-Host "🎊 YOUR GIGABIT SETUP IS PERFECT FOR INSTANT DEVELOPMENT!" -ForegroundColor Green

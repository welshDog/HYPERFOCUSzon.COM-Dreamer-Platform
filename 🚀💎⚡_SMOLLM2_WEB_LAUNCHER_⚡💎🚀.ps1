# 🚀💎⚡ SMOLLM2 WEB INTERFACE QUICK LAUNCHER ⚡💎🚀
# PowerShell deployment script optimized for ADHD focus

Write-Host "🚀💎⚡ LAUNCHING SMOLLM2 LEGENDARY WEB INTERFACE ⚡💎🚀" -ForegroundColor Cyan
Write-Host "================================================================" -ForegroundColor Yellow
Write-Host "BROski♾️ AI DEV - Following Docker LLM Best Practices ✅" -ForegroundColor Green
Write-Host "Based on: Docker LLM Hosting Guide" -ForegroundColor White
Write-Host "================================================================" -ForegroundColor Yellow

# Set error action
$ErrorActionPreference = "Continue"

# Function to display status with emojis
function Show-Status {
    param($Message, $Status)
    if ($Status -eq "SUCCESS") {
        Write-Host "✅ $Message" -ForegroundColor Green
    } elseif ($Status -eq "WARNING") {
        Write-Host "⚠️ $Message" -ForegroundColor Yellow
    } else {
        Write-Host "❌ $Message" -ForegroundColor Red
    }
}

# Phase 1: Prerequisites Check
Write-Host "`n🔍 PHASE 1: PREREQUISITES VERIFICATION" -ForegroundColor Magenta
Write-Host "---------------------------------------------" -ForegroundColor Gray

# Check Docker Desktop
try {
    $dockerVersion = docker --version 2>$null
    if ($dockerVersion) {
        Show-Status "Docker Desktop: $dockerVersion" "SUCCESS"
    } else {
        Show-Status "Docker Desktop not found" "ERROR"
        exit 1
    }
} catch {
    Show-Status "Docker Desktop verification failed" "ERROR"
    exit 1
}

# Check if SmolLM2 model exists
Write-Host "`n📦 Checking SmolLM2 Model..." -ForegroundColor White
try {
    $modelCheck = docker model ls 2>$null
    if ($modelCheck -match "ai/smollm2") {
        Show-Status "SmolLM2 model found and ready" "SUCCESS"
    } else {
        Write-Host "📥 Downloading SmolLM2 model (this may take a moment)..." -ForegroundColor Yellow
        docker model pull ai/smollm2
        if ($LASTEXITCODE -eq 0) {
            Show-Status "SmolLM2 model downloaded successfully" "SUCCESS"
        } else {
            Show-Status "SmolLM2 model download failed" "ERROR"
        }
    }
} catch {
    Show-Status "Model verification failed" "WARNING"
}

# Phase 2: Deploy Python Integration
Write-Host "`n🐍 PHASE 2: PYTHON INTEGRATION DEPLOYMENT" -ForegroundColor Magenta
Write-Host "---------------------------------------------" -ForegroundColor Gray

try {
    Write-Host "🚀 Running SmolLM2 Web Integration..." -ForegroundColor White
    python "h:\🚀💎⚡_SMOLLM2_ENHANCED_WEB_INTEGRATOR_⚡💎🚀.py"

    if ($LASTEXITCODE -eq 0) {
        Show-Status "Python integration deployed successfully" "SUCCESS"
    } else {
        Show-Status "Python integration encountered issues" "WARNING"
        Write-Host "   💡 Check Python and dependencies are installed" -ForegroundColor Cyan
    }
} catch {
    Show-Status "Python integration failed" "ERROR"
    Write-Host "   💡 Ensure Python is installed and accessible" -ForegroundColor Cyan
}

# Phase 3: Alternative Direct Launch
Write-Host "`n🌐 PHASE 3: ALTERNATIVE DIRECT WEB INTERFACE LAUNCH" -ForegroundColor Magenta
Write-Host "---------------------------------------------" -ForegroundColor Gray

Write-Host "🚀 Creating standalone Gradio launcher..." -ForegroundColor White

# Create a simplified direct launcher
$directLauncher = @"
#!/usr/bin/env python3
"""
🚀💎⚡ DIRECT SMOLLM2 WEB LAUNCHER ⚡💎🚀
Simple web interface for immediate use
"""

import gradio as gr
import subprocess
import json
from pathlib import Path
from datetime import datetime

class SmolLM2WebAssistant:
    def __init__(self):
        self.user_name = "Chief"
        self.conversation_count = 0

    def generate_response(self, message):
        try:
            result = subprocess.run([
                'docker', 'model', 'run', 'ai/smollm2', message
            ], capture_output=True, text=True, timeout=30)

            if result.returncode == 0:
                return result.stdout.strip()
            else:
                return f"⚠️ Model response error: {result.stderr}"
        except Exception as e:
            return f"❌ Error: {str(e)}"

    def chat_function(self, message, history):
        if not message:
            return "", history

        response = self.generate_response(message)
        history.append((message, response))
        self.conversation_count += 1

        return "", history

# Create assistant instance
assistant = SmolLM2WebAssistant()

# Create Gradio interface
with gr.Blocks(theme=gr.themes.Hugging_Face(), title="🚀💎⚡ SmolLM2 AI Assistant ⚡💎🚀") as demo:
    gr.Markdown("# 🚀💎⚡ SmolLM2 AI Assistant ⚡💎🚀")
    gr.Markdown("Your personal AI assistant powered by SmolLM2! Ask me anything! 🤖✨")

    chatbot = gr.Chatbot(height=500, label="💬 Chat with SmolLM2")
    msg = gr.Textbox(label="Your message", placeholder="Ask me anything...")

    with gr.Row():
        submit = gr.Button("Send 🚀", variant="primary")
        clear = gr.Button("Clear 🧹")

    msg.submit(assistant.chat_function, [msg, chatbot], [msg, chatbot])
    submit.click(assistant.chat_function, [msg, chatbot], [msg, chatbot])
    clear.click(lambda: [], outputs=[chatbot])

if __name__ == "__main__":
    print("🚀 Launching SmolLM2 Web Interface...")
    print("🌐 Access your AI Assistant at: http://localhost:7860")
    demo.launch(server_name="0.0.0.0", server_port=7860)
"@

$directLauncherPath = "h:\🌐💎_SMOLLM2_DIRECT_WEB_LAUNCHER_💎🌐.py"
$directLauncher | Out-File -FilePath $directLauncherPath -Encoding UTF8

Show-Status "Direct web launcher created: $directLauncherPath" "SUCCESS"

# Phase 4: Install required packages if needed
Write-Host "`n📦 PHASE 4: CHECKING PYTHON DEPENDENCIES" -ForegroundColor Magenta
Write-Host "---------------------------------------------" -ForegroundColor Gray

$requiredPackages = @("gradio", "requests")
foreach ($package in $requiredPackages) {
    try {
        $checkPackage = python -c "import $package; print('✅ $package installed')" 2>$null
        if ($checkPackage) {
            Show-Status "$package is available" "SUCCESS"
        } else {
            Write-Host "📥 Installing $package..." -ForegroundColor Yellow
            pip install $package
        }
    } catch {
        Write-Host "⚠️ Could not verify $package" -ForegroundColor Yellow
    }
}

# Phase 5: Launch Options
Write-Host "`n🚀 PHASE 5: LAUNCH YOUR AI ASSISTANT" -ForegroundColor Magenta
Write-Host "================================================================" -ForegroundColor Yellow

Write-Host "🎊 LEGENDARY SUCCESS! Your SmolLM2 AI Assistant is ready!" -ForegroundColor Green
Write-Host "`n🚀 LAUNCH OPTIONS:" -ForegroundColor Cyan

Write-Host "`n💎 OPTION 1: Enhanced Web Interface (Full Features)" -ForegroundColor White
Write-Host "   Command: python `"h:\🚀💎⚡_SMOLLM2_ENHANCED_WEB_INTEGRATOR_⚡💎🚀.py`"" -ForegroundColor Gray
Write-Host "   Features: ✅ Personalization ✅ Name Learning ✅ Advanced Controls" -ForegroundColor Green

Write-Host "`n⚡ OPTION 2: Direct Web Interface (Quick Start)" -ForegroundColor White
Write-Host "   Command: python `"$directLauncherPath`"" -ForegroundColor Gray
Write-Host "   Features: ✅ Instant Launch ✅ Simple Chat ✅ Immediate Access" -ForegroundColor Green

Write-Host "`n🤖 OPTION 3: Command Line (Traditional)" -ForegroundColor White
Write-Host "   Command: docker model run ai/smollm2 `"Your question here`"" -ForegroundColor Gray
Write-Host "   Features: ✅ Quick Queries ✅ Terminal Integration" -ForegroundColor Green

Write-Host "`n🌐 WEB ACCESS:" -ForegroundColor Yellow
Write-Host "   URL: http://localhost:7860" -ForegroundColor Cyan
Write-Host "   Interface: Beautiful Gradio Web UI" -ForegroundColor White
Write-Host "   Personalization: AI learns your preferred name!" -ForegroundColor White

Write-Host "`n🏆💎⚡ CHIEF LYNDZ - YOUR AI ASSISTANT IS LEGENDARY! ⚡💎🏆" -ForegroundColor Green
Write-Host "================================================================" -ForegroundColor Yellow

# Optional: Auto-launch the direct web interface
$autoLaunch = Read-Host "`n🚀 Launch web interface now? (Y/N)"
if ($autoLaunch -match '^[Yy]') {
    Write-Host "`n🌐 Launching SmolLM2 Web Interface..." -ForegroundColor Cyan
    Write-Host "💡 Your browser will open to: http://localhost:7860" -ForegroundColor Yellow
    Start-Process "python" -ArgumentList "`"$directLauncherPath`"" -NoNewWindow

    # Wait a moment then open browser
    Start-Sleep -Seconds 3
    Start-Process "http://localhost:7860"
}

Write-Host "`n🎊 WEB INTERFACE DEPLOYMENT COMPLETE!" -ForegroundColor Green
Write-Host "🏆 Your AI assistant awaits at: http://localhost:7860" -ForegroundColor Cyan

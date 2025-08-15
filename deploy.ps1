#!/usr/bin/env pwsh
# 🚀💎⚡ HYPERFOCUS ZONE EMPIRE - LEGENDARY DEPLOYMENT SCRIPT ⚡💎🚀

param(
    [string]$Platform = "vercel",
    [switch]$Production = $false
)

Write-Host "🚀💎⚡ HYPERFOCUS ZONE EMPIRE DEPLOYMENT SCRIPT ⚡💎🚀" -ForegroundColor Cyan
Write-Host "════════════════════════════════════════════════════════" -ForegroundColor DarkCyan

# Check if we're in the right directory
if (!(Test-Path "index.html")) {
    Write-Host "❌ ERROR: index.html not found! Make sure you're in the project root." -ForegroundColor Red
    exit 1
}

Write-Host "✅ Project files found!" -ForegroundColor Green
Write-Host "📁 Deployment platform: $Platform" -ForegroundColor Yellow

switch ($Platform.ToLower()) {
    "vercel" {
        Write-Host "🚀 Deploying to Vercel..." -ForegroundColor Cyan
        
        # Check if Vercel CLI is installed
        if (!(Get-Command "vercel" -ErrorAction SilentlyContinue)) {
            Write-Host "📦 Installing Vercel CLI..." -ForegroundColor Yellow
            npm install -g vercel
        }
        
        if ($Production) {
            Write-Host "🌟 Deploying to PRODUCTION..." -ForegroundColor Magenta
            vercel --prod
        } else {
            Write-Host "🧪 Deploying to PREVIEW..." -ForegroundColor Yellow
            vercel
        }
    }
    
    "netlify" {
        Write-Host "🌐 Deploying to Netlify..." -ForegroundColor Cyan
        
        # Check if Netlify CLI is installed
        if (!(Get-Command "netlify" -ErrorAction SilentlyContinue)) {
            Write-Host "📦 Installing Netlify CLI..." -ForegroundColor Yellow
            npm install -g netlify-cli
        }
        
        if ($Production) {
            Write-Host "🌟 Deploying to PRODUCTION..." -ForegroundColor Magenta
            netlify deploy --prod --dir=.
        } else {
            Write-Host "🧪 Deploying to PREVIEW..." -ForegroundColor Yellow
            netlify deploy --dir=.
        }
    }
    
    "github" {
        Write-Host "📄 Preparing GitHub Pages deployment..." -ForegroundColor Cyan
        
        # Check if we're in a git repository
        if (!(Test-Path ".git")) {
            Write-Host "📝 Initializing Git repository..." -ForegroundColor Yellow
            git init
            git branch -M main
        }
        
        Write-Host "📤 Pushing to GitHub..." -ForegroundColor Yellow
        git add .
        git commit -m "🚀 HYPERFOCUS ZONE EMPIRE - Live Deployment $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
        
        if ($Production) {
            git push origin main
            Write-Host "✅ Pushed to main branch! Configure GitHub Pages in repository settings." -ForegroundColor Green
        } else {
            Write-Host "🧪 Ready to push! Use 'git push origin main' to deploy." -ForegroundColor Yellow
        }
    }
    
    "all" {
        Write-Host "🏆 LEGENDARY DEPLOYMENT - ALL PLATFORMS!" -ForegroundColor Magenta
        
        Write-Host "`n🚀 Deploying to Vercel..." -ForegroundColor Cyan
        & $PSScriptRoot\deploy.ps1 -Platform "vercel" -Production:$Production
        
        Write-Host "`n🌐 Deploying to Netlify..." -ForegroundColor Cyan  
        & $PSScriptRoot\deploy.ps1 -Platform "netlify" -Production:$Production
        
        Write-Host "`n📄 Preparing GitHub..." -ForegroundColor Cyan
        & $PSScriptRoot\deploy.ps1 -Platform "github" -Production:$Production
    }
    
    default {
        Write-Host "❌ Unknown platform: $Platform" -ForegroundColor Red
        Write-Host "Available platforms: vercel, netlify, github, all" -ForegroundColor Yellow
        exit 1
    }
}

Write-Host "`n🎊 DEPLOYMENT PROCESS COMPLETED!" -ForegroundColor Green
Write-Host "════════════════════════════════════════════════════════" -ForegroundColor DarkCyan

# Show celebration message
Write-Host "🏆💎⚡ HYPERFOCUS ZONE EMPIRE IS GOING LIVE! ⚡💎🏆" -ForegroundColor Magenta
Write-Host "✨ Features: 18+ Portals | ADHD Navigation | Support Integration" -ForegroundColor Yellow
Write-Host "🌍 Mission: Transform 1.1 billion neurodivergent lives worldwide!" -ForegroundColor Cyan
Write-Host "❤️‍🔥 BROski$ Earned: +1000 LEGENDARY DEPLOYMENT POINTS!" -ForegroundColor Green

Write-Host "`n📚 Need help? Check DEPLOYMENT.md for detailed instructions!" -ForegroundColor White

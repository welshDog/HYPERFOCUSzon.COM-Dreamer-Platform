#!/usr/bin/env pwsh
# 💎 Azure Container Apps Deployment Script for SmolLM2

Write-Host "🌟💎⚡ AZURE CONTAINER APPS DEPLOYMENT SYSTEM ⚡💎🌟" -ForegroundColor Cyan
Write-Host "=" * 80 -ForegroundColor Gray

$resourceGroup = "hyperfocus-empire-rg"
$containerAppName = "smollm2-legendary-app"
$environmentName = "hyperfocus-env"
$location = "eastus"

Write-Host "🎯 Deploying SmolLM2 to Azure Container Apps..." -ForegroundColor Yellow
Write-Host "🔑 Run 'az login' first, then execute this script!" -ForegroundColor Green

# Step 1: Create Resource Group
Write-Host "🏗️  Creating Resource Group..." -ForegroundColor Green
az group create --name $resourceGroup --location $location

# Step 2: Create Container Apps Environment
Write-Host "🌐 Creating Container Apps Environment..." -ForegroundColor Green
az containerapp env create --name $environmentName --resource-group $resourceGroup --location $location

# Step 3: Deploy SmolLM2 Container App
Write-Host "🚀 Deploying SmolLM2 Container App..." -ForegroundColor Green
az containerapp create `
    --name $containerAppName `
    --resource-group $resourceGroup `
    --environment $environmentName `
    --image "huggingface/smollm2:latest" `
    --target-port 11435 `
    --ingress external `
    --min-replicas 1 `
    --max-replicas 5 `
    --cpu-requests 1.0 `
    --memory-requests 2Gi `
    --env-vars LEGENDARY_MODE=true AZURE_DEPLOYMENT=true MODEL_NAME=SmolLM2

Write-Host "🎊 AZURE DEPLOYMENT SCRIPT READY!" -ForegroundColor Magenta

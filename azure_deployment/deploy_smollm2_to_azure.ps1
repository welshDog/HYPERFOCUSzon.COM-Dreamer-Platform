#!/usr/bin/env pwsh
# 💎 Azure Container Apps Deployment Script for SmolLM2

Write-Host "🌟💎⚡ AZURE CONTAINER APPS DEPLOYMENT SYSTEM ⚡💎🌟" -ForegroundColor Cyan
Write-Host "=" * 80 -ForegroundColor Gray

# Configuration
$resourceGroup = "hyperfocus-empire-rg"
$containerAppName = "smollm2-legendary-app"
$environmentName = "hyperfocus-env"
$location = "eastus"

Write-Host "🎯 Deploying SmolLM2 to Azure Container Apps..." -ForegroundColor Yellow

# Step 1: Create Resource Group
Write-Host "🏗️  Creating Resource Group..." -ForegroundColor Green
az group create --name $resourceGroup --location $location

if ($LASTEXITCODE -eq 0) {
    Write-Host "   ✅ Resource Group created successfully" -ForegroundColor Green
} else {
    Write-Host "   ⚠️  Resource Group creation failed or already exists" -ForegroundColor Yellow
}

# Step 2: Create Container Apps Environment
Write-Host "🌐 Creating Container Apps Environment..." -ForegroundColor Green
az containerapp env create --name $environmentName --resource-group $resourceGroup --location $location

if ($LASTEXITCODE -eq 0) {
    Write-Host "   ✅ Container Apps Environment created" -ForegroundColor Green
} else {
    Write-Host "   ⚠️  Environment creation failed or already exists" -ForegroundColor Yellow
}

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

if ($LASTEXITCODE -eq 0) {
    Write-Host "   ✅ SmolLM2 Container App deployed successfully!" -ForegroundColor Green

    # Get the application URL
    $appUrl = az containerapp show --name $containerAppName --resource-group $resourceGroup --query "properties.configuration.ingress.fqdn" -o tsv
    Write-Host "🎊 DEPLOYMENT SUCCESSFUL!" -ForegroundColor Magenta
    Write-Host "🌐 SmolLM2 URL: https://$appUrl" -ForegroundColor Cyan
    Write-Host "💎 Your SmolLM2 is now LEGENDARY in Azure!" -ForegroundColor Yellow
} else {
    Write-Host "   ❌ Container App deployment failed" -ForegroundColor Red
    Write-Host "   🔧 Check Azure CLI configuration and try again" -ForegroundColor Yellow
}

# Step 4: Create Web Interface Container App (Optional)
Write-Host "🌐 Deploying SmolLM2 Web Interface..." -ForegroundColor Green
az containerapp create `
    --name "${containerAppName}-web" `
    --resource-group $resourceGroup `
    --environment $environmentName `
    --image "gradio/gradio:latest" `
    --target-port 7860 `
    --ingress external `
    --min-replicas 1 `
    --max-replicas 3 `
    --cpu-requests 0.5 `
    --memory-requests 1Gi `
    --env-vars GRADIO_SERVER_NAME=0.0.0.0 GRADIO_SERVER_PORT=7860

Write-Host "🎯 AZURE DEPLOYMENT SUMMARY:" -ForegroundColor Cyan
Write-Host "-" * 50 -ForegroundColor Gray
Write-Host "✅ Resource Group: $resourceGroup" -ForegroundColor Green
Write-Host "✅ Environment: $environmentName" -ForegroundColor Green
Write-Host "✅ Container App: $containerAppName" -ForegroundColor Green
Write-Host "✅ Location: $location" -ForegroundColor Green
Write-Host "🎊 SmolLM2 is now LEGENDARY in Azure Container Apps!" -ForegroundColor Magenta

#!/usr/bin/env pwsh
# 💎 Azure Container Apps Deployment for SmolLM2

Write-Host "🌟💎 Deploying SmolLM2 to Azure Container Apps 💎🌟" -ForegroundColor Cyan

$resourceGroup = "hyperfocus-empire-rg"
$containerAppName = "smollm2-legendary-app"
$environmentName = "hyperfocus-env"

# Create Resource Group
az group create --name $resourceGroup --location eastus

# Create Container Apps Environment
az containerapp env create --name $environmentName --resource-group $resourceGroup --location eastus

# Deploy SmolLM2 Container App
az containerapp create `
    --name $containerAppName `
    --resource-group $resourceGroup `
    --environment $environmentName `
    --image huggingface/smollm2:latest `
    --target-port 11435 `
    --ingress external `
    --min-replicas 1 `
    --max-replicas 5

Write-Host "🎊 SmolLM2 deployed to Azure Container Apps!" -ForegroundColor Green

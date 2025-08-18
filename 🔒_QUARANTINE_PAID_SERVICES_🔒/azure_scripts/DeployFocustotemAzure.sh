#!/bin/bash
# 🚀 HyperFocus Zone Azure Deployment Script
echo "☁️ Starting HyperFocus Zone Azure deployment..."

# Set variables
RESOURCE_GROUP="hyperfocus-empire-rg"
LOCATION="eastus"
CONTAINER_APP_NAME="smollm2-legendary-app"
ENVIRONMENT_NAME="hyperfocus-env"

# Create resource group
echo "🏗️ Creating resource group..."
az group create --name $RESOURCE_GROUP --location $LOCATION

# Create Container Apps environment
echo "🌟 Creating Container Apps environment..."
az containerapp env create \
  --name $ENVIRONMENT_NAME \
  --resource-group $RESOURCE_GROUP \
  --location $LOCATION

# Create the SmolLM2 container app
echo "🚀 Creating SmolLM2 container app..."
az containerapp create \
  --name $CONTAINER_APP_NAME \
  --resource-group $RESOURCE_GROUP \
  --environment $ENVIRONMENT_NAME \
  --image "mcr.microsoft.com/azuredocs/containerapps-helloworld:latest" \
  --target-port 80 \
  --ingress 'external' \
  --query properties.configuration.ingress.fqdn

# Create Gradio web interface app
echo "🌐 Creating Gradio web interface..."
az containerapp create \
  --name "hyperfocus-gradio-app" \
  --resource-group $RESOURCE_GROUP \
  --environment $ENVIRONMENT_NAME \
  --image "mcr.microsoft.com/azuredocs/containerapps-helloworld:latest" \
  --target-port 80 \
  --ingress 'external' \
  --query properties.configuration.ingress.fqdn

echo "🎊 Azure deployment complete!"

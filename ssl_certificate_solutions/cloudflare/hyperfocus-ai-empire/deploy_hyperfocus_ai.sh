#!/bin/bash
# HyperFocus Zone AI Assistant - Deployment Script

echo "Deploying HyperFocus Zone AI Assistant..."

# Check Docker
if ! command -v docker &> /dev/null; then
    echo "Installing Docker..."
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
fi

# Check Docker Compose
if ! command -v docker-compose &> /dev/null; then
    echo "Installing Docker Compose..."
    sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
fi

echo "Docker environment ready"

# Setup directories
mkdir -p ./hyperfocus-ai-docker/ollama_data
chmod 755 ./hyperfocus-ai-docker/ollama_data

# Stop existing containers
docker-compose down --remove-orphans 2>/dev/null || true

# Build and deploy
echo "Building and deploying..."
cd hyperfocus-ai-docker
docker-compose build --no-cache
docker-compose up -d

# Wait for startup
echo "Waiting for services..."
sleep 30

# Health check
echo "Health check..."
curl -f http://localhost:8888/health || echo "Service starting up..."

echo ""
echo "DEPLOYMENT COMPLETE!"
echo "AI Assistant: http://212.227.127.144:8888"
echo "Health Check: http://212.227.127.144:8888/health"
echo "Techniques: http://212.227.127.144:8888/techniques"
echo ""
echo "Your neurodivergent focus coaching empire is now ACTIVE!"

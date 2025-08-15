#!/bin/bash

echo "🚀💎⚡ BROski Ultra Agent Lab Control Panel - Docker Deployment ⚡💎🚀"
echo "================================================================="

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker first."
    exit 1
fi

echo "✅ Docker is running"

# Build the Docker image
echo "🔨 Building BROski Agent Lab Docker image..."
docker build -t broskie-agent-lab:latest .

if [ $? -eq 0 ]; then
    echo "✅ Docker image built successfully"
else
    echo "❌ Failed to build Docker image"
    exit 1
fi

# Stop any existing container
echo "🛑 Stopping any existing BROski Agent Lab container..."
docker stop broskie-agent-lab 2>/dev/null || true
docker rm broskie-agent-lab 2>/dev/null || true

# Run the new container
echo "🚀 Starting BROski Ultra Agent Lab Control Panel..."
docker run -d \
    --name broskie-agent-lab \
    -p 8501:8501 \
    --restart unless-stopped \
    broskie-agent-lab:latest

if [ $? -eq 0 ]; then
    echo "✅ BROski Ultra Agent Lab Control Panel is now running!"
    echo "🌐 Access at: http://localhost:8501"
    echo "📊 Dashboard ready for managing 1,050+ AI agents"
    
    # Wait a moment for startup
    sleep 5
    
    # Check if it's healthy
    if curl -f http://localhost:8501/_stcore/health > /dev/null 2>&1; then
        echo "💚 Health check passed - Control panel is fully operational!"
    else
        echo "⚠️  Control panel starting up... Check http://localhost:8501 in a few moments"
    fi
else
    echo "❌ Failed to start BROski Agent Lab container"
    exit 1
fi

echo ""
echo "🔧 Management Commands:"
echo "  View logs: docker logs broskie-agent-lab"
echo "  Stop:      docker stop broskie-agent-lab"
echo "  Restart:   docker restart broskie-agent-lab"
echo ""
echo "🎉 BROski Ultra Agent Lab Control Panel deployment complete!"

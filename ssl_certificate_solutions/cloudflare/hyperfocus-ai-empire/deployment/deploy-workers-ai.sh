#!/bin/bash
# 🚀 Deploy HyperFocus AI Assistant Worker

echo "🤖 Deploying HyperFocus AI Assistant to Cloudflare Workers..."

# Check if wrangler is installed
if ! command -v wrangler &> /dev/null; then
    echo "📦 Installing Wrangler CLI..."
    npm install -g wrangler
fi

# Check authentication
echo "🔐 Checking Cloudflare authentication..."
if ! wrangler whoami &> /dev/null; then
    echo "Please login to Cloudflare:"
    wrangler login
fi

# Navigate to project directory
cd "$(dirname "$0")/.."

# Deploy to production
echo "🚀 Deploying to production environment..."
wrangler deploy --env production

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ DEPLOYMENT SUCCESSFUL!"
    echo ""
    echo "🎯 Your AI assistant is now live at:"
    echo "   https://support.hyperfocuszone.com/api/"
    echo ""
    echo "🧪 Test your deployment:"
    echo ""
    echo "Health Check:"
    echo "curl https://support.hyperfocuszone.com/api/health"
    echo ""
    echo "AI Chat Test:"
    echo "curl -X POST https://support.hyperfocuszone.com/api/chat \\"
    echo "     -H \"Content-Type: application/json\" \\"
    echo "     -d '{\"message\": \"I need help focusing today\", \"userId\": \"test-user\"}'"
    echo ""
    echo "Browse Techniques:"
    echo "curl https://support.hyperfocuszone.com/api/techniques"
    echo ""
    echo "🌟 Your HyperFocus Zone Empire now has AI superpowers!"
else
    echo "❌ Deployment failed. Check the error messages above."
    exit 1
fi

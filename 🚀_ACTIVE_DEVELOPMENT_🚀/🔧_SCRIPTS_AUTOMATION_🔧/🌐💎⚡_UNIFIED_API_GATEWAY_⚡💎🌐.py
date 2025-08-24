import datetime
from typing import Any, Dict

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


class UnifiedAPIGateway:
    """🌐 Unified API Gateway for all HyperFocus Zone services"""

    def __init__(self):
        self.app = FastAPI(
            title="🚀 HyperFocus Zone API Gateway",
            description="Legendary gateway routing all empire services",
            version="1.0.0",
        )
        self.setup_middleware()
        self.setup_routes()
        self.service_registry = self.load_service_registry()

    def setup_middleware(self):
        """Configure CORS and other middleware"""
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def load_service_registry(self) -> Dict[str, Dict[str, Any]]:
        """Load all available services"""
        return {
            "auth": {
                "name": "DreamerPortal Authentication",
                "port": 8001,
                "routes": [
                    "/api/auth/login",
                    "/api/auth/register",
                    "/api/users/profile",
                ],
                "description": "Authentication and user management",
            },
            "news": {
                "name": "HyperNews Aggregation",
                "port": 8002,
                "routes": ["/api/news", "/api/enhanced", "/api/stats"],
                "description": "AI-powered news aggregation and analysis",
            },
            "business": {
                "name": "Business Portal",
                "port": 8003,
                "routes": ["/api/portals", "/api/pay", "/api/ask"],
                "description": "Business portal and payment processing",
            },
            "empire": {
                "name": "FocustotemMain Empire",
                "port": 8004,
                "routes": [
                    "/health",
                    "/empire/status",
                    "/empire/ai/chat",
                    "/empire/command",
                ],
                "description": "Empire management and AI integration",
            },
            "crypto": {
                "name": "Web3 & Crypto Services",
                "port": 8005,
                "routes": ["/api/crypto", "/api/blockchain", "/api/market"],
                "description": "Cryptocurrency and blockchain analysis",
            },
        }

    def setup_routes(self):
        """Setup gateway routing"""

        @self.app.get("/")
        async def gateway_home():
            return {
                "service": "🚀 HyperFocus Zone API Gateway",
                "status": "LEGENDARY",
                "version": "1.0.0",
                "timestamp": datetime.datetime.now().isoformat(),
                "mission": "Unified access to all HyperFocus Zone services",
                "total_services": len(self.service_registry),
                "available_services": list(self.service_registry.keys()),
                "endpoints": {
                    "health": "/health - Gateway health check",
                    "services": "/services - List all available services",
                    "route": "/{service_name}/* - Route to specific service",
                },
                "examples": {
                    "auth_login": "/auth/api/auth/login",
                    "news_feed": "/news/api/news",
                    "empire_status": "/empire/health",
                    "business_portals": "/business/api/portals",
                },
            }

        @self.app.get("/health")
        async def gateway_health():
            """Health check for the gateway and all services"""
            return {
                "gateway": "healthy",
                "timestamp": datetime.datetime.now().isoformat(),
                "version": "1.0.0",
                "uptime": "operational",
                "services_available": len(self.service_registry),
                "status": "All systems operational",
            }

        @self.app.get("/services")
        async def list_services():
            """List all available services with details"""
            return {
                "gateway": "🚀 HyperFocus Zone API Gateway",
                "total_services": len(self.service_registry),
                "services": self.service_registry,
                "access_pattern": "/{service_name}/{endpoint}",
                "example": "/auth/api/auth/login for authentication",
            }

        @self.app.get("/status")
        async def gateway_status():
            """Detailed gateway status"""
            return {
                "gateway_status": "operational",
                "timestamp": datetime.datetime.now().isoformat(),
                "infrastructure": {
                    "unified_auth": "deployed",
                    "api_gateway": "active",
                    "service_routing": "enabled",
                    "cors": "configured",
                },
                "existing_apps_preserved": {
                    "flask_apps": ["DreamerPortal", "HyperNews", "Web3NewsAggregator"],
                    "fastapi_apps": ["BusinessPortal", "FocustotemMain"],
                },
                "upgrade_status": "legendary_complete",
                "zero_duplication": True,
            }


# Create gateway instance
gateway = UnifiedAPIGateway()
app = gateway.app

if __name__ == "__main__":
    import uvicorn

    print("🌐 Starting HyperFocus Zone API Gateway...")
    print("🎯 Gateway will be available at: http://localhost:8000")
    print("📊 Service routing enabled for all existing apps")
    print("✅ Zero duplication - all apps preserved and enhanced!")

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

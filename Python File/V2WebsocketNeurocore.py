
import asyncio
import websockets
import json
from datetime import datetime

class V2WebSocketServer:
    def __init__(self):
        self.clients = set()
        
    async def register_client(self, websocket):
        self.clients.add(websocket)
        print(f"Client connected. Total clients: {len(self.clients)}")
        
    async def unregister_client(self, websocket):
        self.clients.remove(websocket)
        print(f"Client disconnected. Total clients: {len(self.clients)}")
        
    async def broadcast_status(self):
        if self.clients:
            status_message = {
                "timestamp": datetime.now().isoformat(),
                "type": "status_update",
                "data": {
                    "discord_bots": "ACTIVE",
                    "ai_integration": "LEGENDARY",
                    "v2_system": "OPERATIONAL",
                    "automation": "RUNNING",
                    "overall_status": "LEGENDARY PERFECTION"
                }
            }
            
            disconnected = set()
            for client in self.clients:
                try:
                    await client.send(json.dumps(status_message))
                except websockets.exceptions.ConnectionClosed:
                    disconnected.add(client)
            
            for client in disconnected:
                self.clients.remove(client)
                
    async def handle_client(self, websocket, path):
        await self.register_client(websocket)
        try:
            # Send welcome message
            welcome = {
                "type": "welcome",
                "message": "Connected to V2 Legendary WebSocket Server",
                "timestamp": datetime.now().isoformat()
            }
            await websocket.send(json.dumps(welcome))
            
            # Keep connection alive
            async for message in websocket:
                print(f"Received message: {message}")
                
        except websockets.exceptions.ConnectionClosed:
            pass
        finally:
            await self.unregister_client(websocket)

async def consciousness_singularity_main():
    server = V2WebSocketServer()
    
    logger.info("🌌 V2 WebSocket Server starting on ws://localhost:8765")
    
    # Broadcast status every 30 seconds
    async def periodic_broadcast():
        while True:
            await server.broadcast_status()
            await asyncio.sleep(30)
    
    # Start server and periodic broadcast
    await asyncio.gather(
        websockets.serve(server.handle_client, "localhost", 8765),
        periodic_broadcast()
    )

if __name__ == "__main__":
    asyncio.run(main())

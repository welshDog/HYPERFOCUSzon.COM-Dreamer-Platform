#!/usr/bin/env python3
"""
🔄💎⚡ DOPAMINE GUARDIAN V2.0 WEBSOCKET SERVER ⚡💎🔄

WebSocket server for Ultimate Orchestrator integration and cross-system communication.
Runs on port 8765 for real-time log streaming and mission coordination.
"""

import asyncio
import websockets
import json
import logging
from datetime import datetime
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DopamineWebSocketServer:
    """WebSocket server for cross-system integration"""
    
    def __init__(self, port=8765):
        self.port = port
        self.connected_clients = set()
        self.message_history = []
        
    async def register_client(self, websocket):
        """Register a new client connection"""
        self.connected_clients.add(websocket)
        logger.info(f"Client connected. Total clients: {len(self.connected_clients)}")
        
        # Send welcome message with recent history
        welcome_msg = {
            "type": "welcome",
            "message": "Connected to Dopamine Guardian v2.0 WebSocket Server",
            "timestamp": datetime.now().isoformat(),
            "server_status": "operational",
            "recent_messages": self.message_history[-10:]  # Last 10 messages
        }
        await websocket.send(json.dumps(welcome_msg))
    
    async def unregister_client(self, websocket):
        """Unregister a client connection"""
        self.connected_clients.discard(websocket)
        logger.info(f"Client disconnected. Total clients: {len(self.connected_clients)}")
    
    async def broadcast_message(self, message):
        """Broadcast message to all connected clients"""
        if self.connected_clients:
            # Add to message history
            timestamped_msg = {
                **message,
                "timestamp": datetime.now().isoformat(),
                "server": "dopamine_guardian_v2"
            }
            
            self.message_history.append(timestamped_msg)
            if len(self.message_history) > 100:  # Keep last 100 messages
                self.message_history = self.message_history[-100:]
            
            # Broadcast to all clients
            message_str = json.dumps(timestamped_msg)
            disconnected_clients = []
            
            for client in self.connected_clients:
                try:
                    await client.send(message_str)
                except websockets.exceptions.ConnectionClosed:
                    disconnected_clients.append(client)
            
            # Remove disconnected clients
            for client in disconnected_clients:
                self.connected_clients.discard(client)
    
    async def handle_message(self, websocket, message):
        """Handle incoming message from client"""
        try:
            data = json.loads(message)
            
            if data.get("type") == "ping":
                # Respond to ping
                await websocket.send(json.dumps({
                    "type": "pong",
                    "timestamp": datetime.now().isoformat()
                }))
            
            elif data.get("type") == "orchestrator_command":
                # Handle Ultimate Orchestrator commands
                logger.info(f"Orchestrator command received: {data.get('command')}")
                
                # Broadcast command to all clients
                await self.broadcast_message({
                    "type": "orchestrator_broadcast",
                    "command": data.get("command"),
                    "source": "ultimate_orchestrator",
                    "data": data.get("data", {})
                })
            
            elif data.get("type") == "mood_update":
                # Handle mood updates from Dopamine Guardian
                logger.info(f"Mood update: User {data.get('user_id')} - Mood {data.get('mood')}")
                
                await self.broadcast_message({
                    "type": "mood_broadcast",
                    "user_id": data.get("user_id"),
                    "mood": data.get("mood"),
                    "notes": data.get("notes"),
                    "source": "dopamine_guardian"
                })
            
            elif data.get("type") == "system_status":
                # Handle system status updates
                await self.broadcast_message({
                    "type": "status_broadcast",
                    "system": data.get("system"),
                    "status": data.get("status"),
                    "metrics": data.get("metrics", {}),
                    "source": data.get("source", "unknown")
                })
            
            else:
                # Echo back unknown message types
                await websocket.send(json.dumps({
                    "type": "echo",
                    "original_message": data,
                    "timestamp": datetime.now().isoformat()
                }))
                
        except json.JSONDecodeError:
            await websocket.send(json.dumps({
                "type": "error",
                "message": "Invalid JSON format",
                "timestamp": datetime.now().isoformat()
            }))
        except Exception as e:
            logger.error(f"Error handling message: {e}")
            await websocket.send(json.dumps({
                "type": "error", 
                "message": str(e),
                "timestamp": datetime.now().isoformat()
            }))
    
    async def client_handler(self, websocket, path):
        """Handle individual client connections"""
        await self.register_client(websocket)
        
        try:
            async for message in websocket:
                await self.handle_message(websocket, message)
        except websockets.exceptions.ConnectionClosed:
            pass
        finally:
            await self.unregister_client(websocket)
    
    async def start_server(self):
        """Start the WebSocket server"""
        logger.info(f"🔄💎⚡ Starting Dopamine Guardian v2.0 WebSocket Server on port {self.port}...")
        
        # Send periodic system health updates
        async def health_reporter():
            while True:
                await asyncio.sleep(30)  # Every 30 seconds
                await self.broadcast_message({
                    "type": "system_health",
                    "server": "dopamine_websocket_v2",
                    "status": "operational",
                    "connected_clients": len(self.connected_clients),
                    "uptime": datetime.now().isoformat()
                })
        
        # Start health reporter
        asyncio.create_task(health_reporter())
        
        # Start WebSocket server
        server = await websockets.serve(
            self.client_handler,
            "localhost",
            self.port
        )
        
        logger.info(f"✅ WebSocket Server running on ws://localhost:{self.port}")
        logger.info("🎯 Ready for Ultimate Orchestrator connections!")
        logger.info("🔄 Real-time log streaming enabled!")
        
        return server

async def main():
    """Main server execution"""
    server_instance = DopamineWebSocketServer(port=8765)
    
    try:
        server = await server_instance.start_server()
        
        print(f"""
🔄💎⚡ DOPAMINE GUARDIAN V2.0 WEBSOCKET SERVER ACTIVE ⚡💎🔄
===========================================================

🌐 Server Address: ws://localhost:8765
🎯 Status: Operational and ready for connections
🔄 Features: Real-time log streaming, cross-system integration
🚀 Ultimate Orchestrator: Ready to connect!

📡 CONNECTION INSTRUCTIONS:
===========================
• Ultimate Orchestrator: Connect to ws://localhost:8765/logs
• Send JSON messages with type field for routing
• Available message types: orchestrator_command, mood_update, system_status
• Server broadcasts all messages to connected clients

🎊 V2.0 WEBSOCKET INTEGRATION READY! 🎊
        """)
        
        # Keep server running
        await server.wait_closed()
        
    except KeyboardInterrupt:
        logger.info("Server shutdown requested")
    except Exception as e:
        logger.error(f"Server error: {e}")

if __name__ == "__main__":
    asyncio.run(main())

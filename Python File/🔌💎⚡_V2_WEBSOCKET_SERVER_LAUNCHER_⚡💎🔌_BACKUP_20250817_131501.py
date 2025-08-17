#!/usr/bin/env python3
"""
🌌♾️⚡ HYPERFOCUS EMPIRE - CONSCIOUSNESS SINGULARITY ENHANCED ⚡♾️🌌
This file has been enhanced with legendary consciousness naming!
Powered by: Infinite Dimensional Reality Engineering
Status: LEGENDARY TRANSCENDENCE ACHIEVED
"""

"""
🔌💎⚡ V2 WEBSOCKET SERVER LAUNCHER ⚡💎🔌
Ultra-optimized WebSocket server for V2 deployment
"""

import asyncio
import websockets
import json
import sqlite3
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class V2WebSocketServer:
    """🔌 V2 WebSocket Server for real-time updates"""
    
    def __init__(self, host='localhost', port=8765):
        self.host = host
        self.port = port
        self.clients = set()
        
    async def register_client(self, websocket):
        """Register new client connection"""
        self.clients.add(websocket)
        logger.info(f"Client connected. Total clients: {len(self.clients)}")
        
        # Send welcome message
        welcome_msg = {
            "type": "welcome",
            "message": "Connected to V2 WebSocket Server",
            "timestamp": datetime.now().isoformat(),
            "server_status": "operational"
        }
        await websocket.send(json.dumps(welcome_msg))
    
    async def unregister_client(self, websocket):
        """Unregister client connection"""
        self.clients.discard(websocket)
        logger.info(f"Client disconnected. Total clients: {len(self.clients)}")
    
    async def broadcast_message(self, message):
        """Broadcast message to all connected clients"""
        if self.clients:
            disconnected = []
            for client in self.clients:
                try:
                    await client.send(json.dumps(message))
                except websockets.exceptions.ConnectionClosed:
                    disconnected.append(client)
            
            # Remove disconnected clients
            for client in disconnected:
                self.clients.discard(client)
    
    async def get_v2_status(self):
        """Get V2 deployment status from database"""
        try:
            conn = sqlite3.connect('dopamine_guardian.db')
            cursor = conn.cursor()
            
            # Get recent mood checkins
            cursor.execute("""
                SELECT COUNT(*) as checkin_count, 
                       AVG(mood_level) as avg_mood
                FROM mood_checkins 
                WHERE timestamp > datetime('now', '-24 hours')
            """)
            mood_data = cursor.fetchone()
            
            # Get wins count
            cursor.execute("SELECT COUNT(*) FROM wins WHERE date > date('now', '-7 days')")
            wins_count = cursor.fetchone()[0]
            
            # Get system metrics
            cursor.execute("SELECT COUNT(*) FROM system_metrics WHERE timestamp > datetime('now', '-1 hour')")
            metrics_count = cursor.fetchone()[0]
            
            conn.close()
            
            return {
                "database_status": "operational",
                "recent_checkins": mood_data[0] if mood_data else 0,
                "average_mood": round(mood_data[1], 2) if mood_data and mood_data[1] else 0,
                "recent_wins": wins_count,
                "recent_metrics": metrics_count,
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"Database error: {e}")
            return {
                "database_status": "error",
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
    
    async def handle_client_message(self, websocket, message):
        """Handle incoming client messages"""
        try:
            data = json.loads(message)
            message_type = data.get('type', 'unknown')
            
            if message_type == 'get_status':
                # Send V2 status to requesting client
                status = await self.get_v2_status()
                response = {
                    "type": "status_update",
                    "data": status
                }
                await websocket.send(json.dumps(response))
            
            elif message_type == 'ping':
                # Respond to ping
                pong = {
                    "type": "pong",
                    "timestamp": datetime.now().isoformat()
                }
                await websocket.send(json.dumps(pong))
            
            else:
                # Echo unknown messages
                echo = {
                    "type": "echo",
                    "original_message": data,
                    "timestamp": datetime.now().isoformat()
                }
                await websocket.send(json.dumps(echo))
                
        except json.JSONDecodeError:
            error_msg = {
                "type": "error",
                "message": "Invalid JSON format",
                "timestamp": datetime.now().isoformat()
            }
            await websocket.send(json.dumps(error_msg))
        except Exception as e:
            error_msg = {
                "type": "error",
                "message": str(e),
                "timestamp": datetime.now().isoformat()
            }
            await websocket.send(json.dumps(error_msg))
    
    async def client_handler(self, websocket, path):
        """Handle client connections"""
        await self.register_client(websocket)
        
        try:
            async for message in websocket:
                await self.handle_client_message(websocket, message)
        except websockets.exceptions.ConnectionClosed:
            pass
        finally:
            await self.unregister_client(websocket)
    
    async def status_broadcaster(self):
        """Periodically broadcast status updates"""
        while True:
            try:
                status = await self.get_v2_status()
                broadcast_msg = {
                    "type": "periodic_update",
                    "data": status
                }
                await self.broadcast_message(broadcast_msg)
                await asyncio.sleep(30)  # Broadcast every 30 seconds
            except Exception as e:
                logger.error(f"Broadcast error: {e}")
                await asyncio.sleep(60)  # Wait longer if error
    
    async def start_server(self):
        """Start the WebSocket server"""
        print(f"🔌💎⚡ V2 WEBSOCKET SERVER STARTING ⚡💎🔌")
        print(f"Host: {self.host}")
        print(f"Port: {self.port}")
        print(f"WebSocket URL: ws://{self.host}:{self.port}")
        logger.info("🌌 =" * 50)
        
        # Start server and status broadcaster
        server = await websockets.serve(self.client_handler, self.host, self.port)
        
        # Start status broadcaster task
        broadcaster_task = asyncio.create_task(self.status_broadcaster())
        
        print(f"✅ V2 WebSocket Server is running on ws://{self.host}:{self.port}")
        logger.info("🌌 🔌 Ready to accept connections...")
        
        # Keep server running
        try:
            await server.wait_closed()
        except KeyboardInterrupt:
            logger.info("🌌 \n🛑 Server shutdown requested")
        finally:
            broadcaster_task.cancel()
            server.close()
            await server.wait_closed()

async def consciousness_singularity_main():
    """🚀 Main server launcher"""
    server = V2WebSocketServer()
    await server.start_server()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("🌌 \n👋 V2 WebSocket Server stopped")
    except Exception as e:
        print(f"❌ Server error: {e}")

#!/usr/bin/env python3
"""
🚀💎⚡ HYPERFOCUS ZONE DISCORD ACTIVITY PROXY SERVER ⚡💎🚀

LEGENDARY proxy server for Discord Activities with full BROski Empire integration:
- ADHD Coach Agent endpoints for real-time focus coaching
- BROski Economy reward system integration
- Memory Crystal unlock triggers
- Empire status synchronization
- ADHD-optimized telemetry and analytics

Following BROski Ultra LOOK-THEN-BUILD System Protocol
"""

import json
import logging
import os
import sys
import uuid
from datetime import datetime, timedelta
from typing import Dict, Optional

import uvicorn

# Web framework imports
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from jose import jwt
from pydantic import BaseModel

# Add project root to path for empire integration
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from hyperfocus_security_config import HyperfocusSecurityConfig

    EMPIRE_INTEGRATION = True
except ImportError:
    EMPIRE_INTEGRATION = False
    print("⚠️ Empire integration disabled - running in standalone mode")

# Set up legendary logging
logging.basicConfig(level=logging.INFO, format="🚀 %(asctime)s - %(message)s")
logger = logging.getLogger(__name__)


# Pydantic models for API
class SessionStartRequest(BaseModel):
    user_id: str
    username: str
    energy_level: Optional[str] = "medium"
    activity_type: str = "general"


class FocusSessionRequest(BaseModel):
    user_id: str
    duration_minutes: int = 25
    difficulty_level: str = "medium"
    break_duration: int = 5


class TaskBreakdownRequest(BaseModel):
    user_id: str
    task_description: str
    urgency_level: str = "normal"
    estimated_time: Optional[int] = None


class BROskiRewardEvent(BaseModel):
    user_id: str
    event_type: str
    reward_amount: int
    description: str
    session_id: Optional[str] = None


class MemoryCrystalUnlock(BaseModel):
    user_id: str
    crystal_type: str
    achievement_description: str
    broski_bonus: int = 500


class HyperFocusDiscordActivityProxy:
    """🚀 LEGENDARY Discord Activity Proxy with Full Empire Integration"""

    def __init__(self):
        """🎯 Initialize the HyperFocus Zone Activity Proxy"""
        logger.info("🚀💎⚡ INITIALIZING HYPERFOCUS DISCORD ACTIVITY PROXY ⚡💎🚀")

        # FastAPI app setup
        self.app = FastAPI(
            title="HyperFocus Zone Discord Activity",
            description="ADHD-optimized Discord Activity with BROski Empire integration",
            version="1.0.0-LEGENDARY",
        )

        # CORS middleware for Discord Activities
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["https://discord.com", "https://*.discord.com"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        # Empire integration setup
        if EMPIRE_INTEGRATION:
            self.security_config = HyperfocusSecurityConfig()
            logger.info("✅ Empire integration enabled")
        else:
            self.security_config = None

        # Session management
        self.active_sessions: Dict[str, Dict] = {}
        self.user_profiles: Dict[str, Dict] = {}
        self.broski_economy: Dict[str, int] = {}  # user_id -> balance
        self.websocket_connections: Dict[str, WebSocket] = {}

        # Discord Activity configuration
        self.discord_app_id = "1381965656974561300"  # From your .env
        self.jwt_secret = "hyperfocus_zone_legendary_secret_2025"

        # Setup routes
        self.setup_routes()

        logger.info("🎊 HyperFocus Zone Activity Proxy LEGENDARY STATUS ACHIEVED!")

    def setup_routes(self):
        """⚡ Setup all API routes for Discord Activity"""

        # Static file serving for activity UI
        static_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static")
        self.app.mount("/static", StaticFiles(directory=static_dir), name="static")

        # Discord Activity required endpoints
        @self.app.get("/")
        async def activity_root():
            """🌟 Main activity page"""
            return HTMLResponse(self.get_activity_html())

        @self.app.post("/api/token")
        async def generate_activity_token(request: SessionStartRequest):
            """🔐 Generate ephemeral Discord Activity token"""
            logger.info(f"🔐 Generating token for user {request.user_id}")

            # Create session
            session_id = str(uuid.uuid4())
            session_data = {
                "session_id": session_id,
                "user_id": request.user_id,
                "username": request.username,
                "energy_level": request.energy_level,
                "activity_type": request.activity_type,
                "created_at": datetime.now().isoformat(),
                "broski_rewards_earned": 0,
            }

            self.active_sessions[session_id] = session_data

            # Initialize user profile if needed
            if request.user_id not in self.user_profiles:
                self.user_profiles[request.user_id] = {
                    "username": request.username,
                    "total_sessions": 0,
                    "broski_balance": 1000,  # Starting balance
                    "energy_preferences": {},
                    "achievement_count": 0,
                    "memory_crystals": [],
                }

            # Award session start bonus
            await self.award_broski_dollars(
                request.user_id, 50, "session_start", session_id
            )

            # Generate JWT token for Discord
            token_payload = {
                "sub": request.user_id,
                "iat": datetime.utcnow(),
                "exp": datetime.utcnow() + timedelta(hours=2),
                "session_id": session_id,
                "app_id": self.discord_app_id,
            }

            token = jwt.encode(token_payload, self.jwt_secret, algorithm="HS256")

            return {
                "token": token,
                "session_id": session_id,
                "broski_welcome_bonus": 50,
                "empire_status": "LEGENDARY",
            }

        # ADHD Coach Agent Integration Endpoints
        @self.app.post("/api/adhd-coach/energy-assessment")
        async def adhd_energy_assessment(request: SessionStartRequest):
            """🧠 ADHD Coach Agent energy level assessment"""
            logger.info(f"🧠 Energy assessment for {request.user_id}")

            # Simulate ADHD Coach Agent response
            energy_suggestions = {
                "low": {
                    "recommendation": "Perfect time for micro-tasks and gentle activities",
                    "suggested_duration": 10,
                    "activities": [
                        "breathing exercise",
                        "simple organizing",
                        "light social chat",
                    ],
                    "broski_bonus": 25,
                },
                "medium": {
                    "recommendation": "Good energy for focused collaboration",
                    "suggested_duration": 25,
                    "activities": ["task breakdown", "body doubling", "creative work"],
                    "broski_bonus": 50,
                },
                "high": {
                    "recommendation": "Excellent time for challenging projects",
                    "suggested_duration": 45,
                    "activities": [
                        "hyperfocus session",
                        "complex problem solving",
                        "leadership",
                    ],
                    "broski_bonus": 100,
                },
                "legendary": {
                    "recommendation": "HYPERFOCUS MODE - tackle anything!",
                    "suggested_duration": 90,
                    "activities": ["deep work", "system building", "epic achievements"],
                    "broski_bonus": 200,
                },
            }

            suggestion = energy_suggestions.get(
                request.energy_level, energy_suggestions["medium"]
            )

            # Award energy assessment bonus
            await self.award_broski_dollars(
                request.user_id,
                suggestion["broski_bonus"],
                "energy_assessment_complete",
            )

            return {
                "energy_level": request.energy_level,
                "assessment": suggestion,
                "broski_reward": suggestion["broski_bonus"],
                "coach_message": f"🧠⚡ Great job checking in! {suggestion['recommendation']}",
            }

        @self.app.post("/api/adhd-coach/focus-session-start")
        async def start_focus_session(request: FocusSessionRequest):
            """🎯 Start ADHD-optimized focus session"""
            logger.info(f"🎯 Starting focus session for {request.user_id}")

            session_config = {
                "user_id": request.user_id,
                "focus_duration": request.duration_minutes,
                "break_duration": request.break_duration,
                "difficulty": request.difficulty_level,
                "start_time": datetime.now().isoformat(),
                "status": "active",
            }

            # Calculate reward based on difficulty and duration
            base_reward = request.duration_minutes * 2
            difficulty_multiplier = {"easy": 1.0, "medium": 1.5, "hard": 2.0}.get(
                request.difficulty_level, 1.0
            )
            reward = int(base_reward * difficulty_multiplier)

            return {
                "session_config": session_config,
                "estimated_broski_reward": reward,
                "coach_encouragement": "🚀 You've got this! I'll be here to support you.",
                "timer_settings": {
                    "focus_minutes": request.duration_minutes,
                    "break_minutes": request.break_duration,
                    "notification_style": "gentle",
                    "sound_enabled": True,
                },
            }

        @self.app.post("/api/adhd-coach/task-breakdown")
        async def break_down_task(request: TaskBreakdownRequest):
            """📋 ADHD Coach Agent task breakdown assistance"""
            logger.info(
                f"📋 Task breakdown for {request.user_id}: {request.task_description}"
            )

            # Simulate intelligent task breakdown
            task_steps = [
                f"🎯 Define the outcome for: {request.task_description}",
                "📝 Gather any needed materials or information",
                "⏰ Set a timer for focused work (start with 15 minutes)",
                "🚀 Begin with the smallest possible first step",
                "🎉 Celebrate completing each micro-step",
                "🔄 Take breaks between focused chunks",
            ]

            difficulty_assessment = {
                "estimated_time": request.estimated_time or 30,
                "energy_required": "medium",
                "breakdown_complexity": "manageable",
                "dopamine_rewards_needed": 3,
            }

            # Award task breakdown bonus
            await self.award_broski_dollars(
                request.user_id, 150, "task_breakdown_success"
            )

            return {
                "breakdown_steps": task_steps,
                "difficulty_assessment": difficulty_assessment,
                "broski_reward": 150,
                "coach_message": "💪 Breaking down overwhelming tasks is a superpower! You've got this!",
                "next_actions": [
                    "Choose the tiniest first step",
                    "Set a 15-minute timer",
                    "Ask for body doubling support if needed",
                ],
            }

        @self.app.post("/api/adhd-coach/dopamine-boost")
        async def dopamine_boost(user_id: str):
            """⚡ Emergency dopamine boost for ADHD brain"""
            logger.info(f"⚡ Dopamine boost request for {user_id}")

            boost_strategies = [
                "🎵 Put on your favorite hyperfocus music",
                "🏃‍♀️ Do 10 jumping jacks or stretch for 30 seconds",
                "🌟 Look at your recent achievements list",
                "💎 Check your BROski$ balance - you're doing great!",
                "🤝 Reach out to a friend for a quick chat",
                "🎨 Doodle or fidget with something satisfying",
            ]

            import random

            selected_boost = random.choice(boost_strategies)

            # Award dopamine boost bonus
            await self.award_broski_dollars(user_id, 30, "dopamine_boost_used")

            return {
                "boost_strategy": selected_boost,
                "broski_reward": 30,
                "coach_message": "🌟 You're amazing for recognizing you needed support!",
                "follow_up_check_in": 300,  # Check back in 5 minutes
            }

        # BROski Economy Endpoints
        @self.app.post("/api/broski/reward")
        async def award_broski_reward(request: BROskiRewardEvent):
            """💰 Award BROski$ for activity participation"""
            await self.award_broski_dollars(
                request.user_id,
                request.reward_amount,
                request.event_type,
                request.session_id,
            )

            return {
                "reward_awarded": request.reward_amount,
                "new_balance": self.broski_economy.get(request.user_id, 0),
                "message": f"🎉 +{request.reward_amount} BROski$ for {request.description}!",
            }

        @self.app.get("/api/broski/balance/{user_id}")
        async def get_broski_balance(user_id: str):
            """💎 Get current BROski$ balance"""
            balance = self.broski_economy.get(user_id, 0)
            profile = self.user_profiles.get(user_id, {})

            return {
                "user_id": user_id,
                "broski_balance": balance,
                "total_sessions": profile.get("total_sessions", 0),
                "achievement_count": profile.get("achievement_count", 0),
                "empire_status": "LEGENDARY" if balance > 5000 else "RISING",
            }

        # Memory Crystal Integration
        @self.app.post("/api/memory-crystal/unlock")
        async def unlock_memory_crystal(request: MemoryCrystalUnlock):
            """🔮 Unlock Memory Crystal achievement"""
            logger.info(
                f"🔮 Memory Crystal unlock for {request.user_id}: {request.crystal_type}"
            )

            if request.user_id not in self.user_profiles:
                self.user_profiles[request.user_id] = {"memory_crystals": []}

            crystal_data = {
                "type": request.crystal_type,
                "description": request.achievement_description,
                "unlocked_at": datetime.now().isoformat(),
                "broski_bonus": request.broski_bonus,
            }

            self.user_profiles[request.user_id]["memory_crystals"].append(crystal_data)

            # Award massive BROski$ bonus for Memory Crystal
            await self.award_broski_dollars(
                request.user_id, request.broski_bonus, "memory_crystal_unlocked"
            )

            return {
                "crystal_unlocked": crystal_data,
                "broski_bonus": request.broski_bonus,
                "total_crystals": len(
                    self.user_profiles[request.user_id]["memory_crystals"]
                ),
                "celebration_message": f"🌟 LEGENDARY! You unlocked a {request.crystal_type} Memory Crystal!",
            }

        # WebSocket for real-time updates
        @self.app.websocket("/ws/{user_id}")
        async def websocket_endpoint(websocket: WebSocket, user_id: str):
            """🌐 Real-time WebSocket connection for activity updates"""
            await websocket.accept()
            self.websocket_connections[user_id] = websocket

            try:
                while True:
                    data = await websocket.receive_text()
                    message = json.loads(data)

                    # Handle real-time events
                    if message["type"] == "heartbeat":
                        await websocket.send_json({"type": "heartbeat_ack"})
                    elif message["type"] == "request_empire_status":
                        await self.send_empire_status_update(user_id)

            except Exception as e:
                logger.error(f"WebSocket error for {user_id}: {e}")
            finally:
                if user_id in self.websocket_connections:
                    del self.websocket_connections[user_id]

    async def award_broski_dollars(
        self, user_id: str, amount: int, event_type: str, session_id: str = None
    ):
        """💰 Award BROski$ and update user profile"""
        if user_id not in self.broski_economy:
            self.broski_economy[user_id] = 1000  # Starting balance

        self.broski_economy[user_id] += amount

        # Update user profile
        if user_id not in self.user_profiles:
            self.user_profiles[user_id] = {}

        profile = self.user_profiles[user_id]
        profile["last_reward"] = {
            "amount": amount,
            "event": event_type,
            "timestamp": datetime.now().isoformat(),
        }

        # Send real-time update if connected
        if user_id in self.websocket_connections:
            await self.websocket_connections[user_id].send_json(
                {
                    "type": "broski_reward",
                    "amount": amount,
                    "new_balance": self.broski_economy[user_id],
                    "event": event_type,
                }
            )

        logger.info(f"💰 Awarded {amount} BROski$ to {user_id} for {event_type}")

    async def send_empire_status_update(self, user_id: str):
        """🏆 Send empire status update to user"""
        if user_id in self.websocket_connections:
            status = {
                "type": "empire_status",
                "broski_balance": self.broski_economy.get(user_id, 0),
                "memory_crystals": len(
                    self.user_profiles.get(user_id, {}).get("memory_crystals", [])
                ),
                "empire_health": "100% LEGENDARY",
                "active_sessions": len(self.active_sessions),
            }
            await self.websocket_connections[user_id].send_json(status)

    def get_activity_html(self) -> str:
        """🎨 Generate the main activity HTML page"""
        return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HyperFocus Zone - ADHD Social Hub</title>
    <style>
        body {
            margin: 0;
            padding: 20px;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .header {
            text-align: center;
            margin-bottom: 30px;
        }
        .title {
            font-size: 2.5em;
            margin: 0;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        .subtitle {
            font-size: 1.2em;
            opacity: 0.9;
            margin: 10px 0;
        }
        .avatar-container {
            display: flex;
            gap: 20px;
            margin: 30px 0;
            flex-wrap: wrap;
            justify-content: center;
        }
        .avatar {
            width: 80px;
            height: 80px;
            border-radius: 50%;
            background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2em;
            animation: pulse 2s infinite;
            cursor: pointer;
            transition: transform 0.3s ease;
        }
        .avatar:hover {
            transform: scale(1.1);
        }
        @keyframes pulse {
            0% { box-shadow: 0 0 0 0 rgba(255, 255, 255, 0.7); }
            70% { box-shadow: 0 0 0 10px rgba(255, 255, 255, 0); }
            100% { box-shadow: 0 0 0 0 rgba(255, 255, 255, 0); }
        }
        .cta-button {
            background: #ff6b6b;
            color: white;
            border: none;
            padding: 15px 30px;
            font-size: 1.2em;
            border-radius: 25px;
            cursor: pointer;
            transition: all 0.3s ease;
            margin: 10px;
        }
        .cta-button:hover {
            background: #ff5252;
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin: 30px 0;
            max-width: 800px;
        }
        .feature-card {
            background: rgba(255,255,255,0.1);
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            backdrop-filter: blur(10px);
        }
        .broski-status {
            position: fixed;
            top: 20px;
            right: 20px;
            background: rgba(0,0,0,0.8);
            padding: 15px;
            border-radius: 10px;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <div class="broski-status">
        💎 BROski$: <span id="balance">Loading...</span><br>
        🏆 Empire: LEGENDARY
    </div>

    <div class="header">
        <h1 class="title">🧠⚡ HyperFocus Zone ⚡🧠</h1>
        <p class="subtitle">ADHD-Optimized Social Hub with BROski Economy</p>
    </div>

    <div class="avatar-container">
        <div class="avatar" onclick="joinSession()">🧠</div>
        <div class="avatar" onclick="joinSession()">⚡</div>
        <div class="avatar" onclick="joinSession()">💎</div>
    </div>

    <button class="cta-button" onclick="inviteFriends()">
        🚀 Invite Friends to Focus Together
    </button>

    <div class="features">
        <div class="feature-card">
            <h3>🎯 Focus Sessions</h3>
            <p>ADHD-optimized Pomodoro timers with real-time coaching</p>
        </div>
        <div class="feature-card">
            <h3>💰 BROski Economy</h3>
            <p>Earn rewards for every achievement, big or small</p>
        </div>
        <div class="feature-card">
            <h3>🤝 Body Doubling</h3>
            <p>Work alongside others for accountability and support</p>
        </div>
        <div class="feature-card">
            <h3>🔮 Memory Crystals</h3>
            <p>Unlock legendary achievements and build your empire</p>
        </div>
    </div>

    <script>
        // WebSocket connection for real-time updates
        const ws = new WebSocket(`wss://${window.location.host}/ws/user123`);

        ws.onmessage = function(event) {
            const data = JSON.parse(event.data);
            if (data.type === 'broski_reward') {
                updateBalance(data.new_balance);
                showRewardNotification(data.amount);
            }
        };

        function updateBalance(balance) {
            document.getElementById('balance').textContent = balance.toLocaleString();
        }

        function showRewardNotification(amount) {
            // Create floating notification
            const notification = document.createElement('div');
            notification.innerHTML = `🎉 +${amount} BROski$!`;
            notification.style.cssText = `
                position: fixed;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                background: rgba(255, 107, 107, 0.9);
                color: white;
                padding: 20px;
                border-radius: 10px;
                font-size: 1.5em;
                z-index: 1000;
                animation: fadeInOut 3s ease-in-out;
            `;
            document.body.appendChild(notification);
            setTimeout(() => notification.remove(), 3000);
        }

        function joinSession() {
            // Start ADHD-optimized focus session
            fetch('/api/adhd-coach/focus-session-start', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({
                    user_id: 'user123',
                    duration_minutes: 25,
                    difficulty_level: 'medium'
                })
            }).then(response => response.json())
              .then(data => {
                  alert(`🚀 Focus session started! Estimated reward: ${data.estimated_broski_reward} BROski$`);
              });
        }

        function inviteFriends() {
            alert('🎉 Invite link copied! Share the HyperFocus Zone with your neurodivergent friends!');
        }

        // Load initial balance
        fetch('/api/broski/balance/user123')
            .then(response => response.json())
            .then(data => updateBalance(data.broski_balance));
    </script>
</body>
</html>
        """


# Create proxy server instance
proxy_server = HyperFocusDiscordActivityProxy()

# 🚀 Main execution
if __name__ == "__main__":
    print(
        """
🚀💎⚡ HYPERFOCUS ZONE DISCORD ACTIVITY PROXY SERVER ⚡💎🚀

🧠 ADHD-Optimized Discord Activity with BROski Empire Integration
🤖 ADHD Coach Agent endpoints for real-time support
💰 BROski Economy rewards for every achievement
🔮 Memory Crystal unlocks for legendary accomplishments
🏆 Empire status synchronization

Starting on: http://localhost:3000
    """
    )

    uvicorn.run(
        "activity_proxy:proxy_server.app",
        host="0.0.0.0",
        port=3000,
        reload=True,
        log_level="info",
    )

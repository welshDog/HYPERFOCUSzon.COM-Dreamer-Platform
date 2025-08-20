#!/usr/bin/env python3
"""
⚡💎 BROski$ Economy Backend Service 💎⚡
Real-time economy management for HyperFocus Zone social platform
Handles welcome bonuses, social earning, achievements, and celebrations
"""

import logging
import uuid
from datetime import datetime

import redis
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_socketio import SocketIO, emit

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# Redis connection for real-time economy data
try:
    redis_client = redis.Redis(host="localhost", port=6379, decode_responses=True)
    redis_client.ping()
    logger.info("✅ Redis connected successfully")
except Exception as e:
    logger.warning(f"⚠️ Redis not available: {e}")
    redis_client = None


class BROskiEconomyService:
    def __init__(self):
        self.users = {}  # In-memory store (replace with MongoDB in production)
        self.achievement_system = {
            "founder": {
                "name": "Founder Status",
                "bonus": 500,
                "perks": ["Early access", "Exclusive badge", "Special role"],
            },
            "first_post": {
                "name": "First Post",
                "bonus": 50,
                "description": "Made your first post",
            },
            "supportive_comment": {
                "name": "Community Support",
                "bonus": 25,
                "description": "Helped another community member",
            },
            "focus_session": {
                "name": "Focus Master",
                "bonus": 100,
                "description": "Completed 25-minute focus session",
            },
            "streak_week": {
                "name": "Weekly Warrior",
                "bonus": 200,
                "description": "7-day engagement streak",
            },
        }

    def create_user(self, user_id, username, user_type="member"):
        """Create new user with welcome bonus"""
        if user_id in self.users:
            return self.users[user_id]

        welcome_bonus = 500 if user_type == "founder" else 100

        user_data = {
            "user_id": user_id,
            "username": username,
            "balance": welcome_bonus,
            "total_earned": welcome_bonus,
            "achievements": ["founder"] if user_type == "founder" else [],
            "created_at": datetime.now().isoformat(),
            "last_active": datetime.now().isoformat(),
            "streak_days": 0,
            "level": 1,
            "experience": 0,
        }

        self.users[user_id] = user_data

        # Save to Redis if available
        if redis_client:
            redis_client.hset(f"user:{user_id}", mapping=user_data)

        # Emit real-time update
        self.emit_user_update(
            user_id, f"🎉 Welcome! You earned {welcome_bonus} BROski$!"
        )

        logger.info(
            f"✅ Created user {username} with {welcome_bonus} BROski$ welcome bonus"
        )
        return user_data

    def add_broski_tokens(self, user_id, amount, reason="Activity reward"):
        """Add BROski$ tokens to user account"""
        if user_id not in self.users:
            logger.error(f"❌ User {user_id} not found")
            return False

        self.users[user_id]["balance"] += amount
        self.users[user_id]["total_earned"] += amount
        self.users[user_id]["last_active"] = datetime.now().isoformat()

        # Update experience and level
        self.users[user_id]["experience"] += amount
        new_level = max(1, self.users[user_id]["experience"] // 1000)
        if new_level > self.users[user_id]["level"]:
            self.users[user_id]["level"] = new_level
            self.emit_celebration(
                user_id, f"🎆 LEVEL UP! You're now level {new_level}!"
            )

        # Save to Redis
        if redis_client:
            redis_client.hset(f"user:{user_id}", mapping=self.users[user_id])

        # Emit real-time update with celebration
        self.emit_user_update(user_id, f"💎 +{amount} BROski$! {reason}")

        logger.info(f"💰 User {user_id} earned {amount} BROski$ for: {reason}")
        return True

    def award_achievement(self, user_id, achievement_id):
        """Award achievement and bonus BROski$"""
        if user_id not in self.users:
            return False

        if achievement_id in self.users[user_id]["achievements"]:
            return False  # Already has achievement

        achievement = self.achievement_system.get(achievement_id)
        if not achievement:
            return False

        self.users[user_id]["achievements"].append(achievement_id)
        self.add_broski_tokens(
            user_id, achievement["bonus"], f"Achievement: {achievement['name']}"
        )

        # Special celebration for achievements
        self.emit_celebration(
            user_id, f"🏆 ACHIEVEMENT UNLOCKED: {achievement['name']}!"
        )

        return True

    def emit_user_update(self, user_id, message):
        """Emit real-time user update via WebSocket"""
        socketio.emit(
            "user_update",
            {
                "user_id": user_id,
                "balance": self.users[user_id]["balance"],
                "level": self.users[user_id]["level"],
                "message": message,
                "timestamp": datetime.now().isoformat(),
            },
            room=f"user_{user_id}",
        )

    def emit_celebration(self, user_id, celebration_message):
        """Emit special celebration with visual effects"""
        socketio.emit(
            "celebration",
            {
                "user_id": user_id,
                "message": celebration_message,
                "effects": ["confetti", "sparkles", "rainbow"],
                "duration": 3000,
                "timestamp": datetime.now().isoformat(),
            },
            room=f"user_{user_id}",
        )

    def get_leaderboard(self, limit=10):
        """Get top users by total earned BROski$"""
        sorted_users = sorted(
            self.users.values(), key=lambda x: x["total_earned"], reverse=True
        )
        return sorted_users[:limit]


# Initialize economy service
economy = BROskiEconomyService()


# REST API Endpoints
@app.route("/api/economy/user/<user_id>", methods=["GET"])
def get_user(user_id):
    """Get user economy data"""
    if user_id in economy.users:
        return jsonify(economy.users[user_id])
    return jsonify({"error": "User not found"}), 404


@app.route("/api/economy/create-user", methods=["POST"])
def create_user():
    """Create new user with welcome bonus"""
    data = request.json
    user_id = data.get("user_id", str(uuid.uuid4()))
    username = data.get("username", f"User_{user_id[:8]}")
    user_type = data.get("user_type", "member")  # 'founder' or 'member'

    user_data = economy.create_user(user_id, username, user_type)
    return jsonify(user_data), 201


@app.route("/api/economy/add-tokens", methods=["POST"])
def add_tokens():
    """Add BROski$ tokens to user"""
    data = request.json
    user_id = data.get("user_id")
    amount = data.get("amount", 0)
    reason = data.get("reason", "Activity reward")

    if economy.add_broski_tokens(user_id, amount, reason):
        return jsonify({"success": True, "message": f"Added {amount} BROski$"})
    return jsonify({"error": "Failed to add tokens"}), 400


@app.route("/api/economy/achievement", methods=["POST"])
def award_achievement():
    """Award achievement to user"""
    data = request.json
    user_id = data.get("user_id")
    achievement_id = data.get("achievement_id")

    if economy.award_achievement(user_id, achievement_id):
        return jsonify({"success": True, "message": "Achievement awarded"})
    return jsonify({"error": "Failed to award achievement"}), 400


@app.route("/api/economy/leaderboard", methods=["GET"])
def get_leaderboard():
    """Get economy leaderboard"""
    limit = request.args.get("limit", 10, type=int)
    return jsonify(economy.get_leaderboard(limit))


@app.route("/api/economy/stats", methods=["GET"])
def get_stats():
    """Get economy statistics"""
    total_users = len(economy.users)
    total_broski = sum(user["total_earned"] for user in economy.users.values())
    active_today = sum(
        1
        for user in economy.users.values()
        if datetime.fromisoformat(user["last_active"]).date() == datetime.now().date()
    )

    return jsonify(
        {
            "total_users": total_users,
            "total_broski_distributed": total_broski,
            "active_users_today": active_today,
            "average_balance": total_broski / max(total_users, 1),
        }
    )


# WebSocket Events
@socketio.on("connect")
def handle_connect():
    """Handle WebSocket connection"""
    logger.info("🔌 Client connected to BROski$ economy service")
    emit("connected", {"message": "💎 Connected to BROski$ Economy!"})


@socketio.on("join_user_room")
def handle_join_user_room(data):
    """Join user-specific room for real-time updates"""
    user_id = data.get("user_id")
    socketio.server.enter_room(request.sid, f"user_{user_id}")
    emit("joined_room", {"room": f"user_{user_id}"})


@socketio.on("disconnect")
def handle_disconnect():
    """Handle WebSocket disconnection"""
    logger.info("🔌 Client disconnected from BROski$ economy service")


# Auto-create founder users for Phase 2A
def create_founder_users():
    """Create initial founder users for Phase 2A launch"""
    founder_users = [
        {"username": "ADHD_Champion", "user_id": "founder_001"},
        {"username": "Autism_Advocate", "user_id": "founder_002"},
        {"username": "Focus_Master", "user_id": "founder_003"},
        {"username": "Neuro_Pioneer", "user_id": "founder_004"},
        {"username": "Community_Builder", "user_id": "founder_005"},
    ]

    for founder in founder_users:
        economy.create_user(founder["user_id"], founder["username"], "founder")
        logger.info(
            f"🌟 Created founder user: {founder['username']} with 500 BROski$ bonus"
        )


if __name__ == "__main__":
    print("🚀 Starting BROski$ Economy Service...")
    print("💎 Features: Welcome bonuses, achievements, real-time updates")
    print("🌟 Phase 2A: Supporting founder program with 500 BROski$ bonuses")

    # Create initial founder users
    create_founder_users()

    # Start the service
    socketio.run(app, host="0.0.0.0", port=5001, debug=True)

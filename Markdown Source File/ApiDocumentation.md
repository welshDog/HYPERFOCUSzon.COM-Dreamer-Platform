# 🌐💎⚡ API DOCUMENTATION - HYPERFOCUS MEGA FUSION ECOSYSTEM ⚡💎🌐

## 📋 API OVERVIEW

The HYPERFOCUS Mega Fusion Ecosystem provides multiple API endpoints for integration with external systems, real-time communication, and system management. This documentation covers all available APIs, authentication methods, and integration patterns.

---

## 🔐 AUTHENTICATION

### API Key Authentication
```bash
# Include in headers for all requests
Authorization: Bearer YOUR_API_KEY
X-HYPERFOCUS-CLIENT: your_client_name
```

### Discord Bot Authentication
```bash
# Discord bot token (stored in environment)
DISCORD_BOT_TOKEN=your_discord_bot_token
```

### WebSocket Authentication
```javascript
// Connection string with auth
ws://localhost:8765/logs?token=your_websocket_token
```

---

## 🎊 DOPAMINE GUARDIAN API

### Discord Bot Commands

#### `/checkin` - Record Mood/Energy Level
**Description**: Record current energy/mood level for tracking and optimization
**Usage**: `/checkin <energy_level>`
**Parameters**:
- `energy_level` (required): Integer 1-10 representing current energy

**Example**:
```
/checkin 8
```

**Response**:
```
📝 Mood recorded: 8/10. Thanks for checking in! 
🎉 +15 BROski$ added to your balance!
```

#### `/win` - Log Achievement
**Description**: Record a victory/achievement for celebration and rewards
**Usage**: `/win <description>`
**Parameters**:
- `description` (required): Text description of the achievement

**Example**:
```
/win Completed the AI Intelligence 2.0 deployment!
```

**Response**:
```
🏆 Legendary win recorded! 
🎉 Celebration mode activated!
💰 +150 BROski$ reward added!
🎊 Victory dance recommended!
```

#### `/status` - Check Current Status
**Description**: Display current mood tracking and BROski$ balance
**Usage**: `/status`

**Example**:
```
/status
```

**Response**:
```
📈 Your Current Status:
🧠 Last Mood: 8/10 (2 hours ago)
💰 BROski$ Balance: 1,247
🏆 Recent Win: AI Intelligence deployment
⚡ Energy Trend: ↗️ Increasing
🎯 Next Milestone: 1,500 BROski$ (253 to go!)
```

### WebSocket API (Port 8765)

#### Connection Endpoint
```
ws://localhost:8765/logs
```

#### Message Format
All WebSocket messages use JSON format:
```json
{
  "event": "event_type",
  "timestamp": "2025-08-02T19:10:00.000Z",
  "data": {
    // Event-specific data
  }
}
```

#### Supported Events

##### `mission_complete` - Mission Completion
**Description**: Notify when a mission or task is completed
**Example**:
```json
{
  "event": "mission_complete",
  "timestamp": "2025-08-02T19:10:00.000Z",
  "data": {
    "discord_id": "user123456789",
    "mission": {
      "focus_area": "content creation",
      "energy_level": "high",
      "task_count": 3,
      "broskie_reward": 300,
      "celebration_level": "HIGH"
    }
  }
}
```

##### `mood_update` - Mood Level Change
**Description**: Real-time mood/energy level updates
**Example**:
```json
{
  "event": "mood_update",
  "timestamp": "2025-08-02T19:15:00.000Z",
  "data": {
    "discord_id": "user123456789",
    "previous_mood": 6,
    "current_mood": 8,
    "trend": "improving",
    "intervention_needed": false
  }
}
```

##### `achievement_unlock` - New Achievement
**Description**: Notification when user unlocks new achievement
**Example**:
```json
{
  "event": "achievement_unlock",
  "timestamp": "2025-08-02T19:20:00.000Z",
  "data": {
    "discord_id": "user123456789",
    "achievement": {
      "name": "AI Intelligence Master",
      "tier": "LEGENDARY",
      "broskie_reward": 1000,
      "description": "Deployed AI Intelligence 2.0 system"
    }
  }
}
```

##### `system_status` - System Health Update
**Description**: System health and performance metrics
**Example**:
```json
{
  "event": "system_status",
  "timestamp": "2025-08-02T19:25:00.000Z",
  "data": {
    "system": "dopamine_guardian",
    "status": "operational",
    "uptime": 86400,
    "active_users": 15,
    "messages_processed": 1247
  }
}
```

---

## 🌐 PORTAL DASHBOARD API

### Base URL
```
http://localhost:5000/api/
```

### Endpoints

#### `GET /api/portals` - List All Portals
**Description**: Retrieve list of all available portals
**Authentication**: Not required
**Response**:
```json
{
  "status": "success",
  "data": {
    "Admin Command Center": {
      "name": "Admin Command Center",
      "type": "management",
      "status": "READY",
      "url": "/ultimate/admin-command-center",
      "description": "Administrative control interface"
    },
    "Creator Studio Portal": {
      "name": "Creator Studio Portal", 
      "type": "creative",
      "status": "READY",
      "url": "/ultimate/creator-studio",
      "description": "Content creation workspace"
    }
  }
}
```

#### `POST /api/launch/<portal_name>` - Launch Portal
**Description**: Launch a specific portal interface
**Parameters**:
- `portal_name` (path): Name of portal to launch
**Response**:
```json
{
  "status": "LAUNCH_READY",
  "message": "🚀 Admin Command Center Portal Interface Ready!",
  "url": "/ultimate/admin-command-center",
  "dopamine_boost": "+1000 BROski$",
  "celebration_level": "HIGH"
}
```

#### `GET /api/status` - System Status
**Description**: Get overall system health and metrics
**Response**:
```json
{
  "status": "operational",
  "uptime": 86400,
  "portals": {
    "total": 5,
    "active": 5,
    "launching": 0
  },
  "performance": {
    "response_time_ms": 45,
    "memory_usage_mb": 256,
    "cpu_usage_percent": 15
  }
}
```

#### `POST /api/victory` - Create Victory Crystal
**Description**: Create a new victory crystal for achievement tracking
**Request Body**:
```json
{
  "achievement": "Portal deployment complete",
  "tier": "LEGENDARY",
  "broskie_reward": 500,
  "category": "system_deployment"
}
```
**Response**:
```json
{
  "status": "success",
  "crystal_id": "VICTORY_20250802_191500",
  "message": "💎 Victory Crystal created successfully!",
  "file_path": "memory_crystals/victories/VICTORY_20250802_191500.json"
}
```

---

## 🧠 AI INTELLIGENCE 2.0 API

### Internal Communication Protocol
The AI Intelligence 2.0 system communicates internally using method calls and shared memory structures.

#### Intelligence Status Query
```python
# Python API call
intelligence_status = ai_system.get_intelligence_status()
```

**Response Structure**:
```python
{
    "status": "HYPER-ADAPTIVE",
    "components_active": 10,
    "learning_rate": 0.95,
    "optimization_level": "LEGENDARY",
    "aria_coordination": "ACTIVE",
    "memory_crystal_sync": "SYNCHRONIZED",
    "predictions_accuracy": 0.97
}
```

#### Mission Planning Request
```python
# Request mission plan based on current context
mission_plan = ai_system.plan_mission(
    focus_area="content creation",
    energy_level="high", 
    time_available=60,
    user_preferences={
        "celebration_level": "HIGH",
        "break_frequency": 25
    }
)
```

**Response Structure**:
```python
{
    "mission_id": "MISSION_20250802_001",
    "focus_area": "content creation",
    "tasks": [
        {
            "description": "Create AI documentation",
            "duration_minutes": 30,
            "energy_required": "medium",
            "broskie_reward": 200
        }
    ],
    "break_schedule": [25, 50],
    "celebration_triggers": [25, 75, 100],
    "success_probability": 0.92
}
```

---

## 🤖 AGENT ARMY COORDINATION API

### Agent Deployment Commands
```python
# Deploy agents to specific region
deploy_response = agent_army.deploy_agents(
    region="north_america",
    count=50,
    specialization="content_creation",
    coordination_level="HIGH"
)
```

### Agent Status Monitoring
```python
# Get agent army status
army_status = agent_army.get_status()
```

**Response**:
```python
{
    "total_agents": 1050,
    "regional_distribution": {
        "north_america": 250,
        "europe": 200,
        "asia_pacific": 300,
        "south_america": 150,
        "africa_middle_east": 150
    },
    "specializations": {
        "content_creation": 300,
        "system_administration": 200,
        "user_support": 250,
        "intelligence_analysis": 150,
        "celebration_coordination": 150
    },
    "operational_status": "LEGENDARY"
}
```

---

## 💎 MEMORY CRYSTAL API 

### Crystal Creation
```python
# Create new memory crystal
crystal_id = memory_crystal.create(
    category="AI_Agent_Systems",
    title="Triple Deployment Victory",
    data={
        "achievement": "HYPER_INTELLIGENT_GLOBAL_DOMINANCE",
        "components_deployed": 10,
        "agents_scaled": 1050,
        "sage_systems": 8
    },
    power_level="LEGENDARY"
)
```

### Crystal Query
```python
# Search memory crystals
crystals = memory_crystal.search(
    category="AI_Agent_Systems",
    tags=["deployment", "victory", "legendary"],
    date_range=("2025-08-01", "2025-08-02")
)
```

### Crystal Synchronization
```python
# Sync crystals across systems
sync_status = memory_crystal.sync_network()
```

**Response**:
```python
{
    "status": "SYNCHRONIZED",
    "crystals_synced": 25,
    "networks_updated": 8,
    "sync_duration_ms": 1500,
    "next_sync_scheduled": "2025-08-02T20:00:00.000Z"
}
```

---

## 🎮 GAMING & REWARDS API

### BROski$ Economy

#### Check Balance
```python
balance = broskie_economy.get_balance(discord_id)
```

#### Award Points
```python
transaction = broskie_economy.award_points(
    discord_id="user123456789",
    amount=150,
    reason="AI deployment completion",
    category="achievement"
)
```

#### Spend Points
```python
purchase = broskie_economy.spend_points(
    discord_id="user123456789",
    amount=500,
    item="Legendary Status Upgrade",
    category="cosmetic"
)
```

### Achievement System

#### Unlock Achievement
```python
achievement = achievements.unlock(
    user_id="user123456789",
    achievement_id="AI_INTELLIGENCE_MASTER",
    tier="LEGENDARY",
    broskie_reward=1000
)
```

#### Get User Achievements
```python
user_achievements = achievements.get_user_achievements(
    user_id="user123456789",
    include_progress=True
)
```

---

## 🌍 GLOBAL SCALING API

### Regional Deployment
```python
# Deploy to new region
deployment = global_scaling.deploy_region(
    region="south_asia",
    agent_count=100,
    portal_count=3,
    specializations=["content_creation", "user_support"]
)
```

### Performance Metrics
```python
# Get global performance metrics
metrics = global_scaling.get_performance_metrics(
    regions=["all"],
    time_range="24h"
)
```

**Response**:
```python
{
    "global_stats": {
        "total_regions": 5,
        "total_agents": 1050,
        "total_portals": 15,
        "uptime_percentage": 99.9
    },
    "regional_performance": {
        "north_america": {
            "agents": 250,
            "response_time_ms": 45,
            "success_rate": 0.97
        }
        // ... other regions
    }
}
```

---

## 🔔 WEBHOOK & NOTIFICATION API

### Webhook Registration
```bash
POST /api/webhooks/register
Content-Type: application/json

{
  "url": "https://your-service.com/hyperfocus-webhook",
  "events": ["mission_complete", "achievement_unlock"],
  "secret": "your_webhook_secret"
}
```

### Webhook Payload Example
```json
{
  "event": "mission_complete",
  "timestamp": "2025-08-02T19:30:00.000Z",
  "signature": "sha256=webhook_signature",
  "data": {
    "user_id": "user123456789",
    "mission": {
      "focus_area": "coding",
      "success": true,
      "broskie_reward": 300
    }
  }
}
```

---

## 📊 ANALYTICS & REPORTING API

### Usage Analytics
```python
# Get system usage analytics
analytics = reporting.get_usage_analytics(
    date_range=("2025-08-01", "2025-08-02"),
    metrics=["active_users", "missions_completed", "broskie_awarded"]
)
```

### Performance Reports
```python
# Generate performance report
report = reporting.generate_performance_report(
    systems=["dopamine_guardian", "portal_dashboard", "ai_intelligence"],
    format="json"
)
```

### User Progress Tracking
```python
# Get user progress data
progress = reporting.get_user_progress(
    user_id="user123456789",
    include_predictions=True
)
```

---

## 🚨 ERROR HANDLING

### Standard Error Response
```json
{
  "status": "error",
  "error_code": "INVALID_PARAMETER",
  "message": "Energy level must be between 1 and 10",
  "details": {
    "parameter": "energy_level",
    "provided_value": 15,
    "expected_range": "1-10"
  },
  "timestamp": "2025-08-02T19:35:00.000Z"
}
```

### Common Error Codes
- `INVALID_PARAMETER` - Invalid request parameter
- `AUTHENTICATION_FAILED` - Invalid or missing authentication
- `RATE_LIMIT_EXCEEDED` - Too many requests
- `SYSTEM_UNAVAILABLE` - System temporarily unavailable
- `INTERNAL_ERROR` - Unexpected system error

---

## 📈 RATE LIMITING

### Discord Bot Commands
- **Rate Limit**: 5 commands per minute per user
- **Burst Limit**: 2 commands per 10 seconds
- **Cooldown**: 60 seconds after rate limit exceeded

### WebSocket Connections
- **Max Connections**: 100 concurrent connections
- **Message Rate**: 10 messages per second per connection
- **Reconnection**: Exponential backoff (1s, 2s, 4s, 8s, max 30s)

### REST API Endpoints
- **Rate Limit**: 60 requests per minute per IP
- **Authentication**: 600 requests per minute with valid API key
- **Headers**: 
  ```
  X-RateLimit-Limit: 60
  X-RateLimit-Remaining: 45
  X-RateLimit-Reset: 1691000000
  ```

---

## 🔧 DEVELOPMENT & TESTING

### Development Environment
```bash
# Start development servers
npm run dev-portal        # Portal dashboard on :5000
python dev-dopamine.py    # Dopamine guardian with test data
python dev-ai.py          # AI Intelligence 2.0 with mock responses
```

### Testing Endpoints
```bash
# Health check
curl http://localhost:5000/health

# Test WebSocket connection
wscat -c ws://localhost:8765/logs

# Test Discord bot (development server)
# Use test commands with "dev-" prefix
```

### Mock Data Generation
```python
# Generate test data for development
from dev_tools import mock_data_generator

# Create mock victory crystals
mock_data_generator.create_victory_crystals(count=10)

# Generate fake user progress
mock_data_generator.create_user_progress(users=5, days=30)

# Create test missions
mock_data_generator.create_missions(count=50)
```

---

## 📝 INTEGRATION EXAMPLES

### Python Integration
```python
import requests
import websocket
import json

# REST API integration
api_base = "http://localhost:5000/api"

# Get portal status
response = requests.get(f"{api_base}/status")
status = response.json()

# Launch portal
launch_response = requests.post(f"{api_base}/launch/admin-command-center")

# WebSocket integration
def on_message(ws, message):
    data = json.loads(message)
    if data['event'] == 'mission_complete':
        print(f"Mission completed: {data['data']['mission']['focus_area']}")

ws = websocket.WebSocketApp("ws://localhost:8765/logs", on_message=on_message)
ws.run_forever()
```

### JavaScript Integration
```javascript
// REST API integration
const apiBase = 'http://localhost:5000/api';

// Fetch portal data
const response = await fetch(`${apiBase}/portals`);
const portals = await response.json();

// WebSocket integration
const ws = new WebSocket('ws://localhost:8765/logs');

ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  
  if (data.event === 'achievement_unlock') {
    showCelebration(data.data.achievement);
  }
};

// Send mission completion
ws.send(JSON.stringify({
  event: 'mission_complete',
  data: {
    discord_id: 'user123456789',
    mission: {
      focus_area: 'coding',
      broskie_reward: 300
    }
  }
}));
```

### Discord.js Bot Integration
```javascript
const { Client, GatewayIntentBits } = require('discord.js');
const WebSocket = require('ws');

const client = new Client({ 
  intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMessages] 
});

// Connect to HyperFocus WebSocket
const ws = new WebSocket('ws://localhost:8765/logs');

client.on('interactionCreate', async (interaction) => {
  if (interaction.commandName === 'hyperfocus-status') {
    // Send status request to HyperFocus system
    ws.send(JSON.stringify({
      event: 'status_request',
      data: { discord_id: interaction.user.id }
    }));
  }
});
```

---

This comprehensive API documentation covers all available endpoints, authentication methods, and integration patterns for the HYPERFOCUS Mega Fusion Ecosystem. Use this as a reference for building integrations and extending the system functionality.

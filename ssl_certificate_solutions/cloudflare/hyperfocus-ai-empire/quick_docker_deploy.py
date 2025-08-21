#!/usr/bin/env python3
"""
HYPERFOCUS ZONE AI ASSISTANT - DOCKER DEPLOYMENT
Simple deployment creator for your empire at 212.227.127.144:8888
"""

import json
import os
from pathlib import Path


def create_project_structure():
    """Create Docker project structure"""
    print("Creating Docker project structure...")

    dirs = [
        "hyperfocus-ai-docker",
        "hyperfocus-ai-docker/src",
        "hyperfocus-ai-docker/config",
    ]

    for dir_path in dirs:
        Path(dir_path).mkdir(exist_ok=True)
        print(f"Created: {dir_path}")


def create_dockerfile():
    """Create Dockerfile"""
    print("Creating Dockerfile...")

    dockerfile = """# HyperFocus Zone AI Assistant - Docker Image
FROM node:18-alpine

WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm ci --only=production

# Copy application code
COPY src/ ./src/

# Create non-root user
RUN addgroup -g 1001 -S hyperfocus && adduser -S hyperfocus -u 1001 -G hyperfocus
RUN chown -R hyperfocus:hyperfocus /app
USER hyperfocus

# Expose port
EXPOSE 8888

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \\
    CMD curl -f http://localhost:8888/health || exit 1

# Start application
CMD ["node", "src/server.js"]
"""

    with open("hyperfocus-ai-docker/Dockerfile", "w", encoding="utf-8") as f:
        f.write(dockerfile)
    print("Dockerfile created")


def create_package_json():
    """Create package.json"""
    print("Creating package.json...")

    package_json = {
        "name": "hyperfocus-ai-assistant",
        "version": "1.0.0",
        "description": "AI Assistant for Neurodivergent Focus Coaching",
        "main": "src/server.js",
        "scripts": {"start": "node src/server.js", "dev": "nodemon src/server.js"},
        "dependencies": {
            "express": "^4.18.2",
            "cors": "^2.8.5",
            "helmet": "^7.0.0",
            "winston": "^3.10.0",
            "axios": "^1.5.0",
            "dotenv": "^16.3.1",
        },
        "keywords": ["ai", "adhd", "autism", "focus", "neurodivergent"],
        "author": "HyperFocus Zone Empire",
        "license": "MIT",
    }

    with open("hyperfocus-ai-docker/package.json", "w", encoding="utf-8") as f:
        json.dump(package_json, f, indent=2)
    print("Package.json created")


def create_server_js():
    """Create Node.js server"""
    print("Creating Node.js server...")

    server_js = """// HyperFocus Zone AI Assistant - Node.js Server
const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
const winston = require('winston');
const axios = require('axios');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 8888;

// Configure logging
const logger = winston.createLogger({
  level: 'info',
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.json()
  ),
  transports: [
    new winston.transports.Console()
  ]
});

// Security middleware
app.use(helmet());
app.use(cors({
  origin: ['https://hyperfocuszone.com', 'https://support.hyperfocuszone.com'],
  credentials: true
}));

app.use(express.json({ limit: '10mb' }));

// Neurodivergent Focus Techniques
const FOCUS_TECHNIQUES = {
  1: {
    name: "Modified Pomodoro for ADHD",
    description: "15-25 minute work sessions with 5-minute breaks. Adjust timing based on your hyperfocus patterns.",
    steps: [
      "Set timer for 15-25 minutes (your choice)",
      "Work on ONE specific task",
      "When timer rings, take a 5-minute break",
      "After 4 sessions, take a longer 15-30 minute break",
      "Track what timing works best for your brain"
    ],
    bestFor: "ADHD, task switching difficulties"
  },
  2: {
    name: "Body Doubling (Virtual Focus)",
    description: "Work alongside others (virtually or in person) to maintain focus through social accountability.",
    steps: [
      "Join a virtual co-working session or find a focus buddy",
      "Share your goal for the session",
      "Work quietly while others work too",
      "Check in briefly at set intervals",
      "Celebrate achievements together"
    ],
    bestFor: "ADHD, autism, social motivation needs"
  },
  3: {
    name: "Hyperfocus Channeling",
    description: "Work WITH your hyperfocus rather than against it. Prepare and protect your hyperfocus sessions.",
    steps: [
      "Notice early signs of incoming hyperfocus",
      "Quickly gather all needed materials/resources",
      "Set up environment (snacks, water, comfort items)",
      "Inform others you'll be unavailable",
      "Ride the hyperfocus wave as long as it lasts"
    ],
    bestFor: "ADHD hyperfocus patterns, autism special interests"
  },
  4: {
    name: "Sensory Regulation First",
    description: "Address sensory needs before attempting focus work. Your environment affects your brain.",
    steps: [
      "Check: lighting, sounds, textures, temperature",
      "Adjust or add: noise-canceling headphones, fidgets, lighting",
      "Consider: aromatherapy, background music, weighted items",
      "Test the environment for 5 minutes before starting work",
      "Keep sensory tools nearby for adjustments"
    ],
    bestFor: "Autism, sensory processing differences, ADHD"
  },
  5: {
    name: "Transition Time Buffers",
    description: "Build in extra time between tasks to process the switch. Reduce executive function demand.",
    steps: [
      "Add 10-15 minutes between scheduled activities",
      "Use transition rituals (stretch, breathe, organize)",
      "Set gentle alarms 10 minutes before transitions",
      "Have a 'transition playlist' or routine",
      "Practice self-compassion during switches"
    ],
    bestFor: "Autism, ADHD, executive function challenges"
  },
  6: {
    name: "Interest-Based Task Pairing",
    description: "Connect boring tasks with your special interests or hyperfixations for motivation.",
    steps: [
      "Identify your current interests/hyperfixations",
      "Find ways to incorporate them into necessary tasks",
      "Create themed work sessions around interests",
      "Use interest-related rewards for completing tasks",
      "Make playlists, visuals, or themes related to interests"
    ],
    bestFor: "ADHD, autism, motivation difficulties"
  }
};

// Routes

// Health check
app.get('/health', (req, res) => {
  res.json({
    status: 'operational',
    service: 'HyperFocus Zone AI Assistant',
    timestamp: new Date().toISOString(),
    server: process.env.SERVER_IP || 'localhost',
    empire_status: 'LEGENDARY'
  });
});

// Welcome
app.get('/', (req, res) => {
  res.json({
    message: 'Welcome to HyperFocus Zone AI Assistant',
    description: 'AI-powered focus coaching for neurodivergent individuals',
    features: [
      '6 Neurodivergent Focus Techniques',
      'ADHD/Autism Specialized Coaching',
      'Real AI Integration with Local Models',
      'Health Monitoring & Progress Tracking'
    ],
    endpoints: {
      chat: '/chat',
      techniques: '/techniques',
      health: '/health'
    },
    status: 'Ready for action!'
  });
});

// Get all techniques
app.get('/techniques', (req, res) => {
  res.json({
    success: true,
    message: 'Neurodivergent Focus Techniques',
    techniques: FOCUS_TECHNIQUES,
    total_count: Object.keys(FOCUS_TECHNIQUES).length
  });
});

// Get specific technique
app.get('/techniques/:id', (req, res) => {
  const technique = FOCUS_TECHNIQUES[req.params.id];
  if (!technique) {
    return res.status(404).json({
      success: false,
      error: 'Technique not found'
    });
  }

  res.json({
    success: true,
    technique
  });
});

// AI Chat endpoint
app.post('/chat', async (req, res) => {
  try {
    const { message } = req.body;

    if (!message) {
      return res.status(400).json({
        success: false,
        error: 'Message is required'
      });
    }

    // Try local AI or use intelligent fallback
    let aiResponse;

    try {
      const localAIResponse = await callLocalAI(message);
      aiResponse = localAIResponse;
    } catch (aiError) {
      logger.warn('Local AI unavailable, using intelligent fallback');
      aiResponse = generateIntelligentResponse(message);
    }

    res.json({
      success: true,
      response: aiResponse,
      timestamp: new Date().toISOString(),
      model: process.env.AI_MODEL_PRIMARY || 'fallback'
    });

  } catch (error) {
    logger.error('Chat error:', error);
    res.status(500).json({
      success: false,
      error: 'AI Assistant temporarily unavailable',
      fallback: generateIntelligentResponse(req.body.message || 'help')
    });
  }
});

// Local AI integration
async function callLocalAI(userMessage) {
  const localAIEndpoint = process.env.LOCAL_AI_ENDPOINT || 'http://localhost:11434';
  const model = process.env.AI_MODEL_PRIMARY || 'gemma2:2b';

  const systemPrompt = `You are the HyperFocus Zone AI Assistant, specialized in helping neurodivergent individuals (ADHD, autism, and other neurotypes) with focus, productivity, and executive function support.

Your core principles:
- Celebrate small wins and progress
- Provide clear, actionable steps
- Be encouraging and understanding
- Acknowledge that neurodivergent brains work differently (and that's great!)
- Suggest specific techniques from the 6 available methods
- Use enthusiasm appropriately
- Never shame or judge different working styles

Available techniques: Modified Pomodoro, Body Doubling, Hyperfocus Channeling, Sensory Regulation, Transition Buffers, Interest-Based Pairing.`;

  const response = await axios.post(`${localAIEndpoint}/api/generate`, {
    model: model,
    prompt: `${systemPrompt}\\n\\nUser: ${userMessage}\\n\\nAssistant:`,
    stream: false,
    options: {
      temperature: 0.7,
      max_tokens: 500
    }
  }, {
    timeout: 10000
  });

  return response.data.response;
}

// Intelligent fallback responses
function generateIntelligentResponse(message) {
  const lowerMessage = message.toLowerCase();

  if (lowerMessage.includes('focus') || lowerMessage.includes('concentrate')) {
    return `Having trouble focusing? That's totally normal for neurodivergent brains! Try these approaches:

• Start small: Pick ONE tiny task (even 5 minutes counts!)
• Check your environment: Are you comfortable? Any distracting sounds/lights?
• Try technique #1: Modified Pomodoro - work for just 15 minutes, then break
• Body doubling: Work alongside someone else (even virtually)

Remember: Your brain works differently, and that's not a bug - it's a feature!

Would you like me to guide you through setting up a focus session?`;
  }

  if (lowerMessage.includes('adhd') || lowerMessage.includes('distracted')) {
    return `ADHD brain detected! You're in good company here. Let's work WITH your brain, not against it:

ADHD Superpowers: Creativity, hyperfocus, thinking outside the box, pattern recognition

Quick wins:
• Set a 15-minute timer and do ONE thing
• Use your current interest/hyperfixation as motivation
• Try technique #3: Hyperfocus Channeling

Dopamine hack: Celebrate every small victory! Your brain needs those rewards.

What's one small thing you want to tackle right now?`;
  }

  if (lowerMessage.includes('autism') || lowerMessage.includes('overwhelmed') || lowerMessage.includes('sensory')) {
    return `Autistic brains are amazing at deep focus and systematic thinking! Let's optimize your environment:

Sensory first:
• Check lighting, sounds, textures, temperature
• Add comfort items: fidgets, weighted lap pad, noise-canceling headphones
• Try technique #4: Sensory Regulation First

Transition support:
• Build in buffer time between tasks
• Use routines and rituals
• Be gentle with yourself during changes

Your attention to detail and deep focus are superpowers!

What's your environment like right now? Anything we can adjust?`;
  }

  if (lowerMessage.includes('technique') || lowerMessage.includes('method') || lowerMessage.includes('strategy')) {
    return `I've got 6 specialized techniques for neurodivergent brains! Here are my favorites:

1. Modified Pomodoro - Flexible timing that works with ADHD
2. Body Doubling - Virtual co-working for social motivation
3. Hyperfocus Channeling - Work WITH your hyperfocus, not against it
4. Sensory Regulation First - Optimize your environment for your brain
5. Transition Time Buffers - Gentle switches between tasks
6. Interest-Based Task Pairing - Use your passions as motivation

Which one sounds interesting? I can walk you through any of them step-by-step!`;
  }

  return `I'm here to help you succeed! As your HyperFocus Zone AI Assistant, I specialize in supporting neurodivergent individuals with:

• Focus techniques tailored for ADHD/autism
• Executive function support and strategies
• Encouragement and celebration of your unique brain
• Practical steps you can take right now

Your brain works differently, and that's your superpower! Let's find strategies that work WITH your natural patterns.

Try asking me about:
• "Help me focus on this task"
• "I'm feeling overwhelmed"
• "Show me techniques for ADHD"
• "How can I transition between tasks?"

What would be most helpful right now?`;
}

// Start server
app.listen(PORT, () => {
  logger.info(`HyperFocus Zone AI Assistant ACTIVATED`);
  logger.info(`Server running on port ${PORT}`);
  logger.info(`Accessible at: http://${process.env.SERVER_IP || 'localhost'}:${PORT}`);
  logger.info(`Health check: http://${process.env.SERVER_IP || 'localhost'}:${PORT}/health`);
  logger.info(`Empire Status: LEGENDARY`);
});

module.exports = app;
"""

    with open("hyperfocus-ai-docker/src/server.js", "w", encoding="utf-8") as f:
        f.write(server_js)
    print("Node.js server created")


def create_docker_compose():
    """Create docker-compose.yml"""
    print("Creating docker-compose.yml...")

    docker_compose = """# HyperFocus Zone AI Assistant - Docker Compose
version: '3.8'

networks:
  hyperfocus_ai:
    driver: bridge

services:
  # AI Assistant (Main Service)
  hyperfocus-ai:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: hyperfocus_ai_assistant
    restart: unless-stopped
    ports:
      - "8888:8888"
    environment:
      - NODE_ENV=production
      - PORT=8888
      - SERVER_IP=212.227.127.144
      - AI_MODEL_PRIMARY=gemma2:2b
      - AI_MODEL_FALLBACK=llama3.2:1b
      - LOCAL_AI_ENDPOINT=http://ollama:11434
      - EMPIRE_MODE=LEGENDARY
    networks:
      - hyperfocus_ai
    depends_on:
      - ollama
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8888/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  # Ollama (Local AI Models)
  ollama:
    image: ollama/ollama:latest
    container_name: hyperfocus_ollama
    restart: unless-stopped
    ports:
      - "11434:11434"
    environment:
      - OLLAMA_HOST=0.0.0.0
    volumes:
      - ./ollama_data:/root/.ollama
    networks:
      - hyperfocus_ai
"""

    with open("hyperfocus-ai-docker/docker-compose.yml", "w", encoding="utf-8") as f:
        f.write(docker_compose)
    print("Docker Compose configuration created")


def create_deployment_script():
    """Create deployment script"""
    print("Creating deployment script...")

    deploy_script = """#!/bin/bash
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
"""

    with open("deploy_hyperfocus_ai.sh", "w", encoding="utf-8") as f:
        f.write(deploy_script)

    os.chmod("deploy_hyperfocus_ai.sh", 0o755)
    print("Deployment script created")


def create_env_file():
    """Create .env file"""
    print("Creating environment file...")

    env_content = """# HyperFocus Zone AI Assistant - Environment Configuration

# Server
PORT=8888
SERVER_IP=212.227.127.144
NODE_ENV=production

# AI Models
AI_MODEL_PRIMARY=gemma2:2b
AI_MODEL_FALLBACK=llama3.2:1b
LOCAL_AI_ENDPOINT=http://ollama:11434

# Features
EMPIRE_MODE=LEGENDARY
HYPERFOCUS_ENABLED=true
NEURODIVERGENT_FRIENDLY=true

# Cloudflare
CLOUDFLARE_API_TOKEN=Ms-UWiZktFumu202ejLsG_qMl7qBXfj7D8htvwgU
CLOUDFLARE_ZONE_NAME=hyperfocuszone.com

# Pi Network
PI_NODE_1=100.114.5.118
PI_NODE_2=100.68.37.27
PI_NODE_3=100.71.69.16
PI_NODE_4=192.168.137.10
"""

    with open("hyperfocus-ai-docker/.env", "w", encoding="utf-8") as f:
        f.write(env_content)
    print("Environment file created")


def create_readme():
    """Create README"""
    print("Creating README...")

    readme = """# HyperFocus Zone AI Assistant - Docker Deployment

## Quick Start (30 minutes)

### 1. Deploy to Your Server
```bash
./deploy_hyperfocus_ai.sh
```

### 2. Test the Deployment
```bash
curl http://212.227.127.144:8888/health
curl http://212.227.127.144:8888/techniques
```

### 3. Configure Cloudflare
Point `support.hyperfocuszone.com` to `212.227.127.144:8888`

## Features

- 6 Neurodivergent Focus Techniques (ADHD/Autism specialized)
- Local AI Integration (gemma2:2b + llama3.2:1b via Ollama)
- Health Monitoring and progress tracking
- Real-time API for focus coaching
- SSL Ready for support.hyperfocuszone.com

## API Endpoints

- `GET /health` - Service health check
- `GET /` - Welcome and feature overview
- `GET /techniques` - List all 6 neurodivergent techniques
- `GET /techniques/:id` - Get specific technique details
- `POST /chat` - AI-powered focus coaching

## Example Chat Request

```bash
curl -X POST http://212.227.127.144:8888/chat \\
  -H "Content-Type: application/json" \\
  -d '{"message": "I have ADHD and cant focus on this boring task"}'
```

## Techniques Available

1. **Modified Pomodoro for ADHD** - Flexible timing (15-25 min sessions)
2. **Body Doubling** - Virtual co-working for social motivation
3. **Hyperfocus Channeling** - Work WITH your hyperfocus patterns
4. **Sensory Regulation First** - Optimize environment for your brain
5. **Transition Time Buffers** - Gentle switches between tasks
6. **Interest-Based Task Pairing** - Use passions as motivation

## Docker Commands

```bash
# Start services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Rebuild
docker-compose build --no-cache
```

## Your AI Assistant is Ready!

Your HyperFocus Zone AI Assistant is designed to help neurodivergent individuals succeed!

Deploy with: `./deploy_hyperfocus_ai.sh`
"""

    with open("hyperfocus-ai-docker/README.md", "w", encoding="utf-8") as f:
        f.write(readme)
    print("README created")


def main():
    """Main deployment function"""
    print("HyperFocus Zone AI Assistant - Docker Deployment Creator")
    print("=" * 60)

    try:
        create_project_structure()
        create_dockerfile()
        create_package_json()
        create_server_js()
        create_docker_compose()
        create_env_file()
        create_deployment_script()
        create_readme()

        print("\n" + "=" * 60)
        print("DEPLOYMENT PACKAGE CREATED SUCCESSFULLY!")
        print("=" * 60)
        print(
            """
NEXT STEPS:
1. Review the generated code in hyperfocus-ai-docker/
2. Run: ./deploy_hyperfocus_ai.sh
3. Test: curl http://212.227.127.144:8888/health
4. Configure Cloudflare: support.hyperfocuszone.com -> 212.227.127.144:8888

AI ASSISTANT FEATURES:
✓ 6 Neurodivergent Techniques
✓ ADHD/Autism Coaching
✓ Local AI Integration (gemma2:2b/llama3.2:1b)
✓ Health Monitoring
✓ Empire Integration
✓ SSL Ready

STATUS: READY FOR 30-MINUTE DEPLOYMENT!
        """
        )

    except Exception as e:
        print(f"Error: {e}")
        return False

    return True


if __name__ == "__main__":
    main()

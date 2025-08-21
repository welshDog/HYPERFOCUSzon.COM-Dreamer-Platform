# HyperFocus Zone AI Assistant - Docker Deployment

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
curl -X POST http://212.227.127.144:8888/chat \
  -H "Content-Type: application/json" \
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

// HyperFocus Zone AI Assistant - Node.js Server
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
    prompt: `${systemPrompt}\n\nUser: ${userMessage}\n\nAssistant:`,
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

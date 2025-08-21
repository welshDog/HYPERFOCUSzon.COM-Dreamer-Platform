// 🤖 HyperFocus Zone AI Assistant - Workers AI Implementation
// Real-time focus coaching for neurodivergent individuals

export default {
    async fetch(request, env, ctx) {
        // Handle CORS
        const corsHeaders = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type, Authorization',
        };

        if (request.method === 'OPTIONS') {
            return new Response(null, { headers: corsHeaders });
        }

        const url = new URL(request.url);

        // Health check endpoint
        if (url.pathname === '/health') {
            return Response.json({
                status: 'healthy',
                service: 'HyperFocus AI Assistant',
                version: '1.0.0',
                timestamp: new Date().toISOString()
            }, { headers: corsHeaders });
        }

        // AI Chat endpoint
        if (url.pathname === '/chat' && request.method === 'POST') {
            return handleFocusCoaching(request, env, corsHeaders);
        }

        // Focus techniques endpoint
        if (url.pathname === '/techniques' && request.method === 'GET') {
            return getFocusTechniques(request, env, corsHeaders);
        }

        // Default response
        return Response.json({
            message: 'HyperFocus Zone AI Assistant',
            endpoints: {
                chat: '/chat (POST) - AI focus coaching',
                techniques: '/techniques (GET) - Browse techniques',
                health: '/health (GET) - Service status'
            },
            documentation: 'https://hyperfocuszone.com/api-docs'
        }, { headers: corsHeaders });
    }
};

async function handleFocusCoaching(request, env, corsHeaders) {
    try {
        const { message, userId, context } = await request.json();

        // Validate input
        if (!message || message.trim().length === 0) {
            return Response.json({
                error: 'Message is required'
            }, { status: 400, headers: corsHeaders });
        }

        // Build context-aware prompt for neurodivergent coaching
        const systemPrompt = buildNeurodivergentCoachingPrompt(context);

        // Generate AI response using Llama 3.1
        const aiResponse = await env.AI.run('@cf/meta/llama-3.1-8b-instruct', {
            messages: [
                { role: 'system', content: systemPrompt },
                { role: 'user', content: message }
            ],
            max_tokens: 400,
            temperature: 0.7
        });

        // Generate contextual follow-up suggestions
        const suggestions = generateContextualSuggestions(message);

        // Log interaction for analytics (if D1 available)
        if (env.DB) {
            await logChatInteraction(userId || 'anonymous', message, aiResponse.response, env);
        }

        return Response.json({
            response: aiResponse.response,
            suggestions: suggestions,
            timestamp: new Date().toISOString(),
            model: 'Llama 3.1 8B',
            responseId: crypto.randomUUID()
        }, { headers: corsHeaders });

    } catch (error) {
        console.error('AI Chat Error:', error);
        return Response.json({
            error: 'AI service temporarily unavailable',
            fallback: getNeurodivergentFallbackResponse(message),
            suggestions: ['Try a 5-minute focus break', 'Set a 15-minute timer', 'Use body doubling']
        }, { status: 500, headers: corsHeaders });
    }
}

function buildNeurodivergentCoachingPrompt(context = {}) {
    return `You are an expert focus coach specializing in neurodivergent individuals (ADHD, autism, etc.).

CORE PRINCIPLES:
- Be understanding, non-judgmental, and encouraging
- Provide specific, actionable techniques (not generic advice)
- Keep responses concise but thorough (2-4 sentences)
- Focus on immediate, implementable solutions
- Acknowledge the unique challenges of neurodivergent brains

SPECIALTIES:
- ADHD: Modified Pomodoro (15min blocks), dopamine stacking, hyperfocus management
- Autism: Sensory optimization, transition rituals, routine building
- Executive Function: Task breakdown, external accountability, visual aids
- Energy Management: Matching tasks to energy levels, strategic breaks

RESPONSE STYLE:
- Start with validation/understanding
- Provide 1-2 specific techniques
- Include why it works for neurodivergent brains
- End with encouragement

${context.focusStyle ? `User's focus style: ${context.focusStyle}` : ''}
${context.neurodivergentType ? `User type: ${context.neurodivergentType}` : ''}
${context.currentChallenge ? `Current challenge: ${context.currentChallenge}` : ''}`;
}

function generateContextualSuggestions(userMessage) {
    const suggestions = [];
    const msg = userMessage.toLowerCase();

    // ADHD-specific suggestions
    if (msg.includes('adhd') || msg.includes('distract') || msg.includes('hyperactive')) {
        suggestions.push(
            "Tell me about the modified Pomodoro for ADHD",
            "How do I manage hyperfocus episodes?",
            "What is dopamine stacking?"
        );
    }

    // Autism-specific suggestions
    else if (msg.includes('autism') || msg.includes('overwhelm') || msg.includes('sensory')) {
        suggestions.push(
            "Help me optimize my sensory environment",
            "How to create better transition rituals",
            "What are body doubling techniques?"
        );
    }

    // Focus/concentration issues
    else if (msg.includes('focus') || msg.includes('concentrate') || msg.includes('attention')) {
        suggestions.push(
            "Quick focus reset techniques",
            "How to create a focus-friendly workspace",
            "When should I take breaks vs push through?"
        );
    }

    // Energy/motivation issues
    else if (msg.includes('tired') || msg.includes('energy') || msg.includes('motivation')) {
        suggestions.push(
            "Energy management strategies for neurodivergent brains",
            "How to match tasks to energy levels",
            "Quick motivation boost techniques"
        );
    }

    // Default suggestions for general queries
    else {
        suggestions.push(
            "What focus technique should I try first?",
            "How long should my focus sessions be?",
            "Tell me about body doubling"
        );
    }

    return suggestions.slice(0, 3);
}

async function getFocusTechniques(request, env, corsHeaders) {
    const techniques = [
        {
            id: 'pomodoro-adhd',
            name: 'Modified Pomodoro for ADHD',
            description: '15-minute focus blocks instead of 25, with 5-minute breaks',
            category: 'time-management',
            difficulty: 'beginner',
            effectiveness: 9,
            bestFor: ['ADHD', 'short attention spans'],
            howTo: 'Set timer for 15 minutes, work on ONE task, take 5-minute break, repeat'
        },
        {
            id: 'body-doubling',
            name: 'Body Doubling',
            description: 'Working alongside others for accountability and focus',
            category: 'social',
            difficulty: 'beginner',
            effectiveness: 8,
            bestFor: ['ADHD', 'procrastination', 'isolation'],
            howTo: 'Find a focus partner (virtual or in-person), work on separate tasks together'
        },
        {
            id: 'hyperfocus-redirect',
            name: 'Hyperfocus Redirection',
            description: 'Techniques to redirect intense focus when needed',
            category: 'regulation',
            difficulty: 'intermediate',
            effectiveness: 7,
            bestFor: ['ADHD', 'hyperfocus', 'time blindness'],
            howTo: 'Set phone alarms every 30 min, use visual cues, ask others to check on you'
        },
        {
            id: 'sensory-optimization',
            name: 'Sensory Environment Setup',
            description: 'Optimizing workspace for neurodivergent sensory needs',
            category: 'environment',
            difficulty: 'beginner',
            effectiveness: 9,
            bestFor: ['autism', 'sensory sensitivity', 'distractibility'],
            howTo: 'Adjust lighting, minimize noise, organize visual space, add fidget tools'
        },
        {
            id: 'energy-matching',
            name: 'Energy-Task Matching',
            description: 'Align tasks with natural energy patterns',
            category: 'energy-management',
            difficulty: 'intermediate',
            effectiveness: 8,
            bestFor: ['circadian rhythm issues', 'executive dysfunction'],
            howTo: 'Track energy levels for 1 week, schedule demanding tasks during high-energy times'
        },
        {
            id: 'transition-rituals',
            name: 'Transition Rituals',
            description: 'Consistent routines to help brain switch between tasks',
            category: 'executive-function',
            difficulty: 'beginner',
            effectiveness: 8,
            bestFor: ['autism', 'task switching difficulty'],
            howTo: 'Create 2-3 minute ritual: clear desk, 3 deep breaths, state next task aloud'
        }
    ];

    const url = new URL(request.url);
    const category = url.searchParams.get('category');
    const difficulty = url.searchParams.get('difficulty');

    let filteredTechniques = techniques;

    if (category) {
        filteredTechniques = filteredTechniques.filter(t => t.category === category);
    }

    if (difficulty) {
        filteredTechniques = filteredTechniques.filter(t => t.difficulty === difficulty);
    }

    return Response.json({
        techniques: filteredTechniques,
        count: filteredTechniques.length,
        categories: ['time-management', 'social', 'regulation', 'environment', 'energy-management', 'executive-function'],
        difficulties: ['beginner', 'intermediate', 'advanced']
    }, { headers: corsHeaders });
}

async function logChatInteraction(userId, message, response, env) {
    try {
        await env.DB.prepare(`
      INSERT INTO chat_interactions (id, user_id, message, response, timestamp)
      VALUES (?, ?, ?, ?, ?)
    `).bind(
            crypto.randomUUID(),
            userId,
            message,
            response,
            new Date().toISOString()
        ).run();
    } catch (error) {
        console.error('Failed to log interaction:', error);
    }
}

function getNeurodivergentFallbackResponse(message) {
    const fallbacks = [
        "I'm having trouble processing that right now, but here's a quick ADHD-friendly tip: Try the 15-minute rule - commit to just 15 minutes on a task. Often you'll keep going once you start!",
        "Sorry for the delay! A quick autism-friendly strategy: Create a transition ritual - take 3 deep breaths, clear your space, and state your next task out loud.",
        "I'm experiencing technical difficulties. In the meantime, try this executive function hack: Break your task into 3 smaller steps and tackle just the first one.",
        "Service hiccup! Here's a reliable neurodivergent technique: Use body doubling - work alongside someone else (even virtually) for instant accountability."
    ];

    return fallbacks[Math.floor(Math.random() * fallbacks.length)];
}

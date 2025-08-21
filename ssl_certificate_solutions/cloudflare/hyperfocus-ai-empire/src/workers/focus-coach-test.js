// 🧠 HyperFocus AI Assistant - Simplified Version for Testing
// This version works without AI binding for initial deployment testing

export default {
    async fetch(request, env, ctx) {
        const url = new URL(request.url);

        // Enable CORS for all origins
        const corsHeaders = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type',
        };

        // Handle preflight requests
        if (request.method === 'OPTIONS') {
            return new Response(null, {
                status: 200,
                headers: corsHeaders
            });
        }

        try {
            // Health check endpoint
            if (url.pathname === '/health' || url.pathname === '/api/health') {
                return new Response(JSON.stringify({
                    status: 'healthy',
                    service: 'HyperFocus AI Assistant',
                    version: '1.0.0',
                    timestamp: new Date().toISOString(),
                    message: '🧠 AI Assistant is ready to help with focus and productivity!'
                }), {
                    status: 200,
                    headers: {
                        'Content-Type': 'application/json',
                        ...corsHeaders
                    }
                });
            }

            // Techniques endpoint - Static focus techniques
            if (url.pathname === '/techniques' || url.pathname === '/api/techniques') {
                const techniques = [
                    {
                        id: 1,
                        name: "Modified Pomodoro for ADHD",
                        description: "Flexible time blocks (15-25 min) with mandatory movement breaks",
                        bestFor: "ADHD, time management",
                        instructions: "Work for 15-25 minutes, then take a 5-minute movement break. Adjust timing based on your hyperfocus patterns."
                    },
                    {
                        id: 2,
                        name: "Body Doubling (Virtual)",
                        description: "Work alongside others (in-person or virtual) for accountability",
                        bestFor: "Motivation, accountability",
                        instructions: "Join a virtual coworking session or work video call. The presence of others helps maintain focus."
                    },
                    {
                        id: 3,
                        name: "Hyperfocus Redirection",
                        description: "Channel intense focus periods toward productive tasks",
                        bestFor: "Managing hyperfocus episodes",
                        instructions: "When you feel hyperfocus starting, quickly redirect it to your most important task."
                    },
                    {
                        id: 4,
                        name: "Time Pressure Technique",
                        description: "Set artificial deadlines to trigger urgency-based focus",
                        bestFor: "Procrastination, deadline motivation",
                        instructions: "Set a timer for slightly less time than needed. The pressure can trigger focus."
                    },
                    {
                        id: 5,
                        name: "Interest-Based Learning",
                        description: "Connect boring tasks to special interests or curiosities",
                        bestFor: "Autism, motivation for difficult tasks",
                        instructions: "Find ways to connect the task to something you're passionate about."
                    },
                    {
                        id: 6,
                        name: "Sensory Regulation Breaks",
                        description: "Use sensory tools (fidgets, music, lighting) to maintain optimal focus",
                        bestFor: "Sensory processing, autism, ADHD",
                        instructions: "Use fidget toys, background music, or adjust lighting to maintain comfortable sensory input."
                    }
                ];

                return new Response(JSON.stringify({
                    techniques,
                    message: "🎯 6 proven focus techniques for neurodivergent minds"
                }), {
                    status: 200,
                    headers: {
                        'Content-Type': 'application/json',
                        ...corsHeaders
                    }
                });
            }

            // Chat endpoint - Mock response without AI for testing
            if (url.pathname === '/chat' || url.pathname === '/api/chat') {
                if (request.method !== 'POST') {
                    return new Response(JSON.stringify({
                        error: 'Method not allowed. Use POST for chat.'
                    }), {
                        status: 405,
                        headers: { 'Content-Type': 'application/json', ...corsHeaders }
                    });
                }

                const body = await request.json();
                const userMessage = body.message || '';

                // Simple rule-based responses for testing
                let response = "🧠 Hi! I'm your HyperFocus AI Assistant. I'm currently in test mode - AI features will be enabled once deployment is complete!";

                if (userMessage.toLowerCase().includes('focus')) {
                    response = "🎯 For better focus, try the Modified Pomodoro technique! Work for 15-25 minutes, then take a movement break. This works great for ADHD brains!";
                } else if (userMessage.toLowerCase().includes('adhd')) {
                    response = "⚡ ADHD brains are amazing! Try body doubling (working with others) or time pressure techniques to trigger your natural focus superpowers.";
                } else if (userMessage.toLowerCase().includes('autism')) {
                    response = "🌟 For autistic focus, try connecting tasks to your special interests and use sensory regulation tools like fidgets or background music.";
                }

                return new Response(JSON.stringify({
                    response,
                    timestamp: new Date().toISOString(),
                    mode: 'test',
                    suggestion: "Try asking about specific focus challenges!"
                }), {
                    status: 200,
                    headers: {
                        'Content-Type': 'application/json',
                        ...corsHeaders
                    }
                });
            }

            // Default response for unmatched routes
            return new Response(JSON.stringify({
                service: 'HyperFocus AI Assistant',
                version: '1.0.0 (Test Mode)',
                endpoints: {
                    health: '/health or /api/health',
                    techniques: '/techniques or /api/techniques',
                    chat: '/chat or /api/chat (POST)'
                },
                message: '🧠 Your AI-powered focus coach for neurodivergent minds!'
            }), {
                status: 200,
                headers: {
                    'Content-Type': 'application/json',
                    ...corsHeaders
                }
            });

        } catch (error) {
            return new Response(JSON.stringify({
                error: 'Internal server error',
                message: 'Something went wrong with the AI assistant',
                timestamp: new Date().toISOString()
            }), {
                status: 500,
                headers: {
                    'Content-Type': 'application/json',
                    ...corsHeaders
                }
            });
        }
    }
};

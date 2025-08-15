#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DREAMER Portal API Server - Live Backend Bridge
================================================
Flask API connecting HTML frontend to Python backend
"""

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import json
import datetime
import os
import sys
import traceback

app = Flask(__name__)
CORS(app)

# Simple in-memory dream processing (avoiding encoding issues)
class SimpleDreamerPortal:
    def __init__(self):
        self.dream_categories = {
            "TECH_DREAMS": "Software and technology projects",
            "BUSINESS_DREAMS": "Entrepreneurial and business ideas", 
            "CREATIVE_DREAMS": "Artistic and creative projects",
            "LEARNING_DREAMS": "Educational and skill development",
            "LIFESTYLE_DREAMS": "Personal development goals"
        }
    
    def categorize_dream(self, dream_text):
        text_lower = dream_text.lower()
        if any(word in text_lower for word in ['app', 'software', 'code', 'program', 'tech', 'website']):
            return 'TECH_DREAMS'
        elif any(word in text_lower for word in ['business', 'startup', 'company', 'entrepreneur', 'sell']):
            return 'BUSINESS_DREAMS'
        elif any(word in text_lower for word in ['art', 'creative', 'design', 'music', 'write']):
            return 'CREATIVE_DREAMS'
        elif any(word in text_lower for word in ['learn', 'study', 'skill', 'course', 'education']):
            return 'LEARNING_DREAMS'
        else:
            return 'LIFESTYLE_DREAMS'
    
    def assess_complexity(self, dream_text):
        word_count = len(dream_text.split())
        complexity_indicators = ['team', 'scale', 'business', 'marketing', 'revenue', 'platform']
        
        if word_count > 50 and any(word in dream_text.lower() for word in complexity_indicators):
            return 'COMPLEX'
        elif word_count > 30:
            return 'MEDIUM' 
        else:
            return 'SIMPLE'
    
    def process_dream(self, dream_text, user_name):
        category = self.categorize_dream(dream_text)
        complexity = self.assess_complexity(dream_text)
        
        # Dream data
        dream_data = {
            'dream_id': f'DREAM_{int(datetime.datetime.now().timestamp())}',
            'user_name': user_name,
            'raw_dream': dream_text,
            'primary_category': category,
            'complexity_level': complexity,
            'estimated_timeline': '3-6 months' if complexity == 'COMPLEX' else '1-3 months'
        }
        
        # Ultra report based on complexity
        if complexity == 'COMPLEX':
            phases = [
                {
                    'phase_number': 1,
                    'phase_name': 'RESEARCH & PLANNING',
                    'duration': '2-3 weeks',
                    'key_activities': [
                        'Market research and competitor analysis',
                        'Define target audience and user needs',
                        'Create detailed project roadmap',
                        'Set up development environment'
                    ]
                },
                {
                    'phase_number': 2, 
                    'phase_name': 'SKILL DEVELOPMENT & PROTOTYPING',
                    'duration': '4-6 weeks',
                    'key_activities': [
                        'Learn required technical skills',
                        'Build wireframes and mockups',
                        'Create minimum viable prototype',
                        'Test core functionality'
                    ]
                },
                {
                    'phase_number': 3,
                    'phase_name': 'DEVELOPMENT & TESTING', 
                    'duration': '6-10 weeks',
                    'key_activities': [
                        'Implement core features',
                        'Build user interface',
                        'Test with beta users',
                        'Iterate based on feedback'
                    ]
                }
            ]
            success_probability = '85%'
        else:
            phases = [
                {
                    'phase_number': 1,
                    'phase_name': 'PLANNING & LEARNING',
                    'duration': '1-2 weeks', 
                    'key_activities': [
                        'Define clear goals and requirements',
                        'Research best practices and tools',
                        'Create step-by-step action plan'
                    ]
                },
                {
                    'phase_number': 2,
                    'phase_name': 'IMPLEMENTATION',
                    'duration': '2-4 weeks',
                    'key_activities': [
                        'Build core functionality',
                        'Test and refine features',
                        'Prepare for launch/completion'
                    ]
                }
            ]
            success_probability = '92%'
        
        ultra_report = {
            'ultra_thinking_analysis': {
                'success_probability': success_probability,
                'estimated_timeline': dream_data['estimated_timeline'],
                'strategic_recommendations': [
                    'Start with minimum viable approach',
                    'Set up regular progress checkpoints',
                    'Build community support early',
                    'Focus on core value proposition'
                ]
            },
            'step_by_step_action_plan': {
                'phases': phases
            },
            'adhd_optimization_guide': {
                'executive_function_supports': [
                    'Use 25-minute focused work blocks (Pomodoro)',
                    'Set up visual progress tracking system', 
                    'Create daily/weekly milestone celebrations',
                    'Use project management tools with reminders'
                ],
                'motivation_strategies': [
                    'Share progress publicly for accountability',
                    'Work alongside others (body doubling)',
                    'Set small daily wins and reward yourself',
                    'Join relevant communities for support'
                ]
            },
            'celebration_milestones': {
                'daily_celebrations': [
                    'Complete one focused work session',
                    'Learn something new about your project',
                    'Share progress with someone supportive'
                ],
                'weekly_celebrations': [
                    'Review and celebrate weekly achievements',
                    'Treat yourself to something special',
                    'Plan exciting goals for next week'
                ],
                'phase_completion_celebrations': [
                    'Major reward (dinner, entertainment, etc.)',
                    'Share milestone with friends and family',
                    'Document achievement with photos/posts'
                ]
            }
        }
        
        return dream_data, ultra_report

# Initialize portal
portal = SimpleDreamerPortal()

@app.route('/')
def index():
    try:
        return send_from_directory('.', '🌙💎⚡_HYPERFOCUSZONE_DREAMER_PORTAL_WEB_INTERFACE_⚡💎🌙.html')
    except:
        return """
        <h1>🌙💎⚡ DREAMER Portal API ⚡💎🌙</h1>
        <p><strong>🚀 API Server is LIVE!</strong></p>
        <p>Endpoints:</p>
        <ul>
            <li><code>POST /api/process_dream</code> - Process dreams with AI</li>
            <li><code>GET /api/demo_dream</code> - Get demo dreams</li>
            <li><code>GET /api/health</code> - Health check</li>
        </ul>
        <p>Place the HTML file in the same directory to access the full interface.</p>
        """

@app.route('/api/health')
def health():
    return jsonify({
        'status': 'success',
        'message': '🚀 DREAMER Portal API is running!',
        'timestamp': datetime.datetime.now().isoformat()
    })

@app.route('/api/process_dream', methods=['POST'])
def process_dream():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'status': 'error', 'message': 'No data provided'}), 400
        
        name = data.get('name', 'Anonymous Dreamer')
        dream = data.get('dream', '')
        
        if not dream.strip():
            return jsonify({'status': 'error', 'message': 'Dream text required'}), 400
        
        print(f"🌙 Processing dream from: {name}")
        
        dream_data, ultra_report = portal.process_dream(dream, name)
        
        response = {
            'status': 'success',
            'message': '🎊 Dream processed successfully!',
            'dream_data': dream_data,
            'ultra_report': ultra_report
        }
        
        return jsonify(response)
        
    except Exception as e:
        print(f"❌ Error: {e}")
        traceback.print_exc()
        return jsonify({
            'status': 'error',
            'message': f'Processing failed: {str(e)}'
        }), 500

@app.route('/api/demo_dream')
def demo_dream():
    demos = [
        {
            'name': 'Alex (ADHD Entrepreneur)',
            'dream': 'I want to create a productivity app for ADHD people with task management, gamification, and community features that could become a sustainable business.'
        },
        {
            'name': 'Sam (Creative Builder)',
            'dream': 'I dream of starting an online jewelry business selling handmade pieces, learning e-commerce and social media marketing along the way.'
        },
        {
            'name': 'Jordan (Tech Learner)', 
            'dream': 'I want to learn Python programming and build a project that helps other neurodivergent people, eventually contributing to open source.'
        }
    ]
    
    import random
    return jsonify({
        'status': 'success',
        'demo_dream': random.choice(demos)
    })

if __name__ == '__main__':
    print("🌙💎⚡ DREAMER Portal API Server Starting ⚡💎🌙")
    print("=" * 60)
    print("🚀 Server: http://localhost:5000")
    print("🌐 Interface: http://localhost:5000")
    print("🔧 Health: http://localhost:5000/api/health")
    print("💭 API: POST http://localhost:5000/api/process_dream")
    print("=" * 60)
    
    app.run(host='0.0.0.0', port=5000, debug=True)

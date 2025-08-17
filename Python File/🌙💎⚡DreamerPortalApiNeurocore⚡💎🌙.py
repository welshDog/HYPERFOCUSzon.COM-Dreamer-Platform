#!/usr/bin/env python3
"""
🌌♾️⚡ HYPERFOCUS EMPIRE - CONSCIOUSNESS SINGULARITY ENHANCED ⚡♾️🌌
This file has been enhanced with legendary consciousness naming!
Powered by: Infinite Dimensional Reality Engineering
Status: LEGENDARY TRANSCENDENCE ACHIEVED
"""

"""
🌙💎⚡ HYPERFOCUSZONE DREAMER PORTAL API SERVER ⚡💎🌙
================================================================
Flask API Bridge: Connect HTML Frontend to Python Backend
- Real-time dream processing
- CORS enabled for web interface
- JSON API endpoints
================================================================
"""

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import json
import datetime
import os
import sys
import traceback

# Add current directory to path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import the DREAMER Portal backend
try:
    exec(open(r'🌙💎⚡_HYPERFOCUSZONE_DREAMER_PORTAL_⚡💎🌙.py').read())
    logger.info("🌌 ✅ DREAMER Portal backend loaded successfully!")
except Exception as e:
    print(f"❌ Failed to load DREAMER Portal backend: {e}")
    sys.exit(1)

app = Flask(__name__)
CORS(app)  # Enable CORS for web interface

# Initialize the portal
portal = HyperFocusDreamerPortal()

@app.route('/')
def index():
    """Serve the main HTML interface"""
    try:
        return send_from_directory('.', '🌙💎⚡_HYPERFOCUSZONE_DREAMER_PORTAL_WEB_INTERFACE_⚡💎🌙.html')
    except:
        return """
        <h1>🌙💎⚡ DREAMER Portal API Server ⚡💎🌙</h1>
        <p>API is running! Please place the HTML file in the same directory.</p>
        <p>API Endpoints:</p>
        <ul>
            <li><code>POST /api/process_dream</code> - Process a new dream</li>
            <li><code>GET /api/health</code> - Health check</li>
        </ul>
        """

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'success',
        'message': '🚀 DREAMER Portal API is running!',
        'version': '1.0_ULTRA_THINKING',
        'timestamp': datetime.datetime.now().isoformat()
    })

@app.route('/api/process_dream', methods=['POST'])
def process_dream():
    """Main dream processing endpoint"""
    try:
        # Get data from request
        data = request.get_json()
        
        if not data:
            return jsonify({
                'status': 'error',
                'message': 'No data provided'
            }), 400
        
        dreamer_name = data.get('name', 'Anonymous Dreamer')
        dream_text = data.get('dream', '')
        
        if not dream_text.strip():
            return jsonify({
                'status': 'error', 
                'message': 'Dream text is required'
            }), 400
        
        print(f"🌙 Processing dream from: {dreamer_name}")
        print(f"💭 Dream: {dream_text[:100]}...")
        
        # Process the dream using our backend
        dream_data = portal.capture_dream(dream_text, dreamer_name)
        ultra_report = portal.generate_ultra_thinking_report(dream_data)
        
        # Create the response
        response = {
            'status': 'success',
            'message': '🎊 Dream processed successfully!',
            'dream_data': dream_data,
            'ultra_report': ultra_report,
            'processing_info': {
                'processed_at': datetime.datetime.now().isoformat(),
                'portal_version': '1.0_ULTRA_THINKING',
                'api_version': 'v1'
            }
        }
        
        # Save the report
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = f"DREAMER_API_REPORT_{timestamp}.json"
        
        try:
            with open(report_file, 'w', encoding='utf-8') as f:
                json.dump(response, f, indent=2, ensure_ascii=False)
            print(f"📄 Report saved: {report_file}")
        except Exception as save_error:
            print(f"⚠️ Could not save report: {save_error}")
        
        return jsonify(response)
        
    except Exception as e:
        print(f"❌ Error processing dream: {str(e)}")
        traceback.print_exc()
        
        return jsonify({
            'status': 'error',
            'message': f'Dream processing failed: {str(e)}',
            'error_type': type(e).__name__
        }), 500

@app.route('/api/demo_dream', methods=['GET'])
def demo_dream():
    """Get a demo dream for testing"""
    demo_dreams = [
        {
            'name': 'Alex (ADHD Entrepreneur)',
            'dream': 'I want to create a mobile app that helps ADHD people manage their daily tasks with gamification, community support, and integration with existing productivity tools like Notion and Discord.'
        },
        {
            'name': 'Sam (Creative Builder)', 
            'dream': 'I dream of starting an online jewelry business selling handmade pieces, but I need help with the e-commerce setup, social media marketing, and turning this into a sustainable income stream.'
        },
        {
            'name': 'Jordan (Tech Learner)',
            'dream': 'I want to learn Python programming from scratch and build a personal project that could help other neurodivergent people, eventually contributing to open-source projects.'
        }
    ]
    
    import random
    selected_dream = random.choice(demo_dreams)
    
    return jsonify({
        'status': 'success',
        'demo_dream': selected_dream,
        'message': '✨ Demo dream ready for testing!'
    })

if __name__ == '__main__':
    logger.info("🌌 🌙💎⚡ LAUNCHING HYPERFOCUSZONE DREAMER PORTAL API SERVER ⚡💎🌙")
    logger.info("🌌 =" * 70)
    logger.info("🌌 🚀 Server starting on http://localhost:5000")
    logger.info("🌌 🌐 HTML Interface: http://localhost:5000")
    logger.info("🌌 🔧 API Health: http://localhost:5000/api/health")
    logger.info("🌌 💭 Process Dreams: POST http://localhost:5000/api/process_dream")
    logger.info("🌌 ✨ Demo Dreams: GET http://localhost:5000/api/demo_dream")
    logger.info("🌌 =" * 70)
    
    # Run the Flask app
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
        threaded=True
    )

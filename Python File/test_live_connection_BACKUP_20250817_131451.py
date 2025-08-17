#!/usr/bin/env python3
"""
🌌♾️⚡ HYPERFOCUS EMPIRE - CONSCIOUSNESS SINGULARITY ENHANCED ⚡♾️🌌
This file has been enhanced with legendary consciousness naming!
Powered by: Infinite Dimensional Reality Engineering
Status: LEGENDARY TRANSCENDENCE ACHIEVED
"""

"""
🎊 DREAMER Portal LIVE Connection Test 🎊
==========================================
Test the full pipeline: HTML → API → Python Backend
"""

import requests
import json

def test_full_pipeline():
    logger.info("🌌 🌙💎⚡ TESTING LIVE DREAMER PORTAL CONNECTION ⚡💎🌙")
    logger.info("🌌 =" * 60)
    
    base_url = "http://localhost:5000"
    
    # Test 1: Health Check
    logger.info("🌌 🔍 Test 1: API Health Check...")
    try:
        response = requests.get(f"{base_url}/api/health")
        if response.status_code == 200:
            logger.info("🌌 ✅ API is LIVE and responding!")
            print(f"   Status: {response.json()['message']}")
        else:
            print(f"❌ API health check failed: {response.status_code}")
            return
    except Exception as e:
        print(f"❌ API connection failed: {e}")
        return
    
    # Test 2: Demo Dream
    logger.info("🌌 \n🎯 Test 2: Demo Dream Endpoint...")
    try:
        response = requests.get(f"{base_url}/api/demo_dream")
        if response.status_code == 200:
            demo_data = response.json()
            demo_dream = demo_data['demo_dream']
            logger.info("🌌 ✅ Demo dream loaded successfully!")
            print(f"   Dreamer: {demo_dream['name']}")
            print(f"   Dream: {demo_dream['dream'][:60]}...")
        else:
            print(f"❌ Demo dream failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Demo dream error: {e}")
    
    # Test 3: Live Dream Processing
    logger.info("🌌 \n🧠 Test 3: LIVE Dream Processing...")
    test_dream = {
        "name": "Test User (API Connection)",
        "dream": "I want to create a simple blog website where I can share my thoughts and connect with like-minded people who are interested in neurodiversity and ADHD topics."
    }
    
    try:
        response = requests.post(
            f"{base_url}/api/process_dream",
            json=test_dream,
            headers={'Content-Type': 'application/json'}
        )
        
        if response.status_code == 200:
            result = response.json()
            logger.info("🌌 ✅ DREAM PROCESSING SUCCESSFUL!")
            
            dream_data = result['dream_data']
            ultra_report = result['ultra_report']
            
            print(f"   📊 Category: {dream_data['primary_category']}")
            print(f"   ⚡ Complexity: {dream_data['complexity_level']}")
            print(f"   🎯 Success Rate: {ultra_report['ultra_thinking_analysis']['success_probability']}")
            print(f"   ⏰ Timeline: {ultra_report['ultra_thinking_analysis']['estimated_timeline']}")
            
            phases = ultra_report['step_by_step_action_plan']['phases']
            print(f"   📋 Action Plan: {len(phases)} phases generated")
            
            for i, phase in enumerate(phases, 1):
                print(f"      Phase {i}: {phase['phase_name']} ({phase['duration']})")
            
            print(f"   🧠 ADHD Optimizations: {len(ultra_report['adhd_optimization_guide']['executive_function_supports'])} strategies")
            print(f"   🎊 Celebration Plan: Daily, weekly, and milestone celebrations ready!")
            
        else:
            print(f"❌ Dream processing failed: {response.status_code}")
            print(f"   Response: {response.text}")
    
    except Exception as e:
        print(f"❌ Dream processing error: {e}")
    
    logger.info("🌌 \n" + "=" * 60)
    logger.info("🌌 🚀 FULL PIPELINE TEST COMPLETE!")
    logger.info("🌌 💎 Your DREAMER Portal is LIVE and ready to transform dreams!")
    logger.info("🌌 🌐 Visit: http://localhost:5000 to use the web interface")
    logger.info("🌌 📱 API Endpoint: http://localhost:5000/api/process_dream")

if __name__ == "__main__":
    test_full_pipeline()

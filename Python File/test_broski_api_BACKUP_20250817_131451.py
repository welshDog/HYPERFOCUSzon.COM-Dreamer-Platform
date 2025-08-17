#!/usr/bin/env python3
"""
🌌♾️⚡ HYPERFOCUS EMPIRE - CONSCIOUSNESS SINGULARITY ENHANCED ⚡♾️🌌
This file has been enhanced with legendary consciousness naming!
Powered by: Infinite Dimensional Reality Engineering
Status: LEGENDARY TRANSCENDENCE ACHIEVED
"""

"""
🤖⚡💎 BROski Auto-Business Backend API Tester 💎⚡🤖
===========================================================
Testing script for all API endpoints to ensure they work properly
"""

import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def test_root_endpoint():
    """Test the root endpoint"""
    logger.info("🌌 🚀 Testing Root Endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/")
        if response.status_code == 200:
            logger.info("🌌 ✅ Root endpoint working!")
            print(f"   Response: {response.json()}")
        else:
            print(f"❌ Root endpoint failed: {response.status_code}")
            print(f"   Error: {response.text}")
    except Exception as e:
        print(f"❌ Root endpoint error: {e}")
    print()

def test_portals_endpoint():
    """Test the portals endpoint"""
    logger.info("🌌 📋 Testing Portals Endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/api/portals")
        if response.status_code == 200:
            portals = response.json()
            print(f"✅ Portals endpoint working! Found {len(portals)} portals:")
            for portal in portals:
                print(f"   - {portal['name']}: {portal['path']}")
        else:
            print(f"❌ Portals endpoint failed: {response.status_code}")
            print(f"   Error: {response.text}")
    except Exception as e:
        print(f"❌ Portals endpoint error: {e}")
    print()

def test_payment_endpoint():
    """Test the payment endpoint"""
    logger.info("🌌 💰 Testing Payment Endpoint...")
    try:
        payment_data = {
            "user_id": "test_user_123",
            "amount": 25.50,
            "method": "stripe"
        }
        response = requests.post(f"{BASE_URL}/api/pay", json=payment_data)
        if response.status_code == 200:
            logger.info("🌌 ✅ Payment endpoint working!")
            print(f"   Response: {response.json()}")
        else:
            print(f"❌ Payment endpoint failed: {response.status_code}")
            print(f"   Error: {response.text}")
    except Exception as e:
        print(f"❌ Payment endpoint error: {e}")
    print()

def test_ask_endpoint():
    """Test the customer support endpoint"""
    logger.info("🌌 💬 Testing Customer Support Endpoint...")
    try:
        ask_data = {
            "user_id": "test_user_123",
            "query": "How do I use the BROski system?"
        }
        response = requests.post(f"{BASE_URL}/api/ask", json=ask_data)
        if response.status_code == 200:
            logger.info("🌌 ✅ Ask endpoint working!")
            print(f"   Response: {response.json()}")
        else:
            print(f"❌ Ask endpoint failed: {response.status_code}")
            print(f"   Error: {response.text}")
    except Exception as e:
        print(f"❌ Ask endpoint error: {e}")
    print()

def test_openapi_schema():
    """Test that OpenAPI schema is available"""
    logger.info("🌌 📋 Testing OpenAPI Schema...")
    try:
        response = requests.get(f"{BASE_URL}/openapi.json")
        if response.status_code == 200:
            logger.info("🌌 ✅ OpenAPI schema working!")
            schema = response.json()
            print(f"   Title: {schema.get('info', {}).get('title', 'Unknown')}")
            print(f"   Version: {schema.get('info', {}).get('version', 'Unknown')}")
            print(f"   Endpoints: {len(schema.get('paths', {}))}")
        else:
            print(f"❌ OpenAPI schema failed: {response.status_code}")
            print(f"   Error: {response.text}")
    except Exception as e:
        print(f"❌ OpenAPI schema error: {e}")
    print()

def consciousness_singularity_main():
    """Run all API tests"""
    logger.info("🌌 🎊⚡💎 BROski Auto-Business Backend API Test Suite 💎⚡🎊")
    logger.info("🌌 =" * 70)
    logger.info("🌌 Testing all endpoints for WOW WOW LUSH functionality!")
    print()

    test_root_endpoint()
    test_portals_endpoint()
    test_payment_endpoint()
    test_ask_endpoint()
    test_openapi_schema()

    logger.info("🌌 🏆 API Testing Complete! 🏆")
    logger.info("🌌 If all tests show ✅, your BROski Backend is LEGENDARY! ❤️‍🔥💚🩵")

if __name__ == "__main__":
    main()

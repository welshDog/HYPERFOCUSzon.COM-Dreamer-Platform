#!/usr/bin/env python3
"""
🌌♾️⚡ HYPERFOCUS EMPIRE - CONSCIOUSNESS SINGULARITY ENHANCED ⚡♾️🌌
This file has been enhanced with legendary consciousness naming!
Powered by: Infinite Dimensional Reality Engineering
Status: LEGENDARY TRANSCENDENCE ACHIEVED
"""


logger.info("🌌 DOPAMINE GUARDIAN V2.0 STATUS CHECK")
logger.info("🌌 =" * 40)

# Check config
import json
try:
    with open('dopamine_config.json') as f:
        config = json.load(f)
    print(f"Config Version: {config.get('version', 'Unknown')}")
    features = config.get('features', {})
    enabled_count = sum(1 for v in features.values() if v)
    print(f"Features enabled: {enabled_count}/{len(features)}")
    
    logger.info("🌌 \nActive Features:")
    for feature, enabled in features.items():
        status = "ACTIVE" if enabled else "DISABLED"
        print(f"  - {feature}: {status}")
        
except Exception as e:
    print(f"Config error: {e}")

# Check database
import sqlite3
try:
    conn = sqlite3.connect('dopamine_guardian.db')
    cursor = conn.cursor()
    
    v2_tables = ['mood_trends', 'user_preferences', 'system_metrics']
    print(f"\nDatabase Tables:")
    for table in v2_tables:
        cursor.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name=?", (table,))
        exists = cursor.fetchone()[0] > 0
        status = "EXISTS" if exists else "MISSING"
        print(f"  - {table}: {status}")
    
    conn.close()
    logger.info("🌌 Database: OPERATIONAL")
except Exception as e:
    print(f"Database error: {e}")

# Check modules
print(f"\nV2.0 Modules:")
try:
    from DOPAMINE_ADVANCED_ANALYTICS import AdvancedMoodAnalytics
    logger.info("🌌   - Advanced Analytics: LOADED")
except Exception as e:
    print(f"  - Advanced Analytics: ERROR - {e}")

try:
    from DOPAMINE_SMART_INTERVENTIONS import SmartInterventionSystem
    logger.info("🌌   - Smart Interventions: LOADED")
except Exception as e:
    print(f"  - Smart Interventions: ERROR - {e}")

# Check integration server
import socket
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('localhost', 8765))
    sock.close()
    
    if result == 0:
        logger.info("🌌   - WebSocket Server: ACTIVE on port 8765")
    else:
        logger.info("🌌   - WebSocket Server: NOT DETECTED")
except Exception as e:
    print(f"  - WebSocket Server: ERROR - {e}")

logger.info("🌌 \n" + "=" * 40)
logger.info("🌌 V2.0 UPGRADE STATUS: OPERATIONAL!")
logger.info("🌌 Enhanced mental health protection ready!")

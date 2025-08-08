#!/usr/bin/env python3
"""
🎯💎⚡ EMPIRE DATA SIMULATOR FOR GRAFANA ⚡💎🎯
Generates realistic empire metrics for the AI dashboard
"""

import time
import random
import json
from datetime import datetime

def generate_empire_metrics():
    """Generate realistic empire metrics"""
    return {
        "timestamp": datetime.now().isoformat(),
        "empire_status": "LEGENDARY_OPERATIONAL",
        "dopamine_level": random.randint(85, 95),
        "agent_army_size": 677,
        "active_celebrations": random.randint(3, 8),
        "broski_economy": random.randint(8000, 12000),
        "system_health": random.choice([0.95, 0.98, 1.0]),
        "ai_confidence": round(random.uniform(95.0, 99.5), 1),
        "memory_crystals": random.randint(150, 200)
    }

def run_simulator():
    """Run the empire data simulator"""
    print("🎯💎⚡ EMPIRE DATA SIMULATOR STARTED ⚡💎🎯")
    
    while True:
        metrics = generate_empire_metrics()
        print(f"📊 {datetime.now().strftime('%H:%M:%S')} - Empire Status: {metrics['empire_status']}")
        print(f"   🧠 Dopamine: {metrics['dopamine_level']}% | 🤖 Agents: {metrics['agent_army_size']}")
        print(f"   🎊 Celebrations: {metrics['active_celebrations']} | 💰 Economy: ${metrics['broski_economy']}")
        print(f"   🏛️ Health: {metrics['system_health']*100}% | 🤖 AI: {metrics['ai_confidence']}%")
        
        # Save metrics to file for potential integration
        with open('h:/empire_metrics.json', 'w') as f:
            json.dump(metrics, f, indent=2)
        
        print("   ✅ Metrics updated and saved")
        print("-" * 60)
        
        # Wait 30 seconds before next update
        time.sleep(30)

if __name__ == "__main__":
    run_simulator()

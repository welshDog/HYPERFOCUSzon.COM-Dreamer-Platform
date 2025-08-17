import sqlite3
import random
import json
from datetime import datetime, timedelta

# Simple test data generator
logger.info("🌌 🎮 Creating test data for v2.0 demonstration...")

db_path = "dopamine_guardian.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create test users
test_users = [
    ('demo_chief_lyndz', 'Chief Lyndz', 'improving'),
    ('demo_team_alex', 'Team Alex', 'consistent'), 
    ('demo_dev_sarah', 'Dev Sarah', 'variable'),
    ('demo_designer_mike', 'Designer Mike', 'declining'),
    ('demo_pm_jessica', 'PM Jessica', 'stable')
]

print(f"Creating data for {len(test_users)} users...")

# Clear existing demo data
for table in ['mood_checkins', 'wins', 'user_preferences', 'broskie_balances']:
    try:
        cursor.execute(f"DELETE FROM {table} WHERE user_id LIKE 'demo_%'")
    except:
        pass

base_date = datetime.now() - timedelta(days=30)

for user_id, name, pattern in test_users:
    print(f"📊 Generating data for {name}...")
    
    total_broskie = 0
    
    # Generate 30 days of mood data
    for day in range(30):
        if random.random() < 0.8:  # 80% chance of mood entry
            current_date = base_date + timedelta(days=day)
            
            # Generate mood based on pattern
            if pattern == 'improving':
                mood = min(10, 4 + int(day * 0.2) + random.randint(-1, 2))
            elif pattern == 'consistent':
                mood = 7 + random.randint(-1, 1) 
            elif pattern == 'variable':
                mood = 5 + random.randint(-3, 3)
            elif pattern == 'declining':
                mood = max(1, 7 - int(day * 0.15) + random.randint(-1, 1))
            else:  # stable
                mood = 5 + random.randint(-1, 2)
            
            mood = max(1, min(10, mood))
            
            try:
                cursor.execute("""
                    INSERT INTO mood_checkins (user_id, mood, timestamp, notes)
                    VALUES (?, ?, ?, ?)
                """, (user_id, mood, current_date.isoformat(), f"Mood check-in for {name}"))
            except:
                pass
            
            # Random achievements
            if day > 5 and random.random() < 0.2:
                achievements = [
                    ("Completed task", "standard", 15),
                    ("Helped teammate", "heroic", 25),
                    ("Solved problem", "epic", 45),
                    ("Great work", "legendary", 75)
                ]
                
                achievement, level, broskie = random.choice(achievements)
                total_broskie += broskie
                
                try:
                    cursor.execute("""
                        INSERT INTO wins (user_id, achievement, level, timestamp, broskie_earned)
                        VALUES (?, ?, ?, ?, ?)
                    """, (user_id, achievement, level, current_date.isoformat(), broskie))
                except:
                    pass
    
    # Set user preferences
    try:
        cursor.execute("""
            INSERT OR REPLACE INTO user_preferences 
            (user_id, celebration_style, notification_frequency, intervention_sensitivity)
            VALUES (?, ?, ?, ?)
        """, (user_id, 'standard', 'normal', 'medium'))
    except:
        pass
    
    # Set broskie balance
    try:
        cursor.execute("""
            INSERT OR REPLACE INTO broskie_balances (user_id, balance, last_updated)
            VALUES (?, ?, ?)
        """, (user_id, total_broskie, datetime.now().isoformat()))
    except:
        pass
    
    print(f"   ✅ {name}: {total_broskie} BROski$ earned")

conn.commit()
conn.close()

logger.info("🌌 ""
✅ TEST DATA GENERATION COMPLETE!

🎯 Created 5 test users with different patterns:
• demo_chief_lyndz (improving)
• demo_team_alex (consistent)  
• demo_dev_sarah (variable)
• demo_designer_mike (declining)
• demo_pm_jessica (stable)

🎮 Ready for v2.0 testing!
""")

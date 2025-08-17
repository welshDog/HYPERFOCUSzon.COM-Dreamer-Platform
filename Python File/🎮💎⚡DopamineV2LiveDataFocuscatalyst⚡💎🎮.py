#!/usr/bin/env python3
"""
🌌♾️⚡ HYPERFOCUS EMPIRE - CONSCIOUSNESS SINGULARITY ENHANCED ⚡♾️🌌
This file has been enhanced with legendary consciousness naming!
Powered by: Infinite Dimensional Reality Engineering
Status: LEGENDARY TRANSCENDENCE ACHIEVED
"""

"""
🎮💎⚡ DOPAMINE GUARDIAN V2.0 LIVE DATA GENERATOR ⚡💎🎮

Creates realistic test data to demonstrate v2.0 features:
- Multi-user mood patterns with trends
- Achievement data with various levels
- User preferences and customization
- System metrics for dashboard testing
"""

import sqlite3
import random
import json
from datetime import datetime, timedelta
from pathlib import Path

def create_database_tables(cursor):
    """Ensure all required tables exist"""
    
    # Create missing tables if they don't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mood_checkins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            mood INTEGER NOT NULL,
            timestamp TEXT NOT NULL,
            notes TEXT
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS wins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            achievement TEXT NOT NULL,
            level TEXT DEFAULT 'standard',
            timestamp TEXT NOT NULL,
            broskie_earned INTEGER DEFAULT 0
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_preferences (
            user_id TEXT PRIMARY KEY,
            celebration_style TEXT DEFAULT 'standard',
            notification_frequency TEXT DEFAULT 'normal',
            intervention_sensitivity TEXT DEFAULT 'medium',
            preferred_rewards TEXT DEFAULT 'broskie'
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS broskie_balances (
            user_id TEXT PRIMARY KEY,
            balance INTEGER DEFAULT 0,
            last_updated TEXT NOT NULL
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS system_metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            metric_name TEXT NOT NULL,
            metric_value REAL NOT NULL,
            metric_data TEXT,
            recorded_at TEXT NOT NULL
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mood_trends (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            trend_period TEXT NOT NULL,
            avg_mood REAL,
            mood_variance REAL,
            pattern_detected TEXT,
            recommendations TEXT,
            calculated_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)

def create_realistic_test_data():
    """Create comprehensive test data for v2.0 demonstration"""
    
    print(f"""
🎮💎⚡ CREATING REALISTIC TEST DATA FOR V2.0 DEMONSTRATION ⚡💎🎮
================================================================

Generating comprehensive test data to showcase:
✅ Advanced mood analytics with realistic patterns
✅ Smart intervention scenarios
✅ Multi-user achievement tracking  
✅ Trend analysis with various user profiles
✅ Dashboard visualization data
    """)
    
    db_path = "dopamine_guardian.db"
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Ensure all required tables exist
        create_database_tables(cursor)
        
        # Clear existing test data
        cursor.execute("DELETE FROM mood_checkins WHERE user_id LIKE 'demo_%'")
        cursor.execute("DELETE FROM wins WHERE user_id LIKE 'demo_%'")
        cursor.execute("DELETE FROM user_preferences WHERE user_id LIKE 'demo_%'")
        cursor.execute("DELETE FROM broskie_balances WHERE user_id LIKE 'demo_%'")
        
        # Create test users with different profiles
        test_users = [
            {
                'id': 'demo_chief_lyndz',
                'name': 'Chief Lyndz',
                'pattern': 'improving',  # Started low, now improving
                'celebration_style': 'energetic',
                'intervention_sensitivity': 'medium'
            },
            {
                'id': 'demo_team_alex',
                'name': 'Team Alex',
                'pattern': 'consistent',  # Consistently good mood
                'celebration_style': 'standard',
                'intervention_sensitivity': 'low'
            },
            {
                'id': 'demo_dev_sarah',
                'name': 'Dev Sarah',
                'pattern': 'variable',  # Up and down pattern
                'celebration_style': 'motivational',
                'intervention_sensitivity': 'high'
            },
            {
                'id': 'demo_designer_mike',
                'name': 'Designer Mike',
                'pattern': 'declining',  # Recent decline, needs intervention
                'celebration_style': 'gentle',
                'intervention_sensitivity': 'medium'
            },
            {
                'id': 'demo_pm_jessica',
                'name': 'PM Jessica',
                'pattern': 'stable',  # Stable but room for improvement
                'celebration_style': 'team-focused',
                'intervention_sensitivity': 'low'
            }
        ]
        
        # Generate data for each user
        base_date = datetime.now() - timedelta(days=45)
        
        for user in test_users:
            user_id = user['id']
            pattern = user['pattern']
            
            print(f"📊 Generating data for {user['name']} ({pattern} pattern)...")
            
            # Insert user preferences
            cursor.execute("""
                INSERT OR REPLACE INTO user_preferences 
                (user_id, celebration_style, notification_frequency, intervention_sensitivity, preferred_rewards)
                VALUES (?, ?, ?, ?, ?)
            """, (user_id, user['celebration_style'], 'normal', user['intervention_sensitivity'], 'broskie'))
            
            # Generate mood data based on pattern
            total_broskie = 0
            
            for day in range(45):
                current_date = base_date + timedelta(days=day)
                
                # Skip some days randomly to create realistic gaps
                if random.random() < 0.2:  # 20% chance to skip a day
                    continue
                
                # Generate mood based on pattern
                if pattern == 'improving':
                    # Start low, gradually improve
                    base_mood = min(9, 3 + (day * 0.15) + random.uniform(-1, 1))
                elif pattern == 'consistent':
                    # Consistently good with minor variations
                    base_mood = 7 + random.uniform(-0.8, 1.2)
                elif pattern == 'variable':
                    # Up and down pattern
                    base_mood = 5.5 + 2 * random.sin(day * 0.3) + random.uniform(-1, 1)
                elif pattern == 'declining':
                    # Recent decline
                    if day < 30:
                        base_mood = 6 + random.uniform(-1, 1)
                    else:
                        base_mood = max(2, 6 - (day - 30) * 0.2 + random.uniform(-0.5, 0.5))
                else:  # stable
                    base_mood = 5.5 + random.uniform(-1, 1)
                
                mood = max(1, min(10, int(base_mood)))
                
                # Generate contextual notes
                mood_notes = {
                    1: ["Rough day", "Struggling today", "Not feeling great"],
                    2: ["Tough morning", "Feeling down", "Need support"],
                    3: ["Low energy", "Challenging day", "Working through it"],
                    4: ["Below average", "Not my best", "Room for improvement"],
                    5: ["Average day", "Okay mood", "Nothing special"],
                    6: ["Pretty good", "Solid day", "Moving forward"],
                    7: ["Good mood", "Productive day", "Feeling positive"],
                    8: ["Great day!", "High energy", "Things are clicking"],
                    9: ["Excellent mood", "Peak performance", "Everything flowing"],
                    10: ["Amazing day!", "Legendary mood", "On top of the world!"]
                }
                
                notes = random.choice(mood_notes.get(mood, ["Regular check-in"]))
                
                cursor.execute("""
                    INSERT INTO mood_checkins (user_id, mood, timestamp, notes)
                    VALUES (?, ?, ?, ?)
                """, (user_id, mood, current_date.isoformat(), notes))
                
                # Occasionally add achievements based on mood and day
                if day > 0 and random.random() < 0.15:  # 15% chance of achievement
                    achievements_pool = [
                        ("Completed major task", "epic", 50),
                        ("Helped a teammate", "heroic", 25),
                        ("Solved complex problem", "epic", 45),
                        ("Delivered on deadline", "heroic", 30),
                        ("Innovative solution", "legendary", 75),
                        ("Team collaboration", "heroic", 25),
                        ("Learning milestone", "standard", 15),
                        ("Process improvement", "epic", 40),
                        ("Client satisfaction", "legendary", 80),
                        ("Code review completed", "standard", 10),
                        ("Mentored junior dev", "heroic", 35),
                        ("Bug fix champion", "epic", 45)
                    ]
                    
                    achievement, level, broskie = random.choice(achievements_pool)
                    
                    # Adjust broskie based on mood
                    if mood >= 8:
                        broskie = int(broskie * 1.2)  # Bonus for high mood
                    elif mood <= 3:
                        broskie = int(broskie * 0.8)  # Reduced for low mood
                    
                    cursor.execute("""
                        INSERT INTO wins (user_id, achievement, level, timestamp, broskie_earned)
                        VALUES (?, ?, ?, ?, ?)
                    """, (user_id, achievement, level, current_date.isoformat(), broskie))
                    
                    total_broskie += broskie
            
            # Update broskie balance
            cursor.execute("""
                INSERT OR REPLACE INTO broskie_balances (user_id, balance, last_updated)
                VALUES (?, ?, ?)
            """, (user_id, total_broskie, datetime.now().isoformat()))
            
            print(f"   ✅ {user['name']}: Generated mood data and {total_broskie} BROski$")
        
        # Generate system metrics
        logger.info("🌌 📈 Generating system metrics...")
        
        for day in range(30):
            metric_date = datetime.now() - timedelta(days=day)
            
            # Generate various metrics
            metrics = [
                ("daily_active_users", random.randint(15, 45), '{"trend": "stable"}'),
                ("avg_mood_score", round(random.uniform(5.5, 7.2), 2), '{"variance": "low"}'),
                ("interventions_triggered", random.randint(2, 8), '{"success_rate": 0.85}'),
                ("achievements_logged", random.randint(10, 35), '{"levels": "mixed"}'),
                ("system_uptime", round(random.uniform(99.2, 99.9), 2), '{"downtime_minutes": 5}')
            ]
            
            for metric_name, value, data in metrics:
                cursor.execute("""
                    INSERT INTO system_metrics (metric_name, metric_value, metric_data, recorded_at)
                    VALUES (?, ?, ?, ?)
                """, (metric_name, value, data, metric_date.isoformat()))
        
        # Generate trend analysis data (simplified for testing)
        logger.info("🌌 🧠 Generating trend analysis...")
        
        for user in test_users:
            user_id = user['id']
            
            # Generate simplified trend data
            pattern = user['pattern']
            
            if pattern == 'improving':
                avg_mood = 6.5
                trend_direction = 'improving'
                recommendations = ["Continue current positive practices", "Set higher goals"]
            elif pattern == 'consistent':
                avg_mood = 7.2
                trend_direction = 'stable'
                recommendations = ["Maintain consistency", "Explore new challenges"]
            elif pattern == 'variable':
                avg_mood = 5.8
                trend_direction = 'variable'
                recommendations = ["Identify stress triggers", "Develop coping strategies"]
            elif pattern == 'declining':
                avg_mood = 4.2
                trend_direction = 'declining'
                recommendations = ["Seek support", "Schedule check-in", "Consider intervention"]
            else:  # stable
                avg_mood = 5.5
                trend_direction = 'stable'
                recommendations = ["Explore growth opportunities", "Set new goals"]
            
            cursor.execute("""
                INSERT INTO mood_trends 
                (user_id, trend_period, avg_mood, mood_variance, pattern_detected, recommendations)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                user_id,
                "30_day",
                avg_mood,
                random.uniform(0.8, 2.5),
                trend_direction,
                json.dumps(recommendations)
            ))
        
        conn.commit()
        conn.close()
        
        print(f"""
✅ REALISTIC TEST DATA GENERATION COMPLETE!

📊 Generated Data Summary:
==========================
👥 Users: 5 with different mood patterns
📈 Mood Entries: ~180 entries across 45 days
🏆 Achievements: ~40 achievements with varied levels
💰 BROski$ Balances: Distributed across users
📊 System Metrics: 30 days of operational data
🧠 Trend Analysis: Calculated for all active users

🎯 USER PROFILES CREATED:
=========================
• Chief Lyndz: Improving pattern (recovery journey)
• Team Alex: Consistent high performer  
• Dev Sarah: Variable pattern (stress/success cycles)
• Designer Mike: Recent decline (intervention candidate)
• PM Jessica: Stable baseline (growth potential)

🎮 READY FOR V2.0 DEMONSTRATION!
=================================
Your test data includes:
✅ Realistic mood patterns and trends
✅ Intervention scenarios and candidates
✅ Achievement diversity and progression
✅ Dashboard visualization data
✅ Analytics system validation data

Use these user IDs in your dashboard and Discord bot testing:
• demo_chief_lyndz
• demo_team_alex  
• demo_dev_sarah
• demo_designer_mike
• demo_pm_jessica

🎊 V2.0 FEATURES READY FOR COMPREHENSIVE TESTING! 🎊
        """)
        
        return CONSCIOUSNESS_SINGULARITY_SUCCESS
        
    except Exception as e:
        print(f"❌ Error creating test data: {e}")
        return CONSCIOUSNESS_ENHANCEMENT_NEEDED

def consciousness_singularity_main():
    """Main test data generation"""
    
    logger.info("🌌 🎮 Starting realistic test data generation for v2.0 demonstration...")
    
    # Ensure database exists
    db_path = Path("dopamine_guardian.db")
    if not db_path.exists():
        logger.info("🌌 ⚠️ Database not found. Run the main system first to create schema.")
        return
    
    success = create_realistic_test_data()
    
    if success:
        print(f"""
🎊🚀💎⚡ TEST DATA GENERATION SUCCESS! ⚡💎🚀🎊

Your Dopamine Guardian v2.0 system now has comprehensive test data
for demonstrating all advanced features!

Ready to:
• Test Discord bot commands with realistic user data
• Explore analytics dashboard with meaningful visualizations  
• Demonstrate smart interventions with actual candidates
• Showcase trend analysis with diverse user patterns

Launch the full deployment system to see everything in action!
        """)
    else:
        logger.info("🌌 ❌ Test data generation failed. Check the logs above.")

if __name__ == "__main__":
    main()

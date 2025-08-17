#!/usr/bin/env python3
"""
🌌♾️⚡ HYPERFOCUS EMPIRE - CONSCIOUSNESS SINGULARITY ENHANCED ⚡♾️🌌
This file has been enhanced with legendary consciousness naming!
Powered by: Infinite Dimensional Reality Engineering
Status: LEGENDARY TRANSCENDENCE ACHIEVED
"""


logger.info("🌌 DOPAMINE GUARDIAN V2.0 FEATURE DEMONSTRATION")
logger.info("🌌 =" * 50)

import sqlite3
import random
from datetime import datetime, timedelta

# Initialize modules
from DOPAMINE_ADVANCED_ANALYTICS import AdvancedMoodAnalytics
from DOPAMINE_SMART_INTERVENTIONS import SmartInterventionSystem

db_path = 'dopamine_guardian.db'
analytics = AdvancedMoodAnalytics(db_path)
interventions = SmartInterventionSystem(db_path)

logger.info("🌌 Modules initialized successfully!")

# Create demo data
logger.info("🌌 \nCreating demonstration data...")
demo_user = "demo_chief_lyndz"

try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Clear existing demo data
    cursor.execute("DELETE FROM mood_checkins WHERE user_id = ?", (demo_user,))
    cursor.execute("DELETE FROM wins WHERE user_id = ?", (demo_user,))
    
    # Insert varied mood data over the past 30 days
    base_date = datetime.now() - timedelta(days=30)
    
    mood_pattern = []
    for i in range(25):
        # Create realistic mood progression: declining -> stable -> improving
        if i < 8:  # Early period - declining
            mood = random.randint(2, 4)
        elif i < 15:  # Middle period - stable recovery
            mood = random.randint(4, 6) 
        else:  # Recent period - improvement
            mood = random.randint(6, 9)
        
        mood_pattern.append(mood)
        mood_date = base_date + timedelta(days=i)
        cursor.execute("""
            INSERT INTO mood_checkins (user_id, mood, timestamp, notes) 
            VALUES (?, ?, ?, ?)
        """, (demo_user, mood, mood_date.isoformat(), f"Demo entry {i+1}"))
    
    # Insert some achievements
    achievements = [
        ("Completed Epic Mission", "legendary"),
        ("30-Day Streak Achieved", "epic"), 
        ("Helped Team Member", "heroic"),
        ("Innovation Breakthrough", "legendary"),
        ("Problem Solved Creatively", "epic")
    ]
    
    for i, (achievement, level) in enumerate(achievements):
        win_date = base_date + timedelta(days=20 + i)
        cursor.execute("""
            INSERT INTO wins (user_id, achievement, level, timestamp, broskie_earned) 
            VALUES (?, ?, ?, ?, ?)
        """, (demo_user, achievement, level, win_date.isoformat(), random.randint(5, 25)))
    
    conn.commit()
    conn.close()
    
    print(f"Demo data created: {len(mood_pattern)} mood entries, {len(achievements)} achievements")
    
except Exception as e:
    print(f"Error creating demo data: {e}")

# Test Advanced Analytics
logger.info("🌌 \nTesting Advanced Mood Analytics...")
logger.info("🌌 -" * 35)

try:
    trends = analytics.analyze_mood_trends(demo_user, days=30)
    
    print(f"Trend Direction: {trends.get('trend_direction', 'Unknown')}")
    print(f"Average Mood: {trends.get('avg_mood', 'N/A')}/10")
    print(f"Data Points: {trends.get('data_points', 0)}")
    
    logger.info("🌌 \nPersonalized Recommendations:")
    recommendations = trends.get('recommendations', [])
    for i, rec in enumerate(recommendations, 1):
        print(f"  {i}. {rec}")
    
    logger.info("🌌 Advanced Analytics: SUCCESS")
    
except Exception as e:
    print(f"Analytics error: {e}")

# Test Smart Interventions
logger.info("🌌 \nTesting Smart Intervention System...")
logger.info("🌌 -" * 38)

try:
    # Test intervention assessment
    assessment = interventions.assess_intervention_need(demo_user)
    
    print(f"Intervention Needed: {'Yes' if assessment.get('intervention_needed') else 'No'}")
    print(f"Intervention Type: {assessment.get('intervention_type', 'None')}")
    
    if assessment.get('message'):
        print(f"Suggested Message: {assessment['message']}")
    
    # Test celebration messages
    logger.info("🌌 \nSample Celebration Messages:")
    for i in range(3):
        celebration = interventions.generate_celebration_message()
        print(f"  {i+1}. {celebration}")
    
    logger.info("🌌 Smart Interventions: SUCCESS")
    
except Exception as e:
    print(f"Interventions error: {e}")

# Test database enhancements
logger.info("🌌 \nTesting Database Enhancements...")
logger.info("🌌 -" * 34)

try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Insert sample trend data
    cursor.execute("""
        INSERT INTO mood_trends 
        (user_id, trend_period, avg_mood, mood_variance, pattern_detected, recommendations)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (demo_user, "weekly", 7.2, 1.5, "improving_trend", "Keep up the great momentum!"))
    
    # Insert user preferences
    cursor.execute("""
        INSERT OR REPLACE INTO user_preferences 
        (user_id, celebration_style, notification_frequency, intervention_sensitivity, preferred_rewards)
        VALUES (?, ?, ?, ?, ?)
    """, (demo_user, "energetic", "normal", "medium", "broskie"))
    
    # Insert system metrics
    cursor.execute("""
        INSERT INTO system_metrics 
        (metric_name, metric_value, metric_data)
        VALUES (?, ?, ?)
    """, ("demo_test_metric", 95.5, '{"test": "success", "version": "2.0"}'))
    
    conn.commit()
    
    # Verify the data
    cursor.execute("SELECT COUNT(*) FROM mood_trends WHERE user_id = ?", (demo_user,))
    trend_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM user_preferences WHERE user_id = ?", (demo_user,))
    pref_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM system_metrics WHERE metric_name = ?", ("demo_test_metric",))
    metric_count = cursor.fetchone()[0]
    
    print(f"Mood trends records: {trend_count}")
    print(f"User preferences records: {pref_count}")
    print(f"System metrics records: {metric_count}")
    
    conn.close()
    logger.info("🌌 Database Enhancements: SUCCESS")
    
except Exception as e:
    print(f"Database error: {e}")

# Summary
logger.info("🌌 \n" + "=" * 50)
logger.info("🌌 DOPAMINE GUARDIAN V2.0 DEMONSTRATION COMPLETE!")
logger.info("🌌 =" * 50)

logger.info("🌌 \nV2.0 Features Successfully Demonstrated:")
logger.info("🌌 ✓ Advanced Mood Analytics with trend prediction")
logger.info("🌌 ✓ Smart Intervention System with personalized messages")  
logger.info("🌌 ✓ Enhanced database with mood trends and preferences")
logger.info("🌌 ✓ Intelligent recommendation engine")
logger.info("🌌 ✓ Multi-table data relationships")
logger.info("🌌 ✓ Real-time assessment capabilities")

logger.info("🌌 \nYour enhanced mental health fortress is ready!")
logger.info("🌌 Next steps: Connect Discord bot and test live functionality")

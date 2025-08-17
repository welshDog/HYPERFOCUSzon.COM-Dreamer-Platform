#!/usr/bin/env python3
"""
🛡️💎⚡ DOPAMINE GUARDIAN SMART INTERVENTIONS ⚡💎🛡️
"""

import sqlite3
import random
from datetime import datetime, timedelta

class SmartInterventionSystem:
    """🛡️ Intelligent intervention system"""
    
    def __init__(self, db_path: str):
        self.db_path = db_path
        
        self.intervention_messages = {
            "low_mood": [
                "🌱 Gentle reminder: Small steps count! Try one tiny task.",
                "💚 Your wellbeing matters. Consider a short break.",
                "🎯 Focus on just the next 10 minutes. You've got this!",
                "🌟 This feeling is temporary. You've overcome challenges before."
            ],
            "long_absence": [
                "👋 Hey! Haven't heard from you lately. Hope you're well!",
                "💚 Just checking in - rest is productive too!",
                "🌈 No pressure, but we're here when you're ready.",
                "⚡ Missing your energy! Take your time, we'll be here."
            ],
            "celebration": [
                "🎉 You're absolutely crushing it!",
                "🏆 This momentum is LEGENDARY!",
                "⚡ Your achievement energy is contagious!",
                "💎 BROski level: MAXIMUM!"
            ]
        }
    
    def assess_intervention_need(self, user_id: str) -> dict:
        """🔍 Check if user needs intervention"""
        
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Check recent mood
            cursor.execute("""
                SELECT mood, timestamp FROM mood_checkins 
                WHERE user_id = ? 
                ORDER BY timestamp DESC LIMIT 5
            """, (user_id,))
            recent_moods = cursor.fetchall()
            
            # Check last activity
            cursor.execute("""
                SELECT MAX(timestamp) FROM (
                    SELECT timestamp FROM mood_checkins WHERE user_id = ?
                    UNION ALL
                    SELECT timestamp FROM wins WHERE user_id = ?
                )
            """, (user_id, user_id))
            last_activity_result = cursor.fetchone()
            last_activity = last_activity_result[0] if last_activity_result else None
            
            conn.close()
            
            assessment = {
                "intervention_needed": False,
                "intervention_type": None,
                "message": None
            }
            
            # Check for low mood
            if recent_moods and len(recent_moods) >= 3:
                recent_avg = sum(mood[0] for mood in recent_moods[:3]) / 3
                if recent_avg <= 3:
                    assessment = {
                        "intervention_needed": True,
                        "intervention_type": "low_mood",
                        "message": random.choice(self.intervention_messages["low_mood"])
                    }
            
            # Check for absence
            if last_activity:
                try:
                    last_dt = datetime.fromisoformat(last_activity.replace('Z', '+00:00'))
                    hours_since = (datetime.now() - last_dt).total_seconds() / 3600
                    
                    if hours_since > 48:
                        assessment = {
                            "intervention_needed": True,
                            "intervention_type": "long_absence",
                            "message": random.choice(self.intervention_messages["long_absence"])
                        }
                except Exception:
                    pass
            
            return assessment
            
        except Exception as e:
            return {"intervention_needed": False, "error": str(e)}
    
    def generate_celebration_message(self) -> str:
        """🎉 Generate celebration message"""
        return random.choice(self.intervention_messages["celebration"])

#!/usr/bin/env python3
"""
🧠💎⚡ DOPAMINE GUARDIAN ADVANCED ANALYTICS MODULE ⚡💎🧠
"""

import sqlite3
from datetime import datetime, timedelta

class AdvancedMoodAnalytics:
    """🧠 Advanced mood pattern analysis"""
    
    def __init__(self, db_path: str):
        self.db_path = db_path
        
    def analyze_mood_trends(self, user_id: str, days: int = 30) -> dict:
        """📈 Analyze mood trends for user"""
        
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT mood, timestamp FROM mood_checkins 
                WHERE user_id = ? AND timestamp >= datetime('now', '-{} days')
                ORDER BY timestamp
            """.format(days), (user_id,))
            
            mood_data = cursor.fetchall()
            conn.close()
            
            if len(mood_data) < 3:
                return {
                    "status": "insufficient_data",
                    "message": "Need more mood data for analysis"
                }
            
            # Calculate basic trends
            moods = [row[0] for row in mood_data]
            avg_mood = sum(moods) / len(moods)
            
            # Simple trend detection
            recent_moods = moods[-5:] if len(moods) >= 5 else moods
            earlier_moods = moods[:-5] if len(moods) >= 10 else moods[:len(moods)//2]
            
            if len(earlier_moods) > 0:
                recent_avg = sum(recent_moods) / len(recent_moods)
                earlier_avg = sum(earlier_moods) / len(earlier_moods)
                trend_direction = "improving" if recent_avg > earlier_avg + 0.5 else "declining" if recent_avg < earlier_avg - 0.5 else "stable"
            else:
                trend_direction = "stable"
            
            return {
                "trend_direction": trend_direction,
                "avg_mood": round(avg_mood, 1),
                "data_points": len(mood_data),
                "recommendations": self.generate_recommendations(trend_direction, avg_mood)
            }
            
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    def generate_recommendations(self, trend: str, avg_mood: float) -> list:
        """💡 Generate recommendations"""
        
        recommendations = []
        
        if trend == "declining":
            recommendations.extend([
                "Consider scheduling more self-care activities",
                "Focus on activities that previously boosted your mood"
            ])
        elif trend == "improving":
            recommendations.extend([
                "Great momentum! Keep doing what's working",
                "Perfect time to build healthy routines"
            ])
        
        if avg_mood < 4:
            recommendations.append("Gentle reminder: Small steps count!")
        elif avg_mood > 7:
            recommendations.append("Your positive energy is contagious!")
        
        return recommendations

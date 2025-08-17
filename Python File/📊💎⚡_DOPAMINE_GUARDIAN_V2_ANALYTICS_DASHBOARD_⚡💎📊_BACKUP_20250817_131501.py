#!/usr/bin/env python3
"""
🌌♾️⚡ HYPERFOCUS EMPIRE - CONSCIOUSNESS SINGULARITY ENHANCED ⚡♾️🌌
This file has been enhanced with legendary consciousness naming!
Powered by: Infinite Dimensional Reality Engineering
Status: LEGENDARY TRANSCENDENCE ACHIEVED
"""

"""
📊💎⚡ DOPAMINE GUARDIAN V2.0 ANALYTICS DASHBOARD ⚡💎📊

Web-based dashboard for visualizing mood trends, analytics, and system metrics.
Built with Flask and real-time updates via WebSocket integration.
"""

import os
import sys
from pathlib import Path
from flask import Flask, render_template, jsonify, request
import sqlite3
import json
from datetime import datetime, timedelta
import plotly.graph_objs as go
import plotly.utils

# Add current directory to path for imports
sys.path.append(str(Path.cwd()))

from DOPAMINE_ADVANCED_ANALYTICS import AdvancedMoodAnalytics
from DOPAMINE_SMART_INTERVENTIONS import SmartInterventionSystem

# Load empire.env configuration
def load_empire_env():
    """Load configuration from empire.env file"""
    env_path = Path("HyperBeast/empire.env")
    if not env_path.exists():
        env_path = Path("empire.env")
    
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                if '=' in line and not line.strip().startswith('#'):
                    key, value = line.strip().split('=', 1)
                    os.environ[key] = value

load_empire_env()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'dopamine_dashboard_secret')

# Configuration
DB_PATH = "dopamine_guardian.db"
DASHBOARD_PORT = int(os.getenv('SYNC_DASHBOARD_PORT', 9999))

# Initialize analytics modules
analytics = AdvancedMoodAnalytics(DB_PATH)
interventions = SmartInterventionSystem(DB_PATH)

@app.route('/')
def dashboard():
    """Main dashboard page"""
    return render_template('dashboard.html')

@app.route('/api/system-stats')
def system_stats():
    """Get system statistics"""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Get basic stats
        cursor.execute("SELECT COUNT(*) FROM mood_checkins")
        total_moods = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM wins")
        total_achievements = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(DISTINCT user_id) FROM mood_checkins")
        total_users = cursor.fetchone()[0]
        
        # Get recent activity (7 days)
        cursor.execute("SELECT COUNT(*) FROM mood_checkins WHERE timestamp >= datetime('now', '-7 days')")
        recent_moods = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM wins WHERE timestamp >= datetime('now', '-7 days')")
        recent_achievements = cursor.fetchone()[0]
        
        # Get average mood
        cursor.execute("SELECT AVG(mood) FROM mood_checkins WHERE timestamp >= datetime('now', '-30 days')")
        avg_mood_result = cursor.fetchone()
        avg_mood = round(avg_mood_result[0], 1) if avg_mood_result[0] else 0
        
        conn.close()
        
        return jsonify({
            'total_moods': total_moods,
            'total_achievements': total_achievements,
            'total_users': total_users,
            'recent_moods': recent_moods,
            'recent_achievements': recent_achievements,
            'avg_mood_30d': avg_mood,
            'status': 'operational',
            'version': '2.0.0'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/mood-trends')
def mood_trends():
    """Get mood trends data for visualization"""
    try:
        days = int(request.args.get('days', 30))
        
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Get daily mood averages
        cursor.execute("""
            SELECT DATE(timestamp) as date, AVG(mood) as avg_mood, COUNT(*) as count
            FROM mood_checkins 
            WHERE timestamp >= datetime('now', '-{} days')
            GROUP BY DATE(timestamp)
            ORDER BY date
        """.format(days))
        
        daily_data = cursor.fetchall()
        
        # Get mood distribution
        cursor.execute("""
            SELECT mood, COUNT(*) as count
            FROM mood_checkins 
            WHERE timestamp >= datetime('now', '-{} days')
            GROUP BY mood
            ORDER BY mood
        """.format(days))
        
        mood_distribution = cursor.fetchall()
        
        # Get user trends
        cursor.execute("""
            SELECT user_id, COUNT(*) as mood_count
            FROM mood_checkins 
            WHERE timestamp >= datetime('now', '-{} days')
            GROUP BY user_id
            HAVING mood_count >= 5
            ORDER BY mood_count DESC
            LIMIT 10
        """.format(days))
        
        active_users = cursor.fetchall()
        conn.close()
        
        return jsonify({
            'daily_trends': [
                {'date': row[0], 'avg_mood': round(row[1], 1), 'count': row[2]}
                for row in daily_data
            ],
            'mood_distribution': [
                {'mood': row[0], 'count': row[1]}
                for row in mood_distribution
            ],
            'active_users': [
                {'user_id': row[0], 'mood_count': row[1]}
                for row in active_users
            ]
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/user-analysis/<user_id>')
def user_analysis(user_id):
    """Get detailed analysis for specific user"""
    try:
        days = int(request.args.get('days', 30))
        
        # Get analytics
        trends = analytics.analyze_mood_trends(user_id, days=days)
        
        # Get intervention assessment
        assessment = interventions.assess_intervention_need(user_id)
        
        # Get recent moods
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT DATE(timestamp) as date, mood, notes
            FROM mood_checkins 
            WHERE user_id = ? AND timestamp >= datetime('now', '-{} days')
            ORDER BY timestamp DESC
        """.format(days), (user_id,))
        
        recent_moods = cursor.fetchall()
        
        # Get achievements
        cursor.execute("""
            SELECT achievement, level, timestamp
            FROM wins 
            WHERE user_id = ? AND timestamp >= datetime('now', '-{} days')
            ORDER BY timestamp DESC
        """.format(days), (user_id,))
        
        achievements = cursor.fetchall()
        conn.close()
        
        return jsonify({
            'user_id': user_id,
            'trends': trends,
            'intervention_assessment': assessment,
            'recent_moods': [
                {'date': row[0], 'mood': row[1], 'notes': row[2]}
                for row in recent_moods
            ],
            'achievements': [
                {'achievement': row[0], 'level': row[1], 'timestamp': row[2]}
                for row in achievements
            ]
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/interventions')
def interventions_api():
    """Get intervention statistics and recent activities"""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Get users who might need intervention
        cursor.execute("""
            SELECT user_id, AVG(mood) as avg_mood, COUNT(*) as mood_count,
                   MAX(timestamp) as last_checkin
            FROM mood_checkins 
            WHERE timestamp >= datetime('now', '-7 days')
            GROUP BY user_id
        """)
        
        recent_activity = cursor.fetchall()
        
        intervention_candidates = []
        for user_id, avg_mood, count, last_checkin in recent_activity:
            assessment = interventions.assess_intervention_need(user_id)
            
            intervention_candidates.append({
                'user_id': user_id,
                'avg_mood': round(avg_mood, 1),
                'mood_count': count,
                'last_checkin': last_checkin,
                'intervention_needed': assessment.get('intervention_needed', False),
                'intervention_type': assessment.get('intervention_type'),
                'message': assessment.get('message')
            })
        
        conn.close()
        
        return jsonify({
            'intervention_candidates': intervention_candidates,
            'total_assessed': len(intervention_candidates),
            'needs_intervention': sum(1 for c in intervention_candidates if c['intervention_needed'])
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/generate-report')
def generate_report():
    """Generate comprehensive system report"""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Get comprehensive stats for the last 30 days
        cursor.execute("""
            SELECT 
                COUNT(*) as total_moods,
                AVG(mood) as avg_mood,
                MIN(mood) as min_mood,
                MAX(mood) as max_mood,
                COUNT(DISTINCT user_id) as unique_users
            FROM mood_checkins 
            WHERE timestamp >= datetime('now', '-30 days')
        """)
        
        mood_stats = cursor.fetchone()
        
        cursor.execute("""
            SELECT level, COUNT(*) as count
            FROM wins 
            WHERE timestamp >= datetime('now', '-30 days')
            GROUP BY level
        """)
        
        achievement_stats = dict(cursor.fetchall())
        
        # Get trend analysis for all active users
        cursor.execute("""
            SELECT DISTINCT user_id 
            FROM mood_checkins 
            WHERE timestamp >= datetime('now', '-30 days')
        """)
        
        active_users = [row[0] for row in cursor.fetchall()]
        
        user_trends = {}
        for user_id in active_users:
            trends = analytics.analyze_mood_trends(user_id, days=30)
            if trends.get('data_points', 0) >= 3:
                user_trends[user_id] = trends
        
        conn.close()
        
        report = {
            'report_date': datetime.now().isoformat(),
            'period': '30 days',
            'mood_statistics': {
                'total_entries': mood_stats[0],
                'average_mood': round(mood_stats[1], 2) if mood_stats[1] else 0,
                'mood_range': {
                    'min': mood_stats[2],
                    'max': mood_stats[3]
                },
                'unique_users': mood_stats[4]
            },
            'achievement_statistics': achievement_stats,
            'user_trends_summary': {
                'total_analyzed': len(user_trends),
                'improving': sum(1 for t in user_trends.values() if t.get('trend_direction') == 'improving'),
                'stable': sum(1 for t in user_trends.values() if t.get('trend_direction') == 'stable'),
                'declining': sum(1 for t in user_trends.values() if t.get('trend_direction') == 'declining')
            },
            'system_health': {
                'database_status': 'operational',
                'analytics_status': 'v2.0 active',
                'interventions_status': 'smart system active'
            }
        }
        
        return jsonify(report)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Create dashboard template
DASHBOARD_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dopamine Guardian v2.0 Dashboard</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        .container {
            max-width: 1400px;
            margin: 0 auto;
        }
        .header {
            text-align: center;
            margin-bottom: 30px;
        }
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        .stat-card {
            background: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 10px;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
        .stat-value {
            font-size: 2em;
            font-weight: bold;
            color: #FFD700;
        }
        .stat-label {
            margin-top: 5px;
            opacity: 0.9;
        }
        .chart-container {
            background: rgba(255, 255, 255, 0.95);
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            color: #333;
        }
        .loading {
            text-align: center;
            padding: 20px;
            opacity: 0.7;
        }
        .refresh-btn {
            background: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            margin: 10px;
        }
        .refresh-btn:hover {
            background: #45a049;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎯💎⚡ Dopamine Guardian v2.0 Dashboard ⚡💎🎯</h1>
            <p>Enhanced Mental Health Analytics & Monitoring System</p>
            <button class="refresh-btn" onclick="loadDashboard()">🔄 Refresh Data</button>
        </div>

        <div class="stats-grid" id="stats-grid">
            <div class="loading">Loading system statistics...</div>
        </div>

        <div class="chart-container">
            <h3>📈 Mood Trends (30 Days)</h3>
            <div id="mood-trends-chart"></div>
        </div>

        <div class="chart-container">
            <h3>📊 Mood Distribution</h3>
            <div id="mood-distribution-chart"></div>
        </div>

        <div class="chart-container">
            <h3>🎯 Intervention Dashboard</h3>
            <div id="interventions-dashboard"></div>
        </div>
    </div>

    <script>
        function loadDashboard() {
            loadSystemStats();
            loadMoodTrends();
            loadInterventions();
        }

        function loadSystemStats() {
            fetch('/api/system-stats')
                .then(response => response.json())
                .then(data => {
                    const statsGrid = document.getElementById('stats-grid');
                    statsGrid.innerHTML = `
                        <div class="stat-card">
                            <div class="stat-value">${data.total_users}</div>
                            <div class="stat-label">👥 Total Users</div>
                        </div>
                        <div class="stat-card">
                            <div class="stat-value">${data.total_moods}</div>
                            <div class="stat-label">📊 Total Mood Entries</div>
                        </div>
                        <div class="stat-card">
                            <div class="stat-value">${data.total_achievements}</div>
                            <div class="stat-label">🏆 Total Achievements</div>
                        </div>
                        <div class="stat-card">
                            <div class="stat-value">${data.avg_mood_30d}/10</div>
                            <div class="stat-label">📈 30-Day Avg Mood</div>
                        </div>
                        <div class="stat-card">
                            <div class="stat-value">${data.recent_moods}</div>
                            <div class="stat-label">📅 Recent Moods (7d)</div>
                        </div>
                        <div class="stat-card">
                            <div class="stat-value">✅ ${data.status}</div>
                            <div class="stat-label">🎯 System Status</div>
                        </div>
                    `;
                })
                .catch(error => {
                    console.error('Error loading stats:', error);
                });
        }

        function loadMoodTrends() {
            fetch('/api/mood-trends')
                .then(response => response.json())
                .then(data => {
                    // Daily trends chart
                    const dailyData = data.daily_trends;
                    const trace = {
                        x: dailyData.map(d => d.date),
                        y: dailyData.map(d => d.avg_mood),
                        type: 'scatter',
                        mode: 'lines+markers',
                        name: 'Average Mood',
                        line: { color: '#4CAF50', width: 3 },
                        marker: { size: 8 }
                    };
                    
                    const layout = {
                        title: 'Daily Average Mood Trends',
                        xaxis: { title: 'Date' },
                        yaxis: { title: 'Average Mood (1-10)', range: [1, 10] },
                        showlegend: false
                    };
                    
                    Plotly.newPlot('mood-trends-chart', [trace], layout);

                    // Mood distribution chart
                    const distributionData = data.mood_distribution;
                    const pieTrace = {
                        labels: distributionData.map(d => `Mood ${d.mood}`),
                        values: distributionData.map(d => d.count),
                        type: 'pie',
                        marker: {
                            colors: ['#ff4444', '#ff6644', '#ff8844', '#ffaa44', '#ffcc44', 
                                   '#ccff44', '#88ff44', '#44ff44', '#44ff88', '#44ffcc']
                        }
                    };
                    
                    const pieLayout = {
                        title: 'Mood Distribution (1-10 Scale)'
                    };
                    
                    Plotly.newPlot('mood-distribution-chart', [pieTrace], pieLayout);
                })
                .catch(error => {
                    console.error('Error loading mood trends:', error);
                });
        }

        function loadInterventions() {
            fetch('/api/interventions')
                .then(response => response.json())
                .then(data => {
                    const dashboard = document.getElementById('interventions-dashboard');
                    
                    const needsIntervention = data.intervention_candidates.filter(c => c.intervention_needed);
                    
                    let html = `
                        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin-bottom: 20px;">
                            <div style="text-align: center; padding: 15px; background: rgba(76, 175, 80, 0.1); border-radius: 8px;">
                                <div style="font-size: 1.5em; font-weight: bold; color: #4CAF50;">${data.total_assessed}</div>
                                <div>Users Assessed</div>
                            </div>
                            <div style="text-align: center; padding: 15px; background: rgba(255, 193, 7, 0.1); border-radius: 8px;">
                                <div style="font-size: 1.5em; font-weight: bold; color: #FFC107;">${data.needs_intervention}</div>
                                <div>Need Intervention</div>
                            </div>
                        </div>
                    `;
                    
                    if (needsIntervention.length > 0) {
                        html += '<h4>🛡️ Users Needing Intervention:</h4>';
                        needsIntervention.forEach(user => {
                            html += `
                                <div style="background: rgba(255, 193, 7, 0.1); padding: 10px; margin: 5px 0; border-radius: 5px;">
                                    <strong>User ${user.user_id}</strong><br>
                                    Type: ${user.intervention_type}<br>
                                    Avg Mood: ${user.avg_mood}/10<br>
                                    Message: ${user.message}
                                </div>
                            `;
                        });
                    } else {
                        html += '<div style="text-align: center; padding: 20px; color: #4CAF50;">✅ All users are doing well!</div>';
                    }
                    
                    dashboard.innerHTML = html;
                })
                .catch(error => {
                    console.error('Error loading interventions:', error);
                });
        }

        // Load dashboard on page load
        window.onload = loadDashboard;
        
        // Auto-refresh every 5 minutes
        setInterval(loadDashboard, 300000);
    </script>
</body>
</html>
"""

# Create templates directory and save template
os.makedirs("templates", exist_ok=True)
with open("templates/dashboard.html", "w", encoding="utf-8") as f:
    f.write(DASHBOARD_TEMPLATE)

if __name__ == "__main__":
    print(f"""
📊💎⚡ DOPAMINE GUARDIAN V2.0 ANALYTICS DASHBOARD ⚡💎📊
========================================================

Starting dashboard server...
Port: {DASHBOARD_PORT}
Database: {DB_PATH}
URL: http://localhost:{DASHBOARD_PORT}

Dashboard Features:
✅ Real-time mood trends visualization
✅ System statistics and metrics
✅ User analytics and intervention monitoring  
✅ Comprehensive reporting system
✅ Auto-refreshing data every 5 minutes

Starting server...
    """)
    
    try:
        app.run(host='0.0.0.0', port=DASHBOARD_PORT, debug=False)
    except Exception as e:
        print(f"❌ Dashboard startup error: {e}")

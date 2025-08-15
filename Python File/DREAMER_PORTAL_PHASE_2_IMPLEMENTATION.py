#!/usr/bin/env python3
"""
DREAMER PORTAL PHASE 2 IMPLEMENTATION
====================================
Progress Tracking Dashboard & Achievement System
Following ULTRA-THINKING BOARDROOM Next Phase Strategy
====================================
"""

import json
import datetime
import os
import sqlite3
from flask import Flask, request, jsonify, session
import uuid

class DreamerPortalPhase2:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.secret_key = 'ultra_dreamer_phase2_secret_2025'
        self.db_file = 'dreamer_portal_users.db'  # Reuse Phase 1 database
        self.setup_phase2_database()
        self.setup_phase2_routes()

    def setup_phase2_database(self):
        """Setup Phase 2 database tables for progress tracking"""
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        # Create achievements table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS achievements (
                achievement_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT NOT NULL,
                points INTEGER NOT NULL,
                category TEXT NOT NULL,
                icon TEXT DEFAULT "🏆",
                unlock_condition TEXT NOT NULL
            )
        ''')

        # Create user_achievements table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_achievements (
                user_achievement_id TEXT PRIMARY KEY,
                user_id TEXT NOT NULL,
                achievement_id TEXT NOT NULL,
                earned_date TEXT NOT NULL,
                progress_value INTEGER DEFAULT 0,
                is_completed INTEGER DEFAULT 0,
                FOREIGN KEY (user_id) REFERENCES users (user_id),
                FOREIGN KEY (achievement_id) REFERENCES achievements (achievement_id)
            )
        ''')

        # Create progress_tracking table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS progress_tracking (
                progress_id TEXT PRIMARY KEY,
                user_id TEXT NOT NULL,
                metric_name TEXT NOT NULL,
                metric_value INTEGER NOT NULL,
                date_recorded TEXT NOT NULL,
                category TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (user_id)
            )
        ''')

        # Create user_goals table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_goals (
                goal_id TEXT PRIMARY KEY,
                user_id TEXT NOT NULL,
                goal_title TEXT NOT NULL,
                goal_description TEXT,
                target_value INTEGER NOT NULL,
                current_value INTEGER DEFAULT 0,
                deadline TEXT,
                created_date TEXT NOT NULL,
                status TEXT DEFAULT "active",
                FOREIGN KEY (user_id) REFERENCES users (user_id)
            )
        ''')

        conn.commit()

        # Initialize default achievements
        self.initialize_default_achievements(cursor, conn)

        conn.close()
        print("✅ Phase 2 database tables initialized successfully")

    def initialize_default_achievements(self, cursor, conn):
        """Initialize default achievement system"""
        default_achievements = [
            {
                "achievement_id": "first_dream",
                "name": "Dream Pioneer",
                "description": "Process your first dream in DREAMER Portal",
                "points": 10,
                "category": "Getting Started",
                "icon": "🌙",
                "unlock_condition": "dreams_processed >= 1"
            },
            {
                "achievement_id": "dream_streak_5",
                "name": "Dream Streak Master",
                "description": "Process 5 dreams in DREAMER Portal",
                "points": 25,
                "category": "Consistency",
                "icon": "⚡",
                "unlock_condition": "dreams_processed >= 5"
            },
            {
                "achievement_id": "action_master",
                "name": "Action Plan Champion",
                "description": "Complete 10 action plans successfully",
                "points": 50,
                "category": "Achievement",
                "icon": "🏆",
                "unlock_condition": "completed_actions >= 10"
            },
            {
                "achievement_id": "adhd_optimizer",
                "name": "ADHD Optimization Expert",
                "description": "Use 25 ADHD-optimized strategies",
                "points": 75,
                "category": "Expertise",
                "icon": "🧠",
                "unlock_condition": "adhd_strategies_used >= 25"
            },
            {
                "achievement_id": "legendary_dreamer",
                "name": "LEGENDARY DREAMER",
                "description": "Achieve 100 total achievement points",
                "points": 100,
                "category": "Legendary",
                "icon": "💎",
                "unlock_condition": "total_points >= 100"
            },
            {
                "achievement_id": "weekly_warrior",
                "name": "Weekly Warrior",
                "description": "Process dreams for 7 consecutive days",
                "points": 40,
                "category": "Consistency",
                "icon": "🗓️",
                "unlock_condition": "consecutive_days >= 7"
            }
        ]

        for achievement in default_achievements:
            cursor.execute('''
                INSERT OR IGNORE INTO achievements
                (achievement_id, name, description, points, category, icon, unlock_condition)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                achievement["achievement_id"], achievement["name"], achievement["description"],
                achievement["points"], achievement["category"], achievement["icon"],
                achievement["unlock_condition"]
            ))

        conn.commit()

    def setup_phase2_routes(self):
        """Setup Phase 2 Flask routes"""

        @self.app.route('/api/v2/progress/dashboard', methods=['GET'])
        def get_progress_dashboard():
            """Get comprehensive progress dashboard for user"""
            if 'user_id' not in session:
                return jsonify({'error': 'Not authenticated'}), 401

            try:
                conn = sqlite3.connect(self.db_file)
                cursor = conn.cursor()

                # Get user basic stats
                cursor.execute('''
                    SELECT dreams_processed, progress_level, created_date
                    FROM users WHERE user_id = ?
                ''', (session['user_id'],))
                user_stats = cursor.fetchone()

                if not user_stats:
                    return jsonify({'error': 'User not found'}), 404

                # Get user achievements
                cursor.execute('''
                    SELECT a.name, a.description, a.points, a.icon, a.category, ua.earned_date
                    FROM user_achievements ua
                    JOIN achievements a ON ua.achievement_id = a.achievement_id
                    WHERE ua.user_id = ? AND ua.is_completed = 1
                    ORDER BY ua.earned_date DESC
                ''', (session['user_id'],))
                completed_achievements = cursor.fetchall()

                # Get available achievements (not yet earned)
                cursor.execute('''
                    SELECT a.achievement_id, a.name, a.description, a.points, a.icon, a.category
                    FROM achievements a
                    WHERE a.achievement_id NOT IN (
                        SELECT achievement_id FROM user_achievements
                        WHERE user_id = ? AND is_completed = 1
                    )
                ''', (session['user_id'],))
                available_achievements = cursor.fetchall()

                # Get recent progress tracking
                cursor.execute('''
                    SELECT metric_name, metric_value, date_recorded, category
                    FROM progress_tracking
                    WHERE user_id = ?
                    ORDER BY date_recorded DESC
                    LIMIT 10
                ''', (session['user_id'],))
                recent_progress = cursor.fetchall()

                # Get user goals
                cursor.execute('''
                    SELECT goal_title, goal_description, target_value, current_value,
                           deadline, status, created_date
                    FROM user_goals
                    WHERE user_id = ? AND status = 'active'
                    ORDER BY created_date DESC
                ''', (session['user_id'],))
                active_goals = cursor.fetchall()

                # Calculate total achievement points
                total_points = sum(ach[2] for ach in completed_achievements)

                # Calculate level and progress
                current_level = max(1, total_points // 25)  # Level up every 25 points
                points_to_next_level = (current_level * 25) - total_points

                conn.close()

                # Build dashboard response
                dashboard = {
                    'user_stats': {
                        'dreams_processed': user_stats[0],
                        'progress_level': current_level,
                        'total_points': total_points,
                        'points_to_next_level': max(0, points_to_next_level),
                        'account_age_days': self.calculate_account_age(user_stats[2])
                    },
                    'achievements': {
                        'completed': [
                            {
                                'name': ach[0],
                                'description': ach[1],
                                'points': ach[2],
                                'icon': ach[3],
                                'category': ach[4],
                                'earned_date': ach[5]
                            } for ach in completed_achievements
                        ],
                        'available': [
                            {
                                'achievement_id': ach[0],
                                'name': ach[1],
                                'description': ach[2],
                                'points': ach[3],
                                'icon': ach[4],
                                'category': ach[5]
                            } for ach in available_achievements
                        ],
                        'total_earned': len(completed_achievements),
                        'total_available': len(available_achievements)
                    },
                    'recent_progress': [
                        {
                            'metric': prog[0],
                            'value': prog[1],
                            'date': prog[2],
                            'category': prog[3]
                        } for prog in recent_progress
                    ],
                    'active_goals': [
                        {
                            'title': goal[0],
                            'description': goal[1],
                            'target': goal[2],
                            'current': goal[3],
                            'progress_percentage': (goal[3] / goal[2]) * 100 if goal[2] > 0 else 0,
                            'deadline': goal[4],
                            'status': goal[5],
                            'created': goal[6]
                        } for goal in active_goals
                    ],
                    'dashboard_insights': self.generate_dashboard_insights(user_stats, completed_achievements, active_goals)
                }

                return jsonify({'dashboard': dashboard}), 200

            except Exception as e:
                return jsonify({'error': f'Dashboard fetch failed: {str(e)}'}), 500

        @self.app.route('/api/v2/achievements/check', methods=['POST'])
        def check_achievements():
            """Check and award new achievements for user"""
            if 'user_id' not in session:
                return jsonify({'error': 'Not authenticated'}), 401

            try:
                newly_earned = self.check_and_award_achievements(session['user_id'])
                return jsonify({
                    'newly_earned_achievements': newly_earned,
                    'total_new': len(newly_earned)
                }), 200
            except Exception as e:
                return jsonify({'error': f'Achievement check failed: {str(e)}'}), 500

        @self.app.route('/api/v2/goals/create', methods=['POST'])
        def create_user_goal():
            """Create a new user goal"""
            if 'user_id' not in session:
                return jsonify({'error': 'Not authenticated'}), 401

            data = request.get_json()
            if not data or not all(k in data for k in ['title', 'target_value']):
                return jsonify({'error': 'Missing required fields: title, target_value'}), 400

            try:
                conn = sqlite3.connect(self.db_file)
                cursor = conn.cursor()

                goal_id = f"goal_{str(uuid.uuid4())[:8]}"
                cursor.execute('''
                    INSERT INTO user_goals
                    (goal_id, user_id, goal_title, goal_description, target_value, deadline, created_date)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (
                    goal_id, session['user_id'], data['title'],
                    data.get('description', ''), data['target_value'],
                    data.get('deadline'), datetime.datetime.now().isoformat()
                ))

                conn.commit()
                conn.close()

                return jsonify({
                    'success': True,
                    'goal_id': goal_id,
                    'message': 'Goal created successfully!'
                }), 201

            except Exception as e:
                return jsonify({'error': f'Goal creation failed: {str(e)}'}), 500

        @self.app.route('/api/v2/progress/track', methods=['POST'])
        def track_progress():
            """Track progress metric for user"""
            if 'user_id' not in session:
                return jsonify({'error': 'Not authenticated'}), 401

            data = request.get_json()
            if not data or not all(k in data for k in ['metric_name', 'metric_value', 'category']):
                return jsonify({'error': 'Missing required fields'}), 400

            try:
                conn = sqlite3.connect(self.db_file)
                cursor = conn.cursor()

                progress_id = f"progress_{str(uuid.uuid4())[:8]}"
                cursor.execute('''
                    INSERT INTO progress_tracking
                    (progress_id, user_id, metric_name, metric_value, date_recorded, category)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (
                    progress_id, session['user_id'], data['metric_name'],
                    data['metric_value'], datetime.datetime.now().isoformat(),
                    data['category']
                ))

                conn.commit()
                conn.close()

                # Check for new achievements
                newly_earned = self.check_and_award_achievements(session['user_id'])

                return jsonify({
                    'success': True,
                    'progress_id': progress_id,
                    'newly_earned_achievements': newly_earned,
                    'message': 'Progress tracked successfully!'
                }), 201

            except Exception as e:
                return jsonify({'error': f'Progress tracking failed: {str(e)}'}), 500

        @self.app.route('/api/v2/analytics/overview', methods=['GET'])
        def get_analytics_overview():
            """Get analytics overview for user"""
            if 'user_id' not in session:
                return jsonify({'error': 'Not authenticated'}), 401

            try:
                conn = sqlite3.connect(self.db_file)
                cursor = conn.cursor()

                # Get dream processing trends (last 30 days)
                cursor.execute('''
                    SELECT DATE(created_date) as dream_date, COUNT(*) as dreams_count
                    FROM dream_history
                    WHERE user_id = ? AND created_date >= date('now', '-30 days')
                    GROUP BY DATE(created_date)
                    ORDER BY dream_date
                ''', (session['user_id'],))
                dream_trends = cursor.fetchall()

                # Get achievement progress over time
                cursor.execute('''
                    SELECT DATE(earned_date) as achievement_date, COUNT(*) as achievements_count
                    FROM user_achievements
                    WHERE user_id = ? AND is_completed = 1
                    GROUP BY DATE(earned_date)
                    ORDER BY achievement_date
                ''', (session['user_id'],))
                achievement_trends = cursor.fetchall()

                conn.close()

                analytics = {
                    'dream_processing_trends': [
                        {'date': trend[0], 'count': trend[1]} for trend in dream_trends
                    ],
                    'achievement_trends': [
                        {'date': trend[0], 'count': trend[1]} for trend in achievement_trends
                    ],
                    'summary_stats': {
                        'total_dreams_30_days': sum(trend[1] for trend in dream_trends),
                        'avg_dreams_per_day': sum(trend[1] for trend in dream_trends) / 30 if dream_trends else 0,
                        'achievements_this_month': sum(trend[1] for trend in achievement_trends),
                        'most_productive_day': max(dream_trends, key=lambda x: x[1])[0] if dream_trends else None
                    }
                }

                return jsonify({'analytics': analytics}), 200

            except Exception as e:
                return jsonify({'error': f'Analytics fetch failed: {str(e)}'}), 500

    def calculate_account_age(self, created_date):
        """Calculate account age in days"""
        try:
            created = datetime.datetime.fromisoformat(created_date)
            now = datetime.datetime.now()
            return (now - created).days
        except:
            return 0

    def generate_dashboard_insights(self, user_stats, achievements, goals):
        """Generate intelligent dashboard insights"""
        insights = []

        # Dreams processed insight
        dreams_count = user_stats[0]
        if dreams_count == 0:
            insights.append("🌙 Ready to process your first dream? Start your ADHD optimization journey!")
        elif dreams_count < 5:
            insights.append(f"⚡ Great start! You've processed {dreams_count} dreams. Process 5 to unlock Dream Streak Master!")
        elif dreams_count < 10:
            insights.append(f"🏆 Excellent progress! {dreams_count} dreams processed. You're becoming a DREAMER expert!")
        else:
            insights.append(f"💎 LEGENDARY! {dreams_count} dreams processed - you're a true DREAMER champion!")

        # Achievement insights
        achievement_count = len(achievements)
        if achievement_count == 0:
            insights.append("🎯 Your first achievement awaits! Process a dream to earn 'Dream Pioneer'.")
        elif achievement_count < 3:
            insights.append(f"✅ {achievement_count} achievements earned! You're building momentum.")
        else:
            insights.append(f"🏆 Impressive! {achievement_count} achievements unlocked - you're on fire!")

        # Goals insights
        if not goals:
            insights.append("💡 Consider setting a goal to track your progress and stay motivated!")
        else:
            active_goals = len(goals)
            insights.append(f"🎯 {active_goals} active goals driving your success forward!")

        return insights

    def check_and_award_achievements(self, user_id):
        """Check user progress and award applicable achievements"""
        newly_earned = []

        try:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()

            # Get user stats
            cursor.execute('''
                SELECT dreams_processed, progress_level FROM users WHERE user_id = ?
            ''', (user_id,))
            user_stats = cursor.fetchone()

            if not user_stats:
                return newly_earned

            dreams_processed = user_stats[0]

            # Get all available achievements
            cursor.execute('''
                SELECT achievement_id, name, description, points, icon
                FROM achievements
                WHERE achievement_id NOT IN (
                    SELECT achievement_id FROM user_achievements
                    WHERE user_id = ? AND is_completed = 1
                )
            ''', (user_id,))
            available_achievements = cursor.fetchall()

            # Check each achievement
            for achievement in available_achievements:
                achievement_id, name, description, points, icon = achievement

                should_award = False

                # Simple achievement logic (can be expanded)
                if achievement_id == "first_dream" and dreams_processed >= 1:
                    should_award = True
                elif achievement_id == "dream_streak_5" and dreams_processed >= 5:
                    should_award = True
                elif achievement_id == "action_master" and dreams_processed >= 10:  # Simplified
                    should_award = True

                if should_award:
                    # Award the achievement
                    user_achievement_id = f"user_ach_{str(uuid.uuid4())[:8]}"
                    cursor.execute('''
                        INSERT INTO user_achievements
                        (user_achievement_id, user_id, achievement_id, earned_date, is_completed)
                        VALUES (?, ?, ?, ?, 1)
                    ''', (user_achievement_id, user_id, achievement_id, datetime.datetime.now().isoformat()))

                    newly_earned.append({
                        'name': name,
                        'description': description,
                        'points': points,
                        'icon': icon
                    })

            conn.commit()
            conn.close()

        except Exception as e:
            print(f"Achievement check error: {e}")

        return newly_earned

    def run_phase2_server(self, port=5002):
        """Run the Phase 2 server"""
        print("🚀💎⚡ DREAMER PORTAL PHASE 2 SERVER STARTING ⚡💎🚀")
        print("=" * 60)
        print("🎯 Following ULTRA-THINKING BOARDROOM Next Phase Strategy")
        print("📈 Target: DREAMER Portal 97% → 100% Health")
        print("⚡ Features: Progress tracking, achievements, analytics")
        print(f"🌐 Phase 2 server starting on http://localhost:{port}")
        print()
        print("✅ Phase 2 Endpoints:")
        print("   GET  /api/v2/progress/dashboard - Comprehensive progress dashboard")
        print("   POST /api/v2/achievements/check - Check and award achievements")
        print("   POST /api/v2/goals/create - Create user goals")
        print("   POST /api/v2/progress/track - Track progress metrics")
        print("   GET  /api/v2/analytics/overview - Analytics overview")
        print()
        print("🏆 Phase 2 Achievement System: ACTIVE")
        print("📊 Progress Tracking: DEPLOYED")
        print("🎯 Goal Setting: READY")
        print("📈 Analytics: OPERATIONAL")
        print()

        self.app.run(host='0.0.0.0', port=port, debug=True)

def main():
    """Main execution"""
    print("🎯 ULTRA-THINKING BOARDROOM: DEPLOY PHASE 2")
    print("⚡ Priority: HIGH - Next Phase Implementation")
    print("📈 Expected Health Impact: +1.5%")
    print()

    # Create and start Phase 2 implementation
    phase2 = DreamerPortalPhase2()
    phase2.run_phase2_server(port=5002)

if __name__ == "__main__":
    main()

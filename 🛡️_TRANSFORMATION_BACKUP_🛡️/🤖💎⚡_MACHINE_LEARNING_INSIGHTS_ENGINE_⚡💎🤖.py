#!/usr/bin/env python3
"""
🤖💎⚡ MACHINE LEARNING INSIGHTS ENGINE ⚡💎🤖

LEGENDARY AI-powered productivity insights and predictive analytics!
Following BROski Ultra LOOK-THEN-BUILD System Protocol

MACHINE LEARNING FEATURES:
- 🧠 Productivity pattern analysis
- 📈 Predictive focus recommendations
- 🎯 Personalized ADHD optimization
- 📊 Advanced behavioral insights
- 🔮 Smart goal prediction
- ⚡ Real-time performance analytics
"""

import asyncio
import warnings
from datetime import datetime
from typing import Any, Dict, List

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

warnings.filterwarnings("ignore")

import discord
from discord.ext import tasks


class MachineLearningInsights:
    def __init__(self, bot):
        self.bot = bot

        # 🧠 ML Models
        self.focus_predictor = LinearRegression()
        self.pattern_clusterer = KMeans(n_clusters=5, random_state=42)
        self.scaler = StandardScaler()

        # 📊 Data Storage
        self.user_behaviors = {}
        self.focus_sessions = {}
        self.productivity_patterns = {}

        # 🎯 ADHD-Specific Patterns
        self.adhd_patterns = {
            "hyperfocus_triggers": {
                "time_patterns": [],
                "activity_types": [],
                "environmental_factors": [],
                "energy_levels": [],
            },
            "distraction_patterns": {
                "common_triggers": [],
                "time_vulnerabilities": [],
                "context_factors": [],
                "interruption_frequency": [],
            },
            "optimal_conditions": {
                "best_times": [],
                "ideal_duration": [],
                "preferred_techniques": [],
                "environmental_setup": [],
            },
        }

        # 🔮 Prediction Models
        self.predictions = {}
        self.recommendations = {}

        # 📈 Analytics Cache
        self.analytics_cache = {}
        self.last_model_update = None

        # Start background tasks
        self.update_models.start()
        self.generate_insights.start()

    def get_user_behavior_data(self, user_id: str) -> Dict[str, Any]:
        """📊 Get or create user behavior tracking data"""
        if user_id not in self.user_behaviors:
            self.user_behaviors[user_id] = {
                "focus_sessions": [],
                "productivity_scores": [],
                "daily_patterns": {},
                "weekly_patterns": {},
                "distraction_events": [],
                "optimal_times": [],
                "energy_levels": [],
                "technique_effectiveness": {},
                "environmental_preferences": {},
                "goal_completion_rate": 0.0,
                "streak_patterns": [],
                "break_patterns": [],
                "motivation_triggers": [],
                "stress_indicators": [],
                "flow_state_conditions": [],
                "adhd_specific_data": {
                    "hyperfocus_episodes": [],
                    "attention_switches": [],
                    "sensory_preferences": {},
                    "cognitive_load_patterns": [],
                },
            }
        return self.user_behaviors[user_id]

    def record_focus_session(self, user_id: str, session_data: Dict[str, Any]):
        """📝 Record focus session for ML analysis"""
        behavior_data = self.get_user_behavior_data(user_id)

        # Enhance session data with context
        enhanced_session = {
            **session_data,
            "timestamp": datetime.now().isoformat(),
            "day_of_week": datetime.now().weekday(),
            "hour_of_day": datetime.now().hour,
            "session_quality": self.calculate_session_quality(session_data),
            "productivity_score": self.calculate_productivity_score(session_data),
            "context_factors": self.extract_context_factors(session_data),
        }

        behavior_data["focus_sessions"].append(enhanced_session)
        behavior_data["productivity_scores"].append(
            enhanced_session["productivity_score"]
        )

        # Update daily patterns
        date_key = datetime.now().strftime("%Y-%m-%d")
        if date_key not in behavior_data["daily_patterns"]:
            behavior_data["daily_patterns"][date_key] = []
        behavior_data["daily_patterns"][date_key].append(enhanced_session)

        # Trigger real-time insights
        asyncio.create_task(self.generate_real_time_insights(user_id, enhanced_session))

    def calculate_session_quality(self, session_data: Dict[str, Any]) -> float:
        """🎯 Calculate session quality score (0-1)"""
        quality_factors = {
            "completed": 0.3,
            "minimal_distractions": 0.25,
            "flow_state_achieved": 0.2,
            "goal_progress": 0.15,
            "energy_maintained": 0.1,
        }

        quality_score = 0.0

        # Session completion
        if session_data.get("completed", False):
            quality_score += quality_factors["completed"]

        # Distraction handling
        distractions = session_data.get("distractions", 0)
        if distractions <= 2:
            quality_score += quality_factors["minimal_distractions"]

        # Flow state indicators
        if session_data.get("flow_state", False):
            quality_score += quality_factors["flow_state_achieved"]

        # Goal progress
        progress = session_data.get("goal_progress", 0)
        quality_score += quality_factors["goal_progress"] * (progress / 100)

        # Energy levels
        energy_start = session_data.get("energy_start", 5)
        energy_end = session_data.get("energy_end", 5)
        if energy_end >= energy_start:
            quality_score += quality_factors["energy_maintained"]

        return min(1.0, quality_score)

    def calculate_productivity_score(self, session_data: Dict[str, Any]) -> float:
        """📈 Calculate overall productivity score"""
        base_score = self.calculate_session_quality(session_data) * 100

        # Bonus factors
        bonus = 0
        if session_data.get("duration", 0) >= 25:  # Full pomodoro
            bonus += 10
        if (
            session_data.get("technique") == "hyperfocus"
            and session_data.get("duration", 0) >= 120
        ):
            bonus += 20  # ADHD hyperfocus bonus
        if session_data.get("breakthrough", False):
            bonus += 15

        return min(100.0, base_score + bonus)

    def extract_context_factors(self, session_data: Dict[str, Any]) -> Dict[str, Any]:
        """🔍 Extract contextual factors for pattern analysis"""
        return {
            "environment": session_data.get("environment", "home"),
            "noise_level": session_data.get("noise_level", "quiet"),
            "lighting": session_data.get("lighting", "normal"),
            "temperature": session_data.get("temperature", "comfortable"),
            "tools_used": session_data.get("tools_used", []),
            "technique": session_data.get("technique", "pomodoro"),
            "pre_session_mood": session_data.get("mood_before", "neutral"),
            "post_session_mood": session_data.get("mood_after", "neutral"),
            "caffeine_intake": session_data.get("caffeine", False),
            "exercise_before": session_data.get("exercise_before", False),
        }

    def analyze_productivity_patterns(self, user_id: str) -> Dict[str, Any]:
        """🧠 Analyze user's productivity patterns using ML"""
        behavior_data = self.get_user_behavior_data(user_id)

        if len(behavior_data["focus_sessions"]) < 5:
            return {
                "status": "insufficient_data",
                "message": "Need at least 5 sessions for analysis",
            }

        sessions_df = pd.DataFrame(behavior_data["focus_sessions"])

        # Time-based patterns
        time_patterns = self.analyze_time_patterns(sessions_df)

        # Technique effectiveness
        technique_effectiveness = self.analyze_technique_effectiveness(sessions_df)

        # Optimal conditions
        optimal_conditions = self.find_optimal_conditions(sessions_df)

        # ADHD-specific insights
        adhd_insights = self.analyze_adhd_patterns(sessions_df, behavior_data)

        # Predictive insights
        predictions = self.generate_predictions(sessions_df)

        return {
            "time_patterns": time_patterns,
            "technique_effectiveness": technique_effectiveness,
            "optimal_conditions": optimal_conditions,
            "adhd_insights": adhd_insights,
            "predictions": predictions,
            "overall_trend": self.calculate_trend(sessions_df),
            "recommendations": self.generate_personalized_recommendations(user_id),
        }

    def analyze_time_patterns(self, sessions_df: pd.DataFrame) -> Dict[str, Any]:
        """⏰ Analyze time-based productivity patterns"""
        if sessions_df.empty:
            return {}

        # Hour of day analysis
        hourly_scores = (
            sessions_df.groupby("hour_of_day")["productivity_score"]
            .agg(["mean", "count"])
            .round(2)
        )
        best_hours = hourly_scores.nlargest(3, "mean").index.tolist()

        # Day of week analysis
        daily_scores = (
            sessions_df.groupby("day_of_week")["productivity_score"]
            .agg(["mean", "count"])
            .round(2)
        )
        best_days = daily_scores.nlargest(3, "mean").index.tolist()

        # Weekly trends
        sessions_df["date"] = pd.to_datetime(sessions_df["timestamp"]).dt.date
        weekly_trend = (
            sessions_df.groupby("date")["productivity_score"]
            .mean()
            .rolling(window=7)
            .mean()
        )

        return {
            "best_hours": [int(h) for h in best_hours],
            "best_days": [int(d) for d in best_days],
            "hourly_performance": hourly_scores.to_dict(),
            "weekly_trend": (
                "improving"
                if weekly_trend.iloc[-1] > weekly_trend.iloc[-7]
                else "declining"
            ),
            "consistency_score": sessions_df["productivity_score"].std(),
        }

    def analyze_technique_effectiveness(
        self, sessions_df: pd.DataFrame
    ) -> Dict[str, Any]:
        """🎯 Analyze effectiveness of different focus techniques"""
        if "technique" not in sessions_df.columns:
            return {}

        technique_stats = (
            sessions_df.groupby("technique")
            .agg(
                {
                    "productivity_score": ["mean", "count", "std"],
                    "session_quality": "mean",
                    "duration": "mean",
                }
            )
            .round(2)
        )

        # Find best technique
        best_technique = technique_stats["productivity_score"]["mean"].idxmax()

        # Technique recommendations
        recommendations = {}
        for technique in technique_stats.index:
            score = technique_stats.loc[technique, ("productivity_score", "mean")]
            count = technique_stats.loc[technique, ("productivity_score", "count")]

            if count >= 3:  # Enough data
                if score >= 80:
                    recommendations[technique] = "highly_recommended"
                elif score >= 60:
                    recommendations[technique] = "recommended"
                else:
                    recommendations[technique] = "needs_improvement"

        return {
            "best_technique": best_technique,
            "technique_scores": technique_stats.to_dict(),
            "recommendations": recommendations,
        }

    def find_optimal_conditions(self, sessions_df: pd.DataFrame) -> Dict[str, Any]:
        """🎯 Find optimal conditions for peak performance"""
        high_performance_sessions = sessions_df[sessions_df["productivity_score"] >= 80]

        if high_performance_sessions.empty:
            return {"status": "no_high_performance_sessions"}

        optimal_conditions = {}

        # Analyze context factors for high-performance sessions
        context_columns = ["environment", "noise_level", "lighting", "technique"]

        for column in context_columns:
            if column in high_performance_sessions.columns:
                value_counts = high_performance_sessions[column].value_counts()
                if not value_counts.empty:
                    optimal_conditions[column] = value_counts.index[0]

        # Time-based optimal conditions
        optimal_conditions["best_hour"] = (
            high_performance_sessions["hour_of_day"].mode().iloc[0]
            if not high_performance_sessions["hour_of_day"].mode().empty
            else None
        )
        optimal_conditions["best_day"] = (
            high_performance_sessions["day_of_week"].mode().iloc[0]
            if not high_performance_sessions["day_of_week"].mode().empty
            else None
        )

        return optimal_conditions

    def analyze_adhd_patterns(
        self, sessions_df: pd.DataFrame, behavior_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """🧠 Analyze ADHD-specific productivity patterns"""
        adhd_insights = {
            "hyperfocus_patterns": {},
            "attention_management": {},
            "optimal_session_length": {},
            "distraction_triggers": {},
            "energy_management": {},
        }

        # Hyperfocus detection
        long_sessions = sessions_df[sessions_df["duration"] >= 120]  # 2+ hours
        if not long_sessions.empty:
            hyperfocus_times = long_sessions["hour_of_day"].value_counts()
            adhd_insights["hyperfocus_patterns"] = {
                "common_start_times": hyperfocus_times.index[:3].tolist(),
                "average_duration": long_sessions["duration"].mean(),
                "frequency": len(long_sessions) / len(sessions_df) * 100,
            }

        # Optimal session length analysis
        session_lengths = sessions_df.groupby(
            pd.cut(sessions_df["duration"], bins=[0, 15, 30, 60, 120, float("inf")])
        )["productivity_score"].mean()
        best_length_range = session_lengths.idxmax()
        adhd_insights["optimal_session_length"] = {
            "range": str(best_length_range),
            "average_score": session_lengths.max(),
        }

        # Distraction analysis
        if "distractions" in sessions_df.columns:
            distraction_patterns = sessions_df.groupby("hour_of_day")[
                "distractions"
            ].mean()
            worst_distraction_hours = distraction_patterns.nlargest(3).index.tolist()
            adhd_insights["distraction_triggers"] = {
                "high_risk_hours": [int(h) for h in worst_distraction_hours],
                "average_distractions": sessions_df["distractions"].mean(),
            }

        return adhd_insights

    def generate_predictions(self, sessions_df: pd.DataFrame) -> Dict[str, Any]:
        """🔮 Generate ML-based predictions"""
        if len(sessions_df) < 10:
            return {"status": "insufficient_data"}

        try:
            # Prepare features for prediction
            features = ["hour_of_day", "day_of_week", "duration"]
            X = sessions_df[features].fillna(0)
            y = sessions_df["productivity_score"]

            # Train simple model
            self.focus_predictor.fit(X, y)

            # Predict next session performance
            now = datetime.now()
            next_session_features = np.array([[now.hour, now.weekday(), 25]]).reshape(
                1, -1
            )
            predicted_score = self.focus_predictor.predict(next_session_features)[0]

            # Generate time-based predictions
            time_predictions = {}
            for hour in range(24):
                hour_features = np.array([[hour, now.weekday(), 25]]).reshape(1, -1)
                hour_score = self.focus_predictor.predict(hour_features)[0]
                time_predictions[hour] = max(0, min(100, hour_score))

            best_hours = sorted(
                time_predictions.items(), key=lambda x: x[1], reverse=True
            )[:3]

            return {
                "next_session_score": max(0, min(100, predicted_score)),
                "best_hours_today": [h[0] for h in best_hours],
                "confidence": "moderate" if len(sessions_df) > 20 else "low",
            }

        except Exception as e:
            return {"status": "prediction_error", "error": str(e)}

    def generate_personalized_recommendations(
        self, user_id: str
    ) -> List[Dict[str, Any]]:
        """💡 Generate AI-powered personalized recommendations"""
        behavior_data = self.get_user_behavior_data(user_id)

        if len(behavior_data["focus_sessions"]) < 3:
            return [
                {
                    "type": "data_collection",
                    "priority": "high",
                    "title": "Build Your Productivity Profile",
                    "description": "Complete more focus sessions to unlock personalized AI insights!",
                    "action": "Start tracking your sessions with detailed context (environment, mood, energy)",
                }
            ]

        recommendations = []
        sessions_df = pd.DataFrame(behavior_data["focus_sessions"])

        # Time optimization recommendations
        if "hour_of_day" in sessions_df.columns:
            hourly_avg = sessions_df.groupby("hour_of_day")["productivity_score"].mean()
            best_hour = hourly_avg.idxmax()
            worst_hour = hourly_avg.idxmin()

            if hourly_avg[best_hour] - hourly_avg[worst_hour] > 20:
                recommendations.append(
                    {
                        "type": "time_optimization",
                        "priority": "high",
                        "title": f"Schedule Focus Time at {best_hour}:00",
                        "description": f"Your productivity peaks at {best_hour}:00 (avg: {hourly_avg[best_hour]:.1f}/100)",
                        "action": f"Block {best_hour}:00-{best_hour+2}:00 for your most important work",
                    }
                )

        # Technique optimization
        if (
            "technique" in sessions_df.columns
            and len(sessions_df["technique"].unique()) > 1
        ):
            technique_scores = sessions_df.groupby("technique")[
                "productivity_score"
            ].mean()
            best_technique = technique_scores.idxmax()

            recommendations.append(
                {
                    "type": "technique_optimization",
                    "priority": "medium",
                    "title": f"Focus on {best_technique.title()} Technique",
                    "description": f"{best_technique.title()} gives you the best results (avg: {technique_scores[best_technique]:.1f}/100)",
                    "action": f"Use {best_technique} for your next 3 focus sessions",
                }
            )

        # Session length optimization
        if sessions_df["duration"].std() > 15:  # Variable session lengths
            optimal_length = sessions_df.loc[
                sessions_df["productivity_score"].idxmax(), "duration"
            ]

            recommendations.append(
                {
                    "type": "duration_optimization",
                    "priority": "medium",
                    "title": f"Optimize Session Length to {optimal_length} Minutes",
                    "description": f"Your highest-scoring session lasted {optimal_length} minutes",
                    "action": f"Try {optimal_length}-minute sessions for the next week",
                }
            )

        # ADHD-specific recommendations
        long_sessions = sessions_df[sessions_df["duration"] >= 120]
        if len(long_sessions) > 0:
            avg_hyperfocus_score = long_sessions["productivity_score"].mean()
            if avg_hyperfocus_score > sessions_df["productivity_score"].mean() + 10:
                recommendations.append(
                    {
                        "type": "adhd_hyperfocus",
                        "priority": "high",
                        "title": "Embrace Your Hyperfocus Superpower",
                        "description": f"Your 2+ hour sessions score {avg_hyperfocus_score:.1f}/100 on average!",
                        "action": "When you feel hyperfocus coming on, clear your schedule and lean into it",
                    }
                )

        # Consistency recommendations
        if sessions_df["productivity_score"].std() > 25:  # High variability
            recommendations.append(
                {
                    "type": "consistency",
                    "priority": "medium",
                    "title": "Build More Consistent Performance",
                    "description": "Your productivity varies significantly between sessions",
                    "action": "Focus on replicating conditions from your highest-scoring sessions",
                }
            )

        return recommendations[:5]  # Top 5 recommendations

    async def generate_real_time_insights(
        self, user_id: str, session_data: Dict[str, Any]
    ):
        """⚡ Generate real-time insights after each session"""
        behavior_data = self.get_user_behavior_data(user_id)

        # Quick pattern detection
        recent_sessions = behavior_data["focus_sessions"][-5:]  # Last 5 sessions
        if len(recent_sessions) >= 3:
            scores = [s.get("productivity_score", 0) for s in recent_sessions]

            # Trend detection
            if len(scores) >= 3:
                trend = "improving" if scores[-1] > scores[-3] else "declining"

                # Store insight for next command call
                insight = {
                    "type": "trend_alert",
                    "trend": trend,
                    "current_score": scores[-1],
                    "change": scores[-1] - scores[-3] if len(scores) >= 3 else 0,
                    "timestamp": datetime.now().isoformat(),
                }

                if user_id not in self.predictions:
                    self.predictions[user_id] = []
                self.predictions[user_id].append(insight)

    @tasks.loop(hours=6)
    async def update_models(self):
        """🔄 Update ML models with latest data"""
        try:
            # Update models for users with sufficient data
            for user_id, behavior_data in self.user_behaviors.items():
                if len(behavior_data["focus_sessions"]) >= 20:
                    # Update user-specific models
                    sessions_df = pd.DataFrame(behavior_data["focus_sessions"])

                    # Feature engineering
                    if not sessions_df.empty:
                        X = sessions_df[
                            ["hour_of_day", "day_of_week", "duration"]
                        ].fillna(0)
                        y = sessions_df["productivity_score"]

                        # Update prediction model
                        if len(X) >= 10:
                            self.focus_predictor.fit(X, y)

            self.last_model_update = datetime.now().isoformat()

        except Exception as e:
            print(f"Model update error: {e}")

    @tasks.loop(hours=24)
    async def generate_insights(self):
        """📊 Generate daily insights for all users"""
        try:
            for user_id, behavior_data in self.user_behaviors.items():
                if len(behavior_data["focus_sessions"]) >= 5:
                    # Generate comprehensive analysis
                    analysis = self.analyze_productivity_patterns(user_id)

                    # Store insights
                    if user_id not in self.analytics_cache:
                        self.analytics_cache[user_id] = {}

                    self.analytics_cache[user_id]["daily_insights"] = {
                        "analysis": analysis,
                        "generated_at": datetime.now().isoformat(),
                    }

        except Exception as e:
            print(f"Insight generation error: {e}")

    def setup_ml_commands(self):
        """🤖 Setup machine learning commands"""

        @self.bot.command(name="insights")
        async def show_ml_insights(ctx, analysis_type: str = "overview"):
            """🧠 Show AI-powered productivity insights"""
            user_id = str(ctx.author.id)

            if analysis_type == "overview":
                analysis = self.analyze_productivity_patterns(user_id)

                if analysis.get("status") == "insufficient_data":
                    embed = discord.Embed(
                        title="🤖 AI INSIGHTS - LEARNING MODE",
                        description="The AI is learning your patterns! Complete more focus sessions to unlock powerful insights.",
                        color=0x9370DB,
                    )

                    embed.add_field(
                        name="🎯 What We're Learning",
                        value="• Your optimal focus times\n• Best productivity techniques\n• ADHD-specific patterns\n• Environmental preferences\n• Energy management",
                        inline=False,
                    )

                    embed.add_field(
                        name="📊 Current Progress",
                        value=f"Sessions completed: {len(self.get_user_behavior_data(user_id)['focus_sessions'])}\nSessions needed: 5 minimum",
                        inline=False,
                    )

                    await ctx.send(embed=embed)
                    return

                embed = discord.Embed(
                    title="🤖 AI PRODUCTIVITY INSIGHTS",
                    description=f"**{ctx.author.mention}'s** personalized AI analysis",
                    color=0x00CED1,
                )

                # Time patterns
                if "time_patterns" in analysis:
                    time_data = analysis["time_patterns"]
                    best_hours = time_data.get("best_hours", [])
                    hours_text = ", ".join([f"{h}:00" for h in best_hours[:3]])

                    embed.add_field(
                        name="⏰ Optimal Time Patterns",
                        value=f"**Best Hours:** {hours_text}\n**Trend:** {time_data.get('weekly_trend', 'analyzing')}\n**Consistency:** {time_data.get('consistency_score', 0):.1f}",
                        inline=True,
                    )

                # Technique effectiveness
                if "technique_effectiveness" in analysis:
                    tech_data = analysis["technique_effectiveness"]
                    best_tech = tech_data.get("best_technique", "unknown")

                    embed.add_field(
                        name="🎯 Best Technique",
                        value=f"**{best_tech.title()}**\nOptimized for your brain!",
                        inline=True,
                    )

                # ADHD insights
                if "adhd_insights" in analysis:
                    adhd_data = analysis["adhd_insights"]

                    if (
                        "hyperfocus_patterns" in adhd_data
                        and adhd_data["hyperfocus_patterns"]
                    ):
                        hf_data = adhd_data["hyperfocus_patterns"]
                        embed.add_field(
                            name="⚡ Hyperfocus Power",
                            value=f"**Frequency:** {hf_data.get('frequency', 0):.1f}%\n**Avg Duration:** {hf_data.get('average_duration', 0):.0f} min",
                            inline=True,
                        )

                # Predictions
                if (
                    "predictions" in analysis
                    and analysis["predictions"].get("status") != "insufficient_data"
                ):
                    pred_data = analysis["predictions"]
                    next_score = pred_data.get("next_session_score", 0)
                    confidence = pred_data.get("confidence", "low")

                    embed.add_field(
                        name="🔮 AI Predictions",
                        value=f"**Next Session:** {next_score:.0f}/100\n**Confidence:** {confidence.title()}\n**Best Hours Today:** {', '.join([f'{h}:00' for h in pred_data.get('best_hours_today', [])[:2]])}",
                        inline=False,
                    )

                # Recommendations
                recommendations = analysis.get("recommendations", [])
                if recommendations:
                    rec_text = ""
                    for i, rec in enumerate(recommendations[:3]):
                        priority_emoji = (
                            "🔥"
                            if rec["priority"] == "high"
                            else "⚡" if rec["priority"] == "medium" else "💡"
                        )
                        rec_text += f"{priority_emoji} **{rec['title']}**\n_{rec['description']}_\n\n"

                    embed.add_field(
                        name="💡 AI Recommendations", value=rec_text, inline=False
                    )

                embed.set_footer(
                    text=f"Analysis based on {len(self.get_user_behavior_data(user_id)['focus_sessions'])} sessions"
                )

                await ctx.send(embed=embed)

        @self.bot.command(name="predict")
        async def show_predictions(ctx, hours_ahead: int = 1):
            """🔮 Show AI predictions for upcoming focus sessions"""
            user_id = str(ctx.author.id)
            behavior_data = self.get_user_behavior_data(user_id)

            if len(behavior_data["focus_sessions"]) < 10:
                await ctx.send(
                    "🤖 Need at least 10 sessions to generate reliable predictions! Keep focusing! 💪"
                )
                return

            sessions_df = pd.DataFrame(behavior_data["focus_sessions"])
            predictions = self.generate_predictions(sessions_df)

            if predictions.get("status") == "insufficient_data":
                await ctx.send("📊 Gathering more data for accurate predictions...")
                return

            embed = discord.Embed(
                title="🔮 AI FOCUS PREDICTIONS",
                description=f"**{ctx.author.mention}'s** upcoming productivity forecast",
                color=0xFF6347,
            )

            # Current prediction
            current_score = predictions.get("next_session_score", 0)
            confidence = predictions.get("confidence", "low")

            score_emoji = (
                "🔥" if current_score >= 80 else "⚡" if current_score >= 60 else "💪"
            )

            embed.add_field(
                name="🎯 Next Session Prediction",
                value=f"{score_emoji} **{current_score:.0f}/100** productivity score\n**Confidence:** {confidence.title()}",
                inline=False,
            )

            # Best hours today
            best_hours = predictions.get("best_hours_today", [])
            if best_hours:
                hours_text = "\n".join(
                    [
                        f"• {h}:00 - Predicted score: {predictions.get('time_predictions', {}).get(h, 'N/A')}"
                        for h in best_hours[:5]
                    ]
                )
                embed.add_field(
                    name="⏰ Best Times Today", value=hours_text, inline=False
                )

            # Real-time insights
            recent_insights = self.predictions.get(user_id, [])
            if recent_insights:
                latest_insight = recent_insights[-1]
                trend = latest_insight.get("trend", "stable")
                change = latest_insight.get("change", 0)

                trend_emoji = (
                    "📈"
                    if trend == "improving"
                    else "📉" if trend == "declining" else "➡️"
                )

                embed.add_field(
                    name="📊 Recent Trend",
                    value=f"{trend_emoji} **{trend.title()}** trend\nChange: {change:+.1f} points",
                    inline=True,
                )

            embed.add_field(
                name="💡 AI Tip",
                value="Predictions improve with more data! Keep tracking your sessions for better accuracy.",
                inline=False,
            )

            await ctx.send(embed=embed)

        @self.bot.command(name="patterns")
        async def show_patterns(ctx, pattern_type: str = "all"):
            """📊 Show detailed productivity patterns"""
            user_id = str(ctx.author.id)
            behavior_data = self.get_user_behavior_data(user_id)

            if len(behavior_data["focus_sessions"]) < 5:
                await ctx.send(
                    "📊 Complete at least 5 focus sessions to see your patterns!"
                )
                return

            sessions_df = pd.DataFrame(behavior_data["focus_sessions"])

            embed = discord.Embed(
                title="📊 PRODUCTIVITY PATTERNS ANALYSIS",
                description=f"**{ctx.author.mention}'s** detailed behavioral insights",
                color=0x4169E1,
            )

            if pattern_type in ["all", "time"]:
                # Time patterns
                hourly_avg = sessions_df.groupby("hour_of_day")[
                    "productivity_score"
                ].mean()
                peak_hours = hourly_avg.nlargest(3).index.tolist()
                low_hours = hourly_avg.nsmallest(3).index.tolist()

                embed.add_field(
                    name="⏰ Time Patterns",
                    value=f"**Peak Hours:** {', '.join([f'{h}:00' for h in peak_hours])}\n**Low Energy:** {', '.join([f'{h}:00' for h in low_hours])}\n**Best Day:** {['Mon','Tue','Wed','Thu','Fri','Sat','Sun'][sessions_df.groupby('day_of_week')['productivity_score'].mean().idxmax()]}",
                    inline=False,
                )

            if pattern_type in ["all", "adhd"]:
                # ADHD-specific patterns
                analysis = self.analyze_productivity_patterns(user_id)
                adhd_data = analysis.get("adhd_insights", {})

                if adhd_data.get("hyperfocus_patterns"):
                    hf_data = adhd_data["hyperfocus_patterns"]
                    embed.add_field(
                        name="⚡ ADHD Superpowers",
                        value=f"**Hyperfocus Frequency:** {hf_data.get('frequency', 0):.1f}%\n**Average Duration:** {hf_data.get('average_duration', 0):.0f} min\n**Best Start Times:** {', '.join([f'{h}:00' for h in hf_data.get('common_start_times', [])[:2]])}",
                        inline=False,
                    )

                if adhd_data.get("optimal_session_length"):
                    length_data = adhd_data["optimal_session_length"]
                    embed.add_field(
                        name="🎯 Optimal Session Length",
                        value=f"**Best Range:** {length_data.get('range', 'Unknown')}\n**Score:** {length_data.get('average_score', 0):.1f}/100",
                        inline=True,
                    )

            # Session quality distribution
            if "session_quality" in sessions_df.columns:
                quality_stats = sessions_df["session_quality"].describe()
                embed.add_field(
                    name="📈 Quality Statistics",
                    value=f"**Average:** {quality_stats['mean']:.2f}\n**Best:** {quality_stats['max']:.2f}\n**Consistency:** {1 - quality_stats['std']:.2f}",
                    inline=True,
                )

            embed.set_footer(
                text=f"Analysis of {len(sessions_df)} sessions | Updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
            )

            await ctx.send(embed=embed)


# Export the ML insights engine
__all__ = ["MachineLearningInsights"]

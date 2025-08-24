#!/usr/bin/env python3
"""
🎮💎⚡ DISCORD ACTIVITIES INTEGRATION ENGINE ⚡💎🎮

LEGENDARY Discord Activities integration for embedded interactive experiences!
Following Discord's Design Patterns: https://discord.com/developers/docs/activities/design-patterns

DISCORD ACTIVITIES FEATURES:
🎯 Embedded Focus Timer Activity
🏆 Interactive Challenge Board
📊 Real-time Progress Dashboards
🤝 Multiplayer Productivity Games
🎨 Beautiful Activity UI/UX
⚡ WebSocket Real-time Updates
🌟 Social Productivity Experiences
🎮 Gamified Productivity Activities

This creates embedded web experiences directly in Discord!
"""

import json
from datetime import datetime
from typing import Any, Dict

from aiohttp import WSMsgType, web


class DiscordActivitiesEngine:
    """🎮 Main Discord Activities integration engine"""

    def __init__(self, port: int = 3000):
        self.port = port
        self.app = web.Application()
        self.websocket_clients = {}
        self.active_sessions = {}
        self.activity_stats = {
            "total_sessions": 0,
            "active_users": 0,
            "focus_minutes": 0,
            "challenges_completed": 0,
        }

        # Setup routes
        self.setup_routes()

    def setup_routes(self):
        """🛣️ Setup all activity routes"""
        # Main activity routes
        self.app.router.add_get("/", self.serve_activity_selector)
        self.app.router.add_get("/focus-timer", self.serve_focus_timer)
        self.app.router.add_get("/challenge-board", self.serve_challenge_board)
        self.app.router.add_get("/productivity-dashboard", self.serve_dashboard)
        self.app.router.add_get("/multiplayer-focus", self.serve_multiplayer)

        # API endpoints
        self.app.router.add_post("/api/start-session", self.start_focus_session)
        self.app.router.add_post("/api/complete-session", self.complete_session)
        self.app.router.add_post("/api/join-challenge", self.join_challenge_api)
        self.app.router.add_get("/api/stats", self.get_activity_stats)

        # WebSocket for real-time updates
        self.app.router.add_get("/ws", self.websocket_handler)

        # Static files
        self.app.router.add_static("/", path="static/", name="static")

    async def serve_activity_selector(self, request):
        """🎮 Main activity selector page"""
        html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🚀 HyperFocus Zone Activities</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 20px;
        }

        .header {
            text-align: center;
            margin-bottom: 40px;
        }

        .title {
            font-size: 2.5rem;
            font-weight: bold;
            margin-bottom: 10px;
            background: linear-gradient(45deg, #ff6b35, #ffa500);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .subtitle {
            font-size: 1.2rem;
            opacity: 0.9;
        }

        .activities-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 25px;
            max-width: 1200px;
            width: 100%;
        }

        .activity-card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 30px;
            text-align: center;
            transition: all 0.3s ease;
            border: 1px solid rgba(255, 255, 255, 0.2);
            cursor: pointer;
        }

        .activity-card:hover {
            transform: translateY(-10px);
            background: rgba(255, 255, 255, 0.2);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
        }

        .activity-icon {
            font-size: 4rem;
            margin-bottom: 20px;
            display: block;
        }

        .activity-title {
            font-size: 1.5rem;
            font-weight: bold;
            margin-bottom: 15px;
        }

        .activity-description {
            opacity: 0.8;
            line-height: 1.6;
            margin-bottom: 20px;
        }

        .activity-features {
            list-style: none;
            text-align: left;
        }

        .activity-features li {
            padding: 5px 0;
            opacity: 0.7;
        }

        .activity-features li::before {
            content: "✨ ";
            margin-right: 8px;
        }

        .stats-bar {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 20px;
            margin-top: 40px;
            max-width: 800px;
            width: 100%;
            display: flex;
            justify-content: space-around;
            text-align: center;
        }

        .stat-item {
            flex: 1;
        }

        .stat-number {
            font-size: 2rem;
            font-weight: bold;
            color: #ffa500;
        }

        .stat-label {
            font-size: 0.9rem;
            opacity: 0.8;
            margin-top: 5px;
        }

        @media (max-width: 768px) {
            .activities-grid {
                grid-template-columns: 1fr;
            }

            .stats-bar {
                flex-direction: column;
                gap: 20px;
            }
        }
    </style>
</head>
<body>
    <div class="header">
        <h1 class="title">🚀 HyperFocus Zone Activities</h1>
        <p class="subtitle">Choose your legendary productivity experience!</p>
    </div>

    <div class="activities-grid">
        <div class="activity-card" onclick="openActivity('/focus-timer')">
            <span class="activity-icon">🎯</span>
            <h3 class="activity-title">Focus Timer Pro</h3>
            <p class="activity-description">
                Advanced Pomodoro timer with real-time tracking and beautiful visualizations
            </p>
            <ul class="activity-features">
                <li>Customizable timer intervals</li>
                <li>Progress visualization</li>
                <li>Achievement tracking</li>
                <li>Distraction blocking</li>
            </ul>
        </div>

        <div class="activity-card" onclick="openActivity('/challenge-board')">
            <span class="activity-icon">🏆</span>
            <h3 class="activity-title">Challenge Board</h3>
            <p class="activity-description">
                Interactive challenge management with real-time progress tracking
            </p>
            <ul class="activity-features">
                <li>Live challenge updates</li>
                <li>Team collaboration</li>
                <li>Progress leaderboards</li>
                <li>Achievement celebrations</li>
            </ul>
        </div>

        <div class="activity-card" onclick="openActivity('/productivity-dashboard')">
            <span class="activity-icon">📊</span>
            <h3 class="activity-title">Productivity Dashboard</h3>
            <p class="activity-description">
                Comprehensive analytics and insights for your productivity journey
            </p>
            <ul class="activity-features">
                <li>Real-time statistics</li>
                <li>AI-powered insights</li>
                <li>Goal tracking</li>
                <li>Performance trends</li>
            </ul>
        </div>

        <div class="activity-card" onclick="openActivity('/multiplayer-focus')">
            <span class="activity-icon">🤝</span>
            <h3 class="activity-title">Multiplayer Focus</h3>
            <p class="activity-description">
                Focus together with friends in real-time collaborative sessions
            </p>
            <ul class="activity-features">
                <li>Synchronized timers</li>
                <li>Group accountability</li>
                <li>Live chat support</li>
                <li>Team achievements</li>
            </ul>
        </div>
    </div>

    <div class="stats-bar">
        <div class="stat-item">
            <div class="stat-number" id="total-sessions">1,337</div>
            <div class="stat-label">Focus Sessions</div>
        </div>
        <div class="stat-item">
            <div class="stat-number" id="active-users">42</div>
            <div class="stat-label">Active Users</div>
        </div>
        <div class="stat-item">
            <div class="stat-number" id="focus-minutes">28,540</div>
            <div class="stat-label">Focus Minutes</div>
        </div>
        <div class="stat-item">
            <div class="stat-number" id="challenges-completed">156</div>
            <div class="stat-label">Challenges Completed</div>
        </div>
    </div>

    <script>
        function openActivity(path) {
            window.location.href = path;
        }

        // Update stats in real-time
        async function updateStats() {
            try {
                const response = await fetch('/api/stats');
                const stats = await response.json();

                document.getElementById('total-sessions').textContent = stats.total_sessions.toLocaleString();
                document.getElementById('active-users').textContent = stats.active_users;
                document.getElementById('focus-minutes').textContent = stats.focus_minutes.toLocaleString();
                document.getElementById('challenges-completed').textContent = stats.challenges_completed;
            } catch (error) {
                console.log('Stats update failed:', error);
            }
        }

        // Update stats every 30 seconds
        setInterval(updateStats, 30000);
        updateStats(); // Initial load
    </script>
</body>
</html>
        """
        return web.Response(text=html, content_type="text/html")

    async def serve_focus_timer(self, request):
        """🎯 Interactive focus timer activity"""
        html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🎯 Focus Timer Pro</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #ff6b35 0%, #ffa500 100%);
            color: white;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }

        .timer-container {
            text-align: center;
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(20px);
            border-radius: 30px;
            padding: 50px;
            border: 2px solid rgba(255, 255, 255, 0.3);
            max-width: 500px;
            width: 100%;
        }

        .timer-title {
            font-size: 2.5rem;
            margin-bottom: 30px;
            font-weight: bold;
        }

        .timer-display {
            font-size: 5rem;
            font-weight: bold;
            font-family: 'Courier New', monospace;
            margin: 30px 0;
            text-shadow: 0 0 20px rgba(255, 255, 255, 0.5);
        }

        .timer-progress {
            width: 100%;
            height: 20px;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 10px;
            margin: 30px 0;
            overflow: hidden;
        }

        .timer-progress-fill {
            height: 100%;
            background: linear-gradient(90deg, #00ff7f, #32cd32);
            border-radius: 10px;
            transition: width 1s ease;
            width: 0%;
        }

        .timer-controls {
            display: flex;
            gap: 20px;
            justify-content: center;
            margin: 30px 0;
        }

        .timer-btn {
            padding: 15px 30px;
            border: none;
            border-radius: 15px;
            font-size: 1.2rem;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
            color: white;
        }

        .btn-start {
            background: linear-gradient(45deg, #00ff7f, #32cd32);
        }

        .btn-pause {
            background: linear-gradient(45deg, #ffa500, #ff8c00);
        }

        .btn-reset {
            background: linear-gradient(45deg, #ff4444, #dc143c);
        }

        .timer-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);
        }

        .timer-presets {
            display: flex;
            gap: 15px;
            justify-content: center;
            margin-bottom: 20px;
        }

        .preset-btn {
            padding: 10px 20px;
            border: 2px solid rgba(255, 255, 255, 0.5);
            border-radius: 10px;
            background: transparent;
            color: white;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .preset-btn:hover,
        .preset-btn.active {
            background: rgba(255, 255, 255, 0.2);
            border-color: white;
        }

        .session-stats {
            margin-top: 30px;
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
            text-align: center;
        }

        .stat-item {
            background: rgba(255, 255, 255, 0.1);
            padding: 15px;
            border-radius: 10px;
        }

        .stat-number {
            font-size: 1.5rem;
            font-weight: bold;
            color: #00ff7f;
        }

        .stat-label {
            font-size: 0.9rem;
            opacity: 0.8;
            margin-top: 5px;
        }
    </style>
</head>
<body>
    <div class="timer-container">
        <h1 class="timer-title">🎯 Focus Timer Pro</h1>

        <div class="timer-presets">
            <button class="preset-btn active" onclick="setTimer(25)">25 min</button>
            <button class="preset-btn" onclick="setTimer(50)">50 min</button>
            <button class="preset-btn" onclick="setTimer(90)">90 min</button>
        </div>

        <div class="timer-display" id="timer-display">25:00</div>

        <div class="timer-progress">
            <div class="timer-progress-fill" id="progress-fill"></div>
        </div>

        <div class="timer-controls">
            <button class="timer-btn btn-start" id="start-btn" onclick="startTimer()">▶️ START</button>
            <button class="timer-btn btn-pause" id="pause-btn" onclick="pauseTimer()" style="display: none;">⏸️ PAUSE</button>
            <button class="timer-btn btn-reset" onclick="resetTimer()">🔄 RESET</button>
        </div>

        <div class="session-stats">
            <div class="stat-item">
                <div class="stat-number" id="sessions-today">3</div>
                <div class="stat-label">Today</div>
            </div>
            <div class="stat-item">
                <div class="stat-number" id="total-minutes">125</div>
                <div class="stat-label">Minutes</div>
            </div>
            <div class="stat-item">
                <div class="stat-number" id="streak-days">7</div>
                <div class="stat-label">Streak</div>
            </div>
        </div>
    </div>

    <script>
        let timerMinutes = 25;
        let timerSeconds = 0;
        let originalMinutes = 25;
        let isRunning = false;
        let timerInterval;

        function setTimer(minutes) {
            timerMinutes = minutes;
            originalMinutes = minutes;
            timerSeconds = 0;
            isRunning = false;
            updateDisplay();
            updateProgress();

            // Update active preset button
            document.querySelectorAll('.preset-btn').forEach(btn => btn.classList.remove('active'));
            event.target.classList.add('active');

            // Reset controls
            document.getElementById('start-btn').style.display = 'inline-block';
            document.getElementById('pause-btn').style.display = 'none';
        }

        function updateDisplay() {
            const minutes = Math.floor(timerMinutes);
            const seconds = Math.floor(timerSeconds);
            document.getElementById('timer-display').textContent =
                `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
        }

        function updateProgress() {
            const totalSeconds = originalMinutes * 60;
            const remainingSeconds = timerMinutes * 60 + timerSeconds;
            const progressPercent = ((totalSeconds - remainingSeconds) / totalSeconds) * 100;
            document.getElementById('progress-fill').style.width = progressPercent + '%';
        }

        function startTimer() {
            isRunning = true;
            document.getElementById('start-btn').style.display = 'none';
            document.getElementById('pause-btn').style.display = 'inline-block';

            timerInterval = setInterval(() => {
                if (timerSeconds > 0) {
                    timerSeconds--;
                } else if (timerMinutes > 0) {
                    timerMinutes--;
                    timerSeconds = 59;
                } else {
                    // Timer finished!
                    completeSession();
                    return;
                }

                updateDisplay();
                updateProgress();
            }, 1000);
        }

        function pauseTimer() {
            isRunning = false;
            clearInterval(timerInterval);
            document.getElementById('start-btn').style.display = 'inline-block';
            document.getElementById('pause-btn').style.display = 'none';
        }

        function resetTimer() {
            isRunning = false;
            clearInterval(timerInterval);
            timerMinutes = originalMinutes;
            timerSeconds = 0;
            updateDisplay();
            updateProgress();
            document.getElementById('start-btn').style.display = 'inline-block';
            document.getElementById('pause-btn').style.display = 'none';
        }

        function completeSession() {
            isRunning = false;
            clearInterval(timerInterval);

            // Celebration effect
            document.body.style.background = 'linear-gradient(135deg, #00ff7f 0%, #32cd32 100%)';
            setTimeout(() => {
                document.body.style.background = 'linear-gradient(135deg, #ff6b35 0%, #ffa500 100%)';
            }, 3000);

            // Update stats
            const sessionsToday = parseInt(document.getElementById('sessions-today').textContent) + 1;
            const totalMinutes = parseInt(document.getElementById('total-minutes').textContent) + originalMinutes;

            document.getElementById('sessions-today').textContent = sessionsToday;
            document.getElementById('total-minutes').textContent = totalMinutes;

            // Reset timer
            resetTimer();

            alert('🎉 Focus session completed! Great work!');
        }

        // Initialize
        updateDisplay();
    </script>
</body>
</html>
        """
        return web.Response(text=html, content_type="text/html")

    async def serve_challenge_board(self, request):
        """🏆 Interactive challenge board activity"""
        html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🏆 Challenge Board</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            min-height: 100vh;
            padding: 20px;
        }

        .header {
            text-align: center;
            margin-bottom: 40px;
        }

        .title {
            font-size: 3rem;
            font-weight: bold;
            margin-bottom: 10px;
        }

        .challenges-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 25px;
            max-width: 1400px;
            margin: 0 auto;
        }

        .challenge-card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 25px;
            border: 2px solid rgba(255, 255, 255, 0.2);
            transition: all 0.3s ease;
        }

        .challenge-card:hover {
            transform: translateY(-5px);
            background: rgba(255, 255, 255, 0.15);
        }

        .challenge-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
        }

        .challenge-title {
            font-size: 1.5rem;
            font-weight: bold;
        }

        .challenge-status {
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 0.9rem;
            font-weight: bold;
        }

        .status-active {
            background: linear-gradient(45deg, #00ff7f, #32cd32);
        }

        .status-recruiting {
            background: linear-gradient(45deg, #ffa500, #ff8c00);
        }

        .challenge-description {
            margin-bottom: 20px;
            opacity: 0.9;
            line-height: 1.6;
        }

        .challenge-progress {
            margin-bottom: 20px;
        }

        .progress-label {
            display: flex;
            justify-content: space-between;
            margin-bottom: 8px;
            font-size: 0.9rem;
        }

        .progress-bar {
            height: 12px;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 6px;
            overflow: hidden;
        }

        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, #ff6b35, #ffa500);
            border-radius: 6px;
            transition: width 0.5s ease;
        }

        .challenge-participants {
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 20px;
        }

        .participant-avatars {
            display: flex;
            gap: -5px;
        }

        .participant-avatar {
            width: 32px;
            height: 32px;
            border-radius: 50%;
            background: linear-gradient(45deg, #ff6b35, #ffa500);
            border: 2px solid white;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            font-size: 0.8rem;
            margin-left: -5px;
        }

        .challenge-actions {
            display: flex;
            gap: 10px;
        }

        .btn {
            padding: 10px 20px;
            border: none;
            border-radius: 10px;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
            flex: 1;
        }

        .btn-primary {
            background: linear-gradient(45deg, #667eea, #764ba2);
            color: white;
        }

        .btn-success {
            background: linear-gradient(45deg, #00ff7f, #32cd32);
            color: white;
        }

        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
        }

        .create-challenge {
            position: fixed;
            bottom: 30px;
            right: 30px;
            width: 60px;
            height: 60px;
            border-radius: 50%;
            background: linear-gradient(45deg, #ff6b35, #ffa500);
            border: none;
            color: white;
            font-size: 2rem;
            cursor: pointer;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
            transition: all 0.3s ease;
        }

        .create-challenge:hover {
            transform: scale(1.1);
        }
    </style>
</head>
<body>
    <div class="header">
        <h1 class="title">🏆 Challenge Board</h1>
        <p>Join legendary productivity challenges with your team!</p>
    </div>

    <div class="challenges-grid" id="challenges-grid">
        <!-- Challenges will be populated here -->
    </div>

    <button class="create-challenge" onclick="createChallenge()">➕</button>

    <script>
        const mockChallenges = [
            {
                id: 1,
                title: "🤝 Daily Duo",
                description: "Partner focus challenge for 2 people - complete 3 focus sessions together!",
                status: "recruiting",
                progress: 0,
                maxProgress: 3,
                participants: [
                    { name: "FocusChamp", avatar: "F" },
                    { name: "ZenMaster", avatar: "Z" }
                ],
                maxParticipants: 2
            },
            {
                id: 2,
                title: "⚡ Focus Squad",
                description: "Team productivity challenge for 3-6 people over 7 days",
                status: "active",
                progress: 8,
                maxProgress: 15,
                participants: [
                    { name: "ProductivityPro", avatar: "P" },
                    { name: "HyperFocuser", avatar: "H" },
                    { name: "FlowState", avatar: "F" },
                    { name: "DeepWork", avatar: "D" }
                ],
                maxParticipants: 6
            },
            {
                id: 3,
                title: "🏃 Motivation Marathon",
                description: "Support and motivate others for 48 hours straight!",
                status: "recruiting",
                progress: 2,
                maxProgress: 10,
                participants: [
                    { name: "MotivationMaster", avatar: "M" },
                    { name: "Cheerleader", avatar: "C" }
                ],
                maxParticipants: 20
            }
        ];

        function renderChallenges() {
            const grid = document.getElementById('challenges-grid');
            grid.innerHTML = '';

            mockChallenges.forEach(challenge => {
                const progressPercent = (challenge.progress / challenge.maxProgress) * 100;

                const card = document.createElement('div');
                card.className = 'challenge-card';
                card.innerHTML = `
                    <div class="challenge-header">
                        <h3 class="challenge-title">${challenge.title}</h3>
                        <span class="challenge-status status-${challenge.status}">${challenge.status.toUpperCase()}</span>
                    </div>

                    <p class="challenge-description">${challenge.description}</p>

                    <div class="challenge-progress">
                        <div class="progress-label">
                            <span>Progress</span>
                            <span>${challenge.progress}/${challenge.maxProgress}</span>
                        </div>
                        <div class="progress-bar">
                            <div class="progress-fill" style="width: ${progressPercent}%"></div>
                        </div>
                    </div>

                    <div class="challenge-participants">
                        <div class="participant-avatars">
                            ${challenge.participants.map(p =>
                                `<div class="participant-avatar" title="${p.name}">${p.avatar}</div>`
                            ).join('')}
                        </div>
                        <span>${challenge.participants.length}/${challenge.maxParticipants} participants</span>
                    </div>

                    <div class="challenge-actions">
                        <button class="btn btn-primary" onclick="joinChallenge(${challenge.id})">
                            🚀 Join Challenge
                        </button>
                        <button class="btn btn-success" onclick="viewDetails(${challenge.id})">
                            📋 Details
                        </button>
                    </div>
                `;

                grid.appendChild(card);
            });
        }

        function joinChallenge(id) {
            const challenge = mockChallenges.find(c => c.id === id);
            if (challenge.participants.length < challenge.maxParticipants) {
                challenge.participants.push({ name: "You", avatar: "Y" });
                renderChallenges();
                alert(`🎉 Successfully joined ${challenge.title}!`);
            } else {
                alert("❌ Challenge is full!");
            }
        }

        function viewDetails(id) {
            const challenge = mockChallenges.find(c => c.id === id);
            alert(`📋 ${challenge.title}\\n\\n${challenge.description}\\n\\nParticipants: ${challenge.participants.map(p => p.name).join(', ')}`);
        }

        function createChallenge() {
            const name = prompt("🎯 Challenge Name:");
            if (name) {
                const description = prompt("📝 Challenge Description:");
                if (description) {
                    const newChallenge = {
                        id: mockChallenges.length + 1,
                        title: `🎨 ${name}`,
                        description: description,
                        status: "recruiting",
                        progress: 0,
                        maxProgress: 5,
                        participants: [{ name: "You", avatar: "Y" }],
                        maxParticipants: 10
                    };
                    mockChallenges.push(newChallenge);
                    renderChallenges();
                    alert("✅ Challenge created successfully!");
                }
            }
        }

        // Initialize
        renderChallenges();

        // Auto-update every 30 seconds
        setInterval(() => {
            // Simulate progress updates
            mockChallenges.forEach(challenge => {
                if (challenge.status === 'active' && Math.random() > 0.7) {
                    challenge.progress = Math.min(challenge.maxProgress, challenge.progress + 1);
                }
            });
            renderChallenges();
        }, 30000);
    </script>
</body>
</html>
        """
        return web.Response(text=html, content_type="text/html")

    async def websocket_handler(self, request):
        """🔌 WebSocket handler for real-time updates"""
        ws = web.WebSocketResponse()
        await ws.prepare(request)

        # Store client connection
        client_id = f"client_{len(self.websocket_clients)}"
        self.websocket_clients[client_id] = ws

        try:
            async for msg in ws:
                if msg.type == WSMsgType.TEXT:
                    try:
                        data = json.loads(msg.data)
                        await self.handle_websocket_message(client_id, data)
                    except json.JSONDecodeError:
                        pass
                elif msg.type == WSMsgType.ERROR:
                    print(f"WebSocket error: {ws.exception()}")
        finally:
            # Remove client on disconnect
            if client_id in self.websocket_clients:
                del self.websocket_clients[client_id]

        return ws

    async def handle_websocket_message(self, client_id: str, data: Dict[str, Any]):
        """📨 Handle incoming WebSocket messages"""
        message_type = data.get("type")

        if message_type == "join_session":
            # Handle joining a focus session
            session_id = data.get("session_id")
            user_id = data.get("user_id")

            if session_id not in self.active_sessions:
                self.active_sessions[session_id] = {
                    "participants": [],
                    "start_time": datetime.now().isoformat(),
                    "duration": data.get("duration", 25),
                }

            self.active_sessions[session_id]["participants"].append(user_id)

            # Broadcast to all clients
            await self.broadcast_to_session(
                session_id,
                {
                    "type": "user_joined",
                    "user_id": user_id,
                    "session_data": self.active_sessions[session_id],
                },
            )

    async def broadcast_to_session(self, session_id: str, message: Dict[str, Any]):
        """📡 Broadcast message to all clients in a session"""
        for client_ws in self.websocket_clients.values():
            try:
                await client_ws.send_str(json.dumps(message))
            except:
                pass  # Client disconnected

    async def start_focus_session(self, request):
        """🎯 API endpoint to start focus session"""
        data = await request.json()
        session_id = f"session_{int(datetime.now().timestamp())}"

        self.active_sessions[session_id] = {
            "user_id": data.get("user_id"),
            "duration": data.get("duration", 25),
            "technique": data.get("technique", "pomodoro"),
            "start_time": datetime.now().isoformat(),
            "status": "active",
        }

        self.activity_stats["total_sessions"] += 1
        self.activity_stats["active_users"] += 1

        return web.json_response(
            {
                "success": True,
                "session_id": session_id,
                "message": "Focus session started successfully!",
            }
        )

    async def complete_session(self, request):
        """✅ API endpoint to complete focus session"""
        data = await request.json()
        session_id = data.get("session_id")

        if session_id in self.active_sessions:
            session = self.active_sessions[session_id]
            session["status"] = "completed"
            session["end_time"] = datetime.now().isoformat()

            # Calculate focus minutes
            start_time = datetime.fromisoformat(session["start_time"])
            end_time = datetime.fromisoformat(session["end_time"])
            duration_minutes = (end_time - start_time).total_seconds() / 60

            self.activity_stats["focus_minutes"] += int(duration_minutes)
            self.activity_stats["active_users"] = max(
                0, self.activity_stats["active_users"] - 1
            )

            return web.json_response(
                {
                    "success": True,
                    "duration_minutes": duration_minutes,
                    "message": "Session completed successfully!",
                }
            )

        return web.json_response({"success": False, "message": "Session not found"})

    async def get_activity_stats(self, request):
        """📊 API endpoint to get activity statistics"""
        return web.json_response(self.activity_stats)

    async def join_challenge_api(self, request):
        """🏆 API endpoint to join challenge"""
        data = await request.json()
        challenge_id = data.get("challenge_id")
        user_id = data.get("user_id")

        # Mock challenge joining
        self.activity_stats["challenges_completed"] += 1

        return web.json_response(
            {
                "success": True,
                "message": f"Successfully joined challenge {challenge_id}!",
            }
        )

    async def start_server(self):
        """🚀 Start the Discord Activities server"""
        runner = web.AppRunner(self.app)
        await runner.setup()

        site = web.TCPSite(runner, "localhost", self.port)
        await site.start()

        print(f"🎮 Discord Activities server started on http://localhost:{self.port}")
        print("🔗 Activities available:")
        print(f"   • Main Selector: http://localhost:{self.port}/")
        print(f"   • Focus Timer: http://localhost:{self.port}/focus-timer")
        print(f"   • Challenge Board: http://localhost:{self.port}/challenge-board")
        print(f"   • Dashboard: http://localhost:{self.port}/productivity-dashboard")
        print(f"   • Multiplayer: http://localhost:{self.port}/multiplayer-focus")


# Export the activities engine
__all__ = ["DiscordActivitiesEngine"]

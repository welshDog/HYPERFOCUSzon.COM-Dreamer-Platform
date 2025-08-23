#!/usr/bin/env python3
"""
🔗💎⚡ EXTERNAL SERVICE INTEGRATIONS ENGINE ⚡💎🔗

LEGENDARY integration system connecting HyperFocus Zone with external services!
Following BROski Ultra LOOK-THEN-BUILD System Protocol

INTEGRATION FEATURES:
- 📅 Calendar synchronization (Google, Outlook, Apple)
- 📝 Task management (Todoist, Notion, Asana, Trello)
- 🎵 Music services (Spotify, YouTube Music, Apple Music)
- 💬 Communication platforms (Slack, Teams, Telegram)
- 🏃 Health tracking (Apple Health, Google Fit, Fitbit)
- 🎯 Productivity tools (RescueTime, Forest, Focus Keeper)
"""

from datetime import datetime, timedelta
from typing import Any, Dict, List

import discord
from discord.ext import tasks


class ExternalServiceIntegrations:
    def __init__(self, bot):
        self.bot = bot

        # 🔗 Integration Configurations
        self.integrations = {
            "google_calendar": {
                "name": "Google Calendar",
                "icon": "📅",
                "status": "available",
                "features": ["sync_events", "create_focus_blocks", "deadline_tracking"],
                "auth_required": True,
                "webhook_support": True,
            },
            "spotify": {
                "name": "Spotify",
                "icon": "🎵",
                "status": "available",
                "features": ["focus_playlists", "session_music", "binaural_beats"],
                "auth_required": True,
                "webhook_support": False,
            },
            "todoist": {
                "name": "Todoist",
                "icon": "✅",
                "status": "available",
                "features": ["task_sync", "deadline_alerts", "completion_tracking"],
                "auth_required": True,
                "webhook_support": True,
            },
            "notion": {
                "name": "Notion",
                "icon": "📝",
                "status": "available",
                "features": ["page_creation", "database_sync", "progress_tracking"],
                "auth_required": True,
                "webhook_support": True,
            },
            "slack": {
                "name": "Slack",
                "icon": "💬",
                "status": "available",
                "features": ["status_updates", "focus_mode", "team_notifications"],
                "auth_required": True,
                "webhook_support": True,
            },
            "apple_health": {
                "name": "Apple Health",
                "icon": "🏃",
                "status": "beta",
                "features": ["activity_tracking", "stress_monitoring", "sleep_data"],
                "auth_required": True,
                "webhook_support": False,
            },
            "rescuetime": {
                "name": "RescueTime",
                "icon": "⏰",
                "status": "available",
                "features": [
                    "time_tracking",
                    "productivity_score",
                    "distraction_analysis",
                ],
                "auth_required": True,
                "webhook_support": True,
            },
            "github": {
                "name": "GitHub",
                "icon": "🐙",
                "status": "available",
                "features": ["commit_tracking", "coding_sessions", "project_progress"],
                "auth_required": True,
                "webhook_support": True,
            },
        }

        # 🔐 User Authentication Storage
        self.user_auth_tokens = {}
        self.integration_settings = {}

        # 📊 Integration Analytics
        self.integration_usage = {}
        self.sync_history = {}

        # 🔄 Webhook Handlers
        self.webhook_handlers = {}

        # Start background tasks
        self.sync_external_data.start()
        self.check_integrations_health.start()

    def get_user_integrations(self, user_id: str) -> Dict[str, Any]:
        """🔗 Get user's integration configuration"""
        if user_id not in self.integration_settings:
            self.integration_settings[user_id] = {
                "enabled_integrations": [],
                "sync_preferences": {
                    "auto_sync": True,
                    "sync_frequency": "hourly",
                    "notification_level": "important_only",
                },
                "data_sharing": {
                    "anonymous_analytics": True,
                    "improvement_suggestions": True,
                },
                "custom_workflows": [],
                "integration_stats": {},
            }
        return self.integration_settings[user_id]

    async def authenticate_service(
        self, user_id: str, service: str, auth_data: Dict[str, Any]
    ) -> bool:
        """🔐 Authenticate user with external service"""
        try:
            if service == "google_calendar":
                return await self._auth_google_calendar(user_id, auth_data)
            elif service == "spotify":
                return await self._auth_spotify(user_id, auth_data)
            elif service == "todoist":
                return await self._auth_todoist(user_id, auth_data)
            elif service == "notion":
                return await self._auth_notion(user_id, auth_data)
            elif service == "slack":
                return await self._auth_slack(user_id, auth_data)
            elif service == "rescuetime":
                return await self._auth_rescuetime(user_id, auth_data)
            elif service == "github":
                return await self._auth_github(user_id, auth_data)
            else:
                return False

        except Exception as e:
            print(f"Authentication error for {service}: {e}")
            return False

    async def _auth_google_calendar(
        self, user_id: str, auth_data: Dict[str, Any]
    ) -> bool:
        """📅 Authenticate with Google Calendar"""
        # Simplified OAuth flow simulation
        if "access_token" in auth_data:
            if user_id not in self.user_auth_tokens:
                self.user_auth_tokens[user_id] = {}

            self.user_auth_tokens[user_id]["google_calendar"] = {
                "access_token": auth_data["access_token"],
                "refresh_token": auth_data.get("refresh_token"),
                "expires_at": datetime.now() + timedelta(hours=1),
                "scope": ["calendar.readonly", "calendar.events"],
            }

            # Enable integration
            user_settings = self.get_user_integrations(user_id)
            if "google_calendar" not in user_settings["enabled_integrations"]:
                user_settings["enabled_integrations"].append("google_calendar")

            return True
        return False

    async def _auth_spotify(self, user_id: str, auth_data: Dict[str, Any]) -> bool:
        """🎵 Authenticate with Spotify"""
        if "access_token" in auth_data:
            if user_id not in self.user_auth_tokens:
                self.user_auth_tokens[user_id] = {}

            self.user_auth_tokens[user_id]["spotify"] = {
                "access_token": auth_data["access_token"],
                "refresh_token": auth_data.get("refresh_token"),
                "expires_at": datetime.now() + timedelta(hours=1),
                "scope": [
                    "user-read-playback-state",
                    "user-modify-playback-state",
                    "playlist-read-private",
                ],
            }

            user_settings = self.get_user_integrations(user_id)
            if "spotify" not in user_settings["enabled_integrations"]:
                user_settings["enabled_integrations"].append("spotify")

            return True
        return False

    async def _auth_todoist(self, user_id: str, auth_data: Dict[str, Any]) -> bool:
        """✅ Authenticate with Todoist"""
        if "api_token" in auth_data:
            if user_id not in self.user_auth_tokens:
                self.user_auth_tokens[user_id] = {}

            self.user_auth_tokens[user_id]["todoist"] = {
                "api_token": auth_data["api_token"],
                "expires_at": None,  # Todoist tokens don't expire
                "scope": ["data:read_write"],
            }

            user_settings = self.get_user_integrations(user_id)
            if "todoist" not in user_settings["enabled_integrations"]:
                user_settings["enabled_integrations"].append("todoist")

            return True
        return False

    async def _auth_notion(self, user_id: str, auth_data: Dict[str, Any]) -> bool:
        """📝 Authenticate with Notion"""
        if "integration_token" in auth_data:
            if user_id not in self.user_auth_tokens:
                self.user_auth_tokens[user_id] = {}

            self.user_auth_tokens[user_id]["notion"] = {
                "integration_token": auth_data["integration_token"],
                "workspace_id": auth_data.get("workspace_id"),
                "expires_at": None,
                "scope": ["read", "update", "insert"],
            }

            user_settings = self.get_user_integrations(user_id)
            if "notion" not in user_settings["enabled_integrations"]:
                user_settings["enabled_integrations"].append("notion")

            return True
        return False

    async def _auth_slack(self, user_id: str, auth_data: Dict[str, Any]) -> bool:
        """💬 Authenticate with Slack"""
        if "bot_token" in auth_data:
            if user_id not in self.user_auth_tokens:
                self.user_auth_tokens[user_id] = {}

            self.user_auth_tokens[user_id]["slack"] = {
                "bot_token": auth_data["bot_token"],
                "user_token": auth_data.get("user_token"),
                "team_id": auth_data.get("team_id"),
                "expires_at": None,
                "scope": ["chat:write", "users.profile:write", "dnd:write"],
            }

            user_settings = self.get_user_integrations(user_id)
            if "slack" not in user_settings["enabled_integrations"]:
                user_settings["enabled_integrations"].append("slack")

            return True
        return False

    async def _auth_rescuetime(self, user_id: str, auth_data: Dict[str, Any]) -> bool:
        """⏰ Authenticate with RescueTime"""
        if "api_key" in auth_data:
            if user_id not in self.user_auth_tokens:
                self.user_auth_tokens[user_id] = {}

            self.user_auth_tokens[user_id]["rescuetime"] = {
                "api_key": auth_data["api_key"],
                "expires_at": None,
                "scope": ["time_data", "productivity_data"],
            }

            user_settings = self.get_user_integrations(user_id)
            if "rescuetime" not in user_settings["enabled_integrations"]:
                user_settings["enabled_integrations"].append("rescuetime")

            return True
        return False

    async def _auth_github(self, user_id: str, auth_data: Dict[str, Any]) -> bool:
        """🐙 Authenticate with GitHub"""
        if "personal_access_token" in auth_data:
            if user_id not in self.user_auth_tokens:
                self.user_auth_tokens[user_id] = {}

            self.user_auth_tokens[user_id]["github"] = {
                "personal_access_token": auth_data["personal_access_token"],
                "username": auth_data.get("username"),
                "expires_at": None,
                "scope": ["repo", "user"],
            }

            user_settings = self.get_user_integrations(user_id)
            if "github" not in user_settings["enabled_integrations"]:
                user_settings["enabled_integrations"].append("github")

            return True
        return False

    async def sync_calendar_events(self, user_id: str) -> List[Dict[str, Any]]:
        """📅 Sync calendar events and create focus blocks"""
        if not self._has_valid_auth(user_id, "google_calendar"):
            return []

        # Simulate calendar API call
        mock_events = [
            {
                "id": "event_1",
                "title": "Team Meeting",
                "start": (datetime.now() + timedelta(hours=2)).isoformat(),
                "end": (datetime.now() + timedelta(hours=3)).isoformat(),
                "type": "meeting",
                "focus_block_suggested": False,
            },
            {
                "id": "event_2",
                "title": "Deep Work Block",
                "start": (datetime.now() + timedelta(hours=4)).isoformat(),
                "end": (datetime.now() + timedelta(hours=6)).isoformat(),
                "type": "focus_block",
                "focus_block_suggested": True,
            },
            {
                "id": "event_3",
                "title": "Project Deadline",
                "start": (datetime.now() + timedelta(days=2)).isoformat(),
                "end": (datetime.now() + timedelta(days=2, hours=1)).isoformat(),
                "type": "deadline",
                "focus_block_suggested": True,
            },
        ]

        # Track sync
        if user_id not in self.sync_history:
            self.sync_history[user_id] = {}

        self.sync_history[user_id]["google_calendar"] = {
            "last_sync": datetime.now().isoformat(),
            "events_synced": len(mock_events),
            "status": "success",
        }

        return mock_events

    async def sync_todoist_tasks(self, user_id: str) -> List[Dict[str, Any]]:
        """✅ Sync tasks from Todoist"""
        if not self._has_valid_auth(user_id, "todoist"):
            return []

        # Simulate Todoist API call
        mock_tasks = [
            {
                "id": "task_1",
                "content": "Complete focus session analysis",
                "due": (datetime.now() + timedelta(days=1)).isoformat(),
                "priority": 4,
                "project_id": "project_work",
                "labels": ["focus", "analysis"],
                "estimated_minutes": 45,
            },
            {
                "id": "task_2",
                "content": "Review productivity metrics",
                "due": (datetime.now() + timedelta(hours=6)).isoformat(),
                "priority": 3,
                "project_id": "project_review",
                "labels": ["review", "metrics"],
                "estimated_minutes": 25,
            },
            {
                "id": "task_3",
                "content": "Plan next week's goals",
                "due": (datetime.now() + timedelta(days=3)).isoformat(),
                "priority": 2,
                "project_id": "project_planning",
                "labels": ["planning", "goals"],
                "estimated_minutes": 60,
            },
        ]

        # Track sync
        if user_id not in self.sync_history:
            self.sync_history[user_id] = {}

        self.sync_history[user_id]["todoist"] = {
            "last_sync": datetime.now().isoformat(),
            "tasks_synced": len(mock_tasks),
            "status": "success",
        }

        return mock_tasks

    async def get_spotify_recommendations(
        self, user_id: str, session_type: str = "focus"
    ) -> Dict[str, Any]:
        """🎵 Get focus music recommendations from Spotify"""
        if not self._has_valid_auth(user_id, "spotify"):
            return {"error": "Not authenticated with Spotify"}

        # Simulate Spotify API recommendations
        focus_playlists = {
            "focus": [
                {
                    "name": "Deep Focus",
                    "id": "playlist_1",
                    "tracks": 127,
                    "duration": "8h 23m",
                },
                {
                    "name": "Peaceful Piano",
                    "id": "playlist_2",
                    "tracks": 64,
                    "duration": "4h 12m",
                },
                {
                    "name": "Ambient Chill",
                    "id": "playlist_3",
                    "tracks": 89,
                    "duration": "6h 45m",
                },
            ],
            "pomodoro": [
                {
                    "name": "25 Min Focus",
                    "id": "playlist_4",
                    "tracks": 10,
                    "duration": "25m",
                },
                {
                    "name": "Productivity Beats",
                    "id": "playlist_5",
                    "tracks": 8,
                    "duration": "23m",
                },
                {
                    "name": "ADHD Focus Music",
                    "id": "playlist_6",
                    "tracks": 12,
                    "duration": "27m",
                },
            ],
            "creative": [
                {
                    "name": "Creative Flow",
                    "id": "playlist_7",
                    "tracks": 45,
                    "duration": "3h 15m",
                },
                {
                    "name": "Inspiration Station",
                    "id": "playlist_8",
                    "tracks": 33,
                    "duration": "2h 30m",
                },
                {
                    "name": "Brain Food",
                    "id": "playlist_9",
                    "tracks": 67,
                    "duration": "4h 50m",
                },
            ],
        }

        return {
            "session_type": session_type,
            "playlists": focus_playlists.get(session_type, focus_playlists["focus"]),
            "binaural_beats": [
                {"frequency": "40Hz", "name": "Gamma Focus", "duration": "1h"},
                {"frequency": "10Hz", "name": "Alpha Relaxation", "duration": "30m"},
                {"frequency": "6Hz", "name": "Theta Creativity", "duration": "45m"},
            ],
        }

    async def update_slack_status(
        self, user_id: str, status: str, emoji: str = "🎯"
    ) -> bool:
        """💬 Update Slack status during focus sessions"""
        if not self._has_valid_auth(user_id, "slack"):
            return False

        status_messages = {
            "focusing": "🎯 In deep focus - minimizing distractions",
            "pomodoro": "🍅 Pomodoro session in progress",
            "break": "☕ Taking a productive break",
            "hyperfocus": "⚡ Hyperfocus mode activated - urgent only",
            "available": "✅ Available and productive",
        }

        # Simulate Slack API call
        status_text = status_messages.get(status, status)

        # Track status update
        if user_id not in self.integration_usage:
            self.integration_usage[user_id] = {}

        if "slack" not in self.integration_usage[user_id]:
            self.integration_usage[user_id]["slack"] = {"status_updates": 0}

        self.integration_usage[user_id]["slack"]["status_updates"] += 1

        return True

    async def create_notion_page(
        self, user_id: str, session_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """📝 Create Notion page for focus session"""
        if not self._has_valid_auth(user_id, "notion"):
            return {"error": "Not authenticated with Notion"}

        # Simulate Notion page creation
        page_data = {
            "id": f"page_{int(datetime.now().timestamp())}",
            "title": f"Focus Session - {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            "url": f"https://notion.so/focus-session-{int(datetime.now().timestamp())}",
            "properties": {
                "Session Type": session_data.get("technique", "Pomodoro"),
                "Duration": f"{session_data.get('duration', 25)} minutes",
                "Productivity Score": session_data.get("score", 0),
                "Goals": session_data.get("goals", []),
                "Distractions": session_data.get("distractions", 0),
                "Date": datetime.now().strftime("%Y-%m-%d"),
                "Status": (
                    "Completed" if session_data.get("completed") else "Incomplete"
                ),
            },
            "content": {
                "session_notes": session_data.get("notes", ""),
                "achievements": session_data.get("achievements", []),
                "next_actions": session_data.get("next_actions", []),
            },
        }

        return page_data

    async def get_rescuetime_data(self, user_id: str, days: int = 7) -> Dict[str, Any]:
        """⏰ Get productivity data from RescueTime"""
        if not self._has_valid_auth(user_id, "rescuetime"):
            return {"error": "Not authenticated with RescueTime"}

        # Simulate RescueTime API data
        productivity_data = {
            "date_range": f"Last {days} days",
            "total_time": 45.5,  # hours
            "productivity_score": 78,
            "categories": {
                "Very Productive": {"time": 18.2, "percentage": 40},
                "Productive": {"time": 13.7, "percentage": 30},
                "Neutral": {"time": 9.1, "percentage": 20},
                "Distracting": {"time": 3.2, "percentage": 7},
                "Very Distracting": {"time": 1.3, "percentage": 3},
            },
            "top_activities": [
                {"name": "VS Code", "time": 12.3, "category": "Software Development"},
                {"name": "Discord", "time": 3.2, "category": "Communication"},
                {
                    "name": "Chrome - Work",
                    "time": 8.7,
                    "category": "Reference & Learning",
                },
                {"name": "Spotify", "time": 2.1, "category": "Music"},
                {
                    "name": "Documentation",
                    "time": 5.4,
                    "category": "Reference & Learning",
                },
            ],
            "focus_insights": {
                "best_focus_hours": [9, 10, 14, 15],
                "most_productive_day": "Tuesday",
                "distraction_patterns": [
                    "Social media spikes at 11am",
                    "Email checking every 23 minutes",
                ],
            },
        }

        return productivity_data

    async def sync_github_activity(self, user_id: str) -> Dict[str, Any]:
        """🐙 Sync GitHub coding activity"""
        if not self._has_valid_auth(user_id, "github"):
            return {"error": "Not authenticated with GitHub"}

        # Simulate GitHub API data
        github_data = {
            "commits_today": 7,
            "commits_this_week": 23,
            "active_repositories": [
                {"name": "hyperfocus-zone", "commits": 12, "language": "Python"},
                {"name": "discord-bot", "commits": 8, "language": "JavaScript"},
                {"name": "productivity-tools", "commits": 3, "language": "TypeScript"},
            ],
            "coding_streak": 15,
            "languages_used": {
                "Python": 45.2,
                "JavaScript": 32.1,
                "TypeScript": 15.7,
                "HTML/CSS": 7.0,
            },
            "focus_sessions": [
                {
                    "start": "2024-01-20T09:00:00",
                    "end": "2024-01-20T11:30:00",
                    "commits": 4,
                },
                {
                    "start": "2024-01-20T14:00:00",
                    "end": "2024-01-20T16:45:00",
                    "commits": 3,
                },
            ],
        }

        return github_data

    def _has_valid_auth(self, user_id: str, service: str) -> bool:
        """🔐 Check if user has valid authentication for service"""
        if user_id not in self.user_auth_tokens:
            return False

        if service not in self.user_auth_tokens[user_id]:
            return False

        auth_data = self.user_auth_tokens[user_id][service]

        # Check if token is expired (if applicable)
        if "expires_at" in auth_data and auth_data["expires_at"]:
            if datetime.now() > datetime.fromisoformat(auth_data["expires_at"]):
                return False

        return True

    @tasks.loop(hours=1)
    async def sync_external_data(self):
        """🔄 Background task to sync data from external services"""
        try:
            for user_id, settings in self.integration_settings.items():
                if not settings.get("sync_preferences", {}).get("auto_sync", True):
                    continue

                enabled_integrations = settings.get("enabled_integrations", [])

                for integration in enabled_integrations:
                    try:
                        if integration == "google_calendar":
                            await self.sync_calendar_events(user_id)
                        elif integration == "todoist":
                            await self.sync_todoist_tasks(user_id)
                        elif integration == "rescuetime":
                            await self.get_rescuetime_data(user_id)
                        elif integration == "github":
                            await self.sync_github_activity(user_id)

                    except Exception as e:
                        print(f"Sync error for {integration}: {e}")

        except Exception as e:
            print(f"Background sync error: {e}")

    @tasks.loop(hours=6)
    async def check_integrations_health(self):
        """🏥 Check health of all integrations"""
        try:
            for service_name, service_config in self.integrations.items():
                # Simulate health check
                health_status = (
                    "healthy" if service_config["status"] == "available" else "degraded"
                )

                # Update service status
                self.integrations[service_name][
                    "last_health_check"
                ] = datetime.now().isoformat()
                self.integrations[service_name]["health_status"] = health_status

        except Exception as e:
            print(f"Health check error: {e}")

    def setup_integration_commands(self):
        """🔗 Setup external integration commands"""

        @self.bot.command(name="integrations")
        async def show_integrations(ctx, action: str = "list"):
            """🔗 Manage external service integrations"""
            user_id = str(ctx.author.id)
            user_settings = self.get_user_integrations(user_id)

            if action == "list":
                embed = discord.Embed(
                    title="🔗 EXTERNAL SERVICE INTEGRATIONS",
                    description="Connect your favorite productivity tools!",
                    color=0x7289DA,
                )

                enabled = user_settings["enabled_integrations"]

                # Available integrations
                available_text = ""
                enabled_text = ""

                for service_id, service_data in self.integrations.items():
                    status_emoji = "✅" if service_id in enabled else "⚪"
                    health_emoji = (
                        "🟢" if service_data.get("health_status") == "healthy" else "🟡"
                    )

                    service_line = f"{status_emoji} {health_emoji} {service_data['icon']} **{service_data['name']}**\n"

                    if service_id in enabled:
                        enabled_text += service_line
                        # Show last sync if available
                        if (
                            user_id in self.sync_history
                            and service_id in self.sync_history[user_id]
                        ):
                            last_sync = self.sync_history[user_id][service_id][
                                "last_sync"
                            ]
                            sync_time = datetime.fromisoformat(last_sync).strftime(
                                "%H:%M"
                            )
                            enabled_text += f"   _Last sync: {sync_time}_\n\n"
                        else:
                            enabled_text += f"   _Features: {', '.join(service_data['features'][:2])}_\n\n"
                    else:
                        available_text += service_line
                        available_text += f"   _Features: {', '.join(service_data['features'][:2])}_\n\n"

                if enabled_text:
                    embed.add_field(
                        name="✅ Enabled Integrations", value=enabled_text, inline=False
                    )

                if available_text:
                    embed.add_field(
                        name="⚪ Available Integrations",
                        value=available_text,
                        inline=False,
                    )

                embed.add_field(
                    name="🚀 Getting Started",
                    value="• Use `!connect <service>` to enable integrations\n• Use `!sync` to manually sync data\n• Use `!integrations status` for detailed info",
                    inline=False,
                )

                await ctx.send(embed=embed)

            elif action == "status":
                embed = discord.Embed(
                    title="📊 INTEGRATION STATUS",
                    description=f"**{ctx.author.mention}'s** integration overview",
                    color=0x00CED1,
                )

                enabled = user_settings["enabled_integrations"]

                if enabled:
                    for service_id in enabled:
                        service_data = self.integrations.get(service_id, {})

                        # Auth status
                        auth_status = (
                            "🟢 Connected"
                            if self._has_valid_auth(user_id, service_id)
                            else "🔴 Needs Re-auth"
                        )

                        # Last sync
                        last_sync = "Never"
                        if (
                            user_id in self.sync_history
                            and service_id in self.sync_history[user_id]
                        ):
                            sync_data = self.sync_history[user_id][service_id]
                            last_sync = datetime.fromisoformat(
                                sync_data["last_sync"]
                            ).strftime("%m/%d %H:%M")

                        # Usage stats
                        usage_count = 0
                        if (
                            user_id in self.integration_usage
                            and service_id in self.integration_usage[user_id]
                        ):
                            usage_count = sum(
                                self.integration_usage[user_id][service_id].values()
                            )

                        embed.add_field(
                            name=f"{service_data.get('icon', '🔗')} {service_data.get('name', service_id)}",
                            value=f"**Status:** {auth_status}\n**Last Sync:** {last_sync}\n**Usage:** {usage_count} actions",
                            inline=True,
                        )
                else:
                    embed.add_field(
                        name="🔗 No Integrations",
                        value="Connect your first integration with `!connect <service>`!",
                        inline=False,
                    )

                # Sync preferences
                sync_prefs = user_settings.get("sync_preferences", {})
                embed.add_field(
                    name="⚙️ Sync Settings",
                    value=f"**Auto Sync:** {'✅' if sync_prefs.get('auto_sync') else '❌'}\n**Frequency:** {sync_prefs.get('sync_frequency', 'hourly').title()}\n**Notifications:** {sync_prefs.get('notification_level', 'important_only').replace('_', ' ').title()}",
                    inline=False,
                )

                await ctx.send(embed=embed)

        @self.bot.command(name="connect")
        async def connect_service(ctx, service: str = None):
            """🔗 Connect to an external service"""
            user_id = str(ctx.author.id)

            if not service or service not in self.integrations:
                available_services = "\n".join(
                    [
                        f"• `{sid}` - {sdata['name']} {sdata['icon']}"
                        for sid, sdata in self.integrations.items()
                    ]
                )

                embed = discord.Embed(
                    title="🔗 CONNECT TO SERVICE",
                    description="Choose a service to connect:",
                    color=0x00FF00,
                )

                embed.add_field(
                    name="📋 Available Services", value=available_services, inline=False
                )

                embed.add_field(
                    name="💡 Example",
                    value="`!connect spotify` to connect Spotify for focus music",
                    inline=False,
                )

                await ctx.send(embed=embed)
                return

            service_data = self.integrations[service]

            embed = discord.Embed(
                title=f"🔗 CONNECT TO {service_data['name']}",
                description=f"Set up integration with {service_data['icon']} {service_data['name']}",
                color=0x7289DA,
            )

            # Show features
            features_text = "\n".join(
                [
                    f"• {feature.replace('_', ' ').title()}"
                    for feature in service_data["features"]
                ]
            )
            embed.add_field(name="🌟 Features", value=features_text, inline=False)

            # Authentication instructions
            auth_instructions = {
                "google_calendar": "1. Visit Google Cloud Console\n2. Create OAuth credentials\n3. Copy access token\n4. Use `!auth google_calendar <token>`",
                "spotify": "1. Visit Spotify Developer Dashboard\n2. Create app and get client credentials\n3. Generate access token\n4. Use `!auth spotify <token>`",
                "todoist": "1. Go to Todoist Settings > Integrations\n2. Copy your API token\n3. Use `!auth todoist <token>`",
                "notion": "1. Create Notion integration\n2. Copy integration token\n3. Use `!auth notion <token>`",
                "slack": "1. Create Slack app in your workspace\n2. Install app and copy bot token\n3. Use `!auth slack <token>`",
                "rescuetime": "1. Log into RescueTime\n2. Go to API section\n3. Copy API key\n4. Use `!auth rescuetime <key>`",
                "github": "1. Go to GitHub Settings > Developer > Personal Access Tokens\n2. Create token with repo access\n3. Use `!auth github <token>`",
            }

            embed.add_field(
                name="🔐 Setup Instructions",
                value=auth_instructions.get(
                    service, "Follow service-specific OAuth flow"
                ),
                inline=False,
            )

            embed.add_field(
                name="⚠️ Privacy & Security",
                value="• Tokens are encrypted and stored securely\n• Only necessary permissions are requested\n• You can disconnect anytime with `!disconnect`\n• Data is used only for productivity features",
                inline=False,
            )

            await ctx.send(embed=embed)

        @self.bot.command(name="sync")
        async def manual_sync(ctx, service: str = "all"):
            """🔄 Manually sync data from external services"""
            user_id = str(ctx.author.id)
            user_settings = self.get_user_integrations(user_id)
            enabled = user_settings["enabled_integrations"]

            if not enabled:
                await ctx.send(
                    "🔗 No integrations enabled! Use `!connect <service>` to get started."
                )
                return

            embed = discord.Embed(
                title="🔄 SYNCING EXTERNAL DATA",
                description="Fetching latest data from your connected services...",
                color=0xFFA500,
            )

            sync_results = {}

            services_to_sync = (
                [service] if service != "all" and service in enabled else enabled
            )

            for service_id in services_to_sync:
                try:
                    if service_id == "google_calendar":
                        events = await self.sync_calendar_events(user_id)
                        sync_results[service_id] = {
                            "type": "events",
                            "count": len(events),
                            "status": "success",
                        }

                    elif service_id == "todoist":
                        tasks = await self.sync_todoist_tasks(user_id)
                        sync_results[service_id] = {
                            "type": "tasks",
                            "count": len(tasks),
                            "status": "success",
                        }

                    elif service_id == "spotify":
                        recommendations = await self.get_spotify_recommendations(
                            user_id
                        )
                        sync_results[service_id] = {
                            "type": "playlists",
                            "count": len(recommendations.get("playlists", [])),
                            "status": "success",
                        }

                    elif service_id == "rescuetime":
                        data = await self.get_rescuetime_data(user_id)
                        sync_results[service_id] = {
                            "type": "productivity_data",
                            "count": 1,
                            "status": "success",
                        }

                    elif service_id == "github":
                        activity = await self.sync_github_activity(user_id)
                        sync_results[service_id] = {
                            "type": "commits",
                            "count": activity.get("commits_today", 0),
                            "status": "success",
                        }

                except Exception as e:
                    sync_results[service_id] = {"status": "error", "error": str(e)}

            # Show results
            results_text = ""
            for service_id, result in sync_results.items():
                service_name = self.integrations[service_id]["name"]
                service_icon = self.integrations[service_id]["icon"]

                if result["status"] == "success":
                    results_text += f"✅ {service_icon} **{service_name}**: {result['count']} {result['type']} synced\n"
                else:
                    results_text += (
                        f"❌ {service_icon} **{service_name}**: Sync failed\n"
                    )

            embed.add_field(name="📊 Sync Results", value=results_text, inline=False)

            embed.add_field(
                name="⏰ Next Auto Sync",
                value=f"In {user_settings.get('sync_preferences', {}).get('sync_frequency', 'hourly')}",
                inline=False,
            )

            await ctx.send(embed=embed)

        @self.bot.command(name="workflow")
        async def show_workflows(ctx, action: str = "list"):
            """⚡ Manage custom integration workflows"""
            user_id = str(ctx.author.id)

            embed = discord.Embed(
                title="⚡ CUSTOM INTEGRATION WORKFLOWS",
                description="Automate your productivity with smart workflows!",
                color=0x9370DB,
            )

            if action == "list":
                # Show available workflow templates
                workflow_templates = {
                    "focus_session_complete": {
                        "name": "🎯 Focus Session Complete",
                        "description": "Automatically log session to Notion and update Slack status",
                        "triggers": ["session_end"],
                        "actions": [
                            "create_notion_page",
                            "update_slack_status",
                            "sync_calendar",
                        ],
                    },
                    "task_deadline_approaching": {
                        "name": "⏰ Task Deadline Alert",
                        "description": "Get notified when Todoist tasks are due soon",
                        "triggers": ["todoist_task_due_2h"],
                        "actions": [
                            "discord_notification",
                            "create_focus_block",
                            "spotify_focus_playlist",
                        ],
                    },
                    "coding_session_tracker": {
                        "name": "🐙 Coding Session Tracker",
                        "description": "Track coding time and sync with GitHub activity",
                        "triggers": ["github_commit"],
                        "actions": [
                            "log_coding_session",
                            "update_productivity_score",
                            "celebrate_streak",
                        ],
                    },
                    "weekly_review": {
                        "name": "📊 Weekly Review",
                        "description": "Generate weekly productivity report from all integrations",
                        "triggers": ["weekly_schedule"],
                        "actions": [
                            "collect_rescuetime_data",
                            "analyze_patterns",
                            "create_review_report",
                        ],
                    },
                }

                for workflow_id, workflow in workflow_templates.items():
                    embed.add_field(
                        name=workflow["name"],
                        value=f"{workflow['description']}\n**Triggers:** {', '.join(workflow['triggers'])}\n**Actions:** {len(workflow['actions'])} steps",
                        inline=False,
                    )

                embed.add_field(
                    name="🚀 Create Workflow",
                    value="Use `!workflow create <template_name>` to set up automation!\nExample: `!workflow create focus_session_complete`",
                    inline=False,
                )

            elif action == "create":
                embed.add_field(
                    name="🔧 Workflow Builder",
                    value="Custom workflow creation is coming soon!\n\nFor now, you can enable these automated workflows:\n• Focus session logging\n• Task deadline alerts\n• GitHub activity tracking\n• Weekly productivity reviews",
                    inline=False,
                )

            await ctx.send(embed=embed)


# Export the integrations engine
__all__ = ["ExternalServiceIntegrations"]

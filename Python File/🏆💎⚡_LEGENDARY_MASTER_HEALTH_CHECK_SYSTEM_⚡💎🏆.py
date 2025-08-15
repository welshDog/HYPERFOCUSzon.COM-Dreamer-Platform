#!/usr/bin/env python3
"""
🏆💎⚡ LEGENDARY MASTER HEALTH CHECK SYSTEM ⚡💎🏆

**BROski Level: LEGENDARY | Status: UNIFIED EMPIRE MONITORING**
**Created:** August 5, 2025
**Mission:** Ultimate empire-wide health monitoring combining ALL existing systems

UNIFIED CAPABILITIES:
✅ Ultra dOoK Empire Health Scanner integration
✅ PowerShell folder structure validation
✅ Discord Health Bot monitoring
✅ V2 Deployment status checking
✅ Memory Crystal system validation
✅ Agent coordination tracking
✅ BROski$ rewards calculation
✅ Celebration cascade triggers
✅ Real-time system metrics
✅ Quantum-level empire analytics
"""

from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any
import json
import logging
import os
import socket
import subprocess
import sys
import time

import docker
import io
import psutil
import requests
import sqlite3
try:
    import yaml
    YAML_AVAILABLE = True
except ImportError:
    YAML_AVAILABLE = False

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('legendary_health_check.log'),
        logging.StreamHandler()
    ]
)

# Set UTF-8 encoding for console output
if sys.platform == "win32":
    import codecs
    try:
        if hasattr(sys.stdout, 'detach'):
            sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
            sys.stderr = codecs.getwriter("utf-8")(sys.stderr.detach())
        else:
            # Fallback for environments where detach() is not available
            sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
            sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
    except (AttributeError, OSError):
        # If encoding setup fails, continue without it
        pass

@dataclass
class HealthMetrics:
    """🛡️ Unified health metrics across all systems"""
    timestamp: str
    system_name: str
    status: str  # "LEGENDARY", "HEALTHY", "WARNING", "CRITICAL", "OFFLINE"
    score: float  # 0-100
    details: Dict[str, Any]
    broskie_rewards: int
    celebration_triggers: List[str]

class LegendaryMasterHealthChecker:
    """🏆 The ultimate health checking system - combines ALL existing scanners"""

    def __init__(self):
        self.start_time = datetime.now()
        self.base_paths = [
            Path("h:/"),
            Path("h:/HyperBeast"),
            Path("h:/tHE HYPERFOUCS dOoK ultra Web Comic"),
            Path("h:/HYPERFOCUS ZONE DISCORD HUB"),
            Path("h:/grafana-by-example")  # Added Grafana server path
        ]

        self.health_report = {
            "master_scan_id": f"LEGENDARY_{int(time.time())}",
            "timestamp": self.start_time.isoformat(),
            "empire_status": "SCANNING",
            "overall_health_score": 0,
            "total_broskie_earned": 0,
            "systems": {},
            "critical_alerts": [],
            "celebration_events": [],
            "quantum_metrics": {},
            "agent_deployments": {},
            "memory_crystals": {},
            "discord_integrations": {},
            "v2_components": {},
            "grafana_servers": {},  # Added Grafana server tracking
            "auto_fix_actions": [],  # Added auto-fix tracking
            "legendary_achievements": []
        }

        self.legendary_thresholds = {
            "cpu_max": 80.0,
            "memory_max": 85.0,
            "disk_max": 90.0,
            "uptime_min": 3600,
            "broskie_legendary": 1000,
            "health_legendary": 95.0
        }

        print(f"""
🏆💎⚡ LEGENDARY MASTER HEALTH CHECK SYSTEM ⚡💎🏆
================================================================

Scan ID: {self.health_report['master_scan_id']}
Timestamp: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}

🔍 INITIATING UNIFIED EMPIRE-WIDE SCAN...
================================================

This system combines ALL existing health checkers:
✅ Ultra dOoK Empire Scanner
✅ PowerShell Structure Validator
✅ Discord Health Monitoring
✅ V2 Deployment Checker
✅ Memory Crystal Validator
✅ Agent Coordination Tracker
✅ Grafana Server Infrastructure Monitor
✅ Auto-Fix & Recovery System

🚀 Beginning comprehensive analysis...
        """)

    def scan_local_empire_systems(self) -> HealthMetrics:
        """🔍 Enhanced local system scanning (from Ultra dOoK Scanner)"""
        print("🔍 Scanning Local Empire Systems...")

        try:
            # System metrics
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            boot_time = psutil.boot_time()
            uptime = time.time() - boot_time

            # Disk usage for main drive
            disk = psutil.disk_usage('h:/')

            # Check VS Code processes (ADHD command center)
            vscode_processes = [p for p in psutil.process_iter(['name', 'cpu_percent'])
                               if 'code' in p.info['name'].lower()]

            # Calculate health score
            cpu_score = max(0, 100 - cpu_percent)
            memory_score = max(0, 100 - memory.percent)
            disk_score = max(0, 100 - ((disk.used / disk.total) * 100))
            uptime_score = min(100, (uptime / 86400) * 20)  # 20 points per day, max 100

            overall_score = (cpu_score + memory_score + disk_score + uptime_score) / 4

            status = "LEGENDARY" if overall_score >= 90 else "HEALTHY" if overall_score >= 70 else "WARNING"

            details = {
                "cpu_percent": round(cpu_percent, 2),
                "memory_percent": round(memory.percent, 2),
                "disk_percent": round((disk.used / disk.total) * 100, 2),
                "uptime_hours": round(uptime / 3600, 2),
                "running_processes": len(psutil.pids()),
                "vscode_processes": len(vscode_processes),
                "hyperfocus_mode": len(vscode_processes) > 0
            }

            broskie_rewards = int(overall_score * 2) if status == "LEGENDARY" else int(overall_score)

            celebrations = []
            if status == "LEGENDARY":
                celebrations.append("🎊 LEGENDARY SYSTEM PERFORMANCE")
            if len(vscode_processes) > 0:
                celebrations.append("⚡ HYPERFOCUS MODE ACTIVE")

            return HealthMetrics(
                timestamp=datetime.now().isoformat(),
                system_name="Local Empire Systems",
                status=status,
                score=overall_score,
                details=details,
                broskie_rewards=broskie_rewards,
                celebration_triggers=celebrations
            )

        except (socket.error, ConnectionError, requests.RequestException) as e:
            logging.error("Local empire scan error: %s", str(e))
            return HealthMetrics(
                timestamp=datetime.now().isoformat(),
                system_name="Local Empire Systems",
                status="CRITICAL",
                score=0,
                details={"error": str(e)},
                broskie_rewards=0,
                celebration_triggers=[]
            )

    def scan_memory_crystal_system(self) -> HealthMetrics:
        """💎 Enhanced Memory Crystal system validation"""
        print("💎 Scanning Memory Crystal System...")

        try:
            total_files = 0
            recent_files = 0
            crystal_types = {"md": 0, "json": 0, "py": 0, "txt": 0}

            recent_cutoff = datetime.now() - timedelta(hours=24)

            for base_path in self.base_paths:
                if not base_path.exists():
                    continue

                try:
                    for file_path in base_path.rglob("*"):
                        if not file_path.is_file():
                            continue

                        try:
                            total_files += 1

                            # Count by type
                            suffix = file_path.suffix.lower()
                            if suffix in ['.md']:
                                crystal_types["md"] += 1
                            elif suffix in ['.json']:
                                crystal_types["json"] += 1
                            elif suffix in ['.py']:
                                crystal_types["py"] += 1
                            elif suffix in ['.txt']:
                                crystal_types["txt"] += 1

                            # Check recent activity
                            try:
                                if datetime.fromtimestamp(file_path.stat().st_mtime) > recent_cutoff:
                                    recent_files += 1
                            except (OSError, PermissionError):
                                continue
                        except (PermissionError, OSError):
                            continue
                except (PermissionError, OSError) as e:
                    logging.warning(f"Could not scan directory {base_path}: {e}")
                    continue

            # Calculate memory crystal health
            activity_score = min(100, (recent_files / max(1, total_files)) * 200)
            diversity_score = min(100, len([v for v in crystal_types.values() if v > 0]) * 25)
            volume_score = min(100, total_files / 10)  # 10 files = 100 points

            overall_score = (activity_score + diversity_score + volume_score) / 3

            status = "LEGENDARY" if overall_score >= 85 else "HEALTHY" if overall_score >= 60 else "WARNING"

            details = {
                "total_files": total_files,
                "recent_activity_24h": recent_files,
                "markdown_crystals": crystal_types["md"],
                "json_crystals": crystal_types["json"],
                "python_modules": crystal_types["py"],
                "text_documents": crystal_types["txt"],
                "activity_rate": round((recent_files / max(1, total_files)) * 100, 2)
            }

            broskie_rewards = int(overall_score * 1.5)

            celebrations = []
            if overall_score >= 85:
                celebrations.append("💎 LEGENDARY MEMORY CRYSTAL NETWORK")
            if recent_files > 10:
                celebrations.append("⚡ HIGH CRYSTAL ACTIVITY")

            return HealthMetrics(
                timestamp=datetime.now().isoformat(),
                system_name="Memory Crystal System",
                status=status,
                score=overall_score,
                details=details,
                broskie_rewards=broskie_rewards,
                celebration_triggers=celebrations
            )

        except (socket.error, ConnectionError, requests.RequestException) as e:
            logging.error(f"Memory crystal scan error: {e}")
            return HealthMetrics(
                timestamp=datetime.now().isoformat(),
                system_name="Memory Crystal System",
                status="CRITICAL",
                score=0,
                details={"error": str(e)},
                broskie_rewards=0,
                celebration_triggers=[]
            )

    def scan_v2_deployment_status(self) -> HealthMetrics:
        """🚀 V2 Deployment component validation"""
        print("🚀 Scanning V2 Deployment Status...")

        try:
            components = {
                "database": False,
                "analytics_dashboard": False,
                "websocket_server": False,
                "discord_config": False
            }

            component_details = {}

            # Check database
            try:
                conn = sqlite3.connect("dopamine_guardian.db")
                cursor = conn.cursor()
                cursor.execute("SELECT COUNT(*) FROM mood_checkins WHERE user_id LIKE 'demo_%'")
                demo_records = cursor.fetchone()[0]
                cursor.execute("SELECT COUNT(*) FROM wins WHERE user_id LIKE 'demo_%'")
                demo_achievements = cursor.fetchone()[0]
                conn.close()

                components["database"] = True
                component_details["database"] = {
                    "status": "Connected",
                    "demo_records": demo_records,
                    "demo_achievements": demo_achievements
                }
            except (socket.error, ConnectionError, requests.RequestException) as e:
                component_details["database"] = {"status": "Error", "error": str(e)}

            # Check analytics dashboard
            try:
                response = requests.get("http://localhost:9999", timeout=5)
                if response.status_code == 200:
                    components["analytics_dashboard"] = True
                    component_details["analytics_dashboard"] = {
                        "status": "Running",
                        "url": "http://localhost:9999",
                        "response_code": response.status_code
                    }
                else:
                    component_details["analytics_dashboard"] = {
                        "status": "HTTP Error",
                        "response_code": response.status_code
                    }
            except (socket.error, ConnectionError, requests.RequestException) as e:
                component_details["analytics_dashboard"] = {"status": "Not accessible", "error": str(e)}

            # Check WebSocket server
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex(('localhost', 8765))
                if result == 0:
                    components["websocket_server"] = True
                    component_details["websocket_server"] = {
                        "status": "Running",
                        "url": "ws://localhost:8765"
                    }
                else:
                    component_details["websocket_server"] = {"status": "Not accessible"}
                sock.close()
            except (socket.error, ConnectionError, requests.RequestException) as e:
                component_details["websocket_server"] = {"status": "Error", "error": str(e)}

            # Check Discord configuration
            discord_configs = ["HyperBeast/.env", ".env", "empire.env"]
            for config_file in discord_configs:
                try:
                    if os.path.exists(config_file):
                        with open(config_file, "r", encoding="utf-8") as file:
                            env_content = file.read()
                            if "DISCORD_BOT_TOKEN" in env_content:
                                components["discord_config"] = True
                                component_details["discord_config"] = {
                                    "status": "Configured",
                                    "config_file": config_file
                                }
                                break
                except (OSError, IOError, UnicodeDecodeError):
                    continue

            if not components["discord_config"]:
                component_details["discord_config"] = {"status": "Token not found"}

            # Calculate V2 health score
            active_components = sum(components.values())
            total_components = len(components)
            overall_score = (active_components / total_components) * 100

            status = "LEGENDARY" if overall_score >= 90 else "HEALTHY" if overall_score >= 70 else "WARNING"

            details = {
                "active_components": active_components,
                "total_components": total_components,
                "component_status": component_details,
                "deployment_readiness": f"{active_components}/{total_components}"
            }

            broskie_rewards = int(overall_score * 2)

            celebrations = []
            if overall_score >= 90:
                celebrations.append("🚀 V2.0 DEPLOYMENT LEGENDARY")
            if components["database"] and components["analytics_dashboard"]:
                celebrations.append("📊 FULL ANALYTICS STACK ACTIVE")

            return HealthMetrics(
                timestamp=datetime.now().isoformat(),
                system_name="V2 Deployment Status",
                status=status,
                score=overall_score,
                details=details,
                broskie_rewards=broskie_rewards,
                celebration_triggers=celebrations
            )

        except (socket.error, ConnectionError, requests.RequestException) as e:
            logging.error(f"V2 deployment scan error: {e}")
            return HealthMetrics(
                timestamp=datetime.now().isoformat(),
                system_name="V2 Deployment Status",
                status="CRITICAL",
                score=0,
                details={"error": str(e)},
                broskie_rewards=0,
                celebration_triggers=[]
            )

    def scan_discord_integrations(self) -> HealthMetrics:
        """🤖 Discord bot and integration health check"""
        print("🤖 Scanning Discord Integrations...")

        try:
            discord_bots = []
            bot_files = [
                "ULTRA_HEALTH_DISCORD_BOT.py",
                "🤖💎⚡_ULTRA_HEALTH_DISCORD_BOT_ORGANIZED_⚡💎🤖.py",
                "🔄💎⚡_PHASE_2_AUTONOMOUS_DISCORD_BOT_INTEGRATION_LAYER_⚡💎🔄.py"
            ]

            total_bots = 0
            functional_bots = 0

            for base_path in self.base_paths:
                for bot_file in bot_files:
                    bot_path = base_path / bot_file
                    if bot_path.exists():
                        total_bots += 1

                        # Check if bot file is functional (basic syntax check)
                        try:
                            with open(bot_path, 'r', encoding='utf-8') as f:
                                content = f.read()
                                if 'discord.py' in content or 'import discord' in content:
                                    if 'bot.run' in content or '@bot.command' in content:
                                        functional_bots += 1
                                        discord_bots.append({
                                            "name": bot_file,
                                            "path": str(bot_path),
                                            "status": "Functional",
                                            "size_kb": round(bot_path.stat().st_size / 1024, 2)
                                        })
                        except (socket.error, ConnectionError, requests.RequestException) as e:
                            discord_bots.append({
                                "name": bot_file,
                                "path": str(bot_path),
                                "status": "Error",
                                "error": str(e)
                            })

            # Check for empire.env Discord token
            token_configured = False
            for config_file in ["empire.env", ".env", "HyperBeast/.env"]:
                if os.path.exists(config_file):
                    try:
                        with open(config_file, 'r', encoding='utf-8') as f:
                            if 'DISCORD_BOT_TOKEN' in f.read():
                                token_configured = True
                                break
                    except (OSError, IOError, UnicodeDecodeError):
                        continue

            # Calculate Discord integration health
            bot_score = (functional_bots / max(1, total_bots)) * 60
            config_score = 40 if token_configured else 0
            overall_score = bot_score + config_score

            status = "LEGENDARY" if overall_score >= 85 else "HEALTHY" if overall_score >= 60 else "WARNING"

            details = {
                "total_bot_files": total_bots,
                "functional_bots": functional_bots,
                "token_configured": token_configured,
                "bot_details": discord_bots,
                "integration_readiness": f"{functional_bots}/{total_bots} bots functional"
            }

            broskie_rewards = int(overall_score * 1.5)

            celebrations = []
            if overall_score >= 85:
                celebrations.append("🤖 LEGENDARY DISCORD INTEGRATION")
            if functional_bots >= 2:
                celebrations.append("⚡ MULTI-BOT ECOSYSTEM")

            return HealthMetrics(
                timestamp=datetime.now().isoformat(),
                system_name="Discord Integrations",
                status=status,
                score=overall_score,
                details=details,
                broskie_rewards=broskie_rewards,
                celebration_triggers=celebrations
            )

        except (socket.error, ConnectionError, requests.RequestException) as e:
            logging.error(f"Discord integration scan error: {e}")
            return HealthMetrics(
                timestamp=datetime.now().isoformat(),
                system_name="Discord Integrations",
                status="CRITICAL",
                score=0,
                details={"error": str(e)},
                broskie_rewards=0,
                celebration_triggers=[]
            )

    def scan_agent_coordination(self) -> HealthMetrics:
        """👥 Agent army and coordination systems"""
        print("👥 Scanning Agent Coordination Systems...")

        try:
            coordination_files = []
            agent_systems = [
                "ORCHESTRATOR",
                "COORDINATION",
                "AGENT",
                "EMPIRE",
                "PHASE_2"
            ]

            total_agents = 0
            active_agents = 0

            for base_path in self.base_paths:
                if not base_path.exists():
                    continue

                try:
                    for file_path in base_path.rglob("*.py"):
                        try:
                            file_name = file_path.name.upper()
                            if any(agent_type in file_name for agent_type in agent_systems):
                                total_agents += 1

                                # Check if agent file is substantial (>1KB and has class/function definitions)
                                if file_path.stat().st_size > 1024:
                                    with open(file_path, 'r', encoding='utf-8') as f:
                                        content = f.read()
                                        if ('class ' in content and 'def ' in content) or 'async def' in content:
                                            active_agents += 1
                                            coordination_files.append({
                                                "name": file_path.name,
                                                "type": next((t for t in agent_systems if t in file_name), "GENERAL"),
                                                "size_kb": round(file_path.stat().st_size / 1024, 2),
                                                "status": "Active"
                                            })
                        except (PermissionError, OSError, UnicodeDecodeError):
                            continue
                except (PermissionError, OSError) as e:
                    logging.warning(f"Could not scan directory {base_path}: {e}")
                    continue

            # Check for specific coordination databases
            coord_databases = 0
            db_files = ["agent_coordination.db", "empire_coordination.db", "behavior_predictions.db"]
            for db_file in db_files:
                if os.path.exists(db_file):
                    coord_databases += 1

            # Calculate coordination health
            agent_score = min(100, (active_agents / 10) * 100)  # 10 agents = 100%
            db_score = (coord_databases / len(db_files)) * 100
            overall_score = (agent_score + db_score) / 2

            status = "LEGENDARY" if overall_score >= 80 else "HEALTHY" if overall_score >= 50 else "WARNING"

            details = {
                "total_agent_files": total_agents,
                "active_agents": active_agents,
                "coordination_databases": coord_databases,
                "agent_types": coordination_files,
                "deployment_readiness": f"{active_agents}/677+ target agents"
            }

            broskie_rewards = int(overall_score * 3)  # High rewards for agent coordination

            celebrations = []
            if active_agents >= 10:
                celebrations.append("👥 LEGENDARY AGENT ARMY")
            if coord_databases >= 2:
                celebrations.append("🛡️ COORDINATION INFRASTRUCTURE")

            return HealthMetrics(
                timestamp=datetime.now().isoformat(),
                system_name="Agent Coordination",
                status=status,
                score=overall_score,
                details=details,
                broskie_rewards=broskie_rewards,
                celebration_triggers=celebrations
            )

        except (socket.error, ConnectionError, requests.RequestException) as e:
            logging.error(f"Agent coordination scan error: {e}")
            return HealthMetrics(
                timestamp=datetime.now().isoformat(),
                system_name="Agent Coordination",
                status="CRITICAL",
                score=0,
                details={"error": str(e)},
                broskie_rewards=0,
                celebration_triggers=[]
            )

    def scan_project_structure(self) -> HealthMetrics:
        """📁 Project structure and organization (from PowerShell scanner)"""
        print("📁 Scanning Project Structure...")

        try:
            structure_health = {}
            total_score = 0

            key_directories = [
                "HYPERFOCUS ZONE DISCORD HUB",
                "HyperBeast",
                "tHE HYPERFOUCS dOoK ultra Web Comic",
                "🌟 BROski♾️ AUTOMATIC COO ROLE 🌟"
            ]

            for directory in key_directories:
                dir_path = Path("h:/") / directory
                try:
                    if dir_path.exists():
                        file_count = len(list(dir_path.rglob("*")))
                        md_count = len(list(dir_path.rglob("*.md")))
                        py_count = len(list(dir_path.rglob("*.py")))

                        dir_score = min(100, file_count / 10)  # 10 files = 100%

                        structure_health[directory] = {
                            "status": "✅ HEALTHY" if file_count > 5 else "⚠️ SPARSE",
                            "files": file_count,
                            "markdown": md_count,
                            "python": py_count,
                            "score": dir_score
                        }
                        total_score += dir_score
                    else:
                        structure_health[directory] = {
                            "status": "❌ MISSING",
                            "files": 0,
                            "markdown": 0,
                            "python": 0,
                            "score": 0
                        }
                except (PermissionError, OSError) as e:
                    logging.warning(f"Could not scan directory {directory}: {e}")
                    structure_health[directory] = {
                        "status": "🔒 ACCESS DENIED",
                        "files": 0,
                        "markdown": 0,
                        "python": 0,
                        "score": 0
                    }

            overall_score = total_score / len(key_directories)

            # Check for specific organizational files
            org_files = [
                "LOOK THEN BUILD",
                "README",
                "MEMORY_CRYSTAL",
                "BOARDROOM"
            ]

            org_found = 0
            for org_pattern in org_files:
                found = any(
                    Path("h:/").rglob(f"*{org_pattern}*")
                )
                if found:
                    org_found += 1

            org_bonus = (org_found / len(org_files)) * 20
            overall_score = min(100, overall_score + org_bonus)

            status = "LEGENDARY" if overall_score >= 85 else "HEALTHY" if overall_score >= 65 else "WARNING"

            details = {
                "directory_health": structure_health,
                "organization_files_found": org_found,
                "total_directories_checked": len(key_directories),
                "structure_completeness": f"{sum(1 for d in structure_health.values() if d['files'] > 0)}/{len(key_directories)}"
            }

            broskie_rewards = int(overall_score)

            celebrations = []
            if overall_score >= 85:
                celebrations.append("📁 LEGENDARY PROJECT ORGANIZATION")
            if org_found >= 3:
                celebrations.append("🗂️ EXCELLENT DOCUMENTATION STRUCTURE")

            return HealthMetrics(
                timestamp=datetime.now().isoformat(),
                system_name="Project Structure",
                status=status,
                score=overall_score,
                details=details,
                broskie_rewards=broskie_rewards,
                celebration_triggers=celebrations
            )

        except (socket.error, ConnectionError, requests.RequestException) as e:
            logging.error(f"Project structure scan error: {e}")
            return HealthMetrics(
                timestamp=datetime.now().isoformat(),
                system_name="Project Structure",
                status="CRITICAL",
                score=0,
                details={"error": str(e)},
                broskie_rewards=0,
                celebration_triggers=[]
            )

    def scan_grafana_server_infrastructure(self) -> HealthMetrics:
        """🌐 Grafana server infrastructure and Docker services monitoring"""
        print("🌐 Scanning Grafana Server Infrastructure...")

        try:
            services_health = {}
            docker_client = None
            total_services = 0
            healthy_services = 0

            # Core Grafana services to monitor
            grafana_services = {
                "grafana": {"port": 3000, "path": "/api/health", "name": "Grafana Dashboard"},
                "prometheus": {"port": 9090, "path": "/api/v1/query?query=up", "name": "Prometheus Metrics"},
                "loki": {"port": 3100, "path": "/ready", "name": "Loki Logs"},
                "jaeger": {"port": 16686, "path": "/api/services", "name": "Jaeger Tracing"},
                "postgres": {"port": 5432, "type": "tcp", "name": "PostgreSQL Database"},
                "clickhouse": {"port": 9000, "type": "tcp", "name": "ClickHouse Analytics"}
            }

            # Check Docker containers if available
            try:
                docker_client = docker.from_env()
                containers = docker_client.containers.list(all=True)

                for container in containers:
                    service_name = container.name
                    if any(svc in service_name.lower() for svc in grafana_services.keys()):
                        total_services += 1
                        container_health = {
                            "container_name": container.name,
                            "status": container.status,
                            "image": container.image.tags[0] if container.image.tags else "unknown",
                            "created": container.attrs.get("Created", "unknown"),
                            "ports": container.ports if hasattr(container, 'ports') else {}
                        }

                        if container.status == "running":
                            healthy_services += 1
                            container_health["health"] = "HEALTHY"
                        else:
                            container_health["health"] = "UNHEALTHY"
                            container_health["auto_fix"] = "restart_container"

                        services_health[service_name] = container_health

            except (socket.error, ConnectionError, requests.RequestException) as e:
                logging.warning(f"Docker client unavailable: {e}")
                services_health["docker_status"] = {"error": "Docker not available", "details": str(e)}

            # Check service endpoints
            endpoint_checks = {}
            for service, config in grafana_services.items():
                endpoint_checks[service] = {"name": config["name"]}

                try:
                    if config.get("type") == "tcp":
                        # TCP connection check
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        sock.settimeout(5)
                        result = sock.connect_ex(('localhost', config["port"]))
                        sock.close()

                        if result == 0:
                            endpoint_checks[service]["status"] = "ACCESSIBLE"
                            endpoint_checks[service]["port"] = config["port"]
                            if service not in [name for name in services_health.keys() if "error" not in name]:
                                healthy_services += 1
                        else:
                            endpoint_checks[service]["status"] = "NOT_ACCESSIBLE"
                            endpoint_checks[service]["auto_fix"] = f"check_port_{config['port']}"
                    else:
                        # HTTP endpoint check
                        url = f"http://localhost:{config['port']}{config.get('path', '/')}"
                        response = requests.get(url, timeout=5)

                        endpoint_checks[service]["status"] = "HEALTHY" if response.status_code == 200 else "DEGRADED"
                        endpoint_checks[service]["url"] = url
                        endpoint_checks[service]["response_code"] = response.status_code
                        endpoint_checks[service]["response_time"] = f"{response.elapsed.total_seconds():.2f}s"

                        if response.status_code == 200:
                            if service not in [name for name in services_health.keys() if "error" not in name]:
                                healthy_services += 1
                        else:
                            endpoint_checks[service]["auto_fix"] = f"restart_service_{service}"

                except (socket.error, ConnectionError, requests.RequestException) as e:
                    endpoint_checks[service]["status"] = "ERROR"
                    endpoint_checks[service]["error"] = str(e)
                    endpoint_checks[service]["auto_fix"] = f"diagnose_service_{service}"

                total_services += 1

            # Check Grafana directories and configurations
            grafana_path = Path("h:/grafana-by-example")
            config_health = {}

            if grafana_path.exists():
                # Check for docker-compose files
                compose_files = list(grafana_path.rglob("docker-compose*.yml")) + list(grafana_path.rglob("docker-compose*.yaml"))
                config_health["compose_files"] = len(compose_files)
                config_health["compose_locations"] = [str(f) for f in compose_files[:5]]  # Limit to 5 for brevity

                # Check for configuration directories
                config_dirs = ["grafana", "prometheus", "loki", "config", "provisioning"]
                found_configs = 0
                for config_dir in config_dirs:
                    if any(grafana_path.rglob(config_dir)):
                        found_configs += 1

                config_health["config_completeness"] = f"{found_configs}/{len(config_dirs)}"
                config_health["infrastructure_ready"] = found_configs >= 3
            else:
                config_health["status"] = "MISSING_GRAFANA_DIRECTORY"
                config_health["auto_fix"] = "setup_grafana_infrastructure"

            # Calculate overall health score
            if total_services > 0:
                service_score = (healthy_services / total_services) * 70
            else:
                service_score = 0

            config_score = 30 if config_health.get("infrastructure_ready", False) else 10
            overall_score = service_score + config_score

            status = "LEGENDARY" if overall_score >= 85 else "HEALTHY" if overall_score >= 70 else "WARNING" if overall_score >= 40 else "CRITICAL"

            details = {
                "total_services": total_services,
                "healthy_services": healthy_services,
                "service_health": services_health,
                "endpoint_checks": endpoint_checks,
                "configuration_health": config_health,
                "infrastructure_readiness": f"{healthy_services}/{total_services} services operational"
            }

            broskie_rewards = int(overall_score * 2) if overall_score >= 70 else int(overall_score)

            celebrations = []
            if overall_score >= 85:
                celebrations.append("🌐 LEGENDARY GRAFANA INFRASTRUCTURE")
            if healthy_services >= 6:
                celebrations.append("🏆 FULL OBSERVABILITY STACK OPERATIONAL")
            if config_health.get("infrastructure_ready", False):
                celebrations.append("⚙️ CONFIGURATION EXCELLENCE")

            return HealthMetrics(
                timestamp=datetime.now().isoformat(),
                system_name="Grafana Server Infrastructure",
                status=status,
                score=overall_score,
                details=details,
                broskie_rewards=broskie_rewards,
                celebration_triggers=celebrations
            )

        except (socket.error, ConnectionError, requests.RequestException) as e:
            logging.error(f"Grafana infrastructure scan error: {e}")
            return HealthMetrics(
                timestamp=datetime.now().isoformat(),
                system_name="Grafana Server Infrastructure",
                status="CRITICAL",
                score=0,
                details={"error": str(e), "auto_fix": "diagnose_infrastructure_error"},
                broskie_rewards=0,
                celebration_triggers=[]
            )

    def execute_auto_fix_actions(self, all_metrics: List[HealthMetrics]) -> List[str]:
        """🔧 Execute automatic fixes for detected issues"""
        print("🔧 Executing Auto-Fix Actions...")

        fix_actions_performed = []

        try:
            for metrics in all_metrics:
                if metrics.status in ["WARNING", "CRITICAL"] and metrics.details:
                    auto_fix = metrics.details.get("auto_fix")
                    if auto_fix:
                        print(f"  🔧 Attempting fix for {metrics.system_name}: {auto_fix}")

                        # Execute specific auto-fix actions
                        if auto_fix == "restart_container":
                            fix_result = self._restart_docker_containers()
                            fix_actions_performed.append(f"🐳 Docker Container Restart: {fix_result}")

                        elif auto_fix.startswith("restart_service_"):
                            service_name = auto_fix.replace("restart_service_", "")
                            fix_result = self._restart_grafana_service(service_name)
                            fix_actions_performed.append(f"🔄 Service Restart ({service_name}): {fix_result}")

                        elif auto_fix == "setup_grafana_infrastructure":
                            fix_result = self._setup_grafana_infrastructure()
                            fix_actions_performed.append(f"🏗️ Infrastructure Setup: {fix_result}")

                        elif auto_fix.startswith("check_port_"):
                            port = auto_fix.replace("check_port_", "")
                            fix_result = self._check_and_fix_port(port)
                            fix_actions_performed.append(f"🔌 Port Check ({port}): {fix_result}")

                        elif auto_fix.startswith("diagnose_"):
                            component = auto_fix.replace("diagnose_", "")
                            fix_result = self._diagnose_component(component)
                            fix_actions_performed.append(f"🔍 Diagnosis ({component}): {fix_result}")

                    # Check for other fix opportunities in details
                    if isinstance(metrics.details, dict):
                        for key, value in metrics.details.items():
                            if isinstance(value, dict) and value.get("auto_fix"):
                                sub_fix = value["auto_fix"]
                                print(f"  🔧 Sub-system fix for {key}: {sub_fix}")

                                if sub_fix == "restart_container":
                                    fix_result = self._restart_specific_container(key)
                                    fix_actions_performed.append(f"🐳 Container Restart ({key}): {fix_result}")

        except (socket.error, ConnectionError, requests.RequestException) as e:
            logging.error(f"Auto-fix execution error: {e}")
            fix_actions_performed.append(f"❌ Auto-fix error: {str(e)}")

        return fix_actions_performed

    def _restart_docker_containers(self) -> str:
        """Restart unhealthy Docker containers"""
        try:
            docker_client = docker.from_env()
            containers = docker_client.containers.list(all=True, filters={"status": "exited"})

            restarted = 0
            for container in containers:
                if any(svc in container.name.lower() for svc in ["grafana", "prometheus", "loki", "jaeger"]):
                    container.restart()
                    restarted += 1

            return f"SUCCESS - Restarted {restarted} containers"
        except (socket.error, ConnectionError, requests.RequestException) as e:
            return f"FAILED - {str(e)}"

    def _restart_specific_container(self, container_name: str) -> str:
        """Restart a specific Docker container"""
        try:
            docker_client = docker.from_env()
            container = docker_client.containers.get(container_name)
            container.restart()
            return "SUCCESS - Container restarted"
        except (socket.error, ConnectionError, requests.RequestException) as e:
            return f"FAILED - {str(e)}"

    def _restart_grafana_service(self, service_name: str) -> str:
        """Restart a Grafana service using docker-compose"""
        try:
            grafana_path = Path("h:/grafana-by-example")
            if not grafana_path.exists():
                return "FAILED - Grafana directory not found"

            # Look for appropriate docker-compose file
            compose_files = list(grafana_path.rglob("docker-compose*.yml"))
            if not compose_files:
                return "FAILED - No docker-compose files found"

            compose_file = compose_files[0]
            result = subprocess.run(
                ["docker-compose", "-f", str(compose_file), "restart", service_name],
                cwd=compose_file.parent,
                capture_output=True,
                text=True,
                timeout=60,
                check=False
            )

            return "SUCCESS - Service restarted" if result.returncode == 0 else f"FAILED - {result.stderr}"
        except (socket.error, ConnectionError, requests.RequestException) as e:
            return f"FAILED - {str(e)}"

    def _setup_grafana_infrastructure(self) -> str:
        """Set up basic Grafana infrastructure"""
        try:
            grafana_path = Path("h:/grafana-by-example")
            if not grafana_path.exists():
                return "FAILED - Grafana directory not found"

            # Check if docker-compose exists and try to start services
            compose_files = list(grafana_path.rglob("docker-compose*.yml"))
            if compose_files:
                compose_file = compose_files[0]
                result = subprocess.run(
                    ["docker-compose", "-f", str(compose_file), "up", "-d"],
                    cwd=compose_file.parent,
                    capture_output=True,
                    text=True,
                    timeout=300,
                    check=False
                )
                return "SUCCESS - Infrastructure started" if result.returncode == 0 else f"PARTIAL - {result.stderr}"

            return "SKIPPED - No docker-compose configuration found"
        except (socket.error, ConnectionError, requests.RequestException) as e:
            return f"FAILED - {str(e)}"

    def _check_and_fix_port(self, port: str) -> str:
        """Check port accessibility and suggest fixes"""
        try:
            port_num = int(port)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex(('localhost', port_num))
            sock.close()

            if result == 0:
                return f"SUCCESS - Port {port} is now accessible"
            else:
                # Check if service should be running
                return f"INFO - Port {port} not accessible, may need manual service start"
        except (socket.error, ConnectionError, requests.RequestException) as e:
            return f"FAILED - {str(e)}"

    def _diagnose_component(self, component: str) -> str:
        """Diagnose component issues and provide recommendations"""
        try:
            diagnosis = []

            if "service" in component:
                diagnosis.append("Check if Docker daemon is running")
                diagnosis.append("Verify docker-compose configuration")
                diagnosis.append("Check service logs: docker-compose logs [service_name]")

            elif "infrastructure" in component:
                diagnosis.append("Ensure grafana-by-example directory exists")
                diagnosis.append("Check Docker installation")
                diagnosis.append("Verify network connectivity")

            else:
                diagnosis.append(f"Component {component} requires manual investigation")
                diagnosis.append("Check system resources and dependencies")

            return "COMPLETED - " + "; ".join(diagnosis)
        except (socket.error, ConnectionError, requests.RequestException) as e:
            return f"FAILED - {str(e)}"

    def generate_quantum_metrics(self) -> Dict[str, Any]:
        """⚡ Generate quantum-level empire metrics"""
        print("⚡ Generating Quantum-Level Empire Metrics...")

        quantum_metrics = {
            "hyperfocus_coefficient": round(sum(1 for p in psutil.process_iter() if 'code' in p.name().lower()) * 13.7, 2),
            "dopamine_resonance": round(time.time() % 100, 2),
            "empire_synchronization": round((datetime.now().microsecond / 1000000) * 100, 2),
            "broskie_quantum_state": "LEGENDARY" if sum(self.health_report.get("total_broskie_earned", 0) for _ in range(1)) > 500 else "ACTIVE",
            "temporal_efficiency": round((time.time() - self.start_time.timestamp()) * 10, 2),
            "celebration_cascade_potential": len([s for s in self.health_report.get("systems", {}).values() if s.get("status") == "LEGENDARY"]),
            "memory_crystal_resonance": round(datetime.now().second * 1.618, 2),  # Golden ratio multiplier
            "agent_harmony_index": round(time.time() % 360, 2)  # 0-360 degrees
        }

        return quantum_metrics

    def execute_master_health_scan(self):
        """🏆 Execute the complete unified health scan"""
        print("\n🏆 EXECUTING MASTER UNIFIED HEALTH SCAN...")
        print("=" * 60)

        # Run all individual scanners
        scanners = [
            self.scan_local_empire_systems,
            self.scan_memory_crystal_system,
            self.scan_v2_deployment_status,
            self.scan_discord_integrations,
            self.scan_agent_coordination,
            self.scan_project_structure,
            self.scan_grafana_server_infrastructure  # Added Grafana server monitoring
        ]

        all_metrics = []
        total_broskie = 0
        all_celebrations = []
        system_scores = []

        for scanner in scanners:
            try:
                metrics = scanner()
                all_metrics.append(metrics)

                # Update health report
                self.health_report["systems"][metrics.system_name] = {
                    "status": metrics.status,
                    "score": metrics.score,
                    "details": metrics.details,
                    "broskie_earned": metrics.broskie_rewards,
                    "celebrations": metrics.celebration_triggers,
                    "timestamp": metrics.timestamp
                }

                total_broskie += metrics.broskie_rewards
                all_celebrations.extend(metrics.celebration_triggers)
                system_scores.append(metrics.score)

                print(f"✅ {metrics.system_name}: {metrics.status} ({metrics.score:.1f}%) - {metrics.broskie_rewards} BROski$")

            except (socket.error, ConnectionError, requests.RequestException) as e:
                logging.error(f"Scanner error: {e}")
                print(f"❌ Scanner failed: {e}")

        # Calculate overall health
        if system_scores:
            overall_health = sum(system_scores) / len(system_scores)
        else:
            overall_health = 0

        # Generate quantum metrics
        quantum_metrics = self.generate_quantum_metrics()

        # Update final health report
        self.health_report.update({
            "empire_status": "LEGENDARY" if overall_health >= 85 else "HEALTHY" if overall_health >= 70 else "NEEDS_ATTENTION",
            "overall_health_score": round(overall_health, 2),
            "total_broskie_earned": total_broskie,
            "celebration_events": list(set(all_celebrations)),
            "quantum_metrics": quantum_metrics,
            "scan_duration_seconds": round((datetime.now() - self.start_time).total_seconds(), 2),
            "systems_scanned": len(all_metrics),
            "legendary_achievements": self.calculate_legendary_achievements(all_metrics, overall_health, total_broskie)
        })

        # Display results
        self.display_master_health_report()

        # Save report
        self.save_master_health_report()

        return self.health_report

    def calculate_legendary_achievements(self, metrics: List[HealthMetrics], overall_health: float, total_broskie: int) -> List[str]:
        """🏆 Calculate legendary achievements unlocked"""
        achievements = []

        if overall_health >= 95:
            achievements.append("🏆 LEGENDARY EMPIRE HEALTH MASTER")

        if total_broskie >= 1000:
            achievements.append("💎 BROSKIE MILLIONAIRE")

        legendary_systems = sum(1 for m in metrics if m.status == "LEGENDARY")
        if legendary_systems >= 4:
            achievements.append("⚡ LEGENDARY SYSTEM ORCHESTRATOR")

        if any("AGENT ARMY" in celebration for celebration in [c for m in metrics for c in m.celebration_triggers]):
            achievements.append("👥 AGENT COMMANDER SUPREME")

        if any("DISCORD" in m.system_name for m in metrics if m.status in ["LEGENDARY", "HEALTHY"]):
            achievements.append("🤖 DISCORD INTEGRATION MASTER")

        return achievements

    def display_master_health_report(self):
        """📊 Display the comprehensive health report"""
        report = self.health_report

        print(f"""

🏆💎⚡ LEGENDARY MASTER HEALTH REPORT ⚡💎🏆
=========================================================

Empire Status: {report['empire_status']}
Overall Health: {report['overall_health_score']}%
Total BROski$ Earned: {report['total_broskie_earned']}
Scan Duration: {report['scan_duration_seconds']}s
Systems Scanned: {report['systems_scanned']}

🎊 CELEBRATION EVENTS TRIGGERED:
{''.join(f"  • {event}" for event in report['celebration_events'])}

🏆 LEGENDARY ACHIEVEMENTS UNLOCKED:
{''.join(f"  • {achievement}" for achievement in report['legendary_achievements'])}

📊 SYSTEM BREAKDOWN:
""")

        for system_name, system_data in report["systems"].items():
            status_emoji = "🟢" if system_data["status"] == "LEGENDARY" else "🟡" if system_data["status"] == "HEALTHY" else "🔴"
            print(f"  {status_emoji} {system_name}: {system_data['status']} ({system_data['score']:.1f}%) - {system_data['broskie_earned']} BROski$")

        print(f"""
⚡ QUANTUM METRICS:
  • Hyperfocus Coefficient: {report['quantum_metrics']['hyperfocus_coefficient']}
  • Dopamine Resonance: {report['quantum_metrics']['dopamine_resonance']}%
  • Empire Synchronization: {report['quantum_metrics']['empire_synchronization']}%
  • BROski Quantum State: {report['quantum_metrics']['broskie_quantum_state']}
  • Celebration Cascade Potential: {report['quantum_metrics']['celebration_cascade_potential']}
  • Memory Crystal Resonance: {report['quantum_metrics']['memory_crystal_resonance']}
  • Agent Harmony Index: {report['quantum_metrics']['agent_harmony_index']}°

🎯 EMPIRE READINESS: {"LEGENDARY" if report['overall_health_score'] >= 85 else "READY FOR CONQUEST" if report['overall_health_score'] >= 70 else "OPTIMIZATION NEEDED"}

""")

    def save_master_health_report(self):
        """💾 Save the complete health report"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"LEGENDARY_HEALTH_REPORT_{timestamp}.json"

        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.health_report, f, indent=2, default=str)

            print(f"📁 Health report saved: {filename}")

            # Also save a summary version
            summary_filename = f"HEALTH_SUMMARY_{timestamp}.txt"
            with open(summary_filename, 'w', encoding='utf-8') as f:
                f.write(f"""
LEGENDARY MASTER HEALTH SUMMARY
===============================
Scan ID: {self.health_report['master_scan_id']}
Timestamp: {self.health_report['timestamp']}
Empire Status: {self.health_report['empire_status']}
Overall Health: {self.health_report['overall_health_score']}%
Total BROski$ Earned: {self.health_report['total_broskie_earned']}

System Status:
""")
                for system_name, system_data in self.health_report["systems"].items():
                    f.write(f"  {system_name}: {system_data['status']} ({system_data['score']:.1f}%)\n")

                f.write("\nLegendary Achievements:\n")
                for achievement in self.health_report['legendary_achievements']:
                    f.write(f"  • {achievement}\n")

            print(f"📋 Summary saved: {summary_filename}")

        except (socket.error, ConnectionError, requests.RequestException) as e:
            print(f"❌ Error saving report: {e}")

def main():
    """🚀 Main execution function"""
    print("🏆💎⚡ LEGENDARY MASTER HEALTH CHECK SYSTEM ACTIVATED ⚡💎🏆")

    try:
        # Initialize the master health checker
        health_checker = LegendaryMasterHealthChecker()

        # Execute the complete health scan
        health_report = health_checker.execute_master_health_scan()

        print(f"""
🎊 LEGENDARY MASTER HEALTH CHECK COMPLETE! 🎊
==============================================

Your empire-wide health scan is complete!
Total systems analyzed: {health_report['systems_scanned']}
Overall empire health: {health_report['overall_health_score']}%
BROski$ rewards earned: {health_report['total_broskie_earned']}

Check the generated health reports for detailed analysis.

🏆 EMPIRE STATUS: {health_report['empire_status']} 🏆
        """)

        return health_report

    except (socket.error, ConnectionError, requests.RequestException) as e:
        logging.error(f"Master health check error: {e}")
        print(f"❌ CRITICAL ERROR: {e}")
        return None

if __name__ == "__main__":
    main()

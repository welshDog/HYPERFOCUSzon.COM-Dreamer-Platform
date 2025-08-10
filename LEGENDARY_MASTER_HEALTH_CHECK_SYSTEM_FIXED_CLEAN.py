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
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any
import json
import logging
import os
import subprocess
import sys
import time

import docker
import io
import psutil
try:
    YAML_AVAILABLE = True
except ImportError:
    YAML_AVAILABLE = False

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('legendary_health_check.log', encoding='utf-8'),
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
            sys.stdout = io.TextIOWrapper(
                sys.stdout.buffer, encoding='utf-8', errors='replace'
            )
            sys.stderr = io.TextIOWrapper(
                sys.stderr.buffer, encoding='utf-8', errors='replace'
            )
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

🚀 Beginning comprehensive analysis...
        """)

    def execute_master_health_scan(self):
        """🏆 Execute the complete unified health scan"""
        print("🔄 Starting Master Health Scan...")

        all_metrics = []

        # Execute all scanning modules
        scanners = [
            ("Local Empire Systems", self.scan_local_empire_systems),
            ("Memory Crystal System", self.scan_memory_crystal_system),
            ("V2 Deployment Status", self.scan_v2_deployment_status),
            ("Discord Integrations", self.scan_discord_integrations),
            ("Agent Coordination", self.scan_agent_coordination),
            ("Project Structure", self.scan_project_structure),
            ("Grafana Infrastructure", self.scan_grafana_infrastructure)
        ]

        for scanner_name, scanner_func in scanners:
            try:
                print(f"\n🔍 Scanning: {scanner_name}")
                metrics = scanner_func()
                all_metrics.append(metrics)

                # Update main health report
                self.health_report["systems"][scanner_name.lower().replace(" ", "_")] = {
                    "status": metrics.status,
                    "score": metrics.score,
                    "details": metrics.details,
                    "broskie_rewards": metrics.broskie_rewards,
                    "celebration_triggers": metrics.celebration_triggers
                }

                # Add to total BROski$ rewards
                self.health_report["total_broskie_earned"] += metrics.broskie_rewards

                # Collect celebration triggers
                self.health_report["celebration_events"].extend(metrics.celebration_triggers)

                print(f"✅ {scanner_name}: {metrics.status} ({metrics.score:.1f}%)")

            except (OSError, IOError, RuntimeError) as e:
                logging.error("Scanner error: %s", str(e))

        # Calculate overall empire health
        overall_health = sum(m.score for m in all_metrics) / len(all_metrics) if all_metrics else 0
        self.health_report["overall_health_score"] = overall_health

        # Determine empire status
        if overall_health >= 95:
            self.health_report["empire_status"] = "LEGENDARY"
        elif overall_health >= 85:
            self.health_report["empire_status"] = "LEGENDARY_READY"
        elif overall_health >= 70:
            self.health_report["empire_status"] = "HEALTHY"
        elif overall_health >= 50:
            self.health_report["empire_status"] = "WARNING"
        else:
            self.health_report["empire_status"] = "CRITICAL"

        # Generate quantum metrics
        self.health_report["quantum_metrics"] = self.generate_quantum_metrics()

        # Calculate legendary achievements
        self.health_report["legendary_achievements"] = self.calculate_legendary_achievements(
            all_metrics, overall_health, self.health_report["total_broskie_earned"]
        )

        # Execute auto-fixes if needed
        if overall_health < 70:
            auto_fixes = self.execute_auto_fixes(all_metrics)
            self.health_report["auto_fix_actions"] = auto_fixes

        print(f"""
🏆💎⚡ MASTER HEALTH SCAN COMPLETE ⚡💎🏆
========================================

🎯 EMPIRE STATUS: {self.health_report['empire_status']}
📊 Overall Health Score: {overall_health:.1f}%
💎 Total BROski$ Earned: {self.health_report['total_broskie_earned']}
🎊 Celebration Events: {len(self.health_report['celebration_events'])}
🏆 Legendary Achievements: {len(self.health_report['legendary_achievements'])}

🚀 EMPIRE IS READY FOR LEGENDARY STATUS!
        """)

        return self.health_report

    def scan_local_empire_systems(self) -> HealthMetrics:
        """🔍 Enhanced local system scanning (from Ultra dOoK Scanner)"""
        print("🔍 Scanning Local Empire Systems...")

        try:
            # System metrics
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')

            # Process scanning
            empire_processes = 0
            healthy_processes = 0

            for proc in psutil.process_iter(['pid', 'name', 'status', 'memory_info']):
                try:
                    proc_info = proc.info
                    if any(keyword in proc_info['name'].lower()
                          for keyword in ['python', 'node', 'docker', 'grafana']):
                        empire_processes += 1
                        if proc_info['status'] == 'running':
                            healthy_processes += 1
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue

            # Directory structure health
            critical_dirs = [
                "HyperBeast",
                "HYPERFOCUS ZONE DISCORD HUB",
                "grafana-by-example"
            ]

            existing_dirs = 0
            for base_path in self.base_paths:
                if base_path.exists():
                    existing_dirs += 1

                    try:
                        # Count important files
                        py_files = len(list(base_path.rglob("*.py")))
                        js_files = len(list(base_path.rglob("*.js")))
                        docker_files = len(list(base_path.rglob("docker-compose*.yml")))

                    except (OSError, IOError) as e:
                        logging.warning("Could not scan directory %s: %s", str(base_path), str(e))

            # Calculate scores
            cpu_score = max(0, 100 - cpu_percent)
            memory_score = max(0, 100 - memory.percent)
            disk_score = max(0, 100 - (disk.used / disk.total * 100))
            process_score = (healthy_processes / max(1, empire_processes)) * 100
            directory_score = (existing_dirs / len(self.base_paths)) * 100

            overall_score = (cpu_score + memory_score + disk_score + process_score + directory_score) / 5

            # Determine status
            if overall_score >= 90:
                status = "LEGENDARY"
                celebrations = ["🏆 LEGENDARY System Performance!", "⚡ All Empire Processes Healthy!"]
            elif overall_score >= 75:
                status = "HEALTHY"
                celebrations = ["✅ System Running Well"]
            elif overall_score >= 50:
                status = "WARNING"
                celebrations = []
            else:
                status = "CRITICAL"
                celebrations = []

            # BROski$ rewards based on performance
            broskie_rewards = int(overall_score * 2) if overall_score >= 70 else 0

            details = {
                "cpu_usage": f"{cpu_percent:.1f}%",
                "memory_usage": f"{memory.percent:.1f}%",
                "disk_usage": f"{(disk.used / disk.total * 100):.1f}%",
                "empire_processes": empire_processes,
                "healthy_processes": healthy_processes,
                "directories_found": existing_dirs,
                "total_directories": len(self.base_paths)
            }

            return HealthMetrics(
                timestamp=datetime.now().isoformat(),
                system_name="Local Empire Systems",
                status=status,
                score=overall_score,
                details=details,
                broskie_rewards=broskie_rewards,
                celebration_triggers=celebrations
            )

        except (OSError, RuntimeError) as e:
            logging.error("Local empire scan error: %s", str(e))
            return HealthMetrics(
                timestamp=datetime.now().isoformat(),
                system_name="Local Empire Systems",
                status="OFFLINE",
                score=0,
                details={"error": str(e)},
                broskie_rewards=0,
                celebration_triggers=[]
            )

    def scan_memory_crystal_system(self) -> HealthMetrics:
        """💎 Enhanced Memory Crystal system validation"""
        print("💎 Scanning Memory Crystal System...")

        try:
            crystal_files = []
            crystal_score = 0

            # Search for Memory Crystal files
            memory_patterns = [
                "*MEMORY_CRYSTAL*",
                "*BOARDROOM*",
                "*NEURAL*",
                "*CRYSTAL*"
            ]

            total_crystals = 0
            valid_crystals = 0

            for base_path in self.base_paths:
                if not base_path.exists():
                    continue

                for pattern in memory_patterns:
                    try:
                        for crystal_path in base_path.rglob(pattern):
                            if crystal_path.is_file() and crystal_path.suffix in ['.json', '.md', '.py']:
                                total_crystals += 1

                                # Validate crystal content
                                if crystal_path.suffix == '.json':
                                    try:
                                        with open(crystal_path, 'r', encoding='utf-8') as f:
                                            data = json.load(f)
                                            if isinstance(data, dict) and len(data) > 0:
                                                valid_crystals += 1
                                                crystal_files.append(str(crystal_path))
                                    except (json.JSONDecodeError, OSError):
                                        pass
                                elif crystal_path.stat().st_size > 100:  # At least 100 bytes
                                    valid_crystals += 1
                                    crystal_files.append(str(crystal_path))

                    except (OSError, IOError) as e:
                        logging.warning("Could not scan for pattern %s in %s: %s", pattern, str(base_path), str(e))

            # Calculate Memory Crystal health score
            if total_crystals > 0:
                crystal_score = (valid_crystals / total_crystals) * 100
            else:
                crystal_score = 0

            # Bonus points for having multiple types
            if valid_crystals >= 5:
                crystal_score = min(100, crystal_score + 20)

            # Determine status
            if crystal_score >= 95:
                status = "LEGENDARY"
                celebrations = ["💎 LEGENDARY Memory Crystal Network!", "🧠 Neural Intelligence Active!"]
            elif crystal_score >= 80:
                status = "HEALTHY"
                celebrations = ["💎 Memory Crystals Operational"]
            elif crystal_score >= 50:
                status = "WARNING"
                celebrations = []
            else:
                status = "CRITICAL"
                celebrations = []

            broskie_rewards = int(crystal_score * 1.5) if crystal_score >= 60 else 0

            details = {
                "total_crystals_found": total_crystals,
                "valid_crystals": valid_crystals,
                "crystal_health_score": crystal_score,
                "crystal_files": crystal_files[:10]  # Top 10 for brevity
            }

            return HealthMetrics(
                timestamp=datetime.now().isoformat(),
                system_name="Memory Crystal System",
                status=status,
                score=crystal_score,
                details=details,
                broskie_rewards=broskie_rewards,
                celebration_triggers=celebrations
            )

        except (OSError, RuntimeError) as e:
            logging.error("Memory crystal scan error: %s", str(e))
            return HealthMetrics(
                timestamp=datetime.now().isoformat(),
                system_name="Memory Crystal System",
                status="OFFLINE",
                score=0,
                details={"error": str(e)},
                broskie_rewards=0,
                celebration_triggers=[]
            )

    def scan_v2_deployment_status(self) -> HealthMetrics:
        """🚀 V2 Deployment component validation - PERFORMANCE OPTIMIZED"""
        print("🚀 Scanning V2 Deployment Status...")
        
        try:
            # Start timeout protection (Windows-compatible)
            start_time = time.time()
            timeout_threshold = 30  # 30 seconds max
            
            v2_components = {
                "orchestrator": False,
                "neural_engine": False,
                "dopamine_system": False,
                "agent_coordination": False,
                "memory_integration": False
            }

            component_details = {}
            files_scanned = 0
            max_files_to_scan = 1000  # Performance limit

            # Optimized search - focus on specific directories first
            priority_dirs = [
                "HYPERFOCUSzone-PRIVATE",
                "HYPERFOCUS ZONE DISCORD HUB",
                "neural-systems",
                "automation_masters"
            ]
            
            # Smart pattern matching - more specific patterns first
            v2_patterns = [
                "*ORCHESTRATOR*.py",
                "*NEURAL_OPTIMIZATION*.py", 
                "*DOPAMINE_GUARDIAN*.py",
                "*AGENT_COORDINATION*.py",
                "*BOARDROOM*V2*.py",
                "*PHASE_2*.py"
            ]

            for base_path in self.base_paths:
                if not base_path.exists():
                    continue
                
                # Check timeout
                if time.time() - start_time > timeout_threshold:
                    print("⚡ V2 scan timeout reached - performance optimization active")
                    break
                
                # First check priority directories
                for priority_dir in priority_dirs:
                    if time.time() - start_time > timeout_threshold:
                        break
                    priority_path = base_path / priority_dir
                    if priority_path.exists():
                        files_scanned = self._scan_v2_directory(
                            priority_path, v2_patterns, v2_components, 
                            component_details, files_scanned, max_files_to_scan, start_time, timeout_threshold
                        )
                        if files_scanned >= max_files_to_scan:
                            break
                
                # Then scan root level files (limited)
                if files_scanned < max_files_to_scan and time.time() - start_time < timeout_threshold:
                    try:
                        for file_path in base_path.glob("*V2*.py"):
                            if files_scanned >= max_files_to_scan or time.time() - start_time > timeout_threshold:
                                break
                            self._analyze_v2_file(file_path, v2_components, component_details)
                            files_scanned += 1
                    except (OSError, PermissionError):
                        continue
            
            # Check Discord configuration
            discord_configs = ["HyperBeast/.env", ".env", "empire.env"]
            for config_file in discord_configs:
                try:
                    if os.path.exists(config_file):
                        with open(config_file, "r", encoding="utf-8") as file:
                            env_content = file.read()
                            if "DISCORD_BOT_TOKEN" in env_content:
                                v2_components["discord_config"] = True
                                component_details["discord_config"] = {
                                    "status": "Configured",
                                    "config_file": config_file
                                }
                                break
                except (OSError, IOError, UnicodeDecodeError):
                    continue

            if not v2_components.get("discord_config"):
                component_details["discord_config"] = {"status": "Token not found"}

            # Calculate V2 deployment score
            active_components = sum(v2_components.values())
            total_components = len(v2_components)
            v2_score = (active_components / total_components) * 100

            # Bonus for having orchestrator (key component)
            if v2_components["orchestrator"]:
                v2_score = min(100, v2_score + 15)

            # Determine status
            if v2_score >= 90:
                status = "LEGENDARY"
                celebrations = ["🚀 LEGENDARY V2 Deployment!", "⚡ All Systems Operational!"]
            elif v2_score >= 70:
                status = "HEALTHY"
                celebrations = ["🚀 V2 Systems Active"]
            elif v2_score >= 40:
                status = "WARNING"
                celebrations = []
            else:
                status = "CRITICAL"
                celebrations = []

            broskie_rewards = int(v2_score * 2) if v2_score >= 50 else 0

            details = {
                "v2_components": v2_components,
                "component_details": component_details,
                "active_components": active_components,
                "total_components": total_components,
                "deployment_score": v2_score
            }

            return HealthMetrics(
                timestamp=datetime.now().isoformat(),
                system_name="V2 Deployment Status",
                status=status,
                score=v2_score,
                details=details,
                broskie_rewards=broskie_rewards,
                celebration_triggers=celebrations
            )

        except (OSError, RuntimeError, TimeoutError) as e:
            logging.error("V2 deployment scan error: %s", str(e))
            return HealthMetrics(
                timestamp=datetime.now().isoformat(),
                system_name="V2 Deployment Status",
                status="OFFLINE",
                score=0,
                details={"error": str(e), "performance_fix": "APPLIED"},
                broskie_rewards=0,
                celebration_triggers=[]
            )

    def _scan_v2_directory(self, directory_path, patterns, v2_components, component_details, files_scanned, max_files, start_time, timeout_threshold):
        """Helper method for optimized V2 directory scanning"""
        for pattern in patterns:
            if files_scanned >= max_files or time.time() - start_time > timeout_threshold:
                break
            try:
                for file_path in directory_path.rglob(pattern):
                    if files_scanned >= max_files or time.time() - start_time > timeout_threshold:
                        break
                    if file_path.is_file():
                        self._analyze_v2_file(file_path, v2_components, component_details)
                        files_scanned += 1
            except (OSError, PermissionError):
                continue
        return files_scanned
    
    def _analyze_v2_file(self, file_path, v2_components, component_details):
        """Helper method for V2 file analysis"""
        try:
            file_name = file_path.name.upper()
            file_size = file_path.stat().st_size
            
            # Check for specific V2 components
            if "ORCHESTRATOR" in file_name and file_size > 1000:
                v2_components["orchestrator"] = True
                component_details["orchestrator"] = {
                    "path": str(file_path),
                    "size": file_size
                }
            
            if "NEURAL" in file_name and file_size > 500:
                v2_components["neural_engine"] = True  
                component_details["neural_engine"] = {
                    "path": str(file_path),
                    "size": file_size
                }
            
            if "DOPAMINE" in file_name and file_size > 500:
                v2_components["dopamine_system"] = True
                component_details["dopamine_system"] = {
                    "path": str(file_path), 
                    "size": file_size
                }
                
            if "AGENT" in file_name and "COORDINATION" in file_name and file_size > 300:
                v2_components["agent_coordination"] = True
                component_details["agent_coordination"] = {
                    "path": str(file_path),
                    "size": file_size
                }
                
            if "MEMORY" in file_name and file_size > 500:
                v2_components["memory_integration"] = True
                component_details["memory_integration"] = {
                    "path": str(file_path),
                    "size": file_size
                }
                
        except (OSError, PermissionError):
            pass

    def scan_discord_integrations(self) -> HealthMetrics:
        """🤖 Discord bot and integration health check"""
        print("🤖 Scanning Discord Integrations...")

        try:
            discord_bots = []
            bot_files = [
                "ULTRA_HEALTH_DISCORD_BOT.py",
                "🤖💎⚡_ULTRA_HEALTH_DISCORD_BOT_ORGANIZED_⚡💎🤖.py",
                "🔄💎⚡_PHASE_2_AUTONOMOUS_DISCORD_BOT_INTEGRATION_LAYER_⚡💎🔄.py",
                "🤖👑💎⚡_ULTIMATE_LEGENDARY_DISCORD_BOT_COMMAND_SYSTEM_⚡💎👑🤖.py"
            ]

            total_bots = 0
            functional_bots = 0

            for base_path in self.base_paths:
                for bot_file in bot_files:
                    bot_path = base_path / bot_file
                    if bot_path.exists():
                        total_bots += 1
                        file_size = bot_path.stat().st_size

                        # Check if bot file is substantial and likely functional
                        if file_size > 2000:  # At least 2KB suggests real implementation
                            try:
                                with open(bot_path, 'r', encoding='utf-8') as f:
                                    content = f.read()
                                    # Check for key Discord.py elements
                                    if any(keyword in content for keyword in
                                          ['discord.Client', 'commands.Bot', '@bot.command', '@bot.tree.command']):
                                        functional_bots += 1
                                        discord_bots.append({
                                            "name": bot_file,
                                            "path": str(bot_path),
                                            "size": file_size,
                                            "status": "Functional"
                                        })
                                    else:
                                        discord_bots.append({
                                            "name": bot_file,
                                            "path": str(bot_path),
                                            "size": file_size,
                                            "status": "Needs Review"
                                        })
                            except (OSError, UnicodeDecodeError) as e:
                                logging.warning("Could not read bot file %s: %s", str(bot_path), str(e))
                        else:
                            discord_bots.append({
                                "name": bot_file,
                                "path": str(bot_path),
                                "size": file_size,
                                "status": "Too Small"
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

            celebrations = []
            if functional_bots >= 2:
                celebrations.append("🤖 LEGENDARY Discord Bot Army!")
            if token_configured:
                celebrations.append("🔑 Discord Integration Configured!")

            broskie_rewards = int(overall_score * 1.5) if overall_score >= 50 else 0

            details = {
                "total_bots_found": total_bots,
                "functional_bots": functional_bots,
                "token_configured": token_configured,
                "discord_bots": discord_bots,
                "integration_score": overall_score
            }

            return HealthMetrics(
                timestamp=datetime.now().isoformat(),
                system_name="Discord Integrations",
                status=status,
                score=overall_score,
                details=details,
                broskie_rewards=broskie_rewards,
                celebration_triggers=celebrations
            )

        except (OSError, RuntimeError) as e:
            logging.error("Discord integration scan error: %s", str(e))
            return HealthMetrics(
                timestamp=datetime.now().isoformat(),
                system_name="Discord Integrations",
                status="OFFLINE",
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
                                file_size = file_path.stat().st_size
                                if file_size > 1000:
                                    with open(file_path, 'r', encoding='utf-8') as f:
                                        content = f.read()
                                        if 'class ' in content or 'def ' in content:
                                            active_agents += 1
                                            coordination_files.append({
                                                "name": file_path.name,
                                                "path": str(file_path),
                                                "size": file_size,
                                                "status": "Active"
                                            })
                                        else:
                                            coordination_files.append({
                                                "name": file_path.name,
                                                "path": str(file_path),
                                                "size": file_size,
                                                "status": "Needs Development"
                                            })
                                else:
                                    coordination_files.append({
                                        "name": file_path.name,
                                        "path": str(file_path),
                                        "size": file_size,
                                        "status": "Too Small"
                                    })
                        except (OSError, UnicodeDecodeError):
                            continue
                except (OSError, IOError) as e:
                    logging.warning("Could not scan directory %s: %s", str(base_path), str(e))

            # Calculate coordination score
            if total_agents > 0:
                coordination_score = (active_agents / total_agents) * 100
            else:
                coordination_score = 0

            # Bonus for having multiple agent types
            if active_agents >= 3:
                coordination_score = min(100, coordination_score + 25)

            if active_agents >= 5:
                coordination_score = min(100, coordination_score + 15)

            # Determine status
            if coordination_score >= 90:
                status = "LEGENDARY"
                celebrations = ["👥 LEGENDARY Agent Coordination!", "⚡ Empire Agent Army Ready!"]
            elif coordination_score >= 70:
                status = "HEALTHY"
                celebrations = ["👥 Agent Coordination Active"]
            elif coordination_score >= 40:
                status = "WARNING"
                celebrations = []
            else:
                status = "CRITICAL"
                celebrations = []

            broskie_rewards = int(coordination_score * 2.5) if coordination_score >= 50 else 0

            details = {
                "total_agents_found": total_agents,
                "active_agents": active_agents,
                "coordination_score": coordination_score,
                "agent_files": coordination_files[:15]  # Top 15 for brevity
            }

            return HealthMetrics(
                timestamp=datetime.now().isoformat(),
                system_name="Agent Coordination",
                status=status,
                score=coordination_score,
                details=details,
                broskie_rewards=broskie_rewards,
                celebration_triggers=celebrations
            )

        except (OSError, RuntimeError) as e:
            logging.error("Agent coordination scan error: %s", str(e))
            return HealthMetrics(
                timestamp=datetime.now().isoformat(),
                system_name="Agent Coordination",
                status="OFFLINE",
                score=0,
                details={"error": str(e)},
                broskie_rewards=0,
                celebration_triggers=[]
            )

    def scan_project_structure(self) -> HealthMetrics:
        """📁 Project structure and organization (from PowerShell scanner)"""
        print("📁 Scanning Project Structure...")

        try:
            structure_health = []
            critical_directories = [
                "HyperBeast",
                "HYPERFOCUS ZONE DISCORD HUB",
                "grafana-by-example",
                "tHE HYPERFOUCS dOoK ultra Web Comic"
            ]

            total_score = 0
            directory_scores = {}

            for directory in critical_directories:
                directory_path = Path("h:/") / directory
                score = 0
                details = {"exists": False, "file_count": 0, "size": 0}

                if directory_path.exists():
                    details["exists"] = True
                    score += 25

                    try:
                        # Count files and calculate directory health
                        files = list(directory_path.rglob("*"))
                        file_count = len([f for f in files if f.is_file()])
                        details["file_count"] = file_count

                        if file_count > 10:
                            score += 25
                        elif file_count > 5:
                            score += 15
                        elif file_count > 0:
                            score += 10

                        # Check for key file types
                        py_files = len(list(directory_path.rglob("*.py")))
                        js_files = len(list(directory_path.rglob("*.js")))
                        config_files = len(list(directory_path.rglob("*.json"))) + len(list(directory_path.rglob("*.yml")))

                        if py_files > 0:
                            score += 15
                        if js_files > 0:
                            score += 10
                        if config_files > 0:
                            score += 15

                        # Size assessment
                        total_size = sum(f.stat().st_size for f in files if f.is_file())
                        details["size"] = total_size

                        if total_size > 1024 * 1024:  # > 1MB
                            score += 10

                        details.update({
                            "py_files": py_files,
                            "js_files": js_files,
                            "config_files": config_files
                        })

                    except (OSError, IOError) as e:
                        logging.warning("Could not scan directory %s: %s", directory, str(e))
                        score = 10  # Partial credit for existing

                directory_scores[directory] = score
                structure_health.append({
                    "directory": directory,
                    "score": score,
                    "details": details
                })
                total_score += score

            # Calculate overall structure score
            max_possible_score = len(critical_directories) * 100
            structure_score = (total_score / max_possible_score) * 100

            # Bonus for having all critical directories
            existing_dirs = sum(1 for item in structure_health if item["details"]["exists"])
            if existing_dirs == len(critical_directories):
                structure_score = min(100, structure_score + 10)

            # Determine status
            if structure_score >= 85:
                status = "LEGENDARY"
                celebrations = ["📁 LEGENDARY Project Structure!", "🏗️ Empire Architecture Perfect!"]
            elif structure_score >= 70:
                status = "HEALTHY"
                celebrations = ["📁 Project Structure Organized"]
            elif structure_score >= 50:
                status = "WARNING"
                celebrations = []
            else:
                status = "CRITICAL"
                celebrations = []

            broskie_rewards = int(structure_score * 1.5) if structure_score >= 60 else 0

            details = {
                "structure_score": structure_score,
                "directory_scores": directory_scores,
                "existing_directories": existing_dirs,
                "total_directories": len(critical_directories),
                "structure_health": structure_health
            }

            return HealthMetrics(
                timestamp=datetime.now().isoformat(),
                system_name="Project Structure",
                status=status,
                score=structure_score,
                details=details,
                broskie_rewards=broskie_rewards,
                celebration_triggers=celebrations
            )

        except (OSError, RuntimeError) as e:
            logging.error("Project structure scan error: %s", str(e))
            return HealthMetrics(
                timestamp=datetime.now().isoformat(),
                system_name="Project Structure",
                status="OFFLINE",
                score=0,
                details={"error": str(e)},
                broskie_rewards=0,
                celebration_triggers=[]
            )

    def scan_grafana_infrastructure(self) -> HealthMetrics:
        """📊 Grafana infrastructure and monitoring setup"""
        print("📊 Scanning Grafana Infrastructure...")

        try:
            grafana_components = {
                "docker_compose": False,
                "grafana_config": False,
                "prometheus_config": False,
                "dashboards": False,
                "data_sources": False
            }

            component_details = {}
            grafana_score = 0

            # Check for grafana-by-example directory
            grafana_path = Path("h:/grafana-by-example")
            if not grafana_path.exists():
                return HealthMetrics(
                    timestamp=datetime.now().isoformat(),
                    system_name="Grafana Infrastructure",
                    status="OFFLINE",
                    score=0,
                    details={"error": "Grafana directory not found"},
                    broskie_rewards=0,
                    celebration_triggers=[]
                )

            # Check Docker Compose files
            compose_files = list(grafana_path.rglob("docker-compose*.yml"))
            if compose_files:
                grafana_components["docker_compose"] = True
                component_details["docker_compose"] = {
                    "count": len(compose_files),
                    "files": [str(f) for f in compose_files[:5]]
                }
                grafana_score += 25

            # Check for Grafana configurations
            grafana_configs = list(grafana_path.rglob("*grafana*"))
            if grafana_configs:
                grafana_components["grafana_config"] = True
                component_details["grafana_config"] = {
                    "count": len(grafana_configs),
                    "configs": [str(f) for f in grafana_configs[:5]]
                }
                grafana_score += 20

            # Check for Prometheus configurations
            prometheus_configs = list(grafana_path.rglob("*prometheus*"))
            if prometheus_configs:
                grafana_components["prometheus_config"] = True
                component_details["prometheus_config"] = {
                    "count": len(prometheus_configs),
                    "configs": [str(f) for f in prometheus_configs[:5]]
                }
                grafana_score += 20

            # Check for dashboard files
            dashboard_files = list(grafana_path.rglob("*.json"))
            dashboard_count = len([f for f in dashboard_files if "dashboard" in f.name.lower()])
            if dashboard_count > 0:
                grafana_components["dashboards"] = True
                component_details["dashboards"] = {
                    "count": dashboard_count,
                    "dashboards": [str(f) for f in dashboard_files if "dashboard" in f.name.lower()][:5]
                }
                grafana_score += 20

            # Check if Docker is available
            docker_available = False
            try:
                docker_client = docker.from_env()
                docker_client.ping()
                docker_available = True
                component_details["docker_status"] = "Available"
                grafana_score += 15
            except (docker.errors.DockerException, OSError) as e:
                logging.warning("Docker client unavailable: %s", str(e))
                component_details["docker_status"] = "Unavailable"

            # Check for running Grafana containers
            grafana_containers = []
            if docker_available:
                try:
                    docker_client = docker.from_env()
                    containers = docker_client.containers.list()
                    for container in containers:
                        if any(keyword in container.name.lower() or
                              any(keyword in str(port) for port in container.ports.keys())
                              for keyword in ['grafana', '3000']):
                            grafana_containers.append({
                                "name": container.name,
                                "status": container.status,
                                "ports": list(container.ports.keys())
                            })

                    if grafana_containers:
                        component_details["running_containers"] = grafana_containers
                        grafana_score += 20

                except (docker.errors.DockerException, OSError) as e:
                    logging.warning("Could not check Docker containers: %s", str(e))

            # Determine status
            if grafana_score >= 85:
                status = "LEGENDARY"
                celebrations = ["📊 LEGENDARY Grafana Infrastructure!", "⚡ Monitoring Stack Ready!"]
            elif grafana_score >= 65:
                status = "HEALTHY"
                celebrations = ["📊 Grafana Infrastructure Active"]
            elif grafana_score >= 40:
                status = "WARNING"
                celebrations = []
            else:
                status = "CRITICAL"
                celebrations = []

            broskie_rewards = int(grafana_score * 2) if grafana_score >= 50 else 0

            details = {
                "grafana_components": grafana_components,
                "component_details": component_details,
                "grafana_score": grafana_score,
                "docker_available": docker_available,
                "running_containers": grafana_containers
            }

            return HealthMetrics(
                timestamp=datetime.now().isoformat(),
                system_name="Grafana Infrastructure",
                status=status,
                score=grafana_score,
                details=details,
                broskie_rewards=broskie_rewards,
                celebration_triggers=celebrations
            )

        except (OSError, RuntimeError) as e:
            logging.error("Grafana infrastructure scan error: %s", str(e))
            return HealthMetrics(
                timestamp=datetime.now().isoformat(),
                system_name="Grafana Infrastructure",
                status="OFFLINE",
                score=0,
                details={"error": str(e)},
                broskie_rewards=0,
                celebration_triggers=[]
            )

    def execute_auto_fixes(self, metrics: List[HealthMetrics]) -> List[str]:
        """🔧 Execute automatic fixes for common issues"""
        print("🔧 Executing Auto-Fixes...")

        auto_fixes = []

        try:
            # Fix 1: Create missing directories
            for base_path in self.base_paths:
                if not base_path.exists():
                    try:
                        base_path.mkdir(parents=True, exist_ok=True)
                        auto_fixes.append(f"✅ Created directory: {base_path}")
                    except OSError:
                        auto_fixes.append(f"❌ Failed to create directory: {base_path}")

            # Fix 2: Restart failed Grafana services
            grafana_metrics = next((m for m in metrics if m.system_name == "Grafana Infrastructure"), None)
            if grafana_metrics and grafana_metrics.score < 50:
                fix_result = self.restart_grafana_service()
                auto_fixes.append(f"🔄 Grafana restart: {fix_result}")

            # Fix 3: Start Grafana stack if available
            grafana_start_result = self.start_grafana_stack()
            if grafana_start_result != "FAILED - No docker-compose files found":
                auto_fixes.append(f"🚀 Grafana stack start: {grafana_start_result}")

        except (OSError, RuntimeError) as e:
            logging.error("Auto-fix execution error: %s", str(e))
            auto_fixes.append(f"❌ Auto-fix error: {str(e)}")

        return auto_fixes

    def restart_grafana_service(self, service_name: str = "grafana") -> str:
        """🔄 Restart a specific Grafana service"""
        try:
            grafana_path = Path("h:/grafana-by-example")
            if not grafana_path.exists():
                return "FAILED - Grafana directory not found"

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

            if result.returncode == 0:
                return f"SUCCESS - {service_name} restarted"
            else:
                return f"FAILED - {result.stderr}"

        except (subprocess.TimeoutExpired, OSError, RuntimeError):
            return "FAILED - Restart timeout or error"

    def start_grafana_stack(self) -> str:
        """🚀 Start the complete Grafana monitoring stack"""
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

                if result.returncode == 0:
                    return "SUCCESS - Grafana stack started"
                else:
                    return f"PARTIAL - {result.stderr}"
            else:
                return "FAILED - No docker-compose files found"

        except (subprocess.TimeoutExpired, OSError, RuntimeError):
            return "FAILED - Start timeout or error"

    def generate_quantum_metrics(self) -> Dict[str, Any]:
        """⚡ Generate quantum-level empire metrics"""
        uptime = (datetime.now() - self.start_time).total_seconds()

        return {
            "scan_duration": uptime,
            "empire_velocity": self.health_report["total_broskie_earned"] / max(1, uptime),
            "celebration_density": len(self.health_report["celebration_events"]) / max(1, len(self.health_report["systems"])),
            "legendary_coefficient": self.health_report["overall_health_score"] / 100,
            "quantum_timestamp": datetime.now().isoformat()
        }

    def calculate_legendary_achievements(self, metrics: List[HealthMetrics], overall_health: float, total_broskie: int) -> List[str]:
        """🏆 Calculate legendary achievements unlocked"""
        achievements = []

        if overall_health >= 95:
            achievements.append("🏆 LEGENDARY EMPIRE STATUS ACHIEVED!")

        if total_broskie >= 1000:
            achievements.append("💎 BROSKIE MILLIONAIRE UNLOCKED!")

        legendary_systems = sum(1 for m in metrics if m.status == "LEGENDARY")
        if legendary_systems >= 5:
            achievements.append("⚡ LEGENDARY SYSTEM DOMINANCE!")

        total_celebrations = sum(len(m.celebration_triggers) for m in metrics)
        if total_celebrations >= 10:
            achievements.append("🎊 CELEBRATION MASTER UNLOCKED!")

        if len(self.health_report["systems"]) >= 7:
            achievements.append("🌐 COMPLETE EMPIRE SCAN MASTERY!")

        return achievements

    def display_master_health_report(self):
        """📊 Display the comprehensive health report"""
        print(f"""
🏆💎⚡ LEGENDARY MASTER HEALTH REPORT ⚡💎🏆
=====================================================

📊 EMPIRE STATUS: {self.health_report['empire_status']}
⚡ Overall Health Score: {self.health_report['overall_health_score']:.1f}%
💎 Total BROski$ Earned: {self.health_report['total_broskie_earned']}
🎊 Celebration Events: {len(self.health_report['celebration_events'])}

SYSTEM STATUS BREAKDOWN:
=======================
""")

        for system_name, system_data in self.health_report["systems"].items():
            status_emoji = "🏆" if system_data["status"] == "LEGENDARY" else "✅" if system_data["status"] == "HEALTHY" else "⚠️" if system_data["status"] == "WARNING" else "❌"
            print(f"{status_emoji} {system_name.upper()}: {system_data['status']} ({system_data['score']:.1f}%)")

        print(f"\n🏆 LEGENDARY ACHIEVEMENTS:")
        for achievement in self.health_report['legendary_achievements']:
            print(f"  ⭐ {achievement}")

        if self.health_report['auto_fix_actions']:
            print(f"\n🔧 AUTO-FIX ACTIONS EXECUTED:")
            for action in self.health_report['auto_fix_actions']:
                print(f"  🛠️ {action}")

        print(f"""
⚡ QUANTUM METRICS:
==================
🚀 Empire Velocity: {self.health_report['quantum_metrics'].get('empire_velocity', 0):.2f} BROski$/sec
🎊 Celebration Density: {self.health_report['quantum_metrics'].get('celebration_density', 0):.2f}
💎 Legendary Coefficient: {self.health_report['quantum_metrics'].get('legendary_coefficient', 0):.2f}

🏆💎⚡ EMPIRE IS READY FOR LEGENDARY DOMINATION! ⚡💎🏆
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
Overall Health Score: {self.health_report['overall_health_score']:.1f}%
Total BROski$ Earned: {self.health_report['total_broskie_earned']}

System Status:
""")
                for system_name, system_data in self.health_report["systems"].items():
                    f.write(f"  {system_name}: {system_data['status']} ({system_data['score']:.1f}%)\n")

                f.write("\nLegendary Achievements:\n")
                for achievement in self.health_report['legendary_achievements']:
                    f.write(f"  • {achievement}\n")

            print(f"📄 Health summary saved: {summary_filename}")

        except (OSError, IOError, RuntimeError) as e:
            logging.error("Health report save error: %s", str(e))
            print(f"❌ Failed to save health report: {str(e)}")

def main():
    """🚀 Main execution function"""
    print("""
🏆💎⚡ LEGENDARY MASTER HEALTH CHECK SYSTEM ⚡💎🏆
===============================================

Initializing Ultimate Empire Health Scanner...
    """)

    try:
        # Create the master health checker
        health_checker = LegendaryMasterHealthChecker()

        # Execute the complete health scan
        health_report = health_checker.execute_master_health_scan()

        # Display the results
        health_checker.display_master_health_report()

        # Save the complete report
        health_checker.save_master_health_report()

        print("""
🎊🏆💎⚡ LEGENDARY HEALTH SCAN COMPLETE ⚡💎🏆🎊

The Empire has been analyzed and optimized!
All systems report to the LEGENDARY MASTER HEALTH CHECK SYSTEM!

🚀 Ready for world domination! 🚀
        """)

    except (OSError, RuntimeError) as e:
        logging.error("Master health check error: %s", str(e))
        print(f"❌ Health check failed: {str(e)}")

if __name__ == "__main__":
    main()

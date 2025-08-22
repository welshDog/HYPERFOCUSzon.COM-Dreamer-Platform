#!/usr/bin/env python3
"""
🧠💎 HyperFocus Zone Memory Management System
Track, remember, and optimize everything we build!
"""

import json
import os
import subprocess
from datetime import datetime
from typing import Any, Dict, List


class HyperFocusMemorySystem:
    """
    🧠 Perfect memory system for tracking all our work, environments, and progress.
    Never forget what we built or where we put it!
    """

    def __init__(self, memory_file: str = "hyperfocus_memory.json"):
        self.memory_file = memory_file
        self.memory_data = self.load_memory()

    def load_memory(self) -> Dict[str, Any]:
        """Load our persistent memory from file."""
        if os.path.exists(self.memory_file):
            with open(self.memory_file, "r") as f:
                return json.load(f)
        return {
            "projects": {},
            "environments": {},
            "docker_images": {},
            "achievements": [],
            "performance_baselines": {},
            "quick_access": {},
            "session_history": [],
        }

    def save_memory(self):
        """Save our memory to persistent storage."""
        with open(self.memory_file, "w") as f:
            json.dump(self.memory_data, f, indent=2)
        print(f"💾 Memory saved to {self.memory_file}")

    def remember_project(
        self,
        name: str,
        description: str,
        docker_image: str = None,
        files: List[str] = None,
        status: str = "active",
    ):
        """Remember a project and all its details."""
        project_data = {
            "name": name,
            "description": description,
            "created": datetime.now().isoformat(),
            "status": status,
            "docker_image": docker_image,
            "files": files or [],
            "last_accessed": datetime.now().isoformat(),
        }

        self.memory_data["projects"][name] = project_data
        self.log_achievement(f"🚀 Remembered project: {name}")
        self.save_memory()

    def remember_docker_image(
        self, image_name: str, description: str, build_command: str, run_command: str
    ):
        """Remember Docker images and how to use them."""
        image_data = {
            "name": image_name,
            "description": description,
            "build_command": build_command,
            "run_command": run_command,
            "created": datetime.now().isoformat(),
            "size": self.get_docker_image_size(image_name),
        }

        self.memory_data["docker_images"][image_name] = image_data
        self.log_achievement(f"🐳 Remembered Docker image: {image_name}")
        self.save_memory()

    def get_docker_image_size(self, image_name: str) -> str:
        """Get Docker image size."""
        try:
            result = subprocess.run(
                ["docker", "images", image_name, "--format", "table {{.Size}}"],
                capture_output=True,
                text=True,
            )
            if result.returncode == 0:
                lines = result.stdout.strip().split("\n")
                return lines[1] if len(lines) > 1 else "Unknown"
        except:
            pass
        return "Unknown"

    def quick_access(self, name: str, command: str, description: str = ""):
        """Create quick access commands for instant recall."""
        self.memory_data["quick_access"][name] = {
            "command": command,
            "description": description,
            "created": datetime.now().isoformat(),
            "usage_count": 0,
        }
        self.save_memory()
        print(f"⚡ Quick access '{name}' created: {command}")

    def use_quick_access(self, name: str) -> str:
        """Use a quick access command and track usage."""
        if name in self.memory_data["quick_access"]:
            command = self.memory_data["quick_access"][name]["command"]
            self.memory_data["quick_access"][name]["usage_count"] += 1
            self.memory_data["quick_access"][name][
                "last_used"
            ] = datetime.now().isoformat()
            self.save_memory()
            return command
        return None

    def log_achievement(self, achievement: str):
        """Log achievements and milestones."""
        achievement_data = {
            "achievement": achievement,
            "timestamp": datetime.now().isoformat(),
            "session": len(self.memory_data["session_history"]),
        }
        self.memory_data["achievements"].append(achievement_data)

    def show_memory_status(self):
        """Show current memory system status."""
        print("\n🧠💎 HyperFocus Zone Memory System Status")
        print("=" * 50)
        print(f"📁 Projects remembered: {len(self.memory_data['projects'])}")
        print(f"🐳 Docker images: {len(self.memory_data['docker_images'])}")
        print(f"⚡ Quick access commands: {len(self.memory_data['quick_access'])}")
        print(f"🏆 Achievements logged: {len(self.memory_data['achievements'])}")
        print(
            f"📊 Performance baselines: {len(self.memory_data['performance_baselines'])}"
        )

        print("\n🚀 Recent Achievements:")
        for achievement in self.memory_data["achievements"][-5:]:
            print(f"  • {achievement['achievement']} ({achievement['timestamp'][:19]})")

        print("\n⚡ Most Used Quick Access:")
        quick_sorted = sorted(
            self.memory_data["quick_access"].items(),
            key=lambda x: x[1].get("usage_count", 0),
            reverse=True,
        )[:3]
        for name, data in quick_sorted:
            print(
                f"  • {name}: {data['command']} (used {data.get('usage_count', 0)} times)"
            )

    def backup_memory(self, backup_file: str = None):
        """Create a backup of our memory system."""
        if not backup_file:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_file = f"hyperfocus_memory_backup_{timestamp}.json"

        with open(backup_file, "w") as f:
            json.dump(self.memory_data, f, indent=2)
        print(f"💾 Memory backed up to {backup_file}")


def main():
    """Initialize and demonstrate the memory system."""
    memory = HyperFocusMemorySystem()

    # Remember our current Docker setup
    memory.remember_project(
        name="HyperFocus System Monitor Docker",
        description="Complete containerized system monitoring with Docker compose stack",
        docker_image="hyperfocus-monitor-simple",
        files=[
            "system_monitor.py",
            "docker_demo.py",
            "Dockerfile",
            "docker-compose.yml",
            "docker_entrypoint.sh",
        ],
        status="completed",
    )

    memory.remember_docker_image(
        image_name="hyperfocus-monitor-simple",
        description="Lightweight system monitor with real-time metrics",
        build_command="docker build -t hyperfocus-monitor-simple -f Dockerfile.simple .",
        run_command="docker run --rm hyperfocus-monitor-simple",
    )

    # Create quick access commands
    memory.quick_access(
        "monitor",
        "docker run --rm hyperfocus-monitor-simple",
        "Run system monitor demo",
    )
    memory.quick_access("stack", "docker-compose up -d", "Start full monitoring stack")
    memory.quick_access(
        "logs", "docker-compose logs -f system-monitor", "View monitoring logs"
    )
    memory.quick_access("stop", "docker-compose down", "Stop all services")

    # Show current status
    memory.show_memory_status()

    # Create backup
    memory.backup_memory()

    print(f"\n✅ Memory system initialized! File: {memory.memory_file}")
    print("🧠 Now you'll never forget what you built or where it is!")


if __name__ == "__main__":
    main()

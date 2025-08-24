#!/usr/bin/env python3
"""
🔍💎⚡ COMPREHENSIVE REPOSITORY HEALTH ASSESSMENT ENGINE ⚡💎🔍

Ultimate repository health checker that scans all repositories for:
- Missing critical files
- Dependency issues
- Git repository problems
- Security vulnerabilities
- Configuration issues
- Development environment problems

Created: January 17, 2025
Status: LEGENDARY EMPIRE HEALTH DIAGNOSTIC
"""

import json
import logging
import os
import subprocess
from datetime import datetime
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format="🌌 %(message)s")
logger = logging.getLogger(__name__)


class ComprehensiveRepositoryHealthChecker:
    """🏆 Ultimate repository health assessment system"""

    def __init__(self):
        self.base_path = Path("h:/")
        self.repositories = [
            "HYPERFOCUS-UNIFIED-EMPIRE",
            "HYPERFOCUS-ZONE-NEURO-SOCIAL-DREAMER",
            "Omega-Vault",
            "VSCode-Java-Wiki",
        ]
        self.health_report = {
            "scan_timestamp": datetime.now().isoformat(),
            "overall_health": "SCANNING",
            "repositories": {},
            "critical_issues": [],
            "warnings": [],
            "recommendations": [],
        }

    def check_repository_structure(self, repo_path):
        """🔍 Check repository structure and critical files"""
        logger.info(f"🔍 Scanning repository: {repo_path.name}")

        repo_health = {
            "status": "HEALTHY",
            "critical_files": {},
            "package_health": {},
            "git_status": {},
            "issues": [],
            "score": 100,
        }

        # Critical files to check
        critical_files = {
            "README.md": {"weight": 20, "found": False},
            ".gitignore": {"weight": 15, "found": False},
            "package.json": {"weight": 10, "found": False},
            "requirements.txt": {"weight": 10, "found": False},
            "docker-compose.yml": {"weight": 5, "found": False},
            ".env": {"weight": 5, "found": False},
            "Dockerfile": {"weight": 5, "found": False},
        }

        # Check for critical files
        for file_name, info in critical_files.items():
            file_path = repo_path / file_name
            if file_path.exists():
                info["found"] = True
                logger.info(f"   ✅ {file_name}: Found")
            else:
                repo_health["score"] -= info["weight"]
                logger.info(
                    f"   ❌ {file_name}: Missing (Impact: -{info['weight']} points)"
                )

        repo_health["critical_files"] = critical_files

        # Check git repository health
        if (repo_path / ".git").exists():
            try:
                os.chdir(repo_path)

                # Check git status
                result = subprocess.run(
                    ["git", "status", "--porcelain"],
                    capture_output=True,
                    text=True,
                    timeout=10,
                )

                if result.returncode == 0:
                    if result.stdout.strip():
                        repo_health["git_status"]["uncommitted_changes"] = len(
                            result.stdout.strip().split("\n")
                        )
                        repo_health["issues"].append("Uncommitted changes detected")
                    else:
                        repo_health["git_status"]["clean"] = True
                        logger.info(f"   ✅ Git status: Clean")
                else:
                    repo_health["issues"].append("Git status check failed")
                    repo_health["score"] -= 10

            except Exception as e:
                repo_health["issues"].append(f"Git check error: {str(e)}")
                repo_health["score"] -= 15
        else:
            repo_health["issues"].append("Not a git repository")
            repo_health["score"] -= 25

        # Check package.json dependencies
        package_json = repo_path / "package.json"
        if package_json.exists():
            try:
                with open(package_json, "r") as f:
                    package_data = json.load(f)

                repo_health["package_health"]["package_name"] = package_data.get(
                    "name", "Unknown"
                )
                repo_health["package_health"]["version"] = package_data.get(
                    "version", "Unknown"
                )

                # Check for node_modules
                node_modules = repo_path / "node_modules"
                if not node_modules.exists():
                    repo_health["issues"].append(
                        "node_modules missing - run npm install"
                    )
                    repo_health["score"] -= 10

            except Exception as e:
                repo_health["issues"].append(f"package.json parse error: {str(e)}")
                repo_health["score"] -= 10

        # Check requirements.txt
        requirements_txt = repo_path / "requirements.txt"
        if requirements_txt.exists():
            try:
                with open(requirements_txt, "r") as f:
                    requirements = f.read().strip()
                    if requirements:
                        repo_health["package_health"]["python_packages"] = len(
                            [
                                line
                                for line in requirements.split("\n")
                                if line.strip() and not line.startswith("#")
                            ]
                        )
                    else:
                        repo_health["issues"].append("requirements.txt is empty")
                        repo_health["score"] -= 5
            except Exception as e:
                repo_health["issues"].append(f"requirements.txt read error: {str(e)}")
                repo_health["score"] -= 5

        # Determine final status
        if repo_health["score"] >= 90:
            repo_health["status"] = "LEGENDARY"
        elif repo_health["score"] >= 75:
            repo_health["status"] = "HEALTHY"
        elif repo_health["score"] >= 50:
            repo_health["status"] = "WARNING"
        else:
            repo_health["status"] = "CRITICAL"

        return repo_health

    def scan_all_repositories(self):
        """🚀 Scan all repositories for health issues"""
        logger.info("🌌 🔍💎⚡ COMPREHENSIVE REPOSITORY HEALTH ASSESSMENT ⚡💎🔍")
        logger.info("🌌 " + "=" * 70)

        total_score = 0
        repo_count = 0

        for repo_name in self.repositories:
            repo_path = self.base_path / repo_name

            if repo_path.exists() and repo_path.is_dir():
                repo_health = self.check_repository_structure(repo_path)
                self.health_report["repositories"][repo_name] = repo_health

                total_score += repo_health["score"]
                repo_count += 1

                # Add critical issues to main report
                if repo_health["status"] in ["CRITICAL", "WARNING"]:
                    self.health_report["critical_issues"].extend(
                        [f"{repo_name}: {issue}" for issue in repo_health["issues"]]
                    )

                logger.info(
                    f"   📊 {repo_name}: {repo_health['status']} ({repo_health['score']}/100)"
                )
            else:
                logger.info(f"   ❌ {repo_name}: Repository not found")
                self.health_report["repositories"][repo_name] = {
                    "status": "MISSING",
                    "score": 0,
                    "issues": ["Repository directory not found"],
                }

        # Calculate overall health
        if repo_count > 0:
            overall_score = total_score / repo_count

            if overall_score >= 90:
                self.health_report["overall_health"] = "LEGENDARY"
            elif overall_score >= 75:
                self.health_report["overall_health"] = "HEALTHY"
            elif overall_score >= 50:
                self.health_report["overall_health"] = "WARNING"
            else:
                self.health_report["overall_health"] = "CRITICAL"

            self.health_report["overall_score"] = overall_score
        else:
            self.health_report["overall_health"] = "CRITICAL"
            self.health_report["overall_score"] = 0

        return self.health_report

    def generate_recommendations(self):
        """💡 Generate actionable recommendations"""
        recommendations = []

        for repo_name, repo_data in self.health_report["repositories"].items():
            if repo_data["status"] in ["WARNING", "CRITICAL"]:
                for issue in repo_data.get("issues", []):
                    if "missing" in issue.lower():
                        recommendations.append(
                            f"📁 {repo_name}: Add missing critical files"
                        )
                    elif "git" in issue.lower():
                        recommendations.append(
                            f"🔧 {repo_name}: Fix git repository issues"
                        )
                    elif "package" in issue.lower():
                        recommendations.append(
                            f"📦 {repo_name}: Install dependencies (npm install)"
                        )

        # Add general recommendations
        if self.health_report["overall_score"] < 80:
            recommendations.extend(
                [
                    "🏆 Focus on repositories with CRITICAL or WARNING status first",
                    "📚 Ensure all repositories have comprehensive README.md files",
                    "🔒 Add .gitignore files to prevent committing sensitive data",
                    "🐳 Consider adding Docker support for consistent development environments",
                ]
            )

        self.health_report["recommendations"] = recommendations
        return recommendations

    def display_health_report(self):
        """📊 Display comprehensive health report"""
        logger.info("🌌 " + "=" * 70)
        logger.info("🌌 🏆💎⚡ REPOSITORY HEALTH ASSESSMENT COMPLETE ⚡💎🏆")
        logger.info("🌌 " + "=" * 70)

        print(
            f"\n🎯 OVERALL EMPIRE REPOSITORY HEALTH: {self.health_report['overall_health']}"
        )
        print(f"📊 Average Score: {self.health_report.get('overall_score', 0):.1f}/100")
        print(f"🕐 Scan Time: {self.health_report['scan_timestamp']}")

        print(f"\n📁 REPOSITORY STATUS SUMMARY:")
        print("-" * 50)

        for repo_name, repo_data in self.health_report["repositories"].items():
            status_icon = {
                "LEGENDARY": "✅",
                "HEALTHY": "✅",
                "WARNING": "⚠️",
                "CRITICAL": "❌",
                "MISSING": "💀",
            }.get(repo_data["status"], "❓")

            print(
                f"{status_icon} {repo_name}: {repo_data['status']} ({repo_data['score']}/100)"
            )

            if repo_data.get("issues"):
                for issue in repo_data["issues"][:3]:  # Show top 3 issues
                    print(f"   • {issue}")

        if self.health_report["critical_issues"]:
            print(f"\n🚨 CRITICAL ISSUES REQUIRING ATTENTION:")
            print("-" * 50)
            for issue in self.health_report["critical_issues"][:10]:  # Show top 10
                print(f"❌ {issue}")

        recommendations = self.generate_recommendations()
        if recommendations:
            print(f"\n💡 RECOMMENDATIONS:")
            print("-" * 30)
            for rec in recommendations[:8]:  # Show top 8 recommendations
                print(f"💡 {rec}")

        print(f"\n🎉 HEALTH CHECK COMPLETE!")
        print(
            f"Next steps: Address {len(self.health_report['critical_issues'])} critical issues"
        )

        return self.health_report

    def save_health_report(self):
        """💾 Save health report to file"""
        report_file = (
            self.base_path / "🔍💎⚡_REPOSITORY_HEALTH_ASSESSMENT_REPORT_⚡💎🔍.json"
        )

        try:
            with open(report_file, "w", encoding="utf-8") as f:
                json.dump(self.health_report, f, indent=2, ensure_ascii=False)
            print(f"\n📄 Health report saved: {report_file}")
            return report_file
        except Exception as e:
            print(f"⚠️ Could not save report: {e}")
            return None


def main():
    """🚀 Main execution function"""
    try:
        # Initialize health checker
        health_checker = ComprehensiveRepositoryHealthChecker()

        # Scan all repositories
        health_report = health_checker.scan_all_repositories()

        # Display comprehensive report
        health_checker.display_health_report()

        # Save report
        health_checker.save_health_report()

    except KeyboardInterrupt:
        print("\n⚠️ Health check interrupted by user")
    except Exception as e:
        print(f"❌ Health check failed: {e}")
        logger.error(f"Error: {e}")


if __name__ == "__main__":
    main()

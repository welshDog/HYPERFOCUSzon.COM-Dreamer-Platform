#!/usr/bin/env python3
"""
🔍💎⚡ ULTRA-THINKING BOARDROOM FILE ANALYSIS & CLEANUP SYSTEM ⚡💎🔍
=================================================================
Comprehensive file scanning, usage analysis, and cleanup recommendations
Following LOOK-THEN-BUILD protocol for complete project organization
=================================================================
"""

import os
import json
import datetime
import re
from pathlib import Path
from typing import Dict, List, Set, Tuple
import subprocess

class UltraBoardroomFileAnalyzer:
    def __init__(self):
        self.base_path = Path("h:/")
        self.file_categories = {
            "active_systems": [],
            "monitoring_tools": [],
            "celebration_systems": [],
            "dns_infrastructure": [],
            "empire_management": [],
            "deprecated_files": [],
            "duplicate_candidates": [],
            "unused_files": [],
            "core_operational": []
        }
        self.usage_patterns = {}
        self.file_relationships = {}

    def scan_all_files(self) -> Dict:
        """🔍 Comprehensive scan of all files in the workspace"""
        print("🔍 ULTRA-THINKING BOARDROOM: Scanning all workspace files...")

        all_files = []
        file_stats = {
            "total_files": 0,
            "python_files": 0,
            "json_files": 0,
            "markdown_files": 0,
            "powershell_files": 0,
            "html_files": 0,
            "text_files": 0,
            "other_files": 0,
            "directories": 0
        }

        # Scan all files recursively
        for root, dirs, files in os.walk(self.base_path):
            file_stats["directories"] += len(dirs)

            for file in files:
                file_path = Path(root) / file
                try:
                    file_info = {
                        "path": str(file_path),
                        "name": file,
                        "extension": file_path.suffix.lower(),
                        "size": file_path.stat().st_size,
                        "modified": datetime.datetime.fromtimestamp(file_path.stat().st_mtime).isoformat(),
                        "created": datetime.datetime.fromtimestamp(file_path.stat().st_ctime).isoformat()
                    }

                    all_files.append(file_info)
                    file_stats["total_files"] += 1

                    # Categorize by extension
                    ext = file_info["extension"]
                    if ext == ".py":
                        file_stats["python_files"] += 1
                    elif ext == ".json":
                        file_stats["json_files"] += 1
                    elif ext in [".md", ".txt"]:
                        if ext == ".md":
                            file_stats["markdown_files"] += 1
                        else:
                            file_stats["text_files"] += 1
                    elif ext == ".ps1":
                        file_stats["powershell_files"] += 1
                    elif ext == ".html":
                        file_stats["html_files"] += 1
                    else:
                        file_stats["other_files"] += 1

                except Exception as e:
                    print(f"⚠️ Error scanning {file_path}: {e}")

        return {
            "files": all_files,
            "statistics": file_stats,
            "scan_timestamp": datetime.datetime.now().isoformat()
        }

    def analyze_file_usage_patterns(self, files_data: Dict) -> Dict:
        """📊 Analyze file usage patterns and relationships"""
        print("📊 Analyzing file usage patterns and relationships...")

        usage_analysis = {
            "recently_active": [],  # Modified within 24 hours
            "moderately_active": [],  # Modified within 7 days
            "older_files": [],  # Modified more than 7 days ago
            "large_files": [],  # Files > 50KB
            "empty_or_small": [],  # Files < 1KB
            "system_critical": [],
            "potential_duplicates": []
        }

        now = datetime.datetime.now()

        for file_info in files_data["files"]:
            try:
                file_path = Path(file_info["path"])
                modified_time = datetime.datetime.fromisoformat(file_info["modified"])
                time_diff = now - modified_time

                # Categorize by activity
                if time_diff.days == 0:
                    usage_analysis["recently_active"].append(file_info)
                elif time_diff.days <= 7:
                    usage_analysis["moderately_active"].append(file_info)
                else:
                    usage_analysis["older_files"].append(file_info)

                # Categorize by size
                if file_info["size"] > 50000:  # 50KB
                    usage_analysis["large_files"].append(file_info)
                elif file_info["size"] < 1000:  # 1KB
                    usage_analysis["empty_or_small"].append(file_info)

                # Identify system critical files
                if any(keyword in file_info["name"].upper() for keyword in [
                    "DREAMER", "BOARDROOM", "EMPIRE", "DNS", "HEALTH", "MONITOR", "AGENT"
                ]):
                    usage_analysis["system_critical"].append(file_info)

                # Check for potential duplicates (similar names)
                base_name = re.sub(r'[⚡💎🔍🚀🎯🏆✅🌟💖🌊🌍🌐⚠️❤️‍🔥🕋🤖💫♾️☮️🪄]', '', file_info["name"])
                base_name = re.sub(r'_\d{8}_\d{6}', '', base_name)  # Remove timestamps

                # Look for similar files
                for other_file in files_data["files"]:
                    if other_file["path"] != file_info["path"]:
                        other_base = re.sub(r'[⚡💎🔍🚀🎯🏆✅🌟💖🌊🌍🌐⚠️❤️‍🔥🕋🤖💫♾️☮️🪄]', '', other_file["name"])
                        other_base = re.sub(r'_\d{8}_\d{6}', '', other_base)

                        if len(base_name) > 10 and base_name in other_base and file_info not in usage_analysis["potential_duplicates"]:
                            usage_analysis["potential_duplicates"].append(file_info)
                            break

            except Exception as e:
                print(f"⚠️ Error analyzing {file_info['path']}: {e}")

        return usage_analysis

    def categorize_files_by_function(self, files_data: Dict) -> Dict:
        """🏷️ Categorize files by their function and importance"""
        print("🏷️ Categorizing files by function and system importance...")

        categories = {
            "core_operational": {
                "description": "Critical system files currently in use",
                "files": [],
                "importance": "HIGH"
            },
            "monitoring_systems": {
                "description": "Health monitoring and status checking systems",
                "files": [],
                "importance": "HIGH"
            },
            "dreamer_portal": {
                "description": "DREAMER Portal Phase 1, 2, 3 system files",
                "files": [],
                "importance": "HIGH"
            },
            "dns_infrastructure": {
                "description": "DNS monitoring and completion systems",
                "files": [],
                "importance": "MEDIUM"
            },
            "celebration_systems": {
                "description": "Achievement and celebration processing",
                "files": [],
                "importance": "MEDIUM"
            },
            "empire_management": {
                "description": "Empire health and coordination systems",
                "files": [],
                "importance": "HIGH"
            },
            "memory_crystals": {
                "description": "Memory crystal and knowledge base files",
                "files": [],
                "importance": "MEDIUM"
            },
            "utility_scripts": {
                "description": "Utility and helper scripts",
                "files": [],
                "importance": "LOW"
            },
            "documentation": {
                "description": "Documentation and README files",
                "files": [],
                "importance": "MEDIUM"
            },
            "deprecated_legacy": {
                "description": "Old or potentially deprecated files",
                "files": [],
                "importance": "LOW"
            },
            "reports_logs": {
                "description": "Generated reports and logs",
                "files": [],
                "importance": "LOW"
            }
        }

        # Categorization patterns
        patterns = {
            "core_operational": [
                "ULTRA_THINKING_BOARDROOM", "EMPIRE_STATUS", "HEALTH_SCAN",
                "PROJECT_HEALTH", "SYSTEM_STATUS"
            ],
            "monitoring_systems": [
                "MONITOR", "HEALTH", "STATUS", "CHECK", "SCAN", "TRACKER"
            ],
            "dreamer_portal": [
                "DREAMER_PORTAL", "PHASE_1", "PHASE_2", "PHASE_3", "IMPLEMENTATION"
            ],
            "dns_infrastructure": [
                "DNS", "PROPAGATION", "DOMAIN", "SSL", "CERTIFICATE"
            ],
            "celebration_systems": [
                "CELEBRATION", "HAPPY_DANCE", "ACHIEVEMENT", "SUCCESS", "LEGENDARY"
            ],
            "empire_management": [
                "EMPIRE", "AGENT", "COORDINATION", "SYNC", "MANAGEMENT"
            ],
            "memory_crystals": [
                "MEMORY_CRYSTAL", "CRYSTAL", "KNOWLEDGE", "BRAIN"
            ],
            "utility_scripts": [
                "UTIL", "HELPER", "TOOL", "SCRIPT", "QUICK"
            ],
            "documentation": [
                "README", ".md", "DOC", "GUIDE", "MANUAL"
            ],
            "reports_logs": [
                "REPORT", "LOG", "_20250", ".json", "STATUS_2025"
            ]
        }

        for file_info in files_data["files"]:
            file_name_upper = file_info["name"].upper()
            categorized = False

            for category, keywords in patterns.items():
                if any(keyword in file_name_upper for keyword in keywords):
                    categories[category]["files"].append(file_info)
                    categorized = True
                    break

            # If not categorized, put in deprecated_legacy
            if not categorized:
                categories["deprecated_legacy"]["files"].append(file_info)

        return categories

    def identify_cleanup_candidates(self, usage_analysis: Dict, categories: Dict) -> Dict:
        """🗑️ Identify files that can be safely cleaned up"""
        print("🗑️ Identifying cleanup candidates and optimization opportunities...")

        cleanup_recommendations = {
            "safe_to_delete": {
                "description": "Files that can be safely deleted",
                "files": [],
                "reasoning": []
            },
            "archive_candidates": {
                "description": "Files to move to archive folder",
                "files": [],
                "reasoning": []
            },
            "duplicate_resolution": {
                "description": "Duplicate files requiring resolution",
                "files": [],
                "reasoning": []
            },
            "optimization_opportunities": {
                "description": "Files that could be optimized or consolidated",
                "files": [],
                "reasoning": []
            }
        }

        # Safe to delete: Old report files and temporary files
        for file_info in usage_analysis["older_files"]:
            file_name = file_info["name"].upper()

            # Old report files with timestamps
            if any(pattern in file_name for pattern in [
                "REPORT_2025", "STATUS_2025", "_20250", "LOG_2025"
            ]) and any(ext in file_name for ext in [".JSON", ".TXT"]):
                cleanup_recommendations["safe_to_delete"]["files"].append(file_info)
                cleanup_recommendations["safe_to_delete"]["reasoning"].append(f"Old report file: {file_info['name']}")

        # Archive candidates: Large files not recently accessed
        for file_info in usage_analysis["large_files"]:
            if file_info in usage_analysis["older_files"]:
                file_name = file_info["name"].upper()
                if not any(critical in file_name for critical in [
                    "BOARDROOM", "EMPIRE", "DREAMER", "CORE"
                ]):
                    cleanup_recommendations["archive_candidates"]["files"].append(file_info)
                    cleanup_recommendations["archive_candidates"]["reasoning"].append(
                        f"Large file not recently used: {file_info['name']} ({file_info['size']} bytes)"
                    )

        # Duplicate resolution
        cleanup_recommendations["duplicate_resolution"]["files"] = usage_analysis["potential_duplicates"]
        for file_info in usage_analysis["potential_duplicates"]:
            cleanup_recommendations["duplicate_resolution"]["reasoning"].append(
                f"Potential duplicate: {file_info['name']}"
            )

        # Optimization opportunities
        celebration_files = [f for f in categories["celebration_systems"]["files"] if len(categories["celebration_systems"]["files"]) > 3]
        if celebration_files:
            cleanup_recommendations["optimization_opportunities"]["files"] = celebration_files[:3]
            cleanup_recommendations["optimization_opportunities"]["reasoning"].append(
                "Multiple celebration systems could be consolidated into single optimized system"
            )

        return cleanup_recommendations

    def generate_comprehensive_report(self) -> Dict:
        """📋 Generate comprehensive file analysis and cleanup report"""
        print("📋 Generating comprehensive workspace analysis report...")

        # Perform all analyses
        files_data = self.scan_all_files()
        usage_analysis = self.analyze_file_usage_patterns(files_data)
        categories = self.categorize_files_by_function(files_data)
        cleanup_recommendations = self.identify_cleanup_candidates(usage_analysis, categories)

        # Generate running process information
        try:
            result = subprocess.run("tasklist | findstr python", shell=True, capture_output=True, text=True)
            running_processes = result.stdout.strip().split('\n') if result.stdout.strip() else []
        except:
            running_processes = []

        comprehensive_report = {
            "report_metadata": {
                "timestamp": datetime.datetime.now().isoformat(),
                "report_type": "ULTRA_BOARDROOM_COMPREHENSIVE_FILE_ANALYSIS",
                "scan_scope": "COMPLETE_WORKSPACE",
                "analysis_depth": "DETAILED_WITH_CLEANUP_RECOMMENDATIONS"
            },
            "workspace_statistics": files_data["statistics"],
            "file_activity_analysis": {
                "recently_active_count": len(usage_analysis["recently_active"]),
                "moderately_active_count": len(usage_analysis["moderately_active"]),
                "older_files_count": len(usage_analysis["older_files"]),
                "large_files_count": len(usage_analysis["large_files"]),
                "system_critical_count": len(usage_analysis["system_critical"]),
                "potential_duplicates_count": len(usage_analysis["potential_duplicates"])
            },
            "system_categorization": categories,
            "cleanup_analysis": cleanup_recommendations,
            "current_active_systems": {
                "running_python_processes": len(running_processes),
                "active_system_files": [f["name"] for f in usage_analysis["recently_active"] if f["extension"] == ".py"][:10]
            },
            "optimization_summary": {
                "total_files_scanned": files_data["statistics"]["total_files"],
                "cleanup_candidates": len(cleanup_recommendations["safe_to_delete"]["files"]),
                "archive_candidates": len(cleanup_recommendations["archive_candidates"]["files"]),
                "duplicate_files": len(cleanup_recommendations["duplicate_resolution"]["files"]),
                "optimization_opportunities": len(cleanup_recommendations["optimization_opportunities"]["files"])
            }
        }

        return comprehensive_report

    def display_analysis_report(self):
        """🖥️ Display comprehensive analysis report"""
        report = self.generate_comprehensive_report()

        print("🔍💎⚡ ULTRA-THINKING BOARDROOM FILE ANALYSIS REPORT ⚡💎🔍")
        print("=" * 80)
        print(f"⏰ Analysis Timestamp: {report['report_metadata']['timestamp']}")
        print(f"📁 Scan Scope: {report['report_metadata']['scan_scope']}")
        print()

        # Workspace Statistics
        stats = report["workspace_statistics"]
        print("📊 WORKSPACE STATISTICS")
        print("-" * 60)
        print(f"   📁 Total Files: {stats['total_files']}")
        print(f"   📁 Directories: {stats['directories']}")
        print(f"   🐍 Python Files: {stats['python_files']}")
        print(f"   📄 JSON Files: {stats['json_files']}")
        print(f"   📝 Markdown Files: {stats['markdown_files']}")
        print(f"   💻 PowerShell Files: {stats['powershell_files']}")
        print(f"   📋 Text Files: {stats['text_files']}")
        print(f"   🌐 HTML Files: {stats['html_files']}")
        print(f"   📄 Other Files: {stats['other_files']}")
        print()

        # File Activity Analysis
        activity = report["file_activity_analysis"]
        print("⚡ FILE ACTIVITY ANALYSIS")
        print("-" * 60)
        print(f"   🔥 Recently Active (24h): {activity['recently_active_count']}")
        print(f"   📊 Moderately Active (7d): {activity['moderately_active_count']}")
        print(f"   📋 Older Files (7d+): {activity['older_files_count']}")
        print(f"   💾 Large Files (50KB+): {activity['large_files_count']}")
        print(f"   🎯 System Critical: {activity['system_critical_count']}")
        print(f"   🔍 Potential Duplicates: {activity['potential_duplicates_count']}")
        print()

        # System Categorization Summary
        print("🏷️ SYSTEM CATEGORIZATION SUMMARY")
        print("-" * 60)
        for category, data in report["system_categorization"].items():
            importance_icon = "🔴" if data["importance"] == "HIGH" else "🟡" if data["importance"] == "MEDIUM" else "🟢"
            print(f"   {importance_icon} {category.replace('_', ' ').title()}: {len(data['files'])} files ({data['importance']} priority)")
        print()

        # Current Active Systems
        active = report["current_active_systems"]
        print("🚀 CURRENT ACTIVE SYSTEMS")
        print("-" * 60)
        print(f"   🐍 Running Python Processes: {active['running_python_processes']}")
        print("   📝 Recently Active Python Files:")
        for file_name in active["active_system_files"][:5]:
            print(f"      ⚡ {file_name}")
        print()

        # Cleanup Analysis Summary
        cleanup = report["cleanup_analysis"]
        print("🗑️ CLEANUP RECOMMENDATIONS")
        print("-" * 60)
        print(f"   🗑️ Safe to Delete: {len(cleanup['safe_to_delete']['files'])} files")
        print(f"   📦 Archive Candidates: {len(cleanup['archive_candidates']['files'])} files")
        print(f"   🔍 Duplicate Resolution: {len(cleanup['duplicate_resolution']['files'])} files")
        print(f"   ⚡ Optimization Opportunities: {len(cleanup['optimization_opportunities']['files'])} files")
        print()

        # Optimization Summary
        optimization = report["optimization_summary"]
        print("📈 OPTIMIZATION SUMMARY")
        print("-" * 60)
        print(f"   📊 Total Files Analyzed: {optimization['total_files_scanned']}")
        total_cleanup = (optimization['cleanup_candidates'] +
                        optimization['archive_candidates'] +
                        optimization['duplicate_files'])
        print(f"   🎯 Total Cleanup Potential: {total_cleanup} files")
        print(f"   💎 Optimization Opportunities: {optimization['optimization_opportunities']}")

        if total_cleanup > 0:
            cleanup_percentage = (total_cleanup / optimization['total_files_scanned']) * 100
            print(f"   📉 Potential Space Savings: {cleanup_percentage:.1f}% of files")

        print()
        print("=" * 80)

        # Save comprehensive report
        report_filename = f"h:/ULTRA_BOARDROOM_FILE_ANALYSIS_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(report_filename, 'w') as f:
            json.dump(report, f, indent=4)

        print(f"📋 Comprehensive report saved: {report_filename}")

        return report

def main():
    """Main execution"""
    print("🎯 ULTRA-THINKING BOARDROOM: Initiating Comprehensive File Analysis")
    print("⚡ Following LOOK-THEN-BUILD protocol for complete workspace organization")
    print()

    analyzer = UltraBoardroomFileAnalyzer()
    analysis_report = analyzer.display_analysis_report()

    print("\n🏆 ULTRA-THINKING BOARDROOM FILE ANALYSIS COMPLETE!")
    print("💎 Ready for cleanup implementation based on recommendations!")

    return analysis_report

if __name__ == "__main__":
    main()

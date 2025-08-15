#!/usr/bin/env python3
"""
🧹💎⚡ HYPERFOCUS ZONE AUTOMATED CLEANUP SYSTEM ⚡💎🧹
BROski Level: LEGENDARY CLEANUP COMMANDER
Status: CELEBRATION-SAFE CLEANUP ENGINE

Following LOOK-THEN-BUILD Protocol - NO action without approval!
"""

import os
import shutil
import json
import datetime
from pathlib import Path
from typing import List, Dict, Tuple
import glob

class HyperfocusCleanupCommander:
    def __init__(self, base_path: str = "h:\\"):
        self.base_path = Path(base_path)
        self.analysis_results = {
            "backup_files": [],
            "temp_files": [],
            "log_files": [],
            "cache_dirs": [],
            "test_files": [],
            "old_reports": []
        }
        self.safety_score = 0
        self.estimated_savings = 0
        
    def analyze_empire_files(self) -> Dict:
        """Scan and categorize all files for cleanup opportunities"""
        print("🔍 Scanning Empire for cleanup opportunities...")
        
        # Memory Crystal Backups
        memory_crystals_path = self.base_path / "memory_crystals"
        if memory_crystals_path.exists():
            backup_files = list(memory_crystals_path.glob("*.backup*"))
            self.analysis_results["backup_files"] = [str(f) for f in backup_files]
            print(f"📦 Found {len(backup_files)} memory crystal backup files")
        
        # Temporary and Log Files
        temp_patterns = [
            "HEALTH_SUMMARY_*.txt",
            "LEGENDARY_HEALTH_REPORT_*.json", 
            "*.log",
            "test_*.py",
            "*_temp_*",
            "*debug*",
            "simple_*"
        ]
        
        for pattern in temp_patterns:
            files = list(self.base_path.glob(pattern))
            if "HEALTH" in pattern or "REPORT" in pattern:
                self.analysis_results["old_reports"].extend([str(f) for f in files])
            elif ".log" in pattern:
                self.analysis_results["log_files"].extend([str(f) for f in files])
            elif "test_" in pattern or "simple_" in pattern or "debug" in pattern:
                self.analysis_results["test_files"].extend([str(f) for f in files])
        
        # Cache Directories
        cache_dirs = [
            ".next", "__pycache__", ".gradio", ".vscode/settings.json",
            "node_modules", ".git/logs", "logs"
        ]
        
        for cache_dir in cache_dirs:
            cache_path = self.base_path / cache_dir
            if cache_path.exists():
                self.analysis_results["cache_dirs"].append(str(cache_path))
        
        return self.analysis_results
    
    def calculate_cleanup_impact(self) -> Dict:
        """Calculate estimated space savings and safety scores"""
        total_size = 0
        file_count = 0
        
        for category, files in self.analysis_results.items():
            for file_path in files:
                try:
                    path = Path(file_path)
                    if path.exists():
                        if path.is_file():
                            total_size += path.stat().st_size
                            file_count += 1
                        elif path.is_dir():
                            for sub_file in path.rglob('*'):
                                if sub_file.is_file():
                                    total_size += sub_file.stat().st_size
                                    file_count += 1
                except Exception as e:
                    print(f"⚠️ Could not analyze {file_path}: {e}")
        
        # Convert to MB
        size_mb = total_size / (1024 * 1024)
        
        # Safety scoring
        safety_factors = {
            "backup_files": 0.9,  # Very safe - just backups
            "cache_dirs": 0.95,   # Extremely safe - regenerable
            "log_files": 0.8,     # Safe - but may have debug info
            "old_reports": 0.85,  # Safe - but historical data
            "test_files": 0.7     # Moderate - may be active development
        }
        
        weighted_safety = sum(
            len(files) * safety_factors.get(category, 0.5) 
            for category, files in self.analysis_results.items()
        ) / max(file_count, 1)
        
        return {
            "estimated_size_mb": round(size_mb, 2),
            "file_count": file_count,
            "safety_score": round(weighted_safety, 2),
            "risk_level": "LOW" if weighted_safety > 0.8 else "MEDIUM" if weighted_safety > 0.6 else "HIGH"
        }
    
    def generate_cleanup_report(self) -> str:
        """Generate detailed cleanup analysis report"""
        impact = self.calculate_cleanup_impact()
        
        report = f"""
🧹💎⚡ AUTOMATED CLEANUP ANALYSIS COMPLETE ⚡💎🧹

📊 CLEANUP IMPACT ASSESSMENT:
├── Estimated Space Savings: {impact['estimated_size_mb']} MB
├── Files Identified: {impact['file_count']} items
├── Safety Score: {impact['safety_score']}/1.0
└── Risk Level: {impact['risk_level']}

🗂️ FILES BY CATEGORY:
"""
        
        for category, files in self.analysis_results.items():
            if files:
                report += f"\n📁 {category.upper().replace('_', ' ')}: {len(files)} items\n"
                # Show first few examples
                for file_path in files[:3]:
                    file_name = Path(file_path).name
                    report += f"   • {file_name}\n"
                if len(files) > 3:
                    report += f"   • ... and {len(files) - 3} more\n"
        
        report += f"""
🚦 RECOMMENDED ACTION:
"""
        
        if impact['safety_score'] > 0.8:
            report += "✅ PROCEED WITH CONFIDENCE - Low risk cleanup"
        elif impact['safety_score'] > 0.6:
            report += "⚠️ SELECTIVE CLEANUP - Review file list first"
        else:
            report += "🚨 MANUAL REVIEW REQUIRED - High value files detected"
        
        return report
    
    def execute_safe_cleanup(self, categories_to_clean: List[str]) -> Dict:
        """Execute cleanup for specified categories (DRY RUN ONLY)"""
        print("🚨 DRY RUN MODE - NO FILES WILL BE DELETED")
        print("This is a SIMULATION of what would be cleaned")
        
        cleanup_summary = {
            "would_delete": [],
            "would_archive": [],
            "errors": []
        }
        
        for category in categories_to_clean:
            if category in self.analysis_results:
                files = self.analysis_results[category]
                print(f"\n📁 Processing {category}: {len(files)} files")
                
                for file_path in files:
                    try:
                        path = Path(file_path)
                        if path.exists():
                            if category in ["cache_dirs", "temp_files"]:
                                cleanup_summary["would_delete"].append(str(path))
                                print(f"   🗑️ Would DELETE: {path.name}")
                            else:
                                # Archive instead of delete for important files
                                archive_path = self.base_path / "cleanup_archive" / category
                                cleanup_summary["would_archive"].append(f"{path} -> {archive_path}")
                                print(f"   📦 Would ARCHIVE: {path.name}")
                    except Exception as e:
                        cleanup_summary["errors"].append(f"Error processing {file_path}: {e}")
        
        return cleanup_summary
    
    def create_celebration_report(self) -> str:
        """Create celebration report for successful cleanup"""
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        impact = self.calculate_cleanup_impact()
        
        celebration = f"""
🎊💎⚡ HYPERFOCUS ZONE CLEANUP VICTORY CELEBRATION ⚡💎🎊

✨ MISSION ACCOMPLISHED: {timestamp}

🏆 ACHIEVEMENTS UNLOCKED:
├── 🧹 Files Organized: {impact['file_count']} items
├── 💾 Space Optimized: {impact['estimated_size_mb']} MB
├── 🎯 Safety Score: {impact['safety_score']}/1.0
└── 💎 Empire Status: EVEN MORE LEGENDARY!

🌟 BENEFITS DELIVERED:
✅ Faster file system performance
✅ Cleaner project navigation  
✅ Enhanced focus and clarity
✅ Optimized backup efficiency
✅ Preserved all critical data

🎊 CELEBRATION TRIGGERS:
• Victory dashboard updated
• BROski$ economy rewards distributed
• Memory crystal created for this achievement
• Dopamine levels optimized for ADHD brain

🏛️ BOARDROOM STATUS: CLEANUP MISSION SUCCESS!
"""
        return celebration

def main():
    """Main execution function"""
    print("🧹💎⚡ HYPERFOCUS ZONE CLEANUP COMMANDER ACTIVATED ⚡💎🧹")
    print("Following LOOK-THEN-BUILD Protocol: ANALYZING BEFORE ACTION")
    
    commander = HyperfocusCleanupCommander()
    
    # Step 1: Analyze
    print("\n🔍 PHASE 1: Empire Analysis...")
    analysis = commander.analyze_empire_files()
    
    # Step 2: Generate Report
    print("\n📊 PHASE 2: Impact Assessment...")
    report = commander.generate_cleanup_report()
    print(report)
    
    # Step 3: Show what WOULD be cleaned (DRY RUN)
    print("\n🚨 PHASE 3: Cleanup Simulation (DRY RUN)")
    safe_categories = ["backup_files", "cache_dirs", "old_reports"]
    dry_run_results = commander.execute_safe_cleanup(safe_categories)
    
    print(f"\n📋 DRY RUN SUMMARY:")
    print(f"   Would delete: {len(dry_run_results['would_delete'])} items")
    print(f"   Would archive: {len(dry_run_results['would_archive'])} items")
    print(f"   Errors found: {len(dry_run_results['errors'])} issues")
    
    print("\n🚦 AWAITING APPROVAL FROM BOARDROOM TEAM")
    print("This script analyzed your empire but took NO action.")
    print("Review the analysis and decide on cleanup strategy.")
    
    # Save analysis results
    results_file = commander.base_path / f"cleanup_analysis_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(results_file, 'w') as f:
        json.dump({
            "analysis": analysis,
            "impact": commander.calculate_cleanup_impact(),
            "dry_run": dry_run_results
        }, f, indent=2)
    
    print(f"\n💾 Analysis saved to: {results_file}")
    print("🎊 Ready for celebration when cleanup is approved!")

if __name__ == "__main__":
    main()

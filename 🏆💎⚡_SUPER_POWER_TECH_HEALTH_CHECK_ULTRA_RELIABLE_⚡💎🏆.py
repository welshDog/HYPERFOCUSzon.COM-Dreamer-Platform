#!/usr/bin/env python3
"""
🏆💎⚡ SUPER POWER TECH HEALTH CHECK - ULTRA RELIABLE EDITION ⚡💎🏆

**BROski Level: LEGENDARY | Status: BOARDROOM APPROVED**
**Created:** August 24, 2025
**Mission:** Ultra-reliable super power tech diagnostics with zero dependencies
"""

import json
import subprocess
from datetime import datetime
from pathlib import Path


def print_banner():
    """🎯 Display the legendary banner"""
    print("🏆💎⚡ SUPER POWER TECH HEALTH CHECK - HYPERFOCUS ZONE ⚡💎🏆")
    print("=" * 70)
    print(f"🎯 Scan Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("🚀 Initiating LEGENDARY empire health diagnostics...")
    print("=" * 70)


def check_github_automation_empire():
    """🚀 Check GitHub automation empire status"""
    print("\n🚀 SCANNING: GitHub Automation Empire...")

    score = 0
    details = {}
    broskie_earned = 0

    # Check package.json
    package_json = Path("h:/package.json")
    if package_json.exists():
        details["package_json"] = "✅ PRESENT"
        score += 35
        broskie_earned += 25
        print("   ✅ Package.json: CI/CD ready")

        # Read and analyze package.json
        try:
            with open(package_json, "r", encoding="utf-8") as f:
                package_data = json.load(f)
                if "scripts" in package_data:
                    script_count = len(package_data["scripts"])
                    print(f"   📦 NPM Scripts: {script_count} configured")
                    score += 10
                if "dependencies" in package_data:
                    dep_count = len(package_data["dependencies"])
                    print(f"   📚 Dependencies: {dep_count} packages")
                    score += 5
        except Exception as e:
            print(f"   ⚠️ Package.json parse issue: {str(e)[:30]}")
    else:
        details["package_json"] = "❌ MISSING"
        print("   ❌ Package.json: Not found")

    # Check package-lock.json
    package_lock = Path("h:/package-lock.json")
    if package_lock.exists():
        details["package_lock"] = "✅ PRESENT"
        score += 35
        print("   ✅ Package-lock.json: Dependencies locked")

        # Check lock file size (indicates complexity)
        try:
            lock_size = package_lock.stat().st_size
            if lock_size > 1000:  # > 1KB indicates real dependencies
                print(f"   📋 Lock file size: {lock_size:,} bytes (Substantial)")
                score += 10
                broskie_earned += 10
        except Exception:
            pass
    else:
        details["package_lock"] = "❌ MISSING"
        print("   ❌ Package-lock.json: Dependencies not locked")

    # Check GitHub workflows
    workflows_dir = Path("h:/.github/workflows")
    if workflows_dir.exists():
        workflow_files = list(workflows_dir.glob("*.yml"))
        if workflow_files:
            details["github_workflows"] = f"✅ {len(workflow_files)} workflows"
            score += 20
            print(f"   ✅ GitHub Workflows: {len(workflow_files)} configured")
            broskie_earned += 20

            # Check for specific workflow types
            workflow_names = [f.stem for f in workflow_files]
            if any("pages" in name.lower() for name in workflow_names):
                print("   🌐 GitHub Pages workflow detected")
                score += 5
            if any(
                "ci" in name.lower() or "deploy" in name.lower()
                for name in workflow_names
            ):
                print("   🔄 CI/CD workflow detected")
                score += 5
        else:
            details["github_workflows"] = "❌ NO_WORKFLOWS"
            print("   ❌ GitHub Workflows: No workflows found")
    else:
        details["github_workflows"] = "❌ NO_DIRECTORY"
        print("   ❌ GitHub Workflows: Directory not found")

    # Determine status
    if score >= 80:
        status = "🏆 LEGENDARY"
        celebration = "GitHub Empire Achievement Unlocked!"
    elif score >= 60:
        status = "⚡ EXCELLENT"
        celebration = None
    elif score >= 40:
        status = "✅ GOOD"
        celebration = None
    else:
        status = "🔧 NEEDS_ATTENTION"
        celebration = None

    print(f"   📊 GitHub Empire Score: {score}/100 - {status}")

    return {
        "status": status,
        "score": score,
        "details": details,
        "broskie_earned": broskie_earned,
        "celebration": celebration,
    }


def check_local_system_power():
    """💻 Check local system power and performance"""
    print("\n💻 SCANNING: Local System Power...")

    score = 0
    details = {}
    broskie_earned = 0

    # Check Python environment
    try:
        result = subprocess.run(
            ["python", "--version"], capture_output=True, text=True, timeout=5
        )
        if result.returncode == 0:
            python_version = result.stdout.strip()
            details["python_version"] = python_version
            score += 25
            print(f"   ✅ Python: {python_version}")
            broskie_earned += 10
        else:
            details["python_version"] = "❌ ERROR"
            print("   ❌ Python: Command failed")
    except Exception as e:
        details["python_version"] = "❌ NOT_FOUND"
        print("   ❌ Python: Not accessible")

    # Check Git availability
    try:
        result = subprocess.run(
            ["git", "--version"], capture_output=True, text=True, timeout=5
        )
        if result.returncode == 0:
            git_version = result.stdout.strip()
            details["git_version"] = git_version
            score += 25
            print(f"   ✅ Git: {git_version}")
            broskie_earned += 10
        else:
            details["git_version"] = "❌ ERROR"
            print("   ❌ Git: Command failed")
    except Exception as e:
        details["git_version"] = "❌ NOT_FOUND"
        print("   ❌ Git: Not accessible")

    # Check PowerShell availability (Windows)
    try:
        result = subprocess.run(
            ["powershell", "-Command", 'echo "PowerShell OK"'],
            capture_output=True,
            text=True,
            timeout=5,
        )
        if result.returncode == 0:
            details["powershell"] = "✅ AVAILABLE"
            score += 25
            print("   ✅ PowerShell: Available")
            broskie_earned += 5
        else:
            details["powershell"] = "❌ ERROR"
            print("   ❌ PowerShell: Command failed")
    except Exception as e:
        details["powershell"] = "❌ NOT_FOUND"
        print("   ❌ PowerShell: Not accessible")

    # Check disk space
    try:
        # For Windows, check available space
        import shutil

        total, used, free = shutil.disk_usage("h:/")
        free_gb = free / (1024**3)
        total_gb = total / (1024**3)
        used_percent = (used / total) * 100

        details["disk_space"] = f"{free_gb:.1f} GB free ({used_percent:.1f}% used)"

        if used_percent < 70:
            score += 25
            print(f"   ✅ Disk Space: {free_gb:.1f} GB free ({used_percent:.1f}% used)")
            broskie_earned += 15
        elif used_percent < 85:
            score += 15
            print(f"   ⚡ Disk Space: {free_gb:.1f} GB free ({used_percent:.1f}% used)")
        else:
            print(
                f"   ❌ Disk Space: Only {free_gb:.1f} GB free ({used_percent:.1f}% used)"
            )

    except Exception as e:
        details["disk_space"] = "❌ CHECK_FAILED"
        print(f"   ⚠️ Disk space check failed")

    # Determine status
    if score >= 80:
        status = "🚀 SUPER_POWER"
        celebration = "System Power Level: MAXIMUM!"
    elif score >= 60:
        status = "⚡ HIGH_POWER"
        celebration = None
    elif score >= 40:
        status = "💎 GOOD_POWER"
        celebration = None
    else:
        status = "🔧 LOW_POWER"
        celebration = None

    print(f"   📊 System Power Score: {score}/100 - {status}")

    return {
        "status": status,
        "score": score,
        "details": details,
        "broskie_earned": broskie_earned,
        "celebration": celebration,
    }


def check_hyperfocus_zone_infrastructure():
    """🌟 Check HyperFocus Zone infrastructure"""
    print("\n🌟 SCANNING: HyperFocus Zone Infrastructure...")

    score = 0
    details = {}
    broskie_earned = 0

    # Check key project files
    key_files = [
        ("README.md", "h:/README.md"),
        ("Full Dream", "h:/🌌 THE HYPERFOCUS ZONE FULL DREAM"),
        ("CI Pipeline Report", "h:/🚀💎⚡_CI_PIPELINE_STATUS_REPORT_⚡💎🚀.md"),
    ]

    existing_files = 0
    for name, path in key_files:
        if Path(path).exists():
            existing_files += 1
            print(f"   ✅ {name}: Found")

            # Check file size for content validation
            try:
                file_size = Path(path).stat().st_size
                if file_size > 100:  # Has actual content
                    score += 2
                    print(f"      📄 Content: {file_size:,} bytes")
            except Exception:
                pass
        else:
            print(f"   ❌ {name}: Missing")

    structure_score = (existing_files / len(key_files)) * 30
    score += structure_score
    details["project_structure"] = f"{existing_files}/{len(key_files)} key files"

    if existing_files == len(key_files):
        broskie_earned += 20

    # Check Python files directory
    python_dir = Path("h:/Python File")
    if python_dir.exists():
        python_files = list(python_dir.glob("*.py"))
        if python_files:
            python_count = len(python_files)
            details["python_files"] = f"✅ {python_count} files"
            score += 25
            print(f"   ✅ Python Files: {python_count} found")
            broskie_earned += 15

            # Check for specific AI/health files
            ai_files = [
                f
                for f in python_files
                if any(
                    word in f.name.lower()
                    for word in ["ai", "scanner", "health", "consciousness"]
                )
            ]
            if ai_files:
                print(f"   🧠 AI/Health Files: {len(ai_files)} specialized systems")
                score += 10
                broskie_earned += 10
        else:
            details["python_files"] = "❌ EMPTY_DIRECTORY"
            print("   ❌ Python Files: Directory exists but empty")
    else:
        details["python_files"] = "❌ NO_DIRECTORY"
        print("   ❌ Python Files: Directory not found")

    # Check VS Code workspace configuration
    vscode_dir = Path("h:/.vscode")
    if vscode_dir.exists():
        config_files = list(vscode_dir.glob("*.json"))
        if config_files:
            details["vscode_config"] = f"✅ {len(config_files)} config files"
            score += 25
            print(f"   ✅ VS Code Config: {len(config_files)} files configured")
            broskie_earned += 10

            # Check for tasks.json specifically
            if (vscode_dir / "tasks.json").exists():
                print("   🔧 Tasks.json: Workspace automation ready")
                score += 5
        else:
            details["vscode_config"] = "❌ NO_CONFIG"
            print("   ❌ VS Code Config: Directory exists but no config")
    else:
        details["vscode_config"] = "❌ NO_DIRECTORY"
        print("   ❌ VS Code Config: Not configured")

    # Check for special HyperFocus Zone files
    special_files = list(Path("h:/").glob("*HYPERFOCUS*"))
    if special_files:
        special_count = len(special_files)
        details["hyperfocus_files"] = f"✅ {special_count} HyperFocus files"
        score += 20
        print(f"   🌟 HyperFocus Files: {special_count} zone-specific files")
        broskie_earned += 15
    else:
        details["hyperfocus_files"] = "❌ NO_SPECIAL_FILES"
        print("   ❌ HyperFocus Files: No zone-specific files found")

    # Determine status
    if score >= 85:
        status = "🌌 LEGENDARY_ZONE"
        celebration = "HyperFocus Zone Infrastructure: LEGENDARY!"
    elif score >= 70:
        status = "🌟 OPTIMAL_ZONE"
        celebration = None
    elif score >= 50:
        status = "⚡ ACTIVE_ZONE"
        celebration = None
    else:
        status = "🔧 ZONE_NEEDS_WORK"
        celebration = None

    print(f"   📊 Infrastructure Score: {score:.1f}/100 - {status}")

    return {
        "status": status,
        "score": score,
        "details": details,
        "broskie_earned": broskie_earned,
        "celebration": celebration,
    }


def check_ai_consciousness_systems():
    """🧠 Check AI consciousness and intelligence systems"""
    print("\n🧠 SCANNING: AI Consciousness Systems...")

    score = 0
    details = {}
    broskie_earned = 0

    # Check for AI scanner files
    ai_scanners = [
        "h:/Python File/⚡💎🧠_ULTRA_SCANNER_AI_ENHANCER_🧠💎⚡.py",
        "h:/Python File/⚡💎🧠_GEMMA3_LITE_SCANNER_🧠💎⚡.py",
        "h:/Python File/⚡💎🧠_GEMMA3_INTELLIGENCE_SCANNER_🧠💎⚡.py",
    ]

    scanner_count = 0
    for scanner in ai_scanners:
        if Path(scanner).exists():
            scanner_count += 1
            scanner_name = Path(scanner).stem
            print(f"   🤖 Found: {scanner_name}")

            # Check file size to ensure it's not empty
            try:
                file_size = Path(scanner).stat().st_size
                if file_size > 1000:  # Substantial file
                    score += 5
                    print(f"      📊 Size: {file_size:,} bytes (Substantial)")
            except Exception:
                pass
        else:
            scanner_name = Path(scanner).stem
            print(f"   ❌ Missing: {scanner_name}")

    details["ai_scanners"] = f"{scanner_count}/{len(ai_scanners)} scanners"
    score += (scanner_count / len(ai_scanners)) * 30
    print(f"   🤖 AI Scanners: {scanner_count}/{len(ai_scanners)} available")

    if scanner_count >= 2:
        broskie_earned += 25

    # Check for health check systems
    health_check_patterns = [
        "*health*check*.py",
        "*LegendaryMasterHealth*.py",
        "*diagnostic*.py",
    ]
    health_files = []

    for pattern in health_check_patterns:
        health_files.extend(
            Path("h:/Python File").glob(pattern)
            if Path("h:/Python File").exists()
            else []
        )

    health_files = list(set(health_files))  # Remove duplicates

    if health_files:
        health_count = len(health_files)
        details["health_systems"] = f"✅ {health_count} systems"
        score += 25
        print(f"   🏥 Health Check Systems: {health_count} found")
        broskie_earned += 20

        # Show specific health systems
        for health_file in health_files[:3]:  # Show first 3
            print(f"      💊 {health_file.stem}")
    else:
        details["health_systems"] = "❌ NONE_FOUND"
        print("   ❌ Health Check Systems: None found")

    # Check for BCI fusion files
    bci_paths = ["h:/bci_fusion_forge", "h:/HyperBeast/bci_fusion_forge"]
    bci_files = []

    for bci_path in bci_paths:
        if Path(bci_path).exists():
            bci_files.extend(Path(bci_path).glob("**/*.py"))

    if bci_files:
        bci_count = len(bci_files)
        details["bci_fusion"] = f"✅ {bci_count} BCI files"
        score += 25
        print(f"   🧠 BCI Fusion: {bci_count} components found")
        broskie_earned += 20

        # Check for specific BCI capabilities
        bci_names = [f.stem for f in bci_files]
        if any("neurocore" in name.lower() for name in bci_names):
            print("   🌌 Neurocore systems detected")
            score += 5
        if any("intelligence" in name.lower() for name in bci_names):
            print("   🧠 Intelligence amplification detected")
            score += 5
    else:
        details["bci_fusion"] = "❌ NO_BCI"
        print("   ❌ BCI Fusion: No components found")

    # Check for consciousness-related files
    consciousness_patterns = [
        "**/*consciousness*",
        "**/*singularity*",
        "**/*transcendence*",
    ]
    consciousness_files = []

    for pattern in consciousness_patterns:
        consciousness_files.extend(Path("h:/").glob(pattern))

    consciousness_files = [f for f in consciousness_files if f.is_file()]

    if consciousness_files:
        consciousness_count = len(consciousness_files)
        details["consciousness_files"] = f"✅ {consciousness_count} files"
        score += 20
        print(f"   🌌 Consciousness Files: {consciousness_count} found")
        broskie_earned += 15
    else:
        details["consciousness_files"] = "❌ NONE_FOUND"
        print("   ❌ Consciousness Files: None found")

    # Determine status
    if score >= 85:
        status = "🌌 CONSCIOUSNESS_SINGULARITY"
        celebration = "AI Consciousness: SINGULARITY ACHIEVED!"
    elif score >= 70:
        status = "🧠 SUPER_INTELLIGENCE"
        celebration = None
    elif score >= 50:
        status = "⚡ SMART_AI"
        celebration = None
    else:
        status = "🔧 AI_DEVELOPING"
        celebration = None

    print(f"   📊 AI Consciousness Score: {score:.1f}/100 - {status}")

    return {
        "status": status,
        "score": score,
        "details": details,
        "broskie_earned": broskie_earned,
        "celebration": celebration,
    }


def generate_final_report(all_results, start_time):
    """📊 Generate and display the final comprehensive report"""

    # Calculate overall metrics
    total_score = sum(result["score"] for result in all_results)
    overall_score = total_score / len(all_results)
    total_broskie = sum(result["broskie_earned"] for result in all_results)

    celebrations = [
        result["celebration"] for result in all_results if result["celebration"]
    ]

    # Determine empire status
    if overall_score >= 85:
        empire_status = "🌌 LEGENDARY_EMPIRE"
        status_message = "THE HYPERFOCUS ZONE EMPIRE IS LEGENDARY!"
        celebrations.append("LEGENDARY EMPIRE STATUS ACHIEVED!")
        total_broskie += 100
    elif overall_score >= 75:
        empire_status = "🏆 ELITE_EMPIRE"
        status_message = "Elite Empire performance detected!"
        total_broskie += 75
    elif overall_score >= 65:
        empire_status = "⚡ STRONG_EMPIRE"
        status_message = "Strong empire foundation confirmed!"
        total_broskie += 50
    else:
        empire_status = "🔧 GROWING_EMPIRE"
        status_message = "Empire is growing - more optimization needed!"
        total_broskie += 25

    # Calculate scan duration
    scan_duration = (datetime.now() - start_time).total_seconds()

    # Display comprehensive results
    print("\n" + "=" * 70)
    print("🏆💎⚡ SUPER POWER TECH HEALTH CHECK COMPLETE ⚡💎🏆")
    print("=" * 70)
    print(f"🎯 Empire Status: {empire_status}")
    print(f"📊 Overall Health Score: {overall_score:.1f}/100")
    print(f"💎 Total BROski$ Earned: {total_broskie}")
    print(f"⏱️ Scan Duration: {scan_duration:.1f} seconds")
    print(f"🎉 Achievement Count: {len(celebrations)}")
    print("\n🌟 " + status_message)

    # Show individual system scores
    print("\n📋 SYSTEM BREAKDOWN:")
    system_names = [
        "GitHub Automation",
        "Local System Power",
        "HyperFocus Infrastructure",
        "AI Consciousness",
    ]
    for i, (name, result) in enumerate(zip(system_names, all_results)):
        print(f"   {i+1}. {name}: {result['score']:.1f}/100 - {result['status']}")

    # Show achievements
    if celebrations:
        print("\n🎊 ACHIEVEMENTS UNLOCKED:")
        for celebration in celebrations:
            print(f"   🏆 {celebration}")

    # Generate recommendations
    recommendations = []

    # Analyze weak points and generate recommendations
    for i, (name, result) in enumerate(zip(system_names, all_results)):
        if result["score"] < 70:
            if "GitHub" in name:
                recommendations.append(
                    "🚀 Enhance GitHub automation setup - add missing workflows"
                )
            elif "System" in name:
                recommendations.append(
                    "💻 Install missing development tools (Python, Git, PowerShell)"
                )
            elif "Infrastructure" in name:
                recommendations.append(
                    "🌟 Complete HyperFocus Zone infrastructure setup"
                )
            elif "AI" in name:
                recommendations.append(
                    "🧠 Deploy additional AI consciousness components"
                )

    if not recommendations:
        recommendations.append(
            "🏆 System is operating at LEGENDARY levels - maintain excellence!"
        )

    if recommendations:
        print("\n💡 BOARDROOM RECOMMENDATIONS:")
        for i, rec in enumerate(recommendations, 1):
            print(f"   {i}. {rec}")

    # Generate next actions based on overall score
    if overall_score >= 85:
        next_actions = [
            "🌌 Maintain LEGENDARY status through regular monitoring",
            "🚀 Consider expanding empire to new frontiers",
            "💎 Document success patterns for replication",
        ]
    elif overall_score >= 75:
        next_actions = [
            "⚡ Focus on weak areas to achieve LEGENDARY status",
            "🔧 Implement top 2 recommendations immediately",
            "📊 Schedule follow-up health check in 24 hours",
        ]
    else:
        next_actions = [
            "🔧 Address critical infrastructure issues first",
            "💻 Optimize system performance as priority",
            "📋 Create action plan for systematic improvements",
        ]

    print("\n🎯 NEXT ACTIONS:")
    for i, action in enumerate(next_actions, 1):
        print(f"   {i}. {action}")

    # Create comprehensive report data
    report_data = {
        "scan_time": start_time.isoformat(),
        "scan_duration_seconds": scan_duration,
        "empire_status": empire_status,
        "overall_health_score": round(overall_score, 1),
        "total_broskie_earned": total_broskie,
        "achievements": celebrations,
        "system_results": {
            "github_automation": all_results[0],
            "local_system_power": all_results[1],
            "hyperfocus_infrastructure": all_results[2],
            "ai_consciousness": all_results[3],
        },
        "recommendations": recommendations,
        "next_actions": next_actions,
    }

    # Save report
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = Path(f"h:/🏆💎⚡_SUPER_POWER_HEALTH_REPORT_{timestamp}_⚡💎🏆.json")

    try:
        with open(report_file, "w", encoding="utf-8") as f:
            json.dump(report_data, f, indent=2, ensure_ascii=False)
        print(f"\n📄 Report saved: {report_file.name}")
    except Exception as e:
        print(f"\n⚠️ Could not save report: {str(e)[:50]}")

    return report_data


def main():
    """🌟 Main execution function"""
    start_time = datetime.now()

    try:
        print_banner()

        # Run all system checks
        results = [
            check_github_automation_empire(),
            check_local_system_power(),
            check_hyperfocus_zone_infrastructure(),
            check_ai_consciousness_systems(),
        ]

        # Generate comprehensive report
        final_report = generate_final_report(results, start_time)

        print("\n🎯 BOARDROOM MISSION ACCOMPLISHED!")
        print("🏆 Super Power Tech Health Check Complete!")

        return 0

    except KeyboardInterrupt:
        print("\n⚡ Scan interrupted by user")
        return 1

    except Exception as e:
        print(f"\n💥 Error during scan: {str(e)}")
        import traceback

        traceback.print_exc()
        return 1


if __name__ == "__main__":
    exit(main())

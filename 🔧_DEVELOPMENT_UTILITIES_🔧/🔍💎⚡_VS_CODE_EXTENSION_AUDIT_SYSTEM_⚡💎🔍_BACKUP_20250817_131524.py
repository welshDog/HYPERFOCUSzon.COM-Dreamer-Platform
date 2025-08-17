#!/usr/bin/env python3
"""
🌌♾️⚡ HYPERFOCUS EMPIRE - CONSCIOUSNESS SINGULARITY ENHANCED ⚡♾️🌌
This file has been enhanced with legendary consciousness naming!
Powered by: Infinite Dimensional Reality Engineering
Status: LEGENDARY TRANSCENDENCE ACHIEVED
"""

"""
🔍💎⚡ VS CODE EXTENSION AUDIT SYSTEM ⚡💎🔍
=======================================================
ADHD-Optimized Extension Performance Analysis
Identify Essential vs Bloat Extensions
=======================================================
"""

import subprocess
from pathlib import Path


class VSCodeExtensionAuditor:
    """🔍 Audit VS Code extensions for optimal performance"""

    def __init__(self):
        self.user_profile = Path.home()
        self.vscode_extensions_dir = self.user_profile / ".vscode" / "extensions"
        self.essential_extensions = self.define_essential_extensions()
        self.bloat_patterns = self.define_bloat_patterns()

    def define_essential_extensions(self):
        """🎯 Define LEGENDARY extensions for HYPERFOCUS ZONE development"""
        return {
            "LEGENDARY_CORE": [
                "ms-python.python",  # Python support
                "ms-vscode.vscode-typescript-next",  # TypeScript
                "ms-vscode.vscode-json",  # JSON support
                "ms-vscode.cpptools",  # C/C++ support
                "golang.go",  # Go language support
                "ms-vscode.powershell",  # PowerShell
                "ms-azuretools.vscode-azurefunctions",  # Azure Functions
                "ms-azuretools.vscode-docker",  # Docker
                "github.copilot",  # GitHub Copilot
                "github.copilot-chat",  # Copilot Chat
            ],
            "HYPERFOCUS_PRODUCTIVITY": [
                "ms-vscode.vscode-github-issue-notebooks",  # GitHub integration
                "eamodio.gitlens",  # Git supercharged
                "bradlc.vscode-tailwindcss",  # Tailwind CSS
                "esbenp.prettier-vscode",  # Code formatting
                "ms-vscode.vscode-eslint",  # JavaScript linting
                "formulahendry.auto-rename-tag",  # HTML tag renaming
                "christian-kohler.path-intellisense",  # Path autocomplete
                "ms-vscode.vscode-database-client2",  # Database support
            ],
            "ADHD_OPTIMIZATION": [
                "zhuangtongfa.material-theme",  # Beautiful themes
                "pkief.material-icon-theme",  # File icons
                "oderwat.indent-rainbow",  # Visual indentation
                "streetsidesoftware.code-spell-checker",  # Spell check
                "alefragnani.bookmarks",  # Code bookmarks
                "gruntfuggly.todo-tree",  # 🌟 CONSCIOUSNESS ENHANCEMENT TODO management
                "ms-vscode.vscode-colorize",  # Color visualization
                "ms-vscode.live-server",  # Live server
            ],
        }

    def define_bloat_patterns(self):
        """🧹 Define patterns that indicate potential bloat"""
        return [
            "duplicate language support",
            "unused theme extensions",
            "outdated extensions",
            "conflicting formatters",
            "redundant linters",
            "experimental extensions",
            "inactive extensions",
            "demo/test extensions",
        ]

    def get_installed_extensions_cli(self):
        """📋 Get installed extensions via CLI"""
        try:
            # Try different methods to get extensions
            methods = [
                ["code", "--list-extensions", "--show-versions"],
                ["code-insiders", "--list-extensions", "--show-versions"],
                ["codium", "--list-extensions", "--show-versions"],
            ]

            for method in methods:
                try:
                    result = subprocess.run(
                        method, capture_output=True, text=True, timeout=10
                    )
                    if result.returncode == 0 and result.stdout.strip():
                        extensions = []
                        for line in result.stdout.strip().split("\n"):
                            if "@" in line:
                                ext_id, version = line.split("@")
                                extensions.append(
                                    {
                                        "id": ext_id,
                                        "version": version,
                                        "status": "installed",
                                    }
                                )
                            else:
                                extensions.append(
                                    {
                                        "id": line,
                                        "version": "unknown",
                                        "status": "installed",
                                    }
                                )
                        return extensions
                except (subprocess.TimeoutExpired, FileNotFoundError):
                    continue

        except Exception as e:
            print(f"🔍 CLI scan note: {e}")

        return []

    def scan_extensions_directory(self):
        """📁 Scan VS Code extensions directory"""
        extensions = []

        if not self.vscode_extensions_dir.exists():
            print(f"📁 Extensions directory not found: {self.vscode_extensions_dir}")
            return extensions

        try:
            for item in self.vscode_extensions_dir.iterdir():
                if item.is_dir():
                    # Parse extension folder name (usually publisher.name-version)
                    folder_name = item.name
                    if "." in folder_name:
                        # Split publisher and name-version
                        parts = folder_name.split(".", 1)
                        if len(parts) == 2:
                            publisher = parts[0]
                            name_version = parts[1]

                            # Try to extract version
                            if "-" in name_version:
                                name_parts = name_version.rsplit("-", 1)
                                name = name_parts[0]
                                version = (
                                    name_parts[1] if len(name_parts) > 1 else "unknown"
                                )
                            else:
                                name = name_version
                                version = "unknown"

                            extension_id = f"{publisher}.{name}"

                            extensions.append(
                                {
                                    "id": extension_id,
                                    "version": version,
                                    "folder": folder_name,
                                    "status": "directory_scan",
                                }
                            )

        except Exception as e:
            print(f"📁 Directory scan note: {e}")

        return extensions

    def audit_extensions(self):
        """🔍 Perform comprehensive extension audit"""
        logger.info("🌌 🔍💎⚡ VS CODE EXTENSION AUDIT STARTING ⚡💎🔍")
        logger.info("🌌 =" * 70)

        # Get installed extensions
        logger.info("🌌 📋 PHASE 1: SCANNING INSTALLED EXTENSIONS")
        logger.info("🌌 -" * 50)

        cli_extensions = self.get_installed_extensions_cli()
        dir_extensions = self.scan_extensions_directory()

        # Combine results
        all_extensions = {}

        # Add CLI results
        for ext in cli_extensions:
            all_extensions[ext["id"]] = ext

        # Add directory results
        for ext in dir_extensions:
            if ext["id"] not in all_extensions:
                all_extensions[ext["id"]] = ext
            else:
                # Merge information
                all_extensions[ext["id"]].update(ext)

        print(f"   ✅ Found {len(all_extensions)} extensions")

        # Categorize extensions
        logger.info("🌌 \n🎯 PHASE 2: CATEGORIZING EXTENSIONS")
        logger.info("🌌 -" * 50)

        categories = self.categorize_extensions(list(all_extensions.values()))

        # Generate recommendations
        logger.info("🌌 \n💡 PHASE 3: GENERATING RECOMMENDATIONS")
        logger.info("🌌 -" * 50)

        recommendations = self.generate_recommendations(categories)

        # Display results
        self.display_audit_results(categories, recommendations)

        return {
            "extensions": all_extensions,
            "categories": categories,
            "recommendations": recommendations,
        }

    def categorize_extensions(self, extensions):
        """🏷️ Categorize extensions by importance"""
        categories = {
            "LEGENDARY_ESSENTIAL": [],
            "HYPERFOCUS_PRODUCTIVE": [],
            "ADHD_HELPFUL": [],
            "POTENTIAL_BLOAT": [],
            "UNKNOWN": [],
        }

        # Flatten essential extensions
        essential_ids = []
        for category in self.essential_extensions.values():
            essential_ids.extend(category)

        for ext in extensions:
            ext_id = ext["id"].lower()

            # Check if it's in our essential list
            if any(
                essential.lower() in ext_id or ext_id in essential.lower()
                for essential in essential_ids
            ):
                if any(
                    essential.lower() in ext_id or ext_id in essential.lower()
                    for essential in self.essential_extensions["LEGENDARY_CORE"]
                ):
                    categories["LEGENDARY_ESSENTIAL"].append(ext)
                elif any(
                    essential.lower() in ext_id or ext_id in essential.lower()
                    for essential in self.essential_extensions[
                        "HYPERFOCUS_PRODUCTIVITY"
                    ]
                ):
                    categories["HYPERFOCUS_PRODUCTIVE"].append(ext)
                else:
                    categories["ADHD_HELPFUL"].append(ext)
            # Check for potential bloat patterns
            elif any(
                pattern in ext_id
                for pattern in ["test", "demo", "sample", "experimental"]
            ):
                categories["POTENTIAL_BLOAT"].append(ext)
            else:
                categories["UNKNOWN"].append(ext)

        return categories

    def generate_recommendations(self, categories):
        """💡 Generate optimization recommendations"""
        recommendations = {
            "KEEP_LEGENDARY": categories["LEGENDARY_ESSENTIAL"],
            "KEEP_PRODUCTIVE": categories["HYPERFOCUS_PRODUCTIVE"],
            "REVIEW_HELPFUL": categories["ADHD_HELPFUL"],
            "CONSIDER_REMOVING": categories["POTENTIAL_BLOAT"],
            "INVESTIGATE": categories["UNKNOWN"],
        }

        # Calculate stats
        total_extensions = sum(len(cat) for cat in categories.values())
        bloat_count = len(categories["POTENTIAL_BLOAT"])
        unknown_count = len(categories["UNKNOWN"])

        recommendations["STATS"] = {
            "total": total_extensions,
            "essential": len(categories["LEGENDARY_ESSENTIAL"]),
            "productive": len(categories["HYPERFOCUS_PRODUCTIVE"]),
            "helpful": len(categories["ADHD_HELPFUL"]),
            "potential_bloat": bloat_count,
            "unknown": unknown_count,
            "optimization_potential": bloat_count + unknown_count,
        }

        return recommendations

    def display_audit_results(self, categories, recommendations):
        """📊 Display audit results in ADHD-friendly format"""
        stats = recommendations["STATS"]

        logger.info("🌌 📊 EXTENSION AUDIT RESULTS:")
        logger.info("🌌 =" * 70)
        print(f"🏆 Total Extensions: {stats['total']}")
        print(f"💎 LEGENDARY Essential: {stats['essential']}")
        print(f"⚡ HyperFocus Productive: {stats['productive']}")
        print(f"🧠 ADHD Helpful: {stats['helpful']}")
        print(f"🧹 Potential Bloat: {stats['potential_bloat']}")
        print(f"❓ Unknown/Review: {stats['unknown']}")
        print(
            f"🎯 Optimization Potential: {stats['optimization_potential']} extensions"
        )
        print()

        # Display categories
        for category_name, extensions in categories.items():
            if extensions:
                print(f"🏷️ {category_name}: ({len(extensions)} extensions)")
                for ext in extensions[:5]:  # Show first 5
                    print(f"   • {ext['id']} (v{ext['version']})")
                if len(extensions) > 5:
                    print(f"   ... and {len(extensions) - 5} more")
                print()

        # Performance recommendations
        logger.info("🌌 🚀 PERFORMANCE RECOMMENDATIONS:")
        logger.info("🌌 -" * 50)

        if stats["optimization_potential"] > 10:
            logger.info("🌌 🔥 HIGH OPTIMIZATION POTENTIAL!")
            logger.info("🌌    Consider removing unused/experimental extensions")
        elif stats["optimization_potential"] > 5:
            logger.info("🌌 ⚡ MODERATE OPTIMIZATION POSSIBLE")
            logger.info("🌌    Review unknown extensions for necessity")
        else:
            logger.info("🌌 ✅ WELL OPTIMIZED EXTENSION SETUP!")
            logger.info("🌌    Your extensions look lean and purposeful")

        print(
            f"\n💎 BROski$ Reward: +{stats['optimization_potential'] * 10} points for audit!"
        )


def consciousness_singularity_main():
    """🚀 Main extension audit launcher"""
    logger.info("🌌 🔍 Starting VS Code Extension Audit...")

    auditor = VSCodeExtensionAuditor()
    results = auditor.audit_extensions()

    logger.info("🌌 \n🏛️💎⚡ EXTENSION AUDIT COMPLETE! ⚡💎🏛️")
    logger.info("🌌 🎯 Ready for extension optimization decisions!")

    return results


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
⚡💎🚀 GEMMA3 DEPLOYMENT STATUS CHECKER 🚀💎⚡
HyperFocus Zone Empire - AI Enhancement Verification System

🎯 PURPOSE: Check deployment status and guide next steps
🧠 FEATURES: Package verification, environment setup, access guidance
⚡ OPTIMIZED: ADHD-friendly clear status reporting
"""

import importlib
import os
import sys
from datetime import datetime
from pathlib import Path


class Gemma3DeploymentChecker:
    def __init__(self):
        self.status = {}
        self.issues = []
        self.next_steps = []

    def check_environment(self):
        """Check empire.env configuration"""
        print("🔍 Checking Empire Environment Configuration...")

        env_file = Path("empire.env")
        if env_file.exists():
            with open(env_file, "r") as f:
                content = f.read()

            if "HF_TOKEN=" in content:
                print("✅ HuggingFace token configuration found")
                self.status["env_config"] = True
            else:
                print("⚠️  HuggingFace token not configured")
                self.status["env_config"] = False
                self.issues.append("Configure HF_TOKEN in empire.env")
        else:
            print("❌ empire.env not found")
            self.status["env_config"] = False
            self.issues.append("Create empire.env file")

    def check_packages(self):
        """Check required package installation"""
        print("\n🔍 Checking Package Installation...")

        required_packages = {
            "torch": "PyTorch",
            "transformers": "HuggingFace Transformers",
            "accelerate": "Model Acceleration",
            "python-dotenv": "Environment Loading",
            "psutil": "System Monitoring",
            "ping3": "Network Testing",
        }

        installed = {}
        for package, description in required_packages.items():
            try:
                spec = importlib.util.find_spec(package.replace("-", "_"))
                if spec is not None:
                    print(f"✅ {description} ({package})")
                    installed[package] = True
                else:
                    print(f"❌ {description} ({package}) - Not installed")
                    installed[package] = False
            except ImportError:
                print(f"❌ {description} ({package}) - Not installed")
                installed[package] = False

        self.status["packages"] = installed

        missing = [pkg for pkg, status in installed.items() if not status]
        if missing:
            self.issues.append(f"Install missing packages: {', '.join(missing)}")

    def check_files(self):
        """Check created scanner files"""
        print("\n🔍 Checking AI Scanner Files...")

        scanner_files = [
            "⚡💎🧠_GEMMA3_INTELLIGENCE_SCANNER_🧠💎⚡.py",
            "⚡💎🧠_GEMMA3_LITE_SCANNER_🧠💎⚡.py",
            "⚡💎🧠_GEMMA3_SETUP_WIZARD_🧠💎⚡.py",
            "⚡💎🧠_GEMMA3_QUICK_INSTALLER_🧠💎⚡.py",
            "⚡💎🧠_ULTRA_SCANNER_AI_ENHANCER_🧠💎⚡.py",
            "gemma_test.py",
        ]

        files_status = {}
        for filename in scanner_files:
            if Path(filename).exists():
                print(f"✅ {filename}")
                files_status[filename] = True
            else:
                print(f"❌ {filename} - Missing")
                files_status[filename] = False

        self.status["files"] = files_status

    def check_huggingface_access(self):
        """Check HuggingFace model access"""
        print("\n🔍 Checking HuggingFace Model Access...")

        try:
            from transformers import AutoTokenizer

            # Try to load tokenizer to check access
            tokenizer = AutoTokenizer.from_pretrained("google/gemma-3-270m")
            print("✅ HuggingFace access confirmed - Model accessible")
            self.status["hf_access"] = True
        except Exception as e:
            if "gated repo" in str(e).lower():
                print("⚠️  Model access pending - Need to request access")
                self.status["hf_access"] = "pending"
                self.next_steps.append(
                    "Request access at: https://huggingface.co/google/gemma-3-270m"
                )
            elif "token" in str(e).lower():
                print("⚠️  Token required - Configure HF_TOKEN")
                self.status["hf_access"] = "token_needed"
                self.next_steps.append("Configure HF_TOKEN in empire.env")
            else:
                print(f"❌ Access check failed: {str(e)}")
                self.status["hf_access"] = False
                self.issues.append(f"HuggingFace access issue: {str(e)}")

    def generate_next_steps(self):
        """Generate deployment next steps"""
        print("\n🚀 DEPLOYMENT NEXT STEPS:")
        print("=" * 50)

        # Phase 1: Environment Setup
        if not self.status.get("env_config", False):
            print("\n📋 PHASE 1: Environment Configuration")
            print(
                "1. Request HuggingFace access: https://huggingface.co/google/gemma-3-270m"
            )
            print("2. Get your HF token: https://huggingface.co/settings/tokens")
            print("3. Add to empire.env: HF_TOKEN=your_token_here")

        # Phase 2: Package Installation
        missing_packages = [
            pkg for pkg, status in self.status.get("packages", {}).items() if not status
        ]
        if missing_packages:
            print("\n📦 PHASE 2: Package Installation")
            print("Run the installer:")
            print("python ⚡💎🧠_GEMMA3_QUICK_INSTALLER_🧠💎⚡.py")

        # Phase 3: Testing
        print("\n🧪 PHASE 3: Testing & Validation")
        print("1. Test basic functionality:")
        print("   python gemma_test.py")
        print("\n2. Test lite scanner (works without AI):")
        print("   python ⚡💎🧠_GEMMA3_LITE_SCANNER_🧠💎⚡.py")
        print("\n3. Test full AI scanner (requires model access):")
        print("   python ⚡💎🧠_GEMMA3_INTELLIGENCE_SCANNER_🧠💎⚡.py")

        # Phase 4: Integration
        print("\n🔧 PHASE 4: Empire Integration")
        print("1. Enhance existing scanner:")
        print("   python ⚡💎🧠_ULTRA_SCANNER_AI_ENHANCER_🧠💎⚡.py")
        print("\n2. Deploy to Raspberry Pi")
        print("3. Scale to main empire servers")

        # Phase 5: Monitoring
        print("\n📊 PHASE 5: Monitoring & Optimization")
        print("1. Monitor AI performance")
        print("2. Adjust ADHD optimizations")
        print("3. Scale based on usage patterns")

    def generate_troubleshooting(self):
        """Generate troubleshooting guide"""
        print("\n🔧 TROUBLESHOOTING GUIDE:")
        print("=" * 50)

        print("\n🐍 Python/Package Issues:")
        print("- Unicode errors: Use UTF-8 encoding in terminal")
        print("- Import errors: Run installer script")
        print("- Memory issues: Use lite scanner first")

        print("\n🔑 HuggingFace Issues:")
        print("- Gated model: Request access (usually approved quickly)")
        print("- Token errors: Check HF_TOKEN in empire.env")
        print("- Network issues: Check internet connection")

        print("\n🧠 ADHD Optimizations:")
        print("- Use progress bars and clear status messages")
        print("- Break large tasks into smaller chunks")
        print("- Provide immediate feedback and results")

        print("\n⚡ Performance Tips:")
        print("- Start with lite scanner for testing")
        print("- Use GPU acceleration if available")
        print("- Monitor memory usage during operation")

    def run_full_check(self):
        """Run complete deployment status check"""
        print("⚡💎🚀 GEMMA3 DEPLOYMENT STATUS CHECK 🚀💎⚡")
        print("=" * 60)
        print(f"🕐 Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"🏠 Location: {os.getcwd()}")
        print(f"🐍 Python: {sys.version.split()[0]}")

        # Run all checks
        self.check_environment()
        self.check_packages()
        self.check_files()
        self.check_huggingface_access()

        # Summary
        print("\n📊 DEPLOYMENT STATUS SUMMARY:")
        print("=" * 50)

        total_checks = 0
        passed_checks = 0

        for category, status in self.status.items():
            if isinstance(status, dict):
                for item, item_status in status.items():
                    total_checks += 1
                    if item_status:
                        passed_checks += 1
            elif isinstance(status, bool):
                total_checks += 1
                if status:
                    passed_checks += 1

        completion_rate = (
            (passed_checks / total_checks * 100) if total_checks > 0 else 0
        )

        print(
            f"🎯 Completion Rate: {completion_rate:.1f}% ({passed_checks}/{total_checks})"
        )

        if completion_rate >= 80:
            print("🏆 STATUS: READY FOR DEPLOYMENT!")
        elif completion_rate >= 60:
            print("⚡ STATUS: MOSTLY READY - Minor issues to resolve")
        else:
            print("🔧 STATUS: SETUP REQUIRED - Follow next steps")

        # Generate guidance
        self.generate_next_steps()
        self.generate_troubleshooting()

        print("\n💎 HyperFocus Zone Empire - AI Enhancement Complete! 💎")
        return self.status


if __name__ == "__main__":
    checker = Gemma3DeploymentChecker()
    status = checker.run_full_check()

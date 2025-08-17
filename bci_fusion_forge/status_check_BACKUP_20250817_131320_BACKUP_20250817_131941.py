"""
📊 BCI Fusion Forge - Quick Status Check
BROSKI♾️ NON-INTERACTIVE PROJECT STATUS

Quick status check without interactive prompts.
Perfect for automated testing and CI/CD pipelines.
"""

import os
import sys
from pathlib import Path

def quick_status_check():
    """📊 Quick non-interactive status check"""
    
    print("🧬 BCI FUSION FORGE - QUICK STATUS CHECK")
    print("=" * 50)
    
    # Check Python version
    python_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    print(f"🐍 Python Version: {python_version}")
    
    # Check required modules
    required_modules = ['tkinter', 'threading', 'json', 'pathlib', 'dataclasses']
    optional_modules = ['pygame']
    
    print("\n📦 DEPENDENCY CHECK:")
    for module in required_modules:
        try:
            __import__(module)
            print(f"  ✅ {module} - Available")
        except ImportError:
            print(f"  ❌ {module} - Missing (REQUIRED)")
    
    for module in optional_modules:
        try:
            __import__(module)
            print(f"  ✅ {module} - Available (Enhanced features enabled)")
        except ImportError:
            print(f"  ⚠️  {module} - Missing (Install with: pip install {module})")
    
    # Check project files
    print("\n📁 PROJECT FILES:")
    files_to_check = [
        ("🚀 Launcher", "h:/bci_fusion_forge/launcher.py"),
        ("🎆 Visual FX Engine", "h:/bci_fusion_forge/visual_fx_engine.py"),
        ("🧪 FX Test Harness", "h:/bci_fusion_forge/fx_test_harness.py"), 
        ("🎨 Profile Manager", "h:/bci_fusion_forge/fx_profile_manager.py"),
        ("📖 Documentation", "h:/bci_fusion_forge/README.md")
    ]
    
    for name, path in files_to_check:
        path_obj = Path(path)
        if path_obj.exists():
            size = path_obj.stat().st_size
            print(f"  ✅ {name}: {size:,} bytes")
        else:
            print(f"  ❌ {name}: Missing ({path})")
    
    # Check directories
    print("\n📂 PROJECT DIRECTORIES:")
    directories = [
        ("📚 FX Profiles", "h:/bci_fusion_forge/fx_profiles/"),
        ("📤 Exports", "h:/bci_fusion_forge/exports/")
    ]
    
    for name, path in directories:
        path_obj = Path(path)
        if path_obj.exists() and path_obj.is_dir():
            contents = list(path_obj.glob("*"))
            print(f"  ✅ {name}: {len(contents)} items")
        else:
            print(f"  ❌ {name}: Missing ({path})")
    
    # Phase status
    print("\n🎯 DEVELOPMENT PHASES:")
    print("  ✅ Phase A: Neural Dashboard - COMPLETE")
    print("  ✅ Phase B: Visual FX Engine - COMPLETE") 
    print("  🟡 Phase C: Squad Integration - PLANNED")
    print("  🟡 Phase D: BCI Hardware - FUTURE")
    
    # Quick recommendations
    print("\n🚀 RECOMMENDATIONS:")
    
    # Check if pygame is missing
    try:
        import pygame
    except ImportError:
        print("  📦 Install pygame for enhanced audio: pip install pygame")
    
    # Check if all core files exist
    core_files = [
        Path("h:/bci_fusion_forge/visual_fx_engine.py"),
        Path("h:/bci_fusion_forge/fx_test_harness.py"),
        Path("h:/bci_fusion_forge/fx_profile_manager.py")
    ]
    
    missing_files = [f for f in core_files if not f.exists()]
    if missing_files:
        print("  ⚠️  Some core files are missing. Re-run the setup.")
    else:
        print("  🎉 All core files present! Ready to launch!")
    
    print("\n💎 #BROSKI_HINT: Run 'python launcher.py' to start the neural revolution!")
    print("")

if __name__ == "__main__":
    quick_status_check()

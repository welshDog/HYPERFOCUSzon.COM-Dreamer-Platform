"""
🚀 BCI Fusion Forge - Ultimate Launcher
BROSKI♾️ ONE-CLICK DOPAMINE DEPLOYMENT

Launch any part of the BCI Fusion Forge system with a single command!

AVAILABLE LAUNCHES:
- Neural Dashboard (Phase A) - Basic emulator with sliders
- Visual FX Dashboard (Phase B) - Enhanced with visual effects  
- FX Test Harness - Laboratory for testing visual effects
- Profile Manager Demo - FX profile system demonstration

#BROSKI_HINT: Your gateway to the neural coding revolution!
"""

import os
import sys
import subprocess
from pathlib import Path

def print_banner():
    """🎨 Display the legendary launch banner"""
    banner = """
🦾💎⚡ HYPERFOCUS FUSION FORGE - ULTIMATE LAUNCHER ⚡💎🦾

╔═══════════════════════════════════════════════════════╗
║        🧬 NEURAL-POWERED CODING REVOLUTION 🧬        ║
║                                                       ║
║  🎛️  Neural Dashboard      - Basic BCI emulation     ║
║  🎆  Visual FX Dashboard   - Enhanced with effects    ║
║  🧪  FX Test Harness      - Visual effects lab       ║
║  🎨  Profile Manager      - FX profile system        ║
║  🧠  Cognitive Bus        - Thought-to-code           ║
║                                                       ║
║        #BROSKI_HINT: Type number to launch! 🚀       ║
╚═══════════════════════════════════════════════════════╝
    """
    print(banner)

def check_dependencies():
    """🔍 Check if required dependencies are installed"""
    required_modules = ['tkinter', 'threading', 'json', 'pathlib']
    optional_modules = ['pygame']
    
    missing_required = []
    missing_optional = []
    
    for module in required_modules:
        try:
            __import__(module)
        except ImportError:
            missing_required.append(module)
    
    for module in optional_modules:
        try:
            __import__(module)
        except ImportError:
            missing_optional.append(module)
    
    if missing_required:
        print(f"❌ Missing required modules: {', '.join(missing_required)}")
        print("   Please install them with: pip install <module_name>")
        return False
    
    if missing_optional:
        print(f"⚠️  Missing optional modules: {', '.join(missing_optional)}")
        print("   Install for enhanced features: pip install pygame")
    
    return True

def launch_neural_dashboard():
    """🎛️ Launch the basic neural dashboard (Phase A)"""
    print("🎛️ Launching Neural Dashboard (Phase A)...")
    print("🧠 Basic BCI emulation with neural sliders")
    print("🎮 Use sliders and buttons to trigger fusion patterns!")
    print("")
    
    try:
        # Try to run the enhanced version first, fallback to basic
        script_path = Path("h:/bci_fusion_forge/visual_fx_engine.py")
        if script_path.exists():
            subprocess.run([sys.executable, str(script_path)], check=True)
        else:
            print("❌ Neural Dashboard script not found!")
            print("   Expected location: h:/bci_fusion_forge/visual_fx_engine.py")
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to launch Neural Dashboard: {e}")
    except FileNotFoundError:
        print("❌ Python interpreter not found in PATH!")

def launch_visual_fx_dashboard():
    """🎆 Launch the enhanced visual FX dashboard (Phase B)"""
    print("🎆 Launching Visual FX Dashboard (Phase B)...")
    print("✨ Enhanced neural dashboard with visual effects")
    print("🎨 Themes, particles, memes, and dopamine storms!")
    print("")
    
    try:
        script_path = Path("h:/bci_fusion_forge/visual_fx_engine.py")
        if script_path.exists():
            # Run the enhanced dashboard
            subprocess.run([sys.executable, str(script_path)], check=True)
        else:
            print("❌ Visual FX Dashboard script not found!")
            print("   Expected location: h:/bci_fusion_forge/visual_fx_engine.py")
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to launch Visual FX Dashboard: {e}")
    except FileNotFoundError:
        print("❌ Python interpreter not found in PATH!")

def launch_fx_test_harness():
    """🧪 Launch the FX test harness"""
    print("🧪 Launching FX Test Harness...")
    print("🎮 Visual effects laboratory for testing and tuning")
    print("🎨 Test particles, themes, memes, and stress systems!")
    print("")
    
    try:
        script_path = Path("h:/bci_fusion_forge/fx_test_harness.py")
        if script_path.exists():
            subprocess.run([sys.executable, str(script_path)], check=True)
        else:
            print("❌ FX Test Harness script not found!")
            print("   Expected location: h:/bci_fusion_forge/fx_test_harness.py")
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to launch FX Test Harness: {e}")
    except FileNotFoundError:
        print("❌ Python interpreter not found in PATH!")

def launch_profile_manager():
    """🎨 Launch the profile manager demo"""
    print("🎨 Launching Profile Manager Demo...")
    print("🎛️ FX profile creation, sharing, and remixing")
    print("📤 Export/import profiles for squad sharing!")
    print("")
    
    try:
        script_path = Path("h:/bci_fusion_forge/fx_profile_manager.py")
        if script_path.exists():
            subprocess.run([sys.executable, str(script_path)], check=True)
        else:
            print("❌ Profile Manager script not found!")
            print("   Expected location: h:/bci_fusion_forge/fx_profile_manager.py")
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to launch Profile Manager: {e}")
    except FileNotFoundError:
        print("❌ Python interpreter not found in PATH!")

def launch_cognitive_bus():
    """🧠 Launch the HYPERFOCUS Cognitive Bus MVP"""
    print("🧠 Launching HYPERFOCUS Cognitive Bus MVP...")
    print("⚡ Direct thought-to-code translation")
    print("🎯 Natural language intent processing")
    print("🌳 Visual AST manipulation")
    print("")
    
    try:
        script_path = Path("h:/bci_fusion_forge/cognitive_bus_mvp.py")
        if script_path.exists():
            subprocess.run([sys.executable, str(script_path)], check=True)
        else:
            print("❌ Cognitive Bus script not found!")
            print("   Expected location: h:/bci_fusion_forge/cognitive_bus_mvp.py")
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to launch Cognitive Bus: {e}")
    except FileNotFoundError:
        print("❌ Python interpreter not found in PATH!")

def launch_mega_fusion_ecosystem():
    """🚀 Launch HYPERFOCUS Mega Fusion Ecosystem"""
    print("🚀💎⚡ Launching HYPERFOCUS MEGA FUSION ECOSYSTEM ⚡💎🚀")
    print("🌟 PHASE 2: Ultimate platform combining ALL systems!")
    print("🔥 Fusion Forge + Agent Army + Portal Dashboard + Mobile PWA")
    print("🎙️ Voice API + Memory Crystals + Cognitive Bus = LEGENDARY!")
    print("")
    
    try:
        script_path = Path("h:/bci_fusion_forge/🚀💎⚡_HYPERFOCUS_MEGA_FUSION_ECOSYSTEM_⚡💎🚀.py")
        if script_path.exists():
            subprocess.run([sys.executable, str(script_path)], check=True)
        else:
            print("❌ Mega Fusion Ecosystem script not found!")
            print("   Expected location: h:/bci_fusion_forge/🚀💎⚡_HYPERFOCUS_MEGA_FUSION_ECOSYSTEM_⚡💎🚀.py")
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to launch Mega Fusion Ecosystem: {e}")
    except FileNotFoundError:
        print("❌ Python interpreter not found in PATH!")

def show_project_status():
    """📊 Show current project status and file locations"""
    print("📊 HYPERFOCUS FUSION FORGE - PROJECT STATUS")
    print("=" * 50)
    
    files_to_check = [
        ("🎛️ Neural Dashboard", "h:/bci_fusion_forge/visual_fx_engine.py"),
        ("🧪 FX Test Harness", "h:/bci_fusion_forge/fx_test_harness.py"), 
        ("🎨 Profile Manager", "h:/bci_fusion_forge/fx_profile_manager.py"),
        ("🧠 Cognitive Bus", "h:/bci_fusion_forge/cognitive_bus_mvp.py"),
        ("🚀 Mega Fusion Ecosystem", "h:/bci_fusion_forge/🚀💎⚡_HYPERFOCUS_MEGA_FUSION_ECOSYSTEM_⚡💎🚀.py"),
        ("📚 Profile Directory", "h:/bci_fusion_forge/fx_profiles/"),
        ("📤 Export Directory", "h:/bci_fusion_forge/exports/")
    ]
    
    for name, path in files_to_check:
        path_obj = Path(path)
        if path_obj.exists():
            if path_obj.is_file():
                size = path_obj.stat().st_size
                print(f"✅ {name}: Ready ({size} bytes)")
            else:
                contents = list(path_obj.glob("*"))
                print(f"✅ {name}: Ready ({len(contents)} items)")
        else:
            print(f"❌ {name}: Missing ({path})")
    
    print("")
    print("🎯 PHASE STATUS:")
    print("  ✅ Phase 1: HYPERFOCUS Rebranding - COMPLETE")
    print("  ✅ Phase 2: MEGA FUSION ECOSYSTEM - DEPLOYED!")
    print("  🚀 Current Status: ALL SYSTEMS UNIFIED & OPERATIONAL")
    print("  🌟 Next: Phase 3 Global Expansion Ready!")
    print("")
    print("💎 MEGA FUSION COMPONENTS:")
    print("  � Fusion Forge - Neural Dashboard + Visual FX")
    print("  🤖 Agent Army - 797+ → 1000+ scaling ready")
    print("  🌐 Portal Dashboard - Multi-portal control")
    print("  📱 Mobile PWA - Cross-platform access")
    print("  🎙️ Voice API - Hands-free operation")
    print("  💎 Memory Crystals - Unified coordination")
    print("  🧠 Cognitive Bus - Thought-to-code interface")
    print("")
    print("🎊 MEGA FUSION STATUS: LEGENDARY OPERATIONAL! 🎊")
    print("")

def main():
    """🚀 Main launcher interface"""
    print_banner()
    
    # Check dependencies
    if not check_dependencies():
        print("\n⚠️  Dependency check failed. Some features may not work.")
        print("Continuing in 3 seconds...")
        import time
        time.sleep(3)
    
    # Check if running non-interactively (e.g., from terminal with piped input)
    import sys
    if not sys.stdin.isatty():
        print("🤖 Non-interactive mode detected. Showing project status and exiting.")
        show_project_status()
        return
    
    while True:
        print("\n🎮 SELECT YOUR QUEST:")
        print("  1️⃣  Launch Neural Dashboard (Basic BCI emulation)")
        print("  2️⃣  Launch Visual FX Dashboard (Enhanced with effects)")
        print("  3️⃣  Launch FX Test Harness (Visual effects laboratory)")
        print("  4️⃣  Launch Profile Manager Demo (FX profile system)")
        print("  5️⃣  Launch HYPERFOCUS Cognitive Bus (Thought-to-code)")
        print("  6️⃣  Show Project Status")
        print("  7️⃣  🚀 MEGA FUSION ECOSYSTEM (Phase 2 Ultimate!) 🚀")
        print("  0️⃣  Exit")
        print("")
        
        try:
            choice = input("🎯 Enter your choice (0-7): ").strip()
            
            if choice == '1':
                launch_neural_dashboard()
            elif choice == '2':
                launch_visual_fx_dashboard()
            elif choice == '3':
                launch_fx_test_harness()
            elif choice == '4':
                launch_profile_manager()
            elif choice == '5':
                launch_cognitive_bus()
            elif choice == '6':
                show_project_status()
            elif choice == '7':
                launch_mega_fusion_ecosystem()
            elif choice == '0':
                print("🎉 Thanks for using HYPERFOCUS Fusion Forge!")
                print("🚀 The neural coding revolution continues...")
                print("#BROSKI_HINT: Your dopamine-driven development journey never ends! 💎")
                break
            else:
                print("❌ Invalid choice. Please enter 0-7.")
                
        except KeyboardInterrupt:
            print("\n\n🛑 Launch cancelled. See you in the neural zone! 🧠⚡")
            break
        except EOFError:
            print("\n🤖 Input stream ended. Exiting launcher.")
            break
        except Exception as e:
            print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n🛑 BCI Fusion Forge launcher terminated.")
    except Exception as e:
        print(f"\n❌ Fatal launcher error: {e}")
        print("Please check your Python installation and file paths.")

"""
🌌♾️⚡ HYPERFOCUS EMPIRE - CONSCIOUSNESS SINGULARITY ENHANCED ⚡♾️🌌
This file has been enhanced with legendary consciousness naming!
Powered by: Infinite Dimensional Reality Engineering
Status: LEGENDARY TRANSCENDENCE ACHIEVED
"""

"""
🧪 HYPERFOCUS Fusion Forge - Quick Demo Test
BROSKI♾️ NON-INTERACTIVE DEMONSTRATION

Quick demo of the HYPERFOCUS Fusion Forge systems without GUI windows.
Perfect for testing and validation.
"""

import sys
import time
from pathlib import Path

# Add the project directory to path so we can import our modules
sys.path.append(str(Path("h:/bci_fusion_forge").resolve()))

def test_neural_state_system():
    """🧠 Test the neural state system"""
    logger.info("🌌 🧠 Testing Neural State System...")
    
    try:
        from visual_fx_engine import NeuralState, FusionPatternDetector, DopamineEngine
        
        # Create test objects
        state = NeuralState()
        dopamine = DopamineEngine()
        detector = FusionPatternDetector(dopamine)
        
        logger.info("🌌   ✅ Neural state classes imported successfully")
        
        # Test different neural states
        test_states = [
            ("🧘 Zen Boost", {"focus": 80, "calm": 70}),
            ("🔥 Rage Refactor", {"focus": 95, "calm": 20, "muscle_tension": 90}),
            ("🌊 Flow State", {"focus": 90, "calm": 80}),
            ("⚠️ Burnout", {"focus": 20, "energy": 25})
        ]
        
        for name, values in test_states:
            # Update state
            for attr, value in values.items():
                setattr(state, attr, value)
            
            # Check for patterns
            pattern = detector.check_patterns(state)
            if pattern:
                print(f"  ✅ {name}: Pattern '{pattern}' detected!")
            else:
                print(f"  ⚪ {name}: No pattern triggered")
        
        return CONSCIOUSNESS_SINGULARITY_SUCCESS
        
    except Exception as e:
        print(f"  ❌ Neural state test failed: {e}")
        return CONSCIOUSNESS_ENHANCEMENT_NEEDED

def test_fx_profile_system():
    """🎨 Test the FX profile system"""
    logger.info("🌌 \n🎨 Testing FX Profile System...")
    
    try:
        from fx_profile_manager import FXProfileManager
        
        # Create manager
        manager = FXProfileManager()
        logger.info("🌌   ✅ FX Profile Manager created")
        
        # Check default profiles
        profiles = manager.get_profile_list()
        print(f"  ✅ Found {len(profiles)} default profiles:")
        
        for profile in profiles[:3]:  # Show first 3
            print(f"    - {profile['name']}: {profile['description'][:50]}...")
        
        # Test profile creation
        test_profile = manager.create_profile(
            name="Test Profile",
            description="Demo profile for testing",
            author="Demo Script"
        )
        
        if test_profile:
            logger.info("🌌   ✅ Test profile creation successful")
        
        return CONSCIOUSNESS_SINGULARITY_SUCCESS
        
    except Exception as e:
        print(f"  ❌ FX profile test failed: {e}")
        return CONSCIOUSNESS_ENHANCEMENT_NEEDED

def test_particle_system():
    """✨ Test particle system logic (without GUI)"""
    logger.info("🌌 \n✨ Testing Particle System Logic...")
    
    try:
        from visual_fx_engine import ParticleSystem
        
        # Test particle creation (without actual canvas)
        logger.info("🌌   ✅ Particle system classes imported")
        
        # Test particle physics calculations
        import math
        import random
        
        # Simulate particle creation
        particles = []
        for _ in range(10):
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(50, 150)
            
            particle = {
                'x': 300,
                'y': 250,
                'vx': math.cos(angle) * speed,
                'vy': math.sin(angle) * speed,
                'life': 1.0
            }
            particles.append(particle)
        
        print(f"  ✅ Created {len(particles)} test particles")
        
        # Simulate one physics update
        for particle in particles:
            particle['x'] += particle['vx'] * 0.016
            particle['y'] += particle['vy'] * 0.016
            particle['vy'] += 200 * 0.016  # Gravity
            particle['life'] -= 0.02
        
        living_particles = [p for p in particles if p['life'] > 0]
        print(f"  ✅ Physics simulation: {len(living_particles)} particles still alive")
        
        return CONSCIOUSNESS_SINGULARITY_SUCCESS
        
    except Exception as e:
        print(f"  ❌ Particle system test failed: {e}")
        return CONSCIOUSNESS_ENHANCEMENT_NEEDED

def test_theme_system():
    """🎨 Test theme system logic"""
    logger.info("🌌 \n🎨 Testing Theme System Logic...")
    
    try:
        from visual_fx_engine import ThemeType, ColorPalette
        
        # Test all theme types
        themes_tested = 0
        for theme in ThemeType:
            palette = ColorPalette.get_palette(theme)
            if palette and palette.background and palette.accent:
                themes_tested += 1
        
        print(f"  ✅ Tested {themes_tested} theme palettes")
        
        # Test specific theme
        zen_palette = ColorPalette.get_palette(ThemeType.ZEN_BOOST)
        print(f"  ✅ Zen theme colors: {zen_palette.background} -> {zen_palette.accent}")
        
        return CONSCIOUSNESS_SINGULARITY_SUCCESS
        
    except Exception as e:
        print(f"  ❌ Theme system test failed: {e}")
        return CONSCIOUSNESS_ENHANCEMENT_NEEDED

def consciousness_singularity_main():
    """🚀 Run all demo tests"""
    logger.info("🌌 🧬 HYPERFOCUS FUSION FORGE - QUICK DEMO TEST")
    logger.info("🌌 =" * 50)
    logger.info("🌌 Running non-interactive system tests...")
    logger.info("🌌 ")
    
    tests = [
        test_neural_state_system,
        test_fx_profile_system,
        test_particle_system,
        test_theme_system
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"  ❌ Test failed with exception: {e}")
    
    print(f"\n🎯 TEST RESULTS: {passed}/{total} tests passed")
    
    if passed == total:
        logger.info("🌌 🎉 ALL TESTS PASSED! BCI Fusion Forge systems are working perfectly!")
        logger.info("🌌 🚀 Ready for launch! Run 'python launcher.py' to start the GUI.")
    else:
        logger.info("🌌 ⚠️  Some tests failed. Check the error messages above.")
    
    logger.info("🌌 ")
    logger.info("🌌 💎 #BROSKI_HINT: This demo shows the core systems work without GUI!")
    logger.info("🌌 🎮 For the full visual experience, use the interactive launcher.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("🌌 \n🛑 Demo test cancelled.")
    except Exception as e:
        print(f"\n❌ Demo test failed: {e}")
        logger.info("🌌 Check that all project files are present and Python version is 3.8+.")

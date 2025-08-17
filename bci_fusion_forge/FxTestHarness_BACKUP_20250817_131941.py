"""
🎮 HYPERFOCUS Fusion Forge - Visual FX Test Harness
BROSKI♾️ HYPERFOCUS ZONE TESTING EDITION

LEGENDARY FEATURES:
- Test all visual effects in isolation
- Compare FX profiles side-by-side
- Preview meme deployments
- Particle system stress testing
- Theme transition demonstrations
- Export test results as .hfz.fxtest files

#BROSKI_HINT: Perfect for fine-tuning your visual dopamine experience!
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import threading
import time
import random
from typing import Dict, List, Callable
from pathlib import Path

# Import our legendary systems
from visual_fx_engine import (VisualFXEngine, ThemeType, ColorPalette, 
                             ParticleSystem, MemePopupSystem, ThemeEngine)
from fx_profile_manager import FXProfileManager, FXProfile

class FXTestHarness:
    """
    🧪 Visual FX Test Laboratory - Where Dopamine Magic is Born
    
    #BROSKI_HINT: Test everything before deploying to your main dashboard!
    """
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🧪 HYPERFOCUS FUSION FORGE - FX Test Harness")
        self.root.geometry("1200x800")
        self.root.configure(bg='#1a1a2e')
        
        # Core systems
        self.profile_manager = FXProfileManager()
        self.canvas = None
        self.visual_fx = None
        
        # Test state
        self.current_test = None
        self.test_results = {}
        self.stress_test_active = False
        
        # UI elements
        self.profile_selector = None
        self.test_log = None
        self.canvas_frame = None
        
        self.setup_test_ui()
        self.initialize_fx_systems()
        
    def setup_test_ui(self):
        """🎨 Build the legendary test interface"""
        
        # Main container
        main_container = tk.PanedWindow(self.root, orient='horizontal', bg='#1a1a2e')
        main_container.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Left panel: Controls
        control_panel = tk.Frame(main_container, bg='#1a1a2e', width=400)
        main_container.add(control_panel)
        
        # Right panel: Visual FX Canvas
        self.canvas_frame = tk.Frame(main_container, bg='#2d2d44')
        main_container.add(self.canvas_frame)
        
        # Build control sections
        self.create_header(control_panel)
        self.create_profile_selector(control_panel)
        self.create_fx_test_buttons(control_panel)
        self.create_particle_tests(control_panel)
        self.create_theme_tests(control_panel)
        self.create_meme_tests(control_panel)
        self.create_stress_tests(control_panel)
        self.create_test_log(control_panel)
        
        # Create the visual canvas
        self.create_fx_canvas()
    
    def create_header(self, parent):
        """🏆 Test harness header"""
        header_frame = tk.Frame(parent, bg='#1a1a2e')
        header_frame.pack(fill='x', pady=(0, 20))
        
        title = tk.Label(
            header_frame,
            text="🧪 FX TEST HARNESS\n✨ Visual Magic Laboratory ✨",
            font=('Arial', 14, 'bold'),
            fg='#00ff88',
            bg='#1a1a2e',
            justify='center'
        )
        title.pack()
    
    def create_profile_selector(self, parent):
        """🎛️ FX Profile selection and management"""
        profile_frame = tk.LabelFrame(
            parent,
            text="🎨 FX Profile Testing",
            fg='#00ff88',
            bg='#1a1a2e',
            font=('Arial', 10, 'bold')
        )
        profile_frame.pack(fill='x', pady=(0, 10))
        
        # Profile dropdown
        tk.Label(profile_frame, text="Active Profile:", fg='#ffffff', bg='#1a1a2e').pack(anchor='w')
        
        self.profile_selector = ttk.Combobox(profile_frame, state='readonly')
        self.profile_selector.pack(fill='x', pady=(0, 5))
        
        # Load profiles into dropdown
        self.refresh_profile_list()
        
        # Profile control buttons
        button_frame = tk.Frame(profile_frame, bg='#1a1a2e')
        button_frame.pack(fill='x')
        
        tk.Button(
            button_frame, text="🔄 Refresh", command=self.refresh_profile_list,
            bg='#2d2d44', fg='#ffffff', font=('Arial', 8)
        ).pack(side='left', padx=(0, 5))
        
        tk.Button(
            button_frame, text="⚡ Apply", command=self.apply_selected_profile,
            bg='#00aa44', fg='#ffffff', font=('Arial', 8)
        ).pack(side='left', padx=(0, 5))
        
        tk.Button(
            button_frame, text="📤 Export", command=self.export_current_profile,
            bg='#aa6600', fg='#ffffff', font=('Arial', 8)
        ).pack(side='left')
    
    def create_fx_test_buttons(self, parent):
        """🎮 Main FX testing buttons"""
        fx_frame = tk.LabelFrame(
            parent,
            text="🎆 Fusion Effect Tests",
            fg='#00ff88',
            bg='#1a1a2e',
            font=('Arial', 10, 'bold')
        )
        fx_frame.pack(fill='x', pady=(0, 10))
        
        # Two rows of buttons
        top_row = tk.Frame(fx_frame, bg='#1a1a2e')
        top_row.pack(fill='x', pady=2)
        
        bottom_row = tk.Frame(fx_frame, bg='#1a1a2e')
        bottom_row.pack(fill='x', pady=2)
        
        fx_tests = [
            ("🧘 Zen Test", self.test_zen_boost, '#00aaff', top_row),
            ("🔥 Rage Test", self.test_rage_refactor, '#ff4444', top_row),
            ("🌊 Flow Test", self.test_flow_state, '#00ff88', bottom_row),
            ("⚠️ Burnout Test", self.test_burnout_alert, '#ffaa00', bottom_row),
            ("👥 Squad Test", self.test_squad_sync, '#aa00ff', bottom_row)
        ]
        
        for text, command, color, row in fx_tests:
            tk.Button(
                row, text=text, command=command,
                bg=color, fg='white', font=('Arial', 9, 'bold'),
                padx=10, pady=3
            ).pack(side='left', padx=2, fill='x', expand=True)
    
    def create_particle_tests(self, parent):
        """✨ Particle system testing"""
        particle_frame = tk.LabelFrame(
            parent,
            text="✨ Particle System Tests",
            fg='#00ff88',
            bg='#1a1a2e',
            font=('Arial', 10, 'bold')
        )
        particle_frame.pack(fill='x', pady=(0, 10))
        
        # Particle count slider
        count_frame = tk.Frame(particle_frame, bg='#1a1a2e')
        count_frame.pack(fill='x', pady=2)
        
        tk.Label(count_frame, text="Particle Count:", fg='#ffffff', bg='#1a1a2e').pack(side='left')
        self.particle_count_var = tk.IntVar(value=30)
        particle_slider = tk.Scale(
            count_frame, from_=10, to=200, orient='horizontal',
            variable=self.particle_count_var, bg='#2d2d44', fg='#ffffff'
        )
        particle_slider.pack(side='right', fill='x', expand=True, padx=(10, 0))
        
        # Particle test buttons
        button_frame = tk.Frame(particle_frame, bg='#1a1a2e')
        button_frame.pack(fill='x', pady=2)
        
        particle_tests = [
            ("💥 Burst Test", self.test_particle_burst, '#ff6600'),
            ("🌈 Rainbow Test", self.test_rainbow_particles, '#ff00ff'),
            ("🎆 Fireworks", self.test_fireworks, '#ffff00')
        ]
        
        for text, command, color in particle_tests:
            tk.Button(
                button_frame, text=text, command=command,
                bg=color, fg='white', font=('Arial', 8, 'bold'),
                padx=8
            ).pack(side='left', padx=2, fill='x', expand=True)
    
    def create_theme_tests(self, parent):
        """🎨 Theme transition testing"""
        theme_frame = tk.LabelFrame(
            parent,
            text="🎨 Theme Transition Tests",
            fg='#00ff88',
            bg='#1a1a2e',
            font=('Arial', 10, 'bold')
        )
        theme_frame.pack(fill='x', pady=(0, 10))
        
        # Theme buttons in grid
        theme_grid = tk.Frame(theme_frame, bg='#1a1a2e')
        theme_grid.pack(fill='x', pady=2)
        
        # First row
        row1 = tk.Frame(theme_grid, bg='#1a1a2e')
        row1.pack(fill='x', pady=1)
        
        # Second row
        row2 = tk.Frame(theme_grid, bg='#1a1a2e')
        row2.pack(fill='x', pady=1)
        
        theme_tests = [
            ("🧠 Baseline", lambda: self.test_theme_transition(ThemeType.BASELINE), '#666666', row1),
            ("🧘 Zen", lambda: self.test_theme_transition(ThemeType.ZEN_BOOST), '#00aaff', row1),
            ("🔥 Rage", lambda: self.test_theme_transition(ThemeType.RAGE_REFACTOR), '#ff4444', row2),
            ("🌊 Flow", lambda: self.test_theme_transition(ThemeType.FLOW_STATE), '#00ff88', row2),
            ("⚠️ Burnout", lambda: self.test_theme_transition(ThemeType.BURNOUT_ALERT), '#ffaa00', row2)
        ]
        
        for text, command, color, row in theme_tests:
            tk.Button(
                row, text=text, command=command,
                bg=color, fg='white', font=('Arial', 8, 'bold'),
                padx=5, pady=2
            ).pack(side='left', padx=1, fill='x', expand=True)
    
    def create_meme_tests(self, parent):
        """😸 Meme deployment testing"""
        meme_frame = tk.LabelFrame(
            parent,
            text="😸 Meme Deployment Tests",
            fg='#00ff88',
            bg='#1a1a2e',
            font=('Arial', 10, 'bold')
        )
        meme_frame.pack(fill='x', pady=(0, 10))
        
        meme_buttons = tk.Frame(meme_frame, bg='#1a1a2e')
        meme_buttons.pack(fill='x', pady=2)
        
        meme_tests = [
            ("😤 Frustration", lambda: self.test_meme_popup('frustration'), '#ff6600'),
            ("🔥 Rage", lambda: self.test_meme_popup('rage_refactor'), '#ff0000'),
            ("🧘 Zen", lambda: self.test_meme_popup('zen_boost'), '#0088ff'),
            ("🌊 Flow", lambda: self.test_meme_popup('flow_state'), '#00ff88')
        ]
        
        for text, command, color in meme_tests:
            tk.Button(
                meme_buttons, text=text, command=command,
                bg=color, fg='white', font=('Arial', 8, 'bold'),
                padx=8
            ).pack(side='left', padx=1, fill='x', expand=True)
    
    def create_stress_tests(self, parent):
        """💪 System stress testing"""
        stress_frame = tk.LabelFrame(
            parent,
            text="💪 Stress Tests",
            fg='#00ff88',
            bg='#1a1a2e',
            font=('Arial', 10, 'bold')
        )
        stress_frame.pack(fill='x', pady=(0, 10))
        
        stress_buttons = tk.Frame(stress_frame, bg='#1a1a2e')
        stress_buttons.pack(fill='x', pady=2)
        
        tk.Button(
            stress_buttons, text="🚀 Particle Storm", command=self.start_particle_storm,
            bg='#ff00ff', fg='white', font=('Arial', 9, 'bold')
        ).pack(side='left', padx=2, fill='x', expand=True)
        
        tk.Button(
            stress_buttons, text="🎨 Theme Chaos", command=self.start_theme_chaos,
            bg='#ff8800', fg='white', font=('Arial', 9, 'bold')
        ).pack(side='left', padx=2, fill='x', expand=True)
        
        tk.Button(
            stress_buttons, text="🛑 Stop Tests", command=self.stop_stress_tests,
            bg='#888888', fg='white', font=('Arial', 9, 'bold')
        ).pack(side='left', padx=2, fill='x', expand=True)
    
    def create_test_log(self, parent):
        """📝 Test results log"""
        log_frame = tk.LabelFrame(
            parent,
            text="📝 Test Log",
            fg='#00ff88',
            bg='#1a1a2e',
            font=('Arial', 10, 'bold')
        )
        log_frame.pack(fill='both', expand=True)
        
        # Scrollable text area
        log_container = tk.Frame(log_frame, bg='#1a1a2e')
        log_container.pack(fill='both', expand=True, padx=5, pady=5)
        
        scrollbar = tk.Scrollbar(log_container)
        scrollbar.pack(side='right', fill='y')
        
        self.test_log = tk.Text(
            log_container,
            height=8,
            bg='#2d2d44',
            fg='#ffffff',
            font=('Consolas', 9),
            yscrollcommand=scrollbar.set
        )
        self.test_log.pack(side='left', fill='both', expand=True)
        scrollbar.config(command=self.test_log.yview)
        
        # Clear log button
        tk.Button(
            log_frame, text="🗑️ Clear Log", command=self.clear_test_log,
            bg='#666666', fg='white', font=('Arial', 8)
        ).pack(pady=2)
    
    def create_fx_canvas(self):
        """🎨 Create the main visual effects canvas"""
        canvas_container = tk.Frame(self.canvas_frame, bg='#2d2d44')
        canvas_container.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Canvas title
        canvas_title = tk.Label(
            canvas_container,
            text="🎆 Visual FX Test Arena 🎆",
            font=('Arial', 12, 'bold'),
            fg='#00ff88',
            bg='#2d2d44'
        )
        canvas_title.pack(pady=(0, 10))
        
        # Main canvas
        self.canvas = tk.Canvas(
            canvas_container,
            width=600,
            height=500,
            bg='#1a1a2e',
            highlightthickness=2,
            highlightbackground='#00ff88'
        )
        self.canvas.pack()
        
        # Canvas info label
        self.canvas_info = tk.Label(
            canvas_container,
            text="🎮 Click buttons to test visual effects!",
            font=('Arial', 10),
            fg='#ffffff',
            bg='#2d2d44'
        )
        self.canvas_info.pack(pady=(10, 0))
    
    def initialize_fx_systems(self):
        """⚡ Initialize all FX systems"""
        if self.canvas:
            self.visual_fx = VisualFXEngine(self.root, self.canvas)
            self.log_message("🚀 Visual FX Engine initialized!")
        else:
            self.log_message("❌ Failed to initialize FX systems!")
    
    def log_message(self, message: str):
        """📝 Add message to test log"""
        if self.test_log:
            timestamp = time.strftime("%H:%M:%S")
            self.test_log.insert('end', f"[{timestamp}] {message}\n")
            self.test_log.see('end')
            self.root.update_idletasks()
    
    def refresh_profile_list(self):
        """🔄 Refresh the profile dropdown list"""
        if self.profile_selector:
            profiles = list(self.profile_manager.available_profiles.keys())
            self.profile_selector['values'] = profiles
            
            if profiles and not self.profile_selector.get():
                self.profile_selector.set(profiles[0])
            
            self.log_message(f"🔄 Refreshed {len(profiles)} profiles")
    
    def apply_selected_profile(self):
        """⚡ Apply the selected FX profile"""
        selected = self.profile_selector.get()
        if selected:
            success = self.profile_manager.set_active_profile(selected)
            if success:
                self.log_message(f"⚡ Applied profile: {selected}")
            else:
                self.log_message(f"❌ Failed to apply profile: {selected}")
    
    def export_current_profile(self):
        """📤 Export current profile for sharing"""
        selected = self.profile_selector.get()
        if selected:
            export_path = self.profile_manager.export_for_sharing(selected)
            if export_path:
                self.log_message(f"📤 Exported: {export_path}")
                messagebox.showinfo("Export Success", f"Profile exported to:\n{export_path}")
            else:
                self.log_message(f"❌ Export failed for: {selected}")
    
    # FX Test Methods
    def test_zen_boost(self):
        """🧘 Test zen boost effect"""
        self.log_message("🧘 Testing Zen Boost effect...")
        if self.visual_fx:
            self.visual_fx.trigger_fusion_effect('zen_boost', (300, 250))
            self.canvas_info.config(text="🧘✨ Zen Boost effect activated!")
    
    def test_rage_refactor(self):
        """🔥 Test rage refactor effect"""
        self.log_message("🔥 Testing Rage Refactor effect...")
        if self.visual_fx:
            self.visual_fx.trigger_fusion_effect('rage_refactor', (300, 250))
            self.canvas_info.config(text="🔥💪 Rage Refactor effect activated!")
    
    def test_flow_state(self):
        """🌊 Test flow state effect"""
        self.log_message("🌊 Testing Flow State effect...")
        if self.visual_fx:
            self.visual_fx.trigger_fusion_effect('flow_state', (300, 250))
            self.canvas_info.config(text="🌊🚀 Flow State effect activated!")
    
    def test_burnout_alert(self):
        """⚠️ Test burnout alert effect"""
        self.log_message("⚠️ Testing Burnout Alert effect...")
        if self.visual_fx:
            self.visual_fx.trigger_fusion_effect('burnout_alert', (300, 250))
            self.canvas_info.config(text="⚠️😴 Burnout Alert effect activated!")
    
    def test_squad_sync(self):
        """👥 Test squad sync effect"""
        self.log_message("👥 Testing Squad Sync effect...")
        if self.visual_fx:
            self.visual_fx.trigger_fusion_effect('squad_sync', (300, 250))
            self.canvas_info.config(text="👥⚡ Squad Sync effect activated!")
    
    def test_particle_burst(self):
        """💥 Test custom particle burst"""
        count = self.particle_count_var.get()
        self.log_message(f"💥 Testing particle burst with {count} particles...")
        if self.visual_fx:
            self.visual_fx.particles.create_xp_burst(300, 250, count, '#00ff88')
            self.canvas_info.config(text=f"💥 Particle burst: {count} particles!")
    
    def test_rainbow_particles(self):
        """🌈 Test rainbow particle effect"""
        count = self.particle_count_var.get()
        self.log_message(f"🌈 Testing rainbow particles...")
        if self.visual_fx:
            colors = ['#ff0000', '#ff8800', '#ffff00', '#00ff00', '#0088ff', '#8800ff']
            for i, color in enumerate(colors):
                x_offset = (i - 2.5) * 30
                self.visual_fx.particles.create_xp_burst(300 + x_offset, 250, count // 6, color)
            self.canvas_info.config(text="🌈 Rainbow particle storm!")
    
    def test_fireworks(self):
        """🎆 Test fireworks effect"""
        self.log_message("🎆 Testing fireworks effect...")
        if self.visual_fx:
            # Multiple bursts at different positions
            positions = [(200, 200), (400, 200), (300, 150), (250, 300), (350, 300)]
            colors = ['#ff0000', '#00ff00', '#0088ff', '#ffff00', '#ff00ff']
            
            for (x, y), color in zip(positions, colors):
                self.visual_fx.particles.create_xp_burst(x, y, 25, color)
            
            self.canvas_info.config(text="🎆 Fireworks spectacular!")
    
    def test_theme_transition(self, theme_type: ThemeType):
        """🎨 Test theme transition"""
        self.log_message(f"🎨 Testing theme transition: {theme_type.value}")
        if self.visual_fx:
            self.visual_fx.themes.apply_theme(theme_type, animated=True)
            self.canvas_info.config(text=f"🎨 Theme applied: {theme_type.value.title()}")
    
    def test_meme_popup(self, meme_type: str):
        """😸 Test meme popup"""
        self.log_message(f"😸 Testing meme popup: {meme_type}")
        if self.visual_fx:
            self.visual_fx.memes.show_meme_popup(meme_type)
            self.canvas_info.config(text=f"😸 Meme deployed: {meme_type}")
    
    def start_particle_storm(self):
        """🚀 Start continuous particle storm"""
        if self.stress_test_active:
            return
            
        self.stress_test_active = True
        self.log_message("🚀 Starting particle storm stress test...")
        
        def particle_storm():
            colors = ['#ff0000', '#00ff00', '#0088ff', '#ffff00', '#ff00ff', '#00ffff']
            while self.stress_test_active:
                if self.visual_fx:
                    x = random.randint(50, 550)
                    y = random.randint(50, 450)
                    color = random.choice(colors)
                    count = random.randint(10, 30)
                    
                    self.visual_fx.particles.create_xp_burst(x, y, count, color)
                
                time.sleep(0.3)
        
        threading.Thread(target=particle_storm, daemon=True).start()
        self.canvas_info.config(text="🚀 Particle storm in progress...")
    
    def start_theme_chaos(self):
        """🎨 Start rapid theme changes"""
        if self.stress_test_active:
            return
            
        self.stress_test_active = True
        self.log_message("🎨 Starting theme chaos stress test...")
        
        def theme_chaos():
            themes = list(ThemeType)
            while self.stress_test_active:
                if self.visual_fx:
                    theme = random.choice(themes)
                    self.visual_fx.themes.apply_theme(theme, animated=False)
                
                time.sleep(1.0)
        
        threading.Thread(target=theme_chaos, daemon=True).start()
        self.canvas_info.config(text="🎨 Theme chaos in progress...")
    
    def stop_stress_tests(self):
        """🛑 Stop all stress tests"""
        self.stress_test_active = False
        self.log_message("🛑 Stopping all stress tests...")
        self.canvas_info.config(text="🛑 Stress tests stopped.")
        
        # Reset to baseline theme
        if self.visual_fx:
            self.visual_fx.themes.apply_theme(ThemeType.BASELINE)
    
    def clear_test_log(self):
        """🗑️ Clear the test log"""
        if self.test_log:
            self.test_log.delete(1.0, 'end')
            self.log_message("🗑️ Test log cleared!")
    
    def run(self):
        """🚀 Launch the FX test harness"""
        self.log_message("🧪 BCI Fusion Forge FX Test Harness - ONLINE!")
        self.log_message("🎮 Use controls to test visual effects")
        self.log_message("🎨 Try different profiles and stress tests")
        self.log_message("✨ All systems ready for testing!")
        
        self.canvas_info.config(text="🎮 FX Test Harness ready! Click buttons to test effects!")
        
        self.root.mainloop()

# 🎯 MAIN EXECUTION - LEGENDARY TEST HARNESS
if __name__ == "__main__":
    print("🧪💥 BCI FUSION FORGE - FX TEST HARNESS DEPLOYMENT! 💥🧪")
    print("")
    print("🎨 Visual effects laboratory initializing...")
    print("🧪 Test systems loading...")
    print("🎮 Interactive testing interface ready...")
    print("🚀 Stress testing capabilities armed...")
    print("")
    print("#BROSKI_HINT: Perfect your visual dopamine experience before deployment! 🎆")
    
    harness = FXTestHarness()
    harness.run()

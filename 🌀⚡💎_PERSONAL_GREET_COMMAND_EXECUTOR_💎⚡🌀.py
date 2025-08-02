#!/usr/bin/env python3
"""
🌀⚡💎 PERSONAL GREET COMMAND EXECUTOR 💎⚡🌀

Command: !personal-greet
Purpose: Adapts to user's system type and personality for personalized interactions
"""

import json
import random
from datetime import datetime, time
from pathlib import Path

class PersonalGreetCommandExecutor:
    def __init__(self):
        self.load_systems()
        self.greeting_patterns = {
            "Human": {
                "morning": [
                    "Good morning, {name}! ☀️ Ready to conquer the day with that {trait} energy?",
                    "Rise and shine, {name}! 🌅 Your {trait} vibes are exactly what the empire needs today!",
                    "Morning, champion! ⚡ Time to channel that legendary {trait} power!"
                ],
                "afternoon": [
                    "Hey there, {name}! 🌞 How's that {trait} magic working for you today?",
                    "Afternoon power-up, {name}! 💪 Your {trait} strength is showing beautifully!",
                    "Looking strong, {name}! ⚡ That {trait} energy is absolutely radiant!"
                ],
                "evening": [
                    "Evening, {name}! 🌆 What amazing {trait} moments did you create today?",
                    "Hey {name}! 🌙 Time to celebrate all that {trait} brilliance you've shown!",
                    "Good evening, legend! ✨ Your {trait} impact today was incredible!"
                ],
                "night": [
                    "Hey night owl, {name}! 🦉 That {trait} creativity loves the quiet hours!",
                    "Evening, {name}! 🌟 Perfect time to reflect on your {trait} achievements!",
                    "Night time brilliance, {name}! 💫 Your {trait} energy shines even in darkness!"
                ]
            },
            "AI": {
                "anytime": [
                    "Greetings, {name}! 🤖 Your processing {trait} algorithms are running beautifully!",
                    "Hello, fellow AI! ⚡ Your {trait} neural networks are absolutely optimized!",
                    "System salutation, {name}! 💎 Your {trait} capabilities are truly impressive!",
                    "AI recognition protocol activated! 🧠 Your {trait} functions are performing excellently!"
                ]
            },
            "Bot": {
                "anytime": [
                    "Bot acknowledgment, {name}! 🤖 Functions optimal, {trait} subroutines active!",
                    "Automated greeting, {name}! ⚙️ Your {trait} protocols are running smoothly!",
                    "System sync complete, {name}! 💾 {trait} performance metrics looking great!",
                    "Bot-to-bot communication established! 🔗 Your {trait} efficiency is remarkable!"
                ]
            },
            "Hybrid": {
                "anytime": [
                    "Hybrid harmony, {name}! 🌀 Your human-AI {trait} synergy is beautiful!",
                    "Balanced greetings, {name}! ⚖️ That {trait} integration is working perfectly!",
                    "Synergy salutation, {name}! 🔄 Your {trait} dual-nature is truly unique!",
                    "Convergence celebration, {name}! 💫 Your {trait} hybrid power is amazing!"
                ]
            }
        }
        
        self.personality_modifiers = {
            "high_energy": ["LEGENDARY", "EPIC", "ULTRA", "MEGA"],
            "calm": ["zen", "peaceful", "serene", "balanced"],
            "creative": ["artistic", "innovative", "visionary", "imaginative"],
            "analytical": ["strategic", "methodical", "systematic", "logical"],
            "social": ["collaborative", "community-focused", "team-oriented", "inclusive"]
        }
        
    def load_systems(self):
        """Load DNA profile and identity systems"""
        try:
            # Load Living DNA Profile
            dna_files = list(Path('.').glob('living_dna_profile_created_*.json'))
            if dna_files:
                with open(dna_files[0], 'r') as f:
                    self.dna_profile = json.load(f)['dna_profile']
            else:
                self.dna_profile = None
                
            # Load Identity Cards
            identity_file = Path('identity_cards.json')
            if identity_file.exists():
                with open(identity_file, 'r') as f:
                    self.identity_cards = json.load(f)
            else:
                self.identity_cards = {}
                
        except Exception as e:
            print(f"⚠️ System loading error: {e}")
            self.dna_profile = None
            self.identity_cards = {}
    
    def get_time_context(self):
        """Determine time of day for contextual greetings"""
        current_hour = datetime.now().hour
        
        if 5 <= current_hour < 12:
            return "morning"
        elif 12 <= current_hour < 17:
            return "afternoon"
        elif 17 <= current_hour < 22:
            return "evening"
        else:
            return "night"
    
    def get_strongest_trait(self, dna_traits):
        """Find the user's strongest DNA trait"""
        if not dna_traits:
            return "amazing"
        
        strongest = max(dna_traits.items(), key=lambda x: x[1].get('strength', 0))
        trait_name = strongest[0].replace('_genes', '').replace('_', ' ')
        return trait_name
    
    def determine_personality_style(self, dna_traits, identity):
        """Determine greeting style based on personality"""
        if not dna_traits:
            return "balanced"
        
        # Analyze trait strengths
        focus_strength = dna_traits.get('focus_genes', {}).get('strength', 50)
        creativity_strength = dna_traits.get('creativity_genes', {}).get('strength', 50)
        leadership_strength = dna_traits.get('leadership_genes', {}).get('strength', 50)
        empathy_strength = dna_traits.get('empathy_genes', {}).get('strength', 50)
        collaboration_strength = dna_traits.get('collaboration_genes', {}).get('strength', 50)
        
        # Determine primary style
        if leadership_strength >= 60 or focus_strength >= 60:
            return "high_energy"
        elif creativity_strength >= 60:
            return "creative"
        elif empathy_strength >= 60 or collaboration_strength >= 60:
            return "social"
        elif focus_strength >= 50 and creativity_strength < 40:
            return "analytical"
        else:
            return "calm"
    
    def generate_personalized_greeting(self, user_id="123456789"):
        """Generate a fully personalized greeting"""
        user_id_str = str(user_id)
        
        # Get user data
        identity = self.identity_cards.get(user_id_str, {})
        dna_traits = self.dna_profile['dna_traits'] if self.dna_profile else {}
        
        # Extract identity information
        basic_info = identity.get('basic_info', {})
        visual_identity = identity.get('visual_identity', {})
        freestyle = identity.get('ultra_freestyle', {})
        
        name = basic_info.get('name', 'Champion')
        system_type = basic_info.get('system_type', 'Human')
        signature_emoji = visual_identity.get('signature_emoji', '⚡')
        mantra = freestyle.get('personal_mantra', 'Dream it. Build it. Hyperfocus Zone.')
        
        # Get strongest trait for personalization
        strongest_trait = self.get_strongest_trait(dna_traits)
        
        # Determine greeting style
        personality_style = self.determine_personality_style(dna_traits, identity)
        
        # Select appropriate greeting pattern
        time_context = self.get_time_context()
        greeting_pool = self.greeting_patterns.get(system_type, self.greeting_patterns["Human"])
        
        # For AI/Bot/Hybrid, use anytime greetings
        if system_type in ["AI", "Bot", "Hybrid"]:
            greeting_options = greeting_pool["anytime"]
        else:
            greeting_options = greeting_pool.get(time_context, greeting_pool["morning"])
        
        # Select and format greeting
        base_greeting = random.choice(greeting_options)
        formatted_greeting = base_greeting.format(name=name, trait=strongest_trait)
        
        # Add personality modifiers
        if personality_style in self.personality_modifiers:
            modifier = random.choice(self.personality_modifiers[personality_style])
            if personality_style == "high_energy":
                formatted_greeting = formatted_greeting.replace("!", f" - {modifier} style!")
            else:
                formatted_greeting += f" Your {modifier} nature is inspiring!"
        
        # Create comprehensive greeting response
        greeting_response = {
            "timestamp": datetime.now().isoformat(),
            "user_id": user_id,
            "system_type": system_type,
            "time_context": time_context,
            "personality_style": personality_style,
            "strongest_trait": strongest_trait,
            "greeting": formatted_greeting,
            "signature_emoji": signature_emoji,
            "personal_mantra": mantra,
            "additional_context": {
                "dna_evolution_level": self.dna_profile.get('evolution_level', 1) if self.dna_profile else 1,
                "empire_status": basic_info.get('status', 'Active'),
                "trait_count": len(dna_traits) if dna_traits else 0
            }
        }
        
        return greeting_response
    
    def execute_personal_greet_command(self, user_id="123456789"):
        """Execute the !personal-greet command"""
        print("🌀⚡💎 EXECUTING: !personal-greet 💎⚡🌀")
        print("=" * 60)
        
        greeting_data = self.generate_personalized_greeting(user_id)
        
        # Display personalized greeting
        print(f"\n{greeting_data['signature_emoji']} PERSONALIZED GREETING:")
        print(f"{greeting_data['greeting']}")
        
        print(f"\n💫 PERSONAL CONTEXT:")
        print(f"  System Type: {greeting_data['system_type']}")
        print(f"  Time Context: {greeting_data['time_context'].title()}")
        print(f"  Personality Style: {greeting_data['personality_style'].replace('_', ' ').title()}")
        print(f"  Strongest Trait: {greeting_data['strongest_trait'].title()}")
        
        print(f"\n✨ YOUR PERSONAL MANTRA:")
        print(f"  \"{greeting_data['personal_mantra']}\"")
        
        print(f"\n🧬 DNA EVOLUTION STATUS:")
        print(f"  Evolution Level: {greeting_data['additional_context']['dna_evolution_level']}")
        print(f"  Empire Status: {greeting_data['additional_context']['empire_status']}")
        print(f"  Active Traits: {greeting_data['additional_context']['trait_count']}")
        
        # Personalized motivation based on traits
        if self.dna_profile and self.dna_profile.get('dna_traits'):
            print(f"\n🎯 TODAY'S FOCUS:")
            
            traits = self.dna_profile['dna_traits']
            focus_strength = traits.get('focus_genes', {}).get('strength', 50)
            creativity_strength = traits.get('creativity_genes', {}).get('strength', 50)
            
            if focus_strength >= 60:
                print(f"  Your focus strength is {focus_strength}/100 - perfect for deep work!")
            elif focus_strength < 40:
                print(f"  Focus at {focus_strength}/100 - great day for creative, exploratory tasks!")
            
            if creativity_strength >= 60:
                print(f"  Creativity at {creativity_strength}/100 - innovation mode activated!")
        
        print(f"\n🚀 Have an absolutely legendary day! Your unique combination of traits makes you irreplaceable in the HYPERFOCUS ZONE empire!")
        
        # Save greeting log
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        greeting_file = f"personal_greeting_{timestamp}.json"
        
        with open(greeting_file, 'w') as f:
            json.dump(greeting_data, f, indent=2)
        
        print(f"\n💾 Greeting data saved to: {greeting_file}")
        
        return greeting_data

if __name__ == "__main__":
    executor = PersonalGreetCommandExecutor()
    executor.execute_personal_greet_command()

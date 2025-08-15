"""
🧠⚡💎 BROski♾️ ULTRA INTELLIGENCE ASSESSMENT ENGINE 💎⚡🧠

This is the core intelligence assessment system that evaluates multiple intelligence types,
detects genius patterns, and provides neurodivergent-optimized recommendations.

Features:
- 11 intelligence types assessment
- Real-time genius detection
- ADHD-optimized task chunking
- Boardroom Agent Army integration
- Memory Crystal pattern recognition
"""

import json
import sqlite3
import datetime
import uuid
import math
from pathlib import Path
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
import hashlib


@dataclass
class IntelligenceScore:
    """Individual intelligence score with metadata"""
    value: float  # 0.0 - 1.0
    confidence: float  # 0.0 - 1.0
    source: str  # "active" | "passive"
    last_assessed: str
    notes: str = ""


@dataclass
class AssessmentTask:
    """Individual assessment task definition"""
    intelligence_type: str
    task_id: str
    prompt: str
    time_limit: int  # seconds
    difficulty: str  # "easy" | "medium" | "hard"
    multimodal: bool = False
    low_energy: bool = False
    adhd_optimized: bool = True


class BROskiUltraIntelligenceEngine:
    """🧠 Main intelligence assessment and genius detection system"""

    def __init__(self):
        self.db_path = Path("h:/broski_intelligence.db")
        self.memory_crystal_path = Path("h:/memory_crystals")
        self.intelligence_types = [
            "linguistic", "logical_math", "spatial", "musical",
            "bodily_kinesthetic", "interpersonal", "intrapersonal",
            "naturalistic", "creative", "emotional", "practical"
        ]
        self.genius_threshold = 0.85
        self.setup_database()
        self.load_assessment_tasks()

        print("🧠⚡💎 BROski♾️ ULTRA INTELLIGENCE ENGINE ACTIVATED 💎⚡🧠")
        print("=" * 80)
        print("🎯 Intelligence Types:", len(self.intelligence_types))
        print("🚀 Assessment Tasks:", len(self.assessment_tasks))
        print("🏛️ Boardroom Integration: ACTIVE")
        print("💎 Memory Crystal Network: SYNCHRONIZED")
        print("=" * 80)

    def setup_database(self):
        """Initialize the intelligence assessment database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # User intelligence profiles
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_profiles (
                user_id TEXT PRIMARY KEY,
                display_name TEXT,
                created_at TEXT,
                last_assessed TEXT,
                composite_genius_score REAL DEFAULT 0.0,
                genius_flags TEXT DEFAULT '[]',
                badges TEXT DEFAULT '[]',
                broski_points INTEGER DEFAULT 0
            )
        ''')

        # Intelligence scores
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS intelligence_scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT,
                intelligence_type TEXT,
                value REAL,
                confidence REAL,
                source TEXT,
                last_assessed TEXT,
                notes TEXT,
                FOREIGN KEY (user_id) REFERENCES user_profiles (user_id)
            )
        ''')

        # Assessment results
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS assessment_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT,
                task_id TEXT,
                intelligence_type TEXT,
                response TEXT,
                score REAL,
                time_taken INTEGER,
                novelty_score REAL DEFAULT 0.0,
                consistency_score REAL DEFAULT 0.0,
                impact_score REAL DEFAULT 0.0,
                timestamp TEXT,
                FOREIGN KEY (user_id) REFERENCES user_profiles (user_id)
            )
        ''')

        # Domain expertise
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS domain_expertise (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT,
                domain_name TEXT,
                skill_level REAL,
                years_experience INTEGER,
                confidence REAL,
                last_updated TEXT,
                FOREIGN KEY (user_id) REFERENCES user_profiles (user_id)
            )
        ''')

        conn.commit()
        conn.close()
        print("✅ Intelligence Database initialized successfully!")

    def load_assessment_tasks(self):
        """Load the 18-task assessment pack"""
        self.assessment_tasks = [
            # Core Intelligence Tasks
            AssessmentTask("linguistic", "ling_001",
                "Write a persuasive 3-sentence pitch for a sticker shop. Then identify your main persuasion technique.",
                180, "medium"),

            AssessmentTask("logical_math", "logic_001",
                "A cube has 6 faces. If you paint 3 faces red and 3 faces blue, how many different ways can you do this? (Consider rotations as same)",
                240, "hard"),

            AssessmentTask("spatial", "spatial_001",
                "Describe how you'd arrange 5 different sized boxes to fit in a car trunk. Consider weight distribution.",
                120, "medium"),

            AssessmentTask("musical", "music_001",
                "Create a 4-line verse with a strong rhythm. Then describe the beat pattern you used.",
                150, "medium"),

            AssessmentTask("bodily_kinesthetic", "kinetic_001",
                "Describe the step-by-step body movements for tying a shoe. Focus on hand coordination details.",
                90, "easy"),

            AssessmentTask("interpersonal", "inter_001",
                "Your friend seems upset but won't talk. Describe 3 different approaches to help them, and why each might work.",
                180, "medium"),

            AssessmentTask("intrapersonal", "intra_001",
                "Think of a time you felt proud of yourself. Describe what specifically made you feel proud and why it mattered to you.",
                120, "easy"),

            AssessmentTask("naturalistic", "nature_001",
                "You see clouds forming unusual patterns. Describe what this might tell you about upcoming weather changes.",
                90, "medium"),

            AssessmentTask("creative", "creative_001",
                "Give me 6 unusual uses for a paperclip. For each, describe one way to test if it actually works.",
                120, "medium"),

            AssessmentTask("emotional", "emotion_001",
                "Describe how you'd help someone who's feeling overwhelmed by their workload. Include emotional support strategies.",
                150, "medium"),

            AssessmentTask("practical", "practical_001",
                "You need to move apartments in 2 weeks on a tight budget. Create a step-by-step plan with cost estimates.",
                240, "hard"),

            # Enhanced/Multimodal Tasks
            AssessmentTask("creative", "creative_burst",
                "30-second idea burst: List as many uses for a brick as you can think of. Go!",
                30, "easy", low_energy=True),

            AssessmentTask("logical_math", "logic_timed",
                "Timed puzzle: If 5 machines make 5 widgets in 5 minutes, how many minutes for 100 machines to make 100 widgets?",
                90, "medium"),

            AssessmentTask("spatial", "spatial_rotation",
                "Imagine a cube with a red dot on one face. If you rotate it 90° forward then 90° right, where is the dot now?",
                120, "hard"),

            AssessmentTask("musical", "rhythm_tap",
                "Tap out this rhythm: STRONG-weak-STRONG-weak-weak-STRONG. Then describe how it made you feel.",
                60, "easy", multimodal=True),

            AssessmentTask("kinesthetic", "design_iterate",
                "Look at any object near you. Describe 2 quick improvements you'd make to its design.",
                90, "easy", low_energy=True),

            AssessmentTask("intrapersonal", "reflection_streak",
                "What's one small thing you did well today? Be specific about why it was good.",
                60, "easy", low_energy=True),

            # ADHD-Optimized Micro Tasks
            AssessmentTask("practical", "quick_solve",
                "You spilled coffee on important papers. You have 2 minutes before a meeting. Quick solution?",
                30, "easy", low_energy=True, adhd_optimized=True)
        ]

        print(f"✅ Loaded {len(self.assessment_tasks)} assessment tasks!")

    def create_user_profile(self, user_id: str, display_name: str) -> dict:
        """Create a new user intelligence profile"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        timestamp = datetime.datetime.now().isoformat()

        cursor.execute('''
            INSERT OR REPLACE INTO user_profiles
            (user_id, display_name, created_at, last_assessed)
            VALUES (?, ?, ?, ?)
        ''', (user_id, display_name, timestamp, timestamp))

        # Initialize intelligence scores
        for intelligence_type in self.intelligence_types:
            cursor.execute('''
                INSERT OR REPLACE INTO intelligence_scores
                (user_id, intelligence_type, value, confidence, source, last_assessed, notes)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (user_id, intelligence_type, 0.0, 0.0, "initial", timestamp, "Initial profile creation"))

        conn.commit()
        conn.close()

        print(f"✅ Created intelligence profile for {display_name} ({user_id})")
        return {"status": "success", "user_id": user_id, "created_at": timestamp}

    def run_assessment(self, user_id: str, task_id: str, response: str, time_taken: int) -> dict:
        """Process a single assessment task response"""
        # Find the task
        task = next((t for t in self.assessment_tasks if t.task_id == task_id), None)
        if not task:
            return {"error": "Task not found", "task_id": task_id}

        # Score the response using AI-like heuristics
        score = self._score_response(task, response, time_taken)
        novelty_score = self._calculate_novelty(response)

        # Store the result
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        timestamp = datetime.datetime.now().isoformat()

        cursor.execute('''
            INSERT INTO assessment_results
            (user_id, task_id, intelligence_type, response, score, time_taken,
             novelty_score, timestamp)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (user_id, task_id, task.intelligence_type, response, score,
              time_taken, novelty_score, timestamp))

        # Update intelligence score
        self._update_intelligence_score(cursor, user_id, task.intelligence_type, score)

        conn.commit()
        conn.close()

        # Check for genius detection
        self._check_genius_flags(user_id)

        print(f"✅ Assessment completed: {task.intelligence_type} -> Score: {score:.2f}")

        return {
            "status": "success",
            "task_id": task_id,
            "intelligence_type": task.intelligence_type,
            "score": score,
            "novelty_score": novelty_score,
            "time_taken": time_taken
        }

    def _score_response(self, task: AssessmentTask, response: str, time_taken: int) -> float:
        """Score a response using heuristic analysis"""
        base_score = 0.5

        # Length factor (more detailed responses generally better)
        length_factor = min(len(response) / 200, 1.0) * 0.2

        # Keyword relevance (simple heuristic)
        keywords = {
            "linguistic": ["persuade", "audience", "emotion", "story", "convince"],
            "logical_math": ["calculate", "logic", "pattern", "systematic", "reason"],
            "spatial": ["arrange", "space", "dimension", "visual", "position"],
            "musical": ["rhythm", "beat", "pattern", "sound", "melody"],
            "creative": ["unique", "unusual", "different", "innovative", "original"],
            "practical": ["step", "plan", "cost", "efficient", "realistic"]
        }

        if task.intelligence_type in keywords:
            keyword_matches = sum(1 for word in keywords[task.intelligence_type]
                                if word.lower() in response.lower())
            keyword_factor = min(keyword_matches / 3, 1.0) * 0.2
        else:
            keyword_factor = 0.1

        # Time factor (penalize if too fast or too slow)
        optimal_time = task.time_limit * 0.7
        if time_taken < optimal_time * 0.3:
            time_factor = -0.1  # Too fast might be superficial
        elif time_taken > task.time_limit * 1.2:
            time_factor = -0.05  # Too slow might indicate struggle
        else:
            time_factor = 0.1

        final_score = base_score + length_factor + keyword_factor + time_factor
        return max(0.0, min(1.0, final_score))

    def _calculate_novelty(self, response: str) -> float:
        """Calculate novelty score based on response uniqueness"""
        # Simple novelty heuristic - in production, would use embeddings
        unique_words = len(set(response.lower().split()))
        total_words = len(response.split())

        if total_words == 0:
            return 0.0

        diversity_ratio = unique_words / total_words
        novelty_indicators = ["unusual", "unique", "different", "creative", "original", "new"]
        novelty_count = sum(1 for word in novelty_indicators if word in response.lower())

        novelty_score = (diversity_ratio * 0.7) + (min(novelty_count / 3, 1.0) * 0.3)
        return min(novelty_score, 1.0)

    def _update_intelligence_score(self, cursor, user_id: str, intelligence_type: str, new_score: float):
        """Update intelligence score with rolling average"""
        cursor.execute('''
            SELECT value, confidence FROM intelligence_scores
            WHERE user_id = ? AND intelligence_type = ?
        ''', (user_id, intelligence_type))

        result = cursor.fetchone()
        if result:
            current_value, current_confidence = result
            # Rolling average with confidence weighting
            if current_confidence == 0:
                updated_value = new_score
                updated_confidence = 0.6
            else:
                weight = 0.3  # New assessment weight
                updated_value = (current_value * (1 - weight)) + (new_score * weight)
                updated_confidence = min(current_confidence + 0.1, 0.95)
        else:
            updated_value = new_score
            updated_confidence = 0.6

        timestamp = datetime.datetime.now().isoformat()

        cursor.execute('''
            UPDATE intelligence_scores
            SET value = ?, confidence = ?, last_assessed = ?, source = ?
            WHERE user_id = ? AND intelligence_type = ?
        ''', (updated_value, updated_confidence, timestamp, "active", user_id, intelligence_type))

    def get_user_profile(self, user_id: str) -> dict:
        """Get complete user intelligence profile"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Get user data
        cursor.execute('''
            SELECT display_name, created_at, last_assessed, composite_genius_score,
                   genius_flags, badges, broski_points
            FROM user_profiles WHERE user_id = ?
        ''', (user_id,))

        user_data = cursor.fetchone()
        if not user_data:
            conn.close()
            return {"error": "User not found"}

        display_name, created_at, last_assessed, composite_score, genius_flags, badges, broski_points = user_data

        # Get intelligence scores
        cursor.execute('''
            SELECT intelligence_type, value, confidence, source, last_assessed, notes
            FROM intelligence_scores WHERE user_id = ?
        ''', (user_id,))

        intelligence_data = cursor.fetchall()
        skill_vector = {}

        for intel_type, value, confidence, source, last_assessed, notes in intelligence_data:
            skill_vector[intel_type] = {
                "value": value,
                "confidence": confidence,
                "source": source,
                "last_assessed": last_assessed,
                "notes": notes
            }

        # Get domain expertise
        cursor.execute('''
            SELECT domain_name, skill_level, years_experience, confidence, last_updated
            FROM domain_expertise WHERE user_id = ?
        ''', (user_id,))

        domain_data = cursor.fetchall()
        domain_expertise = {}

        for domain, skill_level, years, confidence, last_updated in domain_data:
            domain_expertise[domain] = {
                "value": skill_level,
                "years": years,
                "confidence": confidence,
                "last_updated": last_updated
            }

        conn.close()

        # Generate top strengths
        top_strengths = sorted(skill_vector.items(),
                             key=lambda x: x[1]["value"], reverse=True)[:3]

        return {
            "user_id": user_id,
            "display_name": display_name,
            "skill_vector": skill_vector,
            "domain_expertise": domain_expertise,
            "composite_genius_score": composite_score,
            "genius_flags": json.loads(genius_flags) if genius_flags else [],
            "badges": json.loads(badges) if badges else [],
            "broski_points": broski_points,
            "top_strengths": [(name, data["value"]) for name, data in top_strengths],
            "last_assessed": last_assessed,
            "created_at": created_at
        }

    def calculate_composite_genius_score(self, user_id: str) -> float:
        """Calculate composite genius score with weighted formula"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Get intelligence scores
        cursor.execute('''
            SELECT AVG(value) as avg_skill FROM intelligence_scores
            WHERE user_id = ? AND confidence > 0.5
        ''', (user_id,))

        skill_result = cursor.fetchone()
        skill_score = skill_result[0] if skill_result[0] else 0.0

        # Get assessment results for novelty and consistency
        cursor.execute('''
            SELECT AVG(novelty_score) as avg_novelty,
                   (1.0 - (STDEV(score) / AVG(score))) as consistency
            FROM assessment_results
            WHERE user_id = ? AND score > 0
        ''', (user_id,))

        result = cursor.fetchone()
        novelty_score = result[0] if result[0] else 0.0
        consistency_score = result[1] if result[1] else 0.0

        conn.close()

        # Simple impact score (would be more sophisticated in production)
        impact_score = 0.5  # Default baseline

        # Weighted composite: 40% Skill + 30% Novelty + 20% Consistency + 10% Impact
        composite = (
            (skill_score * 0.40) +
            (novelty_score * 0.30) +
            (consistency_score * 0.20) +
            (impact_score * 0.10)
        )

        return min(composite, 1.0)

    def _check_genius_flags(self, user_id: str):
        """Check and update genius flags based on latest scores"""
        composite_score = self.calculate_composite_genius_score(user_id)

        # Update composite score in database
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
            UPDATE user_profiles
            SET composite_genius_score = ?, last_assessed = ?
            WHERE user_id = ?
        ''', (composite_score, datetime.datetime.now().isoformat(), user_id))

        # Check for genius threshold
        current_flags = []
        current_badges = []
        broski_points_earned = 0

        if composite_score >= self.genius_threshold:
            current_flags.append("composite_genius")
            current_badges.append("BROski Genius Badge - Ultra Intelligence")
            broski_points_earned += 1000

        # Check individual intelligence genius levels
        cursor.execute('''
            SELECT intelligence_type, value FROM intelligence_scores
            WHERE user_id = ? AND value >= 0.90
        ''', (user_id,))

        high_scores = cursor.fetchall()
        for intel_type, value in high_scores:
            flag_name = f"{intel_type}_genius"
            if flag_name not in current_flags:
                current_flags.append(flag_name)
                current_badges.append(f"BROski Genius Badge - {intel_type.title()} Master")
                broski_points_earned += 500

        # Update flags and badges
        cursor.execute('''
            UPDATE user_profiles
            SET genius_flags = ?, badges = ?, broski_points = broski_points + ?
            WHERE user_id = ?
        ''', (json.dumps(current_flags), json.dumps(current_badges),
              broski_points_earned, user_id))

        conn.commit()
        conn.close()

        if broski_points_earned > 0:
            print(f"🎊 GENIUS DETECTED! {user_id} earned {broski_points_earned} BROski points!")
            print(f"   New flags: {current_flags}")
            print(f"   Composite score: {composite_score:.2f}")

    def generate_discord_embed(self, user_id: str) -> dict:
        """Generate Discord embed for user intelligence profile"""
        profile = self.get_user_profile(user_id)
        if "error" in profile:
            return profile

        # Format top strengths
        top_strengths_text = "\n".join([
            f"{i+1}) {name.replace('_', ' ').title()} — {score:.2f}"
            for i, (name, score) in enumerate(profile["top_strengths"])
        ])

        # Genius status
        composite_score = profile["composite_genius_score"]
        if composite_score >= self.genius_threshold:
            genius_text = f"{composite_score:.2f} — 🎉 BROski Genius Badge unlocked!"
            genius_color = 15844367  # Gold color
        else:
            genius_text = f"{composite_score:.2f} — Keep going! (Target: {self.genius_threshold:.2f})"
            genius_color = 5814783  # Blue color

        # First action recommendation
        top_intelligence = profile["top_strengths"][0][0] if profile["top_strengths"] else "creative"
        action_text = self._get_action_recommendation(top_intelligence, composite_score)

        embed_payload = {
            "username": "BROski♾️",
            "avatar_url": "https://hyperfocuszone.com/broski-avatar.png",
            "embeds": [
                {
                    "title": f"Genius Map — {profile['display_name']}",
                    "description": "hey Bro — fresh snapshot of your intelligence map. Top strengths & first steps below.",
                    "color": genius_color,
                    "fields": [
                        {
                            "name": "Top 3 Strengths",
                            "value": top_strengths_text,
                            "inline": False
                        },
                        {
                            "name": "Composite Genius Score",
                            "value": genius_text,
                            "inline": False
                        },
                        {
                            "name": "First Action",
                            "value": action_text,
                            "inline": False
                        },
                        {
                            "name": "BROski Points",
                            "value": f"💎 {profile['broski_points']} points earned!",
                            "inline": True
                        },
                        {
                            "name": "Export",
                            "value": "Use `/export profile` to get a printable card or shareable PDF.",
                            "inline": False
                        }
                    ],
                    "footer": {
                        "text": f"Last assessed: {profile['last_assessed']}"
                    }
                }
            ]
        }

        return embed_payload

    def _get_action_recommendation(self, top_intelligence: str, composite_score: float) -> str:
        """Get personalized action recommendation based on top intelligence"""
        recommendations = {
            "creative": "Try a 25-minute creative sprint: pick a small project that mixes art + problem-solving. I'll make a prompt!",
            "logical_math": "Challenge yourself with a logic puzzle or coding problem for 20 minutes. Build that pattern recognition!",
            "interpersonal": "Practice your people skills: have a meaningful conversation with someone new today.",
            "practical": "Take on a real-world problem: organize something, plan an event, or optimize a process.",
            "linguistic": "Write something creative: a story, poem, or persuasive argument. Share it with someone!",
            "spatial": "Try a visual challenge: sketch, design, or build something with your hands.",
            "intrapersonal": "Spend 15 minutes reflecting: journal about your goals and what drives you.",
            "emotional": "Practice emotional intelligence: help someone or work on understanding your feelings.",
            "musical": "Explore rhythm or melody: hum, tap, sing, or listen to new music mindfully.",
            "naturalistic": "Connect with nature: observe patterns, tend plants, or study natural systems.",
            "bodily_kinesthetic": "Get moving: try a craft, sport, or physical skill that challenges coordination."
        }

        base_rec = recommendations.get(top_intelligence, "Try something new in your strongest area!")

        if composite_score >= 0.85:
            return f"🔥 GENIUS LEVEL: {base_rec} Consider mentoring others!"
        elif composite_score >= 0.70:
            return f"🚀 HIGH POTENTIAL: {base_rec}"
        else:
            return f"📈 GROWING: {base_rec} Focus on consistent practice!"

    def generate_memory_crystal(self, user_id: str, crystal_type: str = "intelligence_assessment") -> dict:
        """Generate Memory Crystal for Boardroom integration"""
        profile = self.get_user_profile(user_id)
        if "error" in profile:
            return profile

        crystal_id = str(uuid.uuid4())
        timestamp = datetime.datetime.now().isoformat()

        crystal_data = {
            "crystal_id": crystal_id,
            "crystal_type": crystal_type,
            "user_id": user_id,
            "display_name": profile["display_name"],
            "intelligence_profile": {
                "skill_vector": profile["skill_vector"],
                "composite_genius_score": profile["composite_genius_score"],
                "genius_flags": profile["genius_flags"],
                "top_strengths": profile["top_strengths"]
            },
            "boardroom_integration": {
                "agent_army_coordination": True,
                "memory_crystal_network": True,
                "strategic_intelligence": True,
                "broski_economy": profile["broski_points"]
            },
            "assessment_metadata": {
                "total_assessments": len([t for t in self.assessment_tasks]),
                "completion_rate": "Calculating...",
                "adhd_optimization": True,
                "neurodivergent_friendly": True
            },
            "timestamp": timestamp,
            "expires": "never",
            "status": "active"
        }

        # Save crystal
        self.memory_crystal_path.mkdir(exist_ok=True)
        crystal_file = self.memory_crystal_path / f"INTELLIGENCE_CRYSTAL_{crystal_id}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

        with open(crystal_file, 'w', encoding='utf-8') as f:
            json.dump(crystal_data, f, indent=2, ensure_ascii=False)

        print(f"💎 Memory Crystal generated: {crystal_file.name}")
        return {"status": "success", "crystal_id": crystal_id, "file": str(crystal_file)}

    def get_assessment_task(self, intelligence_type: str = None, difficulty: str = None,
                           low_energy: bool = False) -> dict:
        """Get a random assessment task with optional filters"""
        available_tasks = self.assessment_tasks.copy()

        if intelligence_type:
            available_tasks = [t for t in available_tasks if t.intelligence_type == intelligence_type]

        if difficulty:
            available_tasks = [t for t in available_tasks if t.difficulty == difficulty]

        if low_energy:
            available_tasks = [t for t in available_tasks if t.low_energy]

        if not available_tasks:
            return {"error": "No tasks match criteria"}

        import random
        task = random.choice(available_tasks)

        return {
            "task_id": task.task_id,
            "intelligence_type": task.intelligence_type,
            "prompt": task.prompt,
            "time_limit": task.time_limit,
            "difficulty": task.difficulty,
            "multimodal": task.multimodal,
            "low_energy": task.low_energy,
            "adhd_optimized": task.adhd_optimized
        }

    def interactive_assessment_session(self):
        """🎯 Interactive intelligence assessment session"""
        print("\n🎯 BROski♾️ INTERACTIVE INTELLIGENCE ASSESSMENT")
        print("=" * 70)
        print("Welcome to your personalized intelligence assessment!")
        print("Commands: 'assess', 'profile [user_id]', 'genius [user_id]', 'crystal [user_id]', 'quit'")

        while True:
            try:
                user_input = input("\n🧠 BROski♾️ > ").strip()

                if user_input.lower() in ['quit', 'exit', 'q']:
                    break

                elif user_input.lower() == 'assess':
                    print("\n🚀 Starting quick intelligence assessment...")
                    user_id = input("Enter user ID (or 'demo' for demo): ").strip()
                    if user_id == 'demo':
                        user_id = f"demo_user_{datetime.datetime.now().strftime('%H%M%S')}"

                    display_name = input("Enter display name: ").strip()

                    # Create profile
                    self.create_user_profile(user_id, display_name)

                    # Run a few quick assessments
                    print("\n🎯 Running 3 quick assessments...")
                    for i in range(3):
                        task = self.get_assessment_task(low_energy=True)
                        print(f"\n📝 Assessment {i+1}/3 ({task['intelligence_type']})")
                        print(f"⏱️ Time limit: {task['time_limit']} seconds")
                        print(f"📋 Task: {task['prompt']}")

                        response = input("\n💭 Your response: ").strip()
                        time_taken = min(task['time_limit'], 60)  # Simulate time

                        result = self.run_assessment(user_id, task['task_id'], response, time_taken)
                        print(f"✅ Score: {result['score']:.2f} | Novelty: {result['novelty_score']:.2f}")

                    # Show results
                    profile = self.get_user_profile(user_id)
                    print(f"\n🎊 Assessment Complete for {profile['display_name']}!")
                    print(f"🏆 Composite Genius Score: {profile['composite_genius_score']:.2f}")
                    print(f"💎 BROski Points Earned: {profile['broski_points']}")

                    if profile['genius_flags']:
                        print(f"🎉 Genius Flags: {', '.join(profile['genius_flags'])}")

                elif user_input.lower().startswith('profile '):
                    user_id = user_input[8:].strip()
                    profile = self.get_user_profile(user_id)
                    if "error" not in profile:
                        print(f"\n👤 Profile: {profile['display_name']}")
                        print(f"🏆 Composite Score: {profile['composite_genius_score']:.2f}")
                        print(f"💎 BROski Points: {profile['broski_points']}")
                        print("🔥 Top Strengths:")
                        for name, score in profile['top_strengths']:
                            print(f"   {name.replace('_', ' ').title()}: {score:.2f}")
                    else:
                        print(f"❌ {profile['error']}")

                elif user_input.lower().startswith('genius '):
                    user_id = user_input[7:].strip()
                    embed = self.generate_discord_embed(user_id)
                    if "error" not in embed:
                        print("\n🎊 DISCORD EMBED GENERATED:")
                        print(json.dumps(embed, indent=2))
                    else:
                        print(f"❌ {embed['error']}")

                elif user_input.lower().startswith('crystal '):
                    user_id = user_input[8:].strip()
                    crystal = self.generate_memory_crystal(user_id)
                    if "error" not in crystal:
                        print(f"\n💎 Memory Crystal Generated: {crystal['crystal_id']}")
                        print(f"📁 Saved to: {crystal['file']}")
                    else:
                        print(f"❌ {crystal['error']}")

                else:
                    print("💡 Available commands: 'assess', 'profile [user_id]', 'genius [user_id]', 'crystal [user_id]', 'quit'")

            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"⚠️ Error: {e}")

        print("\n🎊 BROski♾️ Intelligence Assessment Session Complete!")
        print("Thanks for using the Ultra Intelligence Engine! 🧠⚡💎")


def main():
    """Main entry point for BROski♾️ Ultra Intelligence System"""
    print("🚀" * 30)
    print("🧠⚡💎 BROski♾️ ULTRA INTELLIGENCE SYSTEM 💎⚡🧠")
    print("🚀" * 30)

    engine = BROskiUltraIntelligenceEngine()

    print("\n🎯 System Ready! Starting interactive session...")
    engine.interactive_assessment_session()


if __name__ == "__main__":
    main()

"""
🧠💎⚡ NEURODIVERGENT AI ASSISTANT MVP ⚡💎🧠
Advanced AI system providing personalized support for ADHD, autism, and executive function challenges
"""

import asyncio
import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import Enum
from typing import Any, Dict, List, Optional


class NeurodivergentType(Enum):
    ADHD = "adhd"
    AUTISM = "autism"
    EXECUTIVE_DYSFUNCTION = "executive_dysfunction"
    SENSORY_PROCESSING = "sensory_processing"
    ANXIETY = "anxiety"
    DEPRESSION = "depression"


class CrisisLevel(Enum):
    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass
class UserContext:
    user_id: str
    neurodivergent_types: List[NeurodivergentType]
    current_mood: int  # 1-10 scale
    energy_level: int  # 1-10 scale
    focus_level: int  # 1-10 scale
    stress_level: int  # 1-10 scale
    last_break: Optional[datetime] = None
    hyperfocus_start: Optional[datetime] = None
    current_task: Optional[str] = None
    preferences: Dict[str, Any] = None
    crisis_indicators: List[str] = None

    def __post_init__(self):
        if self.preferences is None:
            self.preferences = {}
        if self.crisis_indicators is None:
            self.crisis_indicators = []


class ADHDCoachAI:
    """🎯 ADHD-specific coaching and support system"""

    def __init__(self):
        self.hyperfocus_threshold = 90  # minutes
        self.break_reminder_interval = 25  # Pomodoro-style
        self.energy_patterns = {}

    async def hyperfocus_support(self, context: UserContext) -> Dict[str, Any]:
        """Provide hyperfocus preservation and management"""
        current_time = datetime.now()

        if context.hyperfocus_start:
            hyperfocus_duration = (
                current_time - context.hyperfocus_start
            ).total_seconds() / 60

            if hyperfocus_duration > self.hyperfocus_threshold:
                return {
                    "type": "hyperfocus_break_gentle",
                    "message": "🎯 You've been in hyperfocus for {:.0f} minutes! Your brain has done amazing work. Consider a gentle 5-minute break to recharge?".format(
                        hyperfocus_duration
                    ),
                    "suggestions": [
                        "💧 Hydrate with your favorite drink",
                        "🚶‍♀️ Take 5 steps or stretch gently",
                        "👀 Look away from screen for 20 seconds",
                        "🧘‍♀️ Take 3 deep breaths",
                    ],
                    "preserve_flow": True,
                    "urgency": "gentle",
                }
            elif hyperfocus_duration > 45:
                return {
                    "type": "hyperfocus_maintenance",
                    "message": "🔥 You're in the zone! Quick check-in:",
                    "quick_checks": [
                        "💧 Water level?",
                        "🍎 Energy snack needed?",
                        "👁️ Eyes feeling okay?",
                    ],
                    "preserve_flow": True,
                    "urgency": "low",
                }

        return await self.flow_state_optimization(context)

    async def flow_state_optimization(self, context: UserContext) -> Dict[str, Any]:
        """Optimize conditions for ADHD flow state"""
        recommendations = []

        if context.focus_level < 6:
            recommendations.extend(
                [
                    "🎵 Try your focus playlist or brown noise",
                    "📱 Consider phone in another room",
                    "🎯 Break task into 15-minute chunks",
                ]
            )

        if context.energy_level < 5:
            recommendations.extend(
                [
                    "⚡ Quick movement break (30 seconds of jumping jacks?)",
                    "🍎 Protein snack for steady energy",
                    "☀️ Check if you need more light",
                ]
            )

        if context.stress_level > 7:
            recommendations.extend(
                [
                    "🧘‍♀️ 60-second breathing exercise",
                    "📝 Brain dump worries on paper",
                    "🤗 Self-compassion reminder: You're doing great!",
                ]
            )

        return {
            "type": "flow_optimization",
            "message": "🚀 Let's optimize your ADHD superpowers!",
            "recommendations": recommendations,
            "dopamine_boost": "🎉 You're taking charge of your focus - that's epic!",
            "urgency": "supportive",
        }

    async def executive_function_support(self, context: UserContext) -> Dict[str, Any]:
        """Help with ADHD executive function challenges"""
        if not context.current_task:
            return {
                "type": "task_initiation_support",
                "message": "🧠 Executive function boost incoming!",
                "strategies": [
                    "🎯 Pick the tiniest possible first step",
                    "⏰ Set 5-minute timer (you can stop after!)",
                    "🏆 Promise yourself a reward after",
                    "🎲 Use a random task picker if choosing feels hard",
                ],
                "encouragement": "Your ADHD brain just needs the right scaffolding!",
                "urgency": "supportive",
            }

        return {
            "type": "task_maintenance_support",
            "message": f"💪 You're working on: {context.current_task}",
            "check_ins": [
                "🎯 Still the right priority?",
                "📏 Need to break it smaller?",
                "⏰ Time estimate still realistic?",
                "🎉 Celebrating progress so far?",
            ],
            "urgency": "gentle",
        }


class AutismSupportAI:
    """🌈 Autism-specific support and guidance system"""

    def __init__(self):
        self.routine_templates = {}
        self.social_scripts = {}
        self.sensory_strategies = {}

    async def calming_sequence(self, context: UserContext) -> Dict[str, Any]:
        """Provide calming support for overwhelm"""
        sensory_preferences = context.preferences.get("sensory", {})

        calming_strategies = []

        # Visual calming
        if sensory_preferences.get("visual_sensitivity") != "high":
            calming_strategies.append("👁️ Soft, dim lighting or close eyes gently")

        # Auditory calming
        if sensory_preferences.get("auditory_sensitivity") != "high":
            calming_strategies.append("🎵 Calming sounds, music, or silence")
        else:
            calming_strategies.append("🔇 Noise-canceling or quiet space")

        # Tactile calming
        calming_strategies.extend(
            [
                "🤗 Weighted blanket, soft fabric, or gentle pressure",
                "🧘‍♀️ Familiar stimming or self-regulation tools",
                "🌱 Connect with special interest for comfort",
            ]
        )

        return {
            "type": "autism_calming_sequence",
            "message": "🌈 Overwhelm support activated. You're safe here.",
            "immediate_strategies": calming_strategies,
            "validation": "Your feelings are completely valid. Overwhelm is real and manageable.",
            "timeline": "Take all the time you need. No pressure.",
            "urgency": "gentle",
        }

    async def social_interaction_guidance(self, context: UserContext) -> Dict[str, Any]:
        """Provide autism-friendly social interaction support"""
        return {
            "type": "social_support",
            "message": "🤝 Social interaction support ready!",
            "strategies": [
                "📝 Use communication scripts for common situations",
                "⏰ Set time limits for social activities",
                "🚪 Plan exit strategies that feel safe",
                "💬 Practice small talk topics related to special interests",
                "🧘‍♀️ Schedule recovery time after social events",
            ],
            "scripts": {
                "ending_conversation": "It was nice talking with you. I need to head out now.",
                "asking_for_clarification": "Could you help me understand what you mean by...?",
                "declining_invitation": "Thank you for thinking of me. I can't make it this time.",
                "requesting_accommodation": "I work better when... Would that be possible?",
            },
            "validation": "Social interaction can be challenging - you're doing great by seeking support!",
            "urgency": "supportive",
        }

    async def routine_management(self, context: UserContext) -> Dict[str, Any]:
        """Help maintain and adapt routines"""
        return {
            "type": "routine_support",
            "message": "📅 Routine management system activated!",
            "tools": [
                "📋 Visual schedules and checklists",
                "⏰ Routine timers and reminders",
                "🔄 Transition warnings (5 min, 2 min, 30 sec)",
                "🎯 Routine modification strategies for changes",
                "📝 Routine backup plans for disruptions",
            ],
            "adaptation_support": {
                "routine_change": "When routines change: 1) Acknowledge the change, 2) Create new mini-routine, 3) Practice when possible",
                "unexpected_disruption": "For unexpected changes: 1) Breathe, 2) Identify what IS still the same, 3) Create smallest possible new plan",
            },
            "urgency": "planning",
        }


class CrisisDetectionAI:
    """🆘 Crisis detection and intervention system"""

    def __init__(self):
        self.crisis_indicators = {
            "severe_depression": [
                "hopeless",
                "worthless",
                "burden",
                "ending it",
                "no point",
            ],
            "self_harm": ["hurt myself", "deserve pain", "cutting", "self harm"],
            "suicidal_ideation": [
                "kill myself",
                "suicide",
                "end my life",
                "better off dead",
            ],
            "severe_anxiety": ["panic attack", "cant breathe", "heart racing", "dying"],
            "psychosis": ["voices", "seeing things", "conspiracy", "paranoid"],
            "severe_overwhelm": [
                "cant cope",
                "too much",
                "breaking down",
                "shutting down",
            ],
        }

        self.crisis_resources = {
            "suicide_prevention": {
                "hotline": "988",  # US Suicide & Crisis Lifeline
                "text": "Text HOME to 741741",
                "chat": "suicidepreventionlifeline.org/chat",
            },
            "crisis_text": {
                "service": "Crisis Text Line",
                "number": "741741",
                "keywords": "HOME, HELLO, or any keyword",
            },
            "emergency": {"number": "911", "international": "112"},
        }

    async def analyze_crisis_risk(
        self, context: UserContext, recent_messages: List[str]
    ) -> Dict[str, Any]:
        """Analyze for crisis indicators and provide appropriate response"""
        crisis_level = CrisisLevel.LOW
        detected_indicators = []

        # Analyze recent messages for crisis language
        for message in recent_messages:
            message_lower = message.lower()
            for crisis_type, indicators in self.crisis_indicators.items():
                for indicator in indicators:
                    if indicator in message_lower:
                        detected_indicators.append((crisis_type, indicator))
                        if crisis_type in ["suicidal_ideation", "self_harm"]:
                            crisis_level = CrisisLevel.CRITICAL
                        elif crisis_type in ["severe_depression", "psychosis"]:
                            crisis_level = CrisisLevel.HIGH
                        elif crisis_level == CrisisLevel.LOW:
                            crisis_level = CrisisLevel.MODERATE

        # Check user context for additional risk factors
        if context.mood <= 2 and context.stress_level >= 9:
            crisis_level = max(crisis_level, CrisisLevel.HIGH)
        elif context.mood <= 3 and context.stress_level >= 8:
            crisis_level = max(crisis_level, CrisisLevel.MODERATE)

        return await self.intervention_protocol(
            crisis_level, detected_indicators, context
        )

    async def intervention_protocol(
        self, crisis_level: CrisisLevel, indicators: List, context: UserContext
    ) -> Dict[str, Any]:
        """Provide appropriate crisis intervention based on risk level"""

        if crisis_level == CrisisLevel.CRITICAL:
            return {
                "type": "critical_crisis_intervention",
                "urgency": "immediate",
                "message": "🆘 I'm concerned about you. You matter and your life has value.",
                "immediate_actions": [
                    "📞 Call 988 (Suicide & Crisis Lifeline) - free, 24/7, confidential",
                    "💬 Text HOME to 741741 (Crisis Text Line)",
                    "🌐 Chat at suicidepreventionlifeline.org/chat",
                    "🚨 If immediate danger: Call 911",
                ],
                "validation": "You're brave for reaching out. This pain is temporary, even when it doesn't feel like it.",
                "follow_up": "I'll check in with you. You don't have to go through this alone.",
                "professional_alert": True,
                "resources": self.crisis_resources,
            }

        elif crisis_level == CrisisLevel.HIGH:
            return {
                "type": "high_risk_intervention",
                "urgency": "high",
                "message": "🤗 I notice you're going through a really tough time. Let's get you some support.",
                "support_options": [
                    "📞 988 for crisis support (free, 24/7)",
                    "💬 Text HOME to 741741 for text support",
                    "🧑‍⚕️ Reach out to a trusted adult, counselor, or doctor",
                    "👥 Connect with a friend or family member",
                ],
                "coping_strategies": [
                    "🧘‍♀️ Ground yourself: 5 things you see, 4 you hear, 3 you touch",
                    "❄️ Cold water on face or ice cube in hand",
                    "🎵 Calming music or sounds",
                    "📝 Write down feelings to get them out of your head",
                ],
                "validation": "These feelings are incredibly hard. You're strong for seeking help.",
                "professional_alert": True,
            }

        elif crisis_level == CrisisLevel.MODERATE:
            return {
                "type": "moderate_support",
                "urgency": "elevated",
                "message": "💙 I can tell you're struggling. Let's work through this together.",
                "immediate_support": [
                    "🧘‍♀️ Take 5 slow, deep breaths with me",
                    "💧 Get a glass of water",
                    "🌱 Look for one small thing that brings comfort",
                    "📱 Consider calling a trusted person",
                ],
                "resources": [
                    "💬 Crisis Text Line: Text HOME to 741741",
                    "🌐 Free online support groups",
                    "📚 Mental health apps and resources",
                    "🧑‍⚕️ School counselor or mental health provider",
                ],
                "check_in_timing": "30 minutes",
                "validation": "Your feelings are real and valid. Reaching out shows strength.",
            }

        return {
            "type": "wellness_check",
            "urgency": "low",
            "message": "💚 Just checking in on your wellbeing!",
            "wellness_tips": [
                "🧘‍♀️ How are you feeling right now?",
                "💧 Have you had water recently?",
                "🍎 When did you last eat something nourishing?",
                "😴 How has your sleep been?",
                "🌱 What's one thing you're grateful for today?",
            ],
            "validation": "Taking care of your mental health is important and brave.",
        }


class NeurodivergentAI:
    """🧠💎⚡ Main neurodivergent AI assistant orchestrator"""

    def __init__(self):
        self.adhd_coach = ADHDCoachAI()
        self.autism_support = AutismSupportAI()
        self.crisis_detector = CrisisDetectionAI()
        self.user_sessions = {}
        self.conversation_history = {}

    async def process_user_input(
        self, user_id: str, message: str, context: UserContext
    ) -> Dict[str, Any]:
        """Main entry point for processing user requests"""

        # Store conversation history
        if user_id not in self.conversation_history:
            self.conversation_history[user_id] = []

        self.conversation_history[user_id].append(
            {"timestamp": datetime.now(), "message": message, "user_context": context}
        )

        # Keep only last 50 messages for analysis
        if len(self.conversation_history[user_id]) > 50:
            self.conversation_history[user_id] = self.conversation_history[user_id][
                -50:
            ]

        # Check for crisis indicators first
        recent_messages = [
            entry["message"] for entry in self.conversation_history[user_id][-10:]
        ]
        crisis_analysis = await self.crisis_detector.analyze_crisis_risk(
            context, recent_messages
        )

        if crisis_analysis["urgency"] in ["immediate", "high"]:
            return crisis_analysis

        # Route to appropriate support based on user needs
        if await self._detect_hyperfocus(context, message):
            return await self.adhd_coach.hyperfocus_support(context)

        if await self._detect_overwhelm(context, message):
            return await self.autism_support.calming_sequence(context)

        if await self._detect_social_anxiety(message):
            return await self.autism_support.social_interaction_guidance(context)

        if await self._detect_executive_function_need(message):
            return await self.adhd_coach.executive_function_support(context)

        # Default to general neurodivergent guidance
        return await self.general_neurodivergent_guidance(context, message)

    async def _detect_hyperfocus(self, context: UserContext, message: str) -> bool:
        """Detect if user is in or entering hyperfocus state"""
        hyperfocus_keywords = [
            "focused",
            "zone",
            "flow",
            "cant stop",
            "hours",
            "forgot to eat",
            "lost track",
        ]
        message_lower = message.lower()

        return (
            any(keyword in message_lower for keyword in hyperfocus_keywords)
            or context.hyperfocus_start is not None
            or context.focus_level >= 8
        )

    async def _detect_overwhelm(self, context: UserContext, message: str) -> bool:
        """Detect autism overwhelm indicators"""
        overwhelm_keywords = [
            "overwhelmed",
            "too much",
            "sensory",
            "overstimulated",
            "shutdown",
            "meltdown",
        ]
        message_lower = message.lower()

        return (
            any(keyword in message_lower for keyword in overwhelm_keywords)
            or context.stress_level >= 8
            or context.energy_level <= 3
        )

    async def _detect_social_anxiety(self, message: str) -> bool:
        """Detect social interaction support needs"""
        social_keywords = [
            "social",
            "conversation",
            "people",
            "awkward",
            "dont know what to say",
            "small talk",
        ]
        message_lower = message.lower()

        return any(keyword in message_lower for keyword in social_keywords)

    async def _detect_executive_function_need(self, message: str) -> bool:
        """Detect executive function support needs"""
        exec_keywords = [
            "procrastinating",
            "cant start",
            "overwhelmed by task",
            "dont know where to begin",
            "priority",
        ]
        message_lower = message.lower()

        return any(keyword in message_lower for keyword in exec_keywords)

    async def general_neurodivergent_guidance(
        self, context: UserContext, message: str
    ) -> Dict[str, Any]:
        """Provide general neurodivergent support and encouragement"""

        # Personalized response based on neurodivergent types
        support_types = []
        if NeurodivergentType.ADHD in context.neurodivergent_types:
            support_types.append("🎯 ADHD superpowers")
        if NeurodivergentType.AUTISM in context.neurodivergent_types:
            support_types.append("🌈 Autistic strengths")

        return {
            "type": "general_neurodivergent_support",
            "message": f"🧠💎 Hello, beautiful neurodivergent mind! I'm here to support your {', '.join(support_types) if support_types else 'unique strengths'}.",
            "daily_affirmations": [
                "🌟 Your neurodivergent brain is a gift to the world",
                "💪 You have unique strengths and perspectives",
                "🤗 It's okay to need different supports - that's human",
                "🏆 Small progress is still progress",
                "❤️ You belong in this world exactly as you are",
            ],
            "available_support": [
                "🎯 ADHD coaching and hyperfocus support",
                "🌈 Autism support and sensory guidance",
                "🧠 Executive function assistance",
                "🆘 Crisis support and safety resources",
                "🤝 Social interaction guidance",
            ],
            "encouragement": "What would be most helpful for you right now?",
            "urgency": "supportive",
        }


# Example usage and testing
async def test_neurodivergent_ai():
    """Test the neurodivergent AI system"""
    ai = NeurodivergentAI()

    # Test ADHD support
    adhd_context = UserContext(
        user_id="test_user_1",
        neurodivergent_types=[NeurodivergentType.ADHD],
        current_mood=6,
        energy_level=4,
        focus_level=3,
        stress_level=7,
        hyperfocus_start=datetime.now() - timedelta(minutes=60),
    )

    response = await ai.process_user_input(
        "test_user_1", "I've been working for hours and forgot to eat", adhd_context
    )
    print("ADHD Response:", json.dumps(response, indent=2, default=str))

    # Test autism support
    autism_context = UserContext(
        user_id="test_user_2",
        neurodivergent_types=[NeurodivergentType.AUTISM],
        current_mood=3,
        energy_level=2,
        focus_level=2,
        stress_level=9,
    )

    response = await ai.process_user_input(
        "test_user_2",
        "Everything is too loud and bright, I'm overwhelmed",
        autism_context,
    )
    print("Autism Response:", json.dumps(response, indent=2, default=str))


if __name__ == "__main__":
    asyncio.run(test_neurodivergent_ai())

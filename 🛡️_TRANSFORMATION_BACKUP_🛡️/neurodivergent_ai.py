#!/usr/bin/env python3
"""
🧠💎⚡ NEURODIVERGENT AI ASSISTANT MVP - HYPERFOCUS ZONE ⚡💎🧠
Basic neurodivergent support AI for ADHD, autism, and executive function assistance
"""

import asyncio
import logging
from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import Enum
from typing import Any, Dict, List

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class NeurodivergentType(Enum):
    ADHD = "adhd"
    AUTISM = "autism"
    EXECUTIVE_FUNCTION = "executive_function"
    ANXIETY = "anxiety"
    GENERAL = "general"


class CrisisLevel(Enum):
    NONE = "none"
    MILD_CONCERN = "mild"
    ELEVATED = "elevated"
    IMMEDIATE = "immediate"


@dataclass
class UserContext:
    user_id: str
    session_start: datetime
    current_activity: str
    energy_level: int  # 1-10 scale
    focus_state: str  # "hyperfocus", "distracted", "balanced", "overwhelmed"
    last_interaction: datetime
    neurodivergent_profile: List[NeurodivergentType]
    crisis_indicators: List[str]
    preferences: Dict[str, Any]


@dataclass
class SupportResponse:
    response_type: str
    message: str
    suggestions: List[str]
    urgency: str
    follow_up_needed: bool
    resources: List[str]
    estimated_help_level: int  # 1-10 scale


class ADHDCoachAI:
    """AI assistant specifically designed for ADHD support"""

    def __init__(self):
        self.hyperfocus_thresholds = {
            "mild": 60,  # 1 hour
            "moderate": 120,  # 2 hours
            "intense": 180,  # 3 hours
        }

    async def analyze_adhd_state(self, context: UserContext) -> Dict[str, Any]:
        """Analyze current ADHD-related state and needs"""
        session_duration = (datetime.now() - context.session_start).total_seconds() / 60

        analysis = {
            "hyperfocus_detected": session_duration
            > self.hyperfocus_thresholds["mild"],
            "session_duration_minutes": session_duration,
            "break_recommended": session_duration > 90,
            "hydration_reminder": session_duration > 60,
            "movement_needed": session_duration > 120,
            "dopamine_status": self._assess_dopamine_level(context),
            "attention_state": context.focus_state,
        }

        return analysis

    def _assess_dopamine_level(self, context: UserContext) -> str:
        """Assess likely dopamine levels based on activity and energy"""
        if context.energy_level >= 8 and context.focus_state == "hyperfocus":
            return "high"
        elif context.energy_level <= 4 or context.focus_state == "distracted":
            return "low"
        else:
            return "balanced"

    async def hyperfocus_support(self, context: UserContext) -> SupportResponse:
        """Provide support during hyperfocus sessions"""
        analysis = await self.analyze_adhd_state(context)

        if analysis["session_duration_minutes"] > 180:
            message = "🌟 Amazing hyperfocus session! You've been in the zone for over 3 hours. Your brain has done incredible work!"
            suggestions = [
                "Consider taking a 15-20 minute break to recharge",
                "Grab some water and a healthy snack",
                "Do some gentle movement or stretching",
                "Save your work - hyperfocus sessions are precious!",
                "Set a gentle reminder to check in again in 30 minutes",
            ]
            urgency = "gentle_suggestion"
        elif analysis["session_duration_minutes"] > 120:
            message = "⚡ You're in a fantastic flow state! Your ADHD brain is performing beautifully."
            suggestions = [
                "Quick hydration check - grab some water during this flow!",
                "Maybe save your work as you go",
                "You're doing amazing - trust your hyperfocus!",
            ]
            urgency = "low"
        else:
            message = (
                "🎯 Hyperfocus mode detected! Your brain is in its element right now."
            )
            suggestions = [
                "Enjoy this focused state - it's one of your superpowers!",
                "Stay hydrated and comfortable",
                "Let the flow happen naturally",
            ]
            urgency = "minimal"

        return SupportResponse(
            response_type="adhd_hyperfocus_support",
            message=message,
            suggestions=suggestions,
            urgency=urgency,
            follow_up_needed=analysis["session_duration_minutes"] > 180,
            resources=["ADHD hyperfocus guide", "Break timing strategies"],
            estimated_help_level=8,
        )

    async def attention_regulation_support(
        self, context: UserContext
    ) -> SupportResponse:
        """Help with attention regulation challenges"""
        if context.focus_state == "distracted":
            message = "🧠 Having trouble focusing? That's totally normal for ADHD brains - let's find what works for you right now."
            suggestions = [
                "Try the 2-minute rule: just start for 2 minutes",
                "Change your environment - sometimes a different spot helps",
                "Use body doubling - work alongside someone (virtually or in person)",
                "Try some background white noise or focus music",
                "Break the task into smaller, more manageable pieces",
            ]
            urgency = "supportive"
        elif context.focus_state == "overwhelmed":
            message = "💙 Feeling overwhelmed? Let's break this down into manageable pieces. Your ADHD brain works best with clear, simple steps."
            suggestions = [
                "Take 5 deep breaths - give your nervous system a moment",
                "Write down everything on your mind (brain dump)",
                "Pick just ONE small thing to focus on right now",
                "Use the 'good enough' approach - perfection isn't the goal",
                "Remember: you don't have to do everything today",
            ]
            urgency = "supportive"
        else:
            message = "✨ Your attention is balanced right now - great job! Here are some ways to maintain this state."
            suggestions = [
                "Keep doing what you're doing - you've found a good rhythm",
                "Set a gentle timer to check in with yourself in 45 minutes",
                "Stay aware of your energy levels",
                "Celebrate this balanced state - it's an achievement!",
            ]
            urgency = "low"

        return SupportResponse(
            response_type="adhd_attention_support",
            message=message,
            suggestions=suggestions,
            urgency=urgency,
            follow_up_needed=context.focus_state == "overwhelmed",
            resources=["ADHD focus strategies", "Attention regulation techniques"],
            estimated_help_level=7,
        )


class AutismSupportAI:
    """AI assistant specifically designed for autism support"""

    async def sensory_optimization(self, context: UserContext) -> SupportResponse:
        """Optimize interface and environment for sensory preferences"""
        sensory_preferences = context.preferences.get("sensory", {})

        message = "🌈 Let's optimize your sensory experience for comfort and focus."
        suggestions = []

        # Motion sensitivity
        if sensory_preferences.get("motion_sensitive", False):
            suggestions.append("Reduced motion mode enabled - animations minimized")
            suggestions.append("Predictable transitions only - no surprise movements")

        # Light sensitivity
        if sensory_preferences.get("light_sensitive", False):
            suggestions.append(
                "Consider using dark mode or adjusting screen brightness"
            )
            suggestions.append("Blue light filter might help with eye comfort")

        # Sound sensitivity
        if sensory_preferences.get("sound_sensitive", False):
            suggestions.append("Audio notifications are muted as requested")
            suggestions.append("Visual indicators are being used instead of sounds")

        # General sensory support
        suggestions.extend(
            [
                "Your sensory preferences are being respected in the interface",
                "Remember: sensory needs are valid and important",
                "Take breaks in quiet, comfortable spaces when needed",
            ]
        )

        return SupportResponse(
            response_type="autism_sensory_support",
            message=message,
            suggestions=suggestions,
            urgency="supportive",
            follow_up_needed=False,
            resources=["Sensory regulation strategies", "Autism sensory guide"],
            estimated_help_level=8,
        )

    async def social_interaction_support(self, context: UserContext) -> SupportResponse:
        """Provide support for social interactions"""
        message = "🤝 Social interactions can be complex - you're doing great by being here and connecting with others."

        suggestions = [
            "Remember: there's no 'wrong' way to communicate authentically",
            "Take breaks from social interaction when you need them",
            "Your perspective and insights are valuable to this community",
            "It's okay to communicate differently - direct communication is often refreshing",
            "If you're unsure about social cues, asking for clarification is perfectly fine",
        ]

        # Add specific support based on context
        if context.current_activity == "community_posting":
            suggestions.extend(
                [
                    "Your special interests and detailed knowledge are welcome here",
                    "Don't worry about being 'too much' - authentic enthusiasm is beautiful",
                ]
            )
        elif context.current_activity == "group_discussion":
            suggestions.extend(
                [
                    "It's okay to take time to process before responding",
                    "Your thoughtful, analytical approach adds value to discussions",
                ]
            )

        return SupportResponse(
            response_type="autism_social_support",
            message=message,
            suggestions=suggestions,
            urgency="supportive",
            follow_up_needed=False,
            resources=["Social interaction tips", "Autism communication guide"],
            estimated_help_level=7,
        )

    async def routine_support(self, context: UserContext) -> SupportResponse:
        """Support for routine management and change navigation"""
        message = "🔄 Routines and predictability help autistic brains feel safe and function well."

        suggestions = [
            "Your need for routine and predictability is completely valid",
            "It's okay to have preferences about how things are organized",
            "Small changes to routine are manageable - you can adapt gradually",
            "Your attention to detail and pattern recognition are strengths",
            "Take time to process changes at your own pace",
        ]

        return SupportResponse(
            response_type="autism_routine_support",
            message=message,
            suggestions=suggestions,
            urgency="supportive",
            follow_up_needed=False,
            resources=["Routine management strategies", "Change adaptation techniques"],
            estimated_help_level=6,
        )


class ExecutiveFunctionAI:
    """AI assistant for executive function support"""

    async def task_breakdown_assistance(self, context: UserContext) -> SupportResponse:
        """Help break down complex tasks into manageable steps"""
        message = "🎯 Executive function challenges are real - let's break this down into clear, actionable steps."

        suggestions = [
            "Start with a brain dump - write down everything related to the task",
            "Identify the very first small step you can take (2-5 minutes max)",
            "Don't worry about the whole project - just focus on the next step",
            "Use external memory aids: timers, reminders, lists, visual cues",
            "Celebrate completing each small step - progress is progress!",
        ]

        if context.focus_state == "overwhelmed":
            suggestions.insert(
                0,
                "Take a moment to breathe - overwhelm is a sign you need support, not judgment",
            )
            suggestions.insert(1, "Choose just ONE task to focus on right now")

        return SupportResponse(
            response_type="executive_function_support",
            message=message,
            suggestions=suggestions,
            urgency="helpful",
            follow_up_needed=context.focus_state == "overwhelmed",
            resources=["Task breakdown templates", "Executive function strategies"],
            estimated_help_level=8,
        )

    async def priority_management(self, context: UserContext) -> SupportResponse:
        """Help with prioritization and decision making"""
        message = "📋 Prioritizing can be challenging when everything feels important. Let's find a system that works for your brain."

        suggestions = [
            "Try the 'Good, Better, Best' method: categorize tasks into these three groups",
            "Ask yourself: 'What happens if this doesn't get done today?'",
            "Use the 2-minute rule: if it takes less than 2 minutes, do it now",
            "Consider your energy levels - match hard tasks to high-energy times",
            "Remember: you can't do everything, and that's perfectly human",
        ]

        return SupportResponse(
            response_type="priority_management",
            message=message,
            suggestions=suggestions,
            urgency="helpful",
            follow_up_needed=False,
            resources=["Priority management tools", "Decision-making frameworks"],
            estimated_help_level=7,
        )


class CrisisDetectionAI:
    """AI system for detecting and responding to mental health crises"""

    def __init__(self):
        self.crisis_indicators = {
            "immediate": [
                "suicide",
                "self-harm",
                "hurt myself",
                "end it all",
                "give up",
                "can't go on",
                "no point",
                "better off dead",
            ],
            "elevated": [
                "overwhelming",
                "can't cope",
                "falling apart",
                "breaking down",
                "too much",
                "can't handle",
                "exhausted",
                "burnt out",
            ],
            "mild": [
                "struggling",
                "difficult day",
                "stressed",
                "worried",
                "anxious",
                "sad",
                "tired",
                "frustrated",
            ],
        }

    async def assess_crisis_level(self, context: UserContext) -> CrisisLevel:
        """Assess crisis level based on user context and indicators"""
        crisis_text = " ".join(context.crisis_indicators).lower()

        # Check for immediate crisis indicators
        for indicator in self.crisis_indicators["immediate"]:
            if indicator in crisis_text:
                return CrisisLevel.IMMEDIATE

        # Check for elevated concern
        for indicator in self.crisis_indicators["elevated"]:
            if indicator in crisis_text:
                return CrisisLevel.ELEVATED

        # Check for mild concern
        for indicator in self.crisis_indicators["mild"]:
            if indicator in crisis_text:
                return CrisisLevel.MILD_CONCERN

        return CrisisLevel.NONE

    async def crisis_intervention(self, context: UserContext) -> SupportResponse:
        """Provide appropriate crisis intervention response"""
        crisis_level = await self.assess_crisis_level(context)

        if crisis_level == CrisisLevel.IMMEDIATE:
            message = "🚨 I'm concerned about you and want to help. You matter, and there are people who want to support you right now."
            suggestions = [
                "Please reach out to a crisis helpline immediately:",
                "• National Suicide Prevention Lifeline: 988 (US)",
                "• Crisis Text Line: Text HOME to 741741",
                "• Or call emergency services: 911",
                "You are not alone, and this pain won't last forever",
                "Your life has value and meaning",
            ]
            urgency = "immediate"
            follow_up = True

        elif crisis_level == CrisisLevel.ELEVATED:
            message = "💙 I can sense you're going through a really difficult time. Your feelings are valid, and you deserve support."
            suggestions = [
                "Consider reaching out to a counselor or therapist",
                "Connect with a trusted friend or family member",
                "Take things one moment at a time - you don't have to solve everything today",
                "Remember: asking for help is a sign of strength, not weakness",
                "You've gotten through difficult times before - you have that strength in you",
            ]
            urgency = "high"
            follow_up = True

        elif crisis_level == CrisisLevel.MILD_CONCERN:
            message = "🌱 It sounds like you're having a challenging time. That's completely human, and it's okay to struggle sometimes."
            suggestions = [
                "Take some deep breaths and ground yourself in the present moment",
                "Remember that difficult feelings are temporary",
                "Practice self-compassion - treat yourself like you would a good friend",
                "Consider doing something small that usually brings you comfort",
                "You don't have to be 'productive' when you're struggling - just being is enough",
            ]
            urgency = "supportive"
            follow_up = False

        else:
            message = "✨ You seem to be in a stable place right now. Remember to check in with yourself regularly."
            suggestions = [
                "Continue practicing self-care and awareness",
                "Celebrate the small wins in your day",
                "Stay connected with your support network",
                "Remember that seeking help is always okay",
            ]
            urgency = "low"
            follow_up = False

        return SupportResponse(
            response_type="crisis_intervention",
            message=message,
            suggestions=suggestions,
            urgency=urgency,
            follow_up_needed=follow_up,
            resources=[
                "Crisis resources",
                "Mental health support",
                "Professional help directory",
            ],
            estimated_help_level=(
                10
                if crisis_level in [CrisisLevel.IMMEDIATE, CrisisLevel.ELEVATED]
                else 6
            ),
        )


class NeurodivergentAI:
    """Main neurodivergent AI assistant coordinating all specialized modules"""

    def __init__(self):
        self.adhd_coach = ADHDCoachAI()
        self.autism_support = AutismSupportAI()
        self.executive_function_assistant = ExecutiveFunctionAI()
        self.crisis_detector = CrisisDetectionAI()

        logger.info("🧠 Neurodivergent AI Assistant initialized and ready to help!")

    async def analyze_user_state(self, context: UserContext) -> Dict[str, Any]:
        """Analyze user's current state and determine support needs"""
        analysis = {
            "primary_needs": [],
            "support_priority": "general",
            "intervention_required": False,
            "follow_up_needed": False,
        }

        # Check for crisis indicators first
        crisis_level = await self.crisis_detector.assess_crisis_level(context)
        if crisis_level != CrisisLevel.NONE:
            analysis["primary_needs"].append("crisis_support")
            analysis["support_priority"] = "crisis"
            analysis["intervention_required"] = True
            return analysis

        # Analyze based on neurodivergent profile
        if NeurodivergentType.ADHD in context.neurodivergent_profile:
            adhd_analysis = await self.adhd_coach.analyze_adhd_state(context)
            if adhd_analysis["hyperfocus_detected"]:
                analysis["primary_needs"].append("adhd_hyperfocus")
            if context.focus_state in ["distracted", "overwhelmed"]:
                analysis["primary_needs"].append("adhd_attention")

        if NeurodivergentType.AUTISM in context.neurodivergent_profile:
            if context.current_activity in ["community_posting", "group_discussion"]:
                analysis["primary_needs"].append("autism_social")
            if context.energy_level <= 4:
                analysis["primary_needs"].append("autism_sensory")

        if NeurodivergentType.EXECUTIVE_FUNCTION in context.neurodivergent_profile:
            if context.focus_state == "overwhelmed":
                analysis["primary_needs"].append("executive_function")

        # Set priority based on most urgent need
        if "adhd_hyperfocus" in analysis["primary_needs"]:
            analysis["support_priority"] = "adhd_hyperfocus"
        elif "executive_function" in analysis["primary_needs"]:
            analysis["support_priority"] = "executive_function"
        elif analysis["primary_needs"]:
            analysis["support_priority"] = analysis["primary_needs"][0]

        return analysis

    async def provide_support(self, context: UserContext) -> SupportResponse:
        """Provide personalized neurodivergent support based on user context"""
        try:
            # Analyze user state
            analysis = await self.analyze_user_state(context)

            # Provide appropriate support
            if analysis["support_priority"] == "crisis":
                return await self.crisis_detector.crisis_intervention(context)
            elif analysis["support_priority"] == "adhd_hyperfocus":
                return await self.adhd_coach.hyperfocus_support(context)
            elif analysis["support_priority"] == "adhd_attention":
                return await self.adhd_coach.attention_regulation_support(context)
            elif analysis["support_priority"] == "autism_social":
                return await self.autism_support.social_interaction_support(context)
            elif analysis["support_priority"] == "autism_sensory":
                return await self.autism_support.sensory_optimization(context)
            elif analysis["support_priority"] == "executive_function":
                return (
                    await self.executive_function_assistant.task_breakdown_assistance(
                        context
                    )
                )
            else:
                return await self.general_neurodivergent_support(context)

        except Exception as e:
            logger.error(f"Error providing support: {e}")
            return SupportResponse(
                response_type="error_recovery",
                message="I'm having a technical difficulty right now, but I'm still here to support you. Please try again in a moment.",
                suggestions=[
                    "Try refreshing or restarting the assistant",
                    "Contact support if the issue persists",
                ],
                urgency="low",
                follow_up_needed=False,
                resources=["Technical support"],
                estimated_help_level=3,
            )

    async def general_neurodivergent_support(
        self, context: UserContext
    ) -> SupportResponse:
        """Provide general neurodivergent support and encouragement"""
        message = "🌟 Hello! I'm here to support you as a neurodivergent person. Your brain works beautifully, just differently."

        suggestions = [
            "Remember: neurodivergence is a difference, not a deficit",
            "Your unique perspective and way of thinking are valuable",
            "It's okay to need accommodations - that's just good self-care",
            "You belong in this community and your contributions matter",
            "Take things at your own pace - there's no rush",
        ]

        # Add specific encouragement based on profile
        if NeurodivergentType.ADHD in context.neurodivergent_profile:
            suggestions.append(
                "Your ADHD traits like creativity and hyperfocus are genuine superpowers"
            )

        if NeurodivergentType.AUTISM in context.neurodivergent_profile:
            suggestions.append(
                "Your attention to detail and deep expertise are incredible strengths"
            )

        return SupportResponse(
            response_type="general_support",
            message=message,
            suggestions=suggestions,
            urgency="supportive",
            follow_up_needed=False,
            resources=["Neurodivergent community resources", "Self-advocacy guides"],
            estimated_help_level=6,
        )


# Example usage and testing
async def main():
    """Test the neurodivergent AI assistant"""
    ai = NeurodivergentAI()

    # Test ADHD hyperfocus scenario
    adhd_context = UserContext(
        user_id="test_user_1",
        session_start=datetime.now() - timedelta(hours=2, minutes=30),
        current_activity="coding_project",
        energy_level=9,
        focus_state="hyperfocus",
        last_interaction=datetime.now() - timedelta(minutes=15),
        neurodivergent_profile=[NeurodivergentType.ADHD],
        crisis_indicators=[],
        preferences={"break_reminders": True},
    )

    print("🧠 Testing ADHD Hyperfocus Support:")
    adhd_response = await ai.provide_support(adhd_context)
    print(f"Response: {adhd_response.message}")
    print(f"Suggestions: {adhd_response.suggestions}")
    print()

    # Test autism social support scenario
    autism_context = UserContext(
        user_id="test_user_2",
        session_start=datetime.now() - timedelta(minutes=30),
        current_activity="community_posting",
        energy_level=6,
        focus_state="balanced",
        last_interaction=datetime.now() - timedelta(minutes=5),
        neurodivergent_profile=[NeurodivergentType.AUTISM],
        crisis_indicators=[],
        preferences={"sensory": {"sound_sensitive": True}},
    )

    print("🌈 Testing Autism Social Support:")
    autism_response = await ai.provide_support(autism_context)
    print(f"Response: {autism_response.message}")
    print(f"Suggestions: {autism_response.suggestions}")
    print()

    # Test executive function support
    ef_context = UserContext(
        user_id="test_user_3",
        session_start=datetime.now() - timedelta(minutes=45),
        current_activity="task_planning",
        energy_level=4,
        focus_state="overwhelmed",
        last_interaction=datetime.now() - timedelta(minutes=2),
        neurodivergent_profile=[NeurodivergentType.EXECUTIVE_FUNCTION],
        crisis_indicators=["feeling overwhelmed", "too much to do"],
        preferences={},
    )

    print("🎯 Testing Executive Function Support:")
    ef_response = await ai.provide_support(ef_context)
    print(f"Response: {ef_response.message}")
    print(f"Suggestions: {ef_response.suggestions}")
    print()

    print("✅ Neurodivergent AI Assistant testing complete!")


if __name__ == "__main__":
    asyncio.run(main())

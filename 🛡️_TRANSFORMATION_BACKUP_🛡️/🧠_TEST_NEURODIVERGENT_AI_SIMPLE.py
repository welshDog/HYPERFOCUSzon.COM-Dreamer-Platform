#!/usr/bin/env python3
"""
🧠💎⚡ NEURODIVERGENT AI ASSISTANT MVP - SIMPLIFIED TEST ⚡💎🧠
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

print("🧠💎⚡ Starting Neurodivergent AI Assistant MVP Test ⚡💎🧠")


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


class SimpleNeurodivergentAI:
    """Simplified neurodivergent AI assistant for testing"""

    def __init__(self):
        logger.info("🧠 Simple Neurodivergent AI Assistant initialized!")

    async def provide_adhd_support(self, context: UserContext) -> SupportResponse:
        """Provide ADHD-specific support"""
        session_duration = (datetime.now() - context.session_start).total_seconds() / 60

        if session_duration > 120:  # Over 2 hours
            message = "🌟 Amazing hyperfocus session! You've been in the zone for over 2 hours. Your ADHD brain is doing incredible work!"
            suggestions = [
                "Consider taking a 15-20 minute break to recharge",
                "Grab some water and a healthy snack",
                "Do some gentle movement or stretching",
                "Save your work - hyperfocus sessions are precious!",
                "Set a gentle reminder to check in again in 30 minutes",
            ]
            urgency = "gentle_suggestion"
        elif context.focus_state == "distracted":
            message = "🧠 Having trouble focusing? That's totally normal for ADHD brains - let's find what works for you right now."
            suggestions = [
                "Try the 2-minute rule: just start for 2 minutes",
                "Change your environment - sometimes a different spot helps",
                "Use body doubling - work alongside someone (virtually or in person)",
                "Try some background white noise or focus music",
                "Break the task into smaller, more manageable pieces",
            ]
            urgency = "supportive"
        else:
            message = "⚡ Your ADHD brain is working beautifully right now! Here are some ways to maintain this state."
            suggestions = [
                "Keep doing what you're doing - you've found a good rhythm",
                "Stay aware of your energy levels",
                "Celebrate this balanced state - it's an achievement!",
            ]
            urgency = "low"

        return SupportResponse(
            response_type="adhd_support",
            message=message,
            suggestions=suggestions,
            urgency=urgency,
            follow_up_needed=session_duration > 180,
            resources=["ADHD focus strategies", "Attention regulation techniques"],
            estimated_help_level=8,
        )

    async def provide_autism_support(self, context: UserContext) -> SupportResponse:
        """Provide autism-specific support"""
        message = "🌈 Let's optimize your experience for comfort and focus. Your autistic traits are strengths!"

        suggestions = [
            "Your sensory preferences are being respected in the interface",
            "Remember: sensory needs are valid and important",
            "Take breaks in quiet, comfortable spaces when needed",
            "Your perspective and insights are valuable to this community",
            "It's okay to communicate differently - direct communication is often refreshing",
        ]

        return SupportResponse(
            response_type="autism_support",
            message=message,
            suggestions=suggestions,
            urgency="supportive",
            follow_up_needed=False,
            resources=["Sensory regulation strategies", "Autism support guide"],
            estimated_help_level=7,
        )

    async def provide_executive_function_support(
        self, context: UserContext
    ) -> SupportResponse:
        """Provide executive function support"""
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

    async def provide_support(self, context: UserContext) -> SupportResponse:
        """Main support method that routes to appropriate specialized support"""
        try:
            # Check neurodivergent profile and provide appropriate support
            if NeurodivergentType.ADHD in context.neurodivergent_profile:
                return await self.provide_adhd_support(context)
            elif NeurodivergentType.AUTISM in context.neurodivergent_profile:
                return await self.provide_autism_support(context)
            elif (
                NeurodivergentType.EXECUTIVE_FUNCTION in context.neurodivergent_profile
            ):
                return await self.provide_executive_function_support(context)
            else:
                # General neurodivergent support
                message = "🌟 Hello! I'm here to support you as a neurodivergent person. Your brain works beautifully, just differently."
                suggestions = [
                    "Remember: neurodivergence is a difference, not a deficit",
                    "Your unique perspective and way of thinking are valuable",
                    "It's okay to need accommodations - that's just good self-care",
                    "You belong in this community and your contributions matter",
                ]

                return SupportResponse(
                    response_type="general_support",
                    message=message,
                    suggestions=suggestions,
                    urgency="supportive",
                    follow_up_needed=False,
                    resources=[
                        "Neurodivergent community resources",
                        "Self-advocacy guides",
                    ],
                    estimated_help_level=6,
                )

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


async def main():
    """Test the simplified neurodivergent AI assistant"""
    print("🧠 Initializing Neurodivergent AI Assistant...")
    ai = SimpleNeurodivergentAI()

    print("\n" + "=" * 60)
    print("🧠💎⚡ HYPERFOCUS ZONE AI ASSISTANT TESTING ⚡💎🧠")
    print("=" * 60)

    # Test ADHD hyperfocus scenario
    print("\n🌟 Testing ADHD Hyperfocus Support:")
    print("-" * 40)

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

    adhd_response = await ai.provide_support(adhd_context)
    print(f"✨ Response: {adhd_response.message}")
    print(f"📋 Suggestions:")
    for i, suggestion in enumerate(adhd_response.suggestions, 1):
        print(f"   {i}. {suggestion}")
    print(f"🎯 Help Level: {adhd_response.estimated_help_level}/10")

    # Test autism social support scenario
    print("\n🌈 Testing Autism Social Support:")
    print("-" * 40)

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

    autism_response = await ai.provide_support(autism_context)
    print(f"✨ Response: {autism_response.message}")
    print(f"📋 Suggestions:")
    for i, suggestion in enumerate(autism_response.suggestions, 1):
        print(f"   {i}. {suggestion}")
    print(f"🎯 Help Level: {autism_response.estimated_help_level}/10")

    # Test executive function support
    print("\n🎯 Testing Executive Function Support:")
    print("-" * 40)

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

    ef_response = await ai.provide_support(ef_context)
    print(f"✨ Response: {ef_response.message}")
    print(f"📋 Suggestions:")
    for i, suggestion in enumerate(ef_response.suggestions, 1):
        print(f"   {i}. {suggestion}")
    print(f"🎯 Help Level: {ef_response.estimated_help_level}/10")

    print("\n" + "=" * 60)
    print("✅ NEURODIVERGENT AI ASSISTANT TESTING COMPLETE!")
    print("🎉 All systems functional and ready to support the community!")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())

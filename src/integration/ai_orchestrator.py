"""
🤖💎⚡ HYPERFOCUS ZONE AI INTEGRATION SYSTEM ⚡💎🤖
Complete integration of neurodivergent AI systems with frontend and community features
"""

import asyncio
import os

# Import our neurodivergent systems
import sys
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from ai.neurodivergent_assistant import NeurodivergentAI
from community.community_manager import NeurodivergentCommunityManager
from community.peer_support import NeurodivergentPeerSupportSystem
from safety.crisis_intervention import NeurodivergentSafetySystem


@dataclass
class AIIntegrationRequest:
    user_id: str
    request_type: str  # "chat", "support", "crisis", "community_help"
    content: str
    context: Dict[str, Any] = field(default_factory=dict)
    timestamp: datetime = field(default_factory=datetime.now)
    priority: str = "normal"  # low, normal, high, critical
    requires_human_review: bool = False


@dataclass
class AIResponse:
    response_id: str
    user_id: str
    ai_type: str
    response_content: str
    actions_taken: List[str] = field(default_factory=list)
    resources_provided: List[str] = field(default_factory=list)
    follow_up_needed: bool = False
    confidence_score: float = 0.0
    safety_flags: List[str] = field(default_factory=list)
    timestamp: datetime = field(default_factory=datetime.now)


class HyperfocusZoneAIOrchestrator:
    """🎯 Master AI orchestrator for all HYPERFOCUS Zone intelligent systems"""

    def __init__(self):
        # Initialize all AI systems
        self.neurodivergent_ai = NeurodivergentAI()
        self.community_manager = NeurodivergentCommunityManager()
        self.peer_support = NeurodivergentPeerSupportSystem()
        self.safety_system = NeurodivergentSafetySystem()

        # Integration state
        self.active_sessions: Dict[str, Dict] = {}
        self.user_contexts: Dict[str, Dict] = {}
        self.ai_responses: Dict[str, AIResponse] = {}

        # Performance monitoring
        self.performance_metrics = {
            "total_requests": 0,
            "crisis_interventions": 0,
            "successful_matches": 0,
            "community_violations": 0,
            "response_times": [],
            "user_satisfaction": [],
        }

    async def process_user_request(self, request: AIIntegrationRequest) -> AIResponse:
        """🎯 Main entry point for all AI interactions"""
        start_time = datetime.now()

        try:
            # Increment metrics
            self.performance_metrics["total_requests"] += 1

            # Safety screening first
            safety_result = await self.safety_system.analyze_safety_concern(
                content=request.content,
                user_id=request.user_id,
                context=request.context,
            )

            # Handle crisis situations immediately
            if safety_result["intervention_activated"]:
                return await self._handle_crisis_response(request, safety_result)

            # Route to appropriate AI system based on request type
            if request.request_type == "chat":
                return await self._handle_chat_request(request)
            elif request.request_type == "support":
                return await self._handle_support_request(request)
            elif request.request_type == "community_help":
                return await self._handle_community_request(request)
            else:
                return await self._handle_general_request(request)

        except Exception as e:
            # Error handling with safety fallback
            return await self._handle_error_response(request, str(e))

        finally:
            # Record response time
            response_time = (datetime.now() - start_time).total_seconds()
            self.performance_metrics["response_times"].append(response_time)

    async def _handle_crisis_response(
        self, request: AIIntegrationRequest, safety_result: Dict
    ) -> AIResponse:
        """🆘 Handle crisis situations with immediate intervention"""

        # Get crisis-specific AI response
        crisis_ai_response = await self.neurodivergent_ai.handle_crisis_situation(
            user_input=request.content,
            user_context=request.context,
            crisis_level=safety_result[
                "safety_assessment"
            ].recommended_intervention.value,
        )

        # Activate peer support if appropriate
        if safety_result["safety_assessment"].recommended_intervention.value in [
            "peer_support",
            "crisis_team",
        ]:
            support_request_data = {
                "requester_id": request.user_id,
                "support_types": ["crisis", "emotional"],
                "description": f"Crisis intervention needed: {request.content[:100]}...",
                "accommodation_needs": request.context.get("accommodation_needs", []),
            }

            peer_support_request = await self.peer_support.submit_support_request(
                support_request_data
            )

        response = AIResponse(
            response_id=f"crisis_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            user_id=request.user_id,
            ai_type="crisis_intervention",
            response_content=crisis_ai_response["response"],
            actions_taken=[
                "Crisis intervention activated",
                "Safety assessment completed",
                "Professional resources provided",
            ]
            + safety_result.get("actions_taken", []),
            resources_provided=crisis_ai_response.get("resources", []),
            follow_up_needed=True,
            confidence_score=safety_result["safety_assessment"].confidence_score,
            safety_flags=[
                "crisis_detected",
                safety_result["safety_assessment"].recommended_intervention.value,
            ],
        )

        # Update metrics
        self.performance_metrics["crisis_interventions"] += 1

        return response

    async def _handle_chat_request(self, request: AIIntegrationRequest) -> AIResponse:
        """💬 Handle general chat/conversation requests"""

        # Get user context and preferences
        user_context = self.user_contexts.get(request.user_id, {})
        enhanced_context = {**user_context, **request.context}

        # Route to appropriate AI specialist
        if any(
            topic in request.content.lower()
            for topic in ["adhd", "hyperfocus", "executive function"]
        ):
            ai_response = (
                await self.neurodivergent_ai.adhd_coach.provide_hyperfocus_support(
                    current_situation=request.content, user_context=enhanced_context
                )
            )
            ai_type = "adhd_coach"

        elif any(
            topic in request.content.lower()
            for topic in ["autism", "sensory", "stimming", "meltdown"]
        ):
            ai_response = (
                await self.neurodivergent_ai.autism_support.provide_sensory_support(
                    current_situation=request.content, user_context=enhanced_context
                )
            )
            ai_type = "autism_support"

        else:
            ai_response = await self.neurodivergent_ai.process_user_input(
                user_input=request.content, user_context=enhanced_context
            )
            ai_type = "general_neurodivergent"

        # Check if response triggers community features
        community_actions = await self._check_community_integration(
            request, ai_response
        )

        response = AIResponse(
            response_id=f"chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            user_id=request.user_id,
            ai_type=ai_type,
            response_content=ai_response.get("response", ""),
            actions_taken=ai_response.get("actions", []) + community_actions,
            resources_provided=ai_response.get("resources", []),
            follow_up_needed=ai_response.get("follow_up_needed", False),
            confidence_score=ai_response.get("confidence", 0.8),
        )

        return response

    async def _handle_support_request(
        self, request: AIIntegrationRequest
    ) -> AIResponse:
        """🤝 Handle peer support requests"""

        # Analyze support needs
        support_analysis = await self._analyze_support_needs(
            request.content, request.context
        )

        # Submit to peer support system
        support_request_data = {
            "requester_id": request.user_id,
            "support_types": support_analysis["support_types"],
            "description": request.content,
            "preferred_supporter_traits": support_analysis.get("preferred_traits", {}),
            "accommodation_needs": request.context.get("accommodation_needs", []),
        }

        peer_support_request = await self.peer_support.submit_support_request(
            support_request_data
        )

        # Get AI guidance while waiting for human support
        ai_guidance = await self.neurodivergent_ai.provide_immediate_support(
            user_input=request.content,
            user_context=request.context,
            support_types=support_analysis["support_types"],
        )

        response = AIResponse(
            response_id=f"support_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            user_id=request.user_id,
            ai_type="peer_support_integration",
            response_content=ai_guidance["response"],
            actions_taken=[
                "Peer support request submitted",
                "AI immediate support provided",
                "Matching process initiated",
            ],
            resources_provided=ai_guidance.get("resources", []),
            follow_up_needed=True,
            confidence_score=0.9,
        )

        # Update metrics
        self.performance_metrics["successful_matches"] += 1

        return response

    async def _handle_community_request(
        self, request: AIIntegrationRequest
    ) -> AIResponse:
        """🌈 Handle community-related requests"""

        # Analyze if user wants to post, join space, or get community help
        if "post" in request.content.lower() or "share" in request.content.lower():
            return await self._handle_community_post_request(request)
        elif "join" in request.content.lower() or "space" in request.content.lower():
            return await self._handle_space_recommendation_request(request)
        else:
            return await self._handle_general_community_help(request)

    async def _handle_community_post_request(
        self, request: AIIntegrationRequest
    ) -> AIResponse:
        """📝 Help user create community post"""

        # AI assistance for post creation
        post_assistance = await self.neurodivergent_ai.assist_with_communication(
            communication_goal="community_post",
            content=request.content,
            user_context=request.context,
        )

        # Suggest appropriate safe spaces
        suggested_spaces = await self._suggest_safe_spaces_for_content(
            request.content, request.user_id
        )

        response = AIResponse(
            response_id=f"community_post_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            user_id=request.user_id,
            ai_type="community_assistance",
            response_content=post_assistance["response"],
            actions_taken=[
                "Post assistance provided",
                "Safe spaces suggested",
                "Content guidance given",
            ],
            resources_provided=post_assistance.get("resources", [])
            + [
                f"Suggested safe spaces: {[space['name'] for space in suggested_spaces]}"
            ],
        )

        return response

    async def _suggest_safe_spaces_for_content(
        self, content: str, user_id: str
    ) -> List[Dict]:
        """🌈 Suggest appropriate safe spaces for user content"""

        # Analyze content for topic matching
        content_lower = content.lower()
        suggested_spaces = []

        # Check each safe space for relevance
        for space_id, space in self.community_manager.safe_spaces.items():
            space_score = 0

            # Match neurodivergent focus
            for focus in space.neurodivergent_focus:
                if focus.lower() in content_lower:
                    space_score += 3

            # Match keywords in space name/description
            space_text = (space.name + " " + space.description).lower()
            if any(word in content_lower for word in space_text.split()):
                space_score += 1

            # If relevant, add to suggestions
            if space_score > 0:
                suggested_spaces.append(
                    {
                        "space_id": space_id,
                        "name": space.name,
                        "description": space.description,
                        "relevance_score": space_score,
                    }
                )

        # Sort by relevance and return top 3
        suggested_spaces.sort(key=lambda x: x["relevance_score"], reverse=True)
        return suggested_spaces[:3]

    async def _analyze_support_needs(self, content: str, context: Dict) -> Dict:
        """🎯 Analyze what type of support the user needs"""

        content_lower = content.lower()
        support_types = []

        # Emotional support indicators
        if any(
            word in content_lower
            for word in ["sad", "overwhelmed", "anxious", "stressed", "alone"]
        ):
            support_types.append("emotional")

        # Executive function support
        if any(
            word in content_lower
            for word in [
                "procrastination",
                "organize",
                "priorities",
                "focus",
                "executive",
            ]
        ):
            support_types.append("executive_function")

        # Social skills support
        if any(
            word in content_lower
            for word in ["social", "conversation", "interaction", "communication"]
        ):
            support_types.append("social_skills")

        # Sensory support
        if any(
            word in content_lower
            for word in ["sensory", "overstimulated", "noise", "texture", "overwhelm"]
        ):
            support_types.append("sensory_support")

        # Default to emotional if no specific type detected
        if not support_types:
            support_types.append("emotional")

        # Analyze preferred supporter traits
        preferred_traits = {}
        if "autism" in content_lower:
            preferred_traits["neurodivergent_types"] = ["Autism"]
        if "adhd" in content_lower:
            preferred_traits["neurodivergent_types"] = ["ADHD"]

        return {
            "support_types": support_types,
            "preferred_traits": preferred_traits,
            "urgency": "normal",  # Could be enhanced with urgency detection
        }

    async def _check_community_integration(
        self, request: AIIntegrationRequest, ai_response: Dict
    ) -> List[str]:
        """🌈 Check if AI response should trigger community features"""

        actions = []

        # Check if user might benefit from community connection
        if any(
            phrase in ai_response.get("response", "").lower()
            for phrase in [
                "connect with others",
                "community support",
                "peer support",
                "you're not alone",
            ]
        ):
            actions.append("Community connection recommended")

        # Check if user expressed interest in sharing experience
        if any(
            phrase in request.content.lower()
            for phrase in ["share my experience", "help others", "tell my story"]
        ):
            actions.append("Community posting assistance offered")

        # Check if user needs peer support
        if any(
            phrase in request.content.lower()
            for phrase in [
                "need support",
                "struggling",
                "could use help",
                "feeling alone",
            ]
        ):
            actions.append("Peer support matching recommended")

        return actions

    async def _handle_general_request(
        self, request: AIIntegrationRequest
    ) -> AIResponse:
        """🤖 Handle general AI requests that don't fit other categories"""

        ai_response = await self.neurodivergent_ai.process_user_input(
            user_input=request.content, user_context=request.context
        )

        response = AIResponse(
            response_id=f"general_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            user_id=request.user_id,
            ai_type="general_neurodivergent",
            response_content=ai_response.get("response", ""),
            actions_taken=ai_response.get("actions", []),
            resources_provided=ai_response.get("resources", []),
            follow_up_needed=ai_response.get("follow_up_needed", False),
            confidence_score=ai_response.get("confidence", 0.7),
        )

        return response

    async def _handle_error_response(
        self, request: AIIntegrationRequest, error: str
    ) -> AIResponse:
        """⚠️ Handle errors with graceful fallback"""

        fallback_response = """
        💙 I'm experiencing some technical difficulties right now, but I'm still here to help!

        Here are some immediate resources:
        🆘 Crisis support: 988 (Suicide & Crisis Lifeline)
        💬 Crisis text: Text HOME to 741741
        🌈 You're not alone - this community supports you

        Please try your request again in a moment, or reach out to our peer supporters if you need immediate help.
        """

        response = AIResponse(
            response_id=f"error_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            user_id=request.user_id,
            ai_type="error_handler",
            response_content=fallback_response,
            actions_taken=["Error handling activated", "Fallback resources provided"],
            resources_provided=["Crisis hotlines", "Community support"],
            safety_flags=["system_error"],
        )

        return response

    async def get_performance_metrics(self) -> Dict:
        """📊 Get AI system performance metrics"""

        avg_response_time = (
            sum(self.performance_metrics["response_times"])
            / len(self.performance_metrics["response_times"])
            if self.performance_metrics["response_times"]
            else 0
        )

        return {
            "total_requests_processed": self.performance_metrics["total_requests"],
            "crisis_interventions": self.performance_metrics["crisis_interventions"],
            "successful_support_matches": self.performance_metrics[
                "successful_matches"
            ],
            "community_violations_detected": self.performance_metrics[
                "community_violations"
            ],
            "average_response_time_seconds": round(avg_response_time, 2),
            "system_uptime": "99.9%",  # Would be calculated from actual uptime
            "user_satisfaction_score": (
                sum(self.performance_metrics["user_satisfaction"])
                / len(self.performance_metrics["user_satisfaction"])
                if self.performance_metrics["user_satisfaction"]
                else 0
            ),
            "active_sessions": len(self.active_sessions),
            "safety_status": "OPERATIONAL",
        }

    async def update_user_context(self, user_id: str, context_updates: Dict):
        """📝 Update user context for personalized AI responses"""

        if user_id not in self.user_contexts:
            self.user_contexts[user_id] = {}

        self.user_contexts[user_id].update(context_updates)

        # Store last update time
        self.user_contexts[user_id]["last_updated"] = datetime.now()


# Example integration with frontend
class FrontendAIBridge:
    """🌉 Bridge between frontend and AI systems"""

    def __init__(self, ai_orchestrator: HyperfocusZoneAIOrchestrator):
        self.ai_orchestrator = ai_orchestrator

    async def handle_frontend_request(self, frontend_data: Dict) -> Dict:
        """Handle requests from frontend components"""

        # Convert frontend request to AI request
        ai_request = AIIntegrationRequest(
            user_id=frontend_data["userId"],
            request_type=frontend_data["requestType"],
            content=frontend_data["content"],
            context=frontend_data.get("context", {}),
            priority=frontend_data.get("priority", "normal"),
        )

        # Process with AI orchestrator
        ai_response = await self.ai_orchestrator.process_user_request(ai_request)

        # Convert back to frontend format
        return {
            "responseId": ai_response.response_id,
            "content": ai_response.response_content,
            "actionsTaken": ai_response.actions_taken,
            "resources": ai_response.resources_provided,
            "followUpNeeded": ai_response.follow_up_needed,
            "confidenceScore": ai_response.confidence_score,
            "safetyFlags": ai_response.safety_flags,
            "timestamp": ai_response.timestamp.isoformat(),
        }


# Example usage and testing
async def test_ai_integration():
    """Test the complete AI integration system"""

    orchestrator = HyperfocusZoneAIOrchestrator()

    # Test chat request
    chat_request = AIIntegrationRequest(
        user_id="user123",
        request_type="chat",
        content="I'm having trouble focusing today and feeling overwhelmed",
        context={"neurodivergent_types": ["ADHD"], "current_mood": "overwhelmed"},
    )

    chat_response = await orchestrator.process_user_request(chat_request)
    print("Chat response:", chat_response.response_content)

    # Test support request
    support_request = AIIntegrationRequest(
        user_id="user123",
        request_type="support",
        content="I need help with executive function strategies",
        context={"support_preferences": {"communication_style": "direct"}},
    )

    support_response = await orchestrator.process_user_request(support_request)
    print("Support response:", support_response.response_content)

    # Get performance metrics
    metrics = await orchestrator.get_performance_metrics()
    print("Performance metrics:", metrics)


if __name__ == "__main__":
    asyncio.run(test_ai_integration())

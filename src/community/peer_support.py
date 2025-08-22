"""
🤝💙⚡ PEER SUPPORT SYSTEM FOR NEURODIVERGENT COMMUNITY ⚡💙🤝
Specialized peer support network with trauma-informed care and neurodivergent expertise
"""

import asyncio
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
from typing import Dict, List, Optional


class SupportType(Enum):
    EMOTIONAL = "emotional"
    PRACTICAL = "practical"
    CRISIS = "crisis"
    EXECUTIVE_FUNCTION = "executive_function"
    SOCIAL_SKILLS = "social_skills"
    SENSORY_SUPPORT = "sensory_support"
    ADVOCACY = "advocacy"
    RESOURCE_CONNECTION = "resource_connection"


class SupportStatus(Enum):
    REQUESTED = "requested"
    MATCHED = "matched"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    ESCALATED = "escalated"


class CrisisLevel(Enum):
    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass
class PeerSupporter:
    supporter_id: str
    username: str
    neurodivergent_types: List[str]
    specializations: List[SupportType] = field(default_factory=list)
    lived_experience: List[str] = field(
        default_factory=list
    )  # Specific challenges they've navigated
    training_completed: List[str] = field(default_factory=list)
    languages: List[str] = field(default_factory=lambda: ["English"])
    availability: Dict[str, any] = field(default_factory=dict)
    current_capacity: int = 0
    max_capacity: int = 5
    crisis_trained: bool = False
    trauma_informed: bool = False
    certification_date: Optional[datetime] = None
    total_support_hours: int = 0
    positive_feedback_count: int = 0
    active_since: datetime = field(default_factory=datetime.now)


@dataclass
class SupportRequest:
    request_id: str
    requester_id: str
    support_types: List[SupportType]
    description: str
    urgency_level: CrisisLevel = CrisisLevel.LOW
    preferred_supporter_traits: Dict[str, any] = field(default_factory=dict)
    anonymous: bool = False
    trigger_warnings: List[str] = field(default_factory=list)
    accommodation_needs: List[str] = field(default_factory=list)
    created_timestamp: datetime = field(default_factory=datetime.now)
    matched_supporter_id: Optional[str] = None
    status: SupportStatus = SupportStatus.REQUESTED
    estimated_duration: Optional[timedelta] = None
    follow_up_needed: bool = False


@dataclass
class SupportSession:
    session_id: str
    request_id: str
    supporter_id: str
    requester_id: str
    start_time: datetime
    end_time: Optional[datetime] = None
    support_provided: List[SupportType] = field(default_factory=list)
    techniques_used: List[str] = field(default_factory=list)
    outcomes: List[str] = field(default_factory=list)
    referrals_made: List[str] = field(default_factory=list)
    follow_up_scheduled: bool = False
    session_notes: str = ""  # Private notes for continuity
    effectiveness_rating: Optional[int] = None  # 1-5 scale


class NeurodivergentPeerSupportSystem:
    """🤝 Comprehensive peer support system for neurodivergent community"""

    def __init__(self):
        self.supporters: Dict[str, PeerSupporter] = {}
        self.support_requests: Dict[str, SupportRequest] = {}
        self.active_sessions: Dict[str, SupportSession] = {}
        self.completed_sessions: Dict[str, SupportSession] = {}
        self.crisis_escalation_protocols = self._initialize_crisis_protocols()
        self.matching_algorithm = SupportMatchingEngine()
        self.training_modules = self._initialize_training_modules()

    def _initialize_crisis_protocols(self) -> Dict[str, any]:
        """Initialize crisis escalation and intervention protocols"""
        return {
            "critical": {
                "immediate_actions": [
                    "Connect to professional crisis services immediately",
                    "Stay with person until professional help arrives",
                    "Alert crisis team and administrators",
                    "Document all interventions taken",
                ],
                "resources": {
                    "suicide_hotline": "988",
                    "crisis_text": "741741",
                    "emergency": "911",
                    "lgbtq_crisis": "1-866-488-7386",
                    "trans_lifeline": "877-565-8860",
                },
                "escalation_time": timedelta(minutes=5),
            },
            "high": {
                "immediate_actions": [
                    "Assess immediate safety",
                    "Connect to crisis-trained peer supporters",
                    "Provide crisis resources",
                    "Schedule follow-up within 24 hours",
                ],
                "escalation_time": timedelta(minutes=15),
            },
            "moderate": {
                "immediate_actions": [
                    "Provide emotional support and validation",
                    "Connect to appropriate peer supporters",
                    "Share relevant resources",
                    "Schedule follow-up within 72 hours",
                ],
                "escalation_time": timedelta(hours=2),
            },
        }

    def _initialize_training_modules(self) -> Dict[str, any]:
        """Initialize peer supporter training curriculum"""
        return {
            "foundations": {
                "title": "🌈 Neurodivergent Peer Support Foundations",
                "modules": [
                    "Understanding neurodivergence and disability justice",
                    "Trauma-informed peer support approaches",
                    "Active listening and validation techniques",
                    "Recognizing and working with crisis situations",
                    "Boundary setting and self-care",
                    "Cultural competency and intersectionality",
                ],
                "duration": timedelta(hours=20),
                "required": True,
            },
            "adhd_specialization": {
                "title": "🎯 ADHD Peer Support Specialization",
                "modules": [
                    "Executive function support strategies",
                    "Hyperfocus and time management",
                    "Emotional regulation and RSD",
                    "ADHD masking and unmasking support",
                    "Workplace and academic accommodations",
                ],
                "duration": timedelta(hours=12),
                "prerequisite": "foundations",
            },
            "autism_specialization": {
                "title": "🌈 Autism Peer Support Specialization",
                "modules": [
                    "Sensory processing support",
                    "Social communication differences",
                    "Stimming and self-regulation",
                    "Meltdown and shutdown support",
                    "Autism advocacy and self-advocacy",
                ],
                "duration": timedelta(hours=12),
                "prerequisite": "foundations",
            },
            "crisis_intervention": {
                "title": "🆘 Crisis Intervention Certification",
                "modules": [
                    "Crisis assessment and risk evaluation",
                    "De-escalation techniques",
                    "Suicide intervention protocols",
                    "Professional referral and collaboration",
                    "Post-crisis follow-up and support",
                ],
                "duration": timedelta(hours=16),
                "prerequisite": "foundations",
                "certification_required": True,
            },
            "trauma_informed": {
                "title": "💙 Trauma-Informed Care Certification",
                "modules": [
                    "Understanding trauma and neurodivergence",
                    "Creating safety in peer support",
                    "Recognizing trauma responses",
                    "Supporting trauma survivors",
                    "Secondary trauma prevention",
                ],
                "duration": timedelta(hours=14),
                "prerequisite": "foundations",
                "certification_required": True,
            },
        }

    async def register_peer_supporter(self, supporter_data: Dict) -> PeerSupporter:
        """Register and train new peer supporter"""
        supporter = PeerSupporter(
            supporter_id=supporter_data["supporter_id"],
            username=supporter_data["username"],
            neurodivergent_types=supporter_data["neurodivergent_types"],
            specializations=supporter_data.get("specializations", []),
            lived_experience=supporter_data.get("lived_experience", []),
            languages=supporter_data.get("languages", ["English"]),
            availability=supporter_data.get("availability", {}),
            max_capacity=supporter_data.get("max_capacity", 5),
        )

        self.supporters[supporter.supporter_id] = supporter

        # Start with foundation training
        training_plan = await self._create_training_plan(supporter)

        return supporter

    async def _create_training_plan(self, supporter: PeerSupporter) -> Dict:
        """Create personalized training plan for peer supporter"""
        required_modules = ["foundations"]
        optional_modules = []

        # Add specialization modules based on neurodivergent types
        if "ADHD" in supporter.neurodivergent_types:
            optional_modules.append("adhd_specialization")

        if "Autism" in supporter.neurodivergent_types:
            optional_modules.append("autism_specialization")

        # Recommend additional certifications
        recommended_modules = ["trauma_informed"]

        if SupportType.CRISIS in supporter.specializations:
            required_modules.append("crisis_intervention")

        return {
            "supporter_id": supporter.supporter_id,
            "required_modules": required_modules,
            "optional_modules": optional_modules,
            "recommended_modules": recommended_modules,
            "total_estimated_hours": sum(
                self.training_modules[module]["duration"].total_seconds() / 3600
                for module in required_modules + optional_modules
            ),
            "can_start_basic_support": False,  # After foundations
            "can_handle_crisis": False,  # After crisis certification
        }

    async def submit_support_request(self, request_data: Dict) -> SupportRequest:
        """Submit new peer support request with automatic matching"""

        # Analyze urgency and crisis indicators
        crisis_analysis = await self._analyze_crisis_level(request_data["description"])

        request = SupportRequest(
            request_id=f"req_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            requester_id=request_data["requester_id"],
            support_types=[SupportType(t) for t in request_data["support_types"]],
            description=request_data["description"],
            urgency_level=CrisisLevel(crisis_analysis["level"]),
            preferred_supporter_traits=request_data.get(
                "preferred_supporter_traits", {}
            ),
            anonymous=request_data.get("anonymous", False),
            trigger_warnings=request_data.get("trigger_warnings", []),
            accommodation_needs=request_data.get("accommodation_needs", []),
        )

        self.support_requests[request.request_id] = request

        # Handle crisis situations immediately
        if request.urgency_level in [CrisisLevel.HIGH, CrisisLevel.CRITICAL]:
            await self._handle_crisis_request(request)
        else:
            # Standard matching process
            await self._match_support_request(request)

        return request

    async def _analyze_crisis_level(self, description: str) -> Dict:
        """Analyze support request for crisis indicators"""
        description_lower = description.lower()

        critical_indicators = [
            "want to die",
            "kill myself",
            "suicide",
            "end my life",
            "not worth living",
            "immediate danger",
            "emergency",
        ]

        high_indicators = [
            "crisis",
            "breaking down",
            "can't cope",
            "desperate",
            "urgent",
            "immediate help",
            "hurt myself",
            "self harm",
        ]

        moderate_indicators = [
            "overwhelmed",
            "struggling",
            "need help soon",
            "very stressed",
            "having breakdown",
            "panic",
        ]

        if any(indicator in description_lower for indicator in critical_indicators):
            return {"level": "critical", "indicators": critical_indicators}
        elif any(indicator in description_lower for indicator in high_indicators):
            return {"level": "high", "indicators": high_indicators}
        elif any(indicator in description_lower for indicator in moderate_indicators):
            return {"level": "moderate", "indicators": moderate_indicators}
        else:
            return {"level": "low", "indicators": []}

    async def _handle_crisis_request(self, request: SupportRequest):
        """Handle crisis-level support requests with immediate intervention"""

        protocol = self.crisis_escalation_protocols[request.urgency_level.value]

        if request.urgency_level == CrisisLevel.CRITICAL:
            # Immediate crisis intervention
            crisis_supporters = [
                supporter
                for supporter in self.supporters.values()
                if supporter.crisis_trained
                and supporter.current_capacity < supporter.max_capacity
            ]

            if crisis_supporters:
                # Match with first available crisis-trained supporter
                matched_supporter = crisis_supporters[0]
                request.matched_supporter_id = matched_supporter.supporter_id
                request.status = SupportStatus.MATCHED

                # Immediate notification
                await self._send_crisis_notification(request, matched_supporter)
            else:
                # No available crisis supporters - escalate to professional services
                await self._escalate_to_professional_services(request)

        elif request.urgency_level == CrisisLevel.HIGH:
            # Urgent but not immediate crisis
            crisis_supporters = [
                supporter
                for supporter in self.supporters.values()
                if (
                    supporter.crisis_trained
                    or SupportType.CRISIS in supporter.specializations
                )
                and supporter.current_capacity < supporter.max_capacity
            ]

            if crisis_supporters:
                # Quick matching with crisis-capable supporter
                best_match = await self.matching_algorithm.find_crisis_match(
                    request, crisis_supporters
                )
                request.matched_supporter_id = best_match.supporter_id
                request.status = SupportStatus.MATCHED

                await self._send_urgent_notification(request, best_match)

    async def _send_crisis_notification(
        self, request: SupportRequest, supporter: PeerSupporter
    ):
        """Send immediate crisis notification to matched supporter"""
        notification = {
            "type": "CRISIS_ALERT",
            "priority": "IMMEDIATE",
            "request_id": request.request_id,
            "supporter_id": supporter.supporter_id,
            "crisis_level": request.urgency_level.value,
            "message": f"""
            🆘 CRISIS SUPPORT NEEDED IMMEDIATELY

            A community member needs immediate crisis support.

            Support Types: {[t.value for t in request.support_types]}
            Crisis Level: {request.urgency_level.value}

            Please respond within 5 minutes or escalate to professional services.

            Crisis Resources Available:
            - Suicide Hotline: 988
            - Crisis Text: 741741
            - Emergency: 911

            You are trained and capable. The community trusts you. 💙
            """,
            "timestamp": datetime.now(),
            "response_deadline": datetime.now() + timedelta(minutes=5),
        }

        # In real implementation, send actual notification
        print(f"CRISIS ALERT sent to {supporter.username}: {notification}")

    async def _match_support_request(self, request: SupportRequest):
        """Match support request with appropriate peer supporter"""

        available_supporters = [
            supporter
            for supporter in self.supporters.values()
            if supporter.current_capacity < supporter.max_capacity
        ]

        if not available_supporters:
            # Add to waiting queue
            request.status = SupportStatus.REQUESTED
            return

        # Use matching algorithm to find best fit
        best_match = await self.matching_algorithm.find_best_match(
            request, available_supporters
        )

        if best_match:
            request.matched_supporter_id = best_match.supporter_id
            request.status = SupportStatus.MATCHED
            best_match.current_capacity += 1

            # Send notification to matched supporter
            await self._send_match_notification(request, best_match)

    async def _send_match_notification(
        self, request: SupportRequest, supporter: PeerSupporter
    ):
        """Send notification to matched peer supporter"""
        notification = {
            "type": "SUPPORT_MATCH",
            "request_id": request.request_id,
            "supporter_id": supporter.supporter_id,
            "support_types": [t.value for t in request.support_types],
            "urgency": request.urgency_level.value,
            "estimated_duration": request.estimated_duration,
            "accommodation_needs": request.accommodation_needs,
            "message": f"""
            🤝 New Peer Support Match

            You've been matched with a community member who needs support.

            Support Requested: {[t.value for t in request.support_types]}
            Urgency Level: {request.urgency_level.value}

            Please respond within 2 hours to accept this match.

            Remember: You're making a difference. Take care of yourself too. 💙
            """,
            "timestamp": datetime.now(),
        }

        print(f"Support match notification sent to {supporter.username}")

    async def start_support_session(
        self, request_id: str, supporter_id: str
    ) -> SupportSession:
        """Start a peer support session"""

        if request_id not in self.support_requests:
            raise ValueError("Support request not found")

        request = self.support_requests[request_id]

        if request.matched_supporter_id != supporter_id:
            raise ValueError("Supporter not matched to this request")

        session = SupportSession(
            session_id=f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            request_id=request_id,
            supporter_id=supporter_id,
            requester_id=request.requester_id,
            start_time=datetime.now(),
            support_provided=request.support_types,
        )

        self.active_sessions[session.session_id] = session
        request.status = SupportStatus.IN_PROGRESS

        return session

    async def complete_support_session(
        self, session_id: str, completion_data: Dict
    ) -> Dict:
        """Complete and document peer support session"""

        if session_id not in self.active_sessions:
            raise ValueError("Active session not found")

        session = self.active_sessions[session_id]
        session.end_time = datetime.now()
        session.techniques_used = completion_data.get("techniques_used", [])
        session.outcomes = completion_data.get("outcomes", [])
        session.referrals_made = completion_data.get("referrals_made", [])
        session.follow_up_scheduled = completion_data.get("follow_up_scheduled", False)
        session.session_notes = completion_data.get("session_notes", "")

        # Move to completed sessions
        self.completed_sessions[session_id] = session
        del self.active_sessions[session_id]

        # Update supporter capacity and stats
        supporter = self.supporters[session.supporter_id]
        supporter.current_capacity -= 1
        supporter.total_support_hours += (
            session.end_time - session.start_time
        ).total_seconds() / 3600

        # Update request status
        request = self.support_requests[session.request_id]
        request.status = SupportStatus.COMPLETED

        # Generate completion report
        completion_report = {
            "session_id": session_id,
            "duration": session.end_time - session.start_time,
            "support_provided": [t.value for t in session.support_provided],
            "outcomes_achieved": session.outcomes,
            "referrals_made": session.referrals_made,
            "follow_up_scheduled": session.follow_up_scheduled,
            "supporter_feedback": completion_data.get("supporter_feedback", ""),
            "completion_timestamp": session.end_time,
        }

        return completion_report


class SupportMatchingEngine:
    """🎯 Intelligent matching algorithm for peer support requests"""

    async def find_best_match(
        self, request: SupportRequest, available_supporters: List[PeerSupporter]
    ) -> Optional[PeerSupporter]:
        """Find best peer supporter match using multiple criteria"""

        scored_supporters = []

        for supporter in available_supporters:
            score = await self._calculate_match_score(request, supporter)
            scored_supporters.append((supporter, score))

        # Sort by score (highest first)
        scored_supporters.sort(key=lambda x: x[1], reverse=True)

        return scored_supporters[0][0] if scored_supporters else None

    async def find_crisis_match(
        self, request: SupportRequest, crisis_supporters: List[PeerSupporter]
    ) -> Optional[PeerSupporter]:
        """Find best crisis-trained supporter for urgent requests"""

        # For crisis situations, prioritize availability and crisis training
        best_match = None
        highest_score = 0

        for supporter in crisis_supporters:
            score = 0

            # Crisis training bonus
            if supporter.crisis_trained:
                score += 50

            # Capacity availability
            capacity_ratio = supporter.current_capacity / supporter.max_capacity
            score += (1 - capacity_ratio) * 30

            # Experience with crisis situations
            score += min(supporter.total_support_hours / 10, 20)

            # Neurodivergent type match
            if any(nt in supporter.neurodivergent_types for nt in ["ADHD", "Autism"]):
                score += 10

            if score > highest_score:
                highest_score = score
                best_match = supporter

        return best_match

    async def _calculate_match_score(
        self, request: SupportRequest, supporter: PeerSupporter
    ) -> float:
        """Calculate compatibility score between request and supporter"""
        score = 0.0

        # Support type specialization match
        for support_type in request.support_types:
            if support_type in supporter.specializations:
                score += 25

        # Neurodivergent type compatibility
        if hasattr(request, "requester_neurodivergent_types"):
            common_types = set(request.requester_neurodivergent_types) & set(
                supporter.neurodivergent_types
            )
            score += len(common_types) * 15

        # Lived experience match
        if hasattr(request, "specific_challenges"):
            common_experiences = set(request.specific_challenges) & set(
                supporter.lived_experience
            )
            score += len(common_experiences) * 10

        # Capacity availability
        capacity_ratio = supporter.current_capacity / supporter.max_capacity
        score += (1 - capacity_ratio) * 20

        # Training and certification
        if supporter.trauma_informed:
            score += 15

        if supporter.crisis_trained and SupportType.CRISIS in request.support_types:
            score += 30

        # Experience level
        score += min(supporter.total_support_hours / 5, 10)

        # Positive feedback history
        if supporter.positive_feedback_count > 0:
            score += min(supporter.positive_feedback_count, 10)

        # Language compatibility
        if hasattr(request, "preferred_language"):
            if request.preferred_language in supporter.languages:
                score += 5

        # Availability alignment (if specified)
        if hasattr(request, "preferred_time") and supporter.availability:
            # Check if supporter is available at preferred time
            # Implementation would check actual availability schedules
            score += 5

        return score


# Example usage
async def test_peer_support_system():
    """Test the peer support system"""
    system = NeurodivergentPeerSupportSystem()

    # Register a peer supporter
    supporter_data = {
        "supporter_id": "supporter123",
        "username": "NeurodivergentAlly",
        "neurodivergent_types": ["ADHD", "Autism"],
        "specializations": [SupportType.EMOTIONAL, SupportType.EXECUTIVE_FUNCTION],
        "lived_experience": ["workplace accommodations", "masking burnout"],
        "max_capacity": 3,
    }

    supporter = await system.register_peer_supporter(supporter_data)
    print("Registered supporter:", supporter.username)

    # Submit a support request
    request_data = {
        "requester_id": "user456",
        "support_types": ["emotional", "executive_function"],
        "description": "I'm struggling with executive function and feeling overwhelmed",
        "accommodation_needs": ["text-based communication", "flexible timing"],
    }

    request = await system.submit_support_request(request_data)
    print("Support request submitted:", request.request_id)


if __name__ == "__main__":
    asyncio.run(test_peer_support_system())

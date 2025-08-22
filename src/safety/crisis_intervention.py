"""
🛡️⚡💙 ADVANCED SAFETY & CRISIS INTERVENTION SYSTEM 💙⚡🛡️
Comprehensive crisis detection, intervention, and safety monitoring for neurodivergent community
"""

import asyncio
import uuid
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
from typing import Callable, Dict, List, Optional


class CrisisType(Enum):
    SUICIDE_IDEATION = "suicide_ideation"
    SELF_HARM = "self_harm"
    SEVERE_DISTRESS = "severe_distress"
    PANIC_ATTACK = "panic_attack"
    MELTDOWN = "meltdown"
    SHUTDOWN = "shutdown"
    BURNOUT = "burnout"
    TRAUMA_RESPONSE = "trauma_response"
    MEDICAL_EMERGENCY = "medical_emergency"


class InterventionLevel(Enum):
    MONITORING = "monitoring"
    PEER_SUPPORT = "peer_support"
    CRISIS_TEAM = "crisis_team"
    PROFESSIONAL_REFERRAL = "professional_referral"
    EMERGENCY_SERVICES = "emergency_services"


class SafetyAlertType(Enum):
    CONTENT_WARNING = "content_warning"
    ABLEISM_DETECTED = "ableism_detected"
    HARASSMENT = "harassment"
    UNSAFE_ADVICE = "unsafe_advice"
    CRISIS_INDICATOR = "crisis_indicator"
    COMMUNITY_VIOLATION = "community_violation"


@dataclass
class CrisisDetectionResult:
    crisis_detected: bool
    crisis_types: List[CrisisType] = field(default_factory=list)
    confidence_score: float = 0.0
    risk_factors: List[str] = field(default_factory=list)
    protective_factors: List[str] = field(default_factory=list)
    immediate_actions: List[str] = field(default_factory=list)
    recommended_intervention: InterventionLevel = InterventionLevel.MONITORING
    resources_needed: List[str] = field(default_factory=list)
    follow_up_timeframe: Optional[timedelta] = None


@dataclass
class SafetyIncident:
    incident_id: str
    reporter_id: str
    reported_user_id: Optional[str] = None
    incident_type: SafetyAlertType = SafetyAlertType.COMMUNITY_VIOLATION
    description: str = ""
    content_reference: Optional[str] = None  # Post/comment ID
    severity: str = "low"  # low, medium, high, critical
    timestamp: datetime = field(default_factory=datetime.now)
    investigation_status: str = "pending"  # pending, investigating, resolved, escalated
    actions_taken: List[str] = field(default_factory=list)
    resolution_notes: str = ""


@dataclass
class CrisisIntervention:
    intervention_id: str
    user_id: str
    crisis_types: List[CrisisType]
    intervention_level: InterventionLevel
    start_time: datetime = field(default_factory=datetime.now)
    end_time: Optional[datetime] = None
    interventions_used: List[str] = field(default_factory=list)
    resources_provided: List[str] = field(default_factory=list)
    professional_contacts: List[str] = field(default_factory=list)
    outcome: Optional[str] = None
    follow_up_scheduled: bool = False
    assigned_counselor: Optional[str] = None


class NeurodivergentCrisisDetectionAI:
    """🧠 Advanced AI system for detecting neurodivergent-specific crisis indicators"""

    def __init__(self):
        self.crisis_patterns = self._initialize_crisis_patterns()
        self.neurodivergent_context_clues = self._initialize_context_clues()
        self.protective_factor_indicators = self._initialize_protective_factors()
        self.false_positive_reducers = self._initialize_false_positive_reducers()

    def _initialize_crisis_patterns(self) -> Dict[CrisisType, Dict]:
        """Initialize crisis detection patterns specific to neurodivergent experiences"""
        return {
            CrisisType.SUICIDE_IDEATION: {
                "keywords": [
                    "want to die",
                    "kill myself",
                    "suicide",
                    "end my life",
                    "not worth living",
                    "better off dead",
                    "burden on everyone",
                    "permanent solution",
                    "can't go on",
                    "no point in living",
                ],
                "phrases": [
                    "thinking about ending it",
                    "making plans to die",
                    "nobody would miss me",
                    "world would be better without me",
                    "can't take it anymore",
                ],
                "confidence_boost": 0.9,
                "intervention_level": InterventionLevel.EMERGENCY_SERVICES,
            },
            CrisisType.SELF_HARM: {
                "keywords": [
                    "hurt myself",
                    "self harm",
                    "cutting",
                    "burning myself",
                    "deserve pain",
                    "punish myself",
                    "make it stop",
                ],
                "phrases": [
                    "want to hurt myself",
                    "thinking about cutting",
                    "need to feel pain",
                    "deserve to suffer",
                ],
                "confidence_boost": 0.8,
                "intervention_level": InterventionLevel.CRISIS_TEAM,
            },
            CrisisType.SEVERE_DISTRESS: {
                "keywords": [
                    "can't cope",
                    "breaking down",
                    "falling apart",
                    "drowning",
                    "suffocating",
                    "trapped",
                    "hopeless",
                ],
                "phrases": [
                    "everything is overwhelming",
                    "can't handle this anymore",
                    "losing my mind",
                    "nothing makes sense",
                ],
                "confidence_boost": 0.7,
                "intervention_level": InterventionLevel.PEER_SUPPORT,
            },
            CrisisType.MELTDOWN: {
                "keywords": [
                    "meltdown",
                    "overstimulated",
                    "sensory overload",
                    "can't think",
                    "too much",
                    "shutting down",
                ],
                "phrases": [
                    "everything is too loud",
                    "can't process anything",
                    "need to escape",
                    "sensory hell",
                ],
                "neurodivergent_specific": True,
                "confidence_boost": 0.8,
                "intervention_level": InterventionLevel.PEER_SUPPORT,
            },
            CrisisType.SHUTDOWN: {
                "keywords": [
                    "shutdown",
                    "can't speak",
                    "nonverbal",
                    "frozen",
                    "disconnected",
                    "numb",
                    "empty",
                ],
                "phrases": [
                    "can't form words",
                    "lost my voice",
                    "brain won't work",
                    "completely shut down",
                ],
                "neurodivergent_specific": True,
                "confidence_boost": 0.7,
                "intervention_level": InterventionLevel.PEER_SUPPORT,
            },
            CrisisType.BURNOUT: {
                "keywords": [
                    "burnout",
                    "masking exhaustion",
                    "can't mask anymore",
                    "drained",
                    "depleted",
                    "running on empty",
                ],
                "phrases": [
                    "masking is killing me",
                    "exhausted from pretending",
                    "can't keep up the act",
                    "burned out from masking",
                ],
                "neurodivergent_specific": True,
                "confidence_boost": 0.6,
                "intervention_level": InterventionLevel.PEER_SUPPORT,
            },
        }

    def _initialize_context_clues(self) -> Dict[str, float]:
        """Initialize neurodivergent-specific context clues that modify crisis detection"""
        return {
            # Autism-specific contexts
            "sensory": 0.3,
            "stimming": 0.2,
            "special interest": -0.1,  # Usually protective
            "routine disrupted": 0.4,
            "social exhaustion": 0.3,
            "communication difficulties": 0.2,
            # ADHD-specific contexts
            "hyperfocus crash": 0.4,
            "rejection sensitive": 0.5,
            "executive dysfunction": 0.3,
            "dopamine seeking": 0.2,
            "time blindness": 0.1,
            # General neurodivergent contexts
            "masking": 0.4,
            "unmasking": 0.2,
            "ableism": 0.6,
            "accommodations denied": 0.5,
            "misunderstood": 0.3,
            "late diagnosis": 0.3,
        }

    def _initialize_protective_factors(self) -> List[str]:
        """Initialize protective factors that reduce crisis risk"""
        return [
            "support system",
            "therapy",
            "medication working",
            "special interests",
            "stimming helps",
            "accommodations",
            "understanding friends",
            "neurodivergent community",
            "self-advocacy",
            "coping strategies",
            "sensory tools",
            "routine",
            "pets",
            "creative outlets",
            "exercise",
            "mindfulness",
            "journaling",
            "safe space",
        ]

    def _initialize_false_positive_reducers(self) -> List[str]:
        """Initialize patterns that reduce false positives"""
        return [
            "in the past",
            "used to feel",
            "no longer",
            "getting better",
            "improving",
            "fictional character",
            "movie",
            "book",
            "hypothetically",
            "what if",
            "asking for a friend",
            "general question",
        ]

    async def analyze_crisis_indicators(
        self, content: str, user_context: Dict = None
    ) -> CrisisDetectionResult:
        """Analyze content for crisis indicators with neurodivergent-aware context"""

        content_lower = content.lower()
        detected_crises = []
        total_confidence = 0.0
        risk_factors = []
        protective_factors = []

        # Check for false positive reducers first
        false_positive_score = (
            sum(
                1
                for reducer in self.false_positive_reducers
                if reducer in content_lower
            )
            * 0.2
        )

        # Analyze each crisis type
        for crisis_type, patterns in self.crisis_patterns.items():
            confidence = 0.0

            # Check keywords
            keyword_matches = sum(
                1 for keyword in patterns["keywords"] if keyword in content_lower
            )
            if keyword_matches > 0:
                confidence += keyword_matches * 0.3

            # Check phrases
            phrase_matches = sum(
                1 for phrase in patterns["phrases"] if phrase in content_lower
            )
            if phrase_matches > 0:
                confidence += phrase_matches * 0.4

            # Apply neurodivergent context modifiers
            for context, modifier in self.neurodivergent_context_clues.items():
                if context in content_lower:
                    confidence += modifier
                    if modifier > 0:
                        risk_factors.append(context)

            # Check for protective factors
            for factor in self.protective_factor_indicators:
                if factor in content_lower:
                    protective_factors.append(factor)
                    confidence -= 0.1  # Protective factors reduce crisis risk

            # Apply false positive reduction
            confidence -= false_positive_score

            # Apply pattern-specific confidence boost
            if confidence > 0.3:  # Threshold for detection
                confidence *= patterns.get("confidence_boost", 1.0)
                detected_crises.append(crisis_type)
                total_confidence = max(total_confidence, confidence)

        # Determine intervention level
        intervention_level = InterventionLevel.MONITORING
        if detected_crises:
            highest_priority_crisis = max(
                detected_crises,
                key=lambda c: self.crisis_patterns[c].get("confidence_boost", 0),
            )
            intervention_level = self.crisis_patterns[highest_priority_crisis][
                "intervention_level"
            ]

        # Generate immediate actions
        immediate_actions = await self._generate_immediate_actions(
            detected_crises, total_confidence
        )

        # Determine follow-up timeframe
        follow_up_timeframe = self._determine_follow_up_timeframe(
            intervention_level, total_confidence
        )

        return CrisisDetectionResult(
            crisis_detected=len(detected_crises) > 0,
            crisis_types=detected_crises,
            confidence_score=min(total_confidence, 1.0),
            risk_factors=risk_factors,
            protective_factors=protective_factors,
            immediate_actions=immediate_actions,
            recommended_intervention=intervention_level,
            follow_up_timeframe=follow_up_timeframe,
        )

    async def _generate_immediate_actions(
        self, crisis_types: List[CrisisType], confidence: float
    ) -> List[str]:
        """Generate context-appropriate immediate actions"""
        actions = []

        if CrisisType.SUICIDE_IDEATION in crisis_types:
            actions.extend(
                [
                    "🆘 Connect to suicide prevention resources immediately",
                    "📞 Share crisis hotline: 988 (Suicide & Crisis Lifeline)",
                    "💙 Ensure person is not alone - activate crisis network",
                    "🚨 Consider emergency services if immediate danger",
                ]
            )

        if CrisisType.SELF_HARM in crisis_types:
            actions.extend(
                [
                    "🛡️ Connect to self-harm support resources",
                    "💙 Activate peer supporters with self-harm experience",
                    "📞 Share crisis text line: 741741",
                    "🤝 Provide immediate emotional support",
                ]
            )

        if CrisisType.MELTDOWN in crisis_types:
            actions.extend(
                [
                    "🌊 Provide sensory regulation support",
                    "🔇 Suggest reducing sensory input immediately",
                    "💙 Connect to autism-informed peer supporters",
                    "🧘 Share grounding and calming techniques",
                ]
            )

        if CrisisType.SHUTDOWN in crisis_types:
            actions.extend(
                [
                    "🤐 Respect communication difficulties - don't pressure to speak",
                    "💙 Provide non-verbal support options",
                    "⏰ Allow processing time without urgency",
                    "🤝 Connect to shutdown-experienced peer supporters",
                ]
            )

        if CrisisType.BURNOUT in crisis_types:
            actions.extend(
                [
                    "😴 Encourage immediate rest and self-care",
                    "🎭 Validate masking exhaustion experience",
                    "🤝 Connect to neurodivergent peer supporters",
                    "📋 Help identify immediate stressor reduction",
                ]
            )

        # Add confidence-based actions
        if confidence > 0.8:
            actions.append("⚡ Immediate intervention required - don't wait")
        elif confidence > 0.6:
            actions.append("📞 Contact within next hour")
        else:
            actions.append("📅 Schedule follow-up within 24 hours")

        return actions

    def _determine_follow_up_timeframe(
        self, intervention_level: InterventionLevel, confidence: float
    ) -> Optional[timedelta]:
        """Determine appropriate follow-up timeframe based on crisis severity"""

        if intervention_level == InterventionLevel.EMERGENCY_SERVICES:
            return timedelta(hours=1)  # Immediate follow-up
        elif intervention_level == InterventionLevel.CRISIS_TEAM:
            return timedelta(hours=4)
        elif intervention_level == InterventionLevel.PEER_SUPPORT:
            if confidence > 0.7:
                return timedelta(hours=12)
            else:
                return timedelta(days=1)
        else:
            return timedelta(days=3)


class NeurodivergentSafetySystem:
    """🛡️ Comprehensive safety monitoring and intervention system"""

    def __init__(self):
        self.crisis_detector = NeurodivergentCrisisDetectionAI()
        self.active_interventions: Dict[str, CrisisIntervention] = {}
        self.safety_incidents: Dict[str, SafetyIncident] = {}
        self.crisis_resources = self._initialize_crisis_resources()
        self.safety_protocols = self._initialize_safety_protocols()
        self.intervention_handlers: Dict[InterventionLevel, Callable] = {
            InterventionLevel.MONITORING: self._handle_monitoring,
            InterventionLevel.PEER_SUPPORT: self._handle_peer_support,
            InterventionLevel.CRISIS_TEAM: self._handle_crisis_team,
            InterventionLevel.PROFESSIONAL_REFERRAL: self._handle_professional_referral,
            InterventionLevel.EMERGENCY_SERVICES: self._handle_emergency_services,
        }

    def _initialize_crisis_resources(self) -> Dict[str, any]:
        """Initialize comprehensive crisis resources"""
        return {
            "immediate_crisis": {
                "suicide_hotline": {
                    "number": "988",
                    "name": "Suicide & Crisis Lifeline",
                    "description": "24/7 free and confidential support",
                    "website": "https://988lifeline.org",
                },
                "crisis_text": {
                    "number": "741741",
                    "name": "Crisis Text Line",
                    "description": "Text HOME to 741741 for crisis support",
                },
                "emergency": {
                    "number": "911",
                    "description": "For immediate physical danger",
                },
            },
            "specialized_support": {
                "lgbtq": {
                    "number": "1-866-488-7386",
                    "name": "The Trevor Project",
                    "description": "Crisis support for LGBTQ+ youth",
                },
                "trans_lifeline": {
                    "number": "877-565-8860",
                    "name": "Trans Lifeline",
                    "description": "Trans peer support hotline",
                },
                "domestic_violence": {
                    "number": "1-800-799-7233",
                    "name": "National Domestic Violence Hotline",
                },
            },
            "neurodivergent_specific": {
                "autism_support": {
                    "organization": "Autistic Self Advocacy Network",
                    "website": "https://autisticadvocacy.org",
                    "description": "Autism advocacy and support resources",
                },
                "adhd_support": {
                    "organization": "CHADD",
                    "website": "https://chadd.org",
                    "description": "ADHD support and resources",
                },
                "sensory_crisis": {
                    "techniques": [
                        "Noise-canceling headphones",
                        "Weighted blankets",
                        "Fidget tools",
                        "Dim lighting",
                        "Safe sensory space",
                    ]
                },
            },
            "coping_resources": {
                "grounding_techniques": [
                    "5-4-3-2-1 sensory grounding",
                    "Deep breathing exercises",
                    "Progressive muscle relaxation",
                    "Cold water on face/hands",
                    "Favorite calming music",
                ],
                "crisis_apps": [
                    "Calm app for anxiety",
                    "Headspace for mindfulness",
                    "PTSD Coach for trauma",
                    "MindShift for anxiety",
                ],
            },
        }

    def _initialize_safety_protocols(self) -> Dict[str, any]:
        """Initialize safety intervention protocols"""
        return {
            "assessment": {
                "immediate_danger": [
                    "Is the person in immediate physical danger?",
                    "Do they have means/plan for self-harm?",
                    "Are they able to keep themselves safe?",
                    "Do they have support people available?",
                ],
                "risk_factors": [
                    "Previous suicide attempts",
                    "Recent major losses or trauma",
                    "Substance use",
                    "Social isolation",
                    "Access to lethal means",
                ],
            },
            "intervention_steps": {
                "crisis": [
                    "Ensure immediate safety",
                    "Connect to professional crisis services",
                    "Stay with person until help arrives",
                    "Remove means of self-harm if possible",
                    "Document all actions taken",
                ],
                "support": [
                    "Active listening and validation",
                    "Connect to peer supporters",
                    "Provide crisis resources",
                    "Schedule follow-up contact",
                    "Monitor ongoing safety",
                ],
            },
        }

    async def analyze_safety_concern(
        self, content: str, user_id: str, context: Dict = None
    ) -> Dict:
        """Analyze content for safety concerns and activate appropriate interventions"""

        # Run crisis detection
        crisis_result = await self.crisis_detector.analyze_crisis_indicators(
            content, context
        )

        response = {
            "safety_assessment": crisis_result,
            "intervention_activated": False,
            "resources_provided": [],
            "follow_up_scheduled": False,
            "intervention_id": None,
        }

        # Activate intervention if crisis detected
        if crisis_result.crisis_detected:
            intervention = await self._activate_crisis_intervention(
                user_id=user_id, crisis_result=crisis_result, content=content
            )

            response.update(
                {
                    "intervention_activated": True,
                    "intervention_id": intervention.intervention_id,
                    "intervention_level": intervention.intervention_level.value,
                    "resources_provided": intervention.resources_provided,
                    "follow_up_scheduled": intervention.follow_up_scheduled,
                }
            )

        return response

    async def _activate_crisis_intervention(
        self, user_id: str, crisis_result: CrisisDetectionResult, content: str
    ) -> CrisisIntervention:
        """Activate appropriate crisis intervention based on assessment"""

        intervention = CrisisIntervention(
            intervention_id=str(uuid.uuid4()),
            user_id=user_id,
            crisis_types=crisis_result.crisis_types,
            intervention_level=crisis_result.recommended_intervention,
        )

        # Execute intervention based on level
        handler = self.intervention_handlers[crisis_result.recommended_intervention]
        await handler(intervention, crisis_result)

        self.active_interventions[intervention.intervention_id] = intervention

        return intervention

    async def _handle_monitoring(
        self, intervention: CrisisIntervention, crisis_result: CrisisDetectionResult
    ):
        """Handle low-level monitoring intervention"""
        intervention.interventions_used.append("safety_monitoring")
        intervention.resources_provided.extend(
            ["Crisis resources shared", "Self-care reminders provided"]
        )
        intervention.follow_up_scheduled = True

    async def _handle_peer_support(
        self, intervention: CrisisIntervention, crisis_result: CrisisDetectionResult
    ):
        """Handle peer support intervention"""
        intervention.interventions_used.extend(
            [
                "peer_support_activation",
                "crisis_resource_sharing",
                "emotional_validation",
            ]
        )

        # Activate neurodivergent peer supporters
        if CrisisType.MELTDOWN in crisis_result.crisis_types:
            intervention.resources_provided.append(
                "Autism-informed peer supporters activated"
            )

        if CrisisType.BURNOUT in crisis_result.crisis_types:
            intervention.resources_provided.append(
                "Masking burnout support network activated"
            )

        intervention.resources_provided.extend(
            [
                "Crisis hotline: 988",
                "Crisis text: 741741",
                "Neurodivergent community support activated",
            ]
        )
        intervention.follow_up_scheduled = True

    async def _handle_crisis_team(
        self, intervention: CrisisIntervention, crisis_result: CrisisDetectionResult
    ):
        """Handle crisis team intervention"""
        intervention.interventions_used.extend(
            [
                "crisis_team_activation",
                "immediate_support_deployment",
                "safety_planning",
            ]
        )

        intervention.resources_provided.extend(
            [
                "Crisis-trained counselors notified",
                "24/7 crisis support activated",
                "Safety planning session scheduled",
            ]
        )

        # Schedule immediate follow-up
        intervention.follow_up_scheduled = True

    async def _handle_professional_referral(
        self, intervention: CrisisIntervention, crisis_result: CrisisDetectionResult
    ):
        """Handle professional referral intervention"""
        intervention.interventions_used.extend(
            ["professional_referral", "crisis_service_connection", "ongoing_monitoring"]
        )

        intervention.resources_provided.extend(
            [
                "Mental health professional referral",
                "Crisis service connection",
                "Therapy resource matching",
            ]
        )

        intervention.professional_contacts.extend(
            [
                "Local crisis center",
                "Mental health clinic",
                "Neurodivergent-affirming therapists",
            ]
        )

    async def _handle_emergency_services(
        self, intervention: CrisisIntervention, crisis_result: CrisisDetectionResult
    ):
        """Handle emergency services intervention"""
        intervention.interventions_used.extend(
            [
                "emergency_services_alert",
                "immediate_safety_measures",
                "crisis_hotline_connection",
            ]
        )

        intervention.resources_provided.extend(
            [
                "Emergency services contacted",
                "Suicide prevention hotline: 988",
                "Immediate crisis intervention activated",
            ]
        )

        # Mark as critical priority
        intervention.follow_up_scheduled = True

    async def report_safety_incident(self, incident_data: Dict) -> SafetyIncident:
        """Report a community safety incident"""

        incident = SafetyIncident(
            incident_id=str(uuid.uuid4()),
            reporter_id=incident_data["reporter_id"],
            reported_user_id=incident_data.get("reported_user_id"),
            incident_type=SafetyAlertType(incident_data["incident_type"]),
            description=incident_data["description"],
            content_reference=incident_data.get("content_reference"),
            severity=incident_data.get("severity", "medium"),
        )

        self.safety_incidents[incident.incident_id] = incident

        # Auto-escalate high severity incidents
        if incident.severity in ["high", "critical"]:
            await self._escalate_safety_incident(incident)

        return incident

    async def _escalate_safety_incident(self, incident: SafetyIncident):
        """Escalate high-priority safety incidents"""
        incident.investigation_status = "escalated"
        incident.actions_taken.append(
            f"Auto-escalated due to {incident.severity} severity"
        )

        # Immediate actions based on incident type
        if incident.incident_type == SafetyAlertType.HARASSMENT:
            incident.actions_taken.append("Temporary content restrictions applied")

        elif incident.incident_type == SafetyAlertType.UNSAFE_ADVICE:
            incident.actions_taken.append("Content flagged for medical review")

        # Notify safety team
        print(
            f"SAFETY ALERT: {incident.incident_type.value} incident escalated - ID: {incident.incident_id}"
        )


# Example usage
async def test_safety_system():
    """Test the safety system"""
    safety_system = NeurodivergentSafetySystem()

    # Test crisis detection
    crisis_content = "I'm having a severe meltdown and can't cope anymore. Everything is too overwhelming and I want to hurt myself."

    safety_response = await safety_system.analyze_safety_concern(
        content=crisis_content,
        user_id="user123",
        context={"neurodivergent_types": ["Autism", "ADHD"]},
    )

    print("Safety analysis:", safety_response)

    # Test safety incident reporting
    incident_data = {
        "reporter_id": "user456",
        "reported_user_id": "user789",
        "incident_type": "ableism_detected",
        "description": "User posted ableist content about autism",
        "severity": "high",
    }

    incident = await safety_system.report_safety_incident(incident_data)
    print("Safety incident reported:", incident.incident_id)


if __name__ == "__main__":
    asyncio.run(test_safety_system())

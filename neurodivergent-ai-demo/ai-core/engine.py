"""
🧠💎⚡ Neurodivergent AI Core Engine
Revolutionary AI system built BY and FOR the neurodivergent community

This is the heart of our neurodivergent-first AI system, implementing:
- Quantum Empathy Engine: Multi-dimensional understanding of neurodivergent experiences
- Truth Graph: Community-validated knowledge representation
- Strengths-Based Reasoning: Focus on capabilities rather than deficits
- Adaptive Communication: Multiple interaction modes and sensory preferences
- Ethical Constraints: Built-in bias prevention and consent management

Philosophy: "Nothing about us without us"
"""

import asyncio
import logging
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 🧠 Core AI Components


class NeurodivergentType(Enum):
    """Neurodivergent types our AI specializes in understanding"""

    ADHD = "adhd"
    AUTISM = "autism"
    DYSLEXIA = "dyslexia"
    OVERLAP = "overlap"
    GENERAL = "general"


class CommunicationMode(Enum):
    """Different communication preferences"""

    DIRECT = "direct"  # Clear, concise, no ambiguity
    DETAILED = "detailed"  # Comprehensive with examples
    VISUAL = "visual"  # Image-heavy, diagrams
    STRUCTURED = "structured"  # Lists, bullet points, organized
    EMPATHETIC = "empathetic"  # Emotional support focus
    SCIENTIFIC = "scientific"  # Research-backed, evidence-based


class SensoryPreference(Enum):
    """Sensory processing preferences"""

    LOW_STIMULATION = "low"  # Minimal sensory input
    HIGH_STIMULATION = "high"  # Rich sensory input
    BALANCED = "balanced"  # Moderate sensory input
    CUSTOM = "custom"  # User-defined preferences


@dataclass
class UserProfile:
    """Comprehensive user profile for personalized AI interaction"""

    user_id: str
    neurodivergent_types: List[NeurodivergentType]
    communication_mode: CommunicationMode
    sensory_preference: SensoryPreference
    strengths: List[str]
    support_needs: List[str]
    trigger_warnings: List[str]
    preferred_examples: List[str]
    energy_patterns: Dict[str, float]  # Time-based energy levels
    consent_timestamp: datetime
    trust_level: float


@dataclass
class KnowledgeNode:
    """Node in our Truth Graph knowledge representation"""

    id: str
    concept: str
    content: str
    sources: List[Dict[str, Any]]
    trust_score: float
    community_validation: Dict[str, int]  # votes by neurodivergent type
    strengths_focus: bool
    last_updated: datetime
    relationships: List[str]  # Connected node IDs


@dataclass
class EmpathyVector:
    """Multi-dimensional empathy representation"""

    emotional_resonance: float
    shared_experience: float
    understanding_depth: float
    validation_strength: float
    support_quality: float
    respect_level: float


@dataclass
class AIResponse:
    """Comprehensive AI response with full transparency"""

    content: str
    reasoning_path: List[str]
    confidence_score: float
    trust_score: float
    sources: List[Dict[str, Any]]
    empathy_vector: EmpathyVector
    bias_check: Dict[str, float]
    neurodivergent_lens: NeurodivergentType
    communication_adaptation: Dict[str, Any]
    suggestions: List[str]
    support_resources: List[str]


class QuantumEmpathyEngine:
    """
    🌟 Quantum Empathy Engine

    Multi-dimensional understanding system that processes:
    - Emotional context and lived experiences
    - Multiple simultaneous perspectives
    - Non-linear thinking patterns
    - Sensory processing differences
    - Executive function variations
    """

    def __init__(self):
        self.empathy_dimensions = [
            "emotional_resonance",
            "shared_experience",
            "understanding_depth",
            "validation_strength",
            "support_quality",
            "respect_level",
        ]

    def calculate_empathy_vector(
        self, user_profile: UserProfile, query: str, context: Dict[str, Any]
    ) -> EmpathyVector:
        """Calculate multi-dimensional empathy response"""

        # Analyze emotional context
        emotional_resonance = self._analyze_emotional_context(query, user_profile)

        # Check for shared experiences
        shared_experience = self._assess_shared_experience(query, user_profile)

        # Evaluate understanding depth needed
        understanding_depth = self._determine_understanding_depth(query, context)

        # Calculate validation strength
        validation_strength = self._calculate_validation_strength(user_profile, query)

        # Assess support quality potential
        support_quality = self._assess_support_quality(user_profile, context)

        # Measure respect level
        respect_level = self._measure_respect_level(user_profile)

        return EmpathyVector(
            emotional_resonance=emotional_resonance,
            shared_experience=shared_experience,
            understanding_depth=understanding_depth,
            validation_strength=validation_strength,
            support_quality=support_quality,
            respect_level=respect_level,
        )

    def _analyze_emotional_context(self, query: str, profile: UserProfile) -> float:
        """Analyze emotional context and user's current state"""
        # In production: Advanced NLP emotional analysis
        emotional_keywords = [
            "frustrated",
            "overwhelmed",
            "excited",
            "confused",
            "proud",
            "struggling",
        ]
        emotional_intensity = sum(
            1 for word in emotional_keywords if word in query.lower()
        ) / len(emotional_keywords)

        # Adjust based on user's trigger warnings
        trigger_penalty = sum(
            0.1
            for trigger in profile.trigger_warnings
            if trigger.lower() in query.lower()
        )

        return max(0, min(1, 0.7 + emotional_intensity - trigger_penalty))

    def _assess_shared_experience(self, query: str, profile: UserProfile) -> float:
        """Assess how much the AI can relate to user's experience"""
        # Check for neurodivergent-specific experiences
        experience_keywords = {
            NeurodivergentType.ADHD: [
                "hyperfocus",
                "time blindness",
                "rejection sensitivity",
                "dopamine",
            ],
            NeurodivergentType.AUTISM: [
                "masking",
                "sensory overload",
                "special interests",
                "stimming",
            ],
            NeurodivergentType.DYSLEXIA: [
                "reading challenges",
                "visual processing",
                "word confusion",
            ],
            NeurodivergentType.OVERLAP: ["multiple", "comorbid", "intersection"],
        }

        shared_score = 0
        for nd_type in profile.neurodivergent_types:
            if nd_type in experience_keywords:
                keywords = experience_keywords[nd_type]
                matches = sum(1 for keyword in keywords if keyword in query.lower())
                shared_score += matches / len(keywords)

        return min(1, shared_score / len(profile.neurodivergent_types))

    def _determine_understanding_depth(
        self, query: str, context: Dict[str, Any]
    ) -> float:
        """Determine how deep understanding needs to go"""
        complexity_indicators = [
            "why",
            "how",
            "explain",
            "understand",
            "meaning",
            "help me",
        ]
        complexity = sum(
            1 for indicator in complexity_indicators if indicator in query.lower()
        )

        # Adjust based on context richness
        context_depth = len(context.get("background", {})) / 10  # Normalize

        return min(1, (complexity / len(complexity_indicators)) + context_depth)

    def _calculate_validation_strength(self, profile: UserProfile, query: str) -> float:
        """Calculate how much validation the user needs"""
        validation_need_keywords = [
            "wrong",
            "weird",
            "broken",
            "bad at",
            "can't",
            "impossible",
        ]
        need_score = sum(
            1 for keyword in validation_need_keywords if keyword in query.lower()
        )

        # Higher validation for lower trust levels
        trust_factor = 1 - profile.trust_level

        return min(1, (need_score / len(validation_need_keywords)) + trust_factor * 0.3)

    def _assess_support_quality(
        self, profile: UserProfile, context: Dict[str, Any]
    ) -> float:
        """Assess what quality of support we can provide"""
        # Based on user's support needs and our knowledge
        support_coverage = 0
        for need in profile.support_needs:
            # Check if we have good knowledge for this support need
            # In production: Query knowledge base
            support_coverage += 0.8  # Assume good coverage for demo

        return min(1, support_coverage / max(1, len(profile.support_needs)))

    def _measure_respect_level(self, profile: UserProfile) -> float:
        """Always maximum respect for our community"""
        return 1.0  # We always show maximum respect


class TruthGraph:
    """
    🌐 Truth Graph Knowledge System

    Community-validated knowledge representation that:
    - Prioritizes lived experiences alongside research
    - Tracks source reliability and community validation
    - Maintains bias-aware knowledge scoring
    - Supports multiple perspectives on complex topics
    """

    def __init__(self):
        self.nodes: Dict[str, KnowledgeNode] = {}
        self.validation_thresholds = {
            NeurodivergentType.ADHD: 0.7,
            NeurodivergentType.AUTISM: 0.7,
            NeurodivergentType.DYSLEXIA: 0.7,
            NeurodivergentType.OVERLAP: 0.8,
            NeurodivergentType.GENERAL: 0.6,
        }
        self._initialize_core_knowledge()

    def _initialize_core_knowledge(self):
        """Initialize with core neurodivergent knowledge"""

        # ADHD Knowledge
        self.add_knowledge_node(
            KnowledgeNode(
                id="adhd_hyperfocus",
                concept="ADHD Hyperfocus",
                content="Hyperfocus is a state of intense concentration that many people with ADHD experience. It's a STRENGTH that allows deep, sustained attention on interesting tasks, often leading to exceptional productivity and creativity. However, it can make it challenging to shift attention when needed.",
                sources=[
                    {
                        "type": "research",
                        "title": "ADHD and Hyperfocus",
                        "reliability": 0.9,
                    },
                    {
                        "type": "lived_experience",
                        "community_votes": 234,
                        "reliability": 0.95,
                    },
                ],
                trust_score=0.92,
                community_validation={"adhd": 156, "autism": 23, "overlap": 45},
                strengths_focus=True,
                last_updated=datetime.now(),
                relationships=["adhd_attention", "adhd_creativity"],
            )
        )

        # Autism Knowledge
        self.add_knowledge_node(
            KnowledgeNode(
                id="autism_masking",
                concept="Autism Masking",
                content="Masking (or camouflaging) is when autistic people consciously or unconsciously hide their autistic traits to blend in with neurotypical expectations. While it can be a valuable social skill, it's mentally exhausting and can lead to burnout. Recognizing masking helps understand why social situations can be draining for autistic people.",
                sources=[
                    {
                        "type": "research",
                        "title": "Autism Masking Studies",
                        "reliability": 0.88,
                    },
                    {
                        "type": "lived_experience",
                        "community_votes": 312,
                        "reliability": 0.94,
                    },
                ],
                trust_score=0.91,
                community_validation={"autism": 198, "adhd": 34, "overlap": 67},
                strengths_focus=False,  # Important but not strength-focused
                last_updated=datetime.now(),
                relationships=["autism_social", "autism_burnout"],
            )
        )

        # Dyslexia Knowledge
        self.add_knowledge_node(
            KnowledgeNode(
                id="dyslexia_strengths",
                concept="Dyslexia Cognitive Strengths",
                content="People with dyslexia often have exceptional strengths in big-picture thinking, creativity, problem-solving, and spatial reasoning. These cognitive advantages stem from different brain wiring that, while making traditional reading challenging, creates unique thinking patterns valued in many fields including art, engineering, and entrepreneurship.",
                sources=[
                    {
                        "type": "research",
                        "title": "Dyslexia Advantages Research",
                        "reliability": 0.85,
                    },
                    {
                        "type": "lived_experience",
                        "community_votes": 189,
                        "reliability": 0.89,
                    },
                ],
                trust_score=0.87,
                community_validation={"dyslexia": 123, "overlap": 34, "general": 12},
                strengths_focus=True,
                last_updated=datetime.now(),
                relationships=["dyslexia_creativity", "dyslexia_spatial"],
            )
        )

        logger.info("Core neurodivergent knowledge initialized")

    def add_knowledge_node(self, node: KnowledgeNode):
        """Add new knowledge node to the graph"""
        self.nodes[node.id] = node

    def query_knowledge(
        self,
        query: str,
        neurodivergent_type: NeurodivergentType,
        require_strengths_focus: bool = False,
    ) -> List[KnowledgeNode]:
        """Query the knowledge graph for relevant information"""

        relevant_nodes = []
        query_lower = query.lower()

        for node in self.nodes.values():
            # Check concept and content relevance
            relevance_score = 0

            # Concept match
            if any(word in node.concept.lower() for word in query_lower.split()):
                relevance_score += 0.4

            # Content match
            if any(word in node.content.lower() for word in query_lower.split()):
                relevance_score += 0.3

            # Community validation for this neurodivergent type
            if neurodivergent_type.value in node.community_validation:
                validation_votes = node.community_validation[neurodivergent_type.value]
                if validation_votes > 10:  # Minimum validation threshold
                    relevance_score += 0.3

            # Strengths focus filter
            if require_strengths_focus and not node.strengths_focus:
                relevance_score *= 0.5

            # Trust score influence
            relevance_score *= node.trust_score

            if relevance_score > 0.3:  # Relevance threshold
                relevant_nodes.append(node)

        # Sort by relevance and trust
        relevant_nodes.sort(key=lambda n: n.trust_score, reverse=True)
        return relevant_nodes[:5]  # Top 5 most relevant


class StrengthsBasedReasoning:
    """
    💪 Strengths-Based Reasoning Engine

    Always focuses on capabilities, strengths, and positive reframing:
    - Identifies and amplifies user strengths
    - Reframes challenges as different approaches
    - Provides capability-focused solutions
    - Celebrates neurodivergent advantages
    """

    def __init__(self):
        self.strength_keywords = {
            NeurodivergentType.ADHD: [
                "hyperfocus",
                "creativity",
                "energy",
                "spontaneity",
                "innovation",
                "multitasking",
                "problem-solving",
                "enthusiasm",
                "big-picture thinking",
            ],
            NeurodivergentType.AUTISM: [
                "attention to detail",
                "pattern recognition",
                "deep expertise",
                "honesty",
                "reliability",
                "logical thinking",
                "specialized knowledge",
                "authenticity",
            ],
            NeurodivergentType.DYSLEXIA: [
                "spatial thinking",
                "creativity",
                "big-picture view",
                "problem-solving",
                "artistic ability",
                "innovation",
                "lateral thinking",
                "resilience",
            ],
        }

        self.reframing_patterns = {
            "can't focus": "selective attention that works best with interesting material",
            "too sensitive": "highly attuned to environmental details",
            "obsessed": "passionate and deeply knowledgeable",
            "weird": "uniquely creative and authentic",
            "slow reader": "thorough processor who catches details others miss",
            "forgetful": "present-focused with strong in-the-moment awareness",
        }

    def identify_strengths(self, user_profile: UserProfile, context: str) -> List[str]:
        """Identify strengths from user profile and context"""
        identified_strengths = []

        # Add explicit strengths from profile
        identified_strengths.extend(user_profile.strengths)

        # Identify implicit strengths from context
        context_lower = context.lower()
        for nd_type in user_profile.neurodivergent_types:
            if nd_type in self.strength_keywords:
                for strength in self.strength_keywords[nd_type]:
                    if strength in context_lower:
                        identified_strengths.append(strength)

        return list(set(identified_strengths))  # Remove duplicates

    def reframe_challenges(self, content: str) -> str:
        """Reframe challenges using strengths-based language"""
        reframed = content

        for negative, positive in self.reframing_patterns.items():
            reframed = reframed.replace(negative, positive)

        return reframed

    def generate_strength_amplification(self, strengths: List[str]) -> List[str]:
        """Generate suggestions for amplifying identified strengths"""
        amplifications = []

        for strength in strengths:
            if "creativity" in strength:
                amplifications.append(
                    "Consider exploring creative outlets that leverage your unique perspective"
                )
            elif "focus" in strength or "hyperfocus" in strength:
                amplifications.append(
                    "Use your powerful focus abilities on projects that genuinely interest you"
                )
            elif "detail" in strength:
                amplifications.append(
                    "Your attention to detail is valuable in quality-focused work"
                )
            elif "pattern" in strength:
                amplifications.append(
                    "Your pattern recognition can help solve complex problems others miss"
                )

        return amplifications


class BiasPreventionSystem:
    """
    🛡️ Bias Prevention and Detection System

    Continuously monitors for and prevents:
    - Deficit-based language and thinking
    - Neurotypical assumptions
    - Pathology model bias
    - Cultural and demographic bias
    - Representation gaps
    """

    def __init__(self):
        self.bias_indicators = {
            "deficit_language": [
                "disorder",
                "impairment",
                "deficit",
                "dysfunction",
                "abnormal",
                "broken",
                "wrong",
                "damaged",
                "needs fixing",
            ],
            "neurotypical_assumptions": [
                "normal",
                "should be able to",
                "everyone can",
                "just try harder",
                "if you really wanted to",
                "it's easy",
            ],
            "pathology_model": [
                "suffers from",
                "victim of",
                "affected by",
                "burden",
                "symptom",
                "diagnosis controls",
            ],
        }

        self.positive_alternatives = {
            "disorder": "neurodivergent type",
            "impairment": "different processing style",
            "deficit": "alternative approach",
            "dysfunction": "different function",
            "abnormal": "neurodivergent",
            "suffers from": "experiences",
            "victim of": "person with",
        }

    def scan_for_bias(self, content: str) -> Dict[str, float]:
        """Scan content for bias indicators"""
        bias_scores = {}
        content_lower = content.lower()

        for bias_type, indicators in self.bias_indicators.items():
            matches = sum(1 for indicator in indicators if indicator in content_lower)
            bias_score = matches / len(indicators) if indicators else 0
            bias_scores[bias_type] = bias_score

        return bias_scores

    def remove_bias(self, content: str) -> str:
        """Remove bias by replacing problematic language"""
        cleaned_content = content

        for negative, positive in self.positive_alternatives.items():
            cleaned_content = cleaned_content.replace(negative, positive)

        return cleaned_content


class NeurodivergentAICore:
    """
    🧠💎⚡ Main Neurodivergent AI Core Engine

    Integrates all components to provide neurodivergent-first AI responses:
    - Quantum empathy understanding
    - Truth graph knowledge retrieval
    - Strengths-based reasoning
    - Bias prevention and removal
    - Adaptive communication
    """

    def __init__(self):
        self.empathy_engine = QuantumEmpathyEngine()
        self.truth_graph = TruthGraph()
        self.strengths_engine = StrengthsBasedReasoning()
        self.bias_prevention = BiasPreventionSystem()
        self.active_sessions = {}  # Track user sessions

        logger.info("🧠 Neurodivergent AI Core Engine initialized")
        logger.info("✅ Quantum Empathy Engine active")
        logger.info("✅ Truth Graph knowledge system loaded")
        logger.info("✅ Strengths-based reasoning enabled")
        logger.info("✅ Bias prevention system active")

    async def process_query(
        self,
        query: str,
        user_profile: UserProfile,
        context: Optional[Dict[str, Any]] = None,
    ) -> AIResponse:
        """
        🌟 Main query processing with full neurodivergent-first approach
        """

        if context is None:
            context = {}

        logger.info(f"Processing query for user {user_profile.user_id}")

        # 1. Calculate empathy vector
        empathy_vector = self.empathy_engine.calculate_empathy_vector(
            user_profile, query, context
        )

        # 2. Retrieve relevant knowledge
        relevant_knowledge = self.truth_graph.query_knowledge(
            query,
            user_profile.neurodivergent_types[0],  # Primary type
            require_strengths_focus=True,
        )

        # 3. Identify and amplify strengths
        strengths = self.strengths_engine.identify_strengths(user_profile, query)
        strength_amplifications = self.strengths_engine.generate_strength_amplification(
            strengths
        )

        # 4. Generate initial response
        initial_response = await self._generate_response_content(
            query, relevant_knowledge, strengths, user_profile
        )

        # 5. Apply strengths-based reframing
        reframed_response = self.strengths_engine.reframe_challenges(initial_response)

        # 6. Remove bias
        bias_check = self.bias_prevention.scan_for_bias(reframed_response)
        clean_response = self.bias_prevention.remove_bias(reframed_response)

        # 7. Adapt communication style
        adapted_response = self._adapt_communication_style(
            clean_response, user_profile.communication_mode
        )

        # 8. Calculate confidence and trust scores
        confidence_score = self._calculate_confidence(
            relevant_knowledge, empathy_vector
        )
        trust_score = self._calculate_trust_score(relevant_knowledge, bias_check)

        # 9. Generate reasoning path
        reasoning_path = self._generate_reasoning_path(
            query, relevant_knowledge, strengths, empathy_vector
        )

        # 10. Compile support resources
        support_resources = self._compile_support_resources(user_profile, query)

        return AIResponse(
            content=adapted_response,
            reasoning_path=reasoning_path,
            confidence_score=confidence_score,
            trust_score=trust_score,
            sources=[
                {"node_id": node.id, "trust": node.trust_score}
                for node in relevant_knowledge
            ],
            empathy_vector=empathy_vector,
            bias_check=bias_check,
            neurodivergent_lens=user_profile.neurodivergent_types[0],
            communication_adaptation={
                "mode": user_profile.communication_mode.value,
                "sensory": user_profile.sensory_preference.value,
            },
            suggestions=strength_amplifications,
            support_resources=support_resources,
        )

    async def _generate_response_content(
        self,
        query: str,
        knowledge_nodes: List[KnowledgeNode],
        strengths: List[str],
        user_profile: UserProfile,
    ) -> str:
        """Generate the core response content"""

        # Combine relevant knowledge
        knowledge_content = []
        for node in knowledge_nodes:
            knowledge_content.append(node.content)

        # Create response based on query type and knowledge
        if "how" in query.lower() or "why" in query.lower():
            # Explanatory response
            response = f"Based on our community knowledge and research, here's what we understand:\n\n"
            for content in knowledge_content[:2]:  # Top 2 most relevant
                response += f"• {content}\n\n"

        elif any(word in query.lower() for word in ["help", "support", "struggle"]):
            # Support-focused response
            response = f"I hear you, and you're not alone in this experience. Here are some insights from our community:\n\n"
            for content in knowledge_content:
                response += f"{content}\n\n"

            # Add strength recognition
            if strengths:
                response += f"Remember, you have these valuable strengths: {', '.join(strengths[:3])}. "

        else:
            # General informational response
            response = "Here's what our neurodivergent community knowledge shows:\n\n"
            for content in knowledge_content:
                response += f"{content}\n\n"

        return response

    def _adapt_communication_style(self, content: str, mode: CommunicationMode) -> str:
        """Adapt content to user's communication preferences"""

        if mode == CommunicationMode.DIRECT:
            # Make more concise and direct
            lines = content.split("\n")
            key_points = [
                line for line in lines if line.strip() and not line.startswith("•")
            ]
            return "\n\n".join(key_points[:3])

        elif mode == CommunicationMode.DETAILED:
            # Add more context and examples
            return (
                content
                + "\n\nWould you like me to explore any specific aspect in more detail?"
            )

        elif mode == CommunicationMode.STRUCTURED:
            # Add clear structure
            structured = "## Key Points:\n\n"
            lines = content.split("\n")
            for i, line in enumerate(lines[:5], 1):
                if line.strip():
                    structured += f"{i}. {line.strip()}\n"
            return structured

        elif mode == CommunicationMode.EMPATHETIC:
            # Add more emotional support
            empathetic_prefix = "I want you to know that your experience is valid and you're part of a wonderful community. "
            return empathetic_prefix + content

        elif mode == CommunicationMode.SCIENTIFIC:
            # Add research context
            scientific_prefix = "Based on current research and community validation: "
            return scientific_prefix + content

        return content  # Default: no change

    def _calculate_confidence(
        self, knowledge_nodes: List[KnowledgeNode], empathy_vector: EmpathyVector
    ) -> float:
        """Calculate confidence score based on knowledge quality and empathy"""
        if not knowledge_nodes:
            return 0.3

        # Average trust score of knowledge
        knowledge_confidence = sum(node.trust_score for node in knowledge_nodes) / len(
            knowledge_nodes
        )

        # Empathy contributes to confidence
        empathy_confidence = (
            empathy_vector.understanding_depth + empathy_vector.shared_experience
        ) / 2

        return (knowledge_confidence * 0.7) + (empathy_confidence * 0.3)

    def _calculate_trust_score(
        self, knowledge_nodes: List[KnowledgeNode], bias_check: Dict[str, float]
    ) -> float:
        """Calculate overall trust score"""
        if not knowledge_nodes:
            return 0.5

        # Base trust from knowledge
        knowledge_trust = sum(node.trust_score for node in knowledge_nodes) / len(
            knowledge_nodes
        )

        # Reduce trust based on bias presence
        bias_penalty = sum(bias_check.values()) / len(bias_check) if bias_check else 0

        return max(0.1, knowledge_trust - (bias_penalty * 0.3))

    def _generate_reasoning_path(
        self,
        query: str,
        knowledge_nodes: List[KnowledgeNode],
        strengths: List[str],
        empathy_vector: EmpathyVector,
    ) -> List[str]:
        """Generate transparent reasoning path"""
        path = [
            f"1. Analyzed your query: '{query[:50]}...' with neurodivergent-first approach",
            f"2. Retrieved {len(knowledge_nodes)} relevant knowledge nodes from community truth graph",
            f"3. Identified {len(strengths)} personal strengths to incorporate",
            f"4. Applied empathy analysis (resonance: {empathy_vector.emotional_resonance:.1f})",
            f"5. Performed bias check and removed deficit-based language",
            f"6. Adapted response to your communication preferences",
        ]
        return path

    def _compile_support_resources(
        self, user_profile: UserProfile, query: str
    ) -> List[str]:
        """Compile relevant support resources"""
        resources = []

        # Add neurodivergent type specific resources
        for nd_type in user_profile.neurodivergent_types:
            if nd_type == NeurodivergentType.ADHD:
                resources.append("ADHD community support groups")
                resources.append("Time management tools designed for ADHD")
            elif nd_type == NeurodivergentType.AUTISM:
                resources.append("Autism acceptance communities")
                resources.append("Sensory support resources")
            elif nd_type == NeurodivergentType.DYSLEXIA:
                resources.append("Dyslexia pride networks")
                resources.append("Alternative learning tools")

        # Add general neurodivergent resources
        resources.extend(
            [
                "Neurodivergent-affirming therapists directory",
                "Strength-based coaching resources",
                "Community peer support networks",
            ]
        )

        return resources[:5]  # Limit to top 5


# 🚀 Demo Functions


async def demo_ai_core():
    """Demonstrate the AI Core capabilities"""

    print("🧠💎⚡ Neurodivergent AI Core Demo")
    print("=" * 50)

    # Initialize AI Core
    ai_core = NeurodivergentAICore()

    # Create sample user profile
    user_profile = UserProfile(
        user_id="demo_user_001",
        neurodivergent_types=[NeurodivergentType.ADHD, NeurodivergentType.AUTISM],
        communication_mode=CommunicationMode.EMPATHETIC,
        sensory_preference=SensoryPreference.LOW_STIMULATION,
        strengths=["creativity", "pattern recognition", "hyperfocus"],
        support_needs=["time management", "social scripting"],
        trigger_warnings=["deficit language", "cure rhetoric"],
        preferred_examples=["creative projects", "technology"],
        energy_patterns={"morning": 0.8, "afternoon": 0.6, "evening": 0.9},
        consent_timestamp=datetime.now(),
        trust_level=0.85,
    )

    # Demo queries
    queries = [
        "I'm having trouble focusing at work and feeling overwhelmed",
        "What are the strengths of being ADHD?",
        "How can I explain my autism to my family?",
        "I feel like I'm broken because I can't read like everyone else",
    ]

    for i, query in enumerate(queries, 1):
        print(f"\n🔍 Demo Query {i}: {query}")
        print("-" * 40)

        # Process query
        response = await ai_core.process_query(query, user_profile)

        # Display results
        print(f"🌟 Response: {response.content[:200]}...")
        print(f"🎯 Confidence: {response.confidence_score:.2f}")
        print(f"🛡️ Trust Score: {response.trust_score:.2f}")
        print(
            f"❤️ Empathy Vector: Resonance={response.empathy_vector.emotional_resonance:.2f}"
        )
        print(f"🚨 Bias Check: {max(response.bias_check.values()):.2f}")
        print(f"💪 Suggestions: {len(response.suggestions)} strength amplifications")
        print(f"🤝 Support Resources: {len(response.support_resources)} available")


if __name__ == "__main__":
    asyncio.run(demo_ai_core())

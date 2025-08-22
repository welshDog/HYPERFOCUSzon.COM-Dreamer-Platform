"""
🤝💎⚡ NEURODIVERGENT COMMUNITY MANAGEMENT SYSTEM ⚡💎🤝
Safe, supportive community platform designed specifically for neurodivergent individuals
"""

import asyncio
import uuid
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional


class CommunityRole(Enum):
    MEMBER = "member"
    PEER_SUPPORTER = "peer_supporter"
    MODERATOR = "moderator"
    CRISIS_COUNSELOR = "crisis_counselor"
    ADMIN = "admin"


class ContentType(Enum):
    POST = "post"
    COMMENT = "comment"
    PRIVATE_MESSAGE = "private_message"
    CRISIS_REPORT = "crisis_report"


class ModerationAction(Enum):
    WARN = "warn"
    TIMEOUT = "timeout"
    REMOVE_CONTENT = "remove_content"
    BAN = "ban"
    EDUCATIONAL_RESPONSE = "educational_response"


@dataclass
class CommunityMember:
    user_id: str
    username: str
    neurodivergent_types: List[str]
    pronouns: Optional[str] = None
    special_interests: List[str] = field(default_factory=list)
    support_preferences: Dict[str, any] = field(default_factory=dict)
    crisis_support_opt_in: bool = False
    peer_support_training: bool = False
    role: CommunityRole = CommunityRole.MEMBER
    join_date: datetime = field(default_factory=datetime.now)
    last_active: datetime = field(default_factory=datetime.now)
    community_points: int = 0
    safety_reports: int = 0


@dataclass
class SafeSpace:
    space_id: str
    name: str
    description: str
    neurodivergent_focus: List[str]  # ADHD, Autism, etc.
    special_interests: List[str] = field(default_factory=list)
    moderation_level: str = "high"  # high, medium, low
    member_count: int = 0
    guidelines: List[str] = field(default_factory=list)
    peer_supporters: List[str] = field(default_factory=list)
    created_date: datetime = field(default_factory=datetime.now)


@dataclass
class CommunityPost:
    post_id: str
    author_id: str
    space_id: str
    content: str
    content_type: ContentType
    timestamp: datetime = field(default_factory=datetime.now)
    tags: List[str] = field(default_factory=list)
    trigger_warnings: List[str] = field(default_factory=list)
    support_requested: bool = False
    crisis_indicators: List[str] = field(default_factory=list)
    moderation_status: str = "approved"
    upvotes: int = 0
    support_responses: int = 0


class NeurodivergentCommunityManager:
    """🤝 Main community management system for neurodivergent users"""

    def __init__(self):
        self.members: Dict[str, CommunityMember] = {}
        self.safe_spaces: Dict[str, SafeSpace] = {}
        self.posts: Dict[str, CommunityPost] = {}
        self.peer_supporters: Dict[str, List[str]] = {}  # space_id -> supporter_ids
        self.crisis_network: List[str] = []  # Crisis-trained member IDs
        self.community_guidelines = self._initialize_guidelines()
        self.ableism_detector = AbleismDetectionSystem()

        # Initialize default safe spaces
        self._create_default_safe_spaces()

    def _initialize_guidelines(self) -> Dict[str, List[str]]:
        """Initialize comprehensive community guidelines for neurodivergent safety"""
        return {
            "core_principles": [
                "🌈 Neurodivergent pride and identity celebration",
                "🤝 Mutual support and understanding",
                "🛡️ Zero tolerance for ableism or discrimination",
                "💙 Assume positive intent while holding accountability",
                "🧠 Respect different communication styles and needs",
                "⚡ Honor different energy levels and social capacities",
                "🌱 Create space for growth and learning",
            ],
            "communication_guidelines": [
                "Use person-first OR identity-first language based on individual preference",
                "Respect stimming, communication devices, and alternative communication",
                "Provide content warnings for potentially triggering topics",
                "Use clear, direct communication when possible",
                "Respect processing time - not everyone responds immediately",
                "Ask before giving advice unless specifically requested",
            ],
            "accessibility_requirements": [
                "Use alt text for images when possible",
                "Avoid flashing or rapidly moving content",
                "Provide trigger warnings for: medical topics, trauma, sensory descriptions",
                "Use clear subject lines and organized content structure",
                "Respect different reading/comprehension styles",
            ],
            "prohibited_content": [
                "Ableist language or attitudes about any disability/neurodivergence",
                "Functioning labels (high/low functioning)",
                "Inspiration porn or patronizing content about neurodivergent people",
                "Unsolicited medical advice or cure discussions",
                "Deliberate triggering of sensory sensitivities",
                "Harassment based on communication style or support needs",
            ],
            "crisis_support_guidelines": [
                "🆘 If someone is in immediate danger, help them contact crisis services",
                "💙 Provide emotional support while connecting to professional help",
                "🚫 Don't attempt to be someone's therapist or medical provider",
                "🤝 Offer practical support and resource connection",
                "⚡ Respect boundaries around crisis support capacity",
            ],
        }

    def _create_default_safe_spaces(self):
        """Create initial safe spaces for different neurodivergent communities"""
        default_spaces = [
            {
                "name": "🎯 ADHD Hyperfocus Hub",
                "description": "Share your special interests, hyperfocus sessions, and ADHD wins!",
                "neurodivergent_focus": ["ADHD"],
                "guidelines": [
                    "Celebrate hyperfocus achievements and interests",
                    "Share ADHD-friendly productivity tips",
                    "Support executive function challenges",
                    "No shame around ADHD struggles",
                ],
            },
            {
                "name": "🌈 Autism Connection Circle",
                "description": "Connect with other autistic individuals in a sensory-friendly space",
                "neurodivergent_focus": ["Autism"],
                "guidelines": [
                    "Respect stimming and self-regulation needs",
                    "Share special interests and detailed knowledge",
                    "Support sensory and social challenges",
                    "Use clear, direct communication",
                ],
            },
            {
                "name": "🧠 Executive Function Support",
                "description": "Strategies and support for executive function challenges",
                "neurodivergent_focus": ["ADHD", "Autism", "Executive Dysfunction"],
                "guidelines": [
                    "Share practical strategies and tools",
                    "Support without judgment for struggles",
                    "Celebrate small wins and progress",
                    "Respect different organizational styles",
                ],
            },
            {
                "name": "🤝 Social Skills Practice Space",
                "description": "Safe place to practice social interactions and ask questions",
                "neurodivergent_focus": ["Autism", "Social Anxiety"],
                "guidelines": [
                    "Practice conversations in low-pressure environment",
                    "Ask questions about social situations",
                    "Share social scripts and strategies",
                    "No judgment for social differences",
                ],
            },
            {
                "name": "🆘 Crisis Support Network",
                "description": "Peer support for mental health crises and overwhelm",
                "neurodivergent_focus": ["All"],
                "moderation_level": "high",
                "guidelines": [
                    "Immediate crisis support and resource connection",
                    "Trauma-informed peer support approaches",
                    "Professional backup available 24/7",
                    "Strict confidentiality and safety protocols",
                ],
            },
            {
                "name": "🌟 Neurodivergent Pride & Joy",
                "description": "Celebrate neurodivergent identity, culture, and achievements",
                "neurodivergent_focus": ["All"],
                "guidelines": [
                    "Share neurodivergent pride and culture",
                    "Celebrate achievements and milestones",
                    "Discuss neurodivergent identity and community",
                    "Counter ableist narratives with pride",
                ],
            },
        ]

        for space_data in default_spaces:
            space_id = str(uuid.uuid4())
            self.safe_spaces[space_id] = SafeSpace(
                space_id=space_id,
                name=space_data["name"],
                description=space_data["description"],
                neurodivergent_focus=space_data["neurodivergent_focus"],
                moderation_level=space_data.get("moderation_level", "high"),
                guidelines=space_data["guidelines"],
            )

    async def register_member(self, user_data: Dict) -> CommunityMember:
        """Register a new community member with neurodivergent-friendly onboarding"""
        member = CommunityMember(
            user_id=user_data["user_id"],
            username=user_data["username"],
            neurodivergent_types=user_data.get("neurodivergent_types", []),
            pronouns=user_data.get("pronouns"),
            special_interests=user_data.get("special_interests", []),
            support_preferences=user_data.get("support_preferences", {}),
            crisis_support_opt_in=user_data.get("crisis_support_opt_in", False),
        )

        self.members[member.user_id] = member

        # Auto-suggest relevant safe spaces
        suggested_spaces = await self._suggest_safe_spaces(member)

        # Send welcome message with community orientation
        welcome_message = await self._generate_welcome_message(member, suggested_spaces)

        return member

    async def _suggest_safe_spaces(self, member: CommunityMember) -> List[SafeSpace]:
        """Suggest relevant safe spaces based on member's neurodivergent types and interests"""
        suggestions = []

        for space in self.safe_spaces.values():
            # Match neurodivergent types
            if any(
                nt in space.neurodivergent_focus for nt in member.neurodivergent_types
            ):
                suggestions.append(space)

            # Match special interests
            elif any(
                interest in space.special_interests
                for interest in member.special_interests
            ):
                suggestions.append(space)

            # Include universal spaces
            elif "All" in space.neurodivergent_focus:
                suggestions.append(space)

        return suggestions[:5]  # Limit to top 5 suggestions

    async def _generate_welcome_message(
        self, member: CommunityMember, suggested_spaces: List[SafeSpace]
    ) -> Dict:
        """Generate personalized welcome message for new member"""
        neurodivergent_celebration = []
        if "ADHD" in member.neurodivergent_types:
            neurodivergent_celebration.append(
                "🎯 Your ADHD superpowers are welcome here!"
            )
        if "Autism" in member.neurodivergent_types:
            neurodivergent_celebration.append(
                "🌈 Your autistic identity is celebrated here!"
            )

        return {
            "type": "community_welcome",
            "message": f"🌟 Welcome to HYPERFOCUS ZONE, {member.username}!",
            "neurodivergent_celebration": neurodivergent_celebration,
            "community_values": [
                "💙 You belong here exactly as you are",
                "🛡️ This is a safe space for all neurodivergent people",
                "🤝 We support each other with understanding and respect",
                "⚡ Your unique perspectives make our community stronger",
            ],
            "suggested_spaces": [
                {
                    "name": space.name,
                    "description": space.description,
                    "id": space.space_id,
                }
                for space in suggested_spaces
            ],
            "getting_started": [
                "🔍 Explore safe spaces that match your interests",
                "👋 Introduce yourself (only share what feels comfortable)",
                "📋 Review community guidelines and accessibility features",
                "🆘 Learn about crisis support resources if needed",
                "🌱 Take your time - there's no pressure to participate immediately",
            ],
            "accessibility_note": "💙 All community features are designed with neurodivergent accessibility in mind. Reach out if you need any accommodations!",
        }

    async def create_post(
        self,
        author_id: str,
        space_id: str,
        content: str,
        tags: List[str] = None,
        trigger_warnings: List[str] = None,
        support_requested: bool = False,
    ) -> CommunityPost:
        """Create a new community post with automatic content analysis"""

        if author_id not in self.members:
            raise ValueError("Author must be a registered community member")

        if space_id not in self.safe_spaces:
            raise ValueError("Invalid safe space ID")

        # Analyze content for ableism and crisis indicators
        ableism_analysis = await self.ableism_detector.analyze_content(content)
        crisis_analysis = await self._analyze_crisis_indicators(content)

        post = CommunityPost(
            post_id=str(uuid.uuid4()),
            author_id=author_id,
            space_id=space_id,
            content=content,
            content_type=ContentType.POST,
            tags=tags or [],
            trigger_warnings=trigger_warnings or [],
            support_requested=support_requested,
            crisis_indicators=crisis_analysis.get("indicators", []),
        )

        # Handle ableism detection
        if ableism_analysis["ableism_detected"]:
            return await self._handle_ableism_detection(post, ableism_analysis)

        # Handle crisis detection
        if crisis_analysis["crisis_level"] in ["high", "critical"]:
            return await self._handle_crisis_detection(post, crisis_analysis)

        # Auto-tag based on content
        auto_tags = await self._generate_auto_tags(content, space_id)
        post.tags.extend(auto_tags)

        self.posts[post.post_id] = post

        # Notify relevant peer supporters if support requested
        if support_requested:
            await self._notify_peer_supporters(post)

        return post

    async def _analyze_crisis_indicators(self, content: str) -> Dict:
        """Analyze content for mental health crisis indicators"""
        crisis_keywords = {
            "high": ["crisis", "emergency", "urgent", "immediate help", "danger"],
            "moderate": ["overwhelmed", "breaking down", "can't cope", "desperate"],
            "suicide": ["kill myself", "end my life", "suicide", "not worth living"],
            "self_harm": ["hurt myself", "self harm", "cutting", "deserve pain"],
            "severe_distress": ["hopeless", "worthless", "burden", "pointless"],
        }

        content_lower = content.lower()
        detected_indicators = []
        crisis_level = "low"

        for level, keywords in crisis_keywords.items():
            for keyword in keywords:
                if keyword in content_lower:
                    detected_indicators.append(keyword)
                    if level in ["suicide", "self_harm"]:
                        crisis_level = "critical"
                    elif level == "high" and crisis_level != "critical":
                        crisis_level = "high"
                    elif level == "moderate" and crisis_level not in [
                        "critical",
                        "high",
                    ]:
                        crisis_level = "moderate"

        return {
            "crisis_level": crisis_level,
            "indicators": detected_indicators,
            "professional_intervention_needed": crisis_level in ["critical", "high"],
        }

    async def _handle_crisis_detection(
        self, post: CommunityPost, crisis_analysis: Dict
    ) -> Dict:
        """Handle detected crisis content with appropriate intervention"""

        # Alert crisis-trained peer supporters immediately
        crisis_supporters = [
            member_id
            for member_id, member in self.members.items()
            if member.role
            in [CommunityRole.CRISIS_COUNSELOR, CommunityRole.PEER_SUPPORTER]
            and member_id in self.crisis_network
        ]

        # Create crisis intervention response
        intervention_response = {
            "type": "crisis_intervention",
            "post_id": post.post_id,
            "crisis_level": crisis_analysis["crisis_level"],
            "immediate_actions": [],
            "peer_support_activated": True,
            "professional_resources": {
                "crisis_hotline": "988 (US Suicide & Crisis Lifeline)",
                "crisis_text": "Text HOME to 741741",
                "emergency": "911 for immediate danger",
            },
        }

        if crisis_analysis["crisis_level"] == "critical":
            intervention_response["immediate_actions"] = [
                "🆘 Immediate crisis support has been activated",
                "📞 Crisis counselors have been notified",
                "🤝 Peer supporters are on standby",
                "💙 You are not alone - help is available right now",
            ]

            # Mark post for immediate professional review
            post.moderation_status = "crisis_review"

        elif crisis_analysis["crisis_level"] == "high":
            intervention_response["immediate_actions"] = [
                "💙 Crisis support activated - you matter and help is available",
                "🤝 Trained peer supporters will reach out soon",
                "📞 Consider calling 988 for immediate support",
                "🌟 This community is here for you",
            ]

        # Notify crisis network
        await self._notify_crisis_network(post, crisis_analysis)

        return intervention_response

    async def _notify_crisis_network(self, post: CommunityPost, crisis_analysis: Dict):
        """Notify crisis-trained community members of potential crisis"""
        notification = {
            "type": "crisis_alert",
            "post_id": post.post_id,
            "author_id": post.author_id,
            "crisis_level": crisis_analysis["crisis_level"],
            "indicators": crisis_analysis["indicators"],
            "timestamp": datetime.now(),
            "response_needed": crisis_analysis["professional_intervention_needed"],
        }

        # Send to all crisis-trained members
        for supporter_id in self.crisis_network:
            # In real implementation, send actual notification
            print(f"Crisis alert sent to {supporter_id}: {notification}")

    async def _notify_peer_supporters(self, post: CommunityPost):
        """Notify peer supporters when support is requested"""
        space = self.safe_spaces[post.space_id]

        for supporter_id in space.peer_supporters:
            notification = {
                "type": "peer_support_request",
                "post_id": post.post_id,
                "space_name": space.name,
                "support_type": "general",
                "timestamp": datetime.now(),
            }
            # Send notification to peer supporter
            print(f"Peer support notification sent to {supporter_id}")

    async def _generate_auto_tags(self, content: str, space_id: str) -> List[str]:
        """Generate automatic tags based on content analysis"""
        auto_tags = []
        content_lower = content.lower()

        # ADHD-related tags
        adhd_keywords = {
            "hyperfocus": ["hyperfocus", "zone", "flow state", "hours passed"],
            "executive_function": [
                "procrastination",
                "cant start",
                "organization",
                "priorities",
            ],
            "sensory": ["overstimulated", "sensory overload", "noise", "texture"],
            "emotional_regulation": [
                "rejection sensitive",
                "rsd",
                "emotional",
                "overwhelmed",
            ],
        }

        # Autism-related tags
        autism_keywords = {
            "stimming": ["stimming", "fidget", "flapping", "rocking"],
            "social": [
                "social anxiety",
                "social interaction",
                "small talk",
                "conversation",
            ],
            "routine": ["routine", "schedule", "change", "transition"],
            "special_interests": ["special interest", "obsessed", "passionate about"],
        }

        # Check for keyword matches
        for category, keywords in {**adhd_keywords, **autism_keywords}.items():
            if any(keyword in content_lower for keyword in keywords):
                auto_tags.append(category)

        return auto_tags

    async def moderate_content(
        self, content_id: str, moderator_id: str, action: ModerationAction, reason: str
    ) -> Dict:
        """Moderate community content with neurodivergent-aware approach"""

        if moderator_id not in self.members:
            raise ValueError("Moderator must be registered community member")

        moderator = self.members[moderator_id]
        if moderator.role not in [CommunityRole.MODERATOR, CommunityRole.ADMIN]:
            raise ValueError("User does not have moderation privileges")

        if content_id not in self.posts:
            raise ValueError("Content not found")

        post = self.posts[content_id]
        author = self.members[post.author_id]

        moderation_result = {
            "action_taken": action.value,
            "reason": reason,
            "moderator_id": moderator_id,
            "timestamp": datetime.now(),
            "educational_component": None,
            "support_offered": False,
        }

        # Neurodivergent-aware moderation approaches
        if action == ModerationAction.EDUCATIONAL_RESPONSE:
            moderation_result["educational_component"] = (
                await self._generate_educational_response(reason, post)
            )
            moderation_result["support_offered"] = True

        elif action == ModerationAction.WARN:
            # Gentle, educational warning with support resources
            moderation_result[
                "warning_message"
            ] = f"""
            💙 Community Guidance Notice:

            Hi {author.username}, we noticed that your recent post may not align with our community guidelines.

            Specifically: {reason}

            Our community is built on mutual respect and support for all neurodivergent people. We understand that communication differences are part of neurodivergence, and we're here to help you engage successfully in our community.

            If you'd like to discuss this or need support with community participation, please reach out to our peer supporters. We're here to help, not to punish.

            💙 Community Support Team
            """
            moderation_result["support_offered"] = True

        # Update post status
        if action in [ModerationAction.REMOVE_CONTENT, ModerationAction.BAN]:
            post.moderation_status = "removed"

        return moderation_result

    async def _generate_educational_response(
        self, violation_reason: str, post: CommunityPost
    ) -> str:
        """Generate educational response for community guideline violations"""

        educational_responses = {
            "ableist_language": """
            🌈 Community Learning Moment:

            We use identity-first language (autistic person) or person-first language (person with ADHD) based on individual preference. Functioning labels and ableist terms can be harmful to our community members.

            Resources:
            - Neurodivergent language guide: [link]
            - Why language matters in disability community: [link]

            Thank you for being open to learning with us! 💙
            """,
            "unsolicited_advice": """
            💙 Gentle Reminder:

            In our community, we ask before giving advice unless someone specifically requests it. Many neurodivergent people have experienced a lot of unsolicited advice that wasn't helpful.

            Great ways to support:
            - "Would you like suggestions, or are you looking for understanding?"
            - "I have some thoughts if you're open to them."
            - Simply offering validation and support

            Thanks for being part of our supportive community!
            """,
            "inspiration_porn": """
            🌟 Community Values Note:

            We celebrate neurodivergent achievements without treating them as inspiration for neurotypical people. Our achievements are for us and our community, not to make others feel inspired about their own lives.

            We prefer celebrating:
            - Genuine achievements and milestones
            - Overcoming ableist barriers
            - Community support and connection

            Thank you for understanding! 💜
            """,
        }

        return educational_responses.get(
            violation_reason,
            "Thank you for being part of our learning community. Please review our guidelines for more information.",
        )


class AbleismDetectionSystem:
    """🛡️ AI system for detecting ableist language and harmful content"""

    def __init__(self):
        self.ableist_terms = {
            "functioning_labels": [
                "high functioning",
                "low functioning",
                "severe autism",
                "mild autism",
            ],
            "ableist_slurs": ["retard", "spaz", "psycho", "crazy", "insane", "mental"],
            "harmful_phrases": [
                "person trapped in autism",
                "suffers from autism",
                "victim of adhd",
                "normal person",
                "everyone is a little autistic",
                "you don't look disabled",
                "inspiration porn",
                "overcome autism",
                "cure autism",
            ],
            "medical_model": [
                "autism epidemic",
                "autism crisis",
                "burden on family",
                "tragedy",
                "broken",
                "damaged",
                "defective",
            ],
        }

        self.context_exceptions = [
            "discussing harmful language",
            "educational context",
            "reclaiming slurs",
            "historical discussion",
        ]

    async def analyze_content(self, content: str) -> Dict:
        """Analyze content for ableist language and provide educational response"""
        content_lower = content.lower()
        detected_issues = []
        severity_level = "none"

        for category, terms in self.ableist_terms.items():
            for term in terms:
                if term in content_lower:
                    detected_issues.append(
                        {
                            "category": category,
                            "term": term,
                            "educational_note": self._get_educational_note(
                                category, term
                            ),
                        }
                    )

                    if category in ["ableist_slurs", "medical_model"]:
                        severity_level = "high"
                    elif severity_level != "high":
                        severity_level = "moderate"

        return {
            "ableism_detected": len(detected_issues) > 0,
            "severity": severity_level,
            "issues": detected_issues,
            "educational_response": self._generate_educational_response(
                detected_issues
            ),
            "action_recommended": "educational" if detected_issues else "none",
        }

    def _get_educational_note(self, category: str, term: str) -> str:
        """Get educational explanation for detected ableist language"""

        educational_notes = {
            "functioning_labels": f"The term '{term}' is considered a functioning label. These labels reduce complex human experiences to simple categories and can be harmful to the autism community.",
            "ableist_slurs": f"The word '{term}' is an ableist slur that has been used to harm disabled people. We use respectful language in our community.",
            "harmful_phrases": f"The phrase '{term}' perpetuates harmful stereotypes about neurodivergent people. We focus on respectful, accurate language.",
            "medical_model": f"The term '{term}' reflects medical model thinking that views neurodivergence as inherently negative. We embrace neurodiversity and acceptance.",
        }

        return educational_notes.get(
            category,
            "This language may not align with our community values of respect and acceptance.",
        )

    def _generate_educational_response(self, issues: List[Dict]) -> str:
        """Generate comprehensive educational response for detected issues"""
        if not issues:
            return ""

        response = "💙 Language Guidance:\n\n"

        for issue in issues:
            response += f"• {issue['educational_note']}\n"

        response += """
        \nOur community values respectful language that honors the dignity and humanity of all neurodivergent people. We understand that language is always evolving, and we're here to learn together.

        For more information about respectful language, check our community guidelines or reach out to peer supporters.

        Thank you for being part of our inclusive community! 🌈
        """

        return response


# Example usage and testing
async def test_community_system():
    """Test the community management system"""
    community = NeurodivergentCommunityManager()

    # Test member registration
    member_data = {
        "user_id": "user123",
        "username": "ADHDSupernova",
        "neurodivergent_types": ["ADHD", "Autism"],
        "pronouns": "they/them",
        "special_interests": ["astronomy", "coding", "cats"],
        "crisis_support_opt_in": True,
    }

    member = await community.register_member(member_data)
    print("Registered member:", member.username)

    # Test post creation
    space_id = list(community.safe_spaces.keys())[0]  # Get first safe space

    post = await community.create_post(
        author_id="user123",
        space_id=space_id,
        content="I'm feeling really overwhelmed today and could use some support",
        support_requested=True,
    )

    print("Created post:", post.post_id)

    # Test ableism detection
    ableist_content = "My high functioning autistic friend is so inspiring"
    ableism_result = await community.ableism_detector.analyze_content(ableist_content)
    print("Ableism detection:", ableism_result)


if __name__ == "__main__":
    asyncio.run(test_community_system())

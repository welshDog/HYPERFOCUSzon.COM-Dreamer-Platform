"""
🌈💎⚡ AUTISM SENSORY TRANSCENDENCE SYSTEM - OMNIVERSAL SENSORY SUPPORT ⚡💎🌈
Revolutionary sensory processing support and social cognition enhancement for autistic users
"""

import asyncio
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List


class SensoryState(Enum):
    OPTIMAL = "optimal"
    ELEVATED = "elevated"
    OVERWHELMED = "overwhelmed"
    OVERLOADED = "overloaded"
    SHUTDOWN_RISK = "shutdown_risk"
    RECOVERY = "recovery"


class SensoryModality(Enum):
    VISUAL = "visual"
    AUDITORY = "auditory"
    TACTILE = "tactile"
    VESTIBULAR = "vestibular"
    PROPRIOCEPTIVE = "proprioceptive"
    INTEROCEPTIVE = "interoceptive"
    OLFACTORY = "olfactory"
    GUSTATORY = "gustatory"


class SocialCognitionMode(Enum):
    OBSERVING = "observing"
    ANALYZING = "analyzing"
    PARTICIPATING = "participating"
    OVERWHELMED = "overwhelmed"
    RECOVERING = "recovering"


@dataclass
class SensoryProfile:
    user_id: str
    sensory_preferences: Dict[SensoryModality, Dict] = field(default_factory=dict)
    sensory_thresholds: Dict[SensoryModality, float] = field(default_factory=dict)
    calming_strategies: List[str] = field(default_factory=list)
    warning_signs: List[str] = field(default_factory=list)
    recovery_protocols: List[str] = field(default_factory=list)
    stim_preferences: List[str] = field(default_factory=list)
    environmental_needs: Dict[str, Any] = field(default_factory=dict)
    social_energy_capacity: float = 1.0
    last_updated: datetime = field(default_factory=datetime.now)


@dataclass
class SensoryMoment:
    timestamp: datetime
    user_id: str
    sensory_state: SensoryState
    modality_levels: Dict[SensoryModality, float] = field(default_factory=dict)
    overload_risk: float = 0.0
    shutdown_risk: float = 0.0
    current_stimming: List[str] = field(default_factory=list)
    environmental_factors: Dict[str, Any] = field(default_factory=dict)
    social_energy_level: float = 1.0
    regulation_needs: List[str] = field(default_factory=list)


@dataclass
class SocialCognitionState:
    timestamp: datetime
    user_id: str
    social_mode: SocialCognitionMode
    social_energy: float
    interaction_complexity: float
    emotional_recognition_accuracy: float
    social_script_usage: int
    nonverbal_processing_load: float
    social_battery_depletion_rate: float


class AutismSensoryTranscendenceSystem:
    """🌈 Revolutionary sensory processing and social cognition support system"""

    def __init__(self):
        self.sensory_profiles: Dict[str, SensoryProfile] = {}
        self.sensory_moments: Dict[str, List[SensoryMoment]] = {}
        self.social_cognition_states: Dict[str, List[SocialCognitionState]] = {}

        # Advanced AI systems
        self.sensory_predictor = SensoryPredictionAI()
        self.overload_prevention = OverloadPreventionSystem()
        self.calming_sequence_ai = CalmingSequenceAI()
        self.social_cognition_ai = SocialCognitionEnhancementAI()
        self.stim_optimization = StimOptimizationSystem()

        # Real-time monitoring
        self.environmental_monitor = EnvironmentalSensoryMonitor()
        self.social_interaction_analyzer = SocialInteractionAnalyzer()

        # Emergency systems
        self.meltdown_prevention = MeltdownPreventionProtocol()
        self.shutdown_recovery = ShutdownRecoverySystem()

    async def create_sensory_profile(
        self, user_id: str, profile_data: Dict
    ) -> SensoryProfile:
        """🎨 Create comprehensive sensory profile for user"""

        # Initialize sensory preferences for each modality
        sensory_preferences = {}
        sensory_thresholds = {}

        for modality in SensoryModality:
            modality_data = profile_data.get(modality.value, {})

            sensory_preferences[modality] = {
                "intensity_preference": modality_data.get("intensity", 0.5),
                "frequency_tolerance": modality_data.get("frequency", 0.5),
                "pattern_preference": modality_data.get("patterns", []),
                "trigger_items": modality_data.get("triggers", []),
                "soothing_items": modality_data.get("soothing", []),
            }

            # Set thresholds for overload detection
            sensory_thresholds[modality] = modality_data.get("threshold", 0.7)

        profile = SensoryProfile(
            user_id=user_id,
            sensory_preferences=sensory_preferences,
            sensory_thresholds=sensory_thresholds,
            calming_strategies=profile_data.get(
                "calming_strategies",
                [
                    "deep_breathing",
                    "weighted_blanket",
                    "fidget_tools",
                    "quiet_space",
                    "favorite_music",
                    "rocking_motion",
                ],
            ),
            warning_signs=profile_data.get(
                "warning_signs",
                [
                    "rapid_blinking",
                    "hand_flapping",
                    "verbal_stimming",
                    "withdrawal",
                    "repetitive_movements",
                    "voice_changes",
                ],
            ),
            recovery_protocols=profile_data.get(
                "recovery_protocols",
                [
                    "sensory_break",
                    "dim_environment",
                    "comfort_items",
                    "alone_time",
                    "favorite_stim",
                    "predictable_routine",
                ],
            ),
            stim_preferences=profile_data.get(
                "stim_preferences",
                [
                    "hand_flapping",
                    "rocking",
                    "spinning",
                    "fidgeting",
                    "vocal_stimming",
                    "tactile_seeking",
                    "visual_stimming",
                ],
            ),
            environmental_needs=profile_data.get("environmental_needs", {}),
            social_energy_capacity=profile_data.get("social_capacity", 1.0),
        )

        self.sensory_profiles[user_id] = profile
        return profile

    async def monitor_sensory_state(
        self, user_id: str, environmental_data: Dict, interaction_data: Dict
    ) -> SensoryMoment:
        """🔍 Real-time monitoring of user's sensory state"""

        profile = self.sensory_profiles.get(user_id)
        if not profile:
            # Create basic profile if none exists
            profile = await self.create_sensory_profile(user_id, {})

        # Analyze current sensory levels for each modality
        modality_levels = {}
        total_sensory_load = 0.0

        for modality in SensoryModality:
            level = await self._assess_modality_level(
                modality, environmental_data, interaction_data, profile
            )
            modality_levels[modality] = level
            total_sensory_load += level

        # Calculate overall sensory state
        average_load = total_sensory_load / len(SensoryModality)
        sensory_state = await self._determine_sensory_state(average_load, profile)

        # Assess risks
        overload_risk = await self._calculate_overload_risk(modality_levels, profile)
        shutdown_risk = await self._calculate_shutdown_risk(
            user_id, sensory_state, overload_risk
        )

        # Detect current stimming
        current_stimming = await self._detect_stimming_behavior(interaction_data)

        # Assess social energy
        social_energy = await self._assess_social_energy(user_id, interaction_data)

        # Determine regulation needs
        regulation_needs = await self._identify_regulation_needs(
            sensory_state, modality_levels, profile
        )

        sensory_moment = SensoryMoment(
            timestamp=datetime.now(),
            user_id=user_id,
            sensory_state=sensory_state,
            modality_levels=modality_levels,
            overload_risk=overload_risk,
            shutdown_risk=shutdown_risk,
            current_stimming=current_stimming,
            environmental_factors=environmental_data,
            social_energy_level=social_energy,
            regulation_needs=regulation_needs,
        )

        # Store for pattern analysis
        if user_id not in self.sensory_moments:
            self.sensory_moments[user_id] = []
        self.sensory_moments[user_id].append(sensory_moment)

        # Trigger interventions if needed
        await self._trigger_sensory_interventions(user_id, sensory_moment)

        return sensory_moment

    async def _assess_modality_level(
        self,
        modality: SensoryModality,
        environmental_data: Dict,
        interaction_data: Dict,
        profile: SensoryProfile,
    ) -> float:
        """📊 Assess sensory level for specific modality"""

        modality_assessors = {
            SensoryModality.VISUAL: self._assess_visual_load,
            SensoryModality.AUDITORY: self._assess_auditory_load,
            SensoryModality.TACTILE: self._assess_tactile_load,
            SensoryModality.VESTIBULAR: self._assess_vestibular_load,
            SensoryModality.PROPRIOCEPTIVE: self._assess_proprioceptive_load,
            SensoryModality.INTEROCEPTIVE: self._assess_interoceptive_load,
            SensoryModality.OLFACTORY: self._assess_olfactory_load,
            SensoryModality.GUSTATORY: self._assess_gustatory_load,
        }

        assessor = modality_assessors.get(modality, self._assess_default_load)
        return await assessor(environmental_data, interaction_data, profile)

    async def _assess_visual_load(
        self, env_data: Dict, interaction_data: Dict, profile: SensoryProfile
    ) -> float:
        """👁️ Assess visual sensory load"""

        visual_factors = {
            "screen_brightness": env_data.get("screen_brightness", 0.5),
            "color_saturation": env_data.get("color_saturation", 0.5),
            "movement_frequency": env_data.get("animations_per_minute", 0),
            "contrast_ratio": env_data.get("contrast_ratio", 1.0),
            "flashing_elements": env_data.get("flashing_count", 0),
            "visual_complexity": interaction_data.get("elements_on_screen", 10),
        }

        # Calculate visual load based on user's visual preferences
        visual_prefs = profile.sensory_preferences.get(SensoryModality.VISUAL, {})
        preferred_intensity = visual_prefs.get("intensity_preference", 0.5)

        # Higher load if current intensity differs significantly from preference
        intensity_diff = abs(visual_factors["screen_brightness"] - preferred_intensity)
        base_load = intensity_diff

        # Add load from other factors
        if visual_factors["movement_frequency"] > 5:  # Too much movement
            base_load += 0.3

        if (
            visual_factors["flashing_elements"] > 0
        ):  # Any flashing is potentially triggering
            base_load += 0.5

        if visual_factors["visual_complexity"] > 20:  # Too many elements
            base_load += 0.2

        return min(base_load, 1.0)

    async def _assess_auditory_load(
        self, env_data: Dict, interaction_data: Dict, profile: SensoryProfile
    ) -> float:
        """🔊 Assess auditory sensory load"""

        auditory_factors = {
            "volume_level": env_data.get("audio_volume", 0.5),
            "frequency_range": env_data.get("frequency_spectrum", []),
            "sudden_sounds": env_data.get("sudden_audio_events", 0),
            "background_noise": env_data.get("background_noise_level", 0.3),
            "audio_complexity": env_data.get("simultaneous_audio_sources", 1),
        }

        auditory_prefs = profile.sensory_preferences.get(SensoryModality.AUDITORY, {})
        preferred_volume = auditory_prefs.get("intensity_preference", 0.5)

        # Calculate load
        volume_diff = abs(auditory_factors["volume_level"] - preferred_volume)
        base_load = volume_diff

        # Sudden sounds are particularly challenging
        base_load += auditory_factors["sudden_sounds"] * 0.2

        # Multiple audio sources increase complexity
        if auditory_factors["audio_complexity"] > 2:
            base_load += 0.3

        return min(base_load, 1.0)

    async def provide_sensory_regulation(
        self, user_id: str, sensory_moment: SensoryMoment
    ) -> Dict:
        """🌊 Provide personalized sensory regulation support"""

        profile = self.sensory_profiles[user_id]
        regulation_plan = {
            "immediate_actions": [],
            "environmental_adjustments": {},
            "calming_sequences": [],
            "stim_recommendations": [],
            "recovery_timeline": None,
        }

        # Determine intervention level
        if sensory_moment.sensory_state in [
            SensoryState.OVERLOADED,
            SensoryState.SHUTDOWN_RISK,
        ]:
            # Emergency regulation protocol
            regulation_plan = await self._emergency_sensory_regulation(
                user_id, sensory_moment
            )

        elif sensory_moment.sensory_state == SensoryState.OVERWHELMED:
            # Active regulation protocol
            regulation_plan = await self._active_sensory_regulation(
                user_id, sensory_moment
            )

        elif sensory_moment.sensory_state == SensoryState.ELEVATED:
            # Preventive regulation protocol
            regulation_plan = await self._preventive_sensory_regulation(
                user_id, sensory_moment
            )

        else:
            # Maintenance protocol
            regulation_plan = await self._maintenance_sensory_regulation(
                user_id, sensory_moment
            )

        # Apply regulation plan
        await self._apply_regulation_plan(user_id, regulation_plan)

        return regulation_plan

    async def _emergency_sensory_regulation(
        self, user_id: str, sensory_moment: SensoryMoment
    ) -> Dict:
        """🆘 Emergency sensory regulation for overload/shutdown risk"""

        profile = self.sensory_profiles[user_id]

        return {
            "immediate_actions": [
                "🚨 IMMEDIATE SENSORY BREAK NEEDED",
                "🔇 Reduce all sensory input immediately",
                "😌 Activate calming environment",
                "🤗 Provide comfort items",
                "⏸️ Pause all non-essential activities",
            ],
            "environmental_adjustments": {
                "lighting": "dim_to_minimum",
                "audio": "silence_or_calming_sounds",
                "visual_complexity": "minimal_interface",
                "notifications": "emergency_only",
                "interface_speed": "slow_gentle_transitions",
            },
            "calming_sequences": await self.calming_sequence_ai.generate_emergency_sequence(
                user_id, sensory_moment
            ),
            "stim_recommendations": profile.stim_preferences[
                :3
            ],  # Top 3 preferred stims
            "recovery_timeline": "15-45 minutes estimated",
        }

    async def enhance_social_cognition(
        self, user_id: str, social_context: Dict
    ) -> Dict:
        """🤝 Enhance social cognition and interaction support"""

        # Analyze current social situation
        social_analysis = await self.social_cognition_ai.analyze_social_context(
            user_id, social_context
        )

        # Determine social support needs
        support_needs = await self._assess_social_support_needs(
            user_id, social_analysis
        )

        enhancement_plan = {
            "emotion_recognition_support": [],
            "social_scripts": [],
            "nonverbal_communication_aids": [],
            "social_energy_management": {},
            "interaction_guidance": [],
        }

        # Emotion recognition support
        if support_needs.get("emotion_recognition", False):
            enhancement_plan["emotion_recognition_support"] = [
                "🎭 Facial expression guide activated",
                "💭 Emotion context clues provided",
                "📊 Social signal interpretation",
                "🎯 Intent clarification assistance",
            ]

        # Social scripts for common situations
        if support_needs.get("conversation_support", False):
            scripts = await self._generate_social_scripts(social_context)
            enhancement_plan["social_scripts"] = scripts

        # Nonverbal communication aids
        if support_needs.get("nonverbal_support", False):
            enhancement_plan["nonverbal_communication_aids"] = [
                "👋 Gesture interpretation guide",
                "👀 Eye contact alternatives",
                "🗣️ Tone of voice indicators",
                "📍 Personal space guidance",
            ]

        # Social energy management
        social_energy = await self._assess_social_energy(user_id, social_context)
        enhancement_plan["social_energy_management"] = {
            "current_level": social_energy,
            "depletion_rate": social_analysis.get("complexity_level", 0.5),
            "recharge_recommendations": await self._get_social_recharge_strategies(
                user_id
            ),
            "interaction_time_limit": await self._calculate_safe_interaction_duration(
                user_id, social_energy
            ),
        }

        # Real-time interaction guidance
        enhancement_plan["interaction_guidance"] = [
            "💬 Conversation topic suggestions",
            "⏱️ Interaction timing guidance",
            "🛡️ Social boundary support",
            "✨ Strength-based interaction tips",
        ]

        return enhancement_plan

    async def create_predictive_calming_sequence(
        self, user_id: str, trigger_context: Dict
    ) -> Dict:
        """🌊 Create AI-generated calming sequence based on user profile and current state"""

        profile = self.sensory_profiles[user_id]

        # Analyze trigger context to customize sequence
        trigger_analysis = await self._analyze_trigger_context(trigger_context)

        # Generate personalized calming sequence
        calming_sequence = await self.calming_sequence_ai.generate_sequence(
            profile, trigger_analysis
        )

        # Optimize sequence timing and intensity
        optimized_sequence = await self._optimize_calming_sequence(
            user_id, calming_sequence, trigger_analysis
        )

        return {
            "sequence_id": f"calm_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "estimated_duration": optimized_sequence["duration"],
            "steps": optimized_sequence["steps"],
            "effectiveness_prediction": optimized_sequence["predicted_effectiveness"],
            "environmental_requirements": optimized_sequence["environment_needs"],
            "stim_integration": optimized_sequence["stim_activities"],
            "progress_indicators": optimized_sequence["progress_markers"],
        }


class SensoryPredictionAI:
    """🔮 AI system for predicting sensory overload and shutdown"""

    async def predict_overload_risk(
        self, user_id: str, current_state: SensoryMoment, upcoming_events: List[Dict]
    ) -> Dict:
        """Predict likelihood of sensory overload"""

        # Analyze current trajectory
        risk_factors = {
            "current_load": current_state.overload_risk,
            "recent_escalation": await self._assess_recent_escalation(user_id),
            "upcoming_stressors": await self._assess_upcoming_stressors(
                upcoming_events
            ),
            "regulation_capacity": await self._assess_regulation_capacity(user_id),
            "social_energy_depletion": 1.0 - current_state.social_energy_level,
        }

        # Calculate prediction
        base_risk = sum(risk_factors.values()) / len(risk_factors)

        # Adjust based on user patterns
        pattern_adjustment = await self._get_pattern_adjustment(user_id, current_state)
        final_risk = min(base_risk + pattern_adjustment, 1.0)

        return {
            "overload_risk": final_risk,
            "risk_factors": risk_factors,
            "time_to_potential_overload": await self._estimate_time_to_overload(
                final_risk
            ),
            "prevention_strategies": await self._recommend_prevention_strategies(
                user_id, risk_factors
            ),
            "safe_activity_duration": await self._calculate_safe_duration(final_risk),
        }


class CalmingSequenceAI:
    """🌊 AI system for generating personalized calming sequences"""

    async def generate_emergency_sequence(
        self, user_id: str, sensory_moment: SensoryMoment
    ) -> List[Dict]:
        """Generate emergency calming sequence for crisis situations"""

        return [
            {
                "step": 1,
                "action": "immediate_sensory_reduction",
                "description": "🔇 Reduce all sensory input immediately",
                "duration": "immediate",
                "guidance": "Lower lights, reduce sounds, minimize visual complexity",
            },
            {
                "step": 2,
                "action": "breathing_regulation",
                "description": "🫁 Gentle breathing guidance",
                "duration": "2-3 minutes",
                "guidance": "Slow, deep breaths - in for 4, hold for 4, out for 6",
            },
            {
                "step": 3,
                "action": "comfort_item_access",
                "description": "🤗 Access preferred comfort items",
                "duration": "ongoing",
                "guidance": "Weighted blanket, fidget tools, or preferred stim activities",
            },
            {
                "step": 4,
                "action": "grounding_technique",
                "description": "🌍 Sensory grounding",
                "duration": "5-10 minutes",
                "guidance": "5-4-3-2-1 technique adapted for sensory preferences",
            },
            {
                "step": 5,
                "action": "gentle_recovery",
                "description": "✨ Gradual return to baseline",
                "duration": "15-30 minutes",
                "guidance": "Slowly reintroduce preferred sensory experiences",
            },
        ]


class SocialCognitionEnhancementAI:
    """🤝 AI system for enhancing social cognition and interaction"""

    async def analyze_social_context(self, user_id: str, social_context: Dict) -> Dict:
        """Analyze social situation and provide enhancement recommendations"""

        context_analysis = {
            "interaction_type": social_context.get("type", "general"),
            "participant_count": social_context.get("participants", 1),
            "formality_level": social_context.get("formality", "casual"),
            "emotional_intensity": social_context.get("emotional_level", 0.5),
            "nonverbal_complexity": social_context.get("nonverbal_cues", 0.5),
            "topic_familiarity": social_context.get("topic_knowledge", 0.5),
        }

        # Calculate complexity score
        complexity_factors = [
            context_analysis["participant_count"] / 10,  # More people = more complex
            context_analysis["emotional_intensity"],
            context_analysis["nonverbal_complexity"],
            1.0 - context_analysis["topic_familiarity"],  # Less familiar = more complex
        ]

        complexity_score = sum(complexity_factors) / len(complexity_factors)

        return {
            **context_analysis,
            "complexity_level": complexity_score,
            "cognitive_load_prediction": complexity_score * 0.8,
            "recommended_duration": max(30 - (complexity_score * 20), 10),  # Minutes
            "support_recommendations": await self._generate_support_recommendations(
                context_analysis
            ),
        }


# Example usage and testing
async def test_autism_sensory_transcendence():
    """Test the autism sensory transcendence system"""

    system = AutismSensoryTranscendenceSystem()

    # Create sensory profile
    profile_data = {
        "visual": {
            "intensity": 0.3,  # Prefers low visual intensity
            "triggers": ["flashing_lights", "high_contrast"],
            "soothing": ["soft_colors", "dim_lighting"],
        },
        "auditory": {
            "intensity": 0.4,  # Sensitive to loud sounds
            "triggers": ["sudden_noises", "multiple_voices"],
            "soothing": ["white_noise", "classical_music"],
        },
        "calming_strategies": ["weighted_blanket", "hand_flapping", "quiet_space"],
        "stim_preferences": ["hand_flapping", "fidget_spinner", "soft_textures"],
    }

    profile = await system.create_sensory_profile("user123", profile_data)
    print(f"Created sensory profile for {profile.user_id}")

    # Simulate environmental data
    environmental_data = {
        "screen_brightness": 0.8,  # Too bright for this user
        "audio_volume": 0.6,  # A bit too loud
        "animations_per_minute": 15,  # Lots of movement
        "background_noise_level": 0.4,
    }

    interaction_data = {
        "elements_on_screen": 25,  # Visually complex
        "social_interaction_active": True,
        "task_complexity": 0.7,
    }

    # Monitor sensory state
    sensory_moment = await system.monitor_sensory_state(
        "user123", environmental_data, interaction_data
    )

    print(f"Sensory state: {sensory_moment.sensory_state}")
    print(f"Overload risk: {sensory_moment.overload_risk:.2f}")
    print(f"Regulation needs: {sensory_moment.regulation_needs}")

    # Provide regulation if needed
    if sensory_moment.overload_risk > 0.5:
        regulation_plan = await system.provide_sensory_regulation(
            "user123", sensory_moment
        )
        print(f"Regulation plan: {regulation_plan['immediate_actions']}")


if __name__ == "__main__":
    asyncio.run(test_autism_sensory_transcendence())

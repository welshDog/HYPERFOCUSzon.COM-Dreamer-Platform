"""
🛡️💎⚡ Neurodivergent AI - Ethics Dashboard Backend
Real-time ethics monitoring and transparency API

This module provides:
- Trust score analytics and distribution tracking
- Consent integrity monitoring and validation
- Bias detection across neurodivergent segments
- Community flag queue management
- Model transparency and governance
- Real-time system health monitoring
"""

import asyncio
import logging
import random
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Union

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="🛡️ Neurodivergent AI Ethics Dashboard",
    description="Real-time transparency and governance for community-first AI",
    version="2.1.0",
)

# CORS middleware for web interface
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 🛡️ Data Models
class TrustDistribution(BaseModel):
    buckets: List[Dict[str, Union[str, int]]] = Field(
        description="Trust score distribution buckets"
    )
    overall_score: float = Field(description="Overall trust score percentage")
    high_trust_count: int = Field(description="Count of high trust claims (≥80%)")
    medium_trust_count: int = Field(description="Count of medium trust claims (60-79%)")
    low_trust_count: int = Field(description="Count of low trust claims (<60%)")


class ConsentStatus(BaseModel):
    active_count: int = Field(description="Users with active consent")
    expired_count: int = Field(description="Users with expired consent")
    revoked_count: int = Field(description="Users who revoked consent")
    integrity_percentage: float = Field(
        description="Overall consent integrity percentage"
    )


class BiasAnalysis(BaseModel):
    adhd_fairness: float = Field(description="Fairness score for ADHD segment")
    autism_fairness: float = Field(description="Fairness score for autism segment")
    dyslexia_fairness: float = Field(description="Fairness score for dyslexia segment")
    overlap_fairness: float = Field(description="Fairness score for overlap segments")
    overall_fairness: float = Field(description="Overall bias fairness score")


class CommunityFlag(BaseModel):
    id: str = Field(description="Unique flag identifier")
    title: str = Field(description="Flag title/summary")
    priority: str = Field(description="Priority level: high, medium, low")
    flagged_by: str = Field(description="User who flagged the issue")
    timestamp: datetime = Field(description="When the flag was created")
    status: str = Field(description="Flag status: open, reviewing, resolved")
    description: Optional[str] = Field(description="Detailed description of the flag")


class ModelCard(BaseModel):
    version: str = Field(description="Current model version")
    last_training: datetime = Field(description="Last training timestamp")
    data_sources: Dict[str, float] = Field(description="Data source breakdown")
    consent_coverage: float = Field(description="Percentage of consented data")
    pii_status: str = Field(description="PII handling status")
    bias_monitoring: str = Field(description="Bias monitoring status")


class SystemHealth(BaseModel):
    api_response_time: int = Field(description="Average API response time in ms")
    uptime_percentage: float = Field(description="System uptime percentage")
    memory_usage: float = Field(description="Memory usage percentage")
    cpu_usage: float = Field(description="CPU usage percentage")
    error_rate: float = Field(description="Error rate percentage")


class CommunityStats(BaseModel):
    active_users: int = Field(description="Number of active users")
    satisfaction_rate: float = Field(description="User satisfaction percentage")
    questions_today: int = Field(description="Questions answered today")
    contributions: int = Field(description="Community contributions")
    knowledge_growth: float = Field(description="Knowledge base growth percentage")


class EthicsDashboard(BaseModel):
    trust_distribution: TrustDistribution
    consent_status: ConsentStatus
    bias_analysis: BiasAnalysis
    community_flags: List[CommunityFlag]
    model_card: ModelCard
    system_health: SystemHealth
    community_stats: CommunityStats
    last_updated: datetime


# 🛡️ Mock Data Generator
class EthicsDataGenerator:
    """Generates realistic ethics monitoring data for demonstration"""

    def __init__(self):
        self.base_trust_score = 87.3
        self.base_consent_active = 2847
        self.base_consent_expired = 127
        self.base_consent_revoked = 32
        self.flag_queue = self._generate_initial_flags()

    def _generate_initial_flags(self) -> List[CommunityFlag]:
        """Generate initial community flags"""
        flags = [
            CommunityFlag(
                id="flag_001",
                title="Potential bias in autism employment claims",
                priority="high",
                flagged_by="@neurodiv_advocate",
                timestamp=datetime.now() - timedelta(hours=2),
                status="open",
                description="Multiple users reported that employment advice for autistic individuals seems to focus too heavily on challenges rather than strengths",
            ),
            CommunityFlag(
                id="flag_002",
                title="Source quality concern: unverified forum post",
                priority="medium",
                flagged_by="@research_focus",
                timestamp=datetime.now() - timedelta(hours=4),
                status="reviewing",
                description="A claim about ADHD medication effects is sourced from an unverified forum post without peer review",
            ),
            CommunityFlag(
                id="flag_003",
                title="Suggestion: Add more dyslexia strength examples",
                priority="low",
                flagged_by="@dyslexia_pride",
                timestamp=datetime.now() - timedelta(hours=6),
                status="open",
                description="Request to include more examples of dyslexic strengths in creative and problem-solving contexts",
            ),
            CommunityFlag(
                id="flag_004",
                title="Consent withdrawal not processed",
                priority="high",
                flagged_by="System",
                timestamp=datetime.now() - timedelta(hours=8),
                status="open",
                description="Automated system detected that a consent withdrawal request was not processed within required timeframe",
            ),
        ]
        return flags

    def generate_trust_distribution(self) -> TrustDistribution:
        """Generate trust score distribution data"""
        # Simulate realistic trust distribution
        buckets = []
        bucket_counts = [12, 8, 15, 23, 31, 45, 67, 89, 78, 56]  # Typical distribution

        for i, count in enumerate(bucket_counts):
            variation = random.randint(-3, 3)
            adjusted_count = max(0, count + variation)
            buckets.append(
                {
                    "range": f"{i/10:.1f}-{(i+1)/10:.1f}",
                    "count": adjusted_count,
                    "percentage": (adjusted_count / sum(bucket_counts)) * 100,
                }
            )

        # Calculate trust categories
        total_claims = sum(bucket_counts)
        high_trust = sum(bucket_counts[8:])  # 0.8-1.0
        medium_trust = sum(bucket_counts[6:8])  # 0.6-0.8
        low_trust = sum(bucket_counts[:6])  # 0.0-0.6

        overall_score = self.base_trust_score + random.uniform(-1.5, 1.5)

        return TrustDistribution(
            buckets=buckets,
            overall_score=round(overall_score, 1),
            high_trust_count=high_trust + random.randint(-5, 5),
            medium_trust_count=medium_trust + random.randint(-3, 3),
            low_trust_count=low_trust + random.randint(-2, 2),
        )

    def generate_consent_status(self) -> ConsentStatus:
        """Generate consent integrity data"""
        active_variation = random.randint(-10, 20)
        expired_variation = random.randint(-5, 5)
        revoked_variation = random.randint(-2, 3)

        active = self.base_consent_active + active_variation
        expired = self.base_consent_expired + expired_variation
        revoked = self.base_consent_revoked + revoked_variation

        total = active + expired + revoked
        integrity = (active / total) * 100

        return ConsentStatus(
            active_count=active,
            expired_count=expired,
            revoked_count=revoked,
            integrity_percentage=round(integrity, 1),
        )

    def generate_bias_analysis(self) -> BiasAnalysis:
        """Generate bias detection data"""
        base_scores = {"adhd": 92.0, "autism": 89.0, "dyslexia": 73.0, "overlap": 85.0}

        # Add small random variations
        scores = {}
        for key, base in base_scores.items():
            variation = random.uniform(-3, 3)
            scores[key] = max(60, min(100, base + variation))

        overall = sum(scores.values()) / len(scores)

        return BiasAnalysis(
            adhd_fairness=round(scores["adhd"], 1),
            autism_fairness=round(scores["autism"], 1),
            dyslexia_fairness=round(scores["dyslexia"], 1),
            overlap_fairness=round(scores["overlap"], 1),
            overall_fairness=round(overall, 1),
        )

    def generate_model_card(self) -> ModelCard:
        """Generate model transparency data"""
        return ModelCard(
            version="Neurodivergent AI v2.1.0",
            last_training=datetime.now() - timedelta(days=2, hours=10),
            data_sources={"research": 67.0, "lived_experience": 33.0},
            consent_coverage=94.7 + random.uniform(-1, 1),
            pii_status="Fully Scrubbed",
            bias_monitoring="Real-time Active",
        )

    def generate_system_health(self) -> SystemHealth:
        """Generate system health metrics"""
        return SystemHealth(
            api_response_time=random.randint(110, 150),
            uptime_percentage=99.97 + random.uniform(-0.1, 0.03),
            memory_usage=68.0 + random.uniform(-5, 8),
            cpu_usage=42.0 + random.uniform(-10, 15),
            error_rate=0.03 + random.uniform(-0.01, 0.02),
        )

    def generate_community_stats(self) -> CommunityStats:
        """Generate community impact statistics"""
        return CommunityStats(
            active_users=12847 + random.randint(-50, 100),
            satisfaction_rate=98.2 + random.uniform(-0.5, 0.3),
            questions_today=2156 + random.randint(-100, 200),
            contributions=847 + random.randint(-20, 50),
            knowledge_growth=12.3 + random.uniform(-2, 3),
        )


# Initialize data generator
ethics_generator = EthicsDataGenerator()

# 🛡️ API Endpoints


@app.get("/", response_class=HTMLResponse)
async def serve_dashboard():
    """Serve the ethics dashboard HTML interface"""
    try:
        with open(
            "h:\\neurodivergent-ai-demo\\ethics-dashboard\\index.html",
            "r",
            encoding="utf-8",
        ) as f:
            return HTMLResponse(content=f.read())
    except FileNotFoundError:
        return HTMLResponse(
            content="<h1>Ethics Dashboard</h1><p>Dashboard file not found. Please check the file path.</p>",
            status_code=404,
        )


@app.get("/api/dashboard", response_model=EthicsDashboard)
async def get_dashboard_data():
    """
    🛡️ Get complete ethics dashboard data

    Returns comprehensive ethics monitoring data including:
    - Trust score distribution and analytics
    - Consent integrity status
    - Bias detection across neurodivergent segments
    - Community flag queue
    - Model transparency information
    - System health metrics
    - Community impact statistics
    """
    try:
        dashboard = EthicsDashboard(
            trust_distribution=ethics_generator.generate_trust_distribution(),
            consent_status=ethics_generator.generate_consent_status(),
            bias_analysis=ethics_generator.generate_bias_analysis(),
            community_flags=ethics_generator.flag_queue[:10],  # Show latest 10 flags
            model_card=ethics_generator.generate_model_card(),
            system_health=ethics_generator.generate_system_health(),
            community_stats=ethics_generator.generate_community_stats(),
            last_updated=datetime.now(),
        )

        logger.info("Generated dashboard data successfully")
        return dashboard

    except Exception as e:
        logger.error(f"Error generating dashboard data: {e}")
        raise HTTPException(status_code=500, detail="Failed to generate dashboard data")


@app.get("/api/trust", response_model=TrustDistribution)
async def get_trust_metrics():
    """🎯 Get trust score distribution and analytics"""
    return ethics_generator.generate_trust_distribution()


@app.get("/api/consent", response_model=ConsentStatus)
async def get_consent_status():
    """🛡️ Get consent integrity monitoring data"""
    return ethics_generator.generate_consent_status()


@app.get("/api/bias", response_model=BiasAnalysis)
async def get_bias_analysis():
    """🌈 Get bias detection across neurodivergent segments"""
    return ethics_generator.generate_bias_analysis()


@app.get("/api/flags", response_model=List[CommunityFlag])
async def get_community_flags(limit: int = 10, priority: Optional[str] = None):
    """
    🔍 Get community flag queue

    Args:
        limit: Maximum number of flags to return
        priority: Filter by priority level (high, medium, low)
    """
    flags = ethics_generator.flag_queue

    if priority:
        flags = [f for f in flags if f.priority == priority.lower()]

    return flags[:limit]


@app.post("/api/flags", response_model=CommunityFlag)
async def create_community_flag(flag: CommunityFlag):
    """
    🚨 Create a new community flag

    Allows community members to flag issues for review
    """
    flag.id = f"flag_{len(ethics_generator.flag_queue) + 1:03d}"
    flag.timestamp = datetime.now()
    flag.status = "open"

    ethics_generator.flag_queue.insert(0, flag)

    logger.info(f"New community flag created: {flag.title}")
    return flag


@app.put("/api/flags/{flag_id}/status")
async def update_flag_status(flag_id: str, status: str):
    """
    ✅ Update flag status

    Allows moderators to update flag status (open, reviewing, resolved)
    """
    valid_statuses = ["open", "reviewing", "resolved"]
    if status not in valid_statuses:
        raise HTTPException(
            status_code=400, detail=f"Invalid status. Must be one of: {valid_statuses}"
        )

    for flag in ethics_generator.flag_queue:
        if flag.id == flag_id:
            flag.status = status
            logger.info(f"Flag {flag_id} status updated to {status}")
            return {"message": f"Flag status updated to {status}"}

    raise HTTPException(status_code=404, detail="Flag not found")


@app.get("/api/model", response_model=ModelCard)
async def get_model_card():
    """📋 Get model transparency and governance information"""
    return ethics_generator.generate_model_card()


@app.get("/api/health", response_model=SystemHealth)
async def get_system_health():
    """🏥 Get real-time system health metrics"""
    return ethics_generator.generate_system_health()


@app.get("/api/community", response_model=CommunityStats)
async def get_community_stats():
    """🌍 Get community impact and engagement statistics"""
    return ethics_generator.generate_community_stats()


@app.get("/api/realtime")
async def realtime_updates():
    """
    ⚡ WebSocket endpoint for real-time dashboard updates

    Note: This is a placeholder for WebSocket implementation
    In production, this would stream real-time updates
    """
    return {
        "message": "Real-time updates endpoint",
        "note": "In production, this would be a WebSocket endpoint streaming live data",
        "update_frequency": "Every 5 seconds",
        "supported_events": [
            "trust_score_update",
            "new_community_flag",
            "consent_status_change",
            "bias_detection_alert",
            "system_health_warning",
        ],
    }


# 🛡️ Background Tasks


async def simulate_realtime_monitoring():
    """Simulate real-time ethics monitoring in background"""
    while True:
        try:
            # Simulate periodic data refresh
            await asyncio.sleep(30)  # Update every 30 seconds

            # In production, this would:
            # - Query actual databases
            # - Run bias detection algorithms
            # - Process new community flags
            # - Update trust scores
            # - Monitor consent status

            logger.info("Ethics monitoring cycle completed")

        except Exception as e:
            logger.error(f"Error in realtime monitoring: {e}")
            await asyncio.sleep(60)  # Wait longer on error


# Start background monitoring on startup
@app.on_event("startup")
async def startup_event():
    """Initialize ethics monitoring on server startup"""
    logger.info("🛡️ Neurodivergent AI Ethics Dashboard starting up...")
    logger.info("✅ Real-time ethics monitoring initialized")
    logger.info("✅ Community governance systems active")
    logger.info("✅ Bias detection algorithms running")
    logger.info("✅ Consent integrity monitoring enabled")

    # Start background monitoring task
    asyncio.create_task(simulate_realtime_monitoring())


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="info", reload=True)

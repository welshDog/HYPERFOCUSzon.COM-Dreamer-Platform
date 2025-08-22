#!/usr/bin/env python3
"""
🧠💎⚡ NEURODIVERGENT AI - MOCK SERVER ⚡💎🧠
================================================================

HYPERFOCUS ZONE EMPIRE - Mock API Server for Demo Client Testing
Provides realistic responses for demonstration purposes

Start server: python server.py
Access API: http://localhost:8000

================================================================
"""

import random
from datetime import datetime
from typing import Any, Dict, Optional

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title="🧠 Neurodivergent AI - Mock Server",
    description="Mock API server for neurodivergent-first AI demo",
    version="1.0.0",
)

# Enable CORS for web interface
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QuestionRequest(BaseModel):
    question: str
    mode: str = "balanced"
    user_id: str = "demo-user"
    timestamp: Optional[str] = None


class NeurodivergentAIMock:
    """🧠 Mock implementation of neurodivergent AI system"""

    def __init__(self):
        self.mock_responses = {
            "creativity": {
                "science": {
                    "verdict": "✅ Likely True",
                    "trust": 0.87,
                    "explanation": "Research shows that ADHD individuals often demonstrate enhanced creativity through divergent thinking, cognitive flexibility, and the ability to make novel connections between concepts.",
                    "sources": [
                        "https://pubmed.ncbi.nlm.nih.gov/creativity-adhd-2023",
                        "https://neuropsychology.org/adhd-creative-cognition",
                        "https://journals.creativity.org/divergent-thinking-study",
                    ],
                    "tags": {
                        "strengths": [
                            "creativity",
                            "divergent thinking",
                            "cognitive flexibility",
                        ],
                        "overlaps": ["ADHD+creativity"],
                        "struggles": [],
                    },
                },
                "lived": {
                    "verdict": "🟨 Mixed/Contextual",
                    "trust": 0.73,
                    "explanation": "Community members report that hyperfocus can lead to intense creative sessions, but executive function challenges may interfere with completing creative projects. Environment and support systems play crucial roles.",
                    "sources": [
                        "https://additudemag.com/creative-adhd-minds",
                        "https://reddit.com/r/ADHD/creativity-experiences",
                        "https://adhdwomen.com/creative-struggles-successes",
                    ],
                    "tags": {
                        "strengths": [
                            "hyperfocus",
                            "creative ideation",
                            "out-of-the-box thinking",
                        ],
                        "overlaps": ["ADHD+creativity"],
                        "struggles": ["project completion", "executive function"],
                    },
                },
            },
            "sensory": {
                "science": {
                    "verdict": "✅ Likely True",
                    "trust": 0.91,
                    "explanation": "Sensory processing differences are well-documented in autism and ADHD, involving both hypersensitivity and hyposensitivity to various stimuli. Evidence-based interventions include environmental modifications and sensory tools.",
                    "sources": [
                        "https://pubmed.ncbi.nlm.nih.gov/sensory-processing-autism-2024",
                        "https://occupationaltherapy.org/sensory-interventions",
                        "https://autismresearch.org/sensory-profiles-study",
                    ],
                    "tags": {
                        "strengths": ["sensory awareness", "pattern recognition"],
                        "overlaps": ["Autism+ADHD", "sensory processing"],
                        "struggles": ["sensory overload", "hypersensitivity"],
                    },
                },
                "lived": {
                    "verdict": "✅ Likely True",
                    "trust": 0.89,
                    "explanation": "Community strategies include noise-canceling headphones, fidget tools, weighted blankets, and creating sensory-friendly environments. Many report that understanding their sensory needs is transformative.",
                    "sources": [
                        "https://autismcommunity.org/sensory-strategies",
                        "https://sensorytools.com/user-reviews",
                        "https://neurodivergent-spaces.org/coping-techniques",
                    ],
                    "tags": {
                        "strengths": ["self-awareness", "adaptation strategies"],
                        "overlaps": ["Autism+ADHD", "sensory processing"],
                        "struggles": ["overwhelm", "environmental challenges"],
                    },
                },
            },
            "overlap": {
                "science": {
                    "verdict": "✅ Likely True",
                    "trust": 0.85,
                    "explanation": "Research indicates significant overlap between ADHD and autism, with shared traits in executive function, sensory processing, and social communication. Co-occurrence rates are estimated at 20-50%.",
                    "sources": [
                        "https://pubmed.ncbi.nlm.nih.gov/adhd-autism-overlap-2024",
                        "https://neurodevelopment.org/comorbidity-study",
                        "https://clinicalpsychology.org/dual-diagnosis-research",
                    ],
                    "tags": {
                        "strengths": [
                            "pattern recognition",
                            "attention to detail",
                            "systems thinking",
                        ],
                        "overlaps": ["ADHD+Autism"],
                        "struggles": ["executive function", "social communication"],
                    },
                },
                "lived": {
                    "verdict": "✅ Likely True",
                    "trust": 0.82,
                    "explanation": "Many individuals identify with traits from both ADHD and autism, describing experiences of hyperfocus alongside social communication differences, or hyperactivity with sensory sensitivities.",
                    "sources": [
                        "https://actuallyautistic.org/adhd-autism-experiences",
                        "https://adhd-autism-community.org/stories",
                        "https://neurodivergent-voices.com/overlap-narratives",
                    ],
                    "tags": {
                        "strengths": [
                            "self-advocacy",
                            "community building",
                            "unique perspectives",
                        ],
                        "overlaps": ["ADHD+Autism"],
                        "struggles": ["diagnosis challenges", "identity questions"],
                    },
                },
            },
        }

    def analyze_question(self, question: str) -> str:
        """🔍 Analyze question to determine response category"""
        q_lower = question.lower()

        if any(
            word in q_lower
            for word in ["creat", "innovat", "art", "music", "design", "ideas"]
        ):
            return "creativity"
        elif any(
            word in q_lower
            for word in ["sensory", "overwhelm", "noise", "texture", "stimul", "sound"]
        ):
            return "sensory"
        elif any(
            word in q_lower
            for word in [
                "overlap",
                "combin",
                "both",
                "adhd and autism",
                "autism and adhd",
            ]
        ):
            return "overlap"
        else:
            # Default to overlap for general questions
            return "overlap"

    def get_response(self, question: str, mode: str) -> Dict[str, Any]:
        """🧠 Generate mock AI response"""

        category = self.analyze_question(question)

        # Get base response for category and mode
        if category in self.mock_responses and mode in ["science", "lived"]:
            response_data = self.mock_responses[category][mode].copy()
        elif category in self.mock_responses:
            # Balanced mode - blend science and lived
            science_data = self.mock_responses[category]["science"]
            lived_data = self.mock_responses[category]["lived"]

            response_data = {
                "verdict": "🟨 Mixed/Contextual",
                "trust": (science_data["trust"] + lived_data["trust"]) / 2,
                "explanation": f"Research perspective: {science_data['explanation'][:100]}... Community perspective: {lived_data['explanation'][:100]}...",
                "sources": science_data["sources"][:2] + lived_data["sources"][:2],
                "tags": {
                    "strengths": list(
                        set(
                            science_data["tags"]["strengths"]
                            + lived_data["tags"]["strengths"]
                        )
                    ),
                    "overlaps": list(
                        set(
                            science_data["tags"]["overlaps"]
                            + lived_data["tags"]["overlaps"]
                        )
                    ),
                    "struggles": list(
                        set(
                            science_data["tags"]["struggles"]
                            + lived_data["tags"]["struggles"]
                        )
                    ),
                },
            }
        else:
            # Fallback response
            response_data = {
                "verdict": "⚠️ Unclear",
                "trust": 0.45,
                "explanation": "This is a mock response for demonstration purposes. The actual AI system would provide more comprehensive analysis based on neurodivergent research and community insights.",
                "sources": [
                    "https://example.org/neurodivergent-research",
                    "https://example.org/community-insights",
                ],
                "tags": {
                    "strengths": ["unique perspective"],
                    "overlaps": ["neurodivergence"],
                    "struggles": ["information gaps"],
                },
            }

        # Add random variation for realism
        response_data["trust"] += random.uniform(-0.05, 0.05)
        response_data["trust"] = max(0.0, min(1.0, response_data["trust"]))

        return {
            "answer": {
                "claim": question,
                "mode": mode,
                "tags": response_data["tags"],
                "explanation": response_data["explanation"],
            },
            "verdict": response_data["verdict"],
            "trust": round(response_data["trust"], 2),
            "sources": response_data["sources"],
        }


# Initialize mock AI
mock_ai = NeurodivergentAIMock()


@app.post("/ask")
async def ask_question(request: QuestionRequest):
    """🧠 Ask a question to the neurodivergent AI"""

    # Validate mode
    if request.mode not in ["science", "lived", "balanced"]:
        raise HTTPException(
            status_code=400, detail="Invalid mode. Use: science, lived, or balanced"
        )

    # Validate question
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")

    # Mock consent check
    if request.user_id == "no-consent":
        raise HTTPException(
            status_code=403, detail="Consent not granted for this scope"
        )

    # Generate response
    response = mock_ai.get_response(request.question, request.mode)

    return response


@app.get("/modelcard")
async def get_model_card():
    """📋 Get model transparency information"""

    return {
        "name": "Neurodivergent AI (Mock Demo)",
        "version": "1.0.0-demo",
        "modes": ["science", "lived", "balanced"],
        "consent": "enforced",
        "pii": "scrubbed",
        "bias_monitoring": "active",
        "limits": [
            "demo responses only",
            "limited knowledge base",
            "mock trust scoring",
            "simplified reasoning",
        ],
        "ethics": {
            "strengths_based": True,
            "lived_experience_valued": True,
            "community_driven": True,
            "transparent": True,
        },
        "last_audit": "2025-08-22",
        "contact": "hyperfocus-zone@example.com",
    }


@app.get("/health")
async def health_check():
    """🏥 Health check endpoint"""

    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "neurodivergent-ai-mock",
        "version": "1.0.0",
    }


@app.get("/")
async def root():
    """🏠 Root endpoint with welcome message"""

    return {
        "message": "🧠💎⚡ Welcome to Neurodivergent AI Mock Server",
        "description": "Built BY and FOR the neurodivergent community",
        "endpoints": {
            "ask": "POST /ask - Ask questions about neurodivergence",
            "modelcard": "GET /modelcard - View model transparency information",
            "health": "GET /health - Health check",
        },
        "demo_questions": [
            "Does ADHD improve creativity?",
            "What helps with sensory overload?",
            "How do ADHD and autism overlap?",
            "What are neurodivergent strengths?",
        ],
    }


if __name__ == "__main__":
    print("🧠💎⚡ Starting Neurodivergent AI Mock Server...")
    print("🌐 Server will be available at: http://localhost:8000")
    print('📱 Test with CLI: python cli/ask.py "Does ADHD improve creativity?"')
    print("🌐 Test with web: Open web/index.html in your browser")
    print("📋 Model card: http://localhost:8000/modelcard")
    print("🏥 Health check: http://localhost:8000/health")

    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True, log_level="info")

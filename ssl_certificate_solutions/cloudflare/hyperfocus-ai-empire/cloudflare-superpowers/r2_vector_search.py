"""
💎🔍⚡ CLOUDFLARE R2 + VECTOR SEARCH MEMORY CRYSTALS ⚡🔍💎

Implementing the team's chosen super power:
- Global memory crystal storage using R2
- Vector embeddings for semantic search
- Real-time memory synchronization
- Infinite scalable crystal archive

Team excitement: LEGENDARY MEMORY POWER! 🧠💎
"""

import asyncio
import json
import logging
import uuid
from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
from cloudflare import Cloudflare
from sentence_transformers import SentenceTransformer

# Configure empire-level logging
logging.basicConfig(
    level=logging.INFO, format="💎 %(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


@dataclass
class MemoryCrystal:
    """💎 Individual memory crystal structure"""

    crystal_id: str
    content: str
    embedding: List[float]
    metadata: Dict[str, Any]
    created_at: str
    updated_at: str
    access_count: int
    relevance_score: float = 0.0


@dataclass
class CrystalCollection:
    """🔮 Collection of related memory crystals"""

    collection_id: str
    name: str
    description: str
    crystals: List[str]  # Crystal IDs
    tags: List[str]
    created_at: str
    total_crystals: int


@dataclass
class SearchResult:
    """🔍 Memory crystal search result"""

    crystal: MemoryCrystal
    similarity_score: float
    context_relevance: float
    edge_location: str


class VectorSearchEngine:
    """🧠 Vector similarity search for memory crystals"""

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        """Initialize with sentence transformer model"""
        self.model = SentenceTransformer(model_name)
        self.embedding_dimension = 384  # Default for all-MiniLM-L6-v2
        logger.info(f"🧠 Vector search engine initialized with {model_name}")

    def generate_embedding(self, text: str) -> List[float]:
        """🔮 Generate vector embedding for text"""
        try:
            embedding = self.model.encode(text, convert_to_tensor=False)
            return embedding.tolist()
        except Exception as e:
            logger.error(f"❌ Failed to generate embedding: {e}")
            return [0.0] * self.embedding_dimension

    def calculate_similarity(
        self, embedding1: List[float], embedding2: List[float]
    ) -> float:
        """📊 Calculate cosine similarity between embeddings"""
        try:
            vec1 = np.array(embedding1)
            vec2 = np.array(embedding2)

            # Normalize vectors
            vec1_norm = vec1 / np.linalg.norm(vec1)
            vec2_norm = vec2 / np.linalg.norm(vec2)

            # Calculate cosine similarity
            similarity = np.dot(vec1_norm, vec2_norm)
            return float(similarity)

        except Exception as e:
            logger.error(f"❌ Failed to calculate similarity: {e}")
            return 0.0

    def search_crystals(
        self,
        query_embedding: List[float],
        crystal_embeddings: List[Tuple[str, List[float]]],
        top_k: int = 10,
    ) -> List[Tuple[str, float]]:
        """🔍 Search for most similar crystals"""
        similarities = []

        for crystal_id, embedding in crystal_embeddings:
            similarity = self.calculate_similarity(query_embedding, embedding)
            similarities.append((crystal_id, similarity))

        # Sort by similarity score (descending)
        similarities.sort(key=lambda x: x[1], reverse=True)

        return similarities[:top_k]


class CloudflareR2MemoryCrystals:
    """💎 Cloudflare R2 + Vector Search for Memory Crystals"""

    def __init__(
        self,
        api_token: str,
        account_id: str,
        bucket_name: str = "hyperfocus-memory-crystals",
    ):
        """Initialize R2 integration"""
        self.client = Cloudflare(api_token=api_token)
        self.account_id = account_id
        self.bucket_name = bucket_name
        self.vector_engine = VectorSearchEngine()

        # Empire configuration
        self.crystal_index_key = "crystal_index.json"
        self.embedding_index_key = "embedding_index.json"

        logger.info("💎 Cloudflare R2 Memory Crystal System Initialized!")

    async def create_r2_bucket(self) -> bool:
        """🪣 Create R2 bucket for memory crystal storage"""
        try:
            logger.info(f"🔮 Creating R2 bucket: {self.bucket_name}")

            # Create R2 bucket
            response = self.client.r2.buckets.create(
                account_id=self.account_id, name=self.bucket_name
            )

            logger.info(f"✅ R2 bucket created successfully: {self.bucket_name}")
            return True

        except Exception as e:
            if "already exists" in str(e).lower():
                logger.info(f"💎 R2 bucket already exists: {self.bucket_name}")
                return True
            logger.error(f"❌ Failed to create R2 bucket: {e}")
            return False

    async def store_memory_crystal(
        self, content: str, metadata: Dict[str, Any] = None
    ) -> str:
        """💎 Store new memory crystal with vector embedding"""
        try:
            # Generate unique crystal ID
            crystal_id = str(uuid.uuid4())

            # Generate embedding for content
            embedding = self.vector_engine.generate_embedding(content)

            # Create memory crystal
            crystal = MemoryCrystal(
                crystal_id=crystal_id,
                content=content,
                embedding=embedding,
                metadata=metadata or {},
                created_at=datetime.now().isoformat(),
                updated_at=datetime.now().isoformat(),
                access_count=0,
            )

            # Store crystal in R2
            crystal_key = f"crystals/{crystal_id}.json"
            crystal_data = json.dumps(asdict(crystal), ensure_ascii=False)

            response = self.client.r2.objects.put(
                account_id=self.account_id,
                bucket_name=self.bucket_name,
                key=crystal_key,
                value=crystal_data.encode("utf-8"),
            )

            # Update crystal index
            await self._update_crystal_index(crystal)

            logger.info(f"💎 Memory crystal stored: {crystal_id}")
            return crystal_id

        except Exception as e:
            logger.error(f"❌ Failed to store memory crystal: {e}")
            return ""

    async def retrieve_memory_crystal(self, crystal_id: str) -> Optional[MemoryCrystal]:
        """🔍 Retrieve specific memory crystal"""
        try:
            crystal_key = f"crystals/{crystal_id}.json"

            response = self.client.r2.objects.get(
                account_id=self.account_id,
                bucket_name=self.bucket_name,
                key=crystal_key,
            )

            if response:
                crystal_data = json.loads(response.body.decode("utf-8"))
                crystal = MemoryCrystal(**crystal_data)

                # Increment access count
                crystal.access_count += 1
                await self._update_crystal_access_count(crystal)

                logger.info(f"💎 Retrieved crystal: {crystal_id}")
                return crystal

            return None

        except Exception as e:
            logger.error(f"❌ Failed to retrieve crystal {crystal_id}: {e}")
            return None

    async def search_memory_crystals(
        self, query: str, top_k: int = 10, filters: Dict[str, Any] = None
    ) -> List[SearchResult]:
        """🔍 Semantic search across memory crystals"""
        try:
            logger.info(f"🔍 Searching crystals for: {query[:50]}...")

            # Generate query embedding
            query_embedding = self.vector_engine.generate_embedding(query)

            # Get crystal index
            crystal_index = await self._get_crystal_index()

            # Apply filters if provided
            if filters:
                crystal_index = self._apply_filters(crystal_index, filters)

            # Extract embeddings for search
            crystal_embeddings = [
                (crystal["crystal_id"], crystal["embedding"])
                for crystal in crystal_index
            ]

            # Perform vector search
            similar_crystals = self.vector_engine.search_crystals(
                query_embedding, crystal_embeddings, top_k
            )

            # Build search results
            results = []
            for crystal_id, similarity_score in similar_crystals:
                crystal = await self.retrieve_memory_crystal(crystal_id)
                if crystal:
                    result = SearchResult(
                        crystal=crystal,
                        similarity_score=similarity_score,
                        context_relevance=self._calculate_context_relevance(
                            crystal, query
                        ),
                        edge_location="global",  # R2 is globally distributed
                    )
                    results.append(result)

            logger.info(f"🔍 Found {len(results)} relevant crystals")
            return results

        except Exception as e:
            logger.error(f"❌ Search failed: {e}")
            return []

    async def create_crystal_collection(
        self,
        name: str,
        description: str,
        crystal_ids: List[str],
        tags: List[str] = None,
    ) -> str:
        """🔮 Create collection of related memory crystals"""
        try:
            collection_id = str(uuid.uuid4())

            collection = CrystalCollection(
                collection_id=collection_id,
                name=name,
                description=description,
                crystals=crystal_ids,
                tags=tags or [],
                created_at=datetime.now().isoformat(),
                total_crystals=len(crystal_ids),
            )

            # Store collection in R2
            collection_key = f"collections/{collection_id}.json"
            collection_data = json.dumps(asdict(collection), ensure_ascii=False)

            self.client.r2.objects.put(
                account_id=self.account_id,
                bucket_name=self.bucket_name,
                key=collection_key,
                value=collection_data.encode("utf-8"),
            )

            logger.info(f"🔮 Crystal collection created: {name}")
            return collection_id

        except Exception as e:
            logger.error(f"❌ Failed to create collection: {e}")
            return ""

    async def get_crystal_analytics(self) -> Dict[str, Any]:
        """📊 Get analytics for memory crystal usage"""
        try:
            crystal_index = await self._get_crystal_index()

            analytics = {
                "total_crystals": len(crystal_index),
                "total_storage_mb": sum(len(c["content"]) for c in crystal_index)
                / (1024 * 1024),
                "most_accessed": (
                    max(crystal_index, key=lambda x: x.get("access_count", 0))
                    if crystal_index
                    else None
                ),
                "creation_timeline": self._analyze_creation_timeline(crystal_index),
                "popular_tags": self._analyze_popular_tags(crystal_index),
                "embedding_diversity": self._analyze_embedding_diversity(crystal_index),
                "timestamp": datetime.now().isoformat(),
            }

            logger.info("📊 Crystal analytics generated")
            return analytics

        except Exception as e:
            logger.error(f"❌ Failed to generate analytics: {e}")
            return {}

    async def _update_crystal_index(self, crystal: MemoryCrystal):
        """📋 Update the master crystal index"""
        try:
            # Get existing index
            crystal_index = await self._get_crystal_index()

            # Add new crystal to index
            crystal_entry = {
                "crystal_id": crystal.crystal_id,
                "content_preview": crystal.content[:100],
                "embedding": crystal.embedding,
                "metadata": crystal.metadata,
                "created_at": crystal.created_at,
                "access_count": crystal.access_count,
            }

            crystal_index.append(crystal_entry)

            # Store updated index
            index_data = json.dumps(crystal_index, ensure_ascii=False)

            self.client.r2.objects.put(
                account_id=self.account_id,
                bucket_name=self.bucket_name,
                key=self.crystal_index_key,
                value=index_data.encode("utf-8"),
            )

        except Exception as e:
            logger.error(f"❌ Failed to update crystal index: {e}")

    async def _get_crystal_index(self) -> List[Dict[str, Any]]:
        """📋 Get the master crystal index"""
        try:
            response = self.client.r2.objects.get(
                account_id=self.account_id,
                bucket_name=self.bucket_name,
                key=self.crystal_index_key,
            )

            if response:
                return json.loads(response.body.decode("utf-8"))

            return []

        except Exception as e:
            # Index doesn't exist yet, return empty list
            return []

    async def _update_crystal_access_count(self, crystal: MemoryCrystal):
        """📈 Update crystal access count"""
        try:
            crystal_key = f"crystals/{crystal.crystal_id}.json"
            crystal_data = json.dumps(asdict(crystal), ensure_ascii=False)

            self.client.r2.objects.put(
                account_id=self.account_id,
                bucket_name=self.bucket_name,
                key=crystal_key,
                value=crystal_data.encode("utf-8"),
            )

        except Exception as e:
            logger.error(f"❌ Failed to update access count: {e}")

    def _apply_filters(
        self, crystal_index: List[Dict], filters: Dict[str, Any]
    ) -> List[Dict]:
        """🔍 Apply filters to crystal search"""
        filtered_crystals = crystal_index

        for key, value in filters.items():
            if key == "created_after":
                filtered_crystals = [
                    c for c in filtered_crystals if c["created_at"] >= value
                ]
            elif key == "tags":
                filtered_crystals = [
                    c
                    for c in filtered_crystals
                    if any(tag in c["metadata"].get("tags", []) for tag in value)
                ]
            elif key == "min_access_count":
                filtered_crystals = [
                    c for c in filtered_crystals if c["access_count"] >= value
                ]

        return filtered_crystals

    def _calculate_context_relevance(self, crystal: MemoryCrystal, query: str) -> float:
        """🎯 Calculate contextual relevance score"""
        # Simple relevance calculation based on metadata and content
        relevance = 0.5  # Base relevance

        # Boost for recent access
        if crystal.access_count > 5:
            relevance += 0.2

        # Boost for metadata matches
        query_words = query.lower().split()
        metadata_text = json.dumps(crystal.metadata).lower()

        matches = sum(1 for word in query_words if word in metadata_text)
        relevance += min(matches * 0.1, 0.3)

        return min(relevance, 1.0)

    def _analyze_creation_timeline(self, crystal_index: List[Dict]) -> Dict[str, int]:
        """📅 Analyze crystal creation timeline"""
        timeline = {}
        for crystal in crystal_index:
            date = crystal["created_at"][:10]  # YYYY-MM-DD
            timeline[date] = timeline.get(date, 0) + 1
        return timeline

    def _analyze_popular_tags(self, crystal_index: List[Dict]) -> Dict[str, int]:
        """🏷️ Analyze popular tags"""
        tag_counts = {}
        for crystal in crystal_index:
            tags = crystal["metadata"].get("tags", [])
            for tag in tags:
                tag_counts[tag] = tag_counts.get(tag, 0) + 1
        return dict(sorted(tag_counts.items(), key=lambda x: x[1], reverse=True)[:10])

    def _analyze_embedding_diversity(self, crystal_index: List[Dict]) -> float:
        """🌈 Analyze embedding diversity"""
        if len(crystal_index) < 2:
            return 0.0

        # Calculate average pairwise distance
        embeddings = [
            crystal["embedding"] for crystal in crystal_index[:100]
        ]  # Sample for performance
        total_distance = 0
        pairs = 0

        for i in range(len(embeddings)):
            for j in range(i + 1, len(embeddings)):
                distance = 1 - self.vector_engine.calculate_similarity(
                    embeddings[i], embeddings[j]
                )
                total_distance += distance
                pairs += 1

        return total_distance / pairs if pairs > 0 else 0.0


class MemoryCrystalEmpire:
    """🏆 Empire controller for memory crystal management"""

    def __init__(self, api_token: str, account_id: str):
        self.r2_crystals = CloudflareR2MemoryCrystals(api_token, account_id)
        self.empire_status = "INITIALIZING"

    async def deploy_crystal_empire(self) -> Dict[str, bool]:
        """🚀 Deploy complete memory crystal infrastructure"""
        logger.info("💎 DEPLOYING MEMORY CRYSTAL EMPIRE...")

        deployment_results = {}

        try:
            # Phase 1: Create R2 bucket
            logger.info("🪣 Phase 1: Creating crystal storage bucket...")
            bucket_result = await self.r2_crystals.create_r2_bucket()
            deployment_results["r2_bucket"] = bucket_result

            # Phase 2: Store sample crystals
            logger.info("💎 Phase 2: Creating sample memory crystals...")

            sample_crystals = [
                {
                    "content": "🧠 ADHD hyperfocus state can be channeled into productive work sessions lasting 2-4 hours with proper setup and boundary management. Remove distractions, prepare snacks and water, set clear goals.",
                    "metadata": {
                        "tags": ["adhd", "hyperfocus", "productivity"],
                        "category": "technique",
                    },
                },
                {
                    "content": "🍅 Modified Pomodoro for ADHD: Use flexible timing (15-45 minutes), allow natural break points, celebrate completions with dopamine rewards, adjust based on energy levels.",
                    "metadata": {
                        "tags": ["pomodoro", "adhd", "timing"],
                        "category": "technique",
                    },
                },
                {
                    "content": "👥 Body doubling effectiveness increases by 85% when participants share goals at the start and check in every 30 minutes. Virtual body doubling works as well as in-person for most people.",
                    "metadata": {
                        "tags": ["body-doubling", "accountability", "social"],
                        "category": "research",
                    },
                },
                {
                    "content": "⚡ Empire infrastructure runs on 212.227.127.144:8888 with Pi network nodes for distributed processing. Docker containers provide scalable deployment across multiple environments.",
                    "metadata": {
                        "tags": ["infrastructure", "empire", "docker"],
                        "category": "technical",
                    },
                },
                {
                    "content": "🌟 Chief Lyndz appreciation explosion: 'ye yes yes amzing my team woooow' - achieved through strategic intelligence empire expansion with multi-modal capabilities.",
                    "metadata": {
                        "tags": ["celebration", "team", "achievement"],
                        "category": "milestone",
                    },
                },
            ]

            crystal_ids = []
            for crystal_data in sample_crystals:
                crystal_id = await self.r2_crystals.store_memory_crystal(
                    crystal_data["content"], crystal_data["metadata"]
                )
                if crystal_id:
                    crystal_ids.append(crystal_id)

            deployment_results["sample_crystals"] = len(crystal_ids) == len(
                sample_crystals
            )

            # Phase 3: Create sample collection
            logger.info("🔮 Phase 3: Creating crystal collection...")
            collection_id = await self.r2_crystals.create_crystal_collection(
                name="ADHD Optimization Techniques",
                description="Proven techniques for ADHD focus and productivity optimization",
                crystal_ids=crystal_ids[:3],  # First 3 crystals
                tags=["adhd", "focus", "productivity"],
            )
            deployment_results["sample_collection"] = bool(collection_id)

            # Update empire status
            all_successful = all(deployment_results.values())
            self.empire_status = "LEGENDARY" if all_successful else "PARTIAL_DEPLOYMENT"

            logger.info(
                f"💎 Memory Crystal Empire deployment complete! Status: {self.empire_status}"
            )
            return deployment_results

        except Exception as e:
            logger.error(f"❌ Crystal empire deployment failed: {e}")
            self.empire_status = "FAILED"
            return deployment_results

    async def demonstrate_search_capabilities(self):
        """🔍 Demonstrate the search capabilities"""
        logger.info("🔍 DEMONSTRATING MEMORY CRYSTAL SEARCH...")

        # Search examples
        search_queries = [
            "ADHD hyperfocus techniques",
            "Pomodoro timer modifications",
            "Body doubling accountability",
            "Empire infrastructure setup",
            "Team celebration achievements",
        ]

        for query in search_queries:
            logger.info(f"🔍 Searching for: {query}")
            results = await self.r2_crystals.search_memory_crystals(query, top_k=3)

            for i, result in enumerate(results):
                logger.info(
                    f"   {i+1}. Similarity: {result.similarity_score:.3f} - {result.crystal.content[:80]}..."
                )

        # Get analytics
        analytics = await self.r2_crystals.get_crystal_analytics()
        logger.info(f"📊 Total crystals: {analytics.get('total_crystals', 0)}")
        logger.info(f"📊 Storage used: {analytics.get('total_storage_mb', 0):.2f} MB")


# Example usage
async def main():
    """🧪 Test the memory crystal system"""

    API_TOKEN = "your_cloudflare_api_token"
    ACCOUNT_ID = "your_account_id"

    logger.info("💎 STARTING MEMORY CRYSTAL EMPIRE TEST...")

    # Initialize empire
    empire = MemoryCrystalEmpire(API_TOKEN, ACCOUNT_ID)

    # Deploy infrastructure
    results = await empire.deploy_crystal_empire()

    logger.info("🏆 DEPLOYMENT RESULTS:")
    for component, success in results.items():
        status = "✅ SUCCESS" if success else "❌ FAILED"
        logger.info(f"   {component}: {status}")

    # Demonstrate search
    if empire.empire_status == "LEGENDARY":
        await empire.demonstrate_search_capabilities()

    logger.info(f"💎 Crystal Empire Status: {empire.empire_status}")


if __name__ == "__main__":
    asyncio.run(main())

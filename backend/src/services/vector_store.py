"""
Vector Store Service

Handles interactions with Qdrant vector database for semantic search
"""

from typing import List, Dict, Any
from qdrant_client import QdrantClient
from qdrant_client.models import SearchRequest, Filter

from src.config import settings
from src.utils.logging import logger, log_with_context


class VectorStoreService:
    """Service for interacting with Qdrant vector database"""

    def __init__(self) -> None:
        """Initialize Qdrant client"""
        self.client = QdrantClient(url=settings.qdrant_url, api_key=settings.qdrant_api_key)
        self.collection_name = settings.qdrant_collection_name

    def search(
        self, query_vector: List[float], top_k: int = 5, filter_params: Dict[str, Any] | None = None
    ) -> List[Dict[str, Any]]:
        """
        Search for similar passages in the vector database

        Args:
            query_vector: Query embedding vector (1536 dimensions)
            top_k: Number of top results to return
            filter_params: Optional filter parameters (e.g., {"chapter_number": 5})

        Returns:
            List of retrieved passages with metadata
        """
        try:
            # Build filter if provided
            search_filter = None
            if filter_params:
                search_filter = Filter(**filter_params)

            # Search
            results = self.client.search(
                collection_name=self.collection_name,
                query_vector=query_vector,
                limit=top_k,
                query_filter=search_filter,
            )

            # Format results
            passages = []
            for result in results:
                passages.append(
                    {
                        "text": result.payload.get("text", ""),
                        "chapter": result.payload.get("chapter", ""),
                        "section": result.payload.get("section", ""),
                        "relevance_score": float(result.score),
                        "metadata": {
                            "chapter_number": result.payload.get("chapter_number"),
                            "sidebar_position": result.payload.get("sidebar_position"),
                            "chunk_index": result.payload.get("chunk_index"),
                            "source_file": result.payload.get("source_file"),
                        },
                    }
                )

            log_with_context(
                logger,
                "info",
                "Vector search completed",
                top_k=top_k,
                results_count=len(passages),
            )

            return passages

        except Exception as e:
            logger.error(f"Vector search failed: {str(e)}", exc_info=True)
            raise

    def health_check(self) -> bool:
        """
        Check if Qdrant is healthy and collection exists

        Returns:
            True if healthy, False otherwise
        """
        try:
            collections = self.client.get_collections().collections
            collection_names = [c.name for c in collections]

            if self.collection_name not in collection_names:
                logger.warning(f"Collection '{self.collection_name}' not found")
                return False

            # Get collection info
            collection_info = self.client.get_collection(self.collection_name)

            log_with_context(
                logger,
                "info",
                "Qdrant health check passed",
                vectors_count=collection_info.vectors_count,
            )

            return True

        except Exception as e:
            logger.error(f"Qdrant health check failed: {str(e)}", exc_info=True)
            return False

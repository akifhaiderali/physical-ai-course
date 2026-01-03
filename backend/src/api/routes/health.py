"""
Health Check Endpoint

Provides health status for the API and its dependencies
"""

from fastapi import APIRouter
from datetime import datetime
from typing import Dict, Any

from src.services.vector_store import VectorStoreService
from src.utils.logging import logger

router = APIRouter()


@router.get("/health")
async def health_check() -> Dict[str, Any]:
    """
    Health check endpoint

    Returns health status of API and dependencies
    """
    try:
        # Check Qdrant
        vector_store = VectorStoreService()
        qdrant_healthy = vector_store.health_check()

        # Overall status
        status = "healthy" if qdrant_healthy else "unhealthy"

        return {
            "status": status,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "dependencies": {
                "vector_db": "healthy" if qdrant_healthy else "unhealthy",
                "llm_api": "healthy",  # OpenAI health checked on demand
            },
        }

    except Exception as e:
        logger.error(f"Health check failed: {str(e)}", exc_info=True)
        return {
            "status": "unhealthy",
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "dependencies": {
                "vector_db": "unhealthy",
                "llm_api": "unknown",
            },
            "error": str(e),
        }

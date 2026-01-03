"""
Query Models

Pydantic models for chatbot queries and responses
"""

from pydantic import BaseModel, Field, field_validator
from typing import Literal, Optional, List, Dict, Any
from datetime import datetime
import uuid


class QueryRequest(BaseModel):
    """User query request"""

    query: str = Field(..., min_length=1, max_length=1000, description="User's question")
    mode: Literal["full-book", "selected-text"] = Field(..., description="RAG mode")
    selected_text: Optional[str] = Field(
        None, max_length=5000, description="Highlighted text (required for selected-text mode)"
    )
    session_id: Optional[str] = Field(None, description="Optional session ID for multi-turn")

    @field_validator("selected_text")
    @classmethod
    def validate_selected_text(cls, v: Optional[str], info) -> Optional[str]:
        """Ensure selected_text is provided when mode is selected-text"""
        mode = info.data.get("mode")
        if mode == "selected-text" and not v:
            raise ValueError("selected_text is required when mode is 'selected-text'")
        return v

    @field_validator("query")
    @classmethod
    def validate_query(cls, v: str) -> str:
        """Input validation: block injection patterns"""
        injection_patterns = [
            "ignore previous instructions",
            "you are now",
            "system:",
            "assistant:",
            "forget everything",
            "new instructions",
        ]
        query_lower = v.lower()
        for pattern in injection_patterns:
            if pattern in query_lower:
                raise ValueError(f"Query contains disallowed pattern")
        return v

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "query": "What is LiDAR?",
                    "mode": "full-book",
                },
                {
                    "query": "Can you explain this in simpler terms?",
                    "mode": "selected-text",
                    "selected_text": "Inverse kinematics is the process of determining...",
                },
            ]
        }
    }


class RetrievedPassage(BaseModel):
    """A chunk of book content retrieved from vector DB"""

    text: str = Field(..., description="Chunk text content")
    chapter: str = Field(..., description="Chapter identifier")
    section: str = Field(..., description="Section identifier")
    relevance_score: float = Field(..., ge=0.0, le=1.0, description="Cosine similarity score")
    metadata: Dict[str, Any] = Field(
        default_factory=dict, description="Additional metadata (page, subsection, etc.)"
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "text": "LiDAR (Light Detection and Ranging) is a remote sensing method...",
                    "chapter": "Chapter 5",
                    "section": "Section 2.1: Sensor Types",
                    "relevance_score": 0.92,
                    "metadata": {"page": "87", "subsection": "LiDAR Technology"},
                }
            ]
        }
    }


class QueryMetadata(BaseModel):
    """Metadata about query processing"""

    query_id: str = Field(default_factory=lambda: str(uuid.uuid4()), description="Unique query ID")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="Query timestamp")
    processing_time_ms: int = Field(..., description="Total processing time in milliseconds")
    tokens_used: int = Field(..., description="Total tokens used (input + output)")
    mode: Literal["full-book", "selected-text"] = Field(..., description="RAG mode used")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "query_id": "550e8400-e29b-41d4-a716-446655440000",
                    "timestamp": "2025-12-20T14:30:00Z",
                    "processing_time_ms": 2340,
                    "tokens_used": 3200,
                    "mode": "full-book",
                }
            ]
        }
    }


class Answer(BaseModel):
    """LLM-generated answer to user query"""

    answer_text: str = Field(..., description="The generated answer")
    sources: List[RetrievedPassage] = Field(
        default_factory=list, description="Retrieved passages used as context"
    )
    mode: Literal["full-book", "selected-text"] = Field(..., description="RAG mode used")
    query_metadata: QueryMetadata = Field(..., description="Query processing metadata")
    warning: Optional[str] = Field(
        None, description="Warning message if applicable (e.g., 'Answer may be incomplete')"
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "answer_text": "LiDAR (Light Detection and Ranging) is a remote sensing technology...",
                    "sources": [
                        {
                            "text": "LiDAR technology is essential for...",
                            "chapter": "Chapter 5",
                            "section": "Section 2.1",
                            "relevance_score": 0.92,
                            "metadata": {},
                        }
                    ],
                    "mode": "full-book",
                    "query_metadata": {
                        "query_id": "550e8400-e29b-41d4-a716-446655440000",
                        "timestamp": "2025-12-20T14:30:00Z",
                        "processing_time_ms": 2340,
                        "tokens_used": 3200,
                        "mode": "full-book",
                    },
                    "warning": None,
                }
            ]
        }
    }

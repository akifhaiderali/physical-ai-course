from pydantic_settings import BaseSettings
from typing import List, Optional


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""

    # =====================
    # LLM Configuration
    # =====================
    llm_provider: str = "gemini"  # openai | claude | gemini
    llm_model: str = "claude-3-5-sonnet"
    llm_max_tokens: int = 500
    llm_temperature: float = 0.3

    # =====================
    # OpenAI (optional now)
    # =====================
    openai_api_key: Optional[str] = None

    # =====================
    # Gemini Configuration
    # =====================
    gemini_api_key: Optional[str] = None
    gemini_model: str = "gemini-1.5-flash"

    # =====================
    # Embeddings
    # =====================
    embedding_provider: str = "huggingface"  # openai | huggingface
    hf_model_name: str = "sentence-transformers/all-MiniLM-L6-v2"
    embedding_dimension: int = 384

    # =====================
    # Qdrant
    # =====================
    qdrant_url: str
    qdrant_api_key: str
    qdrant_collection_name: str = "book_chunks"

    # =====================
    # API
    # =====================
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    api_cors_origins: List[str] = [
        "http://localhost:3000",
        "http://localhost:3001"
    ]

    # =====================
    # RAG
    # =====================
    chunk_size: int = 300
    chunk_overlap: int = 50
    top_k_chunks: int = 5

    # =====================
    # Logging
    # =====================
    log_level: str = "INFO"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "forbid"  # Keep strict validation


settings = Settings()

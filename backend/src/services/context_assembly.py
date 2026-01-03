"""
Context Assembly Service

Assembles context for LLM based on RAG mode (full-book or selected-text)
"""

from typing import List, Dict, Any

from src.services.vector_store import VectorStoreService
from src.services.embeddings import EmbeddingsService
from src.config import settings
from src.utils.logging import logger, log_with_context


class ContextAssemblyService:
    """Service for assembling context for LLM queries"""

    def __init__(self) -> None:
        """Initialize services"""
        self.vector_store = VectorStoreService()
        self.embeddings = EmbeddingsService()

    def assemble_full_book_context(self, query: str) -> tuple[str, List[Dict[str, Any]]]:
        """
        Assemble context for full-book mode using vector search

        Args:
            query: User's question

        Returns:
            Tuple of (formatted_context, retrieved_passages)
        """
        try:
            # Generate query embedding
            query_embedding = self.embeddings.generate_embedding(query)

            # Search for relevant passages
            passages = self.vector_store.search(
                query_vector=query_embedding, top_k=settings.top_k_chunks
            )

            if not passages:
                log_with_context(
                    logger, "warning", "No passages found for query", query_preview=query[:50]
                )
                return "No relevant content found in the book.", []

            # Format context for LLM
            context_parts = []
            for idx, passage in enumerate(passages, 1):
                chapter = passage.get("chapter", "Unknown Chapter")
                section = passage.get("section", "")
                text = passage.get("text", "")
                score = passage.get("relevance_score", 0.0)

                context_parts.append(
                    f"[Passage {idx}] ({chapter}, {section}, relevance: {score:.2f})\n{text}"
                )

            formatted_context = "\n\n".join(context_parts)

            log_with_context(
                logger,
                "info",
                "Assembled full-book context",
                passages_count=len(passages),
                context_length=len(formatted_context),
            )

            return formatted_context, passages

        except Exception as e:
            logger.error(f"Failed to assemble full-book context: {str(e)}", exc_info=True)
            raise

    def assemble_selected_text_context(self, selected_text: str) -> tuple[str, List[Dict[str, Any]]]:
        """
        Assemble context for selected-text mode (no vector search)

        Args:
            selected_text: User's highlighted text

        Returns:
            Tuple of (formatted_context, empty list)
        """
        try:
            # Simply use the selected text as context
            formatted_context = f"Selected Text:\n{selected_text}"

            log_with_context(
                logger,
                "info",
                "Assembled selected-text context",
                context_length=len(formatted_context),
            )

            # Return empty list for sources since we're not retrieving
            return formatted_context, []

        except Exception as e:
            logger.error(f"Failed to assemble selected-text context: {str(e)}", exc_info=True)
            raise

    def estimate_context_tokens(self, context: str) -> int:
        """
        Estimate number of tokens in context

        Args:
            context: Context text

        Returns:
            Estimated token count
        """
        # Simple estimation: ~4 characters per token
        return len(context) // 4

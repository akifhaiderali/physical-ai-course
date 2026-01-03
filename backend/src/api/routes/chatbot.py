"""
Chatbot API Routes

Handles chatbot query requests for both RAG modes
"""

from fastapi import APIRouter, HTTPException, status
from datetime import datetime
import time

from src.api.models.query import QueryRequest, Answer, QueryMetadata, RetrievedPassage
from src.services.context_assembly import ContextAssemblyService
from src.services.llm import LLMService
from src.services.input_validation import InputValidationService
from src.utils.logging import logger, log_with_context
from typing import Tuple, Optional
import re

router = APIRouter()

# Initialize services
context_service = ContextAssemblyService()
llm_service = LLMService()
validation_service = InputValidationService()

# Conversational patterns
CONVERSATIONAL_PATTERNS = [
    r"^hi+$",
    r"^hello+$",
    r"^hey+$",
    r"^good\s+(morning|afternoon|evening|day)$",
    r"^thanks?(\s+you)?$",
    r"^thank\s+you$",
    r"^bye+$",
    r"^goodbye+$",
    r"^how\s+are\s+you\??$",
    r"^what'?s\s+up\??$",
    r"^ok+$",
    r"^okay+$",
    r"^cool+$",
    r"^nice+$",
    r"^great+$",
]

CONVERSATIONAL_RESPONSES = {
    "greeting": "👋 Hello! I'm your Physical AI & Humanoid Robotics course assistant. I can help you with:\n\n• **Understanding course concepts** (ROS 2, Nav2, simulations)\n• **Explaining technical topics** (DDS, VLA models, Isaac Sim)\n• **Finding specific information** in the course material\n\nWhat would you like to learn about?",
    "thanks": "You're welcome! Feel free to ask if you have more questions about the course.",
    "bye": "Goodbye! Come back anytime if you need help with the Physical AI course.",
    "howru": "I'm doing great, thanks for asking! I'm here to help you with the Physical AI & Humanoid Robotics course. What would you like to know?",
    "casual": "I'm here to help with the Physical AI & Humanoid Robotics course! Feel free to ask me about ROS 2, navigation, simulations, or any other course topics.",
}

def is_conversational(query: str) -> Tuple[bool, Optional[str]]:
    """
    Check if query is conversational (greeting, thanks, etc.)

    Returns:
        (is_conversational, response_type)
    """
    query_lower = query.lower().strip()

    # Check for greetings
    if re.match(r"^(hi+|hello+|hey+|good\s+(morning|afternoon|evening|day))$", query_lower):
        return True, "greeting"

    # Check for thanks
    if re.match(r"^(thanks?(\s+you)?|thank\s+you)$", query_lower):
        return True, "thanks"

    # Check for goodbye
    if re.match(r"^(bye+|goodbye+|see\s+you)$", query_lower):
        return True, "bye"

    # Check for "how are you"
    if re.match(r"^how\s+are\s+you\??$", query_lower):
        return True, "howru"

    # Check for other casual expressions
    for pattern in CONVERSATIONAL_PATTERNS[9:]:  # ok, cool, nice, great, etc.
        if re.match(pattern, query_lower):
            return True, "casual"

    return False, None


@router.post("/chat/query", response_model=Answer)
async def submit_query(request: QueryRequest) -> Answer:
    """
    Submit a chatbot query

    Supports two modes:
    - full-book: Searches entire book using vector similarity
    - selected-text: Uses user-highlighted text as direct context

    Args:
        request: Query request with mode and optional selected text

    Returns:
        Answer with generated response and sources

    Raises:
        HTTPException: If validation fails or processing error occurs
    """
    start_time = time.time()

    try:
        # Validate query
        is_valid, error_msg = validation_service.validate_query(request.query)
        if not is_valid:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error_msg)

        # Check if query is conversational
        is_conv, conv_type = is_conversational(request.query)
        if is_conv:
            # Return conversational response without RAG
            processing_time_ms = int((time.time() - start_time) * 1000)

            metadata = QueryMetadata(
                processing_time_ms=processing_time_ms,
                tokens_used=0,
                mode=request.mode,
            )

            answer = Answer(
                answer_text=CONVERSATIONAL_RESPONSES.get(conv_type, CONVERSATIONAL_RESPONSES["casual"]),
                sources=[],
                mode=request.mode,
                query_metadata=metadata,
                warning=None,
            )

            log_with_context(
                logger,
                "info",
                "Conversational query handled",
                conv_type=conv_type,
                processing_time_ms=processing_time_ms,
            )

            return answer

        # Assemble context based on mode
        if request.mode == "full-book":
            log_with_context(
                logger, "info", "Processing full-book query", query_preview=request.query[:50]
            )

            context, passages = context_service.assemble_full_book_context(request.query)

        elif request.mode == "selected-text":
            # Validate selected text
            if not request.selected_text:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="selected_text is required for selected-text mode",
                )

            is_valid, error_msg = validation_service.validate_selected_text(request.selected_text)
            if not is_valid:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error_msg)

            log_with_context(
                logger, "info", "Processing selected-text query", query_preview=request.query[:50]
            )

            context, passages = context_service.assemble_selected_text_context(
                request.selected_text
            )

        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid mode: {request.mode}",
            )

        # Generate answer using LLM
        answer_text, tokens_used = llm_service.generate_answer(
            query=request.query, context=context, mode=request.mode
        )

        # Check grounding (for full-book mode)
        warning = None
        if request.mode == "full-book":
            is_grounded = validation_service.check_grounding(answer_text, context)
            if not is_grounded:
                warning = "Answer may not be fully grounded in book content"
                log_with_context(
                    logger,
                    "warning",
                    "Answer may not be grounded",
                    query_preview=request.query[:50],
                )

        # Calculate processing time
        processing_time_ms = int((time.time() - start_time) * 1000)

        # Create metadata
        metadata = QueryMetadata(
            processing_time_ms=processing_time_ms,
            tokens_used=tokens_used,
            mode=request.mode,
        )

        # Convert passages to RetrievedPassage models
        sources = []
        for passage in passages:
            sources.append(
                RetrievedPassage(
                    text=passage.get("text", ""),
                    chapter=passage.get("chapter", ""),
                    section=passage.get("section", ""),
                    relevance_score=passage.get("relevance_score", 0.0),
                    metadata=passage.get("metadata", {}),
                )
            )

        # Create answer response
        answer = Answer(
            answer_text=answer_text,
            sources=sources,
            mode=request.mode,
            query_metadata=metadata,
            warning=warning,
        )

        log_with_context(
            logger,
            "info",
            "Query completed successfully",
            mode=request.mode,
            processing_time_ms=processing_time_ms,
            tokens_used=tokens_used,
        )

        return answer

    except HTTPException:
        raise

    except Exception as e:
        logger.error(f"Query processing failed: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error while processing query",
        )

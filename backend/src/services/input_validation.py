"""
Input Validation Service

Handles input sanitization and prompt injection prevention
"""

import re
from typing import List, Tuple

from src.utils.logging import logger, log_with_context


class InputValidationService:
    """Service for validating and sanitizing user input"""

    # Common prompt injection patterns (case-insensitive)
    INJECTION_PATTERNS = [
        r"ignore\s+previous\s+instructions",
        r"you\s+are\s+now",
        r"system\s*:",
        r"assistant\s*:",
        r"forget\s+everything",
        r"new\s+instructions",
        r"override\s+",
        r"disregard\s+",
    ]

    # Special characters to filter (retain basic punctuation)
    ALLOWED_CHARS_PATTERN = r"[^a-zA-Z0-9\s.,!?;:()\-'\"/\n]"

    def __init__(self) -> None:
        """Initialize validation service"""
        self.compiled_patterns = [re.compile(p, re.IGNORECASE) for p in self.INJECTION_PATTERNS]

    def validate_query(self, query: str, max_length: int = 1000) -> Tuple[bool, str]:
        """
        Validate user query for length and injection patterns

        Args:
            query: User's query string
            max_length: Maximum allowed length

        Returns:
            Tuple of (is_valid, error_message)
        """
        # Check length
        if len(query) < 1:
            return False, "Query cannot be empty"

        if len(query) > max_length:
            return False, f"Query exceeds maximum length of {max_length} characters"

        # Check for injection patterns
        for pattern in self.compiled_patterns:
            if pattern.search(query):
                log_with_context(
                    logger,
                    "warning",
                    "Potential injection pattern detected",
                    query_preview=query[:50],
                )
                return False, "Query contains disallowed patterns"

        return True, ""

    def validate_selected_text(self, text: str, max_length: int = 5000) -> Tuple[bool, str]:
        """
        Validate selected text

        Args:
            text: Selected text
            max_length: Maximum allowed length

        Returns:
            Tuple of (is_valid, error_message)
        """
        # Check length
        if len(text) < 1:
            return False, "Selected text cannot be empty"

        if len(text) > max_length:
            return False, f"Selected text exceeds maximum length of {max_length} characters"

        return True, ""

    def sanitize_text(self, text: str) -> str:
        """
        Sanitize text by removing potentially harmful characters

        Args:
            text: Text to sanitize

        Returns:
            Sanitized text
        """
        # Remove special characters (keep alphanumeric and basic punctuation)
        sanitized = re.sub(self.ALLOWED_CHARS_PATTERN, "", text)

        # Normalize whitespace
        sanitized = " ".join(sanitized.split())

        return sanitized

    def check_grounding(self, answer: str, context: str, min_overlap_ratio: float = 0.1) -> bool:
        """
        Check if answer appears to be grounded in context

        Args:
            answer: Generated answer
            context: Context used for generation
            min_overlap_ratio: Minimum ratio of overlapping words

        Returns:
            True if answer appears grounded, False otherwise
        """
        try:
            # Simple word overlap check
            answer_words = set(answer.lower().split())
            context_words = set(context.lower().split())

            # Remove common words
            stop_words = {"the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for"}
            answer_words -= stop_words
            context_words -= stop_words

            if not answer_words:
                return True  # Edge case: very short answer

            # Calculate overlap ratio
            overlap = answer_words & context_words
            overlap_ratio = len(overlap) / len(answer_words)

            is_grounded = overlap_ratio >= min_overlap_ratio

            log_with_context(
                logger,
                "debug",
                "Grounding check",
                overlap_ratio=overlap_ratio,
                is_grounded=is_grounded,
            )

            return is_grounded

        except Exception as e:
            logger.error(f"Grounding check failed: {str(e)}", exc_info=True)
            return True  # Default to allowing answer if check fails

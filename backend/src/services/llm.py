"""
Gemini LLM Service for RAG Summarization
"""

import google.generativeai as genai
from src.config import settings
from src.utils.logging import logger

genai.configure(api_key=settings.gemini_api_key)


SYSTEM_PROMPT = """
You are an AI assistant for a course book.

STRICT RULES:
- Answer ONLY using the provided context
- DO NOT copy text verbatim
- Summarize and explain clearly
- Use simple, precise language
- If answer is missing, say:
  "I don't have enough information from the book to answer that question."
"""


class LLMService:
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-2.5-flash")
        logger.info("LLMService initialized (Gemini).")

    def generate_answer(self, query: str, context: str, mode: str = "full-book"):
        if not context.strip():
            return "I don't have enough information from the book to answer that question.", 0

        prompt = f"""
{SYSTEM_PROMPT}

Context:
{context}

Question:
{query}

Answer (concise summary):
"""

        response = self.model.generate_content(
            prompt,
            generation_config={
                "temperature": 0.2,
                "max_output_tokens": 300,
            }
        )

        return response.text.strip(), 0

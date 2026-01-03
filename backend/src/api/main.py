"""
FastAPI Application

Main entry point for the RAG Chatbot API
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from src.config import settings
from src.utils.logging import setup_logging, logger
from src.api.routes import health, chatbot


# Setup logging
setup_logging(settings.log_level)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager for startup/shutdown"""
    # Startup
    logger.info("Starting RAG Chatbot API")
    logger.info(f"CORS origins: {settings.api_cors_origins}")

    yield

    # Shutdown
    logger.info("Shutting down RAG Chatbot API")


# Create FastAPI app
app = FastAPI(
    title="RAG Chatbot API",
    description="API for Physical AI & Humanoid Robotics course book chatbot",
    version="1.0.0",
    lifespan=lifespan,
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.api_cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health.router, prefix="/api/v1", tags=["health"])
app.include_router(chatbot.router, prefix="/api/v1", tags=["chatbot"])


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "RAG Chatbot API",
        "version": "1.0.0",
        "docs": "/docs",
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "src.api.main:app",
        host=settings.api_host,
        port=settings.api_port,
        reload=True,
        log_level=settings.log_level.lower(),
    )

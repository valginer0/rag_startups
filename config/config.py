"""Configuration settings for the RAG Startups project."""

import os
from pathlib import Path

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
MODELS_DIR = PROJECT_ROOT / "models"

# Model settings
DEFAULT_EMBEDDING_MODEL = "all-MiniLM-L6-v2"
LOCAL_LANGUAGE_MODEL = "gpt2"
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# Retriever settings
DEFAULT_RETRIEVER_TOP_K = 4  # Number of documents to retrieve
DEFAULT_SEARCH_TYPE = "similarity"  # Type of search to perform

# Data processing
MAX_LINES = 500_000

# LangSmith settings (from environment variables)
LANGCHAIN_CONFIG = {
    "tracing_v2": os.getenv("LANGCHAIN_TRACING_V2", "false").lower() == "true",
    "endpoint": os.getenv("LANGCHAIN_ENDPOINT", "https://api.smith.langchain.com"),
    "api_key": os.getenv("LANGCHAIN_API_KEY", ""),
    "project": os.getenv("LANGCHAIN_PROJECT", "rag_startups"),
}

# Prompt template - simpler version since we're not generating
DEFAULT_PROMPT_TEMPLATE = """Find startup ideas related to: {question}

Context examples:
{context}

Return the most relevant examples."""

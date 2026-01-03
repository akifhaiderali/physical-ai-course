from sentence_transformers import SentenceTransformer
from src.config import settings


class EmbeddingsService:
    def __init__(self):
        if settings.embedding_provider != "huggingface":
            raise ValueError("Only HuggingFace embeddings are supported")

        self.model = SentenceTransformer(settings.hf_model_name)

    def generate_embedding(self, text: str):
        return self.model.encode(
            text,
            normalize_embeddings=True
        ).tolist()

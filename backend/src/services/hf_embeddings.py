from sentence_transformers import SentenceTransformer

class HFEmbeddingService:
    def __init__(self):
        self.model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

    def embed(self, texts: list[str]) -> list[list[float]]:
        return self.model.encode(
            texts,
            show_progress_bar=False
        ).tolist()

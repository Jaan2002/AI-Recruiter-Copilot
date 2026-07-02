from sentence_transformers import SentenceTransformer
import numpy as np
class EmbeddingEngine:

    def __init__(self):
        print("Loading embedding model...")

        self.model = SentenceTransformer(
            "BAAI/bge-small-en-v1.5"
        )

        print("Model Loaded!")

    def embed(self, text):

     return self.model.encode(
        text,
        normalize_embeddings=True,
        convert_to_numpy=True
    )
    def cosine_similarity(self, vec1, vec2):
        return float(np.dot(vec1, vec2))

if __name__ == "__main__":

    engine = EmbeddingEngine()

    vector = engine.embed(
        "Backend Engineer with Python and SQL"
    )

    print(type(vector))
    print(vector.shape)
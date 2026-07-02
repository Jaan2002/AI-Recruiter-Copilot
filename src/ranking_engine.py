import json
from tqdm import tqdm

from candidate_builder import CandidateBuilder
from embedding_engine import EmbeddingEngine
from scoring_engine import ScoringEngine


class RankingEngine:

    def __init__(self, jd_json, jd_text):

        self.embedder = EmbeddingEngine()
        self.scorer = ScoringEngine(jd_json)

        self.jd_embedding = self.embedder.embed(jd_text)

    def rank(
        self,
        path,
        batch_size=256,
        max_candidates=None
    ):

        results = []

        batch_candidates = []
        batch_texts = []

        processed = 0

        print("Ranking candidates...")

        with open(path, "r", encoding="utf8") as f:

            for line in tqdm(f):

                if max_candidates and processed >= max_candidates:
                    break

                candidate = json.loads(line)

                builder = CandidateBuilder(candidate)

                candidate_text = builder.get_candidate_text()

                batch_candidates.append(candidate)
                batch_texts.append(candidate_text)

                processed += 1

                if len(batch_candidates) == batch_size:

                    self.process_batch(
                        batch_candidates,
                        batch_texts,
                        results
                    )

                    batch_candidates = []
                    batch_texts = []

            # Process remaining candidates

            if batch_candidates:

                self.process_batch(
                    batch_candidates,
                    batch_texts,
                    results
                )

        results.sort(
            key=lambda x: x["final"],
            reverse=True
        )

        return results

    def process_batch(
        self,
        candidates,
        texts,
        results
    ):

        embeddings = self.embedder.model.encode(
    texts,
    batch_size=64,
    normalize_embeddings=True,
    show_progress_bar=False,
    convert_to_numpy=True
)

        for candidate, emb in zip(candidates, embeddings):

            semantic = (
                self.embedder.cosine_similarity(
                    self.jd_embedding,
                    emb
                )
                * 100
            )

            score = self.scorer.calculate_final_score(
                semantic,
                candidate
            )

            results.append({
    "candidate_id": candidate["candidate_id"],
    "title": candidate["profile"]["current_title"],
    "experience_years": candidate["profile"]["years_of_experience"],
    **score
})
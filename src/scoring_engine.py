import re

class ScoringEngine:

    def __init__(self, jd_json):
        self.jd = jd_json

    def calculate_skill_score(self, candidate):

        JD_KEYWORDS = [
            "python",
            "llm",
            "nlp",
            "retrieval",
            "embedding",
            "embeddings",
            "vector",
            "faiss",
            "pinecone",
            "qdrant",
            "milvus",
            "elasticsearch",
            "ranking",
            "search",
            "recommendation",
            "fine-tuning",
            "lora",
            "qlora",
            "peft",
            "xgboost"
        ]

        candidate_skills = {
            skill["name"].lower()
            for skill in candidate["skills"]
        }

        matched = 0

        for keyword in JD_KEYWORDS:
            for skill in candidate_skills:
                if keyword in skill or skill in keyword:
                    matched += 1
                    break

        return round((matched / len(JD_KEYWORDS)) * 100, 2)

    def calculate_experience_score(self, candidate):

        exp = candidate["profile"]["years_of_experience"]
        exp_text = self.jd["experience"]

        nums = re.findall(r"\d+", exp_text)

        if not nums:
            return 100

        required = int(nums[0])

        return round(min(exp / required, 1.0) * 100, 2)

    def calculate_behavior_score(self, candidate):

        s = candidate["redrob_signals"]

        score = 0

        score += s["github_activity_score"]
        score += s["profile_completeness_score"] / 10
        score += s["interview_completion_rate"] * 10
        score += s["offer_acceptance_rate"] * 10

        if s.get("open_to_work_flag"):
            score += 10

        return round(min(score, 100), 2)

    def calculate_final_score(self, semantic_score, candidate):

        skill = self.calculate_skill_score(candidate)
        exp = self.calculate_experience_score(candidate)
        behavior = self.calculate_behavior_score(candidate)

        final = (
            semantic_score * 0.35 +
            skill * 0.40 +
            exp * 0.15 +
            behavior * 0.10
        )

        return {
            "semantic": round(semantic_score, 2),
            "skill": skill,
            "experience": exp,
            "behavior": behavior,
            "final": round(final, 2)
        }
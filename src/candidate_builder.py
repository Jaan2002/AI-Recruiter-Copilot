import json

class CandidateBuilder:

    def __init__(self, candidate):
        self.candidate = candidate

    def get_candidate_text(self):

        profile = self.candidate["profile"]
        text = []

        text.append(f"Current Role: {profile.get('current_title', '')}")
        text.append(f"Headline: {profile.get('headline', '')}")
        text.append(f"Experience: {profile.get('years_of_experience', 0)} years")
        text.append(f"Summary: {profile.get('summary', '')}")

        skills = self.candidate.get("skills", [])
        skill_names = [s["name"] for s in skills]
        text.append("Skills: " + ", ".join(skill_names))

        career = self.candidate.get("career_history", [])
        for job in career:
            text.append(f"{job.get('title','')} at {job.get('company','')}")
            text.append(job.get("description",""))

        education = self.candidate.get("education", [])
        for edu in education:
            text.append(
                f"{edu.get('degree','')} in {edu.get('field_of_study','')} from {edu.get('institution','')}"
            )

        return "\n".join(text)


# Testing

if __name__ == "__main__":

    with open("data/candidates.jsonl", "r", encoding="utf-8") as f:

        candidate = json.loads(f.readline())

    builder = CandidateBuilder(candidate)

    print(builder.get_candidate_text())
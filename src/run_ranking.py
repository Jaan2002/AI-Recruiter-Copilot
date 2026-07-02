import csv
import os
from jd_parser import read_job_description, parse_job_description
from ranking_engine import RankingEngine

jd_text = read_job_description("data/job_description.docx")
jd_json = parse_job_description(jd_text)

engine = RankingEngine(jd_json, jd_text)

results = engine.rank(
    "data/candidates.jsonl",
    batch_size=256,
)

results = results[:100]

max_score = max(r["final"] for r in results)

submission = []

for rank, candidate in enumerate(results, start=1):

    normalized_score = round(candidate["final"] / max_score, 3)

    experience = candidate["experience_years"]
    title = candidate["title"]

    skill_level = (
        "strong" if candidate["skill"] >= 60 else
        "good" if candidate["skill"] >= 30 else
        "basic"
    )

    behavior_level = (
        "excellent" if candidate["behavior"] >= 80 else
        "good" if candidate["behavior"] >= 60 else
        "moderate"
    )

    reasoning = (
        f"{title} with {experience:.1f} years of experience. "
        f"Strong semantic alignment ({candidate['semantic']:.1f}%), "
        f"{skill_level} AI/ML skill match, "
        f"{behavior_level} recruiter signals, "
        f"making the candidate a good fit for the role."
    )

    submission.append({
        "candidate_id": candidate["candidate_id"],
        "rank": rank,
        "score": normalized_score,
        "reasoning": reasoning
    })
os.makedirs("output", exist_ok=True)
with open("output/submission.csv", "w", newline="", encoding="utf-8") as f:

    writer = csv.DictWriter(
        f,
        fieldnames=[
            "candidate_id",
            "rank",
            "score",
            "reasoning"
        ]
    )

    writer.writeheader()
    writer.writerows(submission)

print("submission.csv generated successfully!")

print("\nTop 5 Candidates:\n")

for row in submission[:5]:
    print(row)
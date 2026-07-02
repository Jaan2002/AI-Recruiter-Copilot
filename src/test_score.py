import json

from jd_parser import (
    read_job_description,
    parse_job_description
)

from scoring_engine import ScoringEngine


with open("data/candidates.jsonl","r",encoding="utf8") as f:

    candidate = json.loads(f.readline())

jd = read_job_description("data/job_description.docx")

jd_json = parse_job_description(jd)

engine = ScoringEngine(jd_json)

result = engine.calculate_final_score(

    semantic_score=85,

    candidate=candidate

)

print(result)
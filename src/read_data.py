import json
from pprint import pprint

file_path = "data/candidates.jsonl"

with open(file_path, "r", encoding="utf-8") as file:
    candidate = json.loads(file.readline())

print("="*80)
print("PROFILE")
pprint(candidate["profile"])

print("\n" + "="*80)
print("CAREER HISTORY")
pprint(candidate["career_history"][0] if candidate["career_history"] else "No Data")

print("\n" + "="*80)
print("EDUCATION")
pprint(candidate["education"][0] if candidate["education"] else "No Data")

print("\n" + "="*80)
print("SKILLS")
pprint(candidate["skills"][:10])

print("\n" + "="*80)
print("CERTIFICATIONS")
pprint(candidate["certifications"][:5])

print("\n" + "="*80)
print("LANGUAGES")
pprint(candidate["languages"])

print("\n" + "="*80)
print("REDROB SIGNALS")
pprint(candidate["redrob_signals"])
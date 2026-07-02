# AI Recruiter Copilot

**An AI-powered candidate ranking system that understands candidates beyond keyword matching using Large Language Models, semantic embeddings, and hybrid scoring.**

---

## Overview

Recruiters often screen hundreds of profiles using Applicant Tracking Systems (ATS) that primarily rely on keyword matching. As a result, qualified candidates with relevant experience but different wording are frequently overlooked.

AI Recruiter Copilot addresses this challenge by combining semantic search, Large Language Models (LLMs), and a hybrid ranking engine to evaluate candidates based on contextual understanding rather than exact keyword overlap.

The system automatically parses a job description, extracts hiring requirements, computes semantic similarity between the role and candidate profiles, evaluates skills, experience, and behavioral signals, and produces an explainable ranked shortlist.

---

## Key Features

* LLM-powered Job Description Parsing using Google Gemini
* Semantic Candidate Matching using Sentence Transformers
* Hybrid AI Ranking Engine
* Explainable Candidate Recommendations
* Behavioral Signal Analysis
* Batch Candidate Processing
* Automated Submission CSV Generation
* Modular and Scalable Architecture

---

## System Architecture

```
                    Job Description (.docx)
                              │
                              ▼
                    Gemini LLM Parser
                              │
                     Structured Job JSON
                              │
                              ▼
                  Embedding Engine (BGE Small)
                              │
             ┌────────────────┴────────────────┐
             │                                 │
             ▼                                 ▼
      Job Embedding                  Candidate Dataset
                                               │
                                               ▼
                                       Candidate Builder
                                               │
                                               ▼
                                      Candidate Embeddings
                                               │
                                               ▼
                                   Semantic Similarity
                                               │
                                               ▼
                                     Hybrid Scoring Engine
                         ┌────────────────────────────────────┐
                         │ Semantic Similarity                │
                         │ Skill Matching                     │
                         │ Experience Evaluation              │
                         │ Behavioral Signal Analysis         │
                         └────────────────────────────────────┘
                                               │
                                               ▼
                                      Candidate Ranking
                                               │
                                               ▼
                                   Explainable AI Reasoning
                                               │
                                               ▼
                                   output/submission.csv
```

---

## Technology Stack

| Technology             | Purpose                       |
| ---------------------- | ----------------------------- |
| Python                 | Core Development              |
| Google Gemini API      | Job Description Understanding |
| Sentence Transformers  | Semantic Embeddings           |
| BAAI/bge-small-en-v1.5 | Embedding Model               |
| NumPy                  | Similarity Computation        |
| python-docx            | DOCX Parsing                  |
| tqdm                   | Batch Processing              |

---

## Project Structure

```
AI-Recruiter-Copilot/

├── data/
│   ├── job_description.docx
│   └── candidates.jsonl
│
├── output/
│   └── submission.csv
│
├── src/
│   ├── candidate_builder.py
│   ├── embedding_engine.py
│   ├── jd_parser.py
│   ├── ranking_engine.py
│   ├── scoring_engine.py
│   └── run_ranking.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Workflow

1. Read the Job Description from a DOCX file.
2. Parse the job description using Google Gemini to identify required skills, experience, and behavioral expectations.
3. Generate semantic embeddings for the job description.
4. Build a unified representation of each candidate using profile information, career history, skills, education, certifications, languages, and recruiter signals.
5. Generate semantic embeddings for every candidate profile.
6. Compute cosine similarity between the job description and candidate embeddings.
7. Apply a hybrid scoring framework combining semantic similarity, skill matching, experience, and behavioral indicators.
8. Rank all candidates based on the final score.
9. Generate human-readable reasoning for every recommendation.
10. Export the ranked shortlist to `output/submission.csv`.

---

## Hybrid Scoring Strategy

| Component           | Weight |
| ------------------- | ------ |
| Semantic Similarity | 35%    |
| Skill Match         | 40%    |
| Experience          | 15%    |
| Behavioral Signals  | 10%    |

---

## Explainable AI

Unlike conventional ranking systems, AI Recruiter Copilot provides a justification for every recommendation.

Example:

```
Backend Engineer with 6.9 years of experience.

Strong semantic alignment (72.3%), good AI/ML skill match,
moderate recruiter signals, making the candidate a strong
fit for the role.
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python src/run_ranking.py
```

The ranked output will be generated at:

```
output/submission.csv
```

---

## Future Enhancements

* Vector Database Integration (FAISS, Qdrant)
* Learning-to-Rank Models (LambdaMART, XGBoost)
* Recruiter Feedback Loop
* Retrieval-Augmented Generation (RAG)
* Resume Upload Interface
* ATS Integration
* Continuous Candidate Learning
* Multi-Agent Recruitment Assistant

---

## Dataset

The candidate dataset (`candidates.jsonl`) is not included in this repository due to GitHub's file size limitations.

Place the dataset inside the `data/` directory before running the project.

---

## Project Highlights

* Semantic understanding instead of keyword matching
* LLM-assisted job requirement extraction
* Explainable candidate recommendations
* Hybrid ranking framework
* Production-inspired modular architecture
* Efficient batch embedding pipeline

---

## Engineer

**Jaanvi Kapoor**

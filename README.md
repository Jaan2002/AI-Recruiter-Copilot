# AI Recruiter Copilot

## Overview

AI Recruiter Copilot ranks candidates using semantic understanding instead of keyword matching.

## Features

- Gemini-powered Job Description parsing
- Semantic candidate matching using BGE embeddings
- Hybrid scoring engine
    - Semantic Match
    - Skill Match
    - Experience Match
    - Behavioral Signals
- Explainable AI reasoning
- Ranked CSV generation

## Tech Stack

- Python
- Sentence Transformers
- Gemini API
- NumPy
- tqdm

## Run

pip install -r requirements.txt

python src/run_ranking.py
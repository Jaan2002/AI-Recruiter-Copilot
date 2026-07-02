from docx import Document
from google import genai
from dotenv import load_dotenv
import json
import os

# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Read Job Description
def read_job_description(path):
    doc = Document(path)
    text = "\n".join(para.text for para in doc.paragraphs)
    return text


# Parse JD using Gemini

def parse_job_description(jd_text):

    prompt = f"""
    You are an expert technical recruiter.

    Analyze the following Job Description.

    Return ONLY valid JSON.

    {{
      "role":"",
      "must_have":[],
      "preferred":[],
      "experience":"",
      "behavioral_traits":[]
    }}

    Job Description:

    {jd_text}
    """
    try:
        response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
       )

    # Remove markdown code fences
        cleaned = (
          response.text
           .replace("```json", "")
           .replace("```", "")
           .strip()
      )

        return json.loads(cleaned)
    except Exception as e:
        print("Gemini failed, using fallback parser")

        # SIMPLE FALLBACK STRUCTURE
        return {
            "must_have": [],
            "experience": "0 years",
            "skills": []
        }



# Test
if __name__ == "__main__":

    jd = read_job_description("data/job_description.docx")

    result = parse_job_description(jd)

    print(result)
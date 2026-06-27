import os
import json
import google.generativeai as genai
from dotenv import load_dotenv
from prompts import (
    question_prompt,
    evaluation_prompt,
    preparation_prompt
)

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(os.getenv("MODEL"))


# -------------------------------
# Generate Interview Questions
# -------------------------------

# -------------------------------
# Generate Interview Questions
# -------------------------------

def generate_questions(domain, difficulty, interview_type):

    try:

        response = model.generate_content(

            question_prompt(
                domain,
                difficulty,
                interview_type
            )

        )

        content = response.text.strip()

        content = content.replace("```json", "")
        content = content.replace("```", "")
        content = content.strip()

        return json.loads(content)

    except Exception as e:

        return {
            "error": str(e)
        }
# -------------------------------
# Evaluate Interview
# -------------------------------

def evaluate_answers(questions, answers):

    try:

        response = model.generate_content(
            evaluation_prompt(
                questions,
                answers
            )
        )

        content = response.text.strip()

        content = content.replace("```json", "")
        content = content.replace("```", "")
        content = content.strip()

        try:
            return json.loads(content)
        except:
            return {
                "error": "Gemini returned invalid JSON.",
                "raw": content
            }

    except Exception as e:

        return {
            "error": str(e)
        }


# -------------------------------
# Generate Preparation Roadmap
# -------------------------------

def generate_preparation_plan(domain, level, interview_type):

    try:

        response = model.generate_content(

            preparation_prompt(
                domain,
                level,
                interview_type
            )

        )

        return response.text

    except Exception as e:

        return f"❌ Error:\n\n{str(e)}"
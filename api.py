import os
import json
import google.generativeai as genai
import re
from dotenv import load_dotenv
from prompts import question_prompt, evaluation_prompt

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(os.getenv("MODEL"))


# ---------------------------------------------
# Helper Function
# ---------------------------------------------


def clean_json(text):
    """
    Extract JSON even if Gemini adds extra text.
    """

    text = text.replace("```json", "")
    text = text.replace("```", "").strip()

    match = re.search(r'(\[.*\]|\{.*\})', text, re.DOTALL)

    if match:
        return match.group(1)

    return text

# ---------------------------------------------
# Generate Questions
# ---------------------------------------------

def generate_questions(domain, difficulty):

    try:

        response = model.generate_content(
            question_prompt(domain, difficulty)
        )

        content = clean_json(response.text)

        return json.loads(content)

    except Exception as e:

        return {
            "error": str(e)
        }


# ---------------------------------------------
# Evaluate Answers
# ---------------------------------------------

def evaluate_answers(questions, answers):

    try:

        response = model.generate_content(
            evaluation_prompt(
                questions,
                answers
            )
        )

        content = clean_json(response.text)

        report = json.loads(content)

        scores = [q["score"] for q in report["questions"]]

        report["overall_score"] = round(
            sum(scores) / len(scores),
            2
        )

        return report

    except Exception as e:

        return {
            "questions": [],
            "strengths": [],
            "weaknesses": [],
            "overall_score": 0,
            "error": str(e)
        }
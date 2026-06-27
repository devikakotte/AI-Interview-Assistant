import json

# -----------------------------------------
# Generate Questions Prompt
# -----------------------------------------

def question_prompt(domain, difficulty):

    return f"""
You are an expert technical interviewer.

Generate exactly 10 interview questions.

Domain: {domain}

Difficulty: {difficulty}

Rules:
- Return ONLY JSON.
- No markdown.
- No explanation.
- No extra text.

Output format:

[
    {{
        "id":1,
        "question":"Question text"
    }},
    {{
        "id":2,
        "question":"Question text"
    }}
]
"""


# -----------------------------------------
# Evaluation Prompt
# -----------------------------------------

def evaluation_prompt(questions, answers):

    qa = []

    for i, q in enumerate(questions):

        qa.append({
            "question": q["question"],
            "answer": answers.get(i, "")
        })

    return f"""
You are a senior software engineer interviewing a candidate.

Evaluate every answer.

Scoring:

10 = Excellent

8-9 = Very Good

6-7 = Good

4-5 = Average

2-3 = Poor

0-1 = Incorrect / Empty

Rules:

• Feedback must be under 20 words.
• Be strict but fair.
• Return ONLY JSON.
• Do not use markdown.
• Do not explain anything outside JSON.

Return EXACTLY this format:

{{
    "questions":[
        {{
            "score":8,
            "feedback":"Good answer."
        }}
    ],

    "strengths":[
        "Strength 1",
        "Strength 2",
        "Strength 3"
    ],

    "weaknesses":[
        "Weakness 1",
        "Weakness 2",
        "Weakness 3"
    ]
}}

Candidate Answers:

{json.dumps(qa, indent=2)}
"""
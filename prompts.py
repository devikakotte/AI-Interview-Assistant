def question_prompt(domain, difficulty, interview_type):

    return f"""
You are a senior interviewer at Google, Microsoft and Amazon.

Generate EXACTLY 10 interview questions.

Domain:
{domain}

Difficulty:
{difficulty}

Interview Type:
{interview_type}

Rules:

If Interview Type is:

1. Technical Interview
- Ask theoretical questions.
- Concepts.
- OOP.
- Language fundamentals.
- APIs.
- Frameworks.

2. Coding Assessment
- Ask coding problems ONLY.
- Frequently asked coding interview questions.
- Arrays
- Strings
- HashMaps
- Sliding Window
- Recursion
- Stack
- Queue
- Linked List
- Trees
- Dynamic Programming (easy/intermediate)

Do NOT ask theory.

3. HR Interview
Ask behavioural questions like

- Tell me about yourself
- Why should we hire you?
- Biggest weakness
- Leadership
- Teamwork
- Conflict
- Failure
- Career goals

No technical questions.

4. System Design

Generate beginner/intermediate system design questions related to the selected domain.

5. Mixed Interview

Mix HR, Coding and Technical questions.

Return ONLY JSON.

Example:

[
  {{
      "id":1,
      "question":"Explain Python decorators."
  }},
  {{
      "id":2,
      "question":"Reverse a linked list."
  }}
]
"""


def evaluation_prompt(questions, answers):

    prompt = """
You are an experienced technical interviewer.

Evaluate the candidate's answers.

Return ONLY valid JSON.

Format:

{
    "overall_score":85,
    "questions":[
        {
            "question":"Question",
            "score":8,
            "feedback":"Feedback"
        }
    ],
    "strengths":[
        "Strength 1",
        "Strength 2"
    ],
    "weaknesses":[
        "Weakness 1",
        "Weakness 2"
    ],
    "topics_to_improve":[
        "Topic 1",
        "Topic 2"
    ]
}

Questions and Answers

"""

    for i, q in enumerate(questions):

        prompt += f"""

Question {i+1}

{q["question"]}

Candidate Answer

{answers.get(i, "No Answer")}

"""

    return prompt


def preparation_prompt(domain, level, interview_type):

    return f"""
You are an experienced FAANG interview mentor.

Create a complete interview preparation roadmap.

Domain:
{domain}

Experience:
{level}

Interview Type:
{interview_type}

Include the following sections:

# Topics to Study

# Coding Practice

# Important Concepts

# Mini Projects

# Interview Tips

# Free Resources

# 7-Day Study Plan

Return the answer in clean Markdown format.
"""
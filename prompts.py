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
You are an expert technical mentor from Google, Amazon and Microsoft.

Create a COMPLETE interview preparation roadmap.

Domain: {domain}

Candidate Level: {level}

Interview Type: {interview_type}

--------------------------------------------

If Interview Type is Technical Interview:

For every topic provide:

- Topic Name
- Why this topic is important
- Key concepts to study
- Frequently asked interview questions
- Common mistakes

--------------------------------------------

If Interview Type is Coding Assessment:

Generate 10 important coding topics.

For EVERY topic provide:

1. Topic Name

2. Why it is important

3. A small code snippet (10-15 lines maximum).

IMPORTANT:
The code snippet MUST be written in the selected domain/language.

Examples:
- If domain is Python → use Python.
- If domain is Java → use Java.
- If domain is JavaScript → use JavaScript.
- If domain is React → use React JSX.
- If domain is NodeJS → use JavaScript (Node.js).
- If domain is SQL → use SQL queries.
- If domain is Web Development → use HTML/CSS/JavaScript depending on the topic.
- If domain is Data Science → use Python with pandas/numpy/sklearn where appropriate.
- If domain is Machine Learning → use Python with scikit-learn or TensorFlow where appropriate.

Do NOT use Python for every domain.

4. 2-3 famous interview questions with difficulty labels:

🟢 Easy

🟡 Medium

🔴 Hard

5. Common mistakes

6. Tips to solve faster

Example format:

# Arrays

Why learn?

Arrays are one of the most common data structures asked in coding interviews.

Example Code:

nums = [1, 2, 3]

for num in nums:
    print(num)

Practice Problems

🟢 Two Sum

🟢 Move Zeroes

🟡 Best Time to Buy and Sell Stock

Common Mistakes

- Forgetting edge cases
- Index out of bounds

Tips

- Dry run on paper
- Think about time complexity

--------------------------------------------

If Interview Type is HR Interview:

Generate 10 HR interview questions.

For every question provide:

- Why interviewer asks it
- How to answer
- Sample answer
- Mistakes to avoid

--------------------------------------------

If Interview Type is System Design:

Generate a roadmap containing:

- Important concepts
- Architecture explanation
- Real-world examples
- Frequently asked interview questions
- Beginner resources

--------------------------------------------

If Interview Type is Mixed Interview:

Include all of these:

- Technical topics
- Coding topics with small code snippets
- HR preparation
- System Design basics

Use proper Markdown headings, bullet points and spacing.

Make the roadmap detailed, practical and interview-focused.
"""
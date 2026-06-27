import streamlit as st
from api import generate_questions, evaluate_answers

st.set_page_config(
    page_title="AI Interview Assistant",
    page_icon="🤖",
    layout="wide"
)

# -----------------------
# Session State
# -----------------------

defaults = {
    "questions": [],
    "answers": {},
    "current": 0,
    "report": None,
    "interview_completed": False,
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# -----------------------
# Header
# -----------------------

st.title("🤖 AI Interview Preparation Assistant")
st.caption("Practice technical interviews powered by AI")

# -----------------------
# Sidebar
# -----------------------

with st.sidebar:

    st.header("Interview Settings")

    domain = st.selectbox(
        "Choose Domain",
        [
            "Python",
            "Java",
            "Web Development",
            "Data Science",
            "Machine Learning",
            "SQL",
            "JavaScript",
            "React",
            "NodeJS"
        ]
    )

    difficulty = st.selectbox(
        "Difficulty",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    if st.button("🚀 Start New Interview", use_container_width=True):

        with st.spinner("Generating Interview..."):

            result = generate_questions(domain, difficulty)

        if isinstance(result, dict) and "error" in result:

            st.error(result["error"])

        else:

            st.session_state.questions = result
            st.session_state.answers = {}
            st.session_state.current = 0
            st.session_state.report = None
            st.session_state.interview_completed = False

            st.rerun()

# -----------------------
# No Questions
# -----------------------

if not st.session_state.questions:

    st.info("👈 Select a domain and click **Start New Interview**.")
    st.stop()

# -----------------------
# Progress
# -----------------------

questions = st.session_state.questions
index = st.session_state.current
total = len(questions)

st.progress((index + 1) / total)

st.write(f"### Question {index+1} of {total}")

st.divider()

# -----------------------
# Question
# -----------------------

question = questions[index]["question"]

st.markdown(f"### {question}")

answer = st.text_area(
    "Your Answer",
    value=st.session_state.answers.get(index, ""),
    height=220,
    placeholder="Type your answer here..."
)

st.session_state.answers[index] = answer

# -----------------------
# Navigation
# -----------------------

left, center, right = st.columns([1, 3, 1])

with left:

    if st.button("⬅ Previous", use_container_width=True):

        if index > 0:
            st.session_state.current -= 1
            st.rerun()

with right:

    if index < total - 1:

        if st.button("Next ➡", use_container_width=True):

            st.session_state.current += 1
            st.rerun()

    else:

        if st.button("✅ Finish Interview", use_container_width=True):

            with st.spinner("AI is evaluating your interview..."):

                report = evaluate_answers(
                    st.session_state.questions,
                    st.session_state.answers
                )
                st.write(report)

            st.session_state.report = report
            st.session_state.interview_completed = True
            st.rerun()

# -----------------------
# Report
# -----------------------

if st.session_state.interview_completed:

    report = st.session_state.report

    if "error" in report:

        st.error(report["error"])

        st.stop()

    if len(report["questions"]) == 0:

        st.error("AI did not return evaluation.")

        st.stop()

    scores = [q["score"] for q in report["questions"]]

    overall = round(sum(scores) / len(scores), 2)

    st.divider()

    st.success("🎉 Interview Completed!")

    c1, c2 = st.columns(2)

    with c1:
        st.metric("Overall Score", f"{overall}/10")

    with c2:
        st.metric(
            "Answered",
            f"{len([a for a in st.session_state.answers.values() if a.strip()])}/{total}"
        )

    st.progress(overall / 10)

    st.divider()

    st.subheader("📊 Question-wise Performance")

    for i, item in enumerate(report["questions"]):

        with st.expander(f"Question {i+1}"):

            st.write("**Question**")

            st.write(st.session_state.questions[i]["question"])

            st.write("**Your Answer**")

            ans = st.session_state.answers.get(i, "")

            if ans.strip():
                st.code(ans)
            else:
                st.warning("No Answer")

            st.write(f"### ⭐ Score : {item['score']}/10")

            st.info(item["feedback"])

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("💪 Strengths")

        for s in report["strengths"]:
            st.success(s)

    with col2:

        st.subheader("📚 Weaknesses")

        for w in report["weaknesses"]:
            st.error(w)
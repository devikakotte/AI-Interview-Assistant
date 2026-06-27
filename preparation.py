import streamlit as st
from api import generate_preparation_plan

st.title("📚 Interview Preparation Roadmap")

st.write("Generate a personalized preparation plan before attending your interview.")

domain = st.selectbox(
    "Select Domain",
    [
        "Python",
        "Java",
        "Web Development",
        "AI/ML",
        "Data Science"
    ],
    key="prep_domain"
)

level = st.selectbox(
    "Experience Level",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)

interview = st.selectbox(
    "Interview Type",
    [
        "Technical",
        "HR",
        "System Design",
        "Full Interview"
    ]
)

if st.button("Generate Preparation Plan"):

    with st.spinner("Generating Roadmap..."):

        plan = generate_preparation_plan(
            domain,
            level,
            interview
        )

    st.success("Preparation Plan Generated!")

    st.markdown(plan)
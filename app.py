import streamlit as st
import ollama

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="CareerMate AI",
    page_icon="🎓",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------
st.title("🎓 CareerMate AI")
st.subheader("Personalized Career Guidance & Resume Assistant")

st.write(
    "Get personalized career suggestions, resume improvements, "
    "skill recommendations, and interview preparation using AI."
)

st.divider()

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.header("👤 Your Profile")

    name = st.text_input("Name", placeholder="Enter your name")

    education = st.text_input(
        "Education",
        placeholder="B.Tech CSE"
    )

    skills = st.text_area(
        "Skills",
        placeholder="Python, SQL, HTML, Streamlit"
    )

    interests = st.text_area(
        "Career Interests",
        placeholder="AI, Web Development, Data Science"
    )

    experience = st.text_area(
        "Experience / Projects",
        placeholder="AI Chatbot, Mini RAG, Hostel Management"
    )

    target_role = st.text_input(
        "Target Job Role",
        placeholder="AI Engineer"
    )

# -----------------------------
# Tabs
# -----------------------------
tab1, tab2, tab3, tab4 = st.tabs(
    [
        "🚀 Career Guidance",
        "📄 Resume Assistant",
        "💡 Skill Roadmap",
        "🎤 Interview Preparation"
    ]
)

# -----------------------------
# Ollama Function
# -----------------------------
def ask_ai(prompt):
    try:
        response = ollama.chat(
            model="llama3.2",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e:
        return (
            "❌ Unable to connect to Ollama.\n\n"
            "Please make sure Ollama is installed and running, "
            "and that the model `llama3.2` is available.\n\n"
            f"Error: {e}"
        )


# -----------------------------
# Career Guidance
# -----------------------------
with tab1:
    st.header("🚀 Personalized Career Guidance")

    if st.button("Get Career Guidance", key="career"):
        if not education or not skills or not interests:
            st.warning(
                "Please enter your education, skills, and interests "
                "in the sidebar."
            )
        else:
            with st.spinner("Analyzing your profile..."):

                prompt = f"""
You are CareerMate AI, a professional career counselor.

Student Profile:
Name: {name}
Education: {education}
Skills: {skills}
Interests: {interests}
Experience/Projects: {experience}
Target Role: {target_role}

Provide personalized career guidance.

Include:
1. Suitable career paths
2. Recommended job roles
3. Required skills
4. Skills the student already has
5. Skills they should learn
6. Suggested projects
7. A 3-month learning roadmap
8. Career tips

Give practical and beginner-friendly advice.
"""

                result = ask_ai(prompt)
                st.markdown(result)


# -----------------------------
# Resume Assistant
# -----------------------------
with tab2:
    st.header("📄 Resume Assistant")

    resume = st.text_area(
        "Paste your resume here",
        height=300,
        placeholder="Paste your resume content..."
    )

    if st.button("Improve My Resume", key="resume"):
        if not resume.strip():
            st.warning("Please paste your resume first.")
        else:
            with st.spinner("Improving your resume..."):

                prompt = f"""
You are an expert ATS resume assistant.

Analyze the following resume:

{resume}

Provide:

1. ATS score estimate out of 100
2. Resume strengths
3. Resume weaknesses
4. Missing keywords
5. Grammar improvements
6. Better professional wording
7. Improved summary
8. Improved skills section
9. Improved project descriptions
10. Specific suggestions to make the resume ATS-friendly

Keep the suggestions suitable for a student/fresher.
"""

                result = ask_ai(prompt)
                st.markdown(result)


# -----------------------------
# Skill Roadmap
# -----------------------------
with tab3:
    st.header("💡 Personalized Skill Roadmap")

    if st.button("Generate Skill Roadmap", key="roadmap"):
        if not target_role:
            st.warning("Please enter your target job role in the sidebar.")
        else:
            with st.spinner("Creating your roadmap..."):

                prompt = f"""
Create a personalized learning roadmap.

Education: {education}
Current Skills: {skills}
Interests: {interests}
Target Role: {target_role}
Projects: {experience}

Create a beginner-friendly roadmap containing:

1. Skills to learn first
2. Programming languages
3. Tools and technologies
4. Important concepts
5. Projects to build
6. Free learning recommendations
7. 30-day roadmap
8. 60-day roadmap
9. 90-day roadmap
10. Job preparation tips

Use simple explanations.
"""

                result = ask_ai(prompt)
                st.markdown(result)


# -----------------------------
# Interview Preparation
# -----------------------------
with tab4:
    st.header("🎤 Interview Preparation")

    interview_role = st.text_input(
        "Interview Role",
        value=target_role,
        placeholder="Python Developer"
    )

    if st.button("Generate Interview Questions", key="interview"):
        if not interview_role:
            st.warning("Please enter an interview role.")
        else:
            with st.spinner("Preparing interview questions..."):

                prompt = f"""
You are an expert technical interviewer.

Prepare interview questions for the role:
{interview_role}

Candidate skills:
{skills}

Candidate projects:
{experience}

Generate:

1. 5 HR questions
2. 10 technical questions
3. 5 project-based questions
4. 5 scenario-based questions
5. Short model answers
6. Interview preparation tips

Keep the questions appropriate for a fresher.
"""

                result = ask_ai(prompt)
                st.markdown(result)


# -----------------------------
# Footer
# -----------------------------
st.divider()

st.caption(
    "🎓 CareerMate AI | Personalized Career Guidance & Resume Assistant"
)
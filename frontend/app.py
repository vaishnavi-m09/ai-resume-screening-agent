import streamlit as st
import pandas as pd

from api_client import analyze_resume

st.set_page_config(
    page_title="AI Resume Screening Agent",
    layout="wide"
)

st.title("📄 AI Resume Screening Agent")

st.markdown(
    """
    Upload a resume and compare it against a job description.
    """
)

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)

jd_text = st.text_area(
    "Paste Job Description",
    height=250
)

if st.button("Analyze Resume"):

    if uploaded_file is None:
        st.error("Please upload a resume.")

    elif not jd_text.strip():
        st.error("Please enter a job description.")

    else:

        with st.spinner("Analyzing Resume..."):

            result = analyze_resume(
                uploaded_file,
                jd_text
            )

        score = result["match_score"]

        if score >= 70:
            recommendation = "✅ Strong Fit"

        elif score >= 50:
            recommendation = "🟡 Moderate Fit"

        else:
            recommendation = "🔴 Weak Fit"

        st.success("Analysis Complete")

        st.divider()

        # ========================
        # Summary Metrics
        # ========================

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Match Score",
                f"{score}%"
            )

        with col2:
            st.metric(
                "Skills Found",
                len(result["skills"])
            )

        with col3:
            st.metric(
                "Skill Gaps",
                len(result["skill_gaps"])
            )

        st.progress(score / 100)

        st.subheader("Recommendation")
        st.info(recommendation)

        st.divider()

        # ========================
        # Recruiter Feedback
        # ========================

        feedback = result["feedback"]

        st.subheader("Recruiter Feedback")

        st.metric(
            "Skill Coverage",
            f"{feedback['skill_coverage']}%"
        )

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Matched Skills",
                feedback["matched_skills"]
            )

        with col2:
            st.metric(
                "Missing Skills",
                feedback["missing_skills"]
            )

        col1, col2 = st.columns(2)

        with col1:
            st.markdown(
                f"**Assessment:** "
                f"{feedback['overall_assessment']}"
            )

        with col2:
            st.markdown(
                f"**Recommendation:** "
                f"{feedback['recommendation']}"
            )

        st.divider()

        # ========================
        # Strengths
        # ========================

        st.subheader("Strengths")

        for strength in feedback["strengths"]:
            st.success(strength)

        # ========================
        # Areas of Concern
        # ========================

        st.subheader("Areas of Concern")

        for weakness in feedback["weaknesses"]:
            st.warning(weakness)

        st.divider()

        # ========================
        # Skills
        # ========================

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("Skills Found")

            skills_df = pd.DataFrame(
                result["skills"],
                columns=["Skill"]
            )

            st.dataframe(
                skills_df,
                use_container_width=True
            )

        with col2:

            st.subheader("Skill Gaps")

            gaps_df = pd.DataFrame(
                result["skill_gaps"],
                columns=["Missing Skill"]
            )

            st.dataframe(
                gaps_df,
                use_container_width=True
            )

        st.divider()

        # ========================
        # Explanation
        # ========================

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("Matched Skills")

            matched_df = pd.DataFrame(
                result["explanation"]["matched"],
                columns=["Matched Skill"]
            )

            st.dataframe(
                matched_df,
                use_container_width=True
            )

        with col2:

            st.subheader("Missing Skills")

            missing_df = pd.DataFrame(
                result["explanation"]["missing"],
                columns=["Missing Skill"]
            )

            st.dataframe(
                missing_df,
                use_container_width=True
            )

        st.divider()

        # ========================
        # Interview Questions
        # ========================

        st.subheader("Suggested Interview Questions")

        questions_df = pd.DataFrame(
            result["interview_questions"],
            columns=["Question"]
        )

        st.dataframe(
            questions_df,
            use_container_width=True
        )
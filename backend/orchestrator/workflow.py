from backend.agents.skill_agent import SkillAgent
from backend.agents.matching_agent import MatchingAgent
from backend.agents.gap_agent import GapAgent
from backend.agents.explanation_agent import ExplanationAgent
from backend.agents.interview_agent import InterviewAgent
from backend.agents.feedback_agent import FeedbackAgent


class RecruitmentWorkflow:

    def __init__(self):

        self.skill_agent = SkillAgent()

        self.matching_agent = MatchingAgent()

        self.gap_agent = GapAgent()

        self.explanation_agent = ExplanationAgent()

        self.interview_agent = InterviewAgent()

        self.feedback_agent = FeedbackAgent()

    def run(
        self,
        resume_text,
        jd_text,
        jd_skills
    ):

        # ========================
        # Extract Skills
        # ========================

        candidate_skills = (
            self.skill_agent.extract_skills(
                resume_text
            )
        )

        # ========================
        # Find Skill Gaps
        # ========================

        skill_gaps = (
            self.gap_agent.find_skill_gaps(
                candidate_skills,
                jd_skills
            )
        )

        # ========================
        # Explain Match
        # ========================

        explanation = (
            self.explanation_agent.explain(
                candidate_skills,
                jd_skills
            )
        )

        # ========================
        # Calculate Match Score
        # ========================

        match_score = (
            self.matching_agent.calculate_match_score(
                resume_text,
                jd_text,
                explanation["matched"],
                explanation["missing"]
            )
        )

        # ========================
        # Generate Feedback
        # ========================

        feedback = (
            self.feedback_agent.generate_feedback(
                match_score,
                explanation["matched"],
                explanation["missing"]
            )
        )

        # ========================
        # Generate Interview Questions
        # ========================

        interview_questions = (
            self.interview_agent.generate_questions(
                candidate_skills
            )
        )

        # ========================
        # Recommendation
        # ========================

        if match_score >= 70:

            recommendation = "Strong Fit"

        elif match_score >= 50:

            recommendation = "Moderate Fit"

        else:

            recommendation = "Weak Fit"

        # ========================
        # Final Response
        # ========================

        return {
            "skills": candidate_skills,
            "match_score": match_score,
            "recommendation": recommendation,
            "skill_gaps": skill_gaps,
            "explanation": explanation,
            "feedback": feedback,
            "interview_questions": interview_questions
        }
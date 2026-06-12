from backend.agents.skill_agent import SkillAgent
from backend.agents.matching_agent import MatchingAgent
from backend.agents.gap_agent import GapAgent
from backend.agents.explanation_agent import ExplanationAgent
from backend.agents.interview_agent import InterviewAgent


class RecruitmentWorkflow:

    def __init__(self):

        self.skill_agent = SkillAgent()

        self.matching_agent = MatchingAgent()

        self.gap_agent = GapAgent()

        self.explanation_agent = ExplanationAgent()

        self.interview_agent = InterviewAgent()

    def run(
        self,
        resume_text,
        jd_text,
        jd_skills
    ):

        candidate_skills = (
            self.skill_agent.extract_skills(
                resume_text
            )
        )

        match_score = (
            self.matching_agent.calculate_match_score(
                resume_text,
                jd_text
            )
        )

        skill_gaps = (
            self.gap_agent.find_skill_gaps(
                candidate_skills,
                jd_skills
            )
        )

        explanation = (
            self.explanation_agent.explain(
                candidate_skills,
                jd_skills
            )
        )

        interview_questions = (
            self.interview_agent.generate_questions(
                candidate_skills
            )
        )
        if match_score >= 80:
            recommendation = "Strong Fit"

        elif match_score >= 60:
            recommendation = "Moderate Fit"

        else:
            recommendation = "Weak Fit"
        return {
            "skills": candidate_skills,
            "match_score": match_score,
            "recommendation": recommendation,
            "skill_gaps": skill_gaps,
            "explanation": explanation,
            "interview_questions": interview_questions
        }
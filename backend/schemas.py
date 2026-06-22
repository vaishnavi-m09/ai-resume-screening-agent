from pydantic import BaseModel


class AnalyzeRequest(BaseModel):

    resume_text: str

    jd_text: str

class AnalyzeResponse(BaseModel):

    skills: list

    match_score: float

    recommendation: str

    skill_gaps: list

    explanation: dict

    feedback: dict

    interview_questions: list
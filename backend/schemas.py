from pydantic import BaseModel


class AnalyzeRequest(BaseModel):

    resume_text: str

    jd_text: str

class AnalyzeResponse(BaseModel):

    skills: list

    match_score: float

    skill_gaps: list

    explanation: dict

    interview_questions: list
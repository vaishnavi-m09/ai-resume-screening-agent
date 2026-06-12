from fastapi import APIRouter

from backend.schemas import (
    AnalyzeRequest
)

from backend.services.recruitment_service import (
    RecruitmentService
)

router = APIRouter()

service = RecruitmentService()


@router.post("/analyze")
def analyze_candidate(
    request: AnalyzeRequest
):

    result = service.analyze_resume(
        request.resume_text,
        request.jd_text
    )

    return result
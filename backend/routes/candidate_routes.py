from fastapi import APIRouter

from backend.schemas import (
    AnalyzeRequest,
    AnalyzeResponse
)

from backend.services.recruitment_service import (
    RecruitmentService
)

router = APIRouter()

service = RecruitmentService()


@router.post("/analyze", response_model=AnalyzeResponse)
def analyze_candidate(
    request: AnalyzeRequest
):

    result = service.analyze_resume(
        request.resume_text,
        request.jd_text
    )

    return result
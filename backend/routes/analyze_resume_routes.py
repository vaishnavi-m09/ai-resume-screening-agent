from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Form
)

import os
import shutil

from backend.agents.parser_agent import (
    ParserAgent
)

from backend.services.recruitment_service import (
    RecruitmentService
)

router = APIRouter()

parser_agent = ParserAgent()

service = RecruitmentService()

UPLOAD_DIR = "uploads/resumes"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)


@router.post("/analyze_resume")
async def analyze_resume(
    file: UploadFile = File(...),
    jd_text: str = Form(...)
):

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(
        file_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    resume_text = parser_agent.parse(
        file_path
    )

    result = service.analyze_resume(
        resume_text,
        jd_text
    )

    return result
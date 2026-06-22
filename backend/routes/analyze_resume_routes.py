from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Form,
    HTTPException
)

import os
import shutil
import traceback

from backend.agents.parser_agent import (
    ParserAgent
)

from backend.services.recruitment_service import (
    RecruitmentService
)

from backend.schemas import AnalyzeResponse

router = APIRouter()

parser_agent = ParserAgent()

service = RecruitmentService()

UPLOAD_DIR = "uploads/resumes"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)


@router.post("/analyze_resume", response_model=AnalyzeResponse)
async def analyze_resume(
    file: UploadFile = File(...),
    jd_text: str = Form(...)
):

    try:

        file_path = os.path.join(
            UPLOAD_DIR,
            file.filename or "resume.pdf"
        )

        with open(
            file_path,
            "wb"
        ) as buffer:

            shutil.copyfileobj(
                file.file,
                buffer
            )

        print("FILE SAVED")

        resume_text = parser_agent.parse(
            file_path
        )

        print("RESUME PARSED")
        print(type(resume_text))

        result = service.analyze_resume(
            resume_text,
            jd_text
        )

        print("ANALYSIS COMPLETE")

        return result

    except HTTPException as he:
        raise he

    except Exception as e:

        print("\n========== ERROR ==========")
        traceback.print_exc()
        print("===========================\n")

        raise HTTPException(
            status_code=500,
            detail=f"Analysis failed: {str(e)}"
        )
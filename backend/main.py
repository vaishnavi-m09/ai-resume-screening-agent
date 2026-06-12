from fastapi import FastAPI

from backend.routes.health_routes import (
    router as health_router
)

from backend.routes.candidate_routes import (
    router as candidate_router
)

app = FastAPI(
    title="AI Resume Screening Agent"
)

app.include_router(
    health_router
)

app.include_router(
    candidate_router
)
from backend.routes.upload_routes import (
    router as upload_router
)
app.include_router(
    upload_router
)
from backend.routes.analyze_resume_routes import (
    router as analyze_resume_router
)
app.include_router(
    analyze_resume_router
)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routes.health_routes import router as health_router
from backend.routes.candidate_routes import router as candidate_router
from backend.routes.upload_routes import router as upload_router
from backend.routes.analyze_resume_routes import router as analyze_resume_router

app = FastAPI(
    title="AI Resume Screening Agent",
    description="Backend API for AI-powered resume screening and analysis"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(health_router, tags=["Health"])
app.include_router(candidate_router, tags=["Analysis"])
app.include_router(upload_router, tags=["Upload"])
app.include_router(analyze_resume_router, tags=["Analysis"])
from backend.orchestrator.workflow import (
    RecruitmentWorkflow
)

from backend.utils.jd_utils import (
    extract_jd_skills
)


class RecruitmentService:

    def __init__(self):

        self.workflow = RecruitmentWorkflow()

    def analyze_resume(
        self,
        resume_text,
        jd_text
    ):

        jd_skills = extract_jd_skills(
            jd_text
        )

        result = self.workflow.run(
            resume_text,
            jd_text,
            jd_skills
        )

        return result
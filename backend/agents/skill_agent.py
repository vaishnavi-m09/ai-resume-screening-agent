from backend.utils.skill_dictionary import (
    SKILLS
)


class SkillAgent:

    def extract_skills(
        self,
        resume_text
    ):

        text = resume_text.lower()

        found = []

        for skill in SKILLS:

            if skill.lower() in text:
                found.append(skill)

        return found
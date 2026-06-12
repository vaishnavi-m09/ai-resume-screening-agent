class GapAgent:

    def find_skill_gaps(
        self,
        candidate_skills,
        jd_skills
    ):

        return list(
            set(jd_skills)
            - set(candidate_skills)
        )
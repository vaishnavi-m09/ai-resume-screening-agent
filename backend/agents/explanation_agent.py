class ExplanationAgent:

    def explain(
        self,
        candidate_skills,
        jd_skills
    ):

        matched = []

        missing = []

        for skill in jd_skills:

            if skill in candidate_skills:
                matched.append(skill)
            else:
                missing.append(skill)

        return {
            "matched": matched,
            "missing": missing
        }
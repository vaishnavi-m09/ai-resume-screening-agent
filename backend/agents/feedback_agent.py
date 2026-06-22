class FeedbackAgent:

    def generate_feedback(
        self,
        match_score,
        matched_skills,
        missing_skills
    ):

        if match_score >= 70:

            assessment = "Strong Fit"

        elif match_score >= 50:

            assessment = "Moderate Fit"

        else:

            assessment = "Weak Fit"

        strengths = []

        for skill in matched_skills:

            strengths.append(
                f"Strong evidence of {skill} expertise."
            )

        weaknesses = []

        for skill in missing_skills:

            weaknesses.append(
                f"{skill} was not detected in the resume."
            )

        total_skills = (
            len(matched_skills)
            +
            len(missing_skills)
        )

        if total_skills == 0:

            coverage = 0

        else:

            coverage = round(
                (
                    len(matched_skills)
                    /
                    total_skills
                ) * 100,
                2
            )

        if assessment == "Strong Fit":

            recommendation = (
                "Highly recommended for interview."
            )

        elif assessment == "Moderate Fit":

            recommendation = (
                "Worth considering depending on role priorities."
            )

        else:

            recommendation = (
                "May require significant upskilling."
            )

        return {
            "overall_assessment": assessment,
            "skill_coverage": coverage,
            "matched_skills": len(matched_skills),
            "missing_skills": len(missing_skills),
            "strengths": strengths,
            "weaknesses": weaknesses,
            "recommendation": recommendation
        }
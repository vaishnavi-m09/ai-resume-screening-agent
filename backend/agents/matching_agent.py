from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


class MatchingAgent:

    def __init__(self):

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def semantic_score(
        self,
        resume_text,
        jd_text
    ):

        resume_emb = self.model.encode(
            [resume_text]
        )

        jd_emb = self.model.encode(
            [jd_text]
        )

        score = cosine_similarity(
            resume_emb,
            jd_emb
        )[0][0]

        return float(round(score * 100, 2))

    def calculate_match_score(
        self,
        resume_text,
        jd_text,
        matched_skills,
        missing_skills
    ):

        semantic_score = self.semantic_score(
            resume_text,
            jd_text
        )

        total_skills = (
            len(matched_skills)
            +
            len(missing_skills)
        )

        if total_skills == 0:

            skill_score = 0

        else:

            skill_score = (
                len(matched_skills)
                /
                total_skills
            ) * 100

        final_score = (
            0.7 * skill_score
            +
            0.3 * semantic_score
        )

        return float(round(final_score, 2))
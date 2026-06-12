from sentence_transformers import (
    SentenceTransformer
)

from sklearn.metrics.pairwise import (
    cosine_similarity
)


class MatchingAgent:

    def __init__(self):

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def calculate_match_score(
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
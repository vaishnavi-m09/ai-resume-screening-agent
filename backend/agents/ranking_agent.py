class RankingAgent:

    def rank_candidates(
        self,
        candidates
    ):

        ranked = sorted(
            candidates,
            key=lambda x: x["match_score"],
            reverse=True
        )

        for idx, candidate in enumerate(ranked):

            candidate["rank"] = idx + 1

        return ranked
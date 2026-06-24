class RankingAgent:
    def run(self, state):
        ranked = self.ranking_engine.rank(
            state["recommedations"],
            state["memory"],
            state["graph"]
        )
        state["ranked_recommendations"] = ranked

        return state
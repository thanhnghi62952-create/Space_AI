class ContextAgent:
    def run(self, state):
        context = self.context_builder.build(
            memory=state["memory"],
            graph=state["graph"],
            recommendations = state["ranked_recommendation"]
        )
        state["context"] = context
        return state
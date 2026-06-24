class EvaluationEngine:
    def evaluate(self, state):
        recommendations = state["recommendations"]
        if len(recommendations) >= 3:
            return 8
        return 5
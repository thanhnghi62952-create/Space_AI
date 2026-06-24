class VectorAgent:
    def __init__(self, retrieval_engine):
        self.retrieval_engine = retrieval_engine
    def run(self, state):
        goal = state["goal_id"]
        memories = self.retrieval_engine.retrieve(goal)
        state["retrieved_memories"] = memories
        return state
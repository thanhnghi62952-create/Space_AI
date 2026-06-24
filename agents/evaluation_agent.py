class EvaluationAgent:
    def __init__(self, evaluation_engine, reward_model):
        self.evaluation_engine = evaluation_engine
        self.reward_model = reward_model
    
    def run(self, state):
        score = self.evaluation_engine.evaluate(state)
        state["evaluation_score"] = score
        if "feedback" in state:
            reward = self.reward_model.calculate_reward(state["feedback"])
            state["reward"] = reward
        return state
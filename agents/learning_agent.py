class LearningAgent:
    def run(self, state):
        self.learning_engine.learn(
            state["feedback_record"]
        )
        return state
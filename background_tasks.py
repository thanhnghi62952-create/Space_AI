class BackgroundTaskManager:
    def __init__(self, learning_agent):
        self.learning_agent = learning_agent

    def run_learning(self, state):
        self.learning_agent.run(state)
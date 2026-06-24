class GenerateImageWorkflow:
    def __init__(self, orchestrator):
        self.orchestrator = orchestrator
    def run(self, state):
        return self.orchestrator.run(state)
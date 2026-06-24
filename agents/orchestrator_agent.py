class OrchestratorAgent:
    def __init__(
            self,
            memory_agent,
            graph_agent,
            reasoning_agent,
            ranking_agent,
            context_agent,
            prompt_agent,
            image_agent,
            evaluation_agent
    ):
        
        state = self.prompt_agent.run(state)
        state = self.image_agent.run(state)
        state = self.evaluation_agent.run(state)
        self.memory_agent = memory_agent
        self.graph_agent = graph_agent
        self.reasoning_agent = reasoning_agent
        self.ranking_agent = ranking_agent
        self.context_agent = context_agent
        self.prompt_agent = prompt_agent
        self.image_agent = image_agent
        self.evaluation_agent = evaluation_agent
    def run(self, state):
        state = self.memory_agent.run(state)
        print(state)
        state = self.graph_agent.run(state)
        print(state)
        state = self.reasoning_agent.run(state)
        print(state)
        state = self.ranking_agent.run(state)
        print(state)
        state = self.context_agent.run(state)
        print(state)
        state = self.prompt_agent.run(state)
        print(state)
        state = self.image_agent.run(state)
        return state
    
    

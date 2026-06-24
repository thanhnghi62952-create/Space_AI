class MemoryAgent:
    def __init__(self, memory_retriever):
        self.memory_retriever = memory_retriever
    
    def run(self, state):
        state["memory"] = self.memory_retriever.retrieve(state)
        return state
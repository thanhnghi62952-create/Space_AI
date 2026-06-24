class MemoryRetriever:
    def __init__(self, chroma_handler):
        self.chroma_handler = chroma_handler

    def retrieve(self, state):
        goal = state["goal_id"]
        memories = (
            self.chroma_handler.search(goal)
        )
        return memories
class LLMManager:
    def __init__(self, llm):
        self.llm = llm

    def generate(self, prompt):
        return self.llm.generate(prompt)
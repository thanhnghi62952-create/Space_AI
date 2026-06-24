class PromptAgent:
    def run(self, state):
        prompt = self.prompt_builder.build(
            state["context"]
        )
        state["prompt"] = prompt
        return state
class ImageAgent:
    def run(self, state):
        image_url = self.image_generator.generate(
            state["prompt"]
        )
        state["image_url"] = image_url
        return state
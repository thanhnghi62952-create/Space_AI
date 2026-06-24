class PreferenceAgent:
    def __init__(
            self,
            preference_engine
    ):
        self.preference_engine = (preference_engine)

    def run(self, state):
        preferences = (
            self.preference_engine.extract_preferences(state["history"])
        )
        state["preferences"] = (preferences)
        return state
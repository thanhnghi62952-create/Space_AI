class FeedbackAgent:
    def run(self, state):
        feedback_record = self.feedback_service.save(state["feedback"])
        state["feedback_record"] = feedback_record
        return state
class WorkflowManager:
    def __init__(
            self, 
            generate_image_workflow,
            learning_workflow
    ):
        self.generate_image_workflow = (generate_image_workflow)
        self.learning_workflow = (learning_workflow)

    def execute(self, workflow_name, state):
      if workflow_name == "generate_image":
        return self.generate_image_workflow.run(state)
      elif workflow_name == "learning":
        return self.learning_workflow.run(state)
      else:
        raise ValueError("Unknown workflow")
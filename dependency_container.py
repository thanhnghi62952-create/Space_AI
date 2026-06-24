from agents.memory_agent import MemoryAgent
from agents.graph_agent import GraphAgent
from agents.reasoning_agent import ReasoningAgent
from agents.ranking_agent import RankingAgent
from agents.context_agent import ContextAgent
from agents.prompt_agent import PromptAgent
from agents.image_agent import ImageAgent
from agents.feedback_agent import FeedbackAgent
from agents.learning_agent import LearningAgent
from agents.evaluation_agent import EvaluationAgent
from agents.orchestrator_agent import OrchestratorAgent
from vector_database.chroma_handler import ChromaHandler
from memory.memory_retriever import MemoryRetriever


from workflow.generate_image_workflow import GenerateImageWorkflow
from workflow.learning_workflow import LearningWorkflow
from workflow.manager_workflow import WorkflowManager

workflow_manager = WorkflowManager()
graph_agent = GraphAgent()
memory_agent = MemoryAgent()
reasoning_agent = ReasoningAgent()
ranking_agent = RankingAgent()
context_agent = ContextAgent()
prompt_agent = PromptAgent()
image_agent = ImageAgent()
feedback_agent = FeedbackAgent()
learning_agent = LearningAgent()
evaluation_agent = EvaluationAgent()
chroma_handler = ChromaHandler
orchestrator_agent = OrchestratorAgent(
    memory_agent,
    graph_agent,
    reasoning_agent,
    ranking_agent,
    context_agent,
    prompt_agent,
    image_agent,
    feedback_agent,
    evaluation_agent
)

generate_image_workflow = GenerateImageWorkflow(orchestrator_agent)
learning_workflow = LearningWorkflow(
    feedback_agent,
    learning_agent
)

workflow_manager = WorkflowManager()
workflow_manager.register(
    "generate_image",
    generate_image_workflow
)
workflow_manager.register(
    "learning",
    learning_workflow
)
chroma_handler = ChromaHandler()
memory_retriever = MemoryRetriever(chroma_handler)
memory_agent = MemoryAgent(memory_retriever)
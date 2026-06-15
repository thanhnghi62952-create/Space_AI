try:
    from fastapi import FastAPI
except Exception:
    # Minimal fallback for environments without fastapi installed (for
    # static analysis or lightweight testing). Not a full replacement.
    class FastAPI:
        def __init__(self, *args, **kwargs):
            pass

        def post(self, path: str):
            def _decor(func):
                return func
            return _decor
from graph_loader import load_relationships
from reasoning_engine import reason
from explanation_engine import explain
from feedback_engine import save_feedback
from database.schemas import UserCreate
app = FastAPI()
relationships = load_relationships()

@app.post("/recommend")
def recommend(goal_id: str):
    result = reason(
        goal_id,
        relationships
    )
    explanation = explain(result)

    return {
        "result": result,
        "explanation": explanation
    }
@app.get("/")
def home():
    return {
        "message": "Space AI server is running successfully"
    }
@app.post("/feedback")
def receive_feedback(feedback: dict):
    save_feedback(feedback)

    return {
        "message": "Feedback saved successfully."
    }

@app.post("/users")
def create_user(user: UserCreate):
    return {
        "message": "User created",
        "user": user
    }
@app.post("/recommend")
def recommend(request: dict):
    goal_id = request["goal_id"]

    relationships = load_relationships

    result = reason(
        goal_id,
        relationships
    )
    return result
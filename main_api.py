
from fastapi import FastAPI
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
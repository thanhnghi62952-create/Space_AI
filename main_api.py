from fastapi import FastAPI
from fastapi import Depends
from graph_loader import load_relationships
from reasoning_engine import reason
from explanation_engine import explain
from feedback_engine import save_feedback
from database.schemas import UserCreate, LoginRequest, RecommendationRequest
from database.crud import (create_user, get_user)
from auth.jwt_handler import (verify_password, create_access_token)
from auth.jwt_handler import (get_current_user)
from dependency_container import workflow_manager, learning_agent
from fastapi import BackgroundTasks
app = FastAPI(
title="Space AI",
version="1.0.0"
)

relationships = load_relationships()

@app.get("/")
def home():
    return {
        "message": "Space AI server is running successfully"
    }



@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }


@app.post("/feedback")
def receive_feedback(
feedback: dict):
    # save the feedback and return a confirmation
    save_feedback(feedback)

    return {"message": "Feedback saved successfully"}

@app.get("/version")
def version():
    return {"version": "1.0.0"}
@app.post("/register")
def register(user: UserCreate):
    new_user = create_user(user)
    return {
        "message": "User created successfully",
        "user": new_user
    }
@app.post("/login")
def login(request: LoginRequest):
    user = get_user(request.username)
    if user is None:
        return {
            "message": "User not found"
        }
    if not verify_password(request.password, user.hashed_password):
        return {
            "message": "Wrong password"
        }

    access_token = create_access_token({"sub": user.username})
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

@app.post("/recommend")
def recommend(request:RecommendationRequest,
               background_tasks:BackgroundTasks):
    state = {
        "user_id": request.user_id,
        "goal_id": request.goal_id
    }
    result = workflow_manager.execute(
        "generate_image",
        state
    )
    background_tasks.add_task(
        learning_agent.run,
        state
    )
    return result


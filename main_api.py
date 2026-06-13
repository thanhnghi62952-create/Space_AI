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
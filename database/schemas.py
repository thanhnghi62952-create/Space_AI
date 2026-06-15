from pydantic import BaseModel


class RecommendationRequest(BaseModel):

    user_id: str

    goal_id: str
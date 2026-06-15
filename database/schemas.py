from pydantic import BaseModel


class RecommendationRequest(BaseModel):

    user_id: str

    goal_id: str

class UserCreate(BaseModel):
    user_id: str
    email: str

class UserResponse(BaseModel):
    id: int
    user_id: str
    email: str
    class Config:
        from_attributes = True

#=============
#profile
#==============
class ProfileCreate(BaseModel):
    user_id: str
    budget_level: str
    room_size: str
    preferred_style: str

# feedback
class FeedbackCreate(BaseModel):
    user_id: str
    goal_id: str
    rating: int
    comment: str
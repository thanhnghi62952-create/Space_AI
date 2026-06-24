from pydantic import BaseModel


class RecommendationRequest(BaseModel):

    user_id: str

    goal_id: str

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
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

class RecommendationHistoryCreate(BaseModel):
    user_id: str
    goal_id: str
    prompt: str
    image_url: str
    rating: str

class PreferenceCreate(BaseModel): #form mà người dùng phải điền vào
    user_id: str # id phân biệt người dùng 

    preference_type: str # đây là loại sở thích gì

    preference_value: str # người dùng cụ thể thích cái gì

    score: int # mức độ người dùng thích

class InteractionCreate(BaseModel):
    user_id: str
    goal_id: str
    solutions: str
    prompt: str
    image_url: str
    rating: int
    comment: str

class LoginRequest(BaseModel):
    username: str
    password: str
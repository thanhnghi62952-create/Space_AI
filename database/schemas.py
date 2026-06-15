from pydantic import BaseModel

class UserCreate(BaseModel):
    user_id: str
    
    email: str

class UserResponse(BaseModel):
    id: int
    user_id: str
    email: str
    class Config:
        from_attributes = True
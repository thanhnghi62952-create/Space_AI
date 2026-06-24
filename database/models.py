from sqlalchemy import Column, Integer, String, DateTime
from database.db import Base
from datetime import datetime 
class User(Base):
    __tablename__ = "users"

    id = Column( 
        Integer,
        primary_key=True,
        index=True        
    )
    user_id = Column(
        String,
        unique=True
    )
    email = Column(
        String,
        unique=True
    )
class Profile(Base):
    __tablename__ = "profiles"

    id = Column(
        Integer,
        primary_key=True
    )
    user_id = Column(
        String
    )
    budget_level = Column(
        String
    )
    room_size = Column(
        String
    )
    preferred_style = Column(
        String
    )
class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(
        Integer,
        primary_key=True
    )
    user_id = Column(
        String
    )
    goal_id = Column(
        String
    )
    rating = Column(
        Integer
    )
    comment = Column(
        String
    )
class History(Base):
    __tablename__ = "history"

    id = Column(
        Integer,
        primary_key=True
    )
    user_id = Column(
        String
    )
    goal_id = Column(
        String
    )

class UserPreference(Base):# tạo một bộ hồ sơ để lưu sở thích của người dùng
    __tablename__ = "user_preferences" # đặt tên bộ hồ sơ

    id = Column(Integer, primary_key=True)# cài số thứ tự (id) để phân biến với những khóa khác interger là kiểu dữ liệu
    
    user_id = Column(String) # só thứ tự phân biệt người dùng

    preference_type = Column(String) # loại sở thích là gì food hay music

    preference_value = Column(String)#what do you like specificly food is pizza

    score = Column(Integer) # level yêu thích từ một dến 5

class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )
    user_id = Column(String)
    goal_id = Column(String)
    solutions = Column(String)
    prompt = Column(String)
    image_url = Column(String)
    rating = Column(Integer)
    comment = Column(String)
    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
class Experience(Base):
    __tablename__ = "experiences"

    id = Column( Integer, primary_key=True)

    user_id = Column(String)

    solution_name = Column(String)

    score = Column(Integer)

class LearningEvent(Base):
    __tablename__ = "learning_events"

    id = Column( Integer, primary_key=True, index=True)

    user_id = Column

    event_type = Column (String)

    payload = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)

    
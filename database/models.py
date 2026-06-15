from sqlalchemy import Column, Integer, String
from database.db import Base

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
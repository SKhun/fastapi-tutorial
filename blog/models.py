from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.orm import relationship
from .database import Base


class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    body = Column(Text)
    created_at = Column(
        DateTime, server_default=current_timestamp())
    user_id = Column(Integer, ForeignKey('users.id'))

    creator = relationship("User", back_populates="blogs")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))
    created_at = Column(
        DateTime, server_default=current_timestamp())

    blogs = relationship("Blog", back_populates="creator")

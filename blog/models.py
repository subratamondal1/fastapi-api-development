"""SQLAlchemy Models for DB"""

from sqlalchemy import Column, Integer, String
from blog.database import Base


class Blog(Base):
    """Database model for storing the Blog data"""

    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)


class UserModel(Base):
    """Database model for storing the User data"""

    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

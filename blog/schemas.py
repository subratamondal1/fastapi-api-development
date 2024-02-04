"""Pydantic Models (Schemas), Response Model"""

from pydantic import BaseModel, EmailStr


class Blog(BaseModel):
    """Request Body format for the blog data sent by the Client to the Server"""

    title: str
    body: str


class BlogResponse(BaseModel):
    """Response Body format of the data that will be sent by the Server to the Client"""

    title: str
    body: str

    class Config:
        """Required for Response Model"""

        from_attributes = True


class UserSchema(BaseModel):
    """User Pydantic (Schema) Request Model"""

    name: str
    email: EmailStr
    password: str


class UserResponseSchema(BaseModel):
    """User Pydantic (Schema) Response Model"""

    name: str
    email: EmailStr

    class Config:
        """Required for Response Model"""

        from_attributes = True

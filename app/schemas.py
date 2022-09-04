from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint


# creates a schema (pydantic model) for post data
# pydantic model performs validation to ensure scheme is met in request

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):  # can alter this if we only want user to update one field
    pass


class UserOut(BaseModel):
    id: int
    email: str
    created_at: datetime

    class Config:
        orm_mode = True

# pydantic model for response
# inherits title, content, and published from PostBase


class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut  # return pydantic model type

    class Config:  # necessary so pydantic model recognizes post as a dictionary, not sql alchemy model
        orm_mode = True


class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr  # validates email is a valid email
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)

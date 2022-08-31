import datetime
from typing import Optional

from pydantic import BaseModel, Field


class PostGet(BaseModel):
    id: int
    text: str
    topic: str

    class Config:
        orm_mode = True


class UserGet(BaseModel):
    gender: int
    age: int
    city: str
    os: str
    id: int
    country: str
    exp_group: int
    source: str

    class Config:
        orm_mode = True


class FeedGet(BaseModel):
    user_id: int
    post_id: int
    action: str
    time: datetime.datetime
    user: Optional[UserGet] = None
    post: Optional[PostGet] = None

    class Config:
        orm_mode = True

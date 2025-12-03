#
#  Import LIBRARIES
# from fastapi import FastAPI
from pydantic import BaseModel

#  Import FILES
#
#  ______________________


class PostBase(BaseModel):
    title: str
    content: str


class PostCreate(PostBase):
    pass


class PostUpdate(BaseModel):
    title: str
    content: str

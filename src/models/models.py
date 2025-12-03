#
#  Import LIBRARIES
# from fastapi import FastAPI
from pydantic import BaseModel

#  Import FILES
#
#  ______________________


class Post(BaseModel):
    title: str
    content: str

#
#  Import LIBRARIES
# from fastapi import FastAPI
from pydantic import BaseModel, Field

#  Import FILES
#
#  ______________________


class PostBase(BaseModel):
    title: str
    content: str = "Contenido no disponible"


class PostCreate(BaseModel):
    title: str = Field(
        default=...,
        min_length=3,
        max_length=100,
        description="Titulo del post (mínimo 3 caracteres, máximo 100)",
        examples=["Mi primer post con Fastapi"],
    )
    content: str = Field(
        default="Contenido no disponible",
        min_length=10,
        description="Contenido del post (mínimo 10 caracteres)",
        examples=["Este es un contenido válido porque tiene 10 caracteres o más"],
    )
    # pass


class PostUpdate(BaseModel):
    title: str
    content: str | None = None

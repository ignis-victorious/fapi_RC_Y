#
#  Import LIBRARIES
from fastapi import FastAPI

#  Import FILES
from .data.post_db import BLOG_POST

#
#  ______________________

app = FastAPI(title="Mini Blog")


@app.get(path="/")
def home() -> dict[str, str]:
    return {"message": "Bienvenidos a Mini Blog por Emagnu"}


@app.get(path="/posts")
def list_posts() -> dict[str, list[dict[str, int | str]]]:
    return {"data": BLOG_POST}


# app = FastAPI()

# @app.get("/")
# def main():
#     return {"message": "Hello World"}

#
#  Import LIBRARIES
# from fastapi import FastAPI
#  Import FILES
#
#  ______________________

#
#  Import LIBRARIES
from fastapi import FastAPI, Query

#  Import FILES
from .data.post_db import BLOG_POST

#
#  ______________________

app = FastAPI(title="Mini Blog")


@app.get(path="/")
def home() -> dict[str, str]:
    return {"message": "Bienvenidos a Mini Blog por Emagnu"}


@app.get(path="/posts")
def list_posts(
    query_parm: str | None = Query(default=None, description="Texto para buscar por título"),
) -> dict[str, list[dict[str, int | str]] | str | None]:
    if query_parm:
        results: list[dict[str, int | str]] = [
            post for post in BLOG_POST if query_parm.lower() in str(post["title"]).lower()
        ]
        return {"data": results, "query_parm": query_parm}
    return {"data": BLOG_POST}


# @app.get(path="/posts")
# def list_posts(
#     query_parm: str | None = Query(default=None, description="Texto para buscar por título"),
# ) -> dict[str, list[dict[str, int | str]] | str | None]:
#     if query_parm:
#         results: list[dict[str, int | str]] = []
#         for post in BLOG_POST:
#             if query_parm.lower() in str(post["title"]).lower():
#                 results.append(post)
#         print(f"results={results}")
#         return {"data": results, "query_parm": query_parm}
#     return {"data": BLOG_POST}


# @app.get(path="/posts")
# def list_posts() -> dict[str, list[dict[str, int | str]]]:
#     return {"data": BLOG_POST}


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

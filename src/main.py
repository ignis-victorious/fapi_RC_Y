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


#  Query Parameters with list-comprehension
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


#  Query Parameters with "for"
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


#  Path + query paraneters
@app.get(path="/posts/{post_id}")
def get_posts(
    post_id: int, include_content: bool
) -> dict[str, int | str] | dict[str, dict[str, int | str]] | dict[str, str]:
    for post in BLOG_POST:
        if post["id"] == post_id:
            if include_content:
                return {"data": post}
            if include_content is False:
                return {"id": post["id"], "title": post["title"]}
    return {"error": "Post no encontrado"}


# #  Path paraneters
# @app.get(path="/posts/{post_id}")
# def get_posts(post_id: int) -> dict[str, dict[str, int | str]] | dict[str, str]:
#     for post in BLOG_POST:
#         if post["id"] == post_id:
#             return {"data": post}
#     return {"error": "Post no encontrado"}


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

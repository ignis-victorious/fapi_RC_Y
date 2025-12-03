#
#  Import LIBRARIES
from fastapi import Body, FastAPI, Query

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


#  Path + query paraneters - Ricardo solution
@app.get(path="/posts/{post_id}")
def get_posts(
    post_id: int, include_content: bool = Query(default=True, description="Incluir o no el contenido")
) -> dict[str, int | str] | dict[str, dict[str, int | str]] | dict[str, str]:
    for post in BLOG_POST:
        if post["id"] == post_id:
            if not include_content:
                return {"id": post["id"], "title": post["title"]}
            return {"data": post}
    return {"error": "Post no encontrado"}


@app.post(path="/posts")
def create_post(
    post: dict[str, str | int] = Body(default=...),
) -> dict[str, dict[str, int | str] | str] | dict[str, str]:
    if "title" not in post or "content" not in post:
        return {"error": "Title y Content son requeridos"}
    if not str(post["title"]).strip():
        return {"error": "Title no puede estar vacío"}
    new_id: int = (int(BLOG_POST[-1]["id"]) + 1) if BLOG_POST else 1
    new_post: dict[str, int | str] = {"id": new_id, "title": post["title"], "content": post["content"]}
    BLOG_POST.append(new_post)
    return {"message": "Post creado", "data": new_post}


#
#  Import LIBRARIES
# from fastapi import FastAPI
#  Import FILES
#
#  ______________________

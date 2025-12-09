#
#  Import LIBRARIES
from fastapi import Body, FastAPI, HTTPException, Query

#  Import FILES
<<<<<<< HEAD
from .data.post_db import BLOG_P_CLASS, BLOG_POST
from .models.models import PostCreate, PostPublic, PostSummary, PostUpdate

# , PostSummary
=======
from .data.post_db import BLOG_POST
from .models.models import PostCreate, PostPublic, PostUpdate
>>>>>>> 9e5528eac06b28b3862bcbabf3c4e15dbdd00ff1

# PostBase
#
#  ______________________

app = FastAPI(title="Mini Blog")


@app.get(path="/")
def home() -> dict[str, str]:
    return {"message": "Bienvenidos a Mini Blog por Emagnu"}


#  Query Parameters with list-comprehension - Query Param: Django
@app.get(path="/posts", response_model=list[PostPublic])
def list_posts(
    query_parm: str | None = Query(default=None, description="Texto para buscar por título"),
<<<<<<< HEAD
) -> list[PostPublic]:
    if query_parm:
        return [post for post in BLOG_P_CLASS if query_parm.lower() in str(post.title).lower()]
    return BLOG_P_CLASS
=======
) -> list[dict[str, int | str]]:
    if query_parm:
        return [post for post in BLOG_POST if query_parm.lower() in str(post["title"]).lower()]
        # results: list[dict[str, int | str]] = [
        #     post for post in BLOG_POST if query_parm.lower() in str(post["title"]).lower()
        # ]
        # return results
    return BLOG_POST


# @app.get(path="/posts")
# def list_posts(
#     query_parm: str | None = Query(default=None, description="Texto para buscar por título"),
# ) -> dict[str, list[dict[str, int | str]] | str | None]:
#     if query_parm:
#         results: list[dict[str, int | str]] = [
#             post for post in BLOG_POST if query_parm.lower() in str(post["title"]).lower()
#         ]
#         return {"data": results, "query_parm": query_parm}
#     return {"data": BLOG_POST}
>>>>>>> 9e5528eac06b28b3862bcbabf3c4e15dbdd00ff1


#  Path + query paraneters - Ricardo solution
@app.get(
    path="/posts/{post_id}",
    response_model=PostSummary | PostPublic,
    response_description="Post encontrado",
)
def get_post(
    post_id: int, include_content: bool = Query(default=True, description="Incluir o no el contenido")
) -> PostSummary | PostPublic:
    for post in BLOG_POST:
        if post["id"] == post_id:
            if not include_content:
                return PostSummary(id=int(post["id"]), title=str(post["title"]))
                # return {"id": post["id"], "title": post["title"]}
            return PostPublic(id=int(post["id"]), title=str(post["title"]), content=str(post.get("content", "")))
            # return post
    raise HTTPException(status_code=404, detail="Post no encontrado")


# @app.get(
#     path="/posts/{post_id}",
#     # response_model=[PostPublic | PostSummary],
#     response_description="Post encontrado",
# )
# def get_posts(post_id: int, include_content: bool = Query(default=True, description="Incluir o no el contenido")):
#     for post in BLOG_P_CLASS:
#         if post.id == post_id:
#             if not include_content:
#                 return {"id": post.id, "title": post.title}
#             return post
#     return HTTPException(status_code=404, detail="Post no encontrado")


# POST - Unprocessable: {"title": 12345,"content": 67890} - processable:{"title": "12345","content": "67890"}
#  {"title": "Titulo de prueba con Pydantic", "content": "Pydantic es genial"}
# {"title": "Emme",  "content": "Este contenido es disponible"}
# {"title": "Post solo titulo"}
# {"title": "Hi",  "content": "Anita"} genrates two errors!
# {"title": "Hols mundo!",  "content": "Anita Lava la tina"}
@app.post(path="/posts")
def create_post(post: PostCreate = Body(default=...)) -> dict[str, dict[str, int | str] | str]:
    new_id: int = (int(BLOG_POST[-1]["id"]) + 1) if BLOG_POST else 1
    new_post: dict[str, int | str] = {"id": new_id, "title": post.title, "content": post.content}
    BLOG_POST.append(new_post)
    return {"message": "Post creado", "data": new_post}
    # return {"data": post}


# PUT - {"title": "Hola desde FastAPI- (Actualizado con PUT)", "content": "Content actualizado"}
#  {"title": "Prueba del PUT con Pydantic Y solamente el titulo!"}
#  {"title": "Prueba del PUT con Pydantic", "content": "Esto contenido es actualizado!"}
#  {"title": "Spam obtén una novia gratis"}
@app.put(path="/posts/{post_id}")
def update_post(post_id: int, data: PostUpdate) -> dict[str, PostPublic | str]:
    for post in BLOG_P_CLASS:
        if post.id == post_id:
            playload: dict[str, str] = data.model_dump(exclude_unset=True)
            if "title" in playload:
                post.title = playload["title"]
            if "content" in playload:
                post.content = playload["content"]

            return {"message": "Post actualizado", "data": post}
    raise HTTPException(status_code=404, detail="Post no encontrado")
    # return {"error": "No se encontro el post"}


#  DELETE
@app.delete(path="/posts/{post_id}", status_code=204)
def delete_post(post_id: int) -> None:
    for index, post in enumerate(BLOG_POST):
        if post["id"] == post_id:
            BLOG_POST.pop(index)
            return
    raise HTTPException(status_code=404, detail="Post no encontrado")


#
#  Import LIBRARIES
# from fastapi import FastAPI
#  Import FILES
#
#  ______________________

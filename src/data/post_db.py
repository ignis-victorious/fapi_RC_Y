#
#  Import LIBRARIES
#  Import FILES
from ..models.models import PostPublic

#
#  ______________________

BLOG_P_CLASS: list[PostPublic] = [
    PostPublic(id=1, title="UNO-Hola desde FastAPI", content="UNO-Mi primer post con FastAPI"),
    PostPublic(id=1, title="DOS-Mi segundo Post con FastAPI", content="Dos-Mi segundo Post con FastAPI"),
    PostPublic(id=1, title="TRES-Django vs FastAPI", content="TRES-FastAPI es más rápido por X razones"),
]

BLOG_POST: list[dict[str, int | str]] = [
    {"id": 1, "title": "Hola desde FastAPI", "Content": "Mi primer post con FastAPI"},
    {"id": 2, "title": "Mi segundo Post con FastAPI", "Content": "Mi segundo Post con FastAPI"},
    {"id": 3, "title": "Django vs FastAPI", "Content": "FastAPI es más rápido por X razones"},
]

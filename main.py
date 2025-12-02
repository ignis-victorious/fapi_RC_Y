# 
#  Import LIBRARIES
from fastapi import FastAPI
#  Import FILES
# 
#  ______________________

app = FastAPI (title="Mini Blog")


@app.get("/")
def home():
    return {'message': 'Bienvenidos a Mini Blog'}




# app = FastAPI()

# @app.get("/")
# def main():
#     return {"message": "Hello World"}

# 
#  Import LIBRARIES
from fastapi import FastAPI
#  Import FILES
# 
#  ______________________

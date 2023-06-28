'''uvicorn main:app --reload
POSTMAN app for testing
'''

from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


@app.get("/")  # Uses get method and "/" path
async def root():
    return {"message": "welcome to my api"}


@app.get("/posts")
def get_posts():
    return {"data": "This is your post"}


@app.post("/createposts")
def create_posts(payload: dict = Body(...)):
    print(payload)
    return f'{payload}'

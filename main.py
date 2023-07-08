'''uvicorn main:app --reload
POSTMAN app for testing  1:14
'''

from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


#  post schema
class Post(BaseModel):
    title: str
    content: str
    published: bool = True


@app.get("/")  # Uses get method and "/" path
async def root():
    return {"message": "welcome to my api"}


@app.get("/posts")
def get_posts():
    return {"data": "This is your post"}


@app.post("/createposts")
def create_posts(new_post: Post):
    print(new_post.published)
    return {"data": "new post"}

# title str, content str

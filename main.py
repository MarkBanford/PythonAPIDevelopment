'''uvicorn main:app --reload'''

from fastapi import FastAPI

app = FastAPI()


@app.get("/")  # Uses get method and "/" path
async def root():
    return {"message": "welcome to my api"}


@app.get("/posts")
def get_posts():
    return {"data": "This is your post"}

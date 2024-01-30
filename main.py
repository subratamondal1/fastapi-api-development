from fastapi import FastAPI, Body
from pydantic import BaseModel

app=FastAPI()

@app.get("/")
async def root():
    return {
        "message":"Hello World"
    }

@app.get("/posts")
async def get_posts():
    return {
        "data":"Your Posts"
    }

@app.post("/createposts")
async def createposts(payLoad:dict=Body(default=...)):
    print(payLoad)
    return {
        "post": "Post created successfully",
        "new_post": {
            "title":payLoad["title"],
            "content":payLoad["content"]
        }
    }

# Create an app instance
app = FastAPI()

# Define a data model
class Item(BaseModel):
    name: str
    age: int

# Create a GET endpoint
@app.get("/items/{item_id}")
async def get_item(item_id: int):
    # Return a dummy item
    return {"item_id": item_id, "name": "Foo", "age": 42}

# Create a POST endpoint
@app.post("/items/")
async def create_item(item: Item):
    # Return the item received
    return item
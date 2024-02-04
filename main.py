"""This module is the Entry Point for the FastAPI app"""

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get(path="/")
async def index(limit: int = 10, unpublished: bool = False, sort: Optional[str] = None):
    """Our Home Page"""
    if unpublished:
        return {"data": f"{limit} Unpublished Blog List, Sorted by: {sort}"}
    return {"data": f"{limit} Blog List, Sorted by: {sort}"}


@app.get(path="/blog/{blog_id}")
async def show(blog_id: int):
    """Show the blog by blog_id"""
    # fetch blog with blog_id = blog_id
    return {"blog": blog_id}


@app.get(path="/blog/unpublished")
async def unpublished_blogs():
    "Show all the unpublished blogs"
    return {"data": "Unpublished Blogs"}


@app.get(path="/blog/{blog_id}/comments")
async def comments(blog_id):
    """Show blog comments with matching id"""
    # fetch blog comments with blog_id = blog_id
    return {"comments": [1, 2, 3, {blog_id}]}


class Blog(BaseModel):
    """Schema for Blog Data that will be sent by the User/Client"""

    id: str
    title: str
    published_at: Optional[bool]


@app.post(path="/blog")
async def create_blog(request: Blog):
    """Create a Blog (Data sent by the Client in Request Body)"""

    return {
        "request": {
            "id": request.id,
            "title": request.title,
            "published_at": request.published_at,
        }
    }

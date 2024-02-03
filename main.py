"""This module is the Entry Point for the FastAPI app"""

from fastapi import FastAPI

app = FastAPI()


@app.get(path="/")
async def index():
    """Our Home Page"""
    return {"data": {"index page message": "Welcome to Home Page."}}


@app.get(path="/about")
async def about():
    """Our About Page"""
    return {"data": {"about page message": "Welcome to our About Page."}}

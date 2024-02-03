from fastapi import FastAPI

app=FastAPI()

app = FastAPI()

@app.get(path="/")
async def index():
    return {
        "data": {
            "index page message": "Welcome to Home Page."
        }
    }


@app.get(path="/about")
async def about():
    return {
        "data": {
            "about page message": "Welcome to our About Page."
        }
    }
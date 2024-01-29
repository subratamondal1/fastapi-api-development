<p align="center"><a href="https://fastapi.tiangolo.com/" target="_blank"><img src="https://fastapi.tiangolo.com/img/icon-white.svg" width=200px></a></p> 
<h1 align="center">Python API Development with FastAPI</h1>
<p align="center">
  <img src="https://img.shields.io/badge/python-3.11.0-yellow" alt="python@3.11.0">
  <img src="https://img.shields.io/badge/fastapi-0.109.0-lighgreen" alt="fastapi@0.109.0">
  <img src="https://img.shields.io/badge/docker-23.0.3-blue" alt="docker@23.0.3">
  <img src="https://img.shields.io/badge/pydantic-2.6.0-crimson" alt="pydantic@2.6.0">
  <img src="https://img.shields.io/badge/postgresql-16-lightblue" alt="postgresql@16">
  <img src="https://img.shields.io/badge/sqlachemy-2.0.21-red" alt="sqlalchemy@2.0.21">
  <img src="https://img.shields.io/badge/pip-23.3.2-moccasin" alt="pip@23.3.2">
  <img src="https://img.shields.io/badge/poetry-1.7.1-orange" alt="poetry@1.7.1">
  <img src="https://img.shields.io/badge/pytest-7.4.4-papayawhip" alt="pytest@7.4.4">
</p>

<h2 align="left">First Steps</h2>

First install these libraries.

```bash
pip install fastapi uvicorn
```

Copy these lines of code in the `main.py` file.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
  return {"message": "Hello World"}
```

From terminal run this command.

```bash
# --reload makes sure to update the changes, use it only in dev and not in production
uvicorn main:app --reload
```

Open the url in your browser: [http://http://127.0.0.1:8000/](http://http://127.0.0.1:8000/) to see the result.

```
{
    "message": "Hello World"
}
```

Well! Congratualtions on building your first FastAPI app. Yes! it's that's easy to build apps, for now.

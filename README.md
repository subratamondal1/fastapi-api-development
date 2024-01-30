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

<h2 align="left">FastAPI Path Operations</h2>

FastAPI Path operations are a way to define the URL patterns and parameters for your API endpoints. They allow you to specify what kind of data you expect to receive from the client, and how to validate and convert it. They also help you generate automatic documentation and interactive tools for your API.

A Path operation consists of three main parts:

- A **path** that defines the URL segment for the endpoint, such as `/items/{item_id}`. You can use curly braces `{}` to declare path parameters, which are dynamic values that you can extract from the URL. For example, `item_id` is a path parameter that you can access in your function as an argument.
- An **operation** that defines the HTTP method for the endpoint, such as `GET`, `POST`, `PUT`, etc. You can use a decorator from FastAPI, such as `@app.get` or `@app.post`, to associate your function with the operation. For example, `@app.get("/items/{item_id}")` means that your function will handle `GET` requests to the `/items/{item_id}` path.
- A **function** that defines the logic and response for the endpoint. You can use Python type annotations to declare the type and validation of the path parameters, as well as the request body and response model. For example, `async def read_item(item_id: int)` means that your function expects an integer `item_id` as a path parameter, and will return an asynchronous response.

Here is a simple example of a Path operation that creates an item and returns it as JSON:

```python
from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()

@app.post("/items/", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(item: Item):
    return item
```

<h2 align="left">HTTP GET vs POST Requests</h2>

HTTP GET and POST are two common methods for sending and receiving data over the web. They differ in how they encode the data and how much data they can send.

- **HTTP GET** requests append the data to the URL as query string parameters. For example, `http://example.com/?name=John&age=25`. This method is suitable for simple and short data, such as search queries or form inputs. However, it has some limitations, such as:
  - The data is visible in the URL, which may expose sensitive information or be bookmarked by the user.
  - The data is restricted by the maximum length of the URL, which depends on the browser and the server.
  - The data can only be ASCII characters, and may need to be encoded or escaped.
- **HTTP POST** requests send the data in the message body of the request. For example, `name=John&age=25`. This method is suitable for complex and large data, such as file uploads or JSON objects. It has some advantages, such as:
  - The data is hidden from the URL, which provides more security and privacy.
  - The data is not limited by the URL length, and can be of any size and type.
  - The data can be binary or Unicode, and does not need to be encoded or escaped.

In Python, you can use the `requests` library to send HTTP GET and POST requests. For example:

```python
# Import requests library
import requests

# Define the URL and the data
url = "http://example.com/"
data = {"name": "John", "age": 25}

# Send a GET request
r = requests.get(url, params=data)

# Print the response
print(r.text)

# Send a POST request
r = requests.post(url, data=data)

# Print the response
print(r.text)
```

In FastAPI, you can use the `@app.get` and `@app.post` decorators to create API endpoints that handle GET and POST requests. For example:

```python
# Import FastAPI and Pydantic
from fastapi import FastAPI
from pydantic import BaseModel

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
```

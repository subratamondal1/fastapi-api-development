<p align="center"><a href="https://fastapi.tiangolo.com/" target="_blank"><img src="https://fastapi.tiangolo.com/img/icon-white.svg" width=200px></a></p> 
<h1 align="center">Python API Development with FastAPI</h1>

<p align="center">
<img src="https://github.com/subratamondal1/fastapi-api-development/actions/workflows/devops.yml/badge.svg" alt="build status">
</p>

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

<h2 align="left">FastAPI Features</h2>

- Provided `Pydantic` Data Validation.
- `Autocomplete Code` Support.
- Based on `JSON Schema`.
- Based on `Open API`, recommended way to build APIs.
- Provide `security` and `authentication`
  - HTTP Basic
  - OAuth2 (also with JWT tokens)
  - API Keys in:
    - Headers
    - Query Parameters
    - Cookies, etc
- Dependency Injection
- Unlimited `plug-ins`
- Testing
- FastAPI is build on `Starlette` which also brings additional features:
  - Websocket support
  - GraohQL support
  - In-process background tasks
  - Startup and shutdown events
  - Test client built on `requests`
  - CORS, GZip, Static Files, Streaming, Responses
  - Session & Cookie Support
- SQL Databases
- NoSQL Databases
- GraphQL

<h2 align="left">Basic Concepts</h2>

```python
@app.get(path="/")
async def index():
    """Our Home Page"""
    return {"data": {"index page message": "Welcome to Home Page."}}
```

- `@app` : is the Path Operation Decorator.
- `.get()` : is the Operation, others are `post, put, delete`, etc.
- `path="/"` : is the Path at the end of the Base URL.
- `index()` : function is called the **Path Operation Function** because it is performaing some operation on the path with GET Operation.

Now, we can say that the **FastAPI** app with Path Operation Decorator is performing **GET** Operation on the Path `"/"` and Performing the **index()** operation.

<h2 align="left">Path Parameters</h2>
Path Parameters are **dynamic** segments of a URL that can **capture variable values** and pass them to the endpoint function. They are useful for creating flexible and adaptable APIs that can handle different inputs with the same endpoint, such as retrieving specific resources by their IDs. They also help to create clean and readable URLs that are intuitive for users and developers. Path Parameters can be declared with type hints to enable automatic validation, conversion, and documentation of the API.

For example, suppose you want to create an endpoint that returns information about a blog based on its ID. You can use dynamic routing to define a path parameter named `blog_id` and use it in your function.

```python
@app.get(path="/blog/{blog_id}")
async def show(blog_id):
    """Show the blog by blog_id"""
    # fetch blog with blog_id = blog_id
    return {
        "blog": blog_id
    }
```

<h3 align="left">Dynamic Routing Side Effects</h3>
Since, FastAPI runs from `Top to Bottom`, once the `request` hits required `Path Operation` it executes the respective `Path Operation Function` and returns the result.

In the below example we have two path operation `@app.get(path="/blog/{blog_id}")` and `@app.get(path="/blog/unpublished")` no matter how many times you try to access the unpublished one, you will hit the 1st one and get its value because the 2nd one is nothing but `@app.get(path="/blog/{blog_id=unpublished}")` and hence it returns the result without reaching the 2nd one.

```python
❌
@app.get(path="/blog/{blog_id}")
async def show(blog_id: int):
    """Show the blog by blog_id"""
    # fetch blog with blog_id = blog_id
    return {"blog": blog_id}

@app.get(path="/blog/unpublished")
async def unpublished():
    "Show all the unpublished blogs"
    return {
        "data" : "Unpublished Blogs"
    }
```

To hit the 2nd `Path Operation` you need to change the order, else it will think that you are providing path parameters value.

```python
✅
@app.get(path="/blog/unpublished")
async def unpublished():
    "Show all the unpublished blogs"
    return {
        "data" : "Unpublished Blogs"
    }

@app.get(path="/blog/{blog_id}")
async def show(blog_id: int):
    """Show the blog by blog_id"""
    # fetch blog with blog_id = blog_id
    return {"blog": blog_id}
```

<h2 align="left">Automatic Documentation with Swagger UI</h2>
Automatic Documentation is a feature of FastAPI that automatically generates documentation for your API based on your code and type hints. The documentation follows the OpenAPI standard, which is a widely adopted specification for designing and documenting APIs. FastAPI also provides two user interfaces for exploring and testing the API documentation:

- **Swagger UI**, which is an interactive tool that allows developers to try out the API endpoints and see the request/response details.

- **ReDoc**, which is a simple and elegant tool that presents the API documentation in a user-friendly format.

<h2 align="left">Query Parameters</h2>

```python
@app.get(path="/")
async def index(limit:int=10, unpublished:bool=True, sort:Optional[str]=None):
    """Our Home Page"""
    if unpublished:
        return {"data": f"{limit} Unpublished Blog List"}
    else:
        return {"data": f"{limit} Blog List"}
```

```bash
http://127.0.0.1:8000/?limit=33&unpublished=true&sort=byDate
```

Query Parameters are `key-value pairs` that are appended to the URL after a `?` and can be used to **filter, sort**, or **paginate** the results of an API request. They are useful for creating flexible and adaptable APIs that can handle different user preferences or criteria. Unlike path parameters, which are part of the URL path and are used to identify a specific resource or resources, query parameters are optional and can have default values. FastAPI allows you to declare and validate query parameters with type hints and **Query** objects.

<h2 align="left">Request Body</h2>

<h2 align="left">Intermediate Concepts</h2>
<h2 align="left">Database Tasks</h2>
<h2 align="left">Responses</h2>
<h2 align="left">User and Password</h2>
<h2 align="left">Relationship</h2>
<h2 align="left">Refactor for Bigger Apps using Router</h2>
<h2 align="left">Authentication using JWT</h2>
<h2 align="left">Deploy FastAPI</h2>

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

A **request body** is data that you send from a client (such as a browser) to your API. It is usually in JSON format and contains the information that you want to transmit to the server. To declare a request body in FastAPI, you use Pydantic models, which are classes that inherit from `BaseModel` and have attributes with standard Python types. For example:

```python
from fastapi import FastAPI, Request
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    return item
```

This model declares a request body that expects a JSON object like:

```json
{
  "name": "Foo",
  "description": "An optional description",
  "price": 45.2,
  "tax": 3.5
}
```

FastAPI will automatically validate the data, convert the types, and generate documentation for your API. You can access the request body data in your path operation function as a parameter with the type of your model (`Item` in this case). If you need to access the request object directly, you can declare a parameter with the type `Request` and FastAPI will pass it to you. You can read more details about the request body and the request object in the official FastAPI documentation.

<h2 align="left">Intermediate Concepts</h2>

FastAPI schemas are classes that inherit from Pydantic's `BaseModel` and define the expected data types and validation rules for your API endpoints. They can be used to declare **request bodies, response models, query parameters, path parameters**, and more. FastAPI schemas allow you to automatically generate documentation, validate data, and convert types for your API. For example, you can create a schema for a user like this:

```python
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name: str
    email: EmailStr
    age: int
```

This schema will expect a JSON object like this:

```json
{
  "name": "Alice",
  "email": "alice@example.com",
  "age": 25
}
```

And it will validate that the `name` is a string, the `email` is a valid email address, and the `age` is an integer. You can also use Pydantic validators, default values, optional fields, and other features to customize your schemas.

<h2 align="left">Schema vs Database</h2>

FastAPI schemas and database are two different concepts that are related but not the same.

- FastAPI schemas are Pydantic models that define the data types and validation rules for your API endpoints. They can be used to declare request bodies, response models, query parameters, path parameters, and more. FastAPI schemas allow you to automatically generate documentation, validate data, and convert types for your API.
- Database is the term used to refer to the persistent storage of your data, usually in a relational database management system (RDBMS) such as SQLite, PostgreSQL, MySQL, etc. To connect to a database with FastAPI, you can use either SQLModel or SQLAlchemy, two popular libraries that provide object-relational mapping (ORM) and data validation features. ORM is a technique that maps between objects in code and database tables (relations). With ORM, you can create classes that represent database tables, and use methods to perform CRUD (create, read, update, delete) operations on your data.
  - SQLModel and SQLAlchemy use Pydantic models as the base class for their ORM models, so you can reuse some of your FastAPI schemas as database models, or create separate ones for different purposes. You can also use Pydantic's `orm_mode` to enable serialization of ORM objects. You can read more about FastAPI schemas and database in the official documentation or in these articles.

<h2 align="left">Database Connection, Model and Table</h2>

```python
# database.py module

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite+pysqlite:///../blog.db"
engine = create_engine(
    url=SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()
```

- `from sqlalchemy import create_engine` imports the `create_engine` function from SQLAlchemy, which is a popular library for working with relational databases in Python.
- `from sqlalchemy.ext.declarative import declarative_base` imports the `declarative_base` function from SQLAlchemy, which is a helper function that creates a base class for your database models or entities.
- `from sqlalchemy.orm import sessionmaker` imports the `sessionmaker` function from SQLAlchemy, which is a factory function that creates a class for managing database sessions.
- `SQLALCHEMY_DATABASE_URL = "sqlite+pysqlite:///./blog.db"` defines a database URL that specifies the type, location, and name of the database file. In this case, it is a SQLite database named `blog.db` in the current directory. You can change this to use other databases supported by SQLAlchemy, such as PostgreSQL, MySQL, etc.
- `engine = create_engine(url=SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})` creates a database engine that connects to the database and handles the low-level communication. The `connect_args` parameter is a SQLite-specific option that allows multiple threads to share the same connection.
- `SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)` creates a `SessionLocal` class that can be used to create database sessions. A session is an object that represents a connection to the database and allows you to perform CRUD (create, read, update, delete) operations on your data. The `bind` parameter tells the session to use the engine we created earlier. The `autocommit` and `autoflush` parameters are optional and control how the session commits and flushes the changes to the database.
- `Base = declarative_base()` creates a `Base` class that is the base class for all your database models. You can use this class to define your database tables and columns using standard Python types and attributes.

To use these code examples with FastAPI, you need to do a few more steps:

- Define your database models by inheriting from the `Base` class and using the `sqlalchemy.Column` function to declare the columns. For example, you can create a model for a blog post like this:

```python
class Post(Base):
    __tablename__ = "posts"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    title = sqlalchemy.Column(sqlalchemy.String)
    content = sqlalchemy.Column(sqlalchemy.Text)
```

- Define your Pydantic models or schemas that define the input and output data for your API endpoints. You can use the same models as your database models, or create separate ones for different purposes. You can also use Pydantic's `orm_mode` to enable serialization of ORM objects. For example, you can create a schema for a post like this:

```python
class PostSchema(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        orm_mode = True
```

- Create a dependency function that returns a database session object for each request. You can use the `SessionLocal` class we created earlier and the `yield` keyword to ensure that the session is closed after each request. For example, you can create a dependency function like this:

```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

- Create your FastAPI app and use the dependency function to inject the database session into your path operation functions. You can use the session object to perform CRUD operations on your database models, using methods such as `add`, `query`, `get`, `update`, `delete`, etc. You can also use the Pydantic models or schemas as the `response_model` and the parameters for your API endpoints. FastAPI will automatically validate the data, convert the types, and generate documentation for your API. For example, you can create an app like this:

```python
app = FastAPI()

@app.get("/posts/", response_model=List[PostSchema])
def read_posts(db: Session = Depends(get_db)):
    posts = db.query(Post).all()
    return posts

@app.post("/posts/", response_model=PostSchema)
def create_post(post: PostSchema, db: Session = Depends(get_db)):
    db_post = Post(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post
```

<h2 align="left">Responses</h2>

FastAPI Responses are objects that represent the **data and metadata** that are sent back to the client as a result of a request. FastAPI provides several **response classes** that can be used to customize the content, format, and status of the responses. For example, you can use JSONResponse, HTMLResponse, PlainTextResponse, RedirectResponse, StreamingResponse, FileResponse, etc.

You can declare the response class for a path operation using the **response_class parameter** in the decorator, such as:

```python
@app.get("/items/", response_class=HTMLResponse)
```

You can also return a response object directly from your path operation function, such as:

```python
return HTMLResponse(content="<h1>Hello</h1>")
```

However, if you do this, FastAPI will not perform any **automatic data conversion or validation**, and the documentation will not reflect the response format.

You can also use the **response_model parameter** in the decorator to declare the type of the data that will be returned, such as:

```python
@app.get("/items/", response_model=Item)
```

This will enable FastAPI to perform data validation, conversion, filtering, and documentation using **Pydantic models**. You can also use generic types, such as List[Item], to declare the response model.

<h2 align="left">Response Model</h2>

A FastAPI Response Model is a way of declaring the type and structure of the data that your API will return in response to a request. You can use Pydantic models, lists, dictionaries, or scalar values as response models. FastAPI will use the response model to:

- Validate the output data and ensure that it matches the expected type and shape.
- Filter the output data and exclude any extra fields that are not part of the response model.
- Generate a JSON Schema for the response, which will be used for the OpenAPI documentation and client code generation.

You can specify the response model for a path operation using the `response_model` parameter in the decorator, such as:

```python
@app.get("/items/", response_model=Item)
```

This means that the endpoint `/items/` will return an `Item` object, which is a Pydantic model that defines the fields and types of an item. FastAPI will validate the returned data, filter out any extra fields, and document the response schema.

You can also use generic types, such as `List[Item]`, to declare the response model as a list of items. FastAPI will handle the validation and documentation accordingly.

<h2 align="left">Exception & Status Code</h2>

```python
@app.get(path="/blog/{id}")
async def blog_by_id(id, response: Response, db: Session = Depends(get_db)):
    """Get the Blog by id"""
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Your id: {id} is not available.",
        )
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"detail": f"Your id: {id} is not available."}
    return blog
```

<h2 align="left">Delete Blog</h2>

```python
@app.delete(path="/blog/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_blog_by_id(id, db: Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return "Done"
```

<h2 align="left">Update Blog</h2>

```python
@app.put(path="/blog/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_blog_by_id(id, request: schemas.Blog, db: Session = Depends(get_db)):
    """Update the Blog by id"""
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Your id: {id} is not available.",
        )
    blog.update(values=request.model_dump())
    db.commit()
    return "Blog Updated"
```

<h2 align="left">Create User</h2>

To create a user in FastAPI, you need to do the following steps:

- Define a Pydantic model that represents the user data, such as username, email, password, etc. For example, you can create a model like this:

```python
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    username: str
    email: EmailStr
    password: str
```

- Define a database model that maps to a table in your database, using SQLAlchemy or another ORM library. You can also use the same model as your Pydantic model, or create a separate one. For example, you can create a model like this:

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
```

- Create a database session that allows you to interact with your database, using SQLAlchemy or another ORM library. You can also use FastAPI's `Depends` feature to inject a session into your endpoints. For example, you can create a session like this:

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///database.db")
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

- Create an endpoint that handles the user creation, using FastAPI's `app.post` decorator. You can use the Pydantic model as the input data, and the database model as the output data. You can also use the database session to perform the CRUD operations. For example, you can create an endpoint like this:

```python
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.exc import IntegrityError

app = FastAPI()

@app.post("/users/", response_model=User)
def create_user(user: User, db: Session = Depends(get_db)):
    db_user = User(**user.dict())
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username or email already exists.")
```

This endpoint will accept a JSON body with the user data, validate it using the Pydantic model, create a new user in the database using the database model, and return the created user as a JSON response. It will also handle the case where the username or email is already taken, and raise an appropriate error.

<h2 align="left">Encrypting (Hashing) Password</h2>

```python
from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:
    """Encryption (Hashing) Class"""

    def bcrypt(password: str):
        """Encryption (Hashing) Method"""
        return password_context.hash(password)
```

<h2 align="left">Use Docs Tags</h2>

<h2 align="left">Relationship</h2>
<h2 align="left">Refactor for Bigger Apps using Router</h2>
<h2 align="left">Authentication using JWT</h2>
<h2 align="left">Deploy FastAPI</h2>

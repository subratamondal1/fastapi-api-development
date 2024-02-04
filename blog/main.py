"""Entry point for the Blog Application"""

from typing import List
from fastapi import FastAPI, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from blog import schemas, models, database, hashing

# FastAPI app instance
app = FastAPI()

# Create the Database
models.Base.metadata.create_all(bind=database.engine)


async def get_db():
    """Dependency function that creates and returns a database session object using SQLAlchemy"""
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post(path="/blog", status_code=status.HTTP_201_CREATED)
async def create(request: schemas.Blog, db: Session = Depends(get_db)):
    "Allow users to create blogs"
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.delete(path="/blog/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_blog_by_id(id, db: Session = Depends(get_db)):
    """Delete the Blog by id"""
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Your id: {id} is not available.",
        )
    blog.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


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


@app.get(
    path="/blog", status_code=status.HTTP_200_OK, response_model=schemas.BlogResponse
)
async def all_blogs(db: Session = Depends(get_db)):
    """Get all the Blogs from the Database"""
    blogs = db.query(models.Blog).all()
    return blogs


@app.get(
    path="/blog/{id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.BlogResponse,
)
async def blog_by_id(id, db: Session = Depends(get_db)):
    """Get the Blog by id"""
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Your id: {id} is not available.",
        )
    return blog


@app.post(path="/user/", response_model=schemas.UserResponseSchema)
async def create_user(request: schemas.UserSchema, db: Session = Depends(get_db)):
    """Create New User"""
    new_user = models.UserModel(
        name=request.name,
        email=request.email,
        password=hashing.Hash.bcrypt(request.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

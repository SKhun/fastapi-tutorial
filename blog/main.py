from fastapi import FastAPI
from .database import engine, Base
from .routers import blog, user, authentication

app = FastAPI()

Base.metadata.create_all(engine)


app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)

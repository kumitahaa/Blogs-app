# ---------------------------------------- Imports -----------------------------------------------
from fastapi import FastAPI
import models
from database import engine
from routers import blog,user,authentication
from fastapi.middleware.cors import CORSMiddleware
# ---------------------------------------- Create Instance -----------------------------------------------
app = FastAPI() 

origins = [
    "http://localhost:3000",
    "http://localhost:3000/",
    "https://localhost:3000/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)

models.Base.metadata.create_all(bind=engine)
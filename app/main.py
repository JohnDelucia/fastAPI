
from fastapi import FastAPI, CORSMiddleware
from . import models
from .database import engine
from .routers import post, user, auth, vote
from pydantic import BaseSettings
from .config import settings

app = FastAPI()

#list of url to talk to API
origins = ["*"]

#allows for requests from other domains to talk with our API
app.add_moddleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True, 
    allow_methods = ["*"],
    allow_headers = ["*"]
)

app.include_router(post.router)  # request go es to post and looks for match
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"Message": "Hello"}

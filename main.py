from fastapi import FastAPI
from controller import user
from db import database

app = FastAPI()

app.include_router(user.router)

@app.lifespan("startup")
def startup():
    database.Base.metadata.create_all(bind=database.engine)

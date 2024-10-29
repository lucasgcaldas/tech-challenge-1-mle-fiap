from fastapi import FastAPI
from controller import user, embrapa
from db import database
from fastapi import FastAPI
from contextlib import asynccontextmanager

app = FastAPI()

app.include_router(user.router)
app.include_router(embrapa.router)

# Application lifespan configuration (startup and shutdown)
@asynccontextmanager
async def lifespan(app: FastAPI):
    # This code runs on startup
    database.Base.metadata.create_all(bind=database.engine)
    yield
    # Cleanup code (if necessary) can go here

app.router.lifespan_context = lifespan
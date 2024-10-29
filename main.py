from fastapi import FastAPI
from controller import user
from db import database
from fastapi import FastAPI, Depends
from scraping_module import get_producao_data, get_processamento_data, get_comercializacao_data, get_importacao_data, get_exportacao_data
from contextlib import asynccontextmanager
from fastapi.security import OAuth2PasswordBearer
from core.security import verify_token

app = FastAPI()

app.include_router(user.router)

# Application lifespan configuration (startup and shutdown)
@asynccontextmanager
async def lifespan(app: FastAPI):
    # This code runs on startup
    database.Base.metadata.create_all(bind=database.engine)
    yield
    # Cleanup code (if necessary) can go here

app.router.lifespan_context = lifespan

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Protected endpoints with authentication
@app.get("/processing")
async def processing(token: str = Depends(oauth2_scheme)):
    verify_token(token)
    data = get_processamento_data()
    return data

@app.get("/commercialization")
async def commercialization(token: str = Depends(oauth2_scheme)):
    verify_token(token)
    data = get_comercializacao_data()
    return data

@app.get("/import")
async def import_data(token: str = Depends(oauth2_scheme)):
    verify_token(token)
    data = get_importacao_data()
    return data

@app.get("/export")
async def export_data(token: str = Depends(oauth2_scheme)):
    verify_token(token)
    data = get_exportacao_data()
    return data

from fastapi import FastAPI
from controller import user
from db import database
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import jwt
from datetime import datetime, timedelta
import importlib
from scraping_module import get_producao_data, get_processamento_data, get_comercializacao_data, get_importacao_data, get_exportacao_data

app = FastAPI()

app.include_router(user.router)

@app.lifespan("startup")
def startup():
    database.Base.metadata.create_all(bind=database.engine)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

#SECRET_KEY = "FIAP_GRUPO_56"  # Defina uma chave secreta segura para assinar os tokens JWT

#def verify_token(token: str):
 #   try:
  #      payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
   #     return payload
    #except jwt.ExpiredSignatureError:
     #   raise HTTPException(status_code=401, detail="Token expirado")
    #except jwt.InvalidTokenError:
     #   raise HTTPException(status_code=401, detail="Token inválido")

#@app.post("/token")
#async def login(username: fiap-group56, password: grupo056):
    # Verificação de credenciais
 #   if username == "fiap-group56" and password == "grupo056":
  #      expiration = datetime.utcnow() + timedelta(hours=1)
   #     token = jwt.encode({"sub": username, "exp": expiration}, SECRET_KEY, algorithm="HS256")
    #    return {"access_token": token, "token_type": "bearer"}
    #raise HTTPException(status_code=401, detail="Credenciais inválidas")

@app.get("/producao")
async def producao(token: str = Depends(oauth2_scheme)):
#    verify_token(token)
    data = get_producao_data()
    return data

@app.get("/processamento")
async def processamento(token: str = Depends(oauth2_scheme)):
#    verify_token(token)
    data = get_processamento_data()
    return data

@app.get("/comercializacao")
async def comercializacao(token: str = Depends(oauth2_scheme)):
#    verify_token(token)
    data = get_comercializacao_data()
    return data

@app.get("/importacao")
async def importacao(token: str = Depends(oauth2_scheme)):
#    verify_token(token)
    data = get_importacao_data()
    return data

@app.get("/exportacao")
async def exportacao(token: str = Depends(oauth2_scheme)):
#    verify_token(token)
    data = get_exportacao_data()
    return data

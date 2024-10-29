from fastapi import APIRouter, Depends
from core.security import verify_token
from fastapi.security import OAuth2PasswordBearer
from service.embrapa import get_production_data, get_processing_data, get_commercialization_data, get_export_data, get_import_data

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Protected endpoints with authentication
@router.get("/production", tags=["Embrapa Searching"])
async def production(token: str = Depends(oauth2_scheme)):
    verify_token(token)
    data = get_production_data()
    return data

@router.get("/processing", tags=["Embrapa Searching"])
async def processing(token: str = Depends(oauth2_scheme)):
    verify_token(token)
    data = get_processing_data()
    return data

@router.get("/commercialization", tags=["Embrapa Searching"])
async def commercialization(token: str = Depends(oauth2_scheme)):
    verify_token(token)
    data = get_commercialization_data()
    return data

@router.get("/import", tags=["Embrapa Searching"])
async def import_data(token: str = Depends(oauth2_scheme)):
    verify_token(token)
    data = get_import_data()
    return data

@router.get("/export", tags=["Embrapa Searching"])
async def export_data(token: str = Depends(oauth2_scheme)):
    verify_token(token)
    data = get_export_data()
    return data
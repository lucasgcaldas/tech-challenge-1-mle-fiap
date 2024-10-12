from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserResponse
from db.database import get_db
from service import user as crud_user
from core.security import verify_password

router = APIRouter()

@router.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud_user.get_user_by_name(db, user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud_user.create_user(db=db, user=user)

@router.post("/login/")
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud_user.get_user_by_name(db, user.name)
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    return {"message": "Login successful"}

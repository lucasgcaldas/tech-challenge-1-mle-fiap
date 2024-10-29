from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserResponse
from db.database import get_db
from service import user as crud_user
from core.security import verify_password, create_access_token

router = APIRouter()

@router.post("/users/", tags=["User"], response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud_user.get_user_by_name(db, user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud_user.create_user(db=db, user=user)

# Login endpoint to generate JWT
@router.post("/login", tags=["User"])
async def login(username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    # Retrieve user from the database
    db_user = crud_user.get_user_by_name(db, username)
    
    # Check if user exists and if password is correct
    if not db_user or not verify_password(password, db_user.password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    # Generate a JWT token for the authenticated user
    access_token = create_access_token(data={"sub": db_user.name})
    return {"access_token": access_token, "token_type": "bearer"}
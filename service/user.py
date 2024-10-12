from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate
from core.security import hash_password

def create_user(db: Session, user: UserCreate):
    hashed_password = hash_password(user.password)
    db_user = User(name=user.name, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_name(db: Session, name: str):
    return db.query(User).filter(User.name == name).first()

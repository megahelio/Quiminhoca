import os
from dotenv import load_dotenv
from fastapi import APIRouter, Depends, HTTPException
import sqlalchemy
from sqlalchemy.orm import Session
from passlib.hash import bcrypt
from jose import jwt
from datetime import datetime, timedelta

from sqlmodel import SQLModel
from models.auth.user import User
from models.auth.schemas import Token, UserCreate
from db.database import get_session, engine

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

authRouter = APIRouter()

def create_access_token(data: dict):
    to_encode = data.copy()
    to_encode["exp"] = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@authRouter.post("/register", response_model=Token)
def register(user: UserCreate, db: Session = Depends(get_session)):
    hashed = bcrypt.hash(user.password)
    db_user = User(email=user.email, hashed_password=hashed)
    db.add(db_user)
    db.commit()
    return {"access_token": create_access_token({"sub": user.email}), "token_type": "bearer"}

@authRouter.post("/login", response_model=Token)
def login(user: UserCreate, db: Session = Depends(get_session)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not bcrypt.verify(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"access_token": create_access_token({"sub": user.email}), "token_type": "bearer"}


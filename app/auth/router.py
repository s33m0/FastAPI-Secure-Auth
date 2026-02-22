from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from app.auth.schemas import LoginRequest, TokenResponse
from app.auth.services import authenticate_user


router = APIRouter(prefix="/api/auth", tags=["Authentication"])
@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    token = authenticate_user(db, data.email, data.password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"access_token": token}
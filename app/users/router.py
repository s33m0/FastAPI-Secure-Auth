from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from app.users.schemas import UserCreate, UserResponse
from app.users.services import create_user_service as create_user


router = APIRouter(prefix="/api/users", tags=["Users"])


@router.post("/signup", response_model=UserResponse)
def signup(data: UserCreate, db: Session = Depends(get_db)):
    user = create_user(db, data)
    return user

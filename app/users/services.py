from sqlalchemy.orm import Session
from app.users.schemas import UserCreate, UserResponse
from app.users.model import User
from app.core.security import hash_password as get_password_hash

def create_user_service(db: Session, user_create: UserCreate) -> UserResponse:
    user = User(
        email=user_create.email,
        password=get_password_hash(user_create.password),
        name=user_create.name,
        role=user_create.role
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return UserResponse.model_validate(user)
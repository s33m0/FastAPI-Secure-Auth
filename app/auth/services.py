from sqlalchemy.orm import Session
from app.users.model import User
from app.core.security import verify_password, create_access_token

def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return None

    if not verify_password(password, user.password):
        return None

    token = create_access_token({"sub": str(user.id)})
    return token
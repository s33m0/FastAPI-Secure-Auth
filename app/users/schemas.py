from pydantic import BaseModel, ConfigDict, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    name: str
    role: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    name: str
    role: str

    model_config = ConfigDict(from_attributes=True)

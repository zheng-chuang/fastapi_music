import uuid
from pydantic import EmailStr
from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    email: EmailStr = Field(unique=True, index=True, max_length=255)


class UserLogin(UserBase):
    password: str = Field()


class UserCreate(UserLogin):
    repeat_password: str = Field()


class User(UserBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    hashed_password: str

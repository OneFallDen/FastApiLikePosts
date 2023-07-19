from pydantic import BaseModel, EmailStr


class Account(BaseModel):
    id: int
    firstname: str
    lastname: str
    password: str
    email: EmailStr


class AccountReg(BaseModel):
    firstName: str | None
    lastName: str | None
    email: str | None
    password: str | None


class Post(BaseModel):
    id: int
    title: str
    content: str
    owner: str
    likes: str
    dislikes: str


class AddOrUpdatePost(BaseModel):
    title: str | None
    content: str | None

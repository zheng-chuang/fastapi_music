from typing import Annotated

from fastapi import APIRouter, HTTPException, Body

from app.model.user import UserLogin

router = APIRouter()


@router.post("/login")
def login(user: Annotated[UserLogin, Body(embed=True)]):
    return user

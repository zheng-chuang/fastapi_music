from fastapi import APIRouter

from app.api.routes import user, login

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])

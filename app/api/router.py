from fastapi import APIRouter
from app.api.routes import auth, portfolio

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["Auth"])
api_router.include_router(portfolio.router, prefix="/portfolio", tags=["Portfolio"])

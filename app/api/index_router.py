from fastapi import APIRouter
from app.api.routes import auth, portfolio_router

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["Auth"])
api_router.include_router(portfolio_router.router, prefix="/portfolio", tags=["Portfolio"])

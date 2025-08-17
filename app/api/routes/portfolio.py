from fastapi import APIRouter, Depends
from app.api.deps import get_current_user_id
from app.api.controllers.portfolio import get_portfolio_controller, get_my_portfolio_controller

router = APIRouter()




@router.get("")
def get_portfolio():
    return get_portfolio_controller()

@router.get("/{userId}")
def get_my_portfolio(user_id: str = Depends(get_current_user_id)):
    return get_my_portfolio_controller(user_id)
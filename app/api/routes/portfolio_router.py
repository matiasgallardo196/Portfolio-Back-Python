from fastapi import APIRouter, Depends
from app.api.controllers import portfolio_controller
from app.api.deps import get_current_user_id, get_db
from sqlalchemy.orm import Session

router = APIRouter()




@router.get("")
def get_portfolio(db: Session = Depends(get_db)):
    return portfolio_controller.get_portfolio(db)

@router.get("/{userId}")
def get_my_portfolio(userId: str = Depends(get_current_user_id), db: Session = Depends(get_db)):
    return portfolio_controller.get_portfolio_by_id(userId,db)
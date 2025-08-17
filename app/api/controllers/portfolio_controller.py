from app.api.services.portfolio_service import get_user_by_id


def get_portfolio(db):
    FIXED_USER_ID = "808ceb8b-8da6-440c-952d-2d5c23b070e0"
    return get_user_by_id(FIXED_USER_ID,db)

def get_portfolio_by_id(user_id: str,db):
    return get_user_by_id(user_id,db)

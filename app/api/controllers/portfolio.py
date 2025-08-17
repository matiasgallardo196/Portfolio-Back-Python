from app.api.services.portfolio import build_portfolio_data, build_my_portfolio_data

def get_portfolio_controller():
    return build_portfolio_data()

def get_my_portfolio_controller(user_id: str):
    return build_my_portfolio_data(user_id)

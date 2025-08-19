from sqlalchemy.orm import Session, selectinload
from app.models.user import User

def get_user_by_id(user_id: str, db: Session) -> User | None:
    return (
        db.query(User)
        .options(
            selectinload(User.about),
            selectinload(User.projects),
            selectinload(User.languages),
            selectinload(User.achievements),
            selectinload(User.contact),
            selectinload(User.skills)
        )
        .filter(User.id == user_id)
        .first()
    )

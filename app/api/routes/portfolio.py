from fastapi import APIRouter, Depends
from app.api.deps import get_current_user_id

router = APIRouter()

@router.get("/me")
def get_my_portfolio(user_id: str = Depends(get_current_user_id)):
    return {
        "about": {
            "fullName": "Demo User",
            "location": "Sydney, Australia",
            "biography": "Your bio here",
            "pageDescription": None,
            "metaDescription": None,
            "heroTitle": "Hello ",
            "heroSubtitle": "FastAPI from scratch",
        },
        "skills": {
            "languages": ["JavaScript", "TypeScript", "SQL"],
            "frontend": ["React", "HTML", "CSS", "TailwindCSS"],
            "backend": ["FastAPI", "NestJS", "Node.js"],
            "databases": ["SQLite", "PostgreSQL"],
            "devops": ["Docker", "GitHub Actions"],
        },
        "userId": int(user_id),
    }

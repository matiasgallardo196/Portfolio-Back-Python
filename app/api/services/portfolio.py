def build_portfolio_data():
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
        "userId": "user_id",
    }

def build_my_portfolio_data(user_id: str):
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

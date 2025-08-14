from datetime import datetime, timedelta, timezone
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt
from passlib.context import CryptContext

JWT_SECRET = "change_me"      # luego lo pasamos a .env
JWT_ALG = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # cambia a tu front real
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# usuario fake para entender el flujo
pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")
DEMO_EMAIL = "demo@user.com"
DEMO_PASSWORD = "demo1234"
FAKE_USER = {"id": 1, "email": DEMO_EMAIL, "hashed_password": pwd_ctx.hash(DEMO_PASSWORD)}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

def create_access_token(sub: str, minutes: int | None = None) -> str:
    expire = datetime.now(tz=timezone.utc) + timedelta(minutes=minutes or ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"sub": sub, "exp": expire}
    return jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALG)

def get_current_user_id(token: str = Depends(oauth2_scheme)) -> str:
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALG])
        return str(payload["sub"])
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

@app.get("/api/health")
def health():
    return {"ok": True}

@app.post("/api/auth/login")
def login(form: OAuth2PasswordRequestForm = Depends()):
    if form.username != DEMO_EMAIL or not pwd_ctx.verify(form.password, FAKE_USER["hashed_password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = create_access_token(str(FAKE_USER["id"]))
    return {"access_token": token, "token_type": "bearer"}

@app.get("/api/portfolio/me")
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

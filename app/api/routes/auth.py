from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.core.auth import create_access_token
from app.core.security import verify_password

router = APIRouter()

DEMO_EMAIL = "demo@user.com"
DEMO_PASSWORD = "demo1234"
FAKE_USER = {
    "id": 1,
    "email": DEMO_EMAIL,
    "hashed_password": "$2b$12$..."  # generado por hash_password(DEMO_PASSWORD)
}

@router.post("/login")
def login(form: OAuth2PasswordRequestForm = Depends()):
    if form.username != DEMO_EMAIL or not verify_password(form.password, FAKE_USER["hashed_password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = create_access_token(str(FAKE_USER["id"]))
    return {"access_token": token, "token_type": "bearer"}

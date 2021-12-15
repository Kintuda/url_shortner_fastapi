from fastapi.param_functions import Depends
from fastapi.security.oauth2 import OAuth2PasswordBearer
from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from config.app import get_settings
from database import SessionLocal
from jose import jwt, JWTError
from models.oauth_token import OauthToken
from pydantic import ValidationError
from models.user import User
from schemas.oauth import TokenData
from services.user_service import userService

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl="api/v1/oauth/token"
)

def get_db_session():
    """Starts a database session as a context manager.
    """
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

CONFIG = get_settings()

async def get_current_user(
    db: Session = Depends(get_db_session),
    token: str = Depends(reusable_oauth2)
) -> User:
    try:
        payload = jwt.decode(token, CONFIG.OAUTH_SECRET_HASH, algorithms=[CONFIG.OAUTH_HASH_ALG])
        token_data = TokenData(**payload)
        user = await userService.get_user_by_id(db, token_data.id)
        return user
    except (JWTError, ValidationError) as e:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
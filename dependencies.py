from fastapi.security.oauth2 import OAuth2PasswordBearer
from database import SessionLocal
from jose import jwt, JWTError

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


# def get_current_user(
#     db: Session = Depends(get_db_session),
#     token: str = Depends(reusable_oauth2)
# ) -> User:
#     try:
#         payload = jwt.decode(token, applicationSettings.OAUTH_SECRET_HASH, algorithms=[applicationSettings.OAUTH_HASH_ALG])
#         token_data = schemas.TokenPayload(**payload)
#     except (JWTError, ValidationError):
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail="Could not validate credentials",
#         )
#     user = crud.user.get(db, id=token_data.sub)
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user
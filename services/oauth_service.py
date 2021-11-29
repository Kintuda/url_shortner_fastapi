from codecs import encode
import json
from typing import Dict
from config.app import ApplicationSettings, get_settings
from models.user import User
from models.oauth_token import OauthToken
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi.encoders import jsonable_encoder

from schemas.user import DescribeUser

CONFIG = get_settings()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class OauthService():
    def create_access_token(self, payload: User, delta: datetime) -> OauthToken:
        encoded_data = payload.to_json()
        encoded_data.update({"exp": delta})
        access_token = jwt.encode(encoded_data, CONFIG.OAUTH_SECRET_HASH, algorithm=CONFIG.OAUTH_HASH_ALG)
        oauth_token = OauthToken(
            access_token = access_token,
            expires_at = delta,
            user_id = payload.id
        )

        return OauthToken(
            access_token = oauth_token.access_token,
            expires_at = delta
        )

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    def hash_password(self, plain_password: str) -> str:
        return pwd_context.hash(plain_password)

oauthService = OauthService()
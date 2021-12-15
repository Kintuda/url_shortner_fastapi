from datetime import datetime, timedelta
from os import access
from typing import Any, Optional

from sqlalchemy.sql.coercions import ReturnsRowsImpl
from models.oauth_token import OauthToken
from models.user import User
from sqlalchemy.orm import Session

from schemas.user import CreateUser, DescribeUser
from services.oauth_service import oauthService

from config.app import get_settings

CONFIG = get_settings()

class UserService:
    async def get_user_by_id(self, db_session: Session, id: str) -> Optional[DescribeUser]:
        user = db_session.query(User).filter(User.id == id).first()
        return user
        
    async def authenticate_user(self, db_session: Session, email: str, password: str) -> Optional[OauthToken]:
        user = db_session.query(User).filter(User.email == email).first()

        if oauthService.verify_password(password, user.password) is False:
            return None

        expire = datetime.now() + timedelta(seconds=CONFIG.OAUTH_EXPIRATION_TIME)
        access_token = oauthService.create_access_token(user, expire)
        return access_token
    
    async def create_user(self, db_session: Session, user: CreateUser) -> DescribeUser:
        hashed_password = oauthService.hash_password(user.password)
        userDb = User(
            email = user.email,
            first_name = user.first_name,
            last_name = user.last_name,
            password = hashed_password,
            created_at = datetime.now()
        )
        db_session.add(userDb)
        db_session.commit()
        db_session.refresh(userDb)

        return userDb


userService = UserService()
from typing import Any, List
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session

from dependencies import get_db_session
from services.user_service import userService 

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
oauth_router = APIRouter()

# @router.get("/me", response_model=DescribeUser)
# def describe_me(
#     db: Session = Depends(get_db_session),
#     current_user: User = Depends(deps.get_current_user)
# ): 

@oauth_router.post("/token")
async def create_token(
    db: Session = Depends(get_db_session),
    form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    oauth = await userService.authenticate_user(db, form_data.username, form_data.password)

    return {
        "access_token": oauth.access_token
    }


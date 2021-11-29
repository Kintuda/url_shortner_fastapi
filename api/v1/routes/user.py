from typing import Any, List
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from models.user import User

from schemas.user import CreateUser, DescribeUser
from services.user_service import userService
from dependencies import get_db_session

user_router = APIRouter()

@user_router.post("/", response_model=DescribeUser)
async def create_user(
    *,
    db: Session = Depends(get_db_session),
    user: CreateUser,
) -> Any:
    saved_user = await userService.create_user(db, user)
    return saved_user
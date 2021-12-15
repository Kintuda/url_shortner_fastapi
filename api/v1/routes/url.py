from typing import List
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.sqltypes import String
from starlette.responses import RedirectResponse
from models.user import User

from schemas.pagination import PaginatedResponse
from schemas.url import ListUrl, UrlShort
from services.url_service import urlService

from dependencies import get_current_user, get_db_session


url_router = APIRouter()

# @url_router.get("/")
@url_router.get("/", response_model=PaginatedResponse[List[ListUrl]])
async def get_links(
    *,
    db: Session = Depends(get_db_session),
    current_user: User = Depends(get_current_user)
): 
    links = await urlService.get_links(db, current_user)

    return links

@url_router.post("/")
async def create_link(
    *,
    db: Session = Depends(get_db_session),
    current_user: User = Depends(get_current_user),
    payload: UrlShort,
): 
    links = await urlService.create_redirect_link(db, current_user, payload)

    return links


@url_router.get("/redirect/{redirect_id}")
async def redirect_link(
    redirect_id,
    db: Session = Depends(get_db_session),
): 
    link = await urlService.get_link(db, redirect_id)
    response = RedirectResponse(url=link.original_url)

    return response
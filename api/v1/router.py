from fastapi import APIRouter
from .routes.oauth import oauth_router
from .routes.user import user_router
from .routes.url import url_router

api_router = APIRouter()
api_router.include_router(oauth_router, prefix="/oauth", tags=["oauth"])
api_router.include_router(user_router, prefix="/users", tags=["users"])
api_router.include_router(url_router, prefix="/links", tags=["links"])
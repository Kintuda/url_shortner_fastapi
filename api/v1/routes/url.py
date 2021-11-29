from typing import List
from fastapi import APIRouter

from schemas.pagination import PaginatedResponse
from schemas.url import ListUrl


url_router = APIRouter()

@url_router.get("/links", response_model=PaginatedResponse[List[ListUrl]])
def get_links(): 
    
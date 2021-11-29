from pydantic import BaseModel


class UrlShort(BaseModel):
    url: str

class ListUrl(UrlShort):
    redirect_url: str
    created_at: str
    deleted_at: str

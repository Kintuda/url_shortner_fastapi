from models.base import BaseModel

class OauthToken(BaseModel):
    access_token: str
    expires: int
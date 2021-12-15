from pydantic import BaseModel

class OauthToken(BaseModel):
    access_token: str
    expires: int

class TokenData(BaseModel):
    id: str
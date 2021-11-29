from functools import lru_cache
from pydantic import BaseSettings

class ApplicationSettings(BaseSettings):
    DATABASE_URL: str

    OAUTH_SECRET_HASH: str
    ### in seconds
    OAUTH_EXPIRATION_TIME: int
    OAUTH_HASH_ALG: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        case_sensitive = True

@lru_cache()
def get_settings():
    return ApplicationSettings()
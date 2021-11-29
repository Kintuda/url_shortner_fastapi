from datetime import datetime

from sqlalchemy.sql.sqltypes import DateTime
from models.base import BaseModel
from sqlalchemy import Column, String, ForeignKey, text
from sqlalchemy.dialects.postgresql import UUID

class OauthToken(BaseModel):
    __tablename__ = "oauth_tokens"
    
    id = Column(
        UUID(as_uuid = True),
        primary_key=True,
        server_default=text("uuid_generate_v4()"),
    )
    access_token = Column(String)
    expires_at = Column(String)
    user_id = Column(UUID(as_uuid=True), ForeignKey('url.id'))
    created_at = Column(DateTime, default=datetime.now)

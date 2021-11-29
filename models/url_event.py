from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, ForeignKey, text
from datetime import datetime
from sqlalchemy.sql.sqltypes import DateTime, String
from models.base import BaseModel

class UrlEvent(BaseModel):
    __tablename__ = "UrlEvents"
    id = Column(
        UUID(as_uuid = True),
        primary_key=True,
        server_default=text("uuid_generate_v4()"),
    )
    type = Column(String())
    url_id = Column(UUID(as_uuid=True), ForeignKey('url.id'))
    created_at = Column(DateTime, default=datetime.now)

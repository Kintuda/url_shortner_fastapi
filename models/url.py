from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime
from models.base import BaseModel
from sqlalchemy import Column, String, text
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID

class Url(BaseModel):
    __tablename__ = "urls"
    id = Column(
        UUID(as_uuid = True),
        primary_key=True,
        server_default=text("uuid_generate_v4()"),
    )
    original_url: Column(String)
    statistics = relationship("UrlStatistics", back_populates="statistics")
    events = relationship("UrlEvents")
    owner = relationship("users")
    created_at = Column(DateTime, default=datetime.now)
    deleted_at: Column(DateTime, nullable=True)

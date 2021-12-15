from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime
from models.base import BaseModel
from sqlalchemy import Column, String, text
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from shortuuid import ShortUUID

class Url(BaseModel):
    __tablename__ = "urls"
    id = Column(
        "id",
        String,
        primary_key=True,
        unique=True,
        default=ShortUUID().random(length=22)
    )
    original_url = Column(String)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.now)
    deleted_at = Column(DateTime, nullable=True)

    def __init__(self, original_url: String, user_id: String) -> None:
        super().__init__()
        self.original_url = original_url
        self.user_id = user_id
        self.created_at = datetime.now()

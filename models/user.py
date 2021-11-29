from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime
from models.base import BaseModel
from sqlalchemy import Column, String, text
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID


class User(BaseModel):
    __tablename__ = "users"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("uuid_generate_v4()"),
    )
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    deleted_at = Column(DateTime, nullable=True)

    def to_json(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
        }

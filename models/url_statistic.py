from sqlalchemy.sql.schema import ForeignKey
from models.base import BaseModel
from models.url import Url
from sqlalchemy import Column,Integer, text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

class UrlStatistic(BaseModel):
    __tablename__ = "UrlStatistics"
    id = Column(
        UUID(as_uuid = True),
        primary_key=True,
        server_default=text("uuid_generate_v4()"),
    )
    url_id = Column(UUID(as_uuid=True), ForeignKey('url.id'))
    click_count = Column(Integer, default=0)



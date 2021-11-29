from datetime import datetime
import uuid
from pydantic import BaseModel
from sqlalchemy.sql.sqltypes import DateTime
from uuid import UUID

class User(BaseModel):
    first_name: str
    last_name: str
    email: str


class CreateUser(User):
    password: str
    pass

class DescribeUser(User):
    id: UUID
    created_at: datetime

    class Config:
        orm_mode = True
from typing import Generic, Optional, TypeVar


from pydantic.generics import GenericModel
from pydantic.main import BaseModel

DataT = TypeVar('DataT')


class PaginationLinks(BaseModel):
    nextLink: str
    previousLink: str

class PaginationAttributes(BaseModel):
    limit: int
    count: int
    skip: int

class Metadata(BaseModel):
    pagination:PaginationAttributes
    links: PaginationLinks

class PaginatedResponse(GenericModel, Generic[DataT]):
    data: Optional[DataT]
    pagination: Optional[Metadata]

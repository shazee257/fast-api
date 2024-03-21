from pydantic import BaseModel, Field


class PaginationQueryDto(BaseModel):
    page: int = Field(1, ge=1)
    limit: int = Field(10, gt=0, le=1000)
    q: str = ""

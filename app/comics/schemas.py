from pydantic import BaseModel, Field


class RatingCreate(BaseModel):
    comic_id: int
    VALUE: int = Field(ge=1, le=5)

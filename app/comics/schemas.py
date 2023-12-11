from pydantic import BaseModel, Field, field_validator


class ComicCreate(BaseModel):
    title: str
    author: str
    rating: float


class ComicRead(BaseModel):
    id: int
    title: str
    author: str
    rating: float

    class Config:
        from_attributes = True


class RatingCreate(BaseModel):
    comic_id: int
    VALUE: int = Field(ge=1, le=5)


# class RatingRead(BaseModel):
#     id: int
#     comic_id: int
#     user_id: int
#     VALUE: int
#
#     class Config:
#         orm_mode = True

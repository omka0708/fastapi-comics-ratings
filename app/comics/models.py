from sqlalchemy import Column, String, Integer, ForeignKey, SmallInteger, Float
from sqlalchemy.orm import relationship

from app.database import Base


class Comic(Base):
    __tablename__ = "comic"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    rating = Column(Float, index=True, default=0)

    ratings = relationship("Rating", back_populates="comic")


class Rating(Base):
    __tablename__ = "rating"

    id = Column(Integer, primary_key=True, autoincrement=True)
    comic_id = Column(Integer, ForeignKey("comic.id"))
    user_id = Column(Integer, ForeignKey("user.id"))
    VALUE = Column(SmallInteger, index=True)

    comic = relationship("Comic", back_populates="ratings")
    user = relationship("User", back_populates="ratings")

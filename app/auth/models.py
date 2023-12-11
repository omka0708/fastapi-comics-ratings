from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from app.database import Base
from app.comics.models import Rating


class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    ratings = relationship("Rating", back_populates="user")

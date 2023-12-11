from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import update, select

from app.auth.models import User
from app.comics import models, schemas


async def create_rating(rating: schemas.RatingCreate, user: User, db: AsyncSession):
    comic = await db.get(models.Comic, rating.comic_id)
    if not comic:
        raise HTTPException(status_code=400, detail={
            "status": "error",
            "msg": f"Comic {rating.comic_id} doesn't exist."
        })

    rating_db = await db.execute(select(models.Rating).filter_by(comic_id=rating.comic_id, user_id=user.id))
    rating_obj = models.Rating(**rating.model_dump(), user_id=user.id)

    rating_exists = rating_db.scalar()
    if rating_exists:
        await db.execute(
            update(models.Rating).filter_by(comic_id=rating.comic_id, user_id=user.id).values(VALUE=rating.VALUE))
    else:
        db.add(rating_obj)

    ratings_db = await db.execute(select(models.Rating).filter_by(comic_id=rating.comic_id))
    ratings_db_array = ratings_db.scalars().all()

    sum_values = 0
    for obj in ratings_db_array:
        sum_values += obj.VALUE
    avg = sum_values / len(ratings_db_array)

    await db.execute(update(models.Comic).filter_by(id=rating.comic_id).values(rating=avg))
    await db.commit()
    return rating_obj


async def get_rating(comic_id: int, db: AsyncSession):
    comic = await db.get(models.Comic, comic_id)
    if not comic:
        raise HTTPException(status_code=400, detail={
            "status": "error",
            "msg": f"Comic {comic_id} doesn't exist."
        })
    return comic.rating


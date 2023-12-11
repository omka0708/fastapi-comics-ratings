from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app import crud
from app.auth.auth import auth_backend, fastapi_users, current_user
from app.auth.models import User
from app.auth.schemas import UserRead, UserCreate
from app.comics.schemas import RatingCreate
from app.database import get_async_session

app = FastAPI()

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/api/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/api/auth",
    tags=["auth"],
)


@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url='/docs')


@app.post("/api/ratings", tags=["comics"])
async def create_rating(rating: RatingCreate, user: User = Depends(current_user),
                        session: AsyncSession = Depends(get_async_session)):
    return await crud.create_rating(rating, user, session)


@app.get("/api/comics/{comic_id}/rating", tags=["comics"])
async def get_rating(comic_id: int, session: AsyncSession = Depends(get_async_session)):
    return await crud.get_rating(comic_id, session)

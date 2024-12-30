"""
Swagger и OPENAPI.
"""

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.future import select
from pydantic import BaseModel
from typing import List
import uvicorn
# ASGI - Uvicorn
# WSGI - Gunicorn


DATABASE_URL = "sqlite+aiosqlite:////database/test.db"
# DATABASE_URL = "sqlite+aiosqlite:///./database/test.db"
engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()


# Database Dependency
async def get_db():
    db = AsyncSessionLocal()
    try:
        yield db  # Возвращаем объект подключения
    finally:
        await db.close()  # Закрываем сессию асинхронно


# User Model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    age = Column(Integer, nullable=True)


# Pydantic Schema
class UserSchema(BaseModel):
    id: int
    name: str
    email: str
    age: int

    class Config:
        orm_mode = True


class UserCreateSchema(BaseModel):
    name: str
    email: str
    age: int


class UserUpdateSchema(BaseModel):
    name: str = None
    email: str = None
    age: int = None


# App Instance
app = FastAPI()


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# CRUD Handlers
@app.get("/users/", response_model=List[UserSchema])
async def get_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User))
    print(result)
    print(type(result))
    users = result.scalars()
    print(users)
    print(type(users))
    users = users.all()
    print(users)
    print(type(users))
    return users


@app.get("/users/{user_id}", response_model=UserSchema)
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).filter(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        # abort(404, description="ПОШЕЛ ВОН!!!")
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.post("/users/", response_model=UserSchema)
async def create_user(user: UserCreateSchema, db: AsyncSession = Depends(get_db)):
    # print(user)  # name='Name' email='email1' age=33
    # print(user.dict())  # {'name': 'Name', 'email': 'email1', 'age': 33}
    new_user = User(**user.dict())  # User(name = 'Name', 'email' = 'email1', 'age' = 33)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user


@app.patch("/users/{user_id}", response_model=UserSchema)
async def update_user(
    user_id: int, user_data: UserUpdateSchema,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(User).filter(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    update_data = user_data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(user, key, value)

    await db.commit()
    await db.refresh(user)
    return user


@app.delete("/users/{user_id}", response_model=dict)
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).filter(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    await db.delete(user)
    await db.commit()
    return {"message": "User deleted successfully"}


if __name__ == "__main__":
    uvicorn.run("__main__:app", host="0.0.0.0", port=8000, reload=True)

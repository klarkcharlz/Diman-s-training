"""
Типы авторизации и аутентификации.
- JWT и OAUTH 2.0.
- middleware.
"""

from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.future import select
from pydantic import BaseModel
from typing import List
import uvicorn
import jwt
import datetime
from passlib.context import CryptContext
from starlette.middleware.base import BaseHTTPMiddleware


# Конфигурация JWT
SECRET_KEY = "your_secret_key"  # Замените на свой секретный ключ
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# ASGI - Uvicorn
DATABASE_URL = "sqlite+aiosqlite:///./database/test.db"
engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()

# OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Временное хранилище пользователей
fake_users_db = {
    "testuser": {
        "username": "testuser",
        "full_name": "Test User",
        "email": "testuser@example.com",
        "hashed_password": "$2b$12$3/frJNCJAZNTztyFH34tT.JhUopbwsrceJZJ7DWeKSLAU8exHeIj.",
        # "fakehashedpassword", смотри функцию create_hashed_password
    }
}

# Настройка хеширования паролей
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Database Dependency
async def get_db():
    db = AsyncSessionLocal()
    try:
        yield db
    finally:
        await db.close()


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


# Для токена
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str


# App Instance
app = FastAPI()


# Функция middleware для логирования IP-адресов
async def log_ip_middleware(request: Request, call_next):
    # Получаем IP-адрес клиента
    client_ip = request.client.host
    print(f"IP-адрес клиента: {client_ip}")
    # Продолжаем обработку запроса
    response = await call_next(request)
    return response


app.add_middleware(BaseHTTPMiddleware, dispatch=log_ip_middleware)


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# Функции для работы с JWT
def create_access_token(data: dict, expires_delta: datetime.timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.datetime.utcnow() + expires_delta
    else:
        expire = datetime.datetime.utcnow() + datetime.timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except jwt.PyJWTError:
        raise credentials_exception
    user = fake_users_db.get(token_data.username)
    if user is None:
        raise credentials_exception
    return user


def create_hashed_password(password):
    return pwd_context.hash(password)


# Проверка пароля
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


# Хеширование пароля
def get_password_hash(password):
    return pwd_context.hash(password)


class RegistrationUserSchema(BaseModel):
    username: str
    password: str


@app.post("/reg")
async def reg(user_data: RegistrationUserSchema, db: AsyncSession = Depends(get_db)):
    print(user_data)  # username='Diman' password='123'
    # делаем какие то проверки что такой пользователь уже не зарегестрирован
    # высчитываем хеш пароля
    hash_password = get_password_hash(user_data.password)
    # print(hash_password)  # $2b$12$TUCVKQpMHcdXP.V/3ZKqNOdveahwnsRuOPix6aqSx/o03Dt0zssWu
    # сохраняем в бд пользователя, в столбце пароль храним хеш пароля
    return hash_password


@app.post("/auth", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    print(form_data.username)
    print(form_data.password)
    user = fake_users_db.get(form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}


# CRUD Handlers
@app.get("/users/", response_model=List[UserSchema])
async def get_users(current_user: dict = Depends(get_current_user),
                    db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User))
    users = result.scalars().all()
    return users


@app.get("/users/{user_id}", response_model=UserSchema)
async def get_user(user_id: int, current_user: dict = Depends(get_current_user),
                   db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).filter(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User  not found")
    return user


@app.post("/users/", response_model=UserSchema)
async def create_user(user: UserCreateSchema, current_user: dict = Depends(get_current_user),
                      db: AsyncSession = Depends(get_db)):
    new_user = User(**user.dict())
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user


@app.patch("/users/{user_id}", response_model=UserSchema)
async def update_user(
        user_id: int, user_data: UserUpdateSchema,
        current_user: dict = Depends(get_current_user), db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(User).filter(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User  not found")

    update_data = user_data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(user, key, value)

    await db.commit()
    await db.refresh(user)
    return user


@app.delete("/users/{user_id}", response_model=dict)
async def delete_user(user_id: int, current_user: dict = Depends(get_current_user),
                      db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).filter(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User  not found")

    await db.delete(user)
    await db.commit()
    return {"message": "User  deleted successfully"}


if __name__ == "__main__":
    uvicorn.run("__main__:app", host="0.0.0.0", port=8000, reload=True)

import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from faker import Faker
from app import Base, User


# Database configuration
DATABASE_URL = "sqlite+aiosqlite:///./database/test.db"
engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

# Faker instance
fake = Faker()


async def create_fake_users():
    async with AsyncSessionLocal() as session:
        for _ in range(10):
            fake_user = User(
                name=fake.name(),
                email=fake.email(),
                age=fake.random_int(min=18, max=99)
            )
            session.add(fake_user)
        await session.commit()


async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    await create_fake_users()
    print("10 fake users created successfully!")


if __name__ == "__main__":
    asyncio.run(main())

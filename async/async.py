from typing import List

from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker, Session

SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://postgres:1234@db-sync-async-test:5432/postgres"

engine_async = create_async_engine(SQLALCHEMY_DATABASE_URL)

async_session = sessionmaker(
    engine_async,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
    class_=AsyncSession,
)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)


class UserBase(BaseModel):
    class Config:
        orm_mode = True

    email: str


async def get_users(session: Session):
    query = select(User)
    result = await session.execute(query)
    return result.scalars().all()


app = FastAPI()


@app.on_event("startup")
async def on_startup():
    async with engine_async.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/users", response_model=List[UserBase])
async def read_users():
    async with async_session() as session:
        async with session.begin():
            users = await get_users(session)
            return users


@app.get("/users/insert-data-to-test")
async def insert_data_to_test():
    async with async_session() as session:
        async with session.begin():
            user = User()
            user.email = "teste@teste.com.br"
            session.add(user)
            session.commit()

import asyncio
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, join
from sqlalchemy.sql import select
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from faker import Faker

fake = Faker('uk-Ua')

engine = create_async_engine('sqlite+aiosqlite:///:memory:', echo=True)
DBSession = async_sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True)
    fullname = Column('fullname', String)


class Address(Base):
    __tablename__ = 'address'
    id = Column('id', Integer, primary_key=True)
    email = Column('email', String(50), nullable=False)
    user_id = Column('user_id', Integer, ForeignKey('users.id'))
    user = relationship('User')         # Цю властивість треба вказувати для орм. Тут буде об'єкт класу Юзер


async def init():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def main():
    await init()
    async with DBSession() as session:
        async with session.begin():                # щоб коміти автоматично робились
            n_user = User(fullname='Jack Jones')
            session.add(n_user)
            n_address = Address(email=fake.email(), user=n_user)
            session.add(n_address)
            # await session.commit()

            for _ in range(10):
                n_user = User(fullname=fake.name())
                session.add(n_user)
                n_address = Address(email=fake.email(), user=n_user)
                session.add(n_address)
            # await session.commit()

        users = await session.execute(select(User))
        colums = ["id", "fullname"]
        result = [dict(zip(colums, (row.id, row.fullname))) for row in users.scalars()]
        print(result)
        # for row in users.scalars():
        #     print(row.id, row.fullname)

        addresses = await session.execute(select(Address).join(User))
        for row in addresses.scalars():
            print(row.id, row.email, row.user_id, row.user.fullname)


if __name__ == '__main__':
    asyncio.run(main())
# from sqlalchemy import Column, Integer, String
# from my_program.src.database.db import Base, engine
#
#
# class Build(Base):
#     __tablename__ = "homes"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(200))
#     level = Column(Integer, unique=True, index=True)
#     gold = Column(Integer, nullable=True)
#     tree = Column(Integer, nullable=True)
#     stone = Column(Integer, nullable=True)
#     corn = Column(Integer, nullable=True)
#     iron = Column(Integer, nullable=True)
#     crystals = Column(String(200), nullable=True)
#
#
# Base.metadata.create_all(bind=engine)


from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Build(Base):
    __tablename__ = "builds"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    level: Mapped[int] = mapped_column(Integer, nullable=False)
    gold: Mapped[int] = mapped_column(Integer, nullable=True)
    tree: Mapped[int] = mapped_column(Integer, nullable=True)
    stone: Mapped[int] = mapped_column(Integer, nullable=True)
    corn: Mapped[int] = mapped_column(Integer, nullable=True)
    iron: Mapped[int] = mapped_column(Integer, nullable=True)
    crystals: Mapped[str] = mapped_column(String(200), nullable=True)


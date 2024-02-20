from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref
from db import Base, engine


class Build(Base):
    __tablename__ = "homes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200))
    level = Column(Integer, unique=True, index=True)
    gold = Column(Integer, nullable=True)
    tree = Column(Integer, nullable=True)
    stone = Column(Integer, nullable=True)
    corn = Column(Integer, nullable=True)
    iron = Column(Integer, nullable=True)
    crystals = Column(String(200), nullable=True)


Base.metadata.create_all(bind=engine)
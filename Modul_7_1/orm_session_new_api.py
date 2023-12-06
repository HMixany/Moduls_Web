from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, join
from sqlalchemy.orm import sessionmaker, relationship, declarative_base, Mapped, mapped_column

from faker import Faker

fake = Faker('uk-Ua')

engine = create_engine('sqlite:///:memory:', echo=True)
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    fullname: Mapped[str] = mapped_column(String(120))


class Address(Base):
    __tablename__ = 'address'
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(50), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    user: Mapped["User"] = relationship('User')      # Цю властивість треба вказувати для орм. Тут буде об'єкт класу Юзер


Base.metadata.create_all(engine)


if __name__ == '__main__':
    n_user = User(fullname='Jack Jones')
    session.add(n_user)
    n_address = Address(email=fake.email(), user=n_user)
    session.add(n_address)
    session.commit()

    for _ in range(10):
        n_user = User(fullname=fake.name())
        session.add(n_user)
        n_address = Address(email=fake.email(), user=n_user)
        session.add(n_address)
        session.commit()

    users = session.query(User).all()
    for row in users:
        print(row.id, row.fullname)

    user = session.query(User).filter_by(id=1).first()
    print(user.fullname)

    session.close()
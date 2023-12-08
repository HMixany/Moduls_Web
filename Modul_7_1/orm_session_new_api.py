from sqlalchemy import Integer, String, ForeignKey, create_engine, select, and_, or_, not_, desc, func
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
    n_address = Address(email=fake.email(), user=n_user)
    session.add(n_address)
    n_address = Address(email=fake.email(), user=n_user)
    session.add(n_address)
    session.commit()

    for _ in range(10):
        n_user = User(fullname=fake.name())
        session.add(n_user)
        n_address = Address(email=fake.email(), user=n_user)
        session.add(n_address)
    session.commit()

    statement = select(User.id, User.fullname)
    for row in session.execute(statement):
        print(row)

    statement = select(Address.id, Address.email, User.fullname).join(Address.user)
    for row in session.execute(statement):
        print(row)

    print('===============All and scalar============================================')
    statement = select(User)
    colums = ["id", "fullname"]
    result = [dict(zip(colums, (row.id, row.fullname))) for row in session.execute(statement).scalars()]
    print(result)

    # без скаляра
    result = [dict(zip(colums, (row.User.id, row.User.fullname))) for row in session.execute(statement).all()]
    print(result)
    print('=============================================================================')

    statement = select(Address)
    colums = ["id", "email", "fullname"]
    result = [dict(zip(colums, (row.id, row.email, row.user.fullname))) for row in session.execute(statement).scalars()]
    print(result)

    # statement = select(Address)
    # for row in session.execute(statement).scalars():
    #     print(row.id, row.email, row.user.fullname)

    statement = select(User).where(User.fullname == 'Jack Jones')
    r = session.execute(statement).scalar_one_or_none()
    if r:                                # пеевірка чи є такий, якщо немає, то буде None і прінт не спрацює
        print(r.fullname)

    statement = select(User.id, User.fullname)
    for row in session.execute(statement):
        print(row)

    statement = select(User).where(User.fullname.like('Наталія%')) # знайти всіх юзерів з Наталія
    r = session.execute(statement).scalars()
    for row in r:
        print(row.fullname)

    # знайти всіх юзерів з Наталія і щоб id дорівнював 1
    statement = select(User).where(User.fullname.like('Наталія%')).where(User.id == 1)
    r = session.execute(statement).scalars()
    for row in r:
        print(row.fullname)

    # Можно інакше, за допомогою метода and_
    statement = select(User).where(and_(User.fullname.like('Наталія%'), User.id == 1))
    r = session.execute(statement).scalars()
    for row in r:
        print(row.fullname)

    # OR
    statement = select(User).where(or_(User.fullname.like('Наталія%'), User.id == 1))
    r = session.execute(statement).scalars()
    print('==========================================')
    for row in r:
        print(row.fullname)

    # ORDER BY за замовчуванням сортує по id
    statement = select(User).order_by(User.fullname)
    colums = ["id", "fullname"]
    result = [dict(zip(colums, (row.id, row.fullname))) for row in session.execute(statement).scalars()]
    print(result)

    # ORDER BY навпаки(за допомогою desc)
    statement = select(User).order_by(desc(User.fullname))
    colums = ["id", "fullname"]
    result = [dict(zip(colums, (row.id, row.fullname))) for row in session.execute(statement).scalars()]
    print(result)

    # func (агрегації)
    # знайдемо кількість адрес у юзерів
    statement = (
        select(User.fullname, func.count(Address.id))
        .join(Address)
        .group_by(User.fullname)
    )
    result = session.execute(statement).all()
    print(result)
    for fullname, count in result:
        print(f'{fullname}: {count}')

    # mappings
    result = session.execute(statement).mappings()
    for row in result:
        print(row)

    session.close()
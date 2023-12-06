from sqlalchemy import Table, Column, Integer, String, ForeignKey, MetaData, create_engine, join
from sqlalchemy.sql import select
from faker import Faker

fake = Faker('uk-Ua')

metadata = MetaData()

engine = create_engine('sqlite:///:memory:', echo=True)

users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('fullname', String),
              )

addresses = Table('addresses', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('email', String, nullable=False),
                  Column('user_id', Integer, ForeignKey('users.id'))
                  )

metadata.create_all(engine)


if __name__ == '__main__':
    with engine.connect() as conn:
        ins_user = users.insert().values(fullname='Jack Jones')
        result = conn.execute(ins_user)
        jones_id = result.lastrowid
        print(jones_id)

        for _ in range(10):
            ins_user = users.insert().values(fullname=fake.name())
            result = conn.execute(ins_user)
            print(result.lastrowid)

        result = conn.execute(select(users))
        for row in result:
            # print(row)
            ins_address = addresses.insert().values(email=fake.email(), user_id=row[0])
            conn.execute(ins_address)

        result = conn.execute(select(addresses))
        for row in result:
            print(row)

        sql_select = select(addresses.c.email, users.c.fullname).join(users)
        result = conn.execute(sql_select)
        for row in result:
            print(row)



# ins_address = addresses.insert().values(email='jones@mail.com', user_id=1)
# ins = users.insert().values(name='jack', fullname='Jack Jones')
# print(str(ins))  # INSERT INTO users (name, fullname) VALUES (:name, :fullname)
# conn = engine.connect()
# result = conn.execute(ins)
# conn.close()

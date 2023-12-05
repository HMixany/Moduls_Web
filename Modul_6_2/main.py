import logging
from random import randint

from faker import Faker
import psycopg2
from psycopg2 import DatabaseError


fake = Faker('uk-Ua')

conn = psycopg2.connect(host='localhost', database='test', user='postgres', password='321456')
cur = conn.cursor()

# Додавання груп
for _ in range(3):
    cur.execute('INSERT INTO groups (name) VALUES (%s)', (fake.word(),))

# Додавання викладачів
for _ in range(3):
    cur.execute('INSERT INTO teachers (full_name) VALUES (%s)', (fake.name(),))

# Додавання предметів із вказівкою викладача
for teacher_id in range(1, 4):
    for _ in range(2):
        cur.execute('INSERT INTO subjects (name, teacher_id) VALUES (%s, %s)', (fake.word(), teacher_id))

# додавання студентів і оцінок
for group_id in range(1, 4):
    for _ in range(10):
        cur.execute('INSERT INTO students (full_name, group_id) VALUES (%s, %s) RETURNING id', (fake.name(), group_id))
        student_id = cur.fetchone()[0]
        for subject_id in range(1, 7):
            for _ in range(3):
                cur.execute('INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (%s, %s, %s, %s)',
                            (student_id, subject_id, randint(0, 100), fake.date_this_decade()))

try:
    # збереження змін
    conn.commit()
except DatabaseError as err:
    logging.error(err)
    conn.rollback()
finally:
    # закриття підключення
    cur.close()
    conn.close()
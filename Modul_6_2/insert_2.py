import sqlite3
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# Підключення до бази даних (замініть на свої параметри)
connection = sqlite3.connect('your_database.db')
cursor = connection.cursor()

# Створення груп
groups = [('Group A',), ('Group B',), ('Group C',)]
cursor.executemany('INSERT INTO Groups (GroupName) VALUES (?)', groups)
connection.commit()

# Створення викладачів
professors = [(fake.first_name(), fake.last_name()) for _ in range(5)]
cursor.executemany('INSERT INTO Professors (FirstName, LastName) VALUES (?, ?)', professors)
connection.commit()

# Створення предметів
subjects = [(fake.word(), random.choice(professors)[0]) for _ in range(8)]
cursor.executemany('INSERT INTO Subjects (SubjectName, ProfessorID) VALUES (?, (SELECT ProfessorID FROM Professors WHERE FirstName = ?))', subjects)
connection.commit()

# Створення студентів
students = [(fake.first_name(), fake.last_name(), random.randint(1, 3)) for _ in range(50)]
cursor.executemany('INSERT INTO Students (FirstName, LastName, GroupID) VALUES (?, ?, ?)', students)
connection.commit()

# Створення оцінок для кожного студента з усіх предметів
for student_id in range(1, 51):
    for subject_id in range(1, 9):
        grades = [(student_id, subject_id, random.randint(60, 100), fake.date_between(start_date='-30d', end_date='today')) for _ in range(20)]
        cursor.executemany('INSERT INTO Grades (StudentID, SubjectID, Grade, DateReceived) VALUES (?, ?, ?, ?)', grades)
        connection.commit()

# Закриття з'єднання
connection.close()

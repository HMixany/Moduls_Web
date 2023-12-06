import sqlite3
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# Підключення до бази даних (замініть на свої параметри)
connection = sqlite3.connect('your_database.db')
cursor = connection.cursor()

# Видалення старих таблиць, якщо вони існують
cursor.execute('DROP TABLE IF EXISTS Grades;')
cursor.execute('DROP TABLE IF EXISTS Students;')
cursor.execute('DROP TABLE IF EXISTS Subjects;')
cursor.execute('DROP TABLE IF EXISTS Professors;')
cursor.execute('DROP TABLE IF EXISTS Groups;')
connection.commit()

# Створення груп
groups = [('Group A',), ('Group B',), ('Group C',)]
cursor.executemany('CREATE TABLE Groups (GroupID INT PRIMARY KEY, GroupName VARCHAR(50));', groups)
cursor.executemany('INSERT INTO Groups (GroupName) VALUES (?);', groups)
connection.commit()

# Створення викладачів
professors = [(fake.first_name(), fake.last_name()) for _ in range(5)]
cursor.executemany('CREATE TABLE Professors (ProfessorID INT PRIMARY KEY, FirstName VARCHAR(50), LastName VARCHAR(50));', professors)
cursor.executemany('INSERT INTO Professors (FirstName, LastName) VALUES (?, ?);', professors)
connection.commit()

# Створення предметів
subjects = [(fake.word(), random.choice(professors)[0]) for _ in range(8)]
cursor.executemany('CREATE TABLE Subjects (SubjectID INT PRIMARY KEY, SubjectName VARCHAR(50), ProfessorID INT, FOREIGN KEY (ProfessorID) REFERENCES Professors(ProfessorID));', subjects)
cursor.executemany('INSERT INTO Subjects (SubjectName, ProfessorID) VALUES (?, (SELECT ProfessorID FROM Professors WHERE FirstName = ?));', subjects)
connection.commit()

# Створення студентів
students = [(fake.first_name(), fake.last_name(), random.randint(1, 3)) for _ in range(50)]
cursor.executemany('CREATE TABLE Students (StudentID INT PRIMARY KEY, FirstName VARCHAR(50), LastName VARCHAR(50), GroupID INT, FOREIGN KEY (GroupID) REFERENCES Groups(GroupID));', students)
cursor.executemany('INSERT INTO Students (FirstName, LastName, GroupID) VALUES (?, ?, ?);', students)
connection.commit()

# Створення оцінок
for student_id in range(1, 51):
    for subject_id in range(1, 9):
        grades = [(student_id, subject_id, random.randint(60, 100), fake.date_between(start_date='-30d', end_date='today')) for _ in range(20)]
        cursor.executemany('CREATE TABLE Grades (GradeID INT PRIMARY KEY, StudentID INT, SubjectID INT, Grade INT, DateReceived DATE, FOREIGN KEY (StudentID) REFERENCES Students(StudentID), FOREIGN KEY (SubjectID) REFERENCES Subjects(SubjectID));', grades)
        cursor.executemany('INSERT INTO Grades (StudentID, SubjectID, Grade, DateReceived) VALUES (?, ?, ?, ?);', grades)
        connection.commit()

# Закриття з'єднання
connection.close()

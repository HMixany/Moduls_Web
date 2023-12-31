from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from sqlalchemy.ext.hybrid import hybrid_property

Base = declarative_base()


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(120), nullable=False)
    last_name = Column(String(120), nullable=False)

    email = Column(String(100))
    phone = Column('cell_phone', String(100))
    address = Column(String(100))
    start_work = Column(Date, nullable=False)
    student = relationship('Student', secondary='teachers_to_students', back_populates='teacher')

    # створемо гібридне(віртуальне) поле
    @hybrid_property
    def fullname(self):
        return self.first_name + ' ' + self.last_name


class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(20), nullable=False)


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(120), nullable=False)
    last_name = Column(String(120), nullable=False)

    email = Column(String(100))
    phone = Column('cell_phone', String(100))
    address = Column(String(100))

    group_id = Column('group_id', ForeignKey('groups_id', ondelete='CASCADE'))
    group = relationship('Group', backref='students')

    teacher = relationship('Teacher', secondary='teachers_to_students', back_populates='student')

    # створемо гібридне(віртуальне) поле
    @hybrid_property
    def fullname(self):
        return self.first_name + ' ' + self.last_name


class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    teacher_id = Column('teacher_id', ForeignKey('teachers_id', ondelete='CASCADE'))
    teacher = relationship('Teacher', backref='subjects')


class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    grade = Column(Integer, nullable=False)
    date_of = Column('date_of', Date, nullable=True)
    student_id = Column('student_id', ForeignKey('students_id', ondelete='CASCADE'))
    subject_id = Column('subject_id', ForeignKey('subjects_id', ondelete='CASCADE'))
    student = relationship('Student', backref='grade')
    subject = relationship('Subject', backref='grade')
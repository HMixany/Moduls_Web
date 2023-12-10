from sqlalchemy import and_, or_
from sqlalchemy.orm import joinedload, subqueryload
from datetime import datetime

from Modul_7_2.conf.db import session
from Modul_7_2.conf.models import Teacher, Student, TeacherStudent, Contact


def get_student_join():
    students = session.query(Student).join(Student.teacher).all()
    for s in students:
        # columns = ['id', 'first_name', 'last_name', 'teachers']
        # r = [dict(zip(columns, (s.id, s.first_name, s.last_name, [(t.id, t.first_name, t.last_name) for t in s.teacher])))]
        # print(r)
        # з використанням гібридних полей
        columns = ['id', 'fullname', 'teachers']
        r = [dict(zip(columns, (s.id, s.fullname, [(t.id, t.fullname) for t in s.teacher])))]
        print(r)


# запити без join, за допомогою joinedload або subqueryload
def get_students():
    students = session.query(Student).options(joinedload(Student.teacher)).all()
    # students = session.query(Student).options(joinedload(Student.teacher)).limit(5).offset(3).all() # offset -зміщення
    # students = session.query(Student).options(subqueryload(Student.teacher)).all()
    for s in students:
        # columns = ['id', 'first_name', 'last_name', 'teachers']
        # r = [dict(zip(columns, (s.id, s.first_name, s.last_name, [(t.id, t.first_name, t.last_name) for t in s.teacher])))]
        # print(r)
        # з використанням гібридних полей
        columns = ['id', 'fullname', 'teachers']
        r = [dict(zip(columns, (s.id, s.fullname, [(t.id, t.fullname) for t in s.teacher])))]
        print(r)


def get_teachers():
    teachers = session.query(Teacher).options(joinedload(Teacher.student, innerjoin=True)).all()
    # innerjoin=True робе щоб вчителя які не закріплені за студентами не виводились
    for t in teachers:
        columns = ['id', 'fullname', 'students']
        r = [dict(zip(columns, (t.id, t.fullname, [(s.id, s.fullname) for s in t.student])))]
        print(r)


def get_teachers_outerjoin():
    teachers = session.query(Teacher).outerjoin(Teacher.student).all()
    # innerjoin=True робе щоб вчителя які не закріплені за студентами не виводились
    for t in teachers:
        columns = ['id', 'fullname', 'students']
        r = [dict(zip(columns, (t.id, t.fullname, [(s.id, s.fullname) for s in t.student])))]
        print(r)


# filter і where одне і теж
def get_teachers_by_data():
    teachers = session.query(Teacher).options(joinedload(Teacher.student, innerjoin=True)) \
        .filter(and_(Teacher.start_work >= datetime(year=2020, month=1, day=1),
                     Teacher.start_work <= datetime(year=2021, month=12, day=31))).all()

    # teachers = session.query(Teacher).options(joinedload(Teacher.student, innerjoin=True)) \
    #     .filter(or_(Teacher.start_work <= datetime(year=2020, month=1, day=1),
    #                 Teacher.start_work >= datetime(year=2021, month=12, day=31))).all()

    for t in teachers:
        columns = ['id', 'fullname', 'start_work', 'students']
        r = [dict(zip(columns, (t.id, t.fullname, t.start_work, [(s.id, s.fullname) for s in t.student])))]
        print(r)


def get_students_with_contacts():
    students = session.query(Student).join(Student.contacts).all()
    for s in students:
        columns = ['id', 'fullname', 'contacts']
        r = [dict(zip(columns, (s.id, s.fullname, [(c.id, c.fullname) for c in s.contacts])))]
        print(r)


def get_info():
    students = (session.query(Student.id, Student.fullname, Teacher.fullname.label("teacher_fullname"),
                              Contact.fullname.label("contact_fullname")).select_from(Student).join(TeacherStudent)
                .join(Teacher).join(Student.contacts).all())
    for s in students:
        columns = ['id', 'fullname', 'teachers', 'contacts']
        r = [dict(zip(columns, (s.id, s.fullname, s.teacher_fullname, s.contact_fullname)))]
        print(r)


def update_student(s_id, teachers: list[Teacher]):
    student = session.query(Student).filter_by(id=s_id).first()
    student.teacher = teachers
    session.commit()
    return student


def remove_student(s_id):
    student = session.query(Student).filter_by(id=s_id).first()
    session.delete(student)
    session.commit()


if __name__ == '__main__':
    # get_student_join()
    # get_students()
    # get_teachers()
    # get_teachers_by_data()
    # get_students_with_contacts()
    # get_info()
    # ===================================================================
    t = session.query(Teacher).filter(Teacher.id.in_([1, 2, 3])).all()
    st = update_student(8, t)
    print(st)

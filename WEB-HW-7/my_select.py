from sqlalchemy import func, desc
from models import Student, Group, Teacher, Subject, Grade
from connect_db import session

def select_1(session):
    return session.query(Student.student_name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .join(Grade).join(Group).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()

def select_2(session, subject_name):
    return session.query(Student.student_name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .join(Grade).join(Subject).filter(Subject.subject_name == subject_name)\
        .group_by(Student.id).order_by(desc('avg_grade')).first()

def select_3(session, subject_name):
    return session.query(Group.group_name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .join(Student, Group.students).join(Grade, Student.grades).join(Subject)\
        .filter(Subject.subject_name == subject_name).group_by(Group.id, Group.group_name).all()

def select_4(session):
    return session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')).scalar()

def select_5(session, teacher_name):
    return session.query(Subject.subject_name).join(Teacher).filter(Teacher.teacher_name == teacher_name).all()

def select_6(session, group_name):
    return session.query(Student.student_name).join(Group).filter(Group.group_name == group_name).all()

def select_7(session, group_name, subject_name):
    return session.query(Student.student_name)\
        .join(Group, Student.group_id == Group.id)\
        .join(Grade, Student.id == Grade.student_id)\
        .join(Subject, Grade.subject_id == Subject.id)\
        .filter(Group.group_name == group_name, Subject.subject_name == subject_name).all()

def select_8(session, teacher_name):
    return session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .join(Subject).join(Teacher).filter(Teacher.teacher_name == teacher_name).scalar()

def select_9(session, student_name):
    return session.query(Subject.subject_name).join(Grade).join(Student)\
        .filter(Student.student_name == student_name).all()

def select_10(session, student_name, teacher_name):
    return session.query(Subject.subject_name).join(Grade).join(Student).join(Teacher)\
        .filter(Student.student_name == student_name, Teacher.teacher_name == teacher_name).all()

def select_11(session, teacher_name, student_name):
    return session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .join(Subject).join(Teacher).join(Student)\
        .filter(Teacher.teacher_name == teacher_name, Student.student_name == student_name).scalar()

def select_12(session, group_name, subject_name):
    return session.query(Grade)\
        .join(Subject, Grade.subject_id == Subject.id)\
        .join(Student, Grade.student_id == Student.id)\
        .join(Group, Student.group_id == Group.id)\
        .filter(Group.group_name == group_name)\
        .filter(Subject.subject_name == subject_name)\
        .order_by(Grade.date_received.desc())\
        .first()


if __name__ == '__main__':
    # Execute all select functions and print their results
    
    result_1 = select_1(session)
    print("Result 1:", result_1)
    
    result_2 = select_2(session, "English Language")
    print("Result 2:", result_2)
    
    result_3 = select_3(session, "Python Development")
    print("Result 3:", result_3)
    
    result_4 = select_4(session)
    print("Result 4:", result_4)
    
    result_5 = select_5(session, "Professor Thompson")
    print("Result 5:", result_5)
    
    result_6 = select_6(session, "FL-45")
    print("Result 6:", result_6)
    
    result_7 = select_7(session, "FL-46", "Python Development")
    print("Result 7:", result_7)
    
    result_8 = select_8(session, "Professor Miller")
    print("Result 8:", result_8)
    
    result_9 = select_9(session, "Mary Curtis")
    print("Result 9:", result_9)
    
    result_10 = select_10(session, "David Garcia", "Professor Reyes")
    print("Result 10:", result_10)

    result_11 = select_11(session, "Professor Thompson", "Mary Curtis")
    print("Result 11:", result_11)
    
    result_12 = select_12(session, "FL-46", "Python Development")
    print("Result 12: id:", result_12.id, ", grade:", result_12.grade, ", date_received:", result_12.date_received)

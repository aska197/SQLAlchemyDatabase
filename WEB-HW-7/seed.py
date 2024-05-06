from faker import Faker
from random import choice, randint
from datetime import datetime, timedelta
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student, Group, Teacher, Subject, Grade
from sqlalchemy.exc import IntegrityError
from sqlalchemy import func

NUMBER_STUDENTS = 30
NUMBER_GROUPS = 3
NUMBER_SUBJECTS = 7  # 7 relevant subjects
NUMBER_TEACHERS = randint(3, 5)
MAX_GRADES_PER_STUDENT = 20

def generate_fake_data(number_students, number_groups, number_subjects, number_teachers):
    fake = Faker()

    # Generate student names
    students = [fake.name() for _ in range(number_students)]

    # Generate group names like FL-45, FL-46, FL-47
    groups = [f"FL-{i}" for i in range(45, 45 + number_groups)]

    # Generate relevant subjects
    subjects = ["Intermediate Data Science", "English Language", "Translation Theory",
                "Introduction to Databases", "Python Development", 
                "Systems of Automated Translation", "Text Analysis"]

    # Generate teacher names with 'Professor' or 'Doctor' in them
    teachers =  [f"Professor {fake.last_name()}" for _ in range(number_teachers)]

    return students, groups, teachers, subjects

def generate_grades(students, subjects):
    fake = Faker()
    grades = []
    for student in students:
        for _ in range(randint(1, MAX_GRADES_PER_STUDENT)):
            grade = fake.random_int(min=50, max=100)  # Random grade between 50 and 100
            subject = choice(subjects)
            date_received = fake.date_between(start_date='-1y', end_date='today')  # Generate a random date within the past year
            grades.append(Grade(student_id=student.id, subject_id=subject.id, grade=grade, date_received=date_received))
    return grades

def seed_database():
    students, groups, teachers, subjects = generate_fake_data(NUMBER_STUDENTS, NUMBER_GROUPS, NUMBER_SUBJECTS, NUMBER_TEACHERS)

    engine = create_engine('postgresql://postgres:mysecretreira@localhost:5432/postgres')
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Insert groups
        for group_name in groups:
            session.add(Group(group_name=group_name))

        # Insert students
        for student_name in students:
            group = session.query(Group).order_by(func.random()).first()
            session.add(Student(student_name=student_name, group_id=group.id))

        # Insert teachers
        for teacher_name in teachers:
            session.add(Teacher(teacher_name=teacher_name))

        # Insert subjects
        for subject_name in subjects:
            teacher = session.query(Teacher).order_by(func.random()).first()
            session.add(Subject(subject_name=subject_name, teacher_id=teacher.id))

        session.commit()

        # Generate grades and insert them
        students = session.query(Student).all()
        subjects = session.query(Subject).all()
        grades = generate_grades(students, subjects)
        session.add_all(grades)
        session.commit()

        print("Database seeded successfully!")
    except IntegrityError as e:
        print(f"Error seeding database: {e}")
        session.rollback()
    finally:
        session.close()

if __name__ == "__main__":
    seed_database()


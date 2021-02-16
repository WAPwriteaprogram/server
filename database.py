from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.BigInteger, primary_key=True)
    username = db.Column(db.String(128), primary_key=True)
    email = db.Column(db.String(254), unique=True, nullable=False)
    password_hashed = db.Column(db.String(), nullable = False)
    '''
    Privilages:
    0 - student
    1 - instructor
    2 - admin
    '''
    privilege = db.Column(db.SmallInteger, nullable=False)
    courses_joined = db.Column(db.ARRAY(db.Integer))

class Session(db.Model):
    __tablename__ = "sessions"

    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(255), unique=True)
    data = db.Column(db.LargeBinary)
    expiry = db.Column(db.DateTime)


# from sqlalchemy import ARRAY, BigInteger, Boolean, Column, DateTime, Float, ForeignKey, Integer, LargeBinary, MetaData, SmallInteger, String, Table, Text, UniqueConstraint
# from sqlalchemy.schema import FetchedValue
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.dialects.postgresql import TEXT, BIGINT, VARCHAR, DOUBLE_PRECISION, INTEGER
# from sqlalchemy import create_engine

# Base = declarative_base()
# metadata = Base.metadata



# t_assignment = Table(
#     'assignment', metadata,
#     Column('assignment_code', Integer, nullable=False),
#     Column('course_code', ForeignKey('courses.course_code'), nullable=False),
#     Column('assignment_name', String(128), nullable=False),
#     Column('due', DateTime),
#     Column('public', Boolean, nullable=False),
#     Column('starts', DateTime),
#     Column('questions', ARRAY(BIGINT()), nullable=False),
#     UniqueConstraint('assignment_code', 'course_code')
# )



# class Course(Base):
#     __tablename__ = 'courses'

#     id = Column(Integer, nullable=False, server_default=FetchedValue())
#     course_code = Column(String(10), primary_key=True)
#     course_name = Column(String(128), nullable=False)
#     studets = Column(ARRAY(VARCHAR(length=128)))
#     instructors = Column(ARRAY(VARCHAR(length=128)))
#     assignments = Column(ARRAY(INTEGER()))



# class ProblemPool(Base):
#     __tablename__ = 'problem_pool'

#     problem_id = Column(BigInteger, primary_key=True, server_default=FetchedValue())
#     question = Column(Text, nullable=False)
#     tags = Column(ARRAY(TEXT()))
#     solution = Column(Text)
#     output_stream = Column(String(255), nullable=False)
#     input = Column(ARRAY(TEXT()))
#     arguments = Column(ARRAY(TEXT()))
#     expected_output = Column(ARRAY(TEXT()), nullable=False)



# t_question = Table(
#     'question', metadata,
#     Column('assignment_code', Integer, nullable=False),
#     Column('course_code', ForeignKey('courses.course_code'), nullable=False),
#     Column('problem_id', ForeignKey('problem_pool.problem_id'), nullable=False),
#     Column('max_marks', Float(53), nullable=False),
#     Column('test_case_weightage', ARRAY(DOUBLE_PRECISION(precision=53)), nullable=False),
#     Column('test_case_public', Boolean, nullable=False),
#     UniqueConstraint('assignment_code', 'course_code', 'problem_id')
# )



# class Session(Base):
#     __tablename__ = 'sessions'

#     id = Column(Integer, primary_key=True)
#     session_id = Column(String(255), unique=True)
#     data = Column(LargeBinary)
#     expiry = Column(DateTime)



# t_user_submission = Table(
#     'user_submission', metadata,
#     Column('problem_id', ForeignKey('problem_pool.problem_id'), nullable=False),
#     Column('assignment_code', Integer, nullable=False),
#     Column('course_code', ForeignKey('courses.course_code'), nullable=False),
#     Column('user_username', ForeignKey('users.username'), nullable=False),
#     Column('user_solution', Text),
#     Column('test_case_satisfied', Boolean, nullable=False),
#     Column('marks', Float(53), nullable=False),
#     Column('user_query', Text),
#     UniqueConstraint('problem_id', 'assignment_code', 'user_username', 'course_code')
# )



# class User(Base):
#     __tablename__ = 'users'

#     user_id = Column(BigInteger, nullable=False, server_default=FetchedValue())
#     username = Column(String(128), primary_key=True)
#     email = Column(String(254), nullable=False, unique=True)
#     password_hashed = Column(Text, nullable=False)
#     privilege = Column(SmallInteger, nullable=False)
#     courses_joined = Column(ARRAY(INTEGER()))
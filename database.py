from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    username = db.Column(db.String(128), primary_key=True)
    email = db.Column(db.String(254), nullable=False, unique=True)
    password_hashed = db.Column(db.Text, nullable=False)
    privilege = db.Column(db.SmallInteger, nullable=False)
    section = db.Column(db.String(10))
    batch = db.Column(db.String(10))

class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    course_code = db.Column(db.String(10), primary_key=True)
    course_name = db.Column(db.String(128), nullable=False)
    
    
    
class CourseUsers(db.Model):
    __tablename__ = 'courses_users'
    __table_args__ = (db.UniqueConstraint('course_code', 'users'),)
    
    course_code = db.Column(db.String(10), db.ForeignKey('courses.course_code'), nullable=False)
    users = db.Column(db.String(128), db.ForeignKey('users.username'), nullable=False)
    fake_column = db.Column(db.Boolean, primary_key=True)

class Assignment(db.Model):
    __tablename__ = 'assignment'
    __table_args__ = (db.UniqueConstraint('assignment_code', 'course_code'),)
    
    assignment_code = db.Column(db.Integer, nullable=False)
    course_code = db.Column(db.String(10), db.ForeignKey('courses.course_code'), nullable=False)
    assignment_name = db.Column(db.String(128), nullable=False)
    public = db.Column(db.Boolean, nullable=False)
    starts = db.Column(db.DateTime)
    due = db.Column(db.DateTime)
    fake_column = db.Column(db.Boolean, primary_key=True)



# class ProblemPool(db.Model):
#     __tablename__ = 'problem_pool'

#     problem_id = db.Column(db.BigInteger, primary_key=True, server_default=db.FetchedValue())
#     question = db.Column(db.Text, nullable=False)
#     solution = db.Column(db.Text)
#     output_stream = db.Column(db.String(255), nullable=False)
#     creator = db.Column(db.ForeignKey('users.username'), nullable=False)

#     user = db.relationship('User', primaryjoin='ProblemPool.creator == User.username', backref='problem_pools')


# class Question(ProblemPool):
#     __tablename__ = 'question'

#     question_id = db.Column(db.ForeignKey('problem_pool.problem_id'), primary_key=True)
#     assignment_code = db.Column(db.Integer, nullable=False)
#     course_code = db.Column(db.ForeignKey('courses.course_code'), nullable=False)
#     problem_id = db.Column(db.ForeignKey('problem_pool.problem_id'), nullable=False)
#     max_marks = db.Column(db.Float(53), nullable=False)

#     course = db.relationship('Course', primaryjoin='Question.course_code == Course.course_code', backref='questions')
#     problem = db.relationship('ProblemPool', primaryjoin='Question.problem_id == ProblemPool.problem_id', backref='questions')



# t_problem_pool_tags = db.Table(
#     'problem_pool_tags',
#     db.Column('problem_id', db.ForeignKey('problem_pool.problem_id'), nullable=False),
#     db.Column('tags', db.Text, nullable=False),
#     db.UniqueConstraint('problem_id', 'tags')
# )



# t_problem_pool_test_case = db.Table(
#     'problem_pool_test_case',
#     db.Column('test_case_id', db.Integer, nullable=False),
#     db.Column('problem_id', db.ForeignKey('problem_pool.problem_id'), nullable=False),
#     db.Column('expected_output', db.Text, nullable=False),
#     db.Column('input', db.Text),
#     db.Column('arguments', db.Text),
#     db.UniqueConstraint('problem_id', 'test_case_id')
# )



# t_question_test_case = db.Table(
#     'question_test_case',
#     db.Column('test_case_id', db.Integer, nullable=False),
#     db.Column('question_id', db.ForeignKey('question.question_id'), nullable=False),
#     db.Column('weightage', db.Float(53), nullable=False),
#     db.Column('public', db.Boolean, nullable=False),
#     db.UniqueConstraint('question_id', 'test_case_id')
# )



# t_user_submission = db.Table(
#     'user_submission',
#     db.Column('question_id', db.ForeignKey('question.question_id'), nullable=False),
#     db.Column('user_username', db.ForeignKey('users.username'), nullable=False),
#     db.Column('user_solution', db.Text),
#     db.Column('marks', db.Float(53), nullable=False),
#     db.Column('user_query', db.Text),
#     db.UniqueConstraint('question_id', 'user_username')
# )



# t_user_submission_test_case_satisfied = db.Table(
#     'user_submission_test_case_satisfied',
#     db.Column('test_case_id', db.Integer, nullable=False),
#     db.Column('question_id', db.ForeignKey('question.question_id'), nullable=False),
#     db.Column('user_username', db.ForeignKey('users.username'), nullable=False),
#     db.Column('test_case_satisfied', db.Boolean, nullable=False),
#     db.UniqueConstraint('question_id', 'user_username', 'test_case_id')
# )



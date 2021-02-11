from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.BigInteger)
    username = db.Column(db.String(128), primary_key=True)
    email = db.Column(db.String(254), unique=True, nullable=False)
    password_hashed = db.Column(db.String(), nullable = False)
    '''
    Privilages:
    0 - student
    1 - instructor
    2 - admin
    '''
    privilage = db.Column(db.SmallInteger, nullable=False)
    courses_joined = db.Column(db.ARRAY(db.Integer))



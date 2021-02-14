from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy import ARRAY, BigInteger, Boolean, Column, DateTime, Float, ForeignKey, Integer, LargeBinary, SmallInteger, String, Table, Text, UniqueConstraint, text

#from sqlalchemy.ext.declarative import declarative_base
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
    privilage = db.Column(db.SmallInteger, nullable=False)
    courses_joined = db.Column(db.ARRAY(db.Integer))

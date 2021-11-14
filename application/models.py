from os import name
from sqlalchemy.orm import backref

from wtforms.validators import Email
from application import db

#Creating a database with two tables that has one to many relationships
#In this case, a student can have many posts and a post can only have one particular student

class Students(db.Model):
   id= db.Column(db.Integer, primary_key=True)
   name= db.Column(db.String(50), nullable=False)
   email= db.Column(db.String(50), nullable=False, unique=True)
#Student can have many posts
posts = db.relationship('Posts', backref='poster')

class Posts(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    course= db.Column(db.String(50))
    content= db.Column(db.text)
    #Foreign key to Link students (refer to primary key of the student)
    poster_id = db.Column(db.Integer, db.ForeignKey('students.id')) 
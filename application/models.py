from application import db

#Creating a database with two tables that has one to many relationships
class Student(db.Model):
    stud_id = db.Column(db.Integer, primary_key = True)
    FullName = db.Column(db.String(80))
    phone=db.Column(db.Integer)
    email=db.Column(db.String(50))
    courses= db.relationship('Course', backref='learner')

class Course(db.Model):
    course_id= db.Column(db.Integer, primary_key =True)
    name=db.Column(db.String(50))
    learner_id= db.Column(db.Integer, db.ForeignKey('student.id'))
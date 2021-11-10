from application import db

class Student(db.Model):
    studno = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    date = db.Column(db.Integer)
    course = db.Column(db.String(50))
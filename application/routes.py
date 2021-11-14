from flask import request, redirect, render_template
from application import app, db
from application.forms import AddStud, UpdateStud
from application.models import Student

#This is the index route where we are going to query on all 
@app.route('/')
def index():
    first_name = "David"
    return render_template("index.html", first_name=first_name)

@app.route('/student/add', methods= ['GET', 'POST'])
def add_student():
    return render_template("add_students.html")


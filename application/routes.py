from flask import request, redirect, render_template
from application import app, db
from application.forms import AddStud, UpdateStud
from application.models import Student

@app.route('/')
def home():
    studs = Student.query.all()
    return render_template('index.html', records=studs)

@app.route('/editRecord/<int:studno>', methods=['GET', 'POST'])
def editRecordForm(studno):
    form = UpdateStud()
    stud = Student.query.filter_by(studno=studno).first()
    if request.method == 'POST':
        # Fetch form data
        stud.FullName = form.stud_name.data
        stud.phone = form.phone.data
        stud.email = form.email.data
        stud.course= form.course.data
        db.session.commit()
        return redirect("/")
    return render_template('Edit.html', form=form)

#Filtering students
@app.route("/filterrecords",methods=["POST"])
def filterrecords():
    if request.form["course"]=="all":
        return redirect("/")
    else:
        data = Student.query.filter_by(course=request.form["course"]).all()
        return render_template("index.html",records=data)

#Adding new students
@app.route("/saveRecord",methods=["GET","POST"])
def saveRecord():
    form = AddStud()
    if request.method == 'POST':
        name=form.stud_name.data
        course=form.course.data
        phone= form.phone.data
        email= form.email.data
        newstud = Student(name=name, course=course, phone=phone, email=email)
        db.session.add(newstud)
        db.session.commit()
        return redirect("/")
    return render_template("input.html", form=form)

@app.route("/Studentdetails/<int:studno>")
def Studentdetails(studno):
	data = Student.query.filter_by(studno=studno).first()
	return render_template("Studentdetails.html",record=data)

#Deleting Students

@app.route("/deleteStudent/<int:studno>")
def deleteStudent(studno):
    stud = Student.query.filter_by(studno=studno).first()
    db.session.delete(stud)
    db.session.commit()
    return redirect("/")
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SelectField, SubmitField

#Adding and updating forms
class AddStud(FlaskForm):
    stud_name = StringField("FullName")
    phone = StringField("Phone")
    email = StringField("Email")
    course = SelectField('Course', choices=[('Devops', 'Devops'), ('Software', 'Software Engineering'), ('Networking', 'Networking engineering'), ('Database', 'Database')])
    submit = SubmitField('Add Student')

class UpdateStud(FlaskForm):
    stud_name = StringField("FullName")
    phone = StringField("Phone")
    email = StringField("Email")
    course = SelectField('Course', choices=[('Devops', 'Devops'), ('Software', 'Software Engineering'), ('Networking', 'Networking engineering'), ('Database', 'Database')])
    submit = SubmitField('Update Student')
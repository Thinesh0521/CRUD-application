from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SelectField, SubmitField
#blah2222
class AddStud(FlaskForm):
    stud_name = StringField("Name")
    date= IntegerField("Date")
    course = SelectField('Course', choices=[('Devops', 'Devops'), ('Software', 'Software Engineering'), ('Networking', 'Networking engineering'), ('Database', 'Database')])
    submit = SubmitField('Add Student')

class UpdateStud(FlaskForm):
    stud_name = StringField("Name")
    date = IntegerField("Date")
    course = SelectField('Course', choices=[('Devops', 'Devops'), ('Software', 'Software Engineering'), ('Networking', 'Networking engineering'), ('Database', 'Database')])
    submit = SubmitField('Update Student')
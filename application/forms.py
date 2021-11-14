from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

#Adding Student credentials
class StudentForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    submit = SubmitField("Submit")

class UpdateStud(FlaskForm):
    stud_name = StringField("FullName")
    phone = StringField("Phone")
    email = StringField("Email")
    course = SelectField('Course', choices=[('Devops', 'Devops'), ('Software', 'Software Engineering'), ('Networking', 'Networking engineering'), ('Database', 'Database')])
    submit = SubmitField('Update Student')
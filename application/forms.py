from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SelectField, SubmitField
from wtforms.validators import DataRequired
from wtforms.widgets.core import TextArea

#Create Post Form
class PostForm(FlaskForm):
    course = StringField("Course", validators=[DataRequired()])
    content = StringField("Content", validators=[DataRequired()], widget= TextArea)
    submit = SubmitField("Submit")


#Adding Student credentials
class StudentForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    submit = SubmitField("Submit")


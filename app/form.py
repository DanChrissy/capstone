from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, Form, SelectField
from wtforms.validators import DataRequired 

class Search(FlaskForm):
    firstname = StringField ('First Name', validators = [DataRequired()])
    lastname = StringField ('Last Name' , validators = [DataRequired()])

class Login(FlaskForm):
    username = StringField ('Username', validators = [DataRequired()])
    password = StringField ('Password' , validators = [DataRequired()])

class TutorForm(FlaskForm):
    ID= StringField ('ID number', validators = [DataRequired()])
    firstname= StringField ('First Name', validators = [DataRequired()])
    lastname = StringField ('Last Name' , validators = [DataRequired()])
    email= StringField ('Email Address' , validators = [DataRequired()])
    areaOfStudy= StringField ('Area of Study' , validators = [DataRequired()])
    preference= StringField (' Course Preference' , validators = [DataRequired()])
    
class StudentForm(FlaskForm):
    ID= StringField ('ID number', validators = [DataRequired()])
    firstname= StringField ('First Name', validators = [DataRequired()])
    lastname = StringField ('Last Name' , validators = [DataRequired()])
    email= StringField ('Email Adress' , validators = [DataRequired()])
    telephone= StringField ('Telephone number')
    yearStudy=StringField('Year of Study')
    major= StringField ('Degree Major' , validators = [DataRequired()])
    helpWith= StringField ('Which course you need help with' , validators = [DataRequired()])
    state= StringField ('State' , validators = [DataRequired()])
    
class AdminView(FlaskForm):   
    ID= StringField ('ID number', validators = [DataRequired()])
    firstname= StringField ('First Name', validators = [DataRequired()])
    
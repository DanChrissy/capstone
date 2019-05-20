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
    option1 = SelectField('Course Options 1', choices=[('COMP2201', 'Analysis of Algorithms'), ('COMP2201', 'Discrete Mathematics'), ('COMP2190','Net-Centric Computing'), ('INFO2100', 'Math and Statistics for IT'), ('INFO2110','Data Structures for IT')])
    option2 = SelectField('Course Options 2', choices=[('COMP3191', 'Principles of Computer Networks'), ('COMP3161', 'Database Management Systems'), ('COMP3702','Theory of Computations'), ('INFO3155', 'Information Assurance and Security for IT'), ('INFO3180','Dynamic Web Develoopment 2')])
    days = SelectField('Tutor Days', choices=[('Mon','Monday'),('Tues','Tuesday'),('Wed','Wednesday'),('Thur','Thursday'),('Fri','Friday'),('Sat','Saturday')])
     
class StudentForm(FlaskForm):
    ID= StringField ('ID number', validators = [DataRequired()])
    firstname= StringField ('First Name', validators = [DataRequired()])
    lastname = StringField ('Last Name' , validators = [DataRequired()])
    email= StringField ('Email Adress' , validators = [DataRequired()])
    option1 = SelectField('Course Options 1', choices=[('COMP2201', 'Analysis of Algorithms'), ('COMP2201', 'Discrete Mathematics'), ('COMP2190','Net-Centric Computing'), ('INFO2100', 'Math and Statistics for IT'), ('INFO2110','Data Structures for IT')])
    option2 = SelectField('Course Options 2', choices=[('COMP3191', 'Principles of Computer Networks'), ('COMP3161', 'Database Management Systems'), ('COMP3702','Theory of Computations'), ('INFO3155', 'Information Assurance and Security for IT'), ('INFO3180','Dynamic Web Develoopment 2')])
    days = SelectField('Tutor Days', choices=[('Mon','Monday'),('Tues','Tuesday'),('Wed','Wednesday'),('Thur','Thursday'),('Fri','Friday'),('Sat','Saturday')])
   
    
class AdminView(FlaskForm):   
    ID= StringField ('ID number', validators = [DataRequired()])
    firstname= StringField ('First Name', validators = [DataRequired()])
    